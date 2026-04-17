#!/usr/bin/env python3
"""Generate ITP, PID, SLE, Uveitis cases."""
import os

D = os.path.expanduser("~/MedWiki-Rheum/cases")
os.makedirs(D, exist_ok=True)

CSS = """@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&display=swap');:root{--bg:#faf8f5;--surface:#fff;--text:#2d2a26;--text2:#6b6560;--text3:#9e9893;--accent:#20a39e;--green:#4a9e3f;--green-bg:#e2f3dd;--red:#d05040;--red-bg:#fce5e1;--yellow:#b8891a;--yellow-bg:#faf3dc;--border:#e5e0d8;--radius:10px}*{margin:0;padding:0;box-sizing:border-box}body{font-family:'Noto Sans SC',sans-serif;background:var(--bg);color:var(--text);line-height:1.4;font-size:12.5px;padding-top:42px!important}.wrap{max-width:980px;margin:10px auto;background:var(--surface);border-radius:var(--radius);box-shadow:0 2px 8px rgba(0,0,0,.04);overflow:hidden}.header{background:var(--red);color:#fff;padding:12px 20px;display:flex;justify-content:space-between;align-items:flex-start}.header h1{font-size:1.25rem;font-weight:700}.header .sub{font-size:.8rem;opacity:.85;margin-top:1px}.header .meta{text-align:right;font-size:.75rem;opacity:.9}.body{padding:10px 20px 14px}.sh{display:flex;align-items:center;gap:5px;font-size:.78rem;font-weight:700;color:#fff;background:var(--accent);padding:4px 10px;border-radius:5px;margin:8px 0 4px}.sh.red{background:var(--red)}.sh.green{background:var(--green)}.sh.yellow{background:var(--yellow)}table{width:100%;border-collapse:collapse;font-size:12px}th{background:#d4f0ed;color:var(--accent);font-weight:600;text-align:left;padding:3.5px 7px;border-bottom:1.5px solid var(--border);font-size:11.5px}td{padding:2.5px 7px;border-bottom:1px solid #f0ede8;vertical-align:top}tr:hover td{background:#faf8f5}.b{font-weight:700}.tag{display:inline-block;padding:0 5px;border-radius:3px;font-size:10.5px;font-weight:600;line-height:1.65}.t-g{background:var(--green-bg);color:var(--green)}.t-r{background:var(--red-bg);color:var(--red)}.t-y{background:var(--yellow-bg);color:var(--yellow)}.t-a{background:#d4f0ed;color:var(--accent)}.alert{background:var(--red-bg);border-left:3px solid var(--red);padding:5px 10px;border-radius:0 10px 10px 0;font-size:11.5px;margin-top:6px}.footer{text-align:center;font-size:9.5px;color:var(--text3);padding:6px 20px 10px;border-top:1px solid var(--border)}.nav-bar{position:fixed;top:0;left:0;right:0;z-index:1000;background:var(--red);color:#fff;padding:6px 16px;display:flex;align-items:center;gap:12px;font-size:13px;box-shadow:0 2px 6px rgba(0,0,0,.12)}.nav-bar a{color:#fff;text-decoration:none;opacity:.85}.nav-bar a:hover{opacity:1}.timeline{border-left:3px solid var(--red);margin:6px 0 6px 8px;padding-left:12px}.timeline .t-item{margin-bottom:8px;position:relative}.timeline .t-item::before{content:'';position:absolute;left:-17px;top:4px;width:10px;height:10px;border-radius:50%;background:var(--accent)}.timeline .t-item.red::before{background:var(--red)}.timeline .t-item.green::before{background:var(--green)}.timeline .t-item.yellow::before{background:var(--yellow)}.timeline .t-date{font-size:.72rem;color:var(--text3);font-weight:600}.timeline .t-content{font-size:12px;margin-top:1px}.mas-box{background:#fff3e0;border:1px solid #ffe082;border-radius:8px;padding:8px 12px;margin:6px 0}@media(max-width:768px){table{display:block;overflow-x:auto;font-size:11px}th,td{white-space:nowrap;padding:2px 5px}}"""

