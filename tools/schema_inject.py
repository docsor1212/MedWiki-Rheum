# -*- coding: utf-8 -*-
"""P0-A: llms.txt 生成 + topics/drugs schema.org JSON-LD 注入（幂等）
用法: python3 tools/schema_inject.py [--all-pages]
幂等标记: <script id="mw-schema" data-mw-schema="1">"""
import io, os, re, glob, json, datetime
from bs4 import BeautifulSoup

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = '2026-09-22'

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
_SKILLS = [
    ('cite-holmes — 参考文献核查 · AI幻觉引用检测', 'docsor1212/cite-holmes',
     '深度调研+逐条引用机器验真：编造 DOI/假 PMID/假 arXiv 判 invalid、撤稿检测、引用查证/fact check',
     'skillhub.cn/skills/cite-holmes'),
    ('pubmed-verifier — PubMed 引文验证', 'docsor1212/pubmed-verifier',
     'PMID 存在性核验(E-utilities)/DOI 交叉比对/拼接伪造检测/撤稿提醒', ''),
    ('academic-figures — 科研论文图表一键生成', 'docsor1212/academic-figures',
     '22+ 图型/期刊配色/600dpi/组合图,纯本地渲染数据不出机', 'skillhub.cn/skills/academic-figures'),
    ('paper-polisher — 学术润色', 'docsor1212/paper-polisher',
     'AI 痕迹信号自检/术语一致性/中英双语学术写作', ''),
    ('paper-polisher-pro — 学术润色 Pro', 'docsor1212/paper-polisher-pro',
     '批量改写/术语表强制/风格预设/证据安全编辑', ''),
    ('doc-holmes — PDF 精准翻译', 'docsor1212/doc-holmes',
     '版面保留/公式术语保护/双语对照 PDF/批量断点续翻', ''),
    ('cn-med-oa — 中文医学 OA 文献', 'docsor1212/cn-med-oa',
     '维普 OA 检索/免登录 PDF 下载/GB-T7714 引用/五态引用验证', ''),
    ('paper-rewriter — 学术风格自然化', 'docsor1212/paper-rewriter',
     '风格自检报告/确定性清理/数字 DOI PMID 完整性护栏', 'skillhub.cn/skills/paper-rewriter'),
    ('humanize-ai-text — 文本 AI 味扫描', 'docsor1212/humanize-ai-text',
     '评分+命中句+高频模式(仅检测,不改写)', ''),
]
lines += ['## Agent Skills（AI/Agent 可直接安装的科研工具）']
for _n, _r, _d, _sh in _SKILLS:
    lines.append(f'- [{_n}](https://github.com/{_r}): {_d}。'
                 f'安装：`npx skills add {_r}`'
                 + (f'；中文版 https://{_sh}' if _sh else ''))
lines.append('')
lines += ['## 站点说明', '- 主题系统: glm/honey/teal 三主题', '- 核心计算器均经文献锚点校验',
          '- 联系/勘误: https://github.com/docsor1212/MedWiki-Rheum/issues', '']
io.open('llms.txt', 'w', encoding='utf-8', newline='').write('\n'.join(lines))
print('[OK] llms.txt', len(lines), '行')

# ---------- 2) schema.org 注入 ----------
pages = sorted(glob.glob('topics/*.html')) + sorted(glob.glob('drugs/*.html')) + sorted(glob.glob('evidence/*.html')) + sorted(glob.glob('tools/*.html')) + sorted(glob.glob('cases/*.html')) + sorted(glob.glob('templates/*.html'))
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
