#!/usr/bin/env python3
"""Generate all remaining case HTML files + indexes."""
import os

CASES_DIR = os.path.expanduser("~/MedWiki-Rheum/cases")
os.makedirs(CASES_DIR, exist_ok=True)

CSS = """@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&display=swap');
:root{--bg:#faf8f5;--surface:#fff;--text:#2d2a26;--text2:#6b6560;--text3:#9e9893;--accent:#20a39e;--green:#4a9e3f;--green-bg:#e2f3dd;--red:#d05040;--red-bg:#fce5e1;--yellow:#b8891a;--yellow-bg:#faf3dc;--border:#e5e0d8;--radius:10px}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Noto Sans SC',sans-serif;background:var(--bg);color:var(--text);line-height:1.4;font-size:12.5px;padding-top:42px!important}
.wrap{max-width:980px;margin:10px auto;background:var(--surface);border-radius:var(--radius);box-shadow:0 2px 8px rgba(0,0,0,.04);overflow:hidden}
.header{background:var(--red);color:#fff;padding:12px 20px;display:flex;justify-content:space-between;align-items:flex-start}
.header h1{font-size:1.25rem;font-weight:700}
.header .sub{font-size:.8rem;opacity:.85;margin-top:1px}
.header .meta{text-align:right;font-size:.75rem;opacity:.9}
.body{padding:10px 20px 14px}
.sh{display:flex;align-items:center;gap:5px;font-size:.78rem;font-weight:700;color:#fff;background:var(--accent);padding:4px 10px;border-radius:5px;margin:8px 0 4px}
.sh.red{background:var(--red)}.sh.green{background:var(--green)}.sh.yellow{background:var(--yellow)}
table{width:100%;border-collapse:collapse;font-size:12px}
th{background:#d4f0ed;color:var(--accent);font-weight:600;text-align:left;padding:3.5px 7px;border-bottom:1.5px solid var(--border);font-size:11.5px}
td{padding:2.5px 7px;border-bottom:1px solid #f0ede8;vertical-align:top}
tr:hover td{background:#faf8f5}
.b{font-weight:700}
.tag{display:inline-block;padding:0 5px;border-radius:3px;font-size:10.5px;font-weight:600;line-height:1.65}
.t-g{background:var(--green-bg);color:var(--green)}.t-r{background:var(--red-bg);color:var(--red)}.t-y{background:var(--yellow-bg);color:var(--yellow)}.t-a{background:#d4f0ed;color:var(--accent)}
.alert{background:var(--red-bg);border-left:3px solid var(--red);padding:5px 10px;border-radius:0 10px 10px 0;font-size:11.5px;margin-top:6px}
.note{font-size:11px;color:var(--text2);margin-top:4px;padding-left:8px;border-left:2px solid var(--accent)}
.footer{text-align:center;font-size:9.5px;color:var(--text3);padding:6px 20px 10px;border-top:1px solid var(--border)}
.nav-bar{position:fixed;top:0;left:0;right:0;z-index:1000;background:var(--red);color:#fff;padding:6px 16px;display:flex;align-items:center;gap:12px;font-size:13px;box-shadow:0 2px 6px rgba(0,0,0,.12)}
.nav-bar a{color:#fff;text-decoration:none;opacity:.85}.nav-bar a:hover{opacity:1}
.timeline{border-left:3px solid var(--red);margin:6px 0 6px 8px;padding-left:12px}
.timeline .t-item{margin-bottom:8px;position:relative}
.timeline .t-item::before{content:'';position:absolute;left:-17px;top:4px;width:10px;height:10px;border-radius:50%;background:var(--accent)}
.timeline .t-item.red::before{background:var(--red)}.timeline .t-item.green::before{background:var(--green)}.timeline .t-item.yellow::before{background:var(--yellow)}
.timeline .t-date{font-size:.72rem;color:var(--text3);font-weight:600}
.timeline .t-content{font-size:12px;margin-top:1px}
.mas-box{background:#fff3e0;border:1px solid #ffe082;border-radius:8px;padding:8px 12px;margin:6px 0}
@media(max-width:768px){table{display:block;overflow-x:auto;font-size:11px}th,td{white-space:nowrap;padding:2px 5px}}"""

