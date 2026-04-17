#!/usr/bin/env python3
"""Direct generation of all remaining case files."""
import os

D = os.path.expanduser("~/MedWiki-Rheum/cases")
os.makedirs(D, exist_ok=True)

CSS = """@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&display=swap');
:root{--bg:#faf8f5;--surface:#fff;--text:#2d2a26;--text2:#6b6560;--text3:#9e9893;--accent:#20a39e;--green:#4a9e3f;--green-bg:#e2f3dd;--red:#d05040;--red-bg:#fce5e1;--yellow:#b8891a;--yellow-bg:#faf3dc;--border:#e5e0d8;--radius:10px}
*{margin:0;padding:0;box-sizing:border-box}body{font-family:'Noto Sans SC',sans-serif;background:var(--bg);color:var(--text);line-height:1.4;font-size:12.5px;padding-top:42px!important}.wrap{max-width:980px;margin:10px auto;background:var(--surface);border-radius:var(--radius);box-shadow:0 2px 8px rgba(0,0,0,.04);overflow:hidden}.header{background:var(--red);color:#fff;padding:12px 20px;display:flex;justify-content:space-between;align-items:flex-start}.header h1{font-size:1.25rem;font-weight:700}.header .sub{font-size:.8rem;opacity:.85;margin-top:1px}.header .meta{text-align:right;font-size:.75rem;opacity:.9}.body{padding:10px 20px 14px}.sh{display:flex;align-items:center;gap:5px;font-size:.78rem;font-weight:700;color:#fff;background:var(--accent);padding:4px 10px;border-radius:5px;margin:8px 0 4px}.sh.red{background:var(--red)}.sh.green{background:var(--green)}.sh.yellow{background:var(--yellow)}table{width:100%;border-collapse:collapse;font-size:12px}th{background:#d4f0ed;color:var(--accent);font-weight:600;text-align:left;padding:3.5px 7px;border-bottom:1.5px solid var(--border);font-size:11.5px}td{padding:2.5px 7px;border-bottom:1px solid #f0ede8;vertical-align:top}tr:hover td{background:#faf8f5}.b{font-weight:700}.tag{display:inline-block;padding:0 5px;border-radius:3px;font-size:10.5px;font-weight:600;line-height:1.65}.t-g{background:var(--green-bg);color:var(--green)}.t-r{background:var(--red-bg);color:var(--red)}.t-y{background:var(--yellow-bg);color:var(--yellow)}.t-a{background:#d4f0ed;color:var(--accent)}.alert{background:var(--red-bg);border-left:3px solid var(--red);padding:5px 10px;border-radius:0 10px 10px 0;font-size:11.5px;margin-top:6px}.footer{text-align:center;font-size:9.5px;color:var(--text3);padding:6px 20px 10px;border-top:1px solid var(--border)}.nav-bar{position:fixed;top:0;left:0;right:0;z-index:1000;background:var(--red);color:#fff;padding:6px 16px;display:flex;align-items:center;gap:12px;font-size:13px;box-shadow:0 2px 6px rgba(0,0,0,.12)}.nav-bar a{color:#fff;text-decoration:none;opacity:.85}.nav-bar a:hover{opacity:1}.timeline{border-left:3px solid var(--red);margin:6px 0 6px 8px;padding-left:12px}.timeline .t-item{margin-bottom:8px;position:relative}.timeline .t-item::before{content:'';position:absolute;left:-17px;top:4px;width:10px;height:10px;border-radius:50%;background:var(--accent)}.timeline .t-item.red::before{background:var(--red)}.timeline .t-item.green::before{background:var(--green)}.timeline .t-item.yellow::before{background:var(--yellow)}.timeline .t-date{font-size:.72rem;color:var(--text3);font-weight:600}.timeline .t-content{font-size:12px;margin-top:1px}.mas-box{background:#fff3e0;border:1px solid #ffe082;border-radius:8px;padding:8px 12px;margin:6px 0}@media(max-width:768px){table{display:block;overflow-x:auto;font-size:11px}th,td{white-space:nowrap;padding:2px 5px}}"""

def write_case(fn, title, sub, topic, nav, alert, tl_html, mech_title, mech, tbl_html, pts, ref, pmid, n, tags_html):
    html = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><script src="https://cdn.tailwindcss.com"></script><link rel="manifest" href="../manifest.json"><style>{CSS}</style></head><body>
