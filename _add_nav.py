#!/usr/bin/env python3
"""Add fixed top nav bar to all MedWiki-Rheum sub-pages."""
import re, glob, os

NAV_CSS = """
.nav-bar{position:fixed;top:0;left:0;right:0;z-index:1000;background:#20a39e;color:#fff;
padding:6px 16px;display:flex;align-items:center;gap:12px;font-family:'Noto Sans SC',sans-serif;
font-size:13px;box-shadow:0 2px 6px rgba(0,0,0,.12);}
.nav-bar a{color:#fff;text-decoration:none;opacity:.85;transition:opacity .2s;}
.nav-bar a:hover{opacity:1;}
.nav-bar .nav-title{font-weight:600;margin-left:auto;opacity:.7;font-size:12px;}
body{padding-top:42px !important;}
"""

NAV_HTML_MAP = {
    'topics/': '<div class="nav-bar"><a href="../index.html">🏠 首页</a><a href="../index.html#/topics">📖 疾病</a><a href="../index.html#/drugs">💊 药物</a><a href="../index.html#/tools">🔬 工具</a><span class="nav-title">{title}</span></div>',
    'drugs/':  '<div class="nav-bar"><a href="../index.html">🏠 首页</a><a href="../index.html#/topics">📖 疾病</a><a href="../index.html#/drugs">💊 药物</a><a href="../index.html#/tools">🔬 工具</a><span class="nav-title">{title}</span></div>',
    'tools/':  '<div class="nav-bar"><a href="../index.html">🏠 首页</a><a href="../index.html#/topics">📖 疾病</a><a href="../index.html#/drugs">💊 药物</a><a href="../index.html#/tools">🔬 工具</a><span class="nav-title">{title}</span></div>',
}

count = 0
for subdir in ['topics', 'drugs', 'tools']:
    for fpath in sorted(glob.glob(f'{subdir}/*.html')):
        html = open(fpath, 'r').read()
        
        # Extract title
        m = re.search(r'<title>([^<]+)</title>', html)
        title = m.group(1).replace(' — ', ' · ').strip() if m else os.path.basename(fpath)
        
        nav_html = NAV_HTML_MAP[subdir + '/'].format(title=title)
        
        # Skip if already has nav-bar
        if 'nav-bar' in html:
            print(f'  SKIP (has nav): {fpath}')
            continue
        
        # Add CSS before </style>
        if '</style>' in html:
            html = html.replace('</style>', NAV_CSS + '\n</style>', 1)
        
        # Add nav HTML right after <body...>
        body_match = re.search(r'(<body[^>]*>)', html)
        if body_match:
            pos = body_match.end()
            html = html[:pos] + '\n' + nav_html + html[pos:]
        
        open(fpath, 'w').write(html)
        count += 1
        print(f'  OK: {fpath} ({title})')

print(f'\nDone: {count} pages updated')