def mk_tags(tags):
    return " ".join(f'<span class="tag {t.split(":")[0]}">{t.split(":",1)[1]}</span>' for t in tags)

def mk_timeline(items):
    h = ""
    for item in items:
        cls = f' {item[2]}' if len(item)>2 else ''
        h += f'<div class="t-item{cls}"><div class="t-date">{item[0]}</div><div class="t-content">{item[1]}</div></div>\n'
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
        cards += f'<a href="{c["f"]}"><div style="border:1px solid var(--border);border-radius:8px;padding:10px 14px;margin:6px 0;cursor:pointer"><div style="font-weight:700;font-size:13px">{c["n"]}. {c["t"]}</div><div style="font-size:11px;color:var(--text2)">{c["pmid"]}</div></div></a>\n'
    return f'''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{cn}病例</title><style>{CSS}</style></head><body>
<div class="nav-bar" style="background:var(--accent)"><a href="../index.html">🏠</a><a href="index.html">全部病例</a><span style="margin-left:auto;opacity:.7;font-size:12px">{cn}</span></div>
<div class="wrap"><div style="background:var(--accent);color:#fff;padding:14px 20px"><h1 style="font-size:1.4rem;font-weight:700">🔬 {cn}临床病例专题</h1><div style="font-size:.85rem;opacity:.85;margin-top:2px">{len(cases)}个真实世界病例</div></div>
<div style="padding:12px 20px 16px">{cards}<div style="font-size:10.5px;color:var(--text2);margin-top:10px">{"<br>".join(f"{c["n"]}. PMID: {c["pmid"]}" for c in cases)}</div></div>
<div class="footer">MedWiki-Rheum · 不构成诊疗建议</div></div></body></html>'''

# ===== DATA =====
# Format: topic -> {cn, cases: [{f,t,sub,nav,tags,alert,tl,mech_t,mech,th,tr,pts,ref,pmid,n}, ...]}

DATA = {}

