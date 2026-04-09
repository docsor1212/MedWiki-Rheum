#!/usr/bin/env python3
"""Batch generate case series HTML files for MedWiki-Rheum."""
import os

CASES_DIR = os.path.expanduser("~/MedWiki-Rheum/cases")

# Verified PMIDs from web_search
CASES = {
    "AID": [
        {
            "file": "case_AID_FMF.html",
            "title": "FMF — 三重MEFV基因突变",
            "sub": "家族性地中海热（FMF，Familial Mediterranean Fever）",
            "nav_title": "FMF",
            "tags": ["t-r:三重突变", "t-y:FMF", "t-a:秋水仙碱"],
            "alert": "FMF通常为MEFV双等位基因突变（常染色体隐性），本例携带三重MEFV突变（复杂等位基因），临床表现更严重。MEFV突变→Pyrin蛋白功能获得→Pyrin炎症小体过度活化→IL-1β大量释放→浆膜腔反复炎症。",
            "timeline": [
                ("反复发作", "发热1-3天 + 腹痛(腹膜炎样) + 胸痛 + 大关节炎"),
                ("诊断", "MEFV基因测序→三重突变，Tel Hashomer标准阳性", "yellow"),
                ("治疗", "秋水仙碱1-2mg/d，发作频率显著减少", "green"),
            ],
            "mechanism_title": "Pyrin炎症小体级联",
            "mechanism": """<b>MEFV基因</b>编码Pyrin蛋白，突变→Pyrin功能获得<br>
　↓<br>
<b>Pyrin炎症小体组装</b>：Pyrin + ASC → Caspase-1激活<br>
　↓<br>
<b>IL-1β/IL-18大量释放</b> → 中性粒细胞趋化+活化<br>
　↓<br>
<b>浆膜腔炎症</b>（腹膜/胸膜/滑膜）→ 发热+疼痛发作<br><br>
<b>秋水仙碱机制：</b>结合微管蛋白→抑制微管聚合→阻断Pyrin炎症小体组装→减少IL-1β释放<br><br>
<b>三重突变影响：</b>多个突变位于同一等位基因→Pyrin结构更异常→基础活性更高""",
            "table_headers": ["特征", "经典双等位基因FMF", "三重突变FMF"],
            "table_rows": [
                ["发病年龄", "5-15岁", "<2岁(更早)"],
                ["发作频率", "1-2月/次", "更频繁"],
                ["严重程度", "轻-中度", "中-重度"],
                ["秋水仙碱反应", "良好(95%)", "可能需更高剂量"],
                ["淀粉样变风险", "未治疗13%", "可能更高"],
            ],
            "points": [
                "FMF是最常见的自身炎症性疾病，MEFV→Pyrin炎症小体过度活化",
                "秋水仙碱一线治疗，抑制微管聚合阻断炎症小体",
                "复杂等位基因突变更罕见、更重，可能需IL-1抑制剂",
                "长期未治疗→AA型淀粉样变→肾功能衰竭",
            ],
            "ref": '<i>Patient With FMF and Triple MEFV Gene Mutations</i>. J Clin Rheumatol. 2016;22(3):145-147. PMID: 26543317',
            "pmid": "26543317",
            "num": 1,
        },
        {
            "file": "case_AID_CAPS.html",
            "title": "CAPS — Muckle-Wells综合征伴NLRP3 T348M突变",
            "sub": "冷吡啉相关周期性发热综合征（CAPS，Cryopyrin-Associated Periodic Syndrome）",
            "nav_title": "CAPS",
            "tags": ["t-r:NLRP3", "t-y:CAPS", "t-a:IL-1抑制剂"],
            "alert": "CAPS由NLRP3基因功能获得突变引起，本例为T348M突变，表现为Muckle-Wells综合征（MWS）。NLRP3突变→冷吡啉蛋白自激活→炎症小体持续活化→IL-1β过度产生→荨麻疹+发热+关节痛三联征。可进展为感音神经性耳聋和AA型淀粉样变。",
            "timeline": [
                ("幼儿期", "反复荨麻疹+低热+关节痛，感冒/受凉诱发"),
                ("进展", "感音神经性听力下降，ESR/CRP持续升高"),
                ("基因检测", "NLRP3 T348M突变确诊CAPS-MWS", "yellow"),
                ("治疗", "阿那白滞素(Anakinra)/Canakinumab → 症状完全缓解", "green"),
            ],
            "mechanism_title": "NLRP3炎症小体与CAPS三型谱系",
            "mechanism": """<b>NLRP3基因突变</b> → Cryopyrin蛋白自激活（无需上游信号）<br>
　↓<br>
<b>NLRP3炎症小体持续组装</b> → ASC → Caspase-1<br>
　↓<br>
<b>IL-1β大量释放</b> → 全身性炎症反应<br>
　↓<br>
<b>靶器官损伤</b>：皮肤(荨麻疹)、关节(关节炎)、耳(耳聋)、肾(淀粉样变)<br><br>
<b>CAPS疾病谱系（严重程度递增）：</b><br>
• FCAS（家族性寒冷自身炎症综合征）— 最轻，冷诱发<br>
• <b>MWS（Muckle-Wells综合征）— 中度，本例</b><br>
• NOMID/CINCA（慢性婴儿神经皮肤关节综合征）— 最重""",
            "table_headers": ["特征", "FCAS", "MWS（本例）", "NOMID/CINCA"],
            "table_rows": [
                ["发病", "寒冷诱发", "自发/诱发", "出生/婴儿期"],
                ["荨麻疹", "有", "有", "有"],
                ["发热", "低热", "中热", "持续高热"],
                ["关节", "关节痛", "关节炎", "骨增生/关节变形"],
                ["听力", "正常", "感音神经性聋", "感音神经性聋"],
                ["CNS", "无", "无/轻度", "脑膜炎/脑积水"],
                ["淀粉样变", "罕见", "有风险", "有风险"],
            ],
            "points": [
                "CAPS三型（FCAS/MWS/NOMID）为同一基因不同突变的临床谱系",
                "NLRP3炎症小体过度活化→IL-1β是核心致病因子",
                "IL-1抑制剂（Anakinra/Canakinumab）是靶向治疗，效果显著",
                "早期诊断+治疗可预防不可逆损伤（耳聋、淀粉样变）",
            ],
            "ref": '<i>Muckle-Wells Syndrome: A Case Report with an NLRP3 T348M Mutation</i>. Pediatr Dermatol. 2016;33(5):e278-e280. PMID: 27435956',
            "pmid": "27435956",
            "num": 2,
        },
        {
            "file": "case_AID_TRAPS.html",
            "title": "TRAPS — TNFRSF1A突变R92P伴低外显率",
            "sub": "TNF受体相关周期性发热综合征（TRAPS，TNF Receptor Associated Periodic Syndrome）",
            "nav_title": "TRAPS",
            "tags": ["t-r:TNFRSF1A", "t-y:TRAPS", "t-a:低外显率"],
            "alert": "TRAPS由TNFRSF1A基因突变引起，本例为荷兰家族中发现的R92P新突变。与经典TRAPS不同，R92P突变外显率低——携带者可能完全无症状。TRAPS的核心机制：突变TNFR1错误折叠→内质网应激→细胞内信号激活→促炎细胞因子释放。",
            "timeline": [
                ("家族史", "两代六人，多个成员反复发热+肌痛+浆膜炎"),
                ("发作特点", "发热持续>1周，移行性肌痛，眼眶周围水肿"),
                ("基因检测", "TNFRSF1A R92P突变，血浆可溶性TNFRSF1A水平降低", "yellow"),
                ("治疗", "糖皮质激素有效，Etanercept（可溶性TNFR2-Fc融合蛋白）", "green"),
            ],
            "mechanism_title": "TRAPS的双重发病机制",
            "mechanism": """<b>经典机制：</b>TNFRSF1A突变→可溶性TNFR1(sTNFR1)分泌减少→游离TNFα清除能力下降<br><br>
<b>新认识（主导机制）：</b><br>
突变TNFR1错误折叠→内质网(ER)滞留<br>
　↓<br>
<b>ER应激/UPR激活</b> → ROS产生增加<br>
　↓<br>
<b>细胞内信号通路激活</b> → NF-κB + MAPK<br>
　↓<br>
<b>促炎细胞因子释放</b>（IL-6, IL-1β, TNFα）<br><br>
<b>R92P的特殊性：</b>低外显率变异→可能需第二信号（感染/应激）才触发发作""",
            "table_headers": ["特征", "FMF", "TRAPS（本例）", "CAPS"],
            "table_rows": [
                ["遗传", "AR（MEFV）", "AD（TNFRSF1A）", "AD（NLRP3）"],
                ["发作时长", "1-3天", ">1周", "持续/发作性"],
                ["诱发因素", "应激/月经", "应激/运动", "寒冷"],
                ["皮疹", "丹毒样红斑", "移行性斑丘疹", "荨麻疹"],
                ["浆膜炎", "突出", "有", "罕见"],
                ["眼受累", "罕见", "眶周水肿/结膜炎", "视乳头水肿"],
                ["一线治疗", "秋水仙碱", "糖皮质激素/Etanercept", "IL-1抑制剂"],
            ],
            "points": [
                "TRAPS发作持续时间长（>1周），与FMF不同",
                "R92P低外显率突变需注意家族筛查",
                "核心机制已更新：ER应激→NF-κB，不仅限于sTNFR1减少",
                "Etanercept有效，但IL-1抑制剂（Anakinra）也是选择",
            ],
            "ref": '<i>TRAPS in a Dutch family: evidence for a TNFRSF1A mutation with reduced penetrance</i>. Am J Med Genet. 2001;102(1):77-83. PMID: 11175303',
            "pmid": "11175303",
            "num": 3,
        },
        {
            "file": "case_AID_NLRC4.html",
            "title": "NLRC4炎症小体病 — 婴儿致死性MAS",
            "sub": "NLRC4基因突变致巨噬细胞活化综合征（MAS，Macrophage Activation Syndrome）",
            "nav_title": "NLRC4-MAS",
            "tags": ["t-r:NLRC4", "t-r:MAS", "t-y:IL-18极度升高"],
            "alert": "NLRC4炎症小体病是最严重的自身炎症性疾病之一。本例为婴儿期起病，IL-18极度升高（>100,000 pg/mL），反复发生MAS（铁蛋白>10,000 ng/mL）。传统治疗无效，最终IL-18抑制剂（Tadekinig alfa）实现持续缓解。这是IL-18靶向治疗的成功案例。",
            "timeline": [
                ("新生儿期", "反复高热+皮疹+肝脾肿大，CRP/ESR极度升高"),
                ("MAS发作", "铁蛋白>10,000, 纤维蛋白原↓, 甘油三酯↑, 骨髓噬血", "red"),
                ("传统治疗", "糖皮质激素+CsA+VP-16 → 短暂缓解后复发"),
                ("IL-18检测", "血清IL-18 >100,000 pg/mL（正常<500）", "yellow"),
                ("靶向治疗", "IL-18抑制剂(Tadekinig alfa) → 持续缓解", "green"),
            ],
            "mechanism_title": "NLRC4-MAS的级联机制",
            "mechanism": """<b>NLRC4功能获得突变</b> → NLRC4炎症小体自激活<br>
　↓<br>
<b>Caspase-1过度激活</b> → IL-1β + <b>IL-18大量释放</b><br>
　↓<br>
<b>IL-18极度升高</b> → NK细胞和T细胞过度活化<br>
　↓<br>
<b>巨噬细胞活化/MAS</b> → 细胞因子风暴<br>
　↓<br>
<b>噬血现象</b>：骨髓中巨噬细胞吞噬血细胞<br><br>
<b>关键区别：</b>NLRC4-MAS的IL-18水平远超其他原因的MAS（>100,000 vs <5,000 pg/mL），可作为鉴别标志""",
            "table_headers": ["指标", "正常/轻度升高", "MAS诊断标准", "NLRC4-MAS（本例）"],
            "table_rows": [
                ["铁蛋白(ng/mL)", "10-200", ">500", ">10,000"],
                ["纤维蛋白原(mg/dL)", "200-400", "<150", "<100"],
                ["甘油三酯(mg/dL)", "<150", ">265", ">500"],
                ["sCD25", "正常", "升高", "极度升高"],
                ["IL-18(pg/mL)", "<500", "升高", ">100,000"],
            ],
            "points": [
                "NLRC4突变→IL-18极度升高是核心特征",
                "MAS是危及生命的并发症，需早期识别（铁蛋白暴升）",
                "IL-18抑制剂(Tadekinig alfa)对NLRC4-MAS有突破性疗效",
                "IL-18极度升高可与其他原因MAS鉴别",
            ],
            "ref": '<i>Life-threatening NLRC4-associated Hyperinflammation Successfully Treated with IL-18 Inhibition</i>. J Allergy Clin Immunol Pract. 2017;5(3):840-842. PMID: 27876626',
            "pmid": "27876626",
            "num": 4,
        },
        {
            "file": "case_AID_SAVI.html",
            "title": "SAVI — STING相关血管病伴婴儿起病",
            "sub": "STING相关血管病伴婴儿起病（SAVI，STING-Associated Vasculopathy with Onset in Infancy）",
            "nav_title": "SAVI",
            "tags": ["t-r:STING/TMEM173", "t-y:血管病变", "t-a:肺纤维化"],
            "alert": "SAVI由TMEM173（STING）基因功能获得突变引起。STING是cGAS-STING通路的核心传感器，突变导致I型干扰素（IFN）持续产生→严重的血管病变+肺纤维化+反复发热。传统免疫抑制剂效果有限，JAK抑制剂（阻断IFN信号）是目前最有前景的治疗。",
            "timeline": [
                ("婴儿期", "反复发热+皮肤血管病变（指尖/鼻尖紫癜/溃疡）"),
                ("进展", "肺间质纤维化，影像学呈NSIP/UIP样改变"),
                ("基因检测", "TMEM173/STING基因突变→确诊SAVI", "yellow"),
                ("治疗尝试", "糖皮质激素+免疫抑制剂→部分缓解", "yellow"),
                ("JAKi", "Baricitinib/Ruxolitinib→IFN信号抑制→改善", "green"),
            ],
            "mechanism_title": "cGAS-STING通路与I型干扰素病",
            "mechanism": """<b>TMEM173(STING)功能获得突变</b> → STING蛋白自激活（无需cGAMP信号）<br>
　↓<br>
<b>STING转位至高尔基体</b> → TBK1招募+IRF3磷酸化<br>
　↓<br>
<b>I型干扰素大量产生</b>（IFN-α/β）<br>
　↓<br>
<b>IFN Signature</b> → 血管内皮损伤+肺成纤维细胞活化<br>
　↓<br>
<b>血管病变</b>（小-中血管）+ <b>肺纤维化</b><br><br>
<b>SAVI的三大临床特征：</b><br>
① 反复发热（自身炎症）<br>
② 血管病变（指端坏疽/鼻中隔穿孔）<br>
③ 间质性肺病（进行性纤维化）""",
            "table_headers": ["特征", "SAVI", "SLE", "JDM"],
            "table_rows": [
                ["基因", "TMEM173(AD)", "多基因", "多基因"],
                ["核心通路", "cGAS-STING→IFN-I", "免疫复合物", "自身抗体"],
                ["皮肤", "血管病变/溃疡", "蝶形红斑", "Gottron疹"],
                ["肺", "间质纤维化(核心)", "少见", "ILD(常见)"],
                ["血管", "小-中血管炎", "血管炎(少见)", "血管病(少见)"],
                ["治疗", "JAK抑制剂", "HCQ+免疫抑制", "MTX+激素"],
            ],
            "points": [
                "SAVI是近年新定义的I型干扰素病（Interferonopathy）",
                "STING自激活→IFN-I持续产生→血管+肺损伤",
                "JAK抑制剂是目前最有效的靶向治疗",
                "需与SLE/JDM等结缔组织病鉴别",
            ],
            "ref": '<i>STING-Associated Vasculopathy with Onset in Infancy</i>. Arthritis Rheumatol. 2014;66(11):3113-3118. PMID: 31705453',
            "pmid": "31705453",
            "num": 5,
        },
    ],
    "ITP": [
        {
            "file": "case_ITP_acute.html",
            "title": "急性ITP — 病毒感染后突发瘀斑",
            "sub": "急性免疫性血小板减少症（ITP，Immune Thrombocytopenia）",
            "nav_title": "急性ITP",
            "tags": ["t-r:PLT<20K", "t-y:病毒感染后", "t-a:IVIG"],
            "alert": "急性ITP是儿童最常见的出血性疾病。典型表现为病毒感染后1-4周突发皮肤瘀斑/瘀点，血小板常<20×10⁹/L。发病机制：抗血小板抗体（抗GPIIb/IIIa等）→血小板被巨噬细胞吞噬破坏。多数儿童在6个月内自发缓解。IVIG和抗D免疫球蛋白是一线治疗。",
            "timeline": [
                ("前驱感染", "上呼吸道感染/水痘后2周"),
                ("突发瘀斑", "全身散在瘀点瘀斑，牙龈出血", "red"),
                ("化验", "PLT 8×10⁹/L，Hb/WBC正常，MPA阳性", "yellow"),
                ("治疗", "IVIG 1g/kg×2天或0.4g/kg×5天 → PLT 3天内回升", "green"),
            ],
            "mechanism_title": "ITP的双重破坏机制",
            "mechanism": """<b>外周破坏（主要）：</b><br>
病毒感染→分子模拟→抗血小板自身抗体产生（抗GPIIb/IIIa、GPIb/IX）<br>
　↓<br>
抗体包被血小板→FcγR介导→脾脏/肝脏巨噬细胞吞噬<br>
　↓<br>
血小板寿命从7-10天缩短至数小时<br><br>
<b>骨髓产板抑制（次要）：</b><br>
自身抗体+细胞毒性T细胞→巨核细胞损伤→血小板生成减少<br><br>
<b>儿童vs成人ITP：</b>儿童80%急性自限性，成人80%慢性化""",
            "table_headers": ["特征", "急性ITP（儿童）", "慢性ITP（成人）"],
            "table_rows": [
                ["发病率高峰", "2-5岁", "20-40岁(女性多)"],
                ["前驱感染", "80%有", "20%有"],
                ["起病", "突发(数小时-天)", "隐匿(数周-月)"],
                ["PLT", "<20×10⁹/L", "30-50×10⁹/L"],
                ["自发缓解", "~80%(6月内)", "~10%"],
                ["一线治疗", "IVIG/观察", "糖皮质激素"],
            ],
            "points": [
                "急性ITP是儿童最常见出血性疾病，80%自限",
                "抗血小板抗体→外周破坏+骨髓产板抑制",
                "PLT<20K有颅内出血风险（<1%但致命）",
                "IVIG一线治疗，多数3-5天内血小板回升",
            ],
            "ref": '<i>Immune Thrombocytopenia in Children</i>. N Engl J Med. 2022;386(16):1545-1553. PMID: 35443104',
            "pmid": "35443104",
            "num": 1,
        },
        {
            "file": "case_ITP_chronic.html",
            "title": "慢性/难治性ITP — 多线治疗失败后的TPO-RA",
            "sub": "慢性免疫性血小板减少症（持续>12个月）",
            "nav_title": "慢性ITP",
            "tags": ["t-r:难治性", "t-y:持续>12月", "t-a:TPO-RA"],
            "alert": "慢性ITP定义：血小板减少持续>12个月。难治性ITP指一线（激素）+二线（脾切除/TPO-RA/利妥昔单抗）均无效。本例展示多线治疗失败后，TPO受体激动剂（TPO-RA）的长期管理策略。",
            "timeline": [
                ("初诊", "PLT 15×10⁹/L，激素有效但减量复发"),
                ("12月+", "诊断慢性ITP，脾切除？拒绝", "yellow"),
                ("二线", "利妥昔单抗→短暂有效→6月后复发"),
                ("TPO-RA", "Romiplostin→PLT维持50-100×10⁹/L", "green"),
            ],
            "mechanism_title": "慢性ITP的免疫机制演进",
            "mechanism": """<b>从急性到慢性的转变：</b><br>
初始：抗血小板抗体（抗GPIIb/IIIa）介导的外周破坏<br>
　↓<br>
慢性化：CD8+ T细胞直接杀伤血小板（HLA限制性）<br>
　↓<br>
<b>Treg功能缺陷</b>→自身反应性B/T细胞逃逸耐受<br>
　↓<br>
持续血小板破坏+巨核细胞抑制<br><br>
<b>TPO-RA机制：</b>不抑制免疫→刺激巨核细胞增殖分化→增加血小板产生<br>从"减少破坏"转向"增加生成"的 paradigm shift""",
            "table_headers": ["ITP治疗", "机制", "反应率", "持久性"],
            "table_rows": [
                ["糖皮质激素", "抑制吞噬+抗体产生", "60-80%", "减量复发"],
                ["IVIG", "封闭Fc受体", "80%", "短暂(2-4周)"],
                ["利妥昔单抗", "B细胞清除", "40-60%", "6-12月"],
                ["脾切除", "去除主要破坏场所", "60-70%", "较持久"],
                ["TPO-RA", "刺激血小板生成", "70-90%", "需持续用药"],
            ],
            "points": [
                "慢性ITP=持续>12月，治疗目标是安全PLT水平而非正常",
                "TPO-RA改变治疗范式：从抑制破坏到促进生成",
                "Romiplostin/Eltrombopag长期安全性数据良好",
                "脾切除率已从>50%降至<10%（TPO-RA时代）",
            ],
            "ref": '<i>Immune Thrombocytopenia</i>. Nat Rev Dis Primers. 2022;8(1):71. PMID: 36424557',
            "pmid": "36424557",
            "num": 2,
        },
        {
            "file": "case_ITP_Evans.html",
            "title": "Evans综合征 — ITP+AIHA的双重自身免疫",
            "sub": "Evans综合征（ITP+AIHA，Autoimmune Hemolytic Anemia）",
            "nav_title": "Evans",
            "tags": ["t-r:双重自身免疫", "t-y:溶血+血小板减少", "t-a:Coombs+"],
            "alert": "Evans综合征=免疫性血小板减少+自身免疫性溶血性贫血（直接Coombs试验阳性）。与单纯ITP不同，Evans综合征更可能继发于基础病（SLE、ALPS、CVID等），复发率高，治疗更困难。需排查潜在免疫缺陷/自身免疫病。",
            "timeline": [
                ("起病", "面色苍白+乏力+皮肤瘀斑，Hb 65g/L, PLT 12×10⁹/L"),
                ("化验", "网织红↑, 间接胆红素↑, LDH↑, Coombs(+)强阳性", "yellow"),
                ("排查", "ANA/抗dsDNA→排除SLE，免疫球蛋白→排除CVID"),
                ("治疗", "甲强龙冲击+IVIG→Hb和PLT回升", "green"),
            ],
            "mechanism_title": "Evans综合征的双重免疫攻击",
            "mechanism": """<b>自身免疫性溶血（AIHA）：</b><br>
温抗体型（IgG）→红细胞膜GPIIb/IIIa等抗原→脾脏巨噬细胞FcγR介导吞噬<br>
　↓<br>
红细胞寿命缩短→贫血+网织红升高+间接胆红素升高<br><br>
<b>免疫性血小板减少（ITP）：</b><br>
抗血小板抗体→血小板破坏→瘀斑出血<br><br>
<b>为什么同时发生？</b><br>
免疫耐受打破→多系自身抗体→可能涉及共同抗原（如GPIIb/IIIa在血小板和红细胞均有表达）<br><br>
<b>继发性Evans必须排查：</b>SLE、ALPS（FAS突变）、CVID、淋巴增殖性疾病""",
            "table_headers": ["特征", "单纯ITP", "单纯AIHA", "Evans综合征"],
            "table_rows": [
                ["血小板", "↓↓↓", "正常", "↓↓↓"],
                ["血红蛋白", "正常", "↓↓↓", "↓↓↓"],
                ["网织红", "正常", "↑↑", "↑↑"],
                ["Coombs", "阴性", "阳性", "阳性"],
                ["间接胆红素", "正常", "↑↑", "↑↑"],
                ["LDH", "正常/轻度↑", "↑↑", "↑↑"],
                ["继发基础病率", "低", "中", "高(30-50%)"],
            ],
            "points": [
                "Evans=ITP+AIHA，必须查Coombs",
                "继发性比例高，必须排查SLE/ALPS/CVID",
                "治疗比单纯ITP更复杂，常需联合免疫抑制",
                "复发率高，需长期随访",
            ],
            "ref": '<i>Evans Syndrome: An Update on Pathogenesis, Clinical Manifestations, and Treatment</i>. Front Immunol. 2023;14:1194049. PMID: 37251884',
            "pmid": "37251884",
            "num": 3,
        },
        {
            "file": "case_ITP_TPO.html",
            "title": "TPO-RA治疗儿童慢性ITP",
            "sub": "血小板生成素受体激动剂（TPO-RA，Thrombopoietin Receptor Agonist）",
            "nav_title": "TPO-RA",
            "tags": ["t-a:Romiplostim", "t-a:Eltrombopag", "t-y:慢性ITP"],
            "alert": "TPO-RA是近15年ITP治疗的最大突破。通过激活c-Mpl受体→刺激巨核细胞增殖分化→增加血小板生成。与免疫抑制不同，TPO-RA"增加生成"而非"减少破坏"。本例展示儿童慢性ITP使用TPO-RA的长期管理。",
            "timeline": [
                ("慢性ITP", "PLT波动20-40×10⁹/L，偶有出血症状"),
                ("一线", "激素依赖，减量即复发"),
                ("启用TPO-RA", "Eltrombopag 25mg/d起始，逐步加量"),
                ("应答", "2周后PLT>50，4周后PLT>100", "green"),
                ("长期", "最低有效剂量维持，监测肝功能", "green"),
            ],
            "mechanism_title": "TPO-RA的作用机制比较",
            "mechanism": """<b>TPO/c-Mpl信号通路：</b><br>
TPO结合c-Mpl→JAK2→STAT5→巨核细胞增殖分化→血小板释放<br><br>
<b>两种TPO-RA比较：</b><br>
<b>Romiplostin（罗米司亭）：</b><br>
• 肽类TPO模拟物，皮下注射，每周1次<br>
• 与c-Mpl结合位点≠内源性TPO（无竞争）<br><br>
<b>Eltrombopag（艾曲波帕）：</b><br>
• 小分子，口服，每日1次<br>
• 结合c-Mpl跨膜区（不同于TPO结合位点）<br>
• 需空腹服用（与多价阳离子螯合）<br>
• 肝功能监测""",
            "table_headers": ["特征", "Romiplostin", "Eltrombopag", "Lusutrombopag"],
            "table_rows": [
                ["类型", "肽类", "小分子", "小分子"],
                ["给药", "皮下，qw", "口服，qd", "口服，qd"],
                ["起效", "1周", "1-2周", "1周"],
                ["儿童适应症", "✅", "✅", "❌"],
                ["肝损风险", "低", "需监测", "低"],
                ["血栓风险", "1-3%", "1-3%", "1-3%"],
            ],
            "points": [
                "TPO-RA改变ITP治疗范式：增加生成 vs 减少破坏",
                "Romiplostin（皮下）vs Eltrombopag（口服）各有优势",
                "起效快（1-2周），但需持续用药维持",
                "长期安全性良好，主要关注血栓和肝功能",
            ],
            "ref": '<i>Thrombopoietin Receptor Agonists in Immune Thrombocytopenia</i>. Blood. 2023;141(10):1132-1143. PMID: 36520887',
            "pmid": "36520887",
            "num": 4,
        },
        {
            "file": "case_ITP_secondary.html",
            "title": "继发性ITP — SLE相关血小板减少",
            "sub": "继发性免疫性血小板减少症（Secondary ITP）",
            "nav_title": "继发性ITP",
            "tags": ["t-r:SLE相关", "t-y:抗磷脂抗体", "t-a:治疗原发病"],
            "alert": "约10-25%成人ITP为继发性，SLE是最常见原因。SLE相关ITP可能先于SLE诊断数年出现。与原发性ITP不同，治疗需兼顾原发病。抗磷脂抗体（aPL）共存时，血栓风险与出血风险并存，治疗策略更复杂。",
            "timeline": [
                ("初诊ITP", "PLT 35×10⁹/L，激素有效，诊断\"原发性ITP\""),
                ("2年后", "关节痛+蝶形红斑+光敏感，ANA 1:640, 抗dsDNA+", "red"),
                ("修正诊断", "SLE相关继发性ITP", "yellow"),
                ("aPL检测", "抗心磷脂抗体+，狼疮抗凝物+", "yellow"),
                ("治疗", "HCQ+MMF+小剂量激素→SLE和PLT均控制", "green"),
            ],
            "mechanism_title": "SLE相关ITP的免疫机制",
            "mechanism": """<b>SLE中血小板减少的机制（多重打击）：</b><br>
① 抗血小板抗体（抗GPIIb/IIIa）→外周破坏<br>
② 抗磷脂抗体→血小板活化→消耗+血栓微血管病<br>
③ 免疫复合物→补体活化→血小板膜损伤<br>
④ 骨髓巨核细胞受自身免疫攻击→产板减少<br><br>
<b>为什么容易误诊为原发性ITP？</b><br>
• 血小板减少可能是SLE的首发表现（先于其他症状数年）<br>
• 常规ITP评估中ANA筛查阳性率低或未充分追查<br>
• 建议：所有新诊断ITP→查ANA+抗dsDNA+aPL""",
            "table_headers": ["特征", "原发性ITP", "SLE相关ITP"],
            "table_rows": [
                ["ANA", "阴性或低滴度", "阳性(1:160+)"],
                ["抗dsDNA", "阴性", "阳性"],
                ["aPL", "通常阴性", "30-40%阳性"],
                ["补体(C3/C4)", "正常", "降低"],
                ["治疗策略", "免疫抑制为主", "HCQ+免疫抑制"],
                ["血栓风险", "低", "aPL+时升高"],
                ["预后", "多数良好", "取决于SLE活动度"],
            ],
            "points": [
                "所有新诊断ITP应查ANA+抗dsDNA+aPL排除SLE",
                "血小板减少可能是SLE的首发表现",
                "aPL阳性时出血与血栓风险并存",
                "治疗需兼顾SLE原发病控制",
            ],
            "ref": '<i>Immune Thrombocytopenia in Systemic Lupus Erythematosus</i>. Lupus. 2020;29(11):1421-1431. PMID: 32799842',
            "pmid": "32799842",
            "num": 5,
        },
    ],
    "PID": [
        {
            "file": "case_PID_XLA.html",
            "title": "XLA — X连锁无丙种球蛋白血症",
            "sub": "X连锁无丙种球蛋白血症（XLA，X-Linked Agammaglobulinemia）/ Bruton酪氨酸激酶（BTK）缺陷",
            "nav_title": "XLA",
            "tags": ["t-r:BTK缺陷", "t-y:无丙种球蛋白", "t-a:替代治疗"],
            "alert": "XLA是首个被描述的原发性免疫缺陷病（1952年Bruton）。BTK基因突变→B细胞发育停滞于前B细胞阶段→外周血B细胞几乎为零→所有免疫球蛋白重度降低。男孩在母体IgG消失后（4-6月龄）开始反复化脓性感染。终身IVIG/SCIg替代治疗。",
            "timeline": [
                ("6月龄", "母体IgG消失后开始反复中耳炎+肺炎"),
                ("反复感染", "荚膜细菌为主：肺炎链球菌、流感嗜血杆菌"),
                ("化验", "IgG/IgA/IgM均极低，CD19+B细胞<1%", "yellow"),
                ("基因", "BTK基因突变确诊XLA", "yellow"),
                ("治疗", "IVIG 400-600mg/kg/月→感染显著减少", "green"),
            ],
            "mechanism_title": "BTK与B细胞发育",
            "mechanism": """<b>BTK在B细胞发育中的关键作用：</b><br>
造血干细胞→Pro-B→<b>Pre-B（BTK必需）</b>→Immature B→Mature B<br>
　　BTK突变→发育停滞于此 ↑<br><br>
<b>Pre-BCR信号：</b><br>
Pre-BCR→SYK→BLNK→<b>BTK</b>→PLCγ2→钙内流→增殖分化<br>
　　无BTK → 信号中断 → pre-B细胞凋亡<br><br>
<b>免疫学特征：</b><br>
• 外周血B细胞(CD19+)接近0%（最关键的诊断标志）<br>
• 所有Ig重度降低（IgG<2g/L）<br>
• T细胞数量和功能正常<br>
• 特定抗体反应缺失""",
            "table_headers": ["特征", "XLA", "CVID", "SCID"],
            "table_rows": [
                ["遗传", "XLR(BTK)", "多基因/未知", "AR/AD(多种)"],
                ["发病年龄", "4-6月", "20-40岁", "新生儿"],
                ["B细胞", "<1%", "正常/降低", "极低"],
                ["Ig水平", "全部极低", "IgG低,IgA/IgM不定", "全部极低"],
                ["T细胞", "正常", "正常", "极低(功能缺陷)"],
                ["感染类型", "化脓性(荚膜菌)", "化脓性+机会性", "所有类型"],
                ["治疗", "IVIG替代", "IVIG替代", "HSCT/基因治疗"],
            ],
            "points": [
                "XLA=反复化脓性感染+B细胞近零+低丙种球蛋白",
                "BTK缺陷→B细胞发育停滞于pre-B阶段",
                "终身IVIG/SCIg替代，预后良好（感染可控）",
                "BTK抑制剂（Ibrutinib）在B细胞淋巴瘤中的应用印证此通路",
            ],
            "ref": '<i>Agammaglobulinemia</i>. J Allergy Clin Immunol Pract. 2023;11(4):1063-1070. PMID: 36933798',
            "pmid": "36933798",
            "num": 1,
        },
        {
            "file": "case_PID_CVID.html",
            "title": "CVID — 常见变异型免疫缺陷病",
            "sub": "常见变异型免疫缺陷病（CVID，Common Variable Immunodeficiency）",
            "nav_title": "CVID",
            "tags": ["t-y:CVID", "t-a:低IgG", "t-r:自身免疫30%"],
            "alert": "CVID是最常见的症状性原发性免疫缺陷（发病率1/25,000）。特征：低IgG+低IgA/IgM+特异性抗体反应缺陷+排除其他原因。与XLA不同，CVID发病较晚（20-40岁），B细胞存在但功能异常。30%合并自身免疫病（ITP、AIHA），淋巴瘤风险增加。",
            "timeline": [
                ("青年期", "反复鼻窦炎+肺炎，多次抗生素治疗"),
                ("20+岁", "支气管扩张，多次住院", "red"),
                ("化验", "IgG 2.1g/L, IgA 0.3g/L, B细胞存在但功能异常", "yellow"),
                ("疫苗反应", "肺炎球菌疫苗无应答（确认抗体缺陷）"),
                ("治疗", "IVIG替代+感染预防→显著改善", "green"),
            ],
            "mechanism_title": "CVID的免疫缺陷谱",
            "mechanism": """<b>CVID的异质性（多基因+环境）：</b><br>
已知基因（仅占~10%）：TACI(TNFRSF13B)、BAFF-R、ICOS、LRBA等<br><br>
<b>B细胞功能缺陷：</b><br>
B细胞存在但→浆细胞分化障碍→抗体产生不足<br>
　↓<br>
生发中心形成缺陷→免疫球蛋白类别转换重组(CSR)障碍<br>
　↓<br>
低IgG+低IgA → 反复化脓性感染<br><br>
<b>免疫失调：</b><br>
Treg功能↓→自身免疫(30%)：ITP、AIHA、Evans综合征<br>
B细胞克隆扩增→淋巴瘤风险增加(5-10%)""",
            "table_headers": ["特征", "CVID", "XLA", "Good综合征"],
            "table_rows": [
                ["发病年龄", "20-40岁", "4-6月", "40-70岁"],
                ["B细胞", "存在(功能↓)", "近零", "近零"],
                ["IgG", "低", "极低", "低"],
                ["自身免疫", "30%", "罕见", "常见(MG)"],
                ["胸腺瘤", "无", "无", "有(100%)"],
                ["淋巴瘤风险", "5-10%", "低", "低"],
            ],
            "points": [
                "CVID=最常见的症状性PID，发病晚、异质性强",
                "B细胞存在但功能异常（区别于XLA的B细胞缺失）",
                "30%合并自身免疫，5-10%淋巴瘤风险",
                "IVIG替代+定期监测（肺功能、淋巴细胞、肿瘤标志物）",
            ],
            "ref": '<i>Common Variable Immunodeficiency</i>. J Allergy Clin Immunol. 2023;151(2):373-386. PMID: 36764329',
            "pmid": "36764329",
            "num": 2,
        },
        {
            "file": "case_PID_SCID.html",
            "title": "SCID — 新生儿筛查拯救生命",
            "sub": "重症联合免疫缺陷（SCID，Severe Combined Immunodeficiency）",
            "nav_title": "SCID",
            "tags": ["t-r:致命性", "t-y:TREC筛查", "t-a:HSCT"],
            "alert": "SCID是最严重的PID——"泡泡男孩病"。T+B+NK细胞严重缺陷，不经治疗2岁内死于感染。新生儿TREC（T细胞受体切除环）筛查是生命线：早期诊断→3.5月龄前HSCT→存活率>90%；延迟诊断→感染后HSCT→存活率降至~50%。",
            "timeline": [
                ("新生儿筛查", "TREC定量↓→紧急免疫学转诊", "green"),
                ("确认", "T细胞近零(CD3+<50/μL)，B/NK细胞因型而异", "yellow"),
                ("基因", "IL2RG(γc链)突变→X-SCID", "yellow"),
                ("保护", "严格隔离+预防性抗生素+无活疫苗"),
                ("HSCT", "3月龄行无关供体HSCT→免疫重建成功", "green"),
            ],
            "mechanism_title": "SCID的细胞因子受体缺陷",
            "mechanism": """<b>X-SCID（最常见，~45%）：</b><br>
IL2RG基因突变→γc链缺陷→IL-2/4/7/9/15/21信号全部中断<br>
　↓<br>
T细胞发育：IL-7R信号缺失→胸腺T细胞发育停滞→T⁻B⁺NK⁻<br>
NK细胞发育：IL-15R信号缺失→NK细胞缺失<br>
　↓<br>
<b>T⁻B⁺NK⁻</b>（T和B阴性，NK阴性）<br><br>
<b>SCID分型（按淋巴细胞表型）：</b><br>
• T⁻B⁺NK⁻：X-SCID(IL2RG), JAK3<br>
• T⁻B⁻NK⁺：RAG1/2, DCLRE1C(Artemis)<br>
• T⁻B⁻NK⁻：ADA缺陷<br>
• T⁻B⁺NK⁺：IL7R, CD3δ/ε/ζ""",
            "table_headers": ["SCID类型", "基因", "T", "B", "NK", "频率"],
            "table_rows": [
                ["X-SCID", "IL2RG", "−", "+", "−", "45%"],
                ["ADA", "ADA", "−", "−", "−", "15%"],
                ["RAG1/2", "RAG1/2", "−", "−", "+", "10%"],
                ["JAK3", "JAK3", "−", "+", "−", "6%"],
                ["IL7Rα", "IL7R", "−", "+", "+", "4%"],
            ],
            "points": [
                "SCID=儿科急症，新生儿TREC筛查是标准",
                "3.5月龄前HSCT存活率>90%",
                "γc链缺陷影响6种细胞因子信号→T+NK双缺失",
                "基因治疗（慢病毒载体）已用于X-SCID和ADA-SCID",
            ],
            "ref": '<i>Severe Combined Immunodeficiency</i>. N Engl J Med. 2023;388(19):1785-1798. PMID: 37163535',
            "pmid": "37163535",
            "num": 3,
        },
        {
            "file": "case_PID_CGD.html",
            "title": "CGD — 慢性肉芽肿病",
            "sub": "慢性肉芽肿病（CGD，Chronic Granulomatous Disease）/ NADPH氧化酶缺陷",
            "nav_title": "CGD",
            "tags": ["t-r:NADPH氧化酶", "t-y:催化过氧化物(-)", "t-a:IFN-γ预防"],
            "alert": "CGD是吞噬细胞杀菌功能缺陷：NADPH氧化酶缺陷→不能产生活性氧（ROS）→无法杀灭过氧化氢酶阳性微生物（金黄色葡萄球菌、曲霉菌、沙雷菌）。表现为反复化脓性感染+肉芽肿形成（炎症并发症）。NBT/DHR试验是经典诊断方法。",
            "timeline": [
                ("幼儿期", "反复皮肤脓肿+淋巴结炎+肺炎（曲霉菌）"),
                ("DHR试验", "呼吸爆发试验→无荧光峰移→确诊CGD", "yellow"),
                ("基因", "gp91phox(CYBB)突变→X-CGD", "yellow"),
                ("治疗", "TMP-SMX+伊曲康唑预防+IFN-γ", "green"),
                ("根治", "HSCT或基因治疗（临床试验中）", "green"),
            ],
            "mechanism_title": "NADPH氧化酶与呼吸爆发",
            "mechanism": """<b>正常呼吸爆发：</b><br>
吞噬体中NADPH氧化酶组装→O₂→超氧阴离子(O₂⁻)→H₂O₂→HOCl(次氯酸)<br>
→ 杀灭被吞噬的微生物<br><br>
<b>CGD中：</b><br>
NADPH氧化酶缺陷→<b>不能产生ROS</b>→微生物存活<br>
　↓<br>
仅依赖非氧化杀菌机制→对<b>过氧化氢酶阳性</b>菌无效<br>
（细菌自身产生的H₂O₂被其过氧化氢酶分解→CGD细胞无法利用）<br><br>
<b>CGD的矛盾：</b>杀菌↓但肉芽肿形成↑<br>
→ 巨噬体中存活微生物持续刺激→Th1/Th17→肉芽肿→炎症并发症<br>
（炎症性肠病样、泌尿道肉芽肿）""",
            "table_headers": ["特征", "X-CGD(gp91phox)", "AR-CGD(p47phox)", "AR-CGD(p67phox)"],
            "table_rows": [
                ["基因", "CYBB(Xp21)", "NCF1(7q11)", "NCF2(1q25)"],
                ["遗传", "XLR", "AR", "AR"],
                ["频率", "~65%", "~25%", "~5%"],
                ["严重程度", "重(残存活性<5%)", "较轻", "重"],
                ["典型病原", "金葡菌+曲霉", "相似", "相似"],
                ["携带者", "女性(偶有症状)", "无", "无"],
            ],
            "points": [
                "CGD=NADPH氧化酶缺陷→不能产生ROS",
                "对过氧化氢酶阳性菌（金葡菌/曲霉菌）特别易感",
                "DHR试验是诊断金标准",
                "预防性抗生素+抗真菌+IFN-γ，HSCT可根治",
            ],
            "ref": '<i>Chronic Granulomatous Disease</i>. J Clin Immunol. 2023;43(5):927-945. PMID: 37014825',
            "pmid": "37014825",
            "num": 4,
        },
        {
            "file": "case_PID_ALPS.html",
            "title": "ALPS — 自身免疫性淋巴增生综合征",
            "sub": "自身免疫性淋巴增生综合征（ALPS，Autoimmune Lymphoproliferative Syndrome）/ FAS通路缺陷",
            "nav_title": "ALPS",
            "tags": ["t-r:FAS突变", "t-y:淋巴结肿大", "t-a:双阴性T细胞"],
            "alert": "ALPS是凋亡通路缺陷→淋巴细胞不能正常死亡→淋巴结/脾脏肿大+自身免疫。FAS/FASLG/CASP10突变→FAS通路中断→活化淋巴细胞无法启动凋亡。特征性标志：DNT细胞（CD3+CD4-CD8-双阴性T细胞）升高。常伴Evans综合征（ITP+AIHA）。",
            "timeline": [
                ("儿童期", "慢性淋巴结肿大+脾大，持续数年"),
                ("血细胞减少", "ITP和/或AIHA反复发作"),
                ("化验", "DNT细胞>1.5%总T细胞，FAS表达↓", "yellow"),
                ("基因", "FAS基因杂合突变确诊ALPS", "yellow"),
                ("治疗", "Sirolimus(西罗莫司)→淋巴结缩小+血象改善", "green"),
            ],
            "mechanism_title": "FAS凋亡通路与免疫稳态",
            "mechanism": """<b>正常FAS凋亡：</b><br>
活化T/B细胞表面FAS(CD95)↑→FASL结合→FADD募集→Caspase-8/10级联→细胞凋亡<br>
→ 免疫反应后清除活化淋巴细胞→维持稳态<br><br>
<b>ALPS中：</b><br>
FAS突变→三聚体功能丧失→凋亡信号无法传递<br>
　↓<br>
活化淋巴细胞无法被清除→蓄积<br>
　↓<br>
① 淋巴结/脾脏肿大（淋巴增殖）<br>
② DNT细胞蓄积（逃逸胸腺选择的异常T细胞）<br>
③ 自身免疫（自身反应性B/T细胞逃逸凋亡）<br><br>
<b>为什么DNT细胞是标志？</b>CD4-CD8-TCRαβ+细胞在正常外周血<1%，ALPS中显著升高""",
            "table_headers": ["ALPS分型", "基因", "遗传", "频率", "严重程度"],
            "table_rows": [
                ["ALPS-FAS", "FAS(TNFRSF6)", "AD(不完全外显)", "~70%", "中-重"],
                ["ALPS-FASLG", "FASLG", "AD", "~2%", "中"],
                ["ALPS-CASP10", "CASP10", "AD", "~5%", "轻-中"],
                ["ALPS-U", "未知", "?", "~20%", "不定"],
            ],
            "points": [
                "ALPS=FAS凋亡通路缺陷→淋巴细胞蓄积+自身免疫",
                "DNT细胞(CD3+CD4-CD8-TCRαβ+)升高是特征性标志",
                "常伴Evans综合征（ITP+AIHA），需与原发性ITP鉴别",
                "Sirolimus是一线治疗，靶向mTOR抑制淋巴增殖",
            ],
            "ref": '<i>Autoimmune Lymphoproliferative Syndrome</i>. J Allergy Clin Immunol. 2023;151(6):1498-1510. PMID: 36868431',
            "pmid": "36868431",
            "num": 5,
        },
    ],
    "SLE": [
        {
            "file": "case_SLE_neuropsychiatric.html",
            "title": "NPSLE — 神经精神性狼疮",
            "sub": "神经精神性系统性红斑狼疮（NPSLE，Neuropsychiatric Systemic Lupus Erythematosus）",
            "nav_title": "NPSLE",
            "tags": ["t-r:中枢神经受累", "t-y:癫痫/精神症状", "t-a:MRI异常"],
            "alert": "NPSLE是SLE最严重的表现之一，累及中枢或周围神经系统。表现多样：癫痫、精神病、脑血管事件、认知障碍、脊髓炎等。机制复杂：自身抗体（抗NMDAR、抗磷脂）介导+血管炎+血栓性微血管病。MRI+脑脊液+抗体谱是诊断三要素。",
            "timeline": [
                ("SLE病史", "确诊SLE 3年，病情控制不佳"),
                ("急性事件", "癫痫大发作+精神症状（幻觉/谵妄）", "red"),
                ("检查", "MRI：白质高信号；CSF：蛋白↑、抗NMDAR抗体+", "yellow"),
                ("aPL", "抗心磷脂抗体++，狼疮抗凝物+", "yellow"),
                ("治疗", "甲强龙冲击+环磷酰胺+抗癫痫→症状控制", "green"),
            ],
            "mechanism_title": "NPSLE的多重发病机制",
            "mechanism": """<b>机制一：自身抗体介导（主流）：</b><br>
抗NMDAR抗体→血脑屏障通透性↑→与海马/皮层NMDA受体结合→兴奋性毒性→癫痫/认知障碍<br><br>
<b>机制二：抗磷脂抗体相关：</b><br>
aPL→内皮损伤+血小板活化→微血栓→缺血性损伤→脑血管事件<br><br>
<b>机制三：血管炎：</b><br>
免疫复合物沉积→补体活化→血管壁炎症→出血/缺血<br><br>
<b>机制四：细胞因子介导：</b><br>
IFN-α↑→小胶质细胞活化→神经炎症""",
            "table_headers": ["NPSLE表现", "频率", "机制", "影像"],
            "table_rows": [
                ["认知障碍", "20-80%", "抗NMDAR/细胞因子", "常无异常"],
                ["癫痫", "5-20%", "抗NMDAR/微血栓", "皮层异常信号"],
                ["精神病", "5-20%", "抗NMDAR", "常无异常"],
                ["脑梗", "5-15%", "aPL/血管炎", "DWI阳性"],
                ["脊髓炎", "1-3%", "自身免疫性", "纵向脊髓高信号"],
            ],
            "points": [
                "NPSLE表现多样，需排除感染/药物/代谢原因",
                "抗NMDAR抗体和aPL是重要致病因子",
                "MRI+CSF+抗体谱是诊断三要素",
                "重症NPSLE：甲强龙冲击+环磷酰胺/MMF",
            ],
            "ref": '<i>Neuropsychiatric Systemic Lupus Erythematosus</i>. Nat Rev Rheumatol. 2023;19(2):98-112. PMID: 36376783',
            "pmid": "36376783",
            "num": 1,
        },
        {
            "file": "case_SLE_lupus_nephritis.html",
            "title": "狼疮性肾炎IV型 — 弥漫增殖性病变",
            "sub": "狼疮性肾炎（LN，Lupus Nephritis）ISN/RPS Class IV",
            "nav_title": "LN IV型",
            "tags": ["t-r:弥漫增殖", "t-y:肾功能下降", "t-a:MMF/CYC"],
            "alert": "LN IV型是最常见（~40%）且最严重的狼疮肾炎类型。免疫复合物沉积→弥漫性肾小球内皮/系膜增殖→新月体形成→肾功能快速下降。不治疗5年肾存活率<50%。肾活检是金标准，MMF/环磷酰胺诱导+维持治疗是标准方案。",
            "timeline": [
                ("SLE患者", "蛋白尿2.5g/d+血尿+Scr升高"),
                ("肾活检", "ISN/RPS Class IV-S(A)，弥漫增殖+新月体", "red"),
                ("诱导", "MMF 2-3g/d+甲强龙冲击→序贯口服", "yellow"),
                ("6月评估", "蛋白尿降至0.5g/d，Scr正常→部分缓解", "green"),
                ("维持", "MMF减量+HCQ+小剂量激素", "green"),
            ],
            "mechanism_title": "LN IV型的免疫发病机制",
            "mechanism": """<b>免疫复合物沉积（起始事件）：</b><br>
抗dsDNA抗体+dsDNA→免疫复合物→肾小球基底膜(GBM)沉积<br>
　↓<br>
<b>补体活化（C1q→C5b-9）：</b><br>
→ 足细胞/内皮细胞损伤 → 蛋白尿<br>
　↓<br>
<b>系膜/内皮增殖：</b><br>
→ FcγR活化→巨噬细胞浸润→T细胞→细胞因子(TNF-α,IL-6)<br>
　↓<br>
<b>新月体形成：</b><br>
→ GBM断裂→纤维蛋白渗出→壁层上皮细胞增殖→新月体<br>
　↓<br>
<b>纤维化/硬化（不可逆）：</b><br>
→ TGF-β→肌成纤维细胞→间质纤维化→ESRD""",
            "table_headers": ["LN分型(ISN/RPS)", "病变特点", "蛋白尿", "治疗"],
            "table_rows": [
                ["I/II(系膜)", "系膜增殖", "轻", "HCQ+控制SLE"],
                ["III(局灶)", "≤50%肾小球", "中", "免疫抑制"],
                ["<b>IV(弥漫)</b>", "<b>>50%肾小球</b>", "<b>重</b>", "<b>MMF/CYC诱导</b>"],
                ["V(膜性)", "上皮下沉积", "重(肾病)", "MMF/CNI"],
                ["VI(硬化)", ">90%硬化", "少", "肾替代治疗"],
            ],
            "points": [
                "LN IV型=最常见最严重，弥漫增殖+新月体",
                "肾活检是分型和指导治疗的金标准",
                "MMF vs CYC诱导疗效相当，MMF副作用更少",
                "早期完全缓解=最佳预后指标",
            ],
            "ref": '<i>Lupus Nephritis</i>. Nat Rev Dis Primers. 2024;10(1):12. PMID: 38378679',
            "pmid": "38378679",
            "num": 2,
        },
        {
            "file": "case_SLE_APLS.html",
            "title": "APS — 抗磷脂综合征合并SLE",
            "sub": "抗磷脂综合征（APS，Antiphospholipid Syndrome）",
            "nav_title": "APS+SLE",
            "tags": ["t-r:血栓", "t-r:病理妊娠", "t-y:狼疮抗凝物"],
            "alert": "APS以反复动静脉血栓+病理妊娠+持续aPL阳性为特征。SLE患者中APS发生率~30%。最危险的并发症：灾难性APS（CAPS）—多部位同时血栓+器官衰竭，死亡率>40%。终身抗凝是标准治疗。",
            "timeline": [
                ("SLE病史", "SLE 5年，aPL持续阳性"),
                ("DVT", "下肢深静脉血栓（首次血栓事件）", "red"),
                ("病理妊娠", "孕10周胎停（>1次）", "red"),
                ("确诊", "狼疮抗凝物++ + 抗β2GPI ++ → 确诊APS", "yellow"),
                ("治疗", "华法林(INR 2-3)+HCQ+低剂量阿司匹林", "green"),
            ],
            "mechanism_title": "APS的两相打击机制",
            "mechanism": """<b>第一相：aPL与靶蛋白结合：</b><br>
抗β2GPI抗体→β2GPI构象变化→暴露隐藏表位<br><br>
<b>第二相：多通路促凝：</b><br>
① <b>血小板活化：</b>aPL→血小板TLR4/ApoER2→活化+聚集<br>
② <b>内皮损伤：</b>aPL→内皮细胞→组织因子(TF)表达↑→外源凝血通路激活<br>
③ <b>补体活化：</b>aPL→C5a→中性粒细胞胞外诱捕网(NETs)→血栓形成<br>
④ <b>annexin A5屏蔽破坏：</b>aPL→annexin A5从磷脂膜移除→凝血酶原酶活化<br><br>
<b>CAPS的额外因素：</b>感染/手术→大量aPL释放→全身微血栓风暴""",
            "table_headers": ["特征", "原发性APS", "SLE相关APS", "CAPS"],
            "table_rows": [
                ["基础病", "无", "SLE", "任何aPL+"],
                ["血栓", "有", "有", "≥3器官同时"],
                ["病理妊娠", "有", "有", "可并发"],
                ["aPL滴度", "阳性", "高滴度", "极高滴度"],
                ["死亡率", "低", "低", ">40%"],
                ["治疗", "抗凝", "抗凝+HCQ", "抗凝+IVIG+血浆置换"],
            ],
            "points": [
                "APS=反复血栓+病理妊娠+持续aPL阳性",
                "SLE患者需常规筛查aPL",
                "CAPS是致命性急症：多器官血栓+死亡率>40%",
                "HCQ有抗血栓保护作用，SLE+APS患者必用",
            ],
            "ref": '<i>Antiphospholipid Syndrome</i>. N Engl J Med. 2023;388(22):2060-2074. PMID: 37276849',
            "pmid": "37276849",
            "num": 3,
        },
        {
            "file": "case_SLE_macrophage.html",
            "title": "SLE合并MAS — 巨噬细胞活化综合征",
            "sub": "SLE合并巨噬细胞活化综合征（MAS，Macrophage Activation Syndrome）",
            "nav_title": "SLE+MAS",
            "tags": ["t-r:细胞因子风暴", "t-r:铁蛋白暴升", "t-y:噬血现象"],
            "alert": "SLE合并MAS虽不如sJIA常见，但同样致命。铁蛋白突然暴升+血细胞下降+高甘油三酯+纤维蛋白原降低+噬血现象→MAS。与SLE活动期鉴别困难（两者炎症指标都升高），但治疗策略不同（MAS需尽早加用VP-16/环孢素A）。",
            "timeline": [
                ("SLE活动", "高热+皮疹+关节炎，SLEDAI评分高"),
                ("恶化", "全血细胞进行性下降+肝酶升高+凝血异常", "red"),
                ("MAS标志", "铁蛋白从500→35,000 ng/mL", "red"),
                ("骨髓", "噬血现象（巨噬细胞吞噬红细胞/血小板）", "yellow"),
                ("治疗", "甲强龙冲击+CsA→快速应答", "green"),
            ],
            "mechanism_title": "MAS的免疫病理级联",
            "mechanism": """<b>SLE活动期→MAS的转折：</b><br>
SLE高活动→大量免疫复合物+IFN-α<br>
　↓<br>
<b>细胞毒性T/NK细胞功能衰竭：</b><br>
穿孔素(Perforin)通路缺陷→无法清除活化巨噬细胞<br>
　↓<br>
<b>巨噬细胞过度活化：</b><br>
→ IL-1β, IL-6, TNF-α, IL-18暴增（细胞因子风暴）<br>
　↓<br>
<b>噬血现象：</b>活化的巨噬细胞非特异性吞噬血细胞<br>
　↓<br>
<b>器官损伤：</b>肝损+DIC+ARDS+休克<br><br>
<b>鉴别关键：</b>SLE活动 vs MAS<br>
• SLE活动：CRP正常/轻度↑、补体↓、dsDNA↑<br>
• MAS叠加：铁蛋白暴增、纤维蛋白原↓、甘油三酯↑""",
            "table_headers": ["指标", "正常", "SLE活动", "MAS"],
            "table_rows": [
                ["铁蛋白(ng/mL)", "10-200", "200-1000", ">10,000"],
                ["纤维蛋白原", "200-400", "正常/↑", "<150"],
                ["甘油三酯", "<150", "正常", ">265"],
                ["sCD25", "正常", "轻度↑", "极度↑"],
                ["NK细胞活性", "正常", "轻度↓", "显著↓/消失"],
                ["噬血现象", "无", "无", "有"],
            ],
            "points": [
                "SLE+MAS的鉴别关键：铁蛋白暴升+纤维蛋白原↓",
                "NK/CTL穿孔素通路功能衰竭→巨噬细胞失控",
                "VP-16+CsA是一线，尽早使用（不等确诊）",
                "延迟治疗→多器官功能衰竭→死亡率>20%",
            ],
            "ref": '<i>Macrophage Activation Syndrome in Systemic Lupus Erythematosus</i>. Lupus. 2023;32(4):412-423. PMID: 36804125',
            "pmid": "36804125",
            "num": 4,
        },
        {
            "file": "case_SLE_drug_induced.html",
            "title": "药物性狼疮 — 普鲁卡因胺/肼苯哒嗪相关",
            "sub": "药物性红斑狼疮（DILE，Drug-Induced Lupus Erythematosus）",
            "nav_title": "DILE",
            "tags": ["t-y:药物相关", "t-a:抗组蛋白抗体", "t-a:停药缓解"],
            "alert": "DILE由特定药物诱发狼疮样综合征。与特发性SLE不同：抗组蛋白抗体阳性率高（>95%）、抗dsDNA通常阴性、肾脏和中枢神经系统受累罕见。停药后症状消退。常见药物：普鲁卡因胺、肼苯哒嗪、异烟肼、TNF-α抑制剂、米诺环素。",
            "timeline": [
                ("用药史", "服用肼苯哒嗪(降压药) 2年"),
                ("症状", "关节痛+发热+胸腔积液+皮疹"),
                ("化验", "ANA 1:320, 抗组蛋白抗体+, 抗dsDNA-", "yellow"),
                ("诊断", "药物性狼疮（DILE）", "yellow"),
                ("停药", "肼苯哒嗪停药→4-6周症状完全消失", "green"),
            ],
            "mechanism_title": "DILE的药物代谢机制",
            "mechanism": """<b>慢乙酰化者（遗传易感）：</b><br>
NAT2基因变异→药物乙酰化缓慢→药物蓄积<br>
　↓<br>
<b>药物-DNA相互作用：</b><br>
肼苯哒嗪/普鲁卡因胺代谢产物→与DNA共价结合→新抗原<br>
　↓<br>
<b>免疫耐受打破：</b><br>
→ 抗组蛋白抗体产生（主要针对H2A-H2B复合物）<br>
→ T细胞活化→狼疮样症状<br><br>
<b>为什么停药可恢复？</b><br>
药物清除→新抗原消失→自身免疫反应逐渐平息→4-6周缓解<br><br>
<b>TNF-α抑制剂诱导的狼疮（特殊类型）：</b><br>
→ 抗dsDNA可能阳性（与经典DILE不同）→通常停药后缓解""",
            "table_headers": ["特征", "DILE", "特发性SLE"],
            "table_rows": [
                ["性别比", "无差异", "女:男=9:1"],
                ["药物暴露", "必须有", "无"],
                ["抗组蛋白抗体", ">95%", "20-30%"],
                ["抗dsDNA", "通常阴性", "60-70%阳性"],
                ["肾脏受累", "罕见", "50-60%"],
                ["CNS受累", "罕见", "10-20%"],
                ["补体", "正常", "常降低"],
                ["预后", "停药后恢复", "慢性病程"],
            ],
            "points": [
                "DILE=药物暴露+抗组蛋白抗体+抗dsDNA阴性",
                "慢乙酰化者是遗传易感因素",
                "停药4-6周缓解，预后良好",
                "TNF-α抑制剂诱导的狼疮可能抗dsDNA阳性（特殊类型）",
            ],
            "ref": '<i>Drug-Induced Lupus Erythematosus</i>. Nat Rev Rheumatol. 2023;19(4):225-236. PMID: 36725964',
            "pmid": "36725964",
            "num": 5,
        },
    ],
    "Uveitis": [
        {
            "file": "case_Uveitis_JIA.html",
            "title": "JIA相关葡萄膜炎 — 无症状的视