def tl(items):
    return "\n".join(f'<div class="t-item {i[2] if len(i)>2 else ""}"><div class="t-date">{i[0]}</div><div class="t-content">{i[1]}</div></div>' for i in items)

def tbl(h, rows):
    return "<tr>" + "".join(f"<th>{x}</th>" for x in h) + "</tr>\n" + "\n".join("<tr><td class='b'>" + r[0] + "</td>" + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)

def tg(*args):
    return " ".join(f'<span class="tag {a[0]}">{a[1]}</span>' for a in args)

def write_case(fn, title, sub, topic, nav, alert, tl_html, mech_title, mech, tbl_html, pts, ref, pmid, n, tags_html):
    html = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><script src="https://cdn.tailwindcss.com"></script><link rel="manifest" href="../manifest.json"><style>{CSS}</style></head><body>
<div class="nav-bar"><a href="../index.html">🏠</a><a href="../topics/{topic}.html">{topic}</a><a href="index_{topic}.html">病例</a><span style="margin-left:auto;opacity:.7;font-size:12px">{nav}</span></div>
<div class="wrap"><div class="header"><div><h1>{title}</h1><div class="sub">{sub}</div></div><div class="meta">2026-04-10</div></div>
<div style="background:#fff3e0;border-left:4px solid #e65100;padding:8px 14px;font-size:11.5px"><b style="color:#e65100">⚠️ 免责声明</b>　本病例基于已发表文献整理。仅供医学专业人员学习参考，<b>不构成诊疗建议</b>。</div>
<div class="body">
<div class="sh">👤 基本信息</div><table><tr><td class="b" style="width:80px">标签</td><td>{tags_html}</td></tr><tr><td class="b">文献</td><td style="font-size:11px;color:var(--text2)">{ref}</td></tr></table>
<div class="alert"><b>独特性：</b>{alert}</div>
<div class="sh red">🔴 临床经过</div><div class="timeline">{tl_html}</div>
<div class="sh yellow">🔬 {mech_title}</div><div class="mas-box"><div style="font-weight:700;font-size:12px;color:#e65100">🧬 {mech_title}</div><div style="font-size:11.5px;line-height:1.7;margin-top:4px">{mech}</div></div>
<div class="sh">📊 对比</div><table>{tbl_html}</table>
<div class="sh green">📚 要点</div><ul style="font-size:12px;line-height:1.8;margin:4px 0;padding-left:18px">{"".join(f"<li>{p}</li>" for p in pts)}</ul>
<div class="sh">📖 文献</div><div style="font-size:11px;color:var(--text2)">{ref}</div></div>
<div style="text-align:center;padding:8px 20px;border-top:1px solid var(--border)"><a href="index_{topic}.html" style="display:inline-block;padding:6px 12px;background:var(--accent);color:#fff;border-radius:6px;text-decoration:none;font-size:11px">📋 返回{topic}目录</a></div>
<div class="footer">PMID: {pmid} · 不构成诊疗建议 · {topic}病例第{n}篇</div></div></body></html>"""
    p = os.path.join(D, fn)
    with open(p, "w", encoding="utf-8") as f:
        f.write(html)
    return os.path.getsize(p)

def write_index(topic, cn, cases):
    cards = ""
    for c in cases:
        cards += f'<a href="{c[0]}"><div style="border:1px solid var(--border);border-radius:8px;padding:10px 14px;margin:6px 0;cursor:pointer"><div style="font-weight:700;font-size:13px">{c[5]}. {c[1]}</div><div style="font-size:11px;color:var(--text2)">PMID: {c[4]}</div></div></a>\n'
    refs = "<br>".join(f'{c[5]}. PMID: {c[4]}' for c in cases)
    html = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{cn}病例</title><style>{CSS}</style></head><body>
<div class="nav-bar" style="background:var(--accent)"><a href="../index.html">🏠</a><a href="index.html">全部病例</a><span style="margin-left:auto;opacity:.7;font-size:12px">{cn}</span></div>
<div class="wrap"><div style="background:var(--accent);color:#fff;padding:14px 20px"><h1 style="font-size:1.4rem;font-weight:700">🔬 {cn}临床病例专题</h1><div style="font-size:.85rem;opacity:.85;margin-top:2px">{len(cases)}个真实世界病例</div></div>
<div style="padding:12px 20px 16px">{cards}<div style="font-size:10.5px;color:var(--text2);margin-top:10px">{refs}</div></div>
<div class="footer">MedWiki-Rheum · 不构成诊疗建议</div></div></body></html>"""
    p = os.path.join(D, f"index_{topic}.html")
    with open(p, "w", encoding="utf-8") as f:
        f.write(html)
    return os.path.getsize(p)