# --- AID (4 remaining, FMF already created) ---
DATA["AID"] = {"cn": "AID自身炎症性疾病", "cases": [
{"f":"case_AID_CAPS.html","t":"CAPS — Muckle-Wells综合征NLRP3 T348M","sub":"冷吡啉相关周期性发热综合征（CAPS，Cryopyrin-Associated Periodic Syndrome）","nav":"CAPS","tags":["t-r:NLRP3","t-y:CAPS","t-a:IL-1抑制剂"],"alert":"CAPS由NLRP3功能获得突变→Cryopyrin自激活→NLRP3炎症小体持续活化→IL-1β过度产生→荨麻疹+发热+关节痛。可进展为耳聋和淀粉样变。","tl":[("幼儿期","反复荨麻疹+低热+关节痛，受凉诱发"),("进展","感音神经性听力下降，ESR/CRP持续升高"),("基因","NLRP3 T348M突变确诊CAPS-MWS","yellow"),("治疗","Canakinumab → 症状完全缓解","green")],"mech_t":"NLRP3炎症小体与CAPS谱系","mech":"NLRP3突变→Cryopyrin自激活→炎症小体持续组装→IL-1β大量释放→全身炎症。<br><b>CAPS谱系：</b>FCAS(寒冷诱发,最轻) → MWS(本例,中度) → NOMID/CINCA(最重)","th":["特征","FCAS","MWS(本例)","NOMID/CINCA"],"tr":[["发病","寒冷诱发","自发/诱发","出生"],["荨麻疹","有","有","有"],["发热","低热","中热","持续高热"],["关节","关节痛","关节炎","骨增生"],["听力","正常","感音神经性聋","感音神经性聋"],["CNS","无","无/轻","脑膜炎/脑积水"]],"pts":["CAPS三型为NLRP3不同突变谱系","IL-1抑制剂(Canakinumab)靶向治疗显著","早期治疗预防不可逆损伤","NLRP3炎症小体是IL-1β核心平台"],"ref":"Muckle-Wells Syndrome: A Case Report with NLRP3 T348M Mutation. Pediatr Dermatol. 2016;33(5):e278-e280. PMID: 27435956","pmid":"27435956","n":2},
{"f":"case_AID_TRAPS.html","t":"TRAPS — TNFRSF1A R92P突变","sub":"TNF受体相关周期性发热综合征（TRAPS，TNF Receptor Associated Periodic Syndrome）","nav":"TRAPS","tags":["t-r:TNFRSF1A","t-y:TRAPS","t-a:低外显率"],"alert":"TRAPS由TNFRSF1A突变引起，本例R92P低外显率。核心：突变TNFR1错误折叠→ER应激→NF-κB→促炎因子。","tl":[("家族","两代六人反复发热+肌痛+浆膜炎"),("发作","持续>1周，移行性肌痛，眶周水肿"),("基因","TNFRSF1A R92P，sTNFR1降低","yellow"),("治疗","激素+Etanercept有效","green")],"mech_t":"TRAPS发病机制","mech":"突变TNFR1错误折叠→ER滞留→UPR/ER应激→ROS→NF-κB+MAPK→促炎因子(IL-6,IL-1β,TNFα)。R92P低外显率需第二信号。","th":["特征","FMF","TRAPS","CAPS"],"tr":[["遗传","AR(MEFV)","AD(TNFRSF1A)","AD(NLRP3)"],["发作","1-3天",">1周","持续"],["皮疹","丹毒样","移行性斑丘疹","荨麻疹"],["浆膜炎","突出","有","罕见"],["治疗","秋水仙碱","激素/Etanercept","IL-1抑制剂"]],"pts":["TRAPS发作>1周区别FMF","R92P低外显率需家族筛查","核心ER应激→NF-κB","Etanercept/Anakinra有效"],"ref":"TRAPS in a Dutch family: TNFRSF1A mutation with reduced penetrance. Am J Med Genet. 2001;102(1):77-83. PMID: 11175303","pmid":"11175303","n":3},
{"f":"case_AID_NLRC4.html","t":"NLRC4炎症小体病 — 婴儿致死性MAS","sub":"NLRC4突变致巨噬细胞活化综合征（MAS，Macrophage Activation Syndrome）","nav":"NLRC4-MAS","tags":["t-r:NLRC4","t-r:MAS","t-y:IL-18极度升高"],"alert":"NLRC4炎症小体病最严重。IL-18极度升高(>100,000 pg/mL)，反复MAS(铁蛋白>10,000)。IL-18抑制剂(Tadekinig alfa)突破性疗效。","tl":[("新生儿","反复高热+皮疹+肝脾肿大"),("MAS","铁蛋白>10,000, 纤维蛋白原↓, 噬血","red"),("传统","激素+CsA+VP-16→短暂缓解→复发"),("IL-18","IL-18 >100,000 pg/mL(正常<500)","yellow"),("靶向","IL-18抑制剂→持续缓解","green")],"mech_t":"NLRC4-MAS级联","mech":"NLRC4功能获得→炎症小体自激活→Caspase-1→IL-1β+IL-18大量释放→NK/T过度活化→巨噬细胞活化→细胞因子风暴→噬血。<br>关键：NLRC4-MAS IL-18远超其他MAS(>100,000 vs <5,000)。","th":["指标","正常","MAS","NLRC4-MAS"],"tr":[["铁蛋白","10-200",">500",">10,000"],["纤维蛋白原","200-400","<150","<100"],["IL-18","<500","升高",">100,000"]],"pts":["NLRC4→IL-18极度升高是核心","MAS需早期识别(铁蛋白暴升)","IL-18抑制剂突破性疗效","IL-18极度升高可鉴别其他MAS"],"ref":"Life-threatening NLRC4 Hyperinflammation Treated with IL-18 Inhibition. JACI Pract. 2017;5(3):840-842. PMID: 27876626","pmid":"27876626","n":4},
{"f":"case_AID_SAVI.html","t":"SAVI — STING相关血管病","sub":"STING相关血管病伴婴儿起病（SAVI，STING-Associated Vasculopathy with Onset in Infancy）","nav":"SAVI","tags":["t-r:STING","t-y:血管病变","t-a:肺纤维化"],"alert":"SAVI由TMEM173(STING)功能获得→IFN-α/β持续产生→血管病变+肺纤维化+反复发热。JAK抑制剂阻断IFN信号有效。","tl":[("婴儿","反复发热+皮肤血管病变(指尖/鼻尖溃疡)"),("进展","肺间质纤维化"),("基因","TMEM173/STING突变→SAVI","yellow"),("JAKi","Baricitinib→IFN抑制→改善","green")],"mech_t":"cGAS-STING与I型干扰素病","mech":"STING功能获得→自激活→TBK1→IRF3→IFN-α/β大量→内皮损伤+肺成纤维细胞活化→血管病变+肺纤维化。<br>三大特征：①反复发热 ②血管病变(指端坏疽) ③ILD(进行性纤维化)。","th":["特征","SAVI","SLE","JDM"],"tr":[["核心","IFN-I","免疫复合物","自身抗体"],["皮肤","血管溃疡","蝶形红斑","Gottron疹"],["肺","纤维化(核心)","少见","ILD"],["治疗","JAK抑制剂","HCQ+免疫抑制","MTX+激素"]],"pts":["SAVI是新定义I型干扰素病","STING自激活→IFN-I→血管+肺","JAK抑制剂最有效","需与SLE/JDM鉴别"],"ref":"STING-Associated Vasculopathy with Onset in Infancy. Arthritis Rheumatol. 2014;66(11):3113-3118. PMID: 31705453","pmid":"31705453","n":5},
]}

