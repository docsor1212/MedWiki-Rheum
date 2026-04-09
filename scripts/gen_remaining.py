#!/usr/bin/env python3
"""Generate all remaining case HTML files for AID, ITP, PID, SLE, Uveitis."""
import os, json

CASES_DIR = os.path.expanduser("~/MedWiki-Rheum/cases")
os.makedirs(CASES_DIR, exist_ok=True)

# Load data from JSON
DATA_FILE = os.path.join(os.path.dirname(__file__), "cases_data.json")
with open(DATA_FILE) as f:
    DATA = json.load(f)

CSS = open(os.path.join(os.path.dirname(__file__), "case_css.txt")).read()

def mk_tags(tags):
    return " ".join(f'<span class="tag {t["c"]}">{t["l"]}</span>' for t in tags)

def mk_timeline(items):
    h = ""
    for item in items:
        cls = f' {item.get("c","")}' if item.get("c") else ''
        h += f'<div class="t-item{cls}"><div class="t-date">{item["d"]}</div><div class="t-content">{item["v"]}</div></div>\n'
    return h

def mk_table(headers, rows):
    h = "<tr>" + "".join(f'<th>{x}</th>' for x in headers) + "</tr>\n"
    for r in rows:
        h += '<tr><td class="b">' + r[0] + '</td>' + "".join(f'<td>{c}</td>' for c in r[1:]) + '</tr>\n'
    return h

def mk_case(topic, c):
    return f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{c["t"]}</title><script src="https://cdn.tailwindcss.com"></script><link rel="manifest" href="../manifest.json"><style>{CSS}</style></head><body>
<div class="nav-bar"><a href="../index.html">🏠</a><a href="../topics/{topic}.html">{topic}</a><a href="index_{topic}.html">病例</a><span style="margin-left:auto;opacity:.7;font-size:12px">{c["nav"]}</span></div>
<div class="wrap"><div class="header"><div><h1>{c["t"]}</h1><div class="sub">{c["sub"]}</div></div><div class="meta">2026-04-10</div></div>
<div style="background:#fff3e0;border-left:4px solid #e65100;padding:8px 14px;font-size:11.5px"><b style="color:#e65100">⚠️ 免责声明</b>　本病例基于已发表文献整理。仅供医学专业人员学习参考，<b>不构成诊疗建议</b>。</div>
<div class="body">
<div class="sh">👤 基本信息</div><table><tr><td class="b" style="width:80px">标签</td><td>{mk_tags(c["tags"])}</td></tr><tr><td class="b">文献</td><td style="font-size:11px;color:var(--text2)">{c["ref"]}</td></tr></table>
<div class="alert"><b>独特性：</b>{c["alert"]}</div>
<div class="sh red">🔴 临床经过</div><div class="timeline">{mk_timeline(c["tl"])}</div>
<div class="sh yellow">🔬 {c["mech_t"]}</div><div class="mas-box"><div style="font-weight:700;font-size:12px;color:#e65100">🧬 {c["mech_t"]}</div><div style="font-size:11.5px;line-height:1.7;margin-top:4px">{c["mech"]}</div></div>
<div class="sh">📊 对比</div><table>{mk_table(c["th"],c["tr"])}</table>
<div class="sh green">📚 要点</div><ul style="font-size:12px;line-height:1.8;margin:4px 0;padding-left:18px">{"".join(f"<li>{p}</li>" for p in c["pts"])}</ul>
<div class="sh">📖 文献</div><div style="font-size:11px;color:var(--text2)">{c["ref"]}</div>
</div>
<div style="text-align:center;padding:8px 20px;border-top:1px solid var(--border)"><a href="index_{topic}.html" style="display:inline-block;padding:6px 12px;background:var(--accent);color:#fff;border-radius:6px;text-decoration:none;font-size:11px">📋 返回{topic}目录</a></div>
<div class="footer">PMID: {c["pmid"]} · 不构成诊疗建议 · {topic}病例第{c["n"]}篇</div></div></body></html>'''

def mk_index(topic, cn, cases):
    cards = ""
    for c in cases:
        cards += f'<a href="{c["f"]}"><div style="border:1px solid var(--border);border-radius:8px;padding:10px 14px;margin:6px 0;cursor:pointer"><div style="font-weight:700;font-size:13px">{c["n"]}. {c["t"]}</div><div style="font-size:11px;color:var(--text2)">PMID: {c["pmid"]}</div></div></a>\n'
    refs = "<br>".join(f'{c["n"]}. PMID: {c["pmid"]}' for c in cases)
    return f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{cn}病例</title><style>{CSS}</style></head><body>
<div class="nav-bar" style="background:var(--accent)"><a href="../index.html">🏠</a><a href="index.html">全部病例</a><span style="margin-left:auto;opacity:.7;font-size:12px">{cn}</span></div>
<div class="wrap"><div style="background:var(--accent);color:#fff;padding:14px 20px"><h1 style="font-size:1.4rem;font-weight:700">🔬 {cn}临床病例专题</h1><div style="font-size:.85rem;opacity:.85;margin-top:2px">{len(cases)}个真实世界病例</div></div>
<div style="padding:12px 20px 16px">{cards}<div style="font-size:10.5px;color:var(--text2);margin-top:10px">{refs}</div></div>
<div class="footer">MedWiki-Rheum · 不构成诊疗建议</div></div></body></html>'''

# Generate all
total = 0
for topic, info in DATA.items():
    cn = info["cn"]
    cases = info["cases"]
    # Cases
    for c in cases:
        html = mk_case(topic, c)
        path = os.path.join(CASES_DIR, c["f"])
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        sz = os.path.getsize(path)
        print(f"  {c['f']} ({sz}B)")
        total += 1
    # Index
    idx = mk_index(topic, cn, cases)
    ipath = os.path.join(CASES_DIR, f"index_{topic}.html")
    with open(ipath, "w", encoding="utf-8") as f:
        f.write(idx)
    print(f"  index_{topic}.html ({os.path.getsize(ipath)}B)")
    total += 1

print(f"\nDone! Generated {total} files total.")