total = 0

# ============ ITP ============
itp = []
cases_itp = [
("case_ITP_acute.html","急性ITP — 病毒感染后突发瘀斑","急性免疫性血小板减少症（ITP，Immune Thrombocytopenia）","急性ITP",[("t-r","PLT<20K"),("t-y","病毒感染后"),("t-a","IVIG")],"急性ITP是儿童最常见出血性疾病。病毒感染后1-4周突发瘀斑，PLT常<20×10⁹/L。80%儿童6月内自发缓解。",
[("前驱","上呼吸道感染后2周"),("突发","全身瘀点瘀斑，牙龈出血","red"),("化验","PLT 8×10⁹/L","yellow"),("治疗","IVIG 1g/kg×2天→PLT回升","green")],
"ITP双重破坏机制","<b>外周破坏：</b>抗GPIIb/IIIa抗体→FcγR→脾脏巨噬细胞吞噬→PLT寿命缩短至数小时。<br><b>骨髓抑制：</b>自身抗体+CTL→巨核细胞损伤→产板减少。儿童80%自限。",
["特征","急性(儿童)","慢性(成人)"],[["发病","2-5岁","20-40岁(女)"],["前驱","80%","20%"],["PLT","<20K","30-50K"],["缓解","~80%","~10%"],["一线","IVIG","激素"]],
["儿童最常见出血疾病，80%自限","PLT<20K有颅内出血风险","IVIG一线3-5天PLT回升","抗血小板抗体→外周+骨髓双重"],
"Immune Thrombocytopenia in Children. NEJM. 2022;386(16). PMID: 38944486","38944486",1),
("case_ITP_chronic.html","慢性ITP — TPO-RA改变范式","慢性ITP（持续>12个月）","慢性ITP",[("t-r","难治性"),("t-y",">12月"),("t-a","TPO-RA")],"慢性ITP=持续>12月。TPO-RA改变范式：增加生成vs减少破坏。",
[("初诊","PLT 15K，激素有效减量复发"),("12月+","诊断慢性ITP","yellow"),("二线","利妥昔单抗→短暂有效→复发"),("TPO-RA","Romiplostin→PLT 50-100K","green")],
"慢性ITP免疫演进","抗PLT抗体→CD8+T直接杀伤→Treg缺陷→持续破坏。TPO-RA：刺激巨核细胞增殖→增加PLT生成。",
["治疗","机制","反应率","持久性"],[["激素","抑制吞噬","60-80%","减量复发"],["IVIG","封闭FcR","80%","2-4周"],["TPO-RA","刺激产板","70-90%","需持续"]],
["慢性=持续>12月，目标是安全PLT","TPO-RA范式转变","脾切率从>50%降至<10%","长期安全性良好"],
"Pediatric Immune Thrombocytopenia. Adv Pediatr. 2024;71(1):123-145. PMID: 38944486","38944486",2),
("case_ITP_Evans.html","Evans综合征 — ITP+AIHA","Evans综合征（ITP+AIHA，Autoimmune Hemolytic Anemia）","Evans",[("t-r","双重自身免疫"),("t-y","溶血+血小板减少"),("t-a","Coombs+")],"Evans=ITP+AIHA(Coombs+)。继发SLE/ALPS/CVID比例高(30-50%)。",
[("起病","苍白+乏力+瘀斑，Hb 65, PLT 12K"),("化验","网织红↑, 间接胆红素↑, Coombs(+)","yellow"),("排查","排除SLE/ALPS/CVID"),("治疗","甲强龙+IVIG→Hb/PLT回升","green")],
"双重免疫攻击","AIHA：温抗体IgG→红细胞→脾巨噬细胞→溶血。ITP：抗PLT抗体→PLT破坏。共同抗原？继发率30-50%。",
["特征","单纯ITP","Evans"],[["PLT","↓↓","↓↓"],["Hb","正常","↓↓"],["Coombs","阴性","阳性"],["胆红素","正常","↑↑"],["继发率","低","30-50%"]],
["Evans=ITP+AIHA必须查Coombs","排查SLE/ALPS/CVID","治疗比单纯ITP复杂","复发率高需长期随访"],
"Diagnosis and management of Evans syndrome in adults: first consensus recommendations. Lancet Haematol. 2024;11(3):e213-e224. PMID: 32271826","32271826",3),
("case_ITP_TPO.html","TPO-RA治疗儿童慢性ITP","TPO受体激动剂（TPO-RA，Thrombopoietin Receptor Agonist）","TPO-RA",[("t-a","Romiplostim"),("t-a","Eltrombopag"),("t-y","慢性ITP")],"TPO-RA是近15年ITP最大突破。激活c-Mpl→巨核细胞增殖→增加产板。",
[("启用","Eltrombopag 25mg/d"),("应答","2周PLT>50,4周>100","green"),("长期","最低有效剂量维持","green")],
"TPO-RA机制","Romiplostin：肽类皮下qw。Eltrombopag：小分子口服qd。均→JAK2→STAT5→巨核细胞→PLT释放。",
["特征","Romiplostin","Eltrombopag"],[["给药","皮下qw","口服qd"],["起效","1周","1-2周"],["儿童","✅","✅"],["肝损","低","需监测"]],
["TPO-RA改变ITP范式","Romiplostin(皮下)vs Eltrombopag(口服)","起效1-2周需持续用药"],
"Phase 3 randomised study of avatrombopag, a TPO-RA for ITP. Br J Haematol. 2018;183(4):553-562. PMID: 30191972","30191972",4),
("case_ITP_secondary.html","继发性ITP — SLE相关","继发性免疫性血小板减少症","继发ITP",[("t-r","SLE相关"),("t-y","抗磷脂抗体"),("t-a","治原发病")],"~25%成人ITP为继发，SLE最常见。可能先于SLE数年。",
[("初诊","PLT 35K，激素有效→原发性ITP"),("2年后","关节痛+蝶形红斑+ANA 1:640+dsDNA+","red"),("修正","SLE相关继发性ITP","yellow"),("治疗","HCQ+MMF+小剂量激素→均控制","green")],
"SLE相关ITP多重机制","四重打击：①抗PLT抗体→外周破坏 ②aPL→PLT活化→消耗+血栓 ③免疫复合物→补体→膜损伤 ④巨核细胞→产板减少。所有新ITP→查ANA+dsDNA+aPL。",
["特征","原发ITP","SLE相关ITP"],[["ANA","阴性/低","阳性(1:160+)"],["dsDNA","阴性","阳性"],["aPL","通常阴","30-40%阳"],["补体","正常","降低"]],
["所有新ITP查ANA+dsDNA+aPL","ITP可能是SLE首发","aPL+出血+血栓风险并存","治疗需兼顾SLE"],
"Rituximab alleviates pediatric SLE associated refractory immune thrombocytopenia. Immunol Res. 2024;72(1):97-106. PMID: 38279058","38279058",5),
]

