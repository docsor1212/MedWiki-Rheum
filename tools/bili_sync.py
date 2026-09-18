#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""B站视频自动同步：发现UP主新视频 → 重建首页最新视频版块 → 自动上线
用法: python3 tools/bili_sync.py [--apply]   (缺省dry-run，--apply才写盘和push)
"""
import json, os, re, sys, time, hashlib, http.cookiejar, urllib.request, urllib.parse

MID = '432233902'
ROOT = os.path.expanduser('~/MedWiki-Rheum')
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
MAX_CARDS = 6
REC_BVID = 'BV15h9YBSEp3'   # 强烈推荐标记（AF论文工具箱）
APPLY = '--apply' in sys.argv

MIXIN_TAB = [46,47,18,2,53,8,23,32,15,50,10,31,58,3,45,35,27,43,5,49,33,9,42,19,29,28,14,39,12,38,41,13,37,48,7,16,24,55,40,61,26,17,0,1,60,51,30,4,22,25,54,21,56,59,6,63,57,62,11,36,20,34,44,52]

cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-Agent', UA), ('Referer', 'https://space.bilibili.com/'), ('Origin', 'https://space.bilibili.com')]

def http(url):
    return opener.open(url, timeout=25).read()

def wbi_sign(params):
    nav = json.loads(http('https://api.bilibili.com/x/web-interface/nav').decode('utf-8'))
    w = nav['data']['wbi_img']
    img = w['img_url'].rsplit('/', 1)[1].split('.')[0]
    sub = w['sub_url'].rsplit('/', 1)[1].split('.')[0]
    raw = img + sub
    key = ''.join(raw[i] for i in MIXIN_TAB)[:32]
    params = dict(params)
    params['wts'] = int(time.time())
    qs = urllib.parse.urlencode(sorted(params.items()))
    w_rid = hashlib.md5((qs + key).encode('utf-8')).hexdigest()
    return qs + '&w_rid=' + w_rid

def esc(s):
    return (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;'))

def series_tag(title):
    t = title
    if '免疫前沿' in t or '免疫代谢' in t: return '免疫前沿深读'
    if 'IEI' in t or '免疫出生错误' in t: return 'IEI病种深读'
    if 'Skill' in t or '论文' in t or '图表' in t: return '论文工具箱'
    return 'DoctorQ'

def dur_fmt(v):
    if isinstance(v, str) and ':' in v: return v
    sec = int(v)
    return '{}:{:02d}'.format(sec // 60, sec % 60)

# 1) 预热cookie（获取buvid3，降低风控概率）
try: http('https://www.bilibili.com/')
except Exception as e: print('warmup warn:', str(e)[:80])

# 2) wbi签名拉取UP主最新视频
qs = wbi_sign({'mid': MID, 'ps': str(MAX_CARDS), 'pn': '1', 'order': 'pubdate'})
data = json.loads(http('https://api.bilibili.com/x/space/wbi/arc/search?' + qs).decode('utf-8'))
if data.get('code') != 0:
    print('API错误 code=%s msg=%s —— 本轮不动页面' % (data.get('code'), data.get('message', '')))
    sys.exit(1)
vlist = data['data']['list']['vlist']
print('API返回视频数:', len(vlist))

# 3) 封面下载（增量，已有跳过）
def cover_ok(name):
    p = os.path.join(ROOT, 'assets', name)
    return os.path.exists(p) and os.path.getsize(p) > 5000

# 4) 生成卡片
cards = []
new_covers = 0
for v in vlist[:MAX_CARDS]:
    bvid = v['bvid']
    cover_name = 'video-{}.jpg'.format(bvid)
    if not cover_ok(cover_name):
        try:
            raw = http(v['pic'].replace('http://', 'https://'))
            open(os.path.join(ROOT, 'assets', cover_name), 'wb').write(raw)
            new_covers += 1
            print('cover new:', cover_name, len(raw), 'bytes')
        except Exception as e:
            print('cover fail', bvid, str(e)[:60])
            continue
    rec = ' rec' if bvid == REC_BVID else ''
    chip = '<span class="chip-rec">荐</span>' if bvid == REC_BVID else ''
    tag = esc(series_tag(v['title']))
    cards.append(
        '          <a class="vcard rv{rec}" href="https://www.bilibili.com/video/{bv}/" target="_blank" rel="noopener">\n'
        '            <div class="vbody">\n'
        '              <div class="vcover">\n'
        '                <img src="{prefix}assets/{cover}" alt="{alt}">\n'
        '                <span class="play"><i><svg viewBox="0 0 24 24" fill="#fff"><path d="M8 5v14l11-7z"/></svg></i></span>\n'
        '                <span class="dur">{dur}</span>\n'
        '              </div>\n'
        '              <div class="vinfo">\n'
        '                <span class="vtag">B站 · {tag}</span>\n'
        '                <div class="vtitle">{title}</div>\n'
        '                <p class="vdesc">{desc}</p>\n'
        '              </div>\n'
        '            </div>\n'
        '          </a>'.format(rec=rec, bv=bvid, cover=cover_name, dur=esc(dur_fmt(v['length'])),
                              tag=tag, title=esc(v['title']), chip=chip,
                              desc=esc((v.get('description') or '').replace('\n', ' ')[:90] or tag)))

# 5) 替换index.html标记区
p = os.path.join(ROOT, 'index.html')
s = open(p, encoding='utf-8').read()
m = re.search(r'<!--VIDEOS:START-->.*?<!--VIDEOS:END-->', s, flags=re.S)
if not m:
    print('未找到VIDEOS标记——先跑一次标记安装'); sys.exit(1)
new_region = '<!--VIDEOS:START-->\n' + '\n'.join(cards) + '\n          <!--VIDEOS:END-->'
if s[m.start():m.end()] == new_region:
    print('内容无变化，不提交'); sys.exit(0)
s = s[:m.start()] + new_region + s[m.end():]

if APPLY:
    open(p, 'w', encoding='utf-8', newline='\n').write(s)
    os.chdir(ROOT)
    os.system('git add -A index.html assets && git -c user.name="docsor1212" -c user.email="docsor1212@users.noreply.github.com" commit -m "sync: B站视频版块自动更新" && git push origin master')
    print('APPLIED + pushed')
else:
    print('DRY-RUN：内容有变化（{}张卡），加--apply写盘'.format(len(cards)))
