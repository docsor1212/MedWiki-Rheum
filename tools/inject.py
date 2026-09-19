# -*- coding: utf-8 -*-
"""
MedWiki-Rheum 内容页骨架批量注入 inject.py (Phase 2)
====================================================
分型: skip / minimal(evidence,docs) / tools / standard(cases,drugs,templates,topics)
幂等: <html data-mw-rebuilt="1">
用法: python3 inject.py --dry <rel paths...> | python3 inject.py <rel paths...> | python3 inject.py --all [--dry]
"""
import io, os, re, sys
from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V_THEMES, V_MEDWIKI, V_CONTENT, V_SHARE = 6, 26, 4, 6

SKIP_FILES = {'index.html', 'index_legacy.html', 'clear-cache.html'}
SKIP_PATHS = {'topics/KD.html', 'evidence/ev_TETRA_01.html'}
SKIP_DIRS = ('_templates', 'clinical_tools', 'screenshots', 'medtts', '.git')

EMOJI_RE = re.compile(
    '[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF\u2B00-\u2BFF\uFE0F\u200D\u2705\u274C\u27A1]+')

NAV_HTML = ('<nav class="mnav" aria-label="站点导航">\n'
            '  <div class="mnav-in">\n'
            '  <a class="home" href="../index.html">⌂ MedWiki 首页</a>\n'
            '  <a class="mlink" href="../index.html#topics">疾病专题</a>\n'
            '  <a class="mlink" href="../index.html#drugs">药物手册</a>\n'
            '  <a class="mlink" href="../index.html#tools">临床工具</a>\n'
            '  <a class="mlink" href="../index.html#cases">病例学习</a>\n'
            '  <a class="mlink" href="../docs/pmid_audit_report.html">引用验证</a>\n'
            '  <a class="mlink" href="../index.html#skills">Skills</a>\n'
            '  <a class="mlink" href="https://space.bilibili.com/432233902" target="_blank" rel="noopener">B站</a>\n'
            '  <a class="mlink" href="https://github.com/docsor1212" target="_blank" rel="noopener">GitHub</a>\n'
            '  <span class="brand">MedWiki-Rheum</span>\n'
            '  </div>\n'
            '</nav>')

CATS = {
    'topics':    ('疾病专题', '#topics'),
    'drugs':     ('药物手册', '#drugs'),
    'tools':     ('临床工具', '#tools'),
    'cases':     ('病例学习', '#cases'),
    'evidence':  ('循证证据', '#evidence'),
    'templates': ('医患沟通', '#templates'),
    'docs':      ('参考文档', None),
}

THEME_DOTS = ('<div class="theme-dots" role="group" aria-label="主题切换">\n'
              '  <span class="lbl">主题</span>\n'
              '  <button data-set-theme="glm" aria-pressed="true"><i class="dot glm"></i>GLM</button>\n'
              '  <button data-set-theme="honey" aria-pressed="false"><i class="dot honey"></i>Honey</button>\n'
              '  <button data-set-theme="teal" aria-pressed="false"><i class="dot teal"></i>Teal</button>\n'
              '</div>')

THEME_JS = ('<script>\n'
            '(function(){\n'
            '  var THEMES = ["glm","honey","teal"];\n'
            '  var saved = null;\n'
            '  try { saved = localStorage.getItem("mw-theme"); } catch(e){}\n'
            '  if (THEMES.indexOf(saved) >= 0) document.documentElement.setAttribute("data-theme", saved);\n'
            '  var current = document.documentElement.getAttribute("data-theme") || "glm";\n'
            '  var btns = document.querySelectorAll("[data-set-theme]");\n'
            '  function paint(){ btns.forEach(function(b){ b.setAttribute("aria-pressed", String(b.getAttribute("data-set-theme") === current)); }); }\n'
            '  btns.forEach(function(b){\n'
            '    b.addEventListener("click", function(){\n'
            '      current = b.getAttribute("data-set-theme");\n'
            '      document.documentElement.setAttribute("data-theme", current);\n'
            '      try { localStorage.setItem("mw-theme", current); } catch(e){}\n'
            '      paint();\n'
            '    });\n'
            '  });\n'
            '  paint();\n'
            '})();\n'
            '</script>')