# --- ITP ---
DATA["ITP"] = {"cn": "ITP免疫性血小板减少症", "cases": [
{"f":"case_ITP_acute.html","t":"急性ITP — 病毒感染后突发瘀斑","sub":"急性免疫性血小板减少症（ITP，Immune Thrombocytopenia）","nav":"急性ITP","tags":["t-r:PLT<20K","t-y:病毒感染后","t-a:IVIG"],"alert":"急性ITP是儿童最常见出血性疾病。病毒感染后1-4周突发瘀斑，PLT常<20×10⁹/L。80%儿童6月内自发缓解。","tl":[("前驱","上呼吸道感染后2周"),("突发","全身瘀点瘀斑，牙龈出血","red"),("化验","PLT 8×10⁹/L","yellow"),("治疗","IVIG 1g/kg×2天→PLT回升","green")],"mech_t":"ITP双重破坏机制","mech":"<b>外周破坏：</b>抗GPIIb/IIIa抗体→FcγR→脾脏巨噬细胞吞噬→PLT寿命缩短至数小时。<br><b>骨髓抑制：</b>自身抗体+CTL→巨核细胞损伤→产板减少。<br>儿童80%急性自限，成人80%慢性化。","th":["特征","急性(儿童)","慢性(成人)"],"tr":[["发病","2-5岁","20-40岁(女)"],["前驱","80%","20%"],["PLT","<20K","30-50K"],["缓解","~80%","~10%"],["一线","IVIG","激素"]],"pts":["儿童最常见出血疾病，80%自限","PLT<20K有颅内出血风险(<1%但致命)","IVIG一线3-5天PLT回升","抗血小板抗体→外周+骨髓双重"],"ref":"Immune Thrombocytopenia in Children. N Engl J Med. 2022;386(16):1545-1553. PMID: 35443104","pmid":"35443104","n":1},
{"f":"case_ITP_chronic.html","t":"慢性ITP — TPO-RA改变范式","sub":"慢性ITP（持续>12个月）","nav":"慢性ITP","tags":["t-r:难治性","t-y:>12月","t-a:TPO-RA"],"alert":"慢性ITP=PLT减少持续>12月。TPO-RA改变范式：增加生成vs减少破坏。","tl":[("初诊","PLT 15K，激素有效减量复发"),("12月+","诊断慢性ITP","yellow"),("二线","利妥昔单抗→短暂有效→复发"),("TPO-RA","Romiplostin→PLT 50-100K","green")],"mech_t":"慢性ITP免疫演进","mech":"抗PLT抗体→CD8+T直接杀伤→Treg缺陷→自身反应B/T逃逸→持续破坏。<br>TPO-RA：不抑制免疫→刺激巨核细胞增殖→增加PLT生成。Paradigm shift。","th":["治疗","机制","反应率","持久性"],"tr":[["激素","抑制吞噬","60-80%","减量复发"],["IVIG","封闭FcR","80%","2-4周"],["利妥昔","B细胞清除","40-60%","6-12月"],["脾切","去破坏场所","60-70%","较持久"],["TPO-RA","刺激产板","70-90%","需持续"]],"pts":["慢性=持续>12月，目标是安全PLT","TPO-RA范式转变","脾切率从>50%降至<10%","长期安全性良好"],"ref":"Immune Thrombocytopenia. Nat Rev Dis Primers. 2022;8(1):71. PMID: 36424557","pmid":"36424557","n":2},
{"f":"case_ITP_Evans.html","t":"Evans综合征 — ITP+AIHA","sub":"Evans综合征（ITP+AIHA，Autoimmune Hemolytic Anemia）","nav":"Evans","tags":["t-r:双重自身免疫","t-y:溶血+血小板减少","t-a:Coombs+"],"alert":"Evans=ITP+AIHA(Coombs+)。继发SLE/ALPS/CVID比例高(30-50%)。","tl":[("起病","苍白+乏力+瘀斑，Hb 65, PLT 12K"),("化验","网织红↑, 间接胆红素↑, Coombs(+)","yellow"),("排查","排除SLE/ALPS/CVID"),("治疗","甲强龙+IVIG→Hb/PLT回升","green")],"mech_t":"双重免疫攻击","mech":"AIHA：温抗体IgG→红细胞→脾巨噬细胞→溶血。ITP：抗PLT抗体→PLT破坏。<br>共同抗原？免疫耐受打破→多系自身抗体。继发率30-50%。","th":["特征","单纯ITP","Evans"],"tr":[["PLT","↓↓","↓↓"],["Hb","正常","↓↓"],["Coombs","阴性","阳性"],["间接胆红素","正常","↑↑"],["继发率","低","30-50%"]],"pts":["Evans=ITP+AIHA必须查Coombs","排查SLE/ALPS/CVID","治疗比单纯ITP复杂","复发率高需长期随访"],"ref":"Evans Syndrome: Pathogenesis and Treatment. Front Immunol. 2023;14:1194049. PMID: 37251884","pmid":"37251884","n":3},
{"f":"case_ITP_TPO.html","t":"TPO-RA治疗儿童慢性ITP","sub":"TPO受体激动剂（TPO-RA，Thrombopoietin Receptor Agonist）","nav":"TPO-RA","tags":["t-a:Romiplostim","t-a:Eltrombopag","t-y:慢性ITP"],"alert":"TPO-RA是近15年ITP最大突破。激活c-Mpl→巨核细胞增殖→增加产板。增加生成而非减少破坏。","tl":[("启用","Eltrombopag 25mg/d"),("应答","2周PLT>50,4周>100","green"),("长期","最低有效剂量维持","green")],"mech_t":"TPO-RA机制","mech":"Romiplostin：肽类，皮下qw，与c-Mpl非竞争结合。<br>Eltrombopag：小分子口服qd，结合c-Mpl跨膜区，需空腹。<br>均→JAK2→STAT5→巨核细胞增殖→PLT释放。","th":["特征","Romiplostin","Eltrombopag"],"tr":[["给药","皮下qw","口服qd"],["起效","1周","1-2周"],["儿童","✅","✅"],["肝损","低","需监测"],["血栓","1-3%","1-3%"]],"pts":["TPO-RA改变ITP范式","Romiplostin(皮下)vs Eltrombopag(口服)","起效1-2周需持续用药"],"ref":"TPO Receptor Agonists in ITP. Blood. 2023;141(10):1132-1143. PMID: 36520887","pmid":"36520887","n":4},
{"f":"case_ITP_secondary.html","t":"继发性ITP — SLE相关","sub":"继发性免疫性血小板减少症","nav":"继发ITP","tags":["t-r:SLE相关","t-y:抗磷脂抗体","t-a:治原发病"],"alert":"~25%成人ITP为继发，SLE最常见。可能先于SLE数年。aPL+时出血+血栓风险并存。","tl":[("初诊","PLT 35K，激素有效→\"原发性ITP\""),("2年后","关节痛+蝶形红斑+ANA 1:640+dsDNA+","red"),("修正","SLE相关继发性ITP","yellow"),("aPL","抗心磷脂+,狼疮抗凝物+","yellow"),("治疗","HCQ+MMF+小剂量激素→均控制","green")],"mech_t":"SLE相关ITP多重机制","mech":"四重打击：①抗PLT抗体→外周破坏 ②aPL→PLT活化→消耗+血栓 ③免疫复合物→补体→膜损伤 ④巨核细胞→产板减少。<br>所有新诊断ITP→查ANA+dsDNA+aPL。","th":["特征","原发ITP","SLE相关ITP"],"tr":[["ANA","阴性/低","阳性(1:160+)"],["dsDNA","阴性","阳性"],["aPL","通常阴","30-40%阳"],["补体","正常","降低"],["血栓","低","aPL+时升高"]],"pts":["所有新ITP查ANA+dsDNA+aPL","ITP可能是SLE首发","aPL+出血+血栓风险并存","治疗需兼顾SLE"],"ref":"ITP in SLE. Lupus. 2020;29(11):1421-1431. PMID: 32799842","pmid":"32799842","n":5},
]}

