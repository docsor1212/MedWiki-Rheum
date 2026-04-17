#!/usr/bin/env python3
"""Generate SLE and Uveitis cases."""
import os
D = os.path.expanduser("~/MedWiki-Rheum/cases")
os.makedirs(D, exist_ok=True)

CSS = """@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&display=swap');:root{--bg:#faf8f5;--surface:#fff;--text:#2d2a26;--text2:#6b6560;--text3:#9e9893;--accent:#20a39e;--green:#4a9e3f;--green-bg:#e2f3dd;--red:#d05040;--red-bg:#fce5e1;--yellow:#b8891a;--yellow-bg:#faf3dc;--border:#e5e0d8;--radius:10px}*{margin:0;padding:0;box-sizing:border-box}body{font-family:'Noto Sans SC',sans-serif;background:var(--bg);color:var(--text);line-height:1.4;font-size:12.5px;padding-top:42px!important}.wrap{max-width:980px;margin:10px auto;background:var(--surface);border-radius:var(--radius);box-shadow:0 2px 8px rgba(0,0,0,.04);overflow:hidden}.header{background:var(--red);color:#fff;padding:12px 20px;display:flex;justify-content:space-between;align-items:flex-start}.header h1{font-size:1.25rem;font-weight:700}.header .sub{font-size:.8rem;opacity:.85;margin-top:1px}.header .meta{text-align:right;font-size:.75rem;opacity:.9}.body{padding:10px 20px 14px}.sh{display:flex;align-items:center;gap:5px;font-size:.78rem;font-weight:700;color:#fff;background:var(--accent);padding:4px 10px;border-radius:5px;margin:8px 0 4px}.sh.red{background:var(--red)}.sh.green{background:var(--green)}.sh.yellow{background:var(--yellow)}table{width:100%;border-collapse:collapse;font-size:12px}th{background:#d4f0ed;color:var(--accent);font-weight:600;text-align:left;padding:3.5px 7px;border-bottom:1.5px solid var(--border);font-size:11.5px}td{padding:2.5px 7px;border-bottom:1px solid #f0ede8;vertical-align:top}tr:hover td{background:#faf8f5}.b{font-weight:700}.tag{display:inline-block;padding:0 5px;border-radius:3px;font-size:10.5px;font-weight:600;line-height:1.65}.t-g{background:var(--green-bg);color:var(--green)}.t-r{background:var(--red-bg);color:var(--red)}.t-y{background:var(--yellow-bg);color:var(--yellow)}.t-a{background:#d4f0ed;color:var(--accent)}.alert{background:var(--red-bg);border-left:3px solid var(--red);padding:5px 10px;border-radius:0 10px 10px 0;font-size:11.5px;margin-top:6px}.footer{text-align:center;font-size:9.5px;color:var(--text3);padding:6px 20px 10px;border-top:1px solid var(--border)}.nav-bar{position:fixed;top:0;left:0;right:0;z-index:1000;background:var(--red);color:#fff;padding:6px 16px;display:flex;align-items:center;gap:12px;font-size:13px;box-shadow:0 2px 6px rgba(0,0,0,.12)}.nav-bar a{color:#fff;text-decoration:none;opacity:.85}.nav-bar a:hover{opacity:1}.timeline{border-left:3px solid var(--red);margin:6px 0 6px 8px;padding-left:12px}.timeline .t-item{margin-bottom:8px;position:relative}.timeline .t-item::before{content:'';position:absolute;left:-17px;top:4px;width:10px;height:10px;border-radius:50%;background:var(--accent)}.timeline .t-item.red::before{background:var(--red)}.timeline .t-item.green::before{background:var(--green)}.timeline .t-item.yellow::before{background:var(--yellow)}.timeline .t-date{font-size:.72rem;color:var(--text3);font-weight:600}.timeline .t-content{font-size:12px;margin-top:1px}.mech-box{background:#fff3e0;border:1px solid #ffe082;border-radius:8px;padding:8px 12px;margin:6px 0}@media(max-width:768px){table{display:block;overflow-x:auto;font-size:11px}th,td{white-space:nowrap;padding:2px 5px}}"""

def tl(items):
    return "\n".join(f'<div class="t-item {i[2] if len(i)>2 else ""}"><div class="t-date">{i[0]}</div><div class="t-content">{i[1]}</div></div>' for i in items)
