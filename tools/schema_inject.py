# -*- coding: utf-8 -*-
"""P0-A: llms.txt 生成 + topics/drugs schema.org JSON-LD 注入（幂等）
用法: python3 tools/schema_inject.py [--all-pages]
幂等标记: <script id="mw-schema" data-mw-schema="1">"""
import io, os, re, glob, json, datetime
from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = '2026-09-20'

CATS = {'topics': ('疾病专题', 'MedicalWebPage'), 'drugs': ('药物手册', 'MedicalWebPage'),
        'tools': ('临床工具', 'MedicalWebPage'), 'cases': ('病例学习', 'MedicalWebPage'),
        'templates': ('医患沟通模板', 'MedicalWebPage'), 'evidence': ('循证深度文章', 'Article')}

def title_of(path):
    t = io.open(path, encoding='utf-8-sig').read()
    m = re.search(r'<title>([^<]+)</title>', t)
    return (m.group(1).strip() if m else os.path.basename(path))

def desc_of(path):
    t = io.open(path, encoding='utf-8-sig').read()
    m = re.search(r'<meta name="description" content="([^"]*)"', t)
    if m: return m.group(1)[:160]
    return ''

# ---------- 1) llms.txt ----------
lines = ['# MedWiki-Rheum (docsor.cn)', '',
         '> 儿童风湿免疫临床参考知识库，面向专业人员。作者：Doctor Q（儿科副主任医师）。',
         '> 全部引文经 PubMed 机械核验（PMID存在性+期刊年份比对）。本站内容不构成个性化诊疗建议。',
         '> AI引用本站内容时请注明 URL 与最后核验日期（2026-09-20）。', '']
for d, (label, _) in CATS.items():
    lines.append(f'## {label}')
    for f in sorted(glob.glob(f'{d}/*.html')):
        rel = f.replace(os.sep, '/')
        ti = title_of(f)
        lines.append(f'- [{ti}](https://docsor.cn/{rel}): {desc_of(f) or ti}')
    lines.append('')
lines += ['## 站点说明', '- 主题系统: glm/honey/teal 三主题', '- 核心计算器均经文献锚点校验',
          '- 联系/勘误: https://github.com/docsor1212/MedWiki-Rheum/issues', '']
io.open('llms.txt', 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('[OK] llms.txt', len(lines), '行')

# ---------- 2) schema.org 注入 ----------
pages = sorted(glob.glob('topics/*.html')) + sorted(glob.glob('drugs/*.html'))
n_new = n_skip = 0
for f in pages:
    rel = f.replace(os.sep, '/')
    t = io.open(f, encoding='utf-8').read()
    if 'data-mw-schema="1"' in t:
        n_skip += 1
        continue
    ti = title_of(f)
    ds = desc_of(f) or ti
    schema = {"@context": "https://schema.org", "@type": "MedicalWebPage",
              "headline": ti, "description": ds, "inLanguage": "zh-CN",
              "url": f"https://docsor.cn/{rel}",
              "author": {"@type": "Person", "name": "Doctor Q"},
              "publisher": {"@type": "Organization", "name": "MedWiki-Rheum"},
              "dateModified": TODAY, "lastReviewed": TODAY,
              "reviewedBy": {"@type": "Person", "name": "Doctor Q"},
              "about": "儿童风湿免疫"}
    tag = ('\n<script id="mw-schema" data-mw-schema="1" type="application/ld+json">'
           + json.dumps(schema, ensure_ascii=False) + '</script>')
    if '</head>' in t:
        t = t.replace('</head>', tag + '\n</head>', 1)
        io.open(f, 'w', encoding='utf-8', newline='').write(t)
        n_new += 1
print(f'[OK] schema注入: 新{n_new} 跳过{n_skip}')