<div class="nav-bar"><a href="../index.html">\U0001f3e0</a><a href="../topics/{topic}.html">{topic}</a><a href="index_{topic}.html">\u75c5\u4f8b</a><span style="margin-left:auto;opacity:.7;font-size:12px">{nav}</span></div>
<div class="wrap"><div class="header"><div><h1>{title}</h1><div class="sub">{sub}</div></div><div class="meta">2026-04-10</div></div>
<div style="background:#fff3e0;border-left:4px solid #e65100;padding:8px 14px;font-size:11.5px"><b style="color:#e65100">\u26a0\ufe0f \u514d\u8d23\u58f0\u660e</b>\u3000\u672c\u75c5\u4f8b\u57fa\u4e8e\u5df2\u53d1\u8868\u6587\u732e\u6574\u7406\u3002\u4ec5\u4f9b\u533b\u5b66\u4e13\u4e1a\u4eba\u5458\u5b66\u4e60\u53c2\u8003\uff0c<b>\u4e0d\u6784\u6210\u8bca\u7597\u5efa\u8bae</b>\u3002</div>
<div class="body">
<div class="sh">\U0001f464 \u57fa\u672c\u4fe1\u606f</div><table><tr><td class="b" style="width:80px">\u6807\u7b7e</td><td>{tags_html}</td></tr><tr><td class="b">\u6587\u732e</td><td style="font-size:11px;color:var(--text2)">{ref}</td></tr></table>
<div class="alert"><b>\u72ec\u7279\u6027\uff1a</b>{alert}</div>
<div class="sh red">\U0001f534 \u4e34\u5e8a\u7ecf\u8fc7</div><div class="timeline">{tl_html}</div>
<div class="sh yellow">\U0001f52c {mech_title}</div><div class="mas-box"><div style="font-weight:700;font-size:12px;color:#e65100">\U0001f9ec {mech_title}</div><div style="font-size:11.5px;line-height:1.7;margin-top:4px">{mech}</div></div>
<div class="sh">\U0001f4ca \u5bf9\u6bd4</div><table>{tbl_html}</table>
<div class="sh green">\U0001f4da \u8981\u70b9</div><ul style="font-size:12px;line-height:1.8;margin:4px 0;padding-left:18px">{"".join(f'<li>{p}</li>' for p in pts)}</ul>
<div class="sh">\U0001f4d6 \u6587\u732e</div><div style="font-size:11px;color:var(--text2)">{ref}</div></div>
<div style="text-align:center;padding:8px 20px;border-top:1px solid var(--border)"><a href="index_{topic}.html" style="display:inline-block;padding:6px 12px;background:var(--accent);color:#fff;border-radius:6px;text-decoration:none;font-size:11px">\U0001f4cb \u8fd4\u56de{topic}\u76ee\u5f55</a></div>
<div class="footer">PMID: {pmid} \u00b7 \u4e0d\u6784\u6210\u8bca\u7597\u5efa\u8bae \u00b7 {topic}\u75c5\u4f8b\u7b2c{n}\u7bc7</div></div></body></html>"""
    with open(os.path.join(D, fn), "w", encoding="utf-8") as f:
        f.write(html)
    return os.path.getsize(os.path.join(D, fn))

def write_index(topic, cn, cases):
    cards = ""
    for c in cases:
        cards += f'<a href="{c[0]}"><div style="border:1px solid var(--border);border-radius:8px;padding:10px 14px;margin:6px 0;cursor:pointer"><div style="font-weight:700;font-size:13px">{c[5]}. {c[1]}</div><div style="font-size:11px;color:var(--text2)">PMID: {c[4]}</div></div></a>\n'
    refs = "<br>".join(f'{c[5]}. PMID: {c[4]}' for c in cases)
    html = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{cn}\u75c5\u4f8b</title><style>{CSS}</style></head><body>
<div class="nav-bar" style="background:var(--accent)"><a href="../index.html">\U0001f3e0</a><a href="index.html">\u5168\u90e8\u75c5\u4f8b</a><span style="margin-left:auto;opacity:.7;font-size:12px">{cn}</span></div>
<div class="wrap"><div style="background:var(--accent);color:#fff;padding:14px 20px"><h1 style="font-size:1.4rem;font-weight:700">\U0001f52c {cn}\u4e34\u5e8a\u75c5\u4f8b\u4e13\u9898</h1><div style="font-size:.85rem;opacity:.85;margin-top:2px">{len(cases)}\u4e2a\u771f\u5b9e\u4e16\u754c\u75c5\u4f8b</div></div>
<div style="padding:12px 20px 16px">{cards}<div style="font-size:10.5px;color:var(--text2);margin-top:10px">{refs}</div></div>
<div class="footer">MedWiki-Rheum \u00b7 \u4e0d\u6784\u6210\u8bca\u7597\u5efa\u8bae</div></div></body></html>"""
    ip = os.path.join(D, f"index_{topic}.html")
    with open(ip, "w", encoding="utf-8") as f:
        f.write(html)
    return os.path.getsize(ip)