MFOOT = ('<footer class="mfoot">\n'
         '  <div class="band thin"></div>\n'
         '  <div class="inner">\n'
         '    <span class="word">MedWiki-Rheum</span>\n'
         '    <div class="flinks">\n'
         '      <a href="https://github.com/docsor1212/MedWiki-Rheum" target="_blank" rel="noopener">GitHub 开源仓库 · 欢迎勘误</a>\n'
         '      <a href="https://space.bilibili.com/432233902" target="_blank" rel="noopener">B站 · DoctorQ 免疫前沿</a>\n'
         '      <a href="https://skillhub.cn/user/user_481397b5" target="_blank" rel="noopener">SkillHub · 我们的6个Skills</a>\n'
         '    </div>\n'
         '    儿童风湿免疫临床知识库 · 作者 Doctor Q\n'
         '  </div>\n'
         '</footer>')

BRIDGE_CSS = ('<style data-mw-bridge="1">\n'
              '/* inject.py 桥接层: 旧fixed导航补偿 + 内容卡对齐 + .sh节标题统一(双斜杠) */\n'
              'body{padding-top:0 !important;}\n'
              '.cw-wrap ~ .wrap{max-width:1040px;margin:14px auto 0;}\n'
              '.wrap .sh, .wrap .sh.red, .wrap .sh.green, .wrap .sh.yellow, .wrap .sh.blue{\n'
              '  background:transparent;color:var(--accent-ink,#22303F);padding:0 0 6px;border-radius:0;\n'
              '  border-bottom:2px solid var(--accent-soft,#DCE8F4);box-shadow:none;margin:22px 0 10px;\n'
              '  font-size:15px;font-weight:800;display:flex;align-items:center;gap:9px;flex-wrap:wrap;}\n'
              '.wrap .sh::before{content:\'\';width:5px;height:15px;background:var(--accent,#1B4F8A);\n'
              '  transform:skewX(-18deg);box-shadow:8px 0 0 var(--accent,#1B4F8A);flex:none;}\n'
              '.wrap table{font-size:13px;}\n'
              '.wrap th{background:var(--accent-soft,#DCE8F4);color:var(--accent-ink,#22303F);\n'
              '  border-bottom:2px solid var(--accent,#1B4F8A);padding:7px 10px;}\n'
              '.wrap td{padding:6px 10px;border-bottom:1px solid var(--border,#DDE5EC);line-height:1.65;}\n'
              '.wrap tr:hover td{background:var(--surface-2,#F5F6F8);}\n'
              '.wrap .t-a,.wrap .score-box{background:var(--accent-soft,#DCE8F4);color:var(--accent-ink,#22303F);}\n'
              '</style>')


def strip_emoji(s):
    return EMOJI_RE.sub('', s).strip()


def mount(html_frag, container, index=0):
    """把HTML片段的顶层节点按顺序insert进container的index位置。"""
    frag = BeautifulSoup(html_frag, 'html.parser')
    nodes = list(frag.children)
    for off, node in enumerate(nodes):
        container.insert(index + off, node)
    return len(nodes)


def mount_before(html_frag, target):
    frag = BeautifulSoup(html_frag, 'html.parser')
    for node in list(frag.children):
        target.insert_before(node)


def clean_title(t):
    t = strip_emoji(t or '')
    for suf in (' — MedWiki-Rheum', ' — 儿童风湿免疫临床知识库', ' - MedWiki-Rheum'):
        t = t.replace(suf, '')
    return t.strip(' ：:-')


