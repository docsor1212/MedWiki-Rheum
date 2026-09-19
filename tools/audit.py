# -*- coding: utf-8 -*-
"""
MedWiki-Rheum 内容页验收 audit.py (方案§6清单自动化)
用法: python3 audit.py <rel paths...> | python3 audit.py --all
每页输出逐项检查 + PASS/FAIL 总结行。--quiet 只输出非PASS。
"""
import io, json, os, re, sys
from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_once(rel_path, cache={}):
    if rel_path not in cache:
        p = os.path.join(ROOT, rel_path)
        try:
            with io.open(p, encoding='utf-8') as f:
                cache[rel_path] = f.read()
        except Exception:
            cache[rel_path] = ''
    return cache[rel_path]

def audit(rel):
    full = os.path.join(ROOT, rel)
    try:
        with io.open(full, encoding='utf-8-sig') as f:
            raw = f.read()
    except FileNotFoundError:
        return rel, ['文件不存在'], 'FAIL'
    soup = BeautifulSoup(raw, 'html.parser')
    html = soup.find('html') or soup
    res = []
    def chk(name, ok):
        res.append(f'{"✓" if ok else "✗"}{name}')
        return ok
    rebuilt = 'data-mw-rebuilt="1"' in raw
    bare = rel.startswith('evidence/')  # 成品文章自带品牌hero, 不要求骨架组件
    tetra = rel == 'evidence/ev_TETRA_01.html'  # 自包含deckdoc豁免页(1.09MB, /assets/在docsor.cn根路径可用)
    chk('重建标记', rebuilt or tetra)
    chk('mnav', bare or bool(soup.find(class_='mnav')))
    chk('面包屑', bare or bool(soup.find(class_='cw-crumb')))
    chk('viewport', bool(soup.find('meta', attrs={'name': 'viewport'})))
    chk('theme-color', tetra or bool(soup.find('meta', attrs={'name': 'theme-color'})))
    chk('无tailwind', 'cdn.tailwindcss.com' not in raw)
    chk('无SW注册', 'serviceWorker' not in raw)
    chk('无github.io旧域', 'docsor1212.github.io' not in raw)
    scripts = ' '.join(sc.get('src') or '' for sc in soup.find_all('script', src=True))
    chk('share.js v7', 'share.js?v=7' in scripts)
    chk('qrcode', 'qrcode.min.js' in scripts)
    body_text = soup.get_text()
    chk('免责声明', ('免责声明' in body_text and 'AI 辅助整理' in body_text))
    dsu = html.get('data-share-url', '')
    chk('share-url=docsor.cn', dsu.startswith('https://docsor.cn/'))
    for name, ver in (('themes.css', 6), ('medwiki.css', 26), ('content.css', 4)):
        chk(f'{name}v{ver}', bare or f'{name}?v={ver}' in raw)
    chk('无/assets/绝对路径', tetra or ('src="/assets/' not in raw and 'href="/assets/' not in raw))
    # sitemap + search-index
    sm = load_once('sitemap.xml')
    chk('sitemap收录', rel in sm)
    si = load_once('assets/search-index.json')
    ok_si = False
    if si:
        try:
            entries = json.loads(si)
            for e in (entries if isinstance(entries, list) else entries.get('pages', [])):
                u = json.dumps(e, ensure_ascii=False)
                if rel in u:
                    ok_si = True
                    break
        except Exception:
            ok_si = rel in si
    chk('search-index收录', ok_si)
    fails = [r for r in res if r.startswith('✗')]
    return rel, res, ('PASS' if not fails else 'FAIL:' + ';'.join(fails))

def main():
    argv = sys.argv[1:]
    quiet = '--quiet' in argv
    if '--all' in argv:
        targets = []
        for dirpath, dirnames, filenames in os.walk(ROOT):
            dirnames[:] = [d for d in dirnames if d not in ('.git', 'medtts', '_probe', 'screenshots')]
            for fn in filenames:
                if fn.endswith('.html'):
                    targets.append(os.path.relpath(os.path.join(dirpath, fn), ROOT))
    else:
        targets = [a for a in argv if not a.startswith('--')]
    npass = nfail = 0
    failed = []
    for t in sorted(targets):
        rel, res, verdict = audit(t.replace(os.sep, '/'))
        is_pass = verdict == 'PASS'
        npass, nfail = npass + is_pass, nfail + (not is_pass)
        if not is_pass:
            failed.append(rel)
        if not quiet or not is_pass:
            print(f'[{verdict}] {rel}')
            if not is_pass:
                print('   ', ' '.join(res))
    print(f'\n== PASS {npass} / FAIL {nfail} (共{npass+nfail}) ==')
    if failed:
        print('FAIL清单:', *failed, sep='\n  ')

if __name__ == '__main__':
    main()