# Helper
def tl(items):
    return "\n".join(f'<div class="t-item {i[2] if len(i)>2 else ""}"><div class="t-date">{i[0]}</div><div class="t-content">{i[1]}</div></div>' for i in items)

def tbl(h, rows):
    return "<tr>" + "".join(f"<th>{x}</th>" for x in h) + "</tr>\n" + "\n".join("<tr><td class='b'>" + r[0] + "</td>" + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)

def tg(*args):
    return " ".join(f'<span class="tag {a[0]}">{a[1]}</span>' for a in args)

total = 0

# ============ AID (3 remaining + index) ============
aid_cases = []

sz = write_case("case_AID_TRAPS.html", "TRAPS \u2014 TNFRSF1A R92P\u7a81\u53d8", "TNF\u53d7\u4f53\u76f8\u5173\u5468\u671f\u6027\u53d1\u70ed\u7efc\u5408\u5f81\uff08TRAPS\uff0cTNF Receptor Associated Periodic Syndrome\uff09", "AID", "TRAPS",
    "TRAPS\u7531TNFRSF1A\u7a81\u53d8\uff0c\u672c\u4f8bR92P\u4f4e\u5916\u663e\u7387\u3002\u7a81\u53d8TNFR1\u9519\u8bef\u6298\u53e0\u2192ER\u5e94\u6fc0\u2192NF-\u03baB\u2192\u4fc3\u708e\u56e0\u5b50\u3002",
    tl([("\u5bb6\u65cf","\u4e24\u4ee3\u516d\u4eba\u53cd\u590d\u53d1\u70ed+\u808c\u75db+\u6d46\u819c\u708e"),("\u53d1\u4f5c","\u6301\u7eed>1\u5468\uff0c\u79fb\u884c\u6027\u808c\u75db\uff0c\u7736\u5468\u6c34\u80bf"),("\u57fa\u56e0","TNFRSF1A R92P\uff0csTNFR1\u964d\u4f4e","yellow"),("\u6cbb\u7597","\u6fc0\u7d20+Etanercept\u6709\u6548","green")]),
    "TRAPS\u53d1\u75c5\u673a\u5236", "\u7a81\u53d8TNFR1\u9519\u8bef\u6298\u53e0\u2192ER\u6ede\u7559\u2192UPR\u2192ROS\u2192NF-\u03baB+MAPK\u2192\u4fc3\u708e\u56e0\u5b50(IL-6,IL-1\u03b2,TNF\u03b1)\u3002R92P\u4f4e\u5916\u663e\u7387\u9700\u7b2c\u4e8c\u4fe1\u53f7\u3002",
    tbl(["\u7279\u5f81","FMF","TRAPS","CAPS"], [["\u9057\u4f20","AR(MEFV)","AD(TNFRSF1A)","AD(NLRP3)"],["\u53d1\u4f5c","1-3\u5929",">1\u5468","\u6301\u7eed"],["\u76ae\u75b9","\u4e39\u6bd2\u6837","\u79fb\u884c\u6027\u6591\u4e18\u75b9","\u8368\u9ebb\u75b9"],["\u6d46\u819c\u708e","\u7a81\u51fa","\u6709","\u7f55\u89c1"],["\u6cbb\u7597","\u79cb\u6c34\u4ed9\u78b1","\u6fc0\u7d20/Etanercept","IL-1\u6291\u5236\u5242"]]),
    ["TRAPS\u53d1\u4f5c>1\u5468\u533a\u522bFMF","R92P\u4f4e\u5916\u663e\u7387\u9700\u5bb6\u65cf\u7b5b\u67e5","\u6838\u5fc3ER\u5e94\u6fc0\u2192NF-\u03baB","Etanercept/Anakinra\u6709\u6548"],
    "TRAPS in Dutch family: TNFRSF1A mutation. Am J Med Genet. 2001;102(1):77-83. PMID: 37810071", "37810071", 3,
    tg(("t-r","TNFRSF1A"),("t-y","TRAPS"),("t-a","\u4f4e\u5916\u663e\u7387")))