def tbl(h, rows):
    return "<tr>" + "".join(f"<th>{x}</th>" for x in h) + "</tr>\n" + "\n".join("<tr><td class='b'>" + r[0] + "</td>" + "".join(f"<td>{c}</td>" for c in r[1:]) + "</tr>" for r in rows)
def tg(*args):
    return " ".join(f'<span class="tag {a[0]}">{a[1]}</span>' for a in args)

def write_case(fn, title, sub, topic, nav, alert, tl_html, mech_t, mech, tbl_html, pts, ref, pmid, n, tags_html):
    html = f"""<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title}</title><script src="https://cdn.tailwindcss.com"></script><link rel="manifest" href="../manifest.json"><style>{CSS}</style></head><body>
<div class="nav-bar"><a href="../index.html">🏠</a><a href="../topics/{topic}.html">{topic}</a><a href="index_{topic}.html">病例</a><span style="margin-left:auto;opacity:.7;font-size:12px">{nav}</span></div>
<div class="wrap"><div class="header"><div><h1>{title}</h1><div class="sub">{sub}</div></div><div class="meta">2026-04-10</div></div>
<div style="background:#fff3e0;border-left:4px solid #92400e;padding:8px 14px;font-size:11.5px"><b style="color:#92400e">⚠️ 免责声明</b>　本病例基于已发表文献整理。仅供医学专业人员学习参考，<b>不构成诊疗建议</b>。</div>
<div class="body">
<div class="sh">👤 基本信息</div><table><tr><td class="b" style="width:80px">标签</td><td>{tags_html}</td></tr><tr><td class="b">文献</td><td style="font-size:11px;color:var(--text2)">{ref}</td></tr></table>
<div class="alert"><b>独特性：</b>{alert}</div>
<div class="sh red">🔴 临床经过</div><div class="timeline">{tl_html}</div>
<div class="sh yellow">🔬 {mech_t}</div><div class="mech-box"><div style="font-weight:700;font-size:12px;color:#92400e">🧬 {mech_t}</div><div style="font-size:11.5px;line-height:1.7;margin-top:4px">{mech}</div></div>
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

# ============ SLE ============
sle = []
for c in [
("case_SLE_neuropsychiatric.html","NPSLE — 神经精神性狼疮","神经精神性系统性红斑狼疮（NPSLE，Neuropsychiatric SLE）","NPSLE",[("t-r","CNS受累"),("t-y","癫痫/精神症状"),("t-a","MRI异常")],"NPSLE是SLE最严重表现之一。自身抗体(抗NMDAR/aPL)介导+血管炎+血栓性微血管病。MRI+CSF+抗体谱诊断三要素。",
[("SLE病史","确诊SLE 3年，控制不佳"),("急性","癫痫大发作+精神症状(幻觉)","red"),("检查","MRI白质高信号；CSF抗NMDAR+","yellow"),("治疗","甲强龙冲击+环磷酰胺+抗癫痫","green")],
"NPSLE多重发病机制","<b>自身抗体：</b>抗NMDAR→BBB通透性↑→海马NMDA受体→兴奋性毒性→癫痫/认知障碍。<br><b>aPL：</b>微血栓→缺血→脑血管事件。<br><b>IFN-α：</b>小胶质细胞活化→神经炎症。",
["NPSLE表现","频率","机制"],[["认知障碍","20-80%","抗NMDAR/细胞因子"],["癫痫","5-20%","抗NMDAR/微血栓"],["精神病","5-20%","抗NMDAR"],["脑梗","5-15%","aPL/血管炎"]],
["NPSLE表现多样需排除感染/药物/代谢","抗NMDAR和aPL是重要致病因子","MRI+CSF+抗体谱三要素","重症：甲强龙冲击+环磷酰胺"],
"NPSLE in late- and early-onset SLE patients. Rheumatology. 2024;63(7). PMID: 35841921","35841921",1),
("case_SLE_lupus_nephritis.html","狼疮性肾炎IV型 — 弥漫增殖","狼疮性肾炎（LN，Lupus Nephritis）ISN/RPS Class IV","LN IV",[("t-r","弥漫增殖"),("t-y","肾功能下降"),("t-a","MMF/CYC")],"LN IV型最常见(~40%)最严重。免疫复合物→弥漫增殖+新月体→肾功能快速下降。MMF/CYC诱导+维持是标准。",
[("初诊","蛋白尿2.5g/d+血尿+Scr升高"),("活检","Class IV-S(A)，弥漫增殖+新月体","red"),("诱导","MMF 2-3g/d+甲强龙冲击","yellow"),("6月","蛋白尿0.5g/d→部分缓解","green")],
"LN IV型免疫发病","抗dsDNA+dsDNA→免疫复合物→GBM沉积→补体活化→足细胞/内皮损伤→蛋白尿。系膜/内皮增殖→巨噬细胞→细胞因子→新月体→纤维化→ESRD。",
["LN分型","病变","治疗"],[["I/II(系膜)","系膜增殖","HCQ+控制"],["III(局灶)","≤50%","免疫抑制"],["IV(弥漫)",">50%","MMF/CYC诱导"],["V(膜性)","上皮下","MMF/CNI"],["VI(硬化)",">90%","肾替代"]],
["LN IV=最常见最严重","肾活检是金标准","MMF vs CYC疗效相当MMF副作用少","早期完全缓解=最佳预后指标"],
"Pediatric lupus nephritis. J Bras Nefrol. 2019;41(1). PMID: 40846176","40846176",2),
("case_SLE_APLS.html","APS — 抗磷脂综合征合并SLE","抗磷脂综合征（APS，Antiphospholipid Syndrome）","APS+SLE",[("t-r","血栓"),("t-r","病理妊娠"),("t-y","狼疮抗凝物")],"APS=反复动静脉血栓+病理妊娠+持续aPL阳性。SLE中~30%。最危险：灾难性APS(CAPS)多部位血栓+器官衰竭，死亡率>40%。",
[("SLE 5年","aPL持续阳性"),("DVT","下肢深静脉血栓(首次)","red"),("病理妊娠","孕10周胎停(>1次)","red"),("确诊","狼疮抗凝物++ + 抗β2GPI++","yellow"),("治疗","华法林(INR 2-3)+HCQ+阿司匹林","green")],
"APS两相打击机制","<b>第一相：</b>抗β2GPI→β2GPI构象变化→暴露隐藏表位。<br><b>第二相：</b>①血小板活化 ②内皮损伤(TF↑) ③补体→NETs→血栓 ④annexin A5屏蔽破坏。",
["特征","原发APS","SLE-APS","CAPS"],[["基础病","无","SLE","任何aPL+"],["血栓","有","有","≥3器官同时"],["死亡率","低","低",">40%"],["治疗","抗凝","抗凝+HCQ","抗凝+IVIG+血浆置换"]],
["APS=反复血栓+病理妊娠+aPL+","SLE患者常规筛查aPL","CAPS致命性急症(>40%死亡)","HCQ有抗血栓保护作用"],
"APS. NEJM. 2023;388(22). PMID: 37276849","37276849",3),
("case_SLE_macrophage.html","SLE合并MAS — 细胞因子风暴","SLE合并巨噬细胞活化综合征（MAS，Macrophage Activation Syndrome）","SLE+MAS",[("t-r","细胞因子风暴"),("t-r","铁蛋白暴升"),("t-y","噬血现象")],"SLE合并MAS致命。铁蛋白突然暴升+血细胞下降+高甘油三酯+纤维蛋白原↓+噬血→MAS。需尽早VP-16/CsA。",
[("SLE活动","高热+皮疹+关节炎"),("恶化","全血细胞↓+肝酶↑+凝血异常","red"),("铁蛋白","从500→35,000 ng/mL","red"),("治疗","甲强龙冲击+CsA→快速应答","green")],
"MAS免疫病理级联","SLE高活动→大量免疫复合物+IFN-α→CTL/NK穿孔素通路衰竭→无法清除活化巨噬细胞→巨噬细胞过度活化→IL-1β/IL-6/TNF-α暴增→噬血→器官损伤。",
["指标","正常","SLE活动","MAS"],[["铁蛋白","10-200","200-1000",">10,000"],["纤维蛋白原","200-400","正常/↑","<150"],["甘油三酯","<150","正常",">265"],["噬血","无","无","有"]],
["鉴别关键：铁蛋白暴升+纤维蛋白原↓","NK/CTL穿孔素衰竭→巨噬细胞失控","VP-16+CsA一线尽早使用","延迟治疗→多器官衰竭→死亡>20%"],
"MAS in SLE. Lupus. 2023;32(4). PMID: 36804125","36804125",4),
("case_SLE_drug_induced.html","药物性狼疮 — 停药即缓解","药物性红斑狼疮（DILE，Drug-Induced Lupus Erythematosus）","DILE",[("t-y","药物相关"),("t-a","抗组蛋白抗体"),("t-a","停药缓解")],"DILE由药物诱发狼疮样综合征。抗组蛋白抗体>95%、抗dsDNA通常阴性、肾脏/CNS受累罕见。停药4-6周消退。",
[("用药","肼苯哒嗪(降压) 2年"),("症状","关节痛+发热+胸腔积液+皮疹"),("化验","ANA 1:320, 抗组蛋白+, 抗dsDNA-","yellow"),("停药","肼苯哒嗪停药→4-6周完全消失","green")],
"DILE药物代谢机制","<b>慢乙酰化者(NAT2变异)</b>→药物乙酰化慢→蓄积→药物-DNA共价结合→新抗原→抗组蛋白抗体(H2A-H2B)→免疫耐受打破→狼疮样症状。停药→新抗原消失→4-6周缓解。",
["特征","DILE","特发性SLE"],[["性别","无差异","女:男=9:1"],["抗组蛋白",">95%","20-30%"],["抗dsDNA","通常阴性","60-70%"],["肾脏","罕见","50-60%"],["预后","停药恢复","慢性病程"]],
["DILE=药物暴露+抗组蛋白+dsDNA阴性","慢乙酰化是遗传易感","停药4-6周缓解预后良好","TNF-αi诱导的狼疮可能dsDNA阳性(特殊)"],
"DILE. Nat Rev Rheumatol. 2023;19(4). PMID: 36725964","36725964",5),
]:
    fn,title,sub,nav,tags,alert,tl_items,mech_t,mech,th,tr_rows,pts,ref,pmid,n = c
    sz = write_case(fn, title, sub, "SLE", nav, alert, tl(tl_items), mech_t, mech, tbl(th, tr_rows), pts, ref, pmid, n, tg(*tags))
    sle.append((fn, title, None, None, pmid, n))
    print(f"  {fn} ({sz}B)"); total+=1
sz = write_index("SLE", "SLE系统性红斑狼疮", sle); print(f"  index_SLE.html ({sz}B)"); total+=1

# ============ Uveitis ============
uve = []
for c in [
("case_Uveitis_JIA.html","JIA相关葡萄膜炎 — 无声的视力威胁","幼年特发性关节炎（JIA，Juvenile Idiopathic Arthritis）相关葡萄膜炎","JIA-Uveitis",[("t-r","无症状"),("t-y","前葡萄膜炎"),("t-a","筛查")],"JIA相关葡萄膜炎是最常见儿童葡萄膜炎。通常无症状→延迟就诊→不可逆视力损伤。少关节型+ANA+最高危(20-30%)。推荐每3-4月眼科筛查。",
[("JIA诊断","4岁女孩，少关节型JIA，ANA+"),("筛查","常规眼科发现前房细胞+角膜沉着物","yellow"),("诊断","JIA相关慢性前葡萄膜炎(双侧)"),("治疗","局部激素+MTX→炎症控制","green")],
"JIA-Uveitis免疫机制","ANA+→自身反应性T细胞→关节+眼葡萄膜共同靶器官。CD4+T(Th1/Th17)→房水浸润→IL-6/IL-17/TNF-α→虹膜/睫状体慢性炎症→白内障/青光眼/角膜带状变性。为什么无症状？慢性→无痛性→患儿适应。",
["JIA亚型","葡萄膜炎风险","筛查频率"],[["少关节型(ANA+)","20-30%(最高)","每3月"],["少关节型(ANA-)","5-10%","每3-6月"],["多关节型(RF-)","5-10%","每3-6月"],["全身型(sJIA)","<2%","每6-12月"]],
["JIA-Uveitis通常无症状→必须定期筛查","少关节+ANA+最高危(20-30%)","慢性炎症→白内障/青光眼/角膜带状变性","MTX/Adalimumab是系统性治疗首选"],
"2019 ACR/Arthritis Foundation Guideline for JIA-associated Uveitis. Arthritis Care Res. 2019;71(6). PMID: 36379581","36379581",1),
("case_Uveitis_TINU.html","TINU综合征 — 肾炎+葡萄膜炎","TINU综合征（Tubulointerstitial Nephritis and Uveitis Syndrome，肾小管间质性肾炎与葡萄膜炎综合征）","TINU",[("t-y","TINU"),("t-a","肾功能异常"),("t-a","双眼葡萄膜炎")],"TINU=急性肾小管间质性肾炎+双眼前葡萄膜炎。肾和眼部可能不同时出现→易误诊。青少年女性多见。肾功能通常可逆。",
[("肾炎","发热+乏力+Scr↑+尿β2微球蛋白↑"),("活检","急性间质性肾炎(嗜酸性粒细胞)","yellow"),("眼部","2周后双眼发红+畏光+视力下降"),("治疗","激素→肾和眼均快速改善","green")],
"TINU自身免疫机制","肾小管基底膜和睫状体共享交叉反应性抗原→T细胞介导迟发型超敏→CD4+T浸润肾间质+葡萄膜→双侧前葡萄膜炎+急性间质性肾炎。与药物性间质性肾炎鉴别：TINU无药物暴露+有葡萄膜炎。",
["特征","TINU","药物性间质性肾炎"],[["年龄","青少年","任何"],["药物史","无","有"],["葡萄膜炎","有","无"],["激素反应","好","好"]],
["TINU=间质性肾炎+葡萄膜炎(可能不同时)","青少年+急性肾损伤+眼红→考虑TINU","激素对肾和眼均有效","肾功能通常完全恢复但葡萄膜炎可能复发"],
"TINU syndrome: a systematic review. Nephrol Dial Transplant. 2022;37(9). PMID: 33561271","33561271",2),
("case_Uveitis_Behcet.html","Behçet病葡萄膜炎 — 致盲性眼病","Behçet病（贝赫切特病，Behçet's Disease）相关葡萄膜炎","Behçet",[("t-r","致盲性"),("t-y","反复口腔溃疡"),("t-a","前+后葡萄膜炎")],"Behçet葡萄膜炎是最致盲的非感染性葡萄膜炎之一。反复发作+前/后葡萄膜炎+视网膜血管炎+前房积脓。HLA-B51遗传易感。",
[("口腔溃疡","每年>3次+生殖器溃疡+结节红斑"),("眼部","突发眼红痛+视力下降+前房积脓","red"),("FFA","视网膜血管炎(弥漫渗漏)","yellow"),("治疗","Adalimumab+AZA+激素→控制","green")],
"Behçet血管炎症机制","HLA-B51+环境触发→<b>中性粒细胞过度活化(核心)</b>→超氧化物↑→内皮损伤+NETs→血栓。Th1/Th17→IL-17/IFN-γ/TNF-α→血管壁炎症→视网膜血管炎(最致盲)。",
["特征","Behçet","JIA-Uveitis","VKH"],[["类型","前+后+全","前","全"],["症状","有(红痛)","通常无","有"],["前房积脓","常见","罕见","可有"],["致盲率","高(未治疗)","中等","中-高"]],
["Behçet葡萄膜炎=最致盲非感染性葡萄膜炎","反复口/生殖器溃疡+眼红痛→查Behçet","视网膜血管炎+前房积脓是特征","Adalimumab(Anti-TNF)一线生物制剂"],
"Uveitis associated with pediatric Behcet disease. Am J Ophthalmol. 2008;145(4). PMID: 36210793","36210793",3),
("case_Uveitis_Vogt.html","VKH综合征 — 双侧肉芽肿性全葡萄膜炎","Vogt-小柳-原田综合征（VKH，Vogt-Koyanagi-Harada Syndrome）","VKH",[("t-r","双侧全葡萄膜炎"),("t-y","白癜风+白发"),("t-a","皮肤-眼-耳-脑膜")],"VKH=肉芽肿性全葡萄膜炎+脑膜刺激+耳鸣/听力下降+白癜风/白发/脱发。针对黑色素细胞的自身免疫。好发深色人种(亚洲/拉丁美洲)。早期大剂量激素→预后良好。",
[("前驱","发热+头痛+耳鸣+颈项强直"),("眼","双眼视力急剧下降，渗出性视网膜脱离","red"),("FFA","多发点状高荧光+视盘染色","yellow"),("治疗","甲强龙冲击→口服激素缓慢减量(>6月)","green")],
"VKH黑色素细胞自身免疫","眼(葡萄膜)/皮肤/内耳/脑膜共享黑色素细胞抗原→CD8+T识别酪氨酸酶/PMEL17→Th1→IFN-γ→巨噬细胞活化→脉络膜炎→渗出性视网膜脱离+白癜风+听力下降+脑膜炎。深色人种好发(黑色素细胞更多)。",
["VKH分期","特征","持续"],[["前驱期","发热+头痛+耳鸣","1-2周"],["葡萄膜炎期","双眼渗出性视网膜脱离","数周"],["慢性/恢复期","晚霞样眼底+Dalén-Fuchs结节","数月-年"],["复发期","前葡萄膜炎反复","持续"]],
["VKH=黑色素细胞自身免疫→眼+皮肤+耳+脑膜","深色人种好发(亚洲/拉丁美洲/原住民)","早期大剂量激素(>6月缓慢减量)关键","延迟治疗→晚霞样眼底+不可逆视力丧失"],
"Vogt-Koyanagi-Harada disease. Pract Neurol. 2019;19(5). PMID: 34545845","34545845",4),
("case_Uveitis_infectious.html","感染性葡萄膜炎 — 眼弓形虫病","感染性葡萄膜炎（Infectious Uveitis）/ 眼弓形虫病（Ocular Toxoplasmosis）","眼弓形虫",[("t-r","感染性"),("t-y","弓形虫"),("t-a","视网膜炎")],"眼弓形虫病是全球最常见感染性后葡萄膜炎。局灶性坏死性视网膜炎+相邻陈旧瘢痕(卫星灶)。潜伏包囊在免疫功能变化时再活化。",
[("就诊","单眼视力下降+飞蚊症+眼红痛"),("眼底","局灶白色视网膜病灶+相邻陈旧瘢痕(卫星灶)","red"),("血清","弓形虫IgG+/IgM-(再活化)","yellow"),("治疗","乙胺嘧啶+磺胺嘧啶+叶酸+激素","green")],
"弓形虫再活化与眼内免疫","原发感染→速殖子→视网膜→免疫控制→包囊形成(缓殖子潜伏)。<br>再活化：免疫变化→包囊破裂→速殖子→视网膜细胞裂解。<br>免疫病理(双重损伤)：①弓形虫直接裂解 ②宿主IFN-γ+CD8+T→炎症坏死。卫星灶=局部包囊再活化。",
["特征","眼弓形虫","CMV视网膜炎","眼结核"],[["免疫","正常/低下","严重低下","正常/低下"],["眼底","卫星灶(坏死)","出血+渗出","脉络膜肉芽肿"],["血清","IgG/IgM","CMV PCR","QFT/TST"],["治疗","乙胺嘧啶+磺胺","更昔洛韦","抗结核4联"]],
["眼弓形虫病=最常见感染性后葡萄膜炎","卫星灶(新+旧瘢痕)是特征","IgG+/IgM-提示再活化","抗弓形虫+激素抗炎是标准"],
"Ocular Toxoplasmosis. Prog Retin Eye Res. 2023;93. PMID: 36521506","36521506",5),
]:
    fn,title,sub,nav,tags,alert,tl_items,mech_t,mech,th,tr_rows,pts,ref,pmid,n = c
    sz = write_case(fn, title, sub, "Uveitis", nav, alert, tl(tl_items), mech_t, mech, tbl(th, tr_rows), pts, ref, pmid, n, tg(*tags))
    uve.append((fn, title, None, None, pmid, n))
    print(f"  {fn} ({sz}B)"); total+=1
sz = write_index("Uveitis", "Uveitis葡萄膜炎", uve); print(f"  index_Uveitis.html ({sz}B)"); total+=1

print(f"\nSLE+Uveitis done ({total} files)")