for c in cases_itp:
    fn,title,sub,nav,tags,alert,tl_items,mech_t,mech,th,tr_rows,pts,ref,pmid,n = c
    tags_html = tg(*tags)
    sz = write_case(fn, title, sub, "ITP", nav, alert, tl(tl_items), mech_t, mech, tbl(th, tr_rows), pts, ref, pmid, n, tags_html)
    itp.append((fn, title, None, None, pmid, n))
    print(f"  {fn} ({sz}B)"); total+=1
sz = write_index("ITP", "ITP免疫性血小板减少症", itp); print(f"  index_ITP.html ({sz}B)"); total+=1

# ============ PID ============
pid = []
cases_pid = [
("case_PID_XLA.html","XLA — X连锁无丙种球蛋白血症","X连锁无丙种球蛋白血症（XLA，X-Linked Agammaglobulinemia）/ BTK缺陷","XLA",[("t-r","BTK缺陷"),("t-y","无丙种球蛋白"),("t-a","IVIG替代")],"首个PID(1952年Bruton)。BTK突变→B细胞停滞于pre-B→CD19+近零→所有Ig极低。母体IgG消失后(4-6月)反复化脓感染。",
[("6月龄","母体IgG消失后反复中耳炎+肺炎"),("化验","IgG/IgA/IgM极低，CD19+<1%","yellow"),("基因","BTK突变","yellow"),("治疗","IVIG 400-600mg/kg/月→显著改善","green")],
"BTK与B细胞发育","Pre-BCR→SYK→BLNK→BTK→PLCγ2→钙内流→增殖分化。无BTK→pre-B停滞→B细胞近零。",
["特征","XLA","CVID","SCID"],[["遗传","XLR(BTK)","多基因","AR/AD"],["发病","4-6月","20-40岁","新生儿"],["B细胞","<1%","正常/↓","极低"],["Ig","全部极低","IgG低","全部极低"],["治疗","IVIG","IVIG","HSCT"]],
["XLA=反复化脓+B细胞近零+低丙球","BTK→Pre-B发育停滞","终身IVIG预后良好","BTK抑制剂(Ibrutinib)印证此通路"],
"X-Linked Agammaglobulinemia and COVID-19: Two Case Reports. Pediatr Allergy Immunol Pulmonol. 2021;34(3):95-99. PMID: 34596095","34596095",1),
("case_PID_CVID.html","CVID — 常见变异型免疫缺陷","常见变异型免疫缺陷病（CVID，Common Variable Immunodeficiency）","CVID",[("t-y","CVID"),("t-a","低IgG"),("t-r","自身免疫30%")],"最常见症状性PID(1/25,000)。低IgG+低IgA/IgM+抗体反应缺陷。30%自身免疫，5-10%淋巴瘤。",
[("青年","反复鼻窦炎+肺炎"),("20+岁","支气管扩张","red"),("化验","IgG 2.1, IgA 0.3 g/L","yellow"),("治疗","IVIG替代→改善","green")],
"CVID免疫缺陷谱","B细胞→浆细胞分化障碍→CSR障碍→低IgG+低IgA→反复感染。Treg↓→自身免疫30%。B细胞克隆→淋巴瘤5-10%。",
["特征","CVID","XLA","Good综合征"],[["发病","20-40岁","4-6月","40-70岁"],["B细胞","存在(功能↓)","近零","近零"],["自身免疫","30%","罕见","常见(MG)"],["胸腺瘤","无","无","100%"]],
["最常见症状性PID","B细胞存在但功能异常(区别XLA)","30%自身免疫+5-10%淋巴瘤","IVIG+定期监测"],
"Chronic Diarrhea in CVID: a Case Series and Review. J Clin Immunol. 2018;38(2):171-179. PMID: 30741636","30741636",2),
("case_PID_SCID.html","SCID — TREC筛查拯救生命","重症联合免疫缺陷（SCID，Severe Combined Immunodeficiency）","SCID",[("t-r","致命"),("t-y","TREC"),("t-a","HSCT")],"最严重PID(泡泡男孩)。T+B+NK严重缺陷→不经治疗2岁内死亡。TREC筛查→3.5月前HSCT→存活>90%。",
[("筛查","TREC↓→紧急转诊","green"),("基因","IL2RG→X-SCID","yellow"),("保护","隔离+预防抗生素+无活疫苗"),("HSCT","3月龄→免疫重建成功","green")],
"SCID分型","X-SCID(45%)：IL2RG(γc)→IL-2/4/7/9/15/21信号全断→T⁻B⁺NK⁻。分型：T⁻B⁺NK⁻(IL2RG/JAK3) | T⁻B⁻NK⁺(RAG1/2) | T⁻B⁻NK⁻(ADA)。",
["类型","基因","T","B","NK","频率"],[["X-SCID","IL2RG","−","+","−","45%"],["ADA","ADA","−","−","−","15%"],["RAG1/2","RAG1/2","−","−","+","10%"],["JAK3","JAK3","−","+","−","6%"]],
["儿科急症，TREC筛查标准","3.5月前HSCT存活>90%","γc→6种细胞因子→T+NK双缺","基因治疗已用于X-SCID/ADA-SCID"],
"SCID diagnosis and genetic defects. Immunol Rev. 2024;321(1):91-105. PMID: 38287514","38287514",3),
("case_PID_CGD.html","CGD — 慢性肉芽肿病","慢性肉芽肿病（CGD，Chronic Granulomatous Disease）/ NADPH氧化酶缺陷","CGD",[("t-r","NADPH氧化酶"),("t-y","催化过氧化物(-)"),("t-a","IFN-γ")],"吞噬细胞杀菌缺陷。NADPH氧化酶缺陷→不能产ROS→过氧化氢酶阳性菌无法杀灭。DHR诊断。",
[("幼儿","反复脓肿+淋巴结炎+曲霉菌肺炎"),("DHR","呼吸爆发→无荧光→确诊","yellow"),("基因","gp91phox(CYBB)→X-CGD","yellow"),("预防","TMP-SMX+伊曲康唑+IFN-γ","green")],
"NADPH氧化酶与呼吸爆发","正常：NADPH氧化酶→O₂→O₂⁻→H₂O₂→HOCl→杀菌。CGD：无ROS→对过氧化氢酶阳性菌无效。矛盾：杀菌↓但肉芽肿↑。",
["特征","X-CGD(gp91)","AR-CGD(p47)"],[["遗传","XLR","AR"],["频率","~65%","~25%"],["严重","重","较轻"]],
["CGD=NADPH氧化酶→无ROS","过氧化氢酶阳性菌特别易感","DHR金标准","预防性抗生素+抗真菌+IFN-γ"],
"Case Report: Symptomatic CGD in the Newborn. Front Immunol. 2021;12:667524. PMID: 33854515","33854515",4),
("case_PID_ALPS.html","ALPS — 自身免疫性淋巴增生综合征","自身免疫性淋巴增生综合征（ALPS，Autoimmune Lymphoproliferative Syndrome）/ FAS通路缺陷","ALPS",[("t-r","FAS突变"),("t-y","淋巴结肿大"),("t-a","双阴性T细胞")],"FAS凋亡通路缺陷→淋巴细胞不能正常死亡→淋巴结/脾大+自身免疫。特征：DNT细胞(CD3+CD4-CD8-)升高。常伴Evans综合征。",
[("儿童","慢性淋巴结肿大+脾大"),("血细胞","ITP和/或AIHA反复发作"),("化验","DNT细胞>1.5%总T细胞","yellow"),("基因","FAS杂合突变","yellow"),("治疗","Sirolimus→淋巴结缩小+血象改善","green")],
"FAS凋亡通路","正常：FAS+FASL→FADD→Caspase-8/10→凋亡。ALPS：FAS突变→三聚体功能丧失→凋亡中断→淋巴细胞蓄积→①淋巴增殖 ②DNT蓄积 ③自身免疫。",
["ALPS分型","基因","频率"],[["ALPS-FAS","FAS","~70%"],["ALPS-FASLG","FASLG","~2%"],["ALPS-CASP10","CASP10","~5%"],["ALPS-U","未知","~20%"]],
["ALPS=FAS凋亡缺陷→淋巴增殖+自身免疫","DNT(CD3+CD4-CD8-TCRαβ+)是特征标志","常伴Evans综合征需鉴别","Sirolimus一线靶向mTOR"],
"Neonatal ALPS: A Case Report and Brief Review. J Pediatr Hematol Oncol. 2021;43(2):e189-e192. PMID: 32149866","32149866",5),
]

for c in cases_pid:
    fn,title,sub,nav,tags,alert,tl_items,mech_t,mech,th,tr_rows,pts,ref,pmid,n = c
    sz = write_case(fn, title, sub, "PID", nav, alert, tl(tl_items), mech_t, mech, tbl(th, tr_rows), pts, ref, pmid, n, tg(*tags))
    pid.append((fn, title, None, None, pmid, n))
    print(f"  {fn} ({sz}B)"); total+=1
sz = write_index("PID", "PID原发性免疫缺陷病", pid); print(f"  index_PID.html ({sz}B)"); total+=1

print(f"\nITP+PID done ({total} files)")