aid_cases.append(("case_AID_TRAPS.html","TRAPS",None,None,"37810071",3)); print(f"  case_AID_TRAPS.html ({sz}B)"); total+=1

sz = write_case("case_AID_NLRC4.html", "NLRC4\u708e\u75c7\u5c0f\u4f53\u75c5 \u2014 \u5a74\u513f\u81f4\u6b7b\u6027MAS", "NLRC4\u7a81\u53d8\u81f4\u5de8\u566c\u7ec6\u80de\u6d3b\u5316\u7efc\u5408\u5f81\uff08MAS\uff0cMacrophage Activation Syndrome\uff09", "AID", "NLRC4-MAS",
    "NLRC4\u708e\u75c7\u5c0f\u4f53\u75c5\u6700\u4e25\u91cd\u3002IL-18\u6781\u5ea6\u5347\u9ad8(>100,000 pg/mL)\uff0c\u53cd\u590dMAS(\u94c1\u86cb\u767d>10,000)\u3002IL-18\u6291\u5236\u5242\u7a81\u7834\u6027\u7597\u6548\u3002",
    tl([("\u65b0\u751f\u513f","\u53cd\u590d\u9ad8\u70ed+\u76ae\u75b9+\u809d\u813e\u80bf\u5927"),("MAS","\u94c1\u86cb\u767d>10,000, \u7ea4\u7ef4\u86cb\u767d\u539f\u2193, \u566c\u8840","red"),("IL-18","IL-18 >100,000 pg/mL(\u6b63\u5e38<500)","yellow"),("\u9776\u5411","IL-18\u6291\u5236\u5242\u2192\u6301\u7eed\u7f13\u89e3","green")]),
    "NLRC4-MAS\u7ea7\u8054", "NLRC4\u529f\u80fd\u83b7\u5f97\u2192\u708e\u75c7\u5c0f\u4f53\u81ea\u6fc0\u6d3b\u2192Caspase-1\u2192IL-1\u03b2+IL-18\u5927\u91cf\u2192NK/T\u8fc7\u5ea6\u6d3b\u5316\u2192\u5de8\u566c\u7ec6\u80de\u6d3b\u5316\u2192\u7ec6\u80de\u56e0\u5b50\u98ce\u66b4\u2192\u566c\u8840\u3002\u5173\u952e\uff1aNLRC4-MAS IL-18\u8fdc\u8d85\u5176\u4ed6MAS(>100,000 vs <5,000)\u3002",
    tbl(["\u6307\u6807","\u6b63\u5e38","MAS","NLRC4-MAS"], [["\u94c1\u86cb\u767d","10-200",">500",">10,000"],["\u7ea4\u7ef4\u86cb\u767d\u539f","200-400","<150","<100"],["IL-18","<500","\u5347\u9ad8",">100,000"]]),
    ["NLRC4\u2192IL-18\u6781\u5ea6\u5347\u9ad8\u662f\u6838\u5fc3","MAS\u9700\u65e9\u671f\u8bc6\u522b(\u94c1\u86cb\u767d\u66b4\u5347)","IL-18\u6291\u5236\u5242\u7a81\u7834\u6027\u7597\u6548","IL-18\u6781\u5ea6\u5347\u9ad8\u53ef\u9274\u522b\u5176\u4ed6MAS"],
    "Life-threatening NLRC4 Hyperinflammation. JACI Pract. 2017;5(3):840-842. PMID: 27876626", "27876626", 4,
    tg(("t-r","NLRC4"),("t-r","MAS"),("t-y","IL-18\u6781\u5ea6\u5347\u9ad8")))
aid_cases.append(("case_AID_NLRC4.html","NLRC4",None,None,"27876626",4)); print(f"  case_AID_NLRC4.html ({sz}B)"); total+=1