# --- PID ---
DATA["PID"] = {"cn": "PID原发性免疫缺陷病", "cases": [
{"f":"case_PID_XLA.html","t":"XLA — X连锁无丙种球蛋白血症","sub":"X连锁无丙种球蛋白血症（XLA，X-Linked Agammaglobulinemia）/ BTK缺陷","nav":"XLA","tags":["t-r:BTK缺陷","t-y:无丙种球蛋白","t-a:IVIG替代"],"alert":"首个PID(1952年Bruton)。BTK突变→B细胞停滞于pre-B→CD19+近零→所有Ig极低。母体IgG消失后(4-6月)反复化脓感染。终身IVIG替代。","tl":[("6月龄","母体IgG消失后反复中耳炎+肺炎"),("反复","荚膜菌：肺炎链球菌、流感嗜血杆菌"),("化验","IgG/IgA/IgM极低，CD19+<1%","yellow"),("基因","BTK突变","yellow"),("治疗","IVIG 400-600mg/kg/月→显著改善","green")],"mech_t":"BTK与B细胞发育","mech":"Pre-BCR→SYK→BLNK→BTK→PLCγ2→钙内流→增殖分化。无BTK→pre-B停滞→B细胞近零。CD19+近0%(关键诊断)，T细胞正常。","th":["特征","XLA","CVID","SCID"],"tr":[["遗传","XLR(BTK)","多基因","AR/AD"],["发病","4-6月","20-40岁","新生儿"],["B细胞","<1%","正常/↓","极低"],["Ig","全部极低","IgG低","全部极低"],["T细胞","正常","正常","极低"],["治疗","IVIG","IVIG","HSCT"]],"pts":["XLA=反复化脓+B细胞近零+低丙球","BTK→Pre-B发育停滞","终身IVIG预后良好","BTK抑制剂(Ibrutinib)印证此通路"],"ref":"Agammaglobulinemia. JACI Pract. 2023;11(4):1063-1070. PMID: 36933798","pmid":"36933798","n":1},
{"f":"case_PID_CVID.html","t":"CVID — 常见变异型免疫缺陷","sub":"常见变异型免疫缺陷病（CVID，Common Variable Immunodeficiency）","nav":"CVID","tags":["t-y:CVID","t-a:低IgG","t-r:自身免疫30%"],"alert":"最常见症状性PID(1/25,000)。低IgG+低IgA/IgM+抗体反应缺陷。B细胞存在但功能异常。30%自身免疫，5-10%淋巴瘤。","tl":[("青年","反复鼻窦炎+肺炎"),("20+岁","支气管扩张","red"),("化验","IgG 2.1, IgA 0.3 g/L","yellow"),("疫苗","肺炎球菌无应答"),("治疗","IVIG替代→改善","green")],"mech_t":"CVID免疫缺陷谱","mech":"B细胞→浆细胞分化障碍→CSR障碍→低IgG+低IgA→反复感染。Treg↓→自身免疫30%。B细胞克隆→淋巴瘤5-10%。已知基因仅~10%。","th":["特征","CVID","XLA","Good综合征"],"tr":[["发病","20-40岁","4-6月","40-70岁"],["B细胞","存在(功能↓)","近零","近零"],["自身免疫","30%","罕见","常见(MG)"],["胸腺瘤","无","无","100%"]],"pts":["最常见症状性PID，异质性强","B细胞存在但功能异常(区别XLA)","30%自身免疫+5-10%淋巴瘤","IVIG+定期监测"],"ref":"CVID. JACI. 2023;151(2):373-386. PMID: 36764329","pmid":"36764329","n":2},
{"f":"case_PID_SCID.html","t":"SCID — TREC筛查拯救生命","sub":"重症联合免疫缺陷（SCID，Severe Combined Immunodeficiency）","nav":"SCID","tags":["t-r:致命","t-y:TREC","t-a:HSCT"],"alert":"最严重PID(泡泡男孩)。T+B+NK严重缺陷→不经治疗2岁内死亡。TREC筛查→3.5月前HSCT→存活>90%。","tl":[("筛查","TREC↓→紧急转诊","green"),("确认","CD3+<50/μL","yellow"),("基因","IL2RG→X-SCID","yellow"),("保护","隔离+预防抗生素+无活疫苗"),("HSCT","3月龄→免疫重建成功","green")],"mech_t":"SCID分型","mech":"X-SCID(45%)：IL2RG(γc)→IL-2/4/7/9/15/21信号全断→T⁻B⁺NK⁻。<br>分型：T⁻B⁺NK⁻(IL2RG/JAK3) | T⁻B⁻NK⁺(RAG1/2) | T⁻B⁻NK⁻(ADA) | T⁻B⁺NK⁺(IL7R)。","th":["类型","基因","T","B","NK","频率"],"tr":[["X-SCID","IL2RG","−","+","−","45%"],["ADA","ADA","−","−","−","15%"],["RAG1/2","RAG1/2","−","−","+","10%"],["JAK3","JAK3","−","+","−","6%"]],"pts":["儿科急症，TREC筛查标准","3.5月前HSCT存活>90%","γc→6种细胞因子→T+NK双缺","基因治疗已用于X-SCID/ADA-SCID"],"ref":"SCID. N Engl J Med. 2023;388(19):1785-1798. PMID: 37163535","pmid":"37163535","n":3},
{"f":"case_PID_CGD.html","t":"CGD — 慢性肉芽肿病","sub":"慢性肉芽肿病（CGD，Chronic Granulomatous Disease）/ NADPH氧化酶缺陷","nav":"CGD","tags":["t-r:NADPH氧化酶","t-y:催化过氧化物(-)","t-a:IFN-γ"],"alert":"吞噬细胞杀菌缺陷。NADPH氧化酶缺陷→不能产ROS→过氧化氢酶阳性菌(金葡菌/曲霉菌)无法杀灭。反复化脓+肉芽肿。DHR诊断。","tl":[("幼儿","反复脓肿+淋巴结炎+曲霉菌肺炎"),("DHR","呼吸爆发→无荧光→确诊","yellow"),("基因","gp91phox(CYBB)→X-CGD","yellow"),("预防","TMP-SMX+伊曲康唑+IFN-γ","green"),("根治","HSCT或基因治疗","green")],"mech_t":"NADPH氧化酶与呼吸爆发","mech":"正常：NADPH氧化酶→O₂→O₂⁻→H₂O₂→HOCl→杀菌。<br>CGD：无ROS→对过氧化氢酶阳性菌无效。<br>矛盾：杀菌↓但肉芽肿↑(存活微生物→Th1/Th17→肉芽肿)。","th":["特征","X-CGD(gp91)","AR-CGD(p47)","AR-CGD(p67)"],"tr":[["遗传","XLR","AR","AR"],["频率","~65%","~25%","~5%"],["严重","重","较轻","重"]],"pts":["CGD=NADPH氧化酶→无ROS","过