def detect_mode(rel):
    d = rel.replace(os.sep, '/')
    if d in SKIP_PATHS or d in SKIP_FILES:  # 只按完整相对路径跳过根页面, 不误伤 cases/index.html 等目录索引
        return 'skip'
    if d.startswith(SKIP_DIRS) or '/'.join(d.split('/')[:1]) in SKIP_DIRS:
        return 'skip'
    if d.startswith('evidence/'):
        return 'bare'      # 成品文章自带品牌hero, 只做合规修复不动结构
    if d.startswith('docs/'):
        return 'minimal'   # 工具型文档页: 注入mnav+面包屑
    if d.startswith('tools/'):
        return 'tools'
    if d.startswith(('cases/', 'drugs/', 'templates/', 'topics/')):
        return 'standard'
    return 'skip'


def crumb_html(rel, title):
    dirn = os.path.dirname(rel)
    label, anchor = CATS.get(dirn, (None, None))
    parts = ['<a href="../index.html">首页</a><span class="sep">‹</span>']
    if label:
        href = '../index.html' + anchor if anchor else '../index.html'
        parts.append(f'<a href="{href}">{label}</a><span class="sep">‹</span>')
    parts.append(f'<span class="here">{title}</span>')
    return '<div class="cw-crumb">' + ''.join(parts) + '</div>'


def get_text(el):
    return strip_emoji(el.get_text(' ', strip=True)) if el else ''


def build_cwhead(header, title):
    h1, sub, meta = title, '', ''
    if header:
        t = get_text(header.find('h1'))
        if t:
            h1 = t
        sub = get_text(header.find(class_='sub'))
        meta = get_text(header.find(class_='meta'))
    inner = f'<div>\n      <h1>{h1}</h1>'
    if sub:
        inner += f'\n      <div class="cw-sub">{sub}</div>'
    inner += '\n    </div>'
    if meta:
        inner += f'\n    <div class="cw-meta">{meta}</div>'
    return f'  <div class="cw-head">\n    {inner}\n  </div>'