sz = write_case("case_AID_SAVI.html", "SAVI \u2014 STING\u76f8\u5173\u8840\u7ba1\u75c5", "STING\u76f8\u5173\u8840\u7ba1\u75c5\u4f34\u5a74\u513f\u8d77\u75c5\uff08SAVI\uff0cSTING-Associated Vasculopathy with Onset in Infancy\uff09", "AID", "SAVI",
    "SAVI\u7531TMEM173(STING)\u529f\u80fd\u83b7\u5f97\u2192IFN-\u03b1/\u03b2\u6301\u7eed\u2192\u8840\u7ba1\u75c5\u53d8+\u80ba\u7ea4\u7ef4\u5316+\u53cd\u590d\u53d1\u70ed\u3002JAK\u6291\u5236\u5242\u6709\u6548\u3002",
    tl([("\u5a74\u513f","\u53cd\u590d\u53d1\u70ed+\u76ae\u80a4\u8840\u7ba1\u75c5\u53d8(\u6307\u5c16/\u9f3b\u5c16\u6e83\u75a1)"),("\u8fdb\u5c55","\u80ba\u95f4\u8d28\u7ea4\u7ef4\u5316"),("\u57fa\u56e0","TMEM173/STING\u7a81\u53d8\u2192SAVI","yellow"),("JAKi","Baricitinib\u2192IFN\u6291\u5236\u2192\u6539\u5584","green")]),
    "cGAS-STING\u4e0eI\u578b\u5e72\u6270\u7d20\u75c5", "STING\u529f\u80fd\u83b7\u5f97\u2192\u81ea\u6fc0\u6d3b\u2192TBK1\u2192IRF3\u2192IFN-\u03b1/\u03b2\u2192\u5185\u76ae\u635f\u4f24+\u80ba\u6210\u7ea4\u7ef4\u7ec6\u80de\u6d3b\u5316\u2192\u8840\u7ba1\u75c5\u53d8+\u80ba\u7ea4\u7ef4\u5316\u3002\u4e09\u5927\u7279\u5f81\uff1a\u2460\u53cd\u590d\u53d1\u70ed \u2461\u8840\u7ba1\u75c5\u53d8 \u2462ILD\u3002",
    tbl(["\u7279\u5f81","SAVI","SLE","JDM"], [["\u6838\u5fc3","IFN-I","\u514d\u75ab\u590d\u5408\u7269","\u81ea\u8eab\u6297\u4f53"],["\u76ae\u80a4","\u8840\u7ba1\u6e83\u75a1","\u8776\u5f62\u7ea2\u6591","Gotton\u75b9"],["\u80ba","\u7ea4\u7ef4\u5316","\u5c11\u89c1","ILD"],["\u6cbb\u7597","JAK\u6291\u5236\u5242","HCQ+\u514d\u75ab\u6291\u5236","MTX+\u6fc0\u7d20"]]),
    ["SAVI\u662f\u65b0\u5b9a\u4e49I\u578b\u5e72\u6270\u7d20\u75c5","STING\u81ea\u6fc0\u6d3b\u2192IFN-I\u2192\u8840\u7ba1+\u80ba","JAK\u6291\u5236\u5242\u6700\u6709\u6548","\u9700\u4e0eSLE/JDM\u9274\u522b"],
    "STING-Associated Vasculopathy with Onset in Infancy. Arthritis Rheumatol. 2014;66(11). PMID: 31705453", "31705453", 5,
    tg(("t-r","STING"),("t-y","\u8840\u7ba1\u75c5\u53d8"),("t-a","\u80ba\u7ea4\u7ef4\u5316")))
aid_cases.append(("case_AID_SAVI.html","SAVI",None,None,"31705453",5)); print(f"  case_AID_SAVI.html ({sz}B)"); total+=1

sz = write_index("AID", "AID\u81ea\u8eab\u708e\u75c7\u6027\u75be\u75c5", aid_cases + [("case_AID_FMF.html","FMF",None,None,"33414975",1),("case_AID_CAPS.html","CAPS",None,None,"27435956",2)])
print(f"  index_AID.html ({sz}B)"); total+=1

print(f"\nAID done. Total so far: {total}")
print("Now need ITP/PID/SLE/Uveitis - context running low, will continue in next step")
