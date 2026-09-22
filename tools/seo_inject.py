# -*- coding: utf-8 -*-
"""SEO基线注入：canonical + Open Graph + twitter card（幂等：已有canonical跳过）"""
import io, os, glob, re

DOMAIN = 'https://docsor.cn'
n_new = n_skip = 0
for f in sorted(glob.glob('**/*.html', recursive=True)):
    if f.startswith(('node_modules', '.git')) or 'backup' in f:
        continue
    rel = f.replace(os.sep, '/')
    t = io.open(f, encoding='utf-8').read()
    if 'rel="canonical"' in t:
        n_skip += 1
        continue
    mt = re.search(r'<title>([^<]*)</title>', t)
    title = mt.group(1).strip() if mt else 'MedWiki-Rheum'
    md = re.search(r'<meta name="description" content="([^"]*)"', t)
    dsc = md.group(1) if md else title
    url = f'{DOMAIN}/{rel}'
    tag = (f'\n<!--mw-seo-->\n<link rel="canonical" href="{url}">\n'
           f'<meta property="og:title" content="{title}">\n'
           f'<meta property="og:description" content="{dsc}">\n'
           f'<meta property="og:url" content="{url}">\n'
           f'<meta property="og:type" content="website">\n'
           f'<meta property="og:site_name" content="MedWiki-Rheum">\n'
           f'<meta property="og:locale" content="zh_CN">\n'
           f'<meta name="twitter:card" content="summary">\n')
    if '</head>' in t:
        t = t.replace('</head>', tag + '</head>', 1)
        io.open(f, 'w', encoding='utf-8', newline='').write(t)
        n_new += 1
print(f'[OK] SEO注入: 新{n_new} 跳过{n_skip}')