def process(path, rel, mode, dry):
    with io.open(path, encoding='utf-8-sig') as f:
        raw = f.read()
    if 'data-mw-rebuilt="1"' in raw:
        return (rel, 'skip-rebuilt', '')
    soup = BeautifulSoup(raw, 'html.parser')
    html, head, body = soup.find('html'), soup.find('head'), soup.find('body')
    if not (html and head and body):
        return (rel, 'skip-malformed', '')
    acts = []

    # ---- html属性 ----
    html['data-mw-rebuilt'] = '1'
    if not html.get('data-theme'):
        html['data-theme'] = 'glm'
    dsu = html.get('data-share-url', '')
    if 'docsor1212.github.io' in dsu:
        html['data-share-url'] = dsu.replace('https://docsor1212.github.io/MedWiki-Rheum', 'https://docsor.cn')
        acts.append('share-url修正')
    elif not dsu:
        html['data-share-url'] = 'https://docsor.cn/' + rel
        acts.append('share-url新增')

    # ---- head: 去tailwind, 补theme-color, CSS按序注入 ----
    for sc in head.find_all('script', src=re.compile('cdn\\.tailwindcss\\.com')):
        sc.decompose()
        acts.append('-tailwind')
    if not head.find('meta', attrs={'name': 'theme-color'}):
        mt = soup.new_tag('meta')
        mt.attrs = {'name': 'theme-color', 'content': '#12365F'}
        head.append(mt)
        acts.append('+theme-color')

    styles = head.find_all('style')
    first_style, last_style = (styles[0] if styles else None), (styles[-1] if styles else None)
    for ln in head.find_all('link', href=re.compile('assets/(themes|medwiki|content)\\.css')):
        ln.decompose()
    if mode != 'bare':  # 成品文章不注入骨架CSS
        pre = soup.new_tag('link'); pre.attrs = {'rel': 'stylesheet', 'href': f'../assets/content.css?v={V_CONTENT}'}
        pre2 = soup.new_tag('link'); pre2.attrs = {'rel': 'stylesheet', 'href': f'../assets/medwiki.css?v={V_MEDWIKI}'}
        post = soup.new_tag('link'); post.attrs = {'rel': 'stylesheet', 'href': f'../assets/themes.css?v={V_THEMES}'}
        if first_style is not None:
            first_style.insert_before(pre)
            first_style.insert_before(pre2)
            last_style.insert_after(post)
        else:
            head.extend([pre, pre2, post])
        acts.append('+css×3')

    # ---- body通用: 去旧导航 / SW注册 ----
    for nb in body.find_all(class_='nav-bar'):
        nb.decompose()
        acts.append('-nav-bar')
    for sc in body.find_all('script'):
        if sc.string and 'serviceWorker' in sc.string:
            sc.decompose()
            acts.append('-sw-reg')

    title = clean_title(soup.title.get_text()) if soup.title else os.path.basename(rel)

    wrap = body.find('div', class_='wrap', recursive=False) or body.find('div', class_='wrap')
    if mode in ('standard', 'tools') and wrap is None:
        mode = 'minimal'

    if mode == 'bare':
        # 成品文章: 不注入mnav/面包屑/骨架CSS/bridge/主题切换——只做合规修复
        if 'AI 辅助整理' not in soup.get_text():
            disc = ('<div style="max-width:1100px;margin:26px auto 0;padding:12px 20px 30px;font-size:12px;'
                    'color:#5A6B7C;line-height:1.8;border-top:1px solid #DDE5EC;"><b>免责声明</b>　'
                    '本页内容为临床参考资料，由 AI 辅助整理、Cite-holmes 及人工审校，仅供专业交流，'
                    '不构成对具体患者的诊疗建议；临床决策请结合患者实际情况并遵循所在医疗机构规范。'
                    '所引指南与文献均标注来源与核验状态，引用请以原文为准。</div>')
            mount(disc, body, len(body.contents))
            acts.append('+disc')
    elif mode == 'standard':
        header = wrap.find('div', class_='header')
        if header:
            # judge阻断3: wrap正文已有免责时不搬header免责(防双免责重复)
            wrap_has_disc = False
            for ch in wrap.find_all('div', recursive=True):
                if ch.parent is wrap and ch is not header and '免责' in ch.get_text():
                    wrap_has_disc = True
                    break
            if not wrap_has_disc:
                # 只搬"自身直接子级含免责标注"的div——不碰结构性包裹div(其内含h1/sub)
                def is_disc_div(d):
                    if '免责' in ' '.join(t for t in d.find_all(string=True, recursive=False)):
                        return True
                    return any('免责' in ch.get_text() for ch in d.find_all(['b', 'strong'], recursive=False))
                for d in header.find_all('div'):
                    if is_disc_div(d) and not any(is_disc_div(p) and p != d for p in d.parents if p.name == 'div'):
                        wrap.insert(0, d.extract())
                        acts.append('免责出header')
        cwhead = build_cwhead(header, title)
        if header:
            header.decompose()
            acts.append('header→cw-head')
        shs = wrap.find_all(class_='sh')
        links = []
        for i, sh in enumerate(shs, 1):
            if not sh.get('id'):
                sh['id'] = f'sec-{i}'
            txt = strip_emoji(sh.get_text(' ', strip=True))
            if txt:
                links.append(f'<a href="#{sh["id"]}">{txt}</a>')
        mount(NAV_HTML + '\n<div class="cw-wrap">\n' + crumb_html(rel, title) + '\n' + cwhead + '\n</div>', body, 0)
        acts.append('+mnav+cw-head')
        if links:
            mount('<div class="cw-anchor">' + ''.join(links) + '</div>', wrap, 0)
            acts.append(f'+anchor×{len(links)}')
        for sh in shs:  # .sh文本去emoji
            for ns in list(sh.strings):
                if EMOJI_RE.search(str(ns)):
                    ns.replace_with(strip_emoji(str(ns)))
        tail = MFOOT + '\n' + THEME_DOTS + '\n' + THEME_JS + '\n' + BRIDGE_CSS
        disc = None
        for d in body.find_all('div'):
            if d.parent is body and d.name == 'div' and d.get_text(strip=True).startswith('免责声明'):
                disc = d
                break
        if disc is not None:
            mount_before(tail, disc)
        else:
            mount(tail, body, len(body.contents))
        acts.append('+mfoot+theme')
    else:  # minimal / tools
        mount(NAV_HTML + '\n<div class="cw-wrap">' + crumb_html(rel, title) + '</div>', body, 0)
        acts.append(f'+mnav+crumb({mode})')
        if mode == 'minimal' and 'AI 辅助整理' not in soup.get_text():
            disc = ('<div class="cw-wrap" style="margin-top:14px;"><div class="disc"><b>免责声明</b>　'
                    '本页内容为临床参考资料，由 AI 辅助整理、Cite-holmes 及人工审校，仅供专业交流，'
                    '不构成对具体患者的诊疗建议；临床决策请结合患者实际情况并遵循所在医疗机构规范。'
                    '所引指南与文献均标注来源与核验状态，引用请以原文为准。</div></div>')
            mount(disc, body, len(body.contents))
            acts.append('+disc')
        mount(THEME_DOTS + '\n' + THEME_JS + '\n' + BRIDGE_CSS, body, len(body.contents))
        acts.append('+theme')

    if mode == 'tools':
        for st in head.find_all('style') + body.find_all('style'):
            s = st.string or st.get_text()
            if s and 'padding:56px' in s:
                st.string = s.replace('padding:56px', 'padding:20px', 1)
                acts.append('wrap-pad→20')
        # judge确认项: 工具页手机端主题切换圆点抬离粘性底栏
        mount('<style data-mw-bridge="1">@media (max-width:768px){.theme-dots{bottom:96px;}}</style>',
              body, len(body.contents))
        acts.append('dots抬离底栏')

    # ---- 全局: 正文内 github.io 旧域链接 → docsor.cn ----
    for a in soup.find_all('a', href=True):
        if 'docsor1212.github.io/MedWiki-Rheum' in a['href']:
            a['href'] = a['href'].replace('https://docsor1212.github.io/MedWiki-Rheum', 'https://docsor.cn')
            acts.append('旧域链接修正')

    # ---- 末尾脚本: qrcode+share统一v6 / 绝对路径修正 / 缺则补 ----
    for sc in body.find_all('script', src=True):
        src = sc['src']
        new = src
        if new.startswith('/assets/'):
            new = '..' + new
            acts.append('绝对路径修正')
        new = re.sub(r'share\.js\?v=\d+', f'share.js?v={V_SHARE}', new)
        if new != src:
            sc['src'] = new
    if not any('share.js' in (sc.get('src') or '') for sc in body.find_all('script', src=True)):
        mount(f'<script src="../assets/qrcode.min.js"></script>\n<script src="../assets/share.js?v={V_SHARE}" defer></script>',
              body, len(body.contents))
        acts.append('+share')

    out = str(soup)
    if out == raw:
        return (rel, 'nochange', '')
    if dry:
        return (rel, 'DRY ' + ','.join(acts), f'{len(raw)}→{len(out)}B')
    with io.open(path, 'w', encoding='utf-8', newline='') as f:
        f.write(out)
    return (rel, 'OK ' + ','.join(acts), f'{len(raw)}→{len(out)}B')


def main():
    argv = sys.argv[1:]
    dry = '--dry' in argv
    if '--all' in argv:
        targets = []
        for dirpath, dirnames, filenames in os.walk(ROOT):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for fn in filenames:
                if fn.endswith('.html'):
                    targets.append(os.path.relpath(os.path.join(dirpath, fn), ROOT))
    else:
        targets = [a for a in argv if not a.startswith('--')]
    n_ok = n_skip = 0
    for t in sorted(targets):
        rel = t.replace(os.sep, '/').lstrip('/')
        mode = detect_mode(rel)
        if mode == 'skip':
            n_skip += 1
            continue
        full = os.path.join(ROOT, rel)
        if not os.path.isfile(full):
            print(f'[ERR] 不存在: {rel}')
            continue
        r = process(full, rel, mode, dry)
        print(f'[{r[1]}] {r[0]} | {r[2]}')
        n_ok += 1
    print(f'\n== 处理 {n_ok} 页, skip {n_skip} 项, dry={dry} ==')


if __name__ == '__main__':
    main()
