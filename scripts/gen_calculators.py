#!/usr/bin/env python3
"""Generate interactive clinical calculator HTML files for MedWiki-Rheum."""

import os

TEAL = "#20a39e"
TEAL_DARK = "#178f8a"

COMMON_HEAD = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — MedWiki-Rheum</title>
<script src="https://cdn.tailwindcss.com"></script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&display=swap');
:root{{--bg:#f8fafb;--surface:#fff;--text:#1e293b;--text2:#64748b;--accent:#20a39e;--accent-dark:#178f8a;--accent-bg:#e6f5f4;--border:#e0edec;--green:#22a87e;--green-bg:#e2f8ef;--yellow:#d4892a;--yellow-bg:#fef3e2;--red:#d45050;--red-bg:#fde8e8;--radius:14px;}}
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{font-family:'Noto Sans SC','Inter',sans-serif;background:var(--bg);color:var(--text);line-height:1.5;font-size:13px;}}
.wrap{{max-width:720px;margin:0 auto;padding:56px 12px 180px;}}
.card{{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:20px;margin-bottom:16px;box-shadow:0 2px 8px rgba(32,163,158,0.06);}}
h1{{font-size:1.5rem;font-weight:800;margin-bottom:2px;}}
h1 span{{color:var(--accent);}}
.sub{{font-size:0.78rem;color:var(--text2);margin-bottom:12px;}}
.section-title{{font-size:0.7rem;font-weight:800;color:#fff;background:var(--accent);padding:4px 12px;border-radius:6px;display:inline-block;margin:12px 0 8px;text-transform:uppercase;letter-spacing:0.05em;}}
.section-title.red{{background:var(--red);}}
.section-title.green{{background:var(--green);}}
.section-title.yellow{{background:var(--yellow);}}
label{{display:block;font-size:0.78rem;font-weight:600;color:var(--text2);margin-bottom:3px;}}
.input-group{{margin-bottom:10px;}}
input[type=number],select{{width:100%;padding:8px 12px;border:1.5px solid var(--border);border-radius:8px;font-size:0.9rem;font-weight:600;background:#f4fafa;color:var(--text);outline:none;transition:border 0.2s;}}
input[type=number]:focus,select:focus{{border-color:var(--accent);}}
input[type=range]{{width:100%;accent-color:var(--accent);height:6px;}}
.range-row{{display:flex;justify-content:space-between;align-items:center;gap:10px;}}
.range-val{{min-width:48px;text-align:center;font-weight:800;color:var(--accent);font-size:1.1rem;}}
.btn{{padding:8px 20px;border-radius:8px;font-size:0.8rem;font-weight:700;cursor:pointer;border:none;transition:all 0.2s;}}
.btn-primary{{background:var(--accent);color:#fff;}}
.btn-primary:hover{{background:var(--accent-dark);}}
.btn-reset{{background:var(--red-bg);color:var(--red);}}
.btn-reset:hover{{background:var(--red);color:#fff;}}
.result-box{{background:linear-gradient(135deg,#f0fafa,#e6f5f4);border:1.5px solid var(--accent);border-radius:var(--radius);padding:16px;text-align:center;margin-top:12px;}}
.result-num{{font-size:2.5rem;font-weight:900;color:var(--accent);line-height:1;}}
.result-label{{font-size:0.75rem;color:var(--text2);margin-top:2px;font-weight:600;}}
.result-status{{display:inline-block;padding:4px 16px;border-radius:20px;font-size:0.8rem;font-weight:800;margin-top:8px;color:#fff;}}
table{{width:100%;border-collapse:collapse;font-size:0.75rem;margin:6px 0;}}
th{{background:var(--accent-bg);color:var(--accent);font-weight:700;text-align:left;padding:5px 8px;border-bottom:1.5px solid var(--border);}}
td{{padding:4px 8px;border-bottom:1px solid #f0f5f4;}}
tr:hover td{{background:#f8fafa;}}
.disclaimer{{font-size:0.65rem;color:var(--text2);text-align:center;margin-top:16px;padding:8px;border-top:1px solid var(--border);}}
.nav-bar{{position:fixed;top:0;left:0;right:0;z-index:1000;background:#20a39e;color:#fff;padding:6px 16px;display:flex;align-items:center;gap:12px;font-size:13px;box-shadow:0 2px 6px rgba(32,163,158,0.18);}}
.nav-bar a{{color:#fff;text-decoration:none;opacity:.85;transition:opacity .2s;}}
.nav-bar a:hover{{opacity:1;}}
.nav-bar .nav-title{{font-weight:600;margin-left:auto;opacity:.7;font-size:12px;}}
.sticky-footer{{position:fixed;bottom:0;left:0;right:0;background:rgba(255,255,255,0.94);backdrop-filter:blur(20px);border-top:1px solid var(--border);z-index:50;padding:12px 16px;padding-bottom:calc(12px + env(safe-area-inset-bottom));}}
.sticky-inner{{max-width:720px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;gap:12px;}}
.footer-score{{text-align:center;}}
.footer-score .num{{font-size:2.2rem;font-weight:900;color:var(--accent);line-height:1;}}
.footer-score .lbl{{font-size:0.6rem;color:var(--text2);font-weight:700;text-transform:uppercase;letter-spacing:0.05em;}}
.footer-status{{padding:6px 20px;border-radius:20px;font-size:0.75rem;font-weight:800;color:#fff;transition:all 0.3s;}}
.footer-path{{flex:1;font-size:0.7rem;color:var(--text2);font-style:italic;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;}}
@media(max-width:640px){{.sticky-inner{{flex-wrap:wrap;}}.footer-path{{order:3;width:100%;}}}}
</style>
<link rel="manifest" href="../manifest.json">
<meta name="theme-color" content="#20a39e">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="MedWiki">
<link rel="apple-touch-icon" href="../icons/icon-192.png">
</head>
<body>
<div class="nav-bar"><a href="../index.html">🏠</a><a href="../index.html#topics">📖</a><a href="../index.html#drugs">💊</a><a href="../index.html#tools">🔬</a><span class="nav-title">{nav_title}</span></div>
<div class="wrap">
'''

COMMON_FOOTER = '''
<div class="disclaimer">⚠️ 本工具仅供临床参考，不构成诊疗建议。最终决策请结合临床实际并遵循相关指南。</div>
</div>
<div class="sticky-footer"><div class="sticky-inner">
<div class="footer-path" id="pathLine">输入参数后自动计算...</div>
<div class="footer-score"><div class="lbl">Score</div><div class="num" id="footerScore">—</div></div>
<div class="footer-status" id="footerStatus" style="background:#cbd5e1;color:#fff">待评估</div>
</div></div>
<script>if('serviceWorker' in navigator){{navigator.serviceWorker.register('../sw.js').catch(()=>{{}})}}</script>
</body></html>'''


def write_file(name, content):
    path = os.path.expanduser(f"~/MedWiki-Rheum/tools/{name}")
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ {name} ({len(content)} bytes)")


def gen_jadas27():
    html = COMMON_HEAD.format(title="JADAS-27 交互式评分", nav_title="JADAS-27 评分") + '''
<div class="card">
<h1>JADAS <span>- 27</span></h1>
<div class="sub">Juvenile Arthritis Disease Activity Score · 儿童JIA金标准 · Consolaro 2012</div>

<div class="section-title">📐 输入参数</div>

<div class="input-group">
<label>活动关节数（Active Joint Count, 0-27）</label>
<input type="range" id="joints" min="0" max="27" value="0" oninput="calc()">
<div class="range-row"><span>0</span><span class="range-val" id="joints_val">0</span><span>27</span></div>
</div>

<div class="input-group">
<label>医生整体评估 PhGA（Physician Global Assessment, 0-10 cm VAS）</label>
<input type="range" id="phga" min="0" max="10" step="0.1" value="0" oninput="calc()">
<div class="range-row"><span>0</span><span class="range-val" id="phga_val">0.0</span><span>10</span></div>
</div>

<div class="input-group">
<label>患者/家长整体评估 PtGA（Parent Global Assessment, 0-10 cm VAS）</label>
<input type="range" id="ptga" min="0" max="10" step="0.1" value="0" oninput="calc()">
<div class="range-row"><span>0</span><span class="range-val" id="ptga_val">0.0</span><span>10</span></div>
</div>

<div class="input-group">
<label>ESR（红细胞沉降率, mm/h）</label>
<input type="number" id="esr" min="0" max="150" value="10" oninput="calc()" placeholder="输入ESR值">
</div>

<div class="section-title green">📊 计算结果</div>
<div class="result-box">
<div class="result-label">JADAS-27 评分（范围 0-57）</div>
<div class="result-num" id="score">0.0</div>
<div class="result-status" id="status" style="background:#22a87e">不活动</div>
</div>
</div>

<div class="card">
<div class="section-title yellow">📝 ESR归一化规则</div>
<table><tr><th>ESR值</th><th>归一化分数</th></tr>
<tr><td>≤ 20 mm/h</td><td style="color:#22a87e;font-weight:700">0 分</td></tr>
<tr><td>&gt; 20 mm/h</td><td>ESR ÷ 10，上限10分</td></tr></table>

<div class="section-title red">🎯 儿科疾病活动度分级</div>
<table><tr><th>JADAS-27</th><th>活动度</th><th>临床意义</th></tr>
<tr><td style="font-weight:700;color:#22a87e">≤ 1.0</td><td style="font-weight:700;color:#22a87e">不活动</td><td>治疗达标，考虑减量</td></tr>
<tr><td>1.1 – 3.8</td><td>低活动度</td><td>接近达标</td></tr>
<tr><td style="font-weight:700;color:#d4892a">3.9 – 10.5</td><td style="font-weight:700;color:#d4892a">中活动度</td><td>考虑升级治疗</td></tr>
<tr><td style="font-weight:700;color:#d45050">&gt; 10.5</td><td style="font-weight:700;color:#d45050">高活动度</td><td>强化治疗</td></tr></table>
<div class="disclaimer" style="border:none;margin-top:4px">参考: Consolaro et al. Arthritis Care Res 2012 · 目标: 不活动 ≤ 1.0</div>
</div>

<script>
function calc(){
  const j=+document.getElementById('joints').value;
  const p=+document.getElementById('phga').value;
  const t=+document.getElementById('ptga').value;
  const e=+document.getElementById('esr').value||0;
  document.getElementById('joints_val').textContent=j;
  document.getElementById('phga_val').textContent=p.toFixed(1);
  document.getElementById('ptga_val').textContent=t.toFixed(1);
  const esrNorm=e<=20?0:Math.min(10,e/10);
  const score=j+p+t+esrNorm;
  document.getElementById('score').textContent=score.toFixed(1);
  const fs=document.getElementById('footerScore');
  const st=document.getElementById('status');
  const fst=document.getElementById('footerStatus');
  const path=document.getElementById('pathLine');
  const parts=[`活动关节${j}`,`PhGA ${p.toFixed(1)}`,`PtGA ${t.toFixed(1)}`,`ESR归一化 ${esrNorm.toFixed(1)}`];
  path.textContent=parts.join(' + ');
  fs.textContent=score.toFixed(1);
  let label,c;
  if(score<=1.0){label="不活动";c="#22a87e";}
  else if(score<=3.8){label="低活动度";c="#20a39e";}
  else if(score<=10.5){label="中活动度";c="#d4892a";}
  else{label="高活动度";c="#d45050";}
  st.textContent=label;st.style.background=c;
  fst.textContent=label;fst.style.background=c;
}
calc();
</script>
''' + COMMON_FOOTER
    write_file("JADAS27.html", html)


def gen_jadas71():
    html = COMMON_HEAD.format(title="JADAS-71 交互式评分", nav_title="JADAS-71 评分") + '''
<div class="card">
<h1>JADAS <span>- 71</span></h1>
<div class="sub">Juvenile Arthritis Disease Activity Score · 71关节评估 · 扩展版</div>

<div class="section-title">📐 输入参数</div>

<div class="input-group">
<label>活动关节数（Active Joint Count, 0-71）</label>
<input type="range" id="joints" min="0" max="71" value="0" oninput="calc()">
<div class="range-row"><span>0</span><span class="range-val" id="joints_val">0</span><span>71</span></div>
</div>

<div class="input-group">
<label>医生整体评估 PhGA（0-10 cm VAS）</label>
<input type="range" id="phga" min="0" max="10" step="0.1" value="0" oninput="calc()">
<div class="range-row"><span>0</span><span class="range-val" id="phga_val">0.0</span><span>10</span></div>
</div>

<div class="input-group">
<label>患者/家长整体评估 PtGA（0-10 cm VAS）</label>
<input type="range" id="ptga" min="0" max="10" step="0.1" value="0" oninput="calc()">
<div class="range-row"><span>0</span><span class="range-val" id="ptga_val">0.0</span><span>10</span></div>
</div>

<div class="input-group">
<label>ESR（红细胞沉降率, mm/h）</label>
<input type="number" id="esr" min="0" max="150" value="10" oninput="calc()">
</div>

<div class="section-title green">📊 计算结果</div>
<div class="result-box">
<div class="result-label">JADAS-71 评分</div>
<div class="result-num" id="score">0.0</div>
<div class="result-status" id="status" style="background:#22a87e">不活动</div>
</div>
</div>

<div class="card">
<div class="section-title">ℹ️ JADAS-71 vs JADAS-27</div>
<table><tr><th>版本</th><th>关节数</th><th>适用</th></tr>
<tr><td>JADAS-27</td><td>27关节</td><td>日常临床首选</td></tr>
<tr><td style="font-weight:700;color:#20a39e">JADAS-71</td><td>71关节</td><td>全面评估（含手足小关节）</td></tr></table>
<p style="font-size:0.72rem;color:#64748b;margin-top:6px">JADAS-71使用相同的评分公式和分级标准，仅关节数上限不同（71 vs 27）。总分上限 = 71+10+10+10 = 101。</p>
</div>

<script>
function calc(){
  const j=+document.getElementById('joints').value;
  const p=+document.getElementById('phga').value;
  const t=+document.getElementById('ptga').value;
  const e=+document.getElementById('esr').value||0;
  document.getElementById('joints_val').textContent=j;
  document.getElementById('phga_val').textContent=p.toFixed(1);
  document.getElementById('ptga_val').textContent=t.toFixed(1);
  const esrNorm=e<=20?0:Math.min(10,e/10);
  const score=j+p+t+esrNorm;
  document.getElementById('score').textContent=score.toFixed(1);
  const fs=document.getElementById('footerScore');
  const st=document.getElementById('status');
  const fst=document.getElementById('footerStatus');
  const path=document.getElementById('pathLine');
  const parts=[`活动关节${j}`,`PhGA ${p.toFixed(1)}`,`PtGA ${t.toFixed(1)}`,`ESR归一化 ${esrNorm.toFixed(1)}`];
  path.textContent=parts.join(' + ');
  fs.textContent=score.toFixed(1);
  let label,c;
  if(score<=1.0){label="不活动";c="#22a87e";}
  else if(score<=3.8){label="低活动度";c="#20a39e";}
  else if(score<=10.5){label="中活动度";c="#d4892a";}
  else{label="高活动度";c="#d45050";}
  st.textContent=label;st.style.background=c;
  fst.textContent=label;fst.style.background=c;
}
calc();
</script>
''' + COMMON_FOOTER
    write_file("JADAS71.html", html)


def gen_das28():
    html = COMMON_HEAD.format(title="DAS28 交互式评分", nav_title="DAS28 评分") + '''
<div class="card">
<h1>DAS <span>- 28</span></h1>
<div class="sub">Disease Activity Score · 28关节 · 大龄青少年/成人适用</div>

<div class="section-title">📐 选择计算方式</div>
<div style="display:flex;gap:8px;margin-bottom:10px">
<button class="btn btn-primary" id="btn_esr" onclick="switchMode('esr')">DAS28-ESR</button>
<button class="btn" id="btn_crp" onclick="switchMode('crp')" style="background:#e6f5f4;color:#20a39e">DAS28-CRP</button>
</div>

<div class="input-group">
<label>压痛关节数 TJC28（Tender Joint Count, 0-28）</label>
<input type="range" id="tjc" min="0" max="28" value="0" oninput="calc()">
<div class="range-row"><span>0</span><span class="range-val" id="tjc_val">0</span><span>28</span></div>
</div>

<div class="input-group">
<label>肿胀关节数 SJC28（Swollen Joint Count, 0-28）</label>
<input type="range" id="sjc" min="0" max="28" value="0" oninput="calc()">
<div class="range-row"><span>0</span><span class="range-val" id="sjc_val">0</span><span>28</span></div>
</div>

<div class="input-group" id="esr_group">
<label>ESR（红细胞沉降率, mm/h）</label>
<input type="number" id="esr" min="1" max="150" value="10" oninput="calc()">
</div>

<div class="input-group" id="crp_group" style="display:none">
<label>CRP（C反应蛋白, mg/L）</label>
<input type="number" id="crp" min="0" max="300" value="5" oninput="calc()">
</div>

<div class="input-group">
<label>患者整体评估 GH（General Health, 0-100 mm VAS）</label>
<input type="range" id="gh" min="0" max="100" value="0" oninput="calc()">
<div class="range-row"><span>0</span><span class="range-val" id="gh_val">0</span><span>100</span></div>
</div>

<div class="section-title green">📊 计算结果</div>
<div class="result-box">
<div class="result-label" id="result_label">DAS28-ESR</div>
<div class="result-num" id="score">0.00</div>
<div class="result-status" id="status" style="background:#22a87e">缓解</div>
</div>
</div>

<div class="card">
<div class="section-title red">🎯 DAS28分级标准</div>
<table><tr><th>DAS28</th><th>活动度</th></tr>
<tr><td style="font-weight:700;color:#22a87e">&lt; 2.6</td><td style="font-weight:700;color:#22a87e">缓解 Remission</td></tr>
<tr><td>2.6 – 3.2</td><td>低活动度</td></tr>
<tr><td style="color:#d4892a;font-weight:700">3.2 – 5.1</td><td style="color:#d4892a;font-weight:700">中活动度</td></tr>
<tr><td style="color:#d45050;font-weight:700">&gt; 5.1</td><td style="color:#d45050;font-weight:700">高活动度</td></tr></table>
<div class="disclaimer" style="border:none;margin-top:4px">⚠️ DAS28主要用于成人RA，大龄青少年(≥16岁)亦可使用。低龄儿童请首选JADAS-27。</div>
</div>

<script>
let mode='esr';
function switchMode(m){
  mode=m;
  document.getElementById('esr_group').style.display=m==='esr'?'block':'none';
  document.getElementById('crp_group').style.display=m==='crp'?'block':'none';
  document.getElementById('btn_esr').className='btn '+(m==='esr'?'btn-primary':'');
  document.getElementById('btn_crp').className='btn '+(m==='crp'?'btn-primary':'');
  document.getElementById('btn_esr').style.background=m==='esr'?'#20a39e':'#e6f5f4';
  document.getElementById('btn_esr').style.color=m==='esr'?'#fff':'#20a39e';
  document.getElementById('btn_crp').style.background=m==='crp'?'#20a39e':'#e6f5f4';
  document.getElementById('btn_crp').style.color=m==='crp'?'#fff':'#20a39e';
  document.getElementById('result_label').textContent=m==='esr'?'DAS28-ESR':'DAS28-CRP';
  calc();
}
function calc(){
  const tjc=+document.getElementById('tjc').value;
  const sjc=+document.getElementById('sjc').value;
  const gh=+document.getElementById('gh').value;
  document.getElementById('tjc_val').textContent=tjc;
  document.getElementById('sjc_val').textContent=sjc;
  document.getElementById('gh_val').textContent=gh;
  let score;
  if(mode==='esr'){
    const esr=Math.max(1,+document.getElementById('esr').value||1);
    score=0.56*Math.sqrt(tjc)+0.28*Math.sqrt(sjc)+0.70*Math.log(esr+1)+0.014*gh;
  }else{
    const crp=Math.max(0,+document.getElementById('crp').value||0);
    score=0.56*Math.sqrt(tjc)+0.28*Math.sqrt(sjc)+0.36*Math.log(crp+1)+0.014*gh+0.96;
  }
  document.getElementById('score').textContent=score.toFixed(2);
  document.getElementById('footerScore').textContent=score.toFixed(2);
  let label,c;
  if(score<2.6){label="缓解";c="#22a87e";}
  else if(score<=3.2){label="低活动度";c="#20a39e";}
  else if(score<=5.1){label="中活动度";c="#d4892a";}
  else{label="高活动度";c="#d45050";}
  document.getElementById('status').textContent=label;
  document.getElementById('status').style.background=c;
  document.getElementById('footerStatus').textContent=label;
  document.getElementById('footerStatus').style.background=c;
  document.getElementById('pathLine').textContent=`TJC${tjc} + SJC${sjc} + GH${gh}`+(mode==='esr'?` + ESR`:` + CRP`);
}
calc();
</script>
''' + COMMON_FOOTER
    write_file("DAS28.html", html)


def gen_cdai():
    html = COMMON_HEAD.format(title="CDAI 交互式评分", nav_title="CDAI 评分") + '''
<div class="card">
<h1>CDAI</h1>
<div class="sub">Clinical Disease Activity Index · 临床疾病活动指数</div>

<div class="section-title">📐 输入参数</div>

<div class="input-group">
<label>压痛关节数 TJC28（0-28）</label>
<input type="range" id="tjc" min="0" max="28" value="0" oninput="calc()">
<div class="range-row"><span>0</span><span class="range-val" id="tjc_val">0</span><span>28</span></div>
</div>

<div class="input-group">
<label>肿胀关节数 SJC28（0-28）</label>
<input type="range" id="sjc" min="0" max="28" value="0" oninput="calc()">
<div class="range-row"><span>0</span><span class="range-val" id="sjc_val">0</span><span>28</span></div>
</div>

<div class="input-group">
<label>医生整体评估 PhGA（0-10 cm VAS）</label>
<input type="range" id="phga" min="0" max="10" step="0.1" value="0" oninput="calc()">
<div class="range-row"><span>0</span><span class="range-val" id="phga_val">0.0</span><span>10</span></div>
</div>

<div class="input-group">
<label>患者整体评估 PtGA（0-10 cm VAS）</label>
<input type="range" id="ptga" min="0" max="10" step="0.1" value="0" oninput="calc()">
<div class="range-row"><span>0</span><span class="range-val" id="ptga_val">0.0</span><span>10</span></div>
</div>

<div class="section-title green">📊 计算结果</div>
<div class="result-box">
<div class="result-label">CDAI = TJC + SJC + PhGA + PtGA</div>
<div class="result-num" id="score">0.0</div>
<div class="result-status" id="status" style="background:#22a87e">缓解</div>
</div>
</div>

<div class="card">
<div class="section-title red">🎯 CDAI分级</div>
<table><tr><th>CDAI</th><th>活动度</th></tr>
<tr><td style="font-weight:700;color:#22a87e">≤ 2.8</td><td style="font-weight:700;color:#22a87e">缓解</td></tr>
<tr><td>2.9 – 10.0</td><td>低活动度</td></tr>
<tr><td style="font-weight:700;color:#d4892a">10.1 – 22.0</td><td style="font-weight:700;color:#d4892a">中活动度</td></tr>
<tr><td style="font-weight:700;color:#d45050">&gt; 22.0</td><td style="font-weight:700;color:#d45050">高活动度</td></tr></table>
</div>

<script>
function calc(){
  const tjc=+document.getElementById('tjc').value;
  const sjc=+document.getElementById('sjc').value;
  const phga=+document.getElementById('phga').value;
  const ptga=+document.getElementById('ptga').value;
  document.getElementById('tjc_val').textContent=tjc;
  document.getElementById('sjc_val').textContent=sjc;
  document.getElementById('phga_val').textContent=phga.toFixed(1);
  document.getElementById('ptga_val').textContent=ptga.toFixed(1);
  const score=tjc+sjc+phga+ptga;
  document.getElementById('score').textContent=score.toFixed(1);
  document.getElementById('footerScore').textContent=score.toFixed(1);
  let label,c;
  if(score<=2.8){label="缓解";c="#22a87e";}
  else if(score<=10){label="低活动度";c="#20a39e";}
  else if(score<=22){label="中活动度";c="#d4892a";}
  else{label="高活动度";c="#d45050";}
  document.getElementById('status').textContent=label;document.getElementById('status').style.background=c;
  document.getElementById('footerStatus').textContent=label;document.getElementById('footerStatus').style.background=c;
  document.getElementById('pathLine').textContent=`TJC${tjc}+SJC${sjc}+PhGA${phga.toFixed(1)}+PtGA${ptga.toFixed(1)}`;
}
calc();
</script>
''' + COMMON_FOOTER
    write_file("CDAI.html", html)


def gen_sdai():
    html = COMMON_HEAD.format(title="SDAI 交互式评分", nav_title="SDAI 评分") + '''
<div class="card">
<h1>SDAI</h1>
<div class="sub">Simplified Disease Activity Index · 简化疾病活动指数</div>

<div class="section-title">📐 输入参数</div>

<div class="input-group">
<label>压痛关节数 TJC28（0-28）</label>
<input type="range" id="tjc" min="0" max="28" value="0" oninput="calc()">
<div class="range-row"><span>0</span><span class="range-val" id="tjc_val">0</span><span>28</span></div>
</div>

<div class="input-group">
<label>肿胀关节数 SJC28（0-28）</label>
<input type="range" id="sjc" min="0" max="28" value="0" oninput="calc()">
<div class="range-row"><span>0</span><span class="range-val" id="sjc_val">0</span><span>28</span></div>
</div>

<div class="input-group">
<label>医生整体评估 PhGA（0-10 cm VAS）</label>
<input type="range" id="phga" min="0" max="10" step="0.1" value="0" oninput="calc()">
<div class="range-row"><span>0</span><span class="range-val" id="phga_val">0.0</span><span>10</span></div>
</div>

<div class="input-group">
<label>患者整体评估 PtGA（0-10 cm VAS）</label>
<input type="range" id="ptga" min="0" max="10" step="0.1" value="0" oninput="calc()">
<div class="range-row"><span>0</span><span class="range-val" id="ptga_val">0.0</span><span>10</span></div>
</div>

<div class="input-group">
<label>CRP（C反应蛋白, mg/dL）</label>
<input type="number" id="crp" min="0" max="20" step="0.1" value="0.5" oninput="calc()">
</div>

<div class="section-title green">📊 计算结果</div>
<div class="result-box">
<div class="result-label">SDAI = TJC + SJC + PhGA + PtGA + CRP</div>
<div class="result-num" id="score">0.0</div>
<div class="result-status" id="status" style="background:#22a87e">缓解</div>
</div>
</div>

<div class="card">
<div class="section-title red">🎯 SDAI分级</div>
<table><tr><th>SDAI</th><th>活动度</th></tr>
<tr><td style="font-weight:700;color:#22a87e">≤ 3.3</td><td style="font-weight:700;color:#22a87e">缓解</td></tr>
<tr><td>3.4 – 11.0</td><td>低活动度</td></tr>
<tr><td style="font-weight:700;color:#d4892a">11.1 – 26.0</td><td style="font-weight:700;color:#d4892a">中活动度</td></tr>
<tr><td style="font-weight:700;color:#d45050">&gt; 26.0</td><td style="font-weight:700;color:#d45050">高活动度</td></tr></table>
<div class="disclaimer" style="border:none;margin-top:4px">⚠️ CRP单位为 mg/dL（如化验单为 mg/L，需除以10）</div>
</div>

<script>
function calc(){
  const tjc=+document.getElementById('tjc').value;
  const sjc=+document.getElementById('sjc').value;
  const phga=+document.getElementById('phga').value;
  const ptga=+document.getElementById('ptga').value;
  const crp=+document.getElementById('crp').value||0;
  document.getElementById('tjc_val').textContent=tjc;
  document.getElementById('sjc_val').textContent=sjc;
  document.getElementById('phga_val').textContent=phga.toFixed(1);
  document.getElementById('ptga_val').textContent=ptga.toFixed(1);
  const score=tjc+sjc+phga+ptga+crp;
  document.getElementById('score').textContent=score.toFixed(1);
  document.getElementById('footerScore').textContent=score.toFixed(1);
  let label,c;
  if(score<=3.3){label="缓解";c="#22a87e";}
  else if(score<=11){label="低活动度";c="#20a39e";}
  else if(score<=26){label="中活动度";c="#d4892a";}
  else{label="高活动度";c="#d45050";}
  document.getElementById('status').textContent=label;document.getElementById('status').style.background=c;
  document.getElementById('footerStatus').textContent=label;document.getElementById('footerStatus').style.background=c;
  document.getElementById('pathLine').textContent=`TJC${tjc}+SJC${sjc}+PhGA${phga.toFixed(1)}+PtGA${ptga.toFixed(1)}+CRP${crp.toFixed(1)}`;
}
calc();
</script>
''' + COMMON_FOOTER
    write_file("SDAI.html", html)


def gen_bmi():
    html = COMMON_HEAD.format(title="BMI Z-score 计算器", nav_title="BMI Z-score") + '''
<div class="card">
<h1>BMI <span>Z-score</span></h1>
<div class="sub">Body Mass Index · 体质量指数 · 儿童青少年百分位评估</div>

<div class="section-title">📐 输入参数</div>

<div class="input-group">
<label>年龄（岁）</label>
<input type="number" id="age" min="2" max="18" step="0.1" value="10" oninput="calc()">
</div>

<div class="input-group">
<label>性别</label>
<select id="sex" onchange="calc()">
<option value="M">男</option><option value="F">女</option>
</select>
</div>

<div class="input-group">
<label>身高（cm）</label>
<input type="number" id="height" min="50" max="200" step="0.1" value="140" oninput="calc()">
</div>

<div class="input-group">
<label>体重（kg）</label>
<input type="number" id="weight" min="3" max="150" step="0.1" value="35" oninput="calc()">
</div>

<div class="section-title green">📊 计算结果</div>
<div class="result-box">
<div class="result-label">BMI（kg/m²）</div>
<div class="result-num" id="bmi_val">17.9</div>
<div id="percentile" style="font-size:0.8rem;color:#64748b;margin-top:4px">百分位评估</div>
<div class="result-status" id="status" style="background:#22a87e">正常体重</div>
</div>
</div>

<div class="card">
<div class="section-title red">🎯 儿童BMI百分位分类（2-18岁）</div>
<table><tr><th>百分位</th><th>分类</th><th>建议</th></tr>
<tr><td style="font-weight:700;color:#d45050">&lt; 第5百分位</td><td style="font-weight:700;color:#d45050">体重过低</td><td>评估营养状况</td></tr>
<tr><td style="font-weight:700;color:#22a87e">第5 – 85百分位</td><td style="font-weight:700;color:#22a87e">正常体重</td><td>维持健康饮食运动</td></tr>
<tr><td style="color:#d4892a;font-weight:700">第85 – 95百分位</td><td style="color:#d4892a;font-weight:700">超重</td><td>生活方式干预</td></tr>
<tr><td style="color:#d45050;font-weight:700">&gt; 第95百分位</td><td style="color:#d45050;font-weight:700">肥胖</td><td>综合管理</td></tr></table>

<div class="section-title yellow">📝 临床提示</div>
<p style="font-size:0.72rem;color:#64748b">风湿免疫患儿长期使用糖皮质激素可导致体重增加和向心性肥胖。BMI监测是药物安全性评估的重要指标。建议每次随访记录BMI变化趋势。</p>
</div>

<script>
/* Simplified BMI calculation with approximate percentile estimation */
const REF_50={
M:{2:16.5,3:15.7,4:15.5,5:15.4,6:15.4,7:15.5,8:15.7,9:15.9,10:16.2,11:16.6,12:17.2,13:17.8,14:18.4,15:19.0,16:19.5,17:19.9,18:20.2},
F:{2:16.3,3:15.6,4:15.4,5:15.3,6:15.3,7:15.4,8:15.6,9:15.9,10:16.2,11:16.7,12:17.4,13:18.2,14:18.9,15:19.4,16:19.8,17:20.0,18:20.2}
};
function calc(){
  const age=+document.getElementById('age').value;
  const sex=document.getElementById('sex').value;
  const h=+document.getElementById('height').value/100;
  const w=+document.getElementById('weight').value;
  if(h<=0||w<=0)return;
  const bmi=w/(h*h);
  document.getElementById('bmi_val').textContent=bmi.toFixed(1);
  document.getElementById('footerScore').textContent=bmi.toFixed(1);
  const p50=REF_50[sex][Math.round(age)]||18;
  const diff=bmi-p50;
  let cat,c,pLabel;
  if(diff<-3){cat="体重过低";c="#d45050";pLabel="&lt; 第5百分位";}
  else if(diff<-1.5){cat="偏瘦";c="#20a39e";pLabel="第5-25百分位";}
  else if(diff<=2){cat="正常体重";c="#22a87e";pLabel="第25-75百分位";}
  else if(diff<=3.5){cat="超重";c="#d4892a";pLabel="第85-95百分位";}
  else{cat="肥胖";c="#d45050";pLabel="&gt; 第95百分位";}
  document.getElementById('percentile').innerHTML=`约 <b>${pLabel}</b>`;
  document.getElementById('status').textContent=cat;document.getElementById('status').style.background=c;
  document.getElementById('footerStatus').textContent=cat;document.getElementById('footerStatus').style.background=c;
  document.getElementById('pathLine').textContent=`${age}岁${sex==='M'?'男':'女'} · 身高${(h*100).toFixed(0)}cm · 体重${w.toFixed(1)}kg`;
}
calc();
</script>
''' + COMMON_FOOTER
    write_file("BMI_Zscore.html", html)


def gen_bsa():
    html = COMMON_HEAD.format(title="BSA 体表面积计算器", nav_title="BSA 体表面积") + '''
<div class="card">
<h1>BSA <span>体表面积</span></h1>
<div class="sub">Body Surface Area · Mosteller公式 · 儿童药物剂量计算</div>

<div class="section-title">📐 输入参数</div>

<div class="input-group">
<label>身高（cm）</label>
<input type="number" id="height" min="40" max="200" step="0.1" value="120" oninput="calc()">
</div>

<div class="input-group">
<label>体重（kg）</label>
<input type="number" id="weight" min="2" max="150" step="0.1" value="25" oninput="calc()">
</div>

<div class="section-title green">📊 计算结果</div>
<div class="result-box">
<div class="result-label">BSA（Mosteller公式, m²）</div>
<div class="result-num" id="bsa_val">0.93</div>
<div id="mtx_info" style="font-size:0.75rem;color:#64748b;margin-top:6px"></div>
</div>
</div>

<div class="card">
<div class="section-title">📝 Mosteller 公式</div>
<div style="background:linear-gradient(135deg,#f0fafa,#e6f5f4);padding:12px;border-radius:10px;font-size:0.85rem;text-align:center;font-weight:700;color:#20a39e">
BSA (m²) = √( 身高cm × 体重kg ÷ 3600 )
</div>

<div class="section-title yellow">💊 常见BSA相关剂量参考</div>
<table><tr><th>药物</th><th>剂量</th><th>说明</th></tr>
<tr><td style="font-weight:700;color:#20a39e">MTX（甲氨蝶呤）</td><td>10-15 mg/m²/周</td><td>起始剂量，最大25 mg/m²/周</td></tr>
<tr><td>环磷酰胺</td><td>500-1000 mg/m²</td><td>静脉冲击，每月1次</td></tr>
<tr><td>IVIG</td><td>2 g/kg</td><td>KD方案：分2-5天</td></tr></table>
</div>

<script>
function calc(){
  const h=+document.getElementById('height').value;
  const w=+document.getElementById('weight').value;
  if(h<=0||w<=0)return;
  const bsa=Math.sqrt(h*w/3600);
  document.getElementById('bsa_val').textContent=bsa.toFixed(2);
  document.getElementById('footerScore').textContent=bsa.toFixed(2)+' m²';
  const mtLow=(bsa*10).toFixed(0);
  const mtHigh=(bsa*15).toFixed(0);
  const mtMax=(bsa*25).toFixed(0);
  document.getElementById('mtx_info').innerHTML=`💡 MTX起始剂量参考：<b>${mtLow}-${mtHigh} mg/周</b>（最大${mtMax} mg/周）`;
  document.getElementById('footerStatus').textContent=`${bsa.toFixed(2)} m²`;
  document.getElementById('footerStatus').style.background='#20a39e';
  document.getElementById('pathLine').textContent=`身高${h}cm · 体重${w}kg`;
}
calc();
</script>
''' + COMMON_FOOTER
    write_file("BSA.html", html)


def gen_mtx():
    html = COMMON_HEAD.format(title="MTX 甲氨蝶呤剂量计算器", nav_title="MTX 剂量计算") + '''
<div class="card">
<h1>MTX <span>剂量计算</span></h1>
<div class="sub">Methotrexate（甲氨蝶呤）· JIA一线DMARDs · 儿科剂量</div>

<div class="section-title">📐 输入参数</div>

<div class="input-group">
<label>体重（kg）</label>
<input type="number" id="weight" min="3" max="100" step="0.1" value="25" oninput="calc()">
</div>

<div class="input-group">
<label>身高（cm）— 用于计算BSA</label>
<input type="number" id="height" min="40" max="200" step="0.1" value="120" oninput="calc()">
</div>

<div class="input-group">
<label>计算方式</label>
<select id="mode" onchange="calc()">
<option value="bsa">按体表面积（推荐）</option>
<option value="weight">按体重</option>
</select>
</div>

<div class="section-title green">📊 推荐剂量</div>
<div class="result-box">
<div id="dose_info" style="font-size:0.78rem;color:#64748b;margin-bottom:4px"></div>
<div class="result-num" id="dose">10.5</div>
<div class="result-label">mg/周</div>
<div id="range_info" style="font-size:0.72rem;color:#64748b;margin-top:6px"></div>
</div>
</div>

<div class="card">
<div class="section-title yellow">📝 儿科MTX用药要点</div>
<table><tr><th>项目</th><th>说明</th></tr>
<tr><td>起始剂量</td><td>10-15 mg/m²/周 或 0.3-0.5 mg/kg/周</td></tr>
<tr><td style="font-weight:700;color:#d45050">最大剂量</td><td style="font-weight:700;color:#d45050">25 mg/m²/周 或 1 mg/kg/周（上限25 mg/周）</td></tr>
<tr><td>给药途径</td><td>口服为主，效果不佳可改为皮下注射</td></tr>
<tr><td>叶酸补充</td><td>每周MTX后24-48h口服叶酸 1-5 mg</td></tr>
<tr><td>起效时间</td><td>4-8周</td></tr>
<tr><td>监测</td><td>每1-3月查血常规、肝肾功能</td></tr></table>

<div class="section-title red">⚠️ 注意事项</div>
<div style="background:#fde8e8;border-left:3px solid #d45050;padding:8px 12px;border-radius:0 10px 10px 0;font-size:0.72rem;color:#64748b">
<ul style="padding-left:14px;margin:0">
<li>肝功能异常时慎用或暂停</li>
<li>合并感染时暂停</li>
<li>育龄期女性需避孕</li>
<li>避免与SMZ联用（增加骨髓抑制风险）</li></ul></div>
</div>

<script>
function calc(){
  const w=+document.getElementById('weight').value;
  const h=+document.getElementById('height').value;
  const mode=document.getElementById('mode').value;
  const bsa=Math.sqrt(h*w/3600);
  let startLow,startHigh,maxDose,unit;
  if(mode==='bsa'){
    startLow=bsa*10;startHigh=bsa*15;maxDose=Math.min(bsa*25,25);
    unit='mg/m²/周';
    document.getElementById('dose_info').textContent=`BSA = ${bsa.toFixed(2)} m² · 按${unit}计算`;
    document.getElementById('range_info').innerHTML=`起始范围 <b>${startLow.toFixed(1)}-${startHigh.toFixed(1)} mg/周</b> · 最大 <b>${maxDose.toFixed(1)} mg/周</b>`;
  }else{
    startLow=w*0.3;startHigh=w*0.5;maxDose=Math.min(w*1,25);
    unit='mg/kg/周';
    document.getElementById('dose_info').textContent=`体重 = ${w} kg · 按${unit}计算`;
    document.getElementById('range_info').innerHTML=`起始范围 <b>${startLow.toFixed(1)}-${startHigh.toFixed(1)} mg/周</b> · 最大 <b>${maxDose.toFixed(1)} mg/周</b>`;
  }
  const mid=(startLow+startHigh)/2;
  document.getElementById('dose').textContent=mid.toFixed(1);
  document.getElementById('footerScore').textContent=mid.toFixed(1)+' mg';
  document.getElementById('footerStatus').textContent=`起始${startLow.toFixed(0)}-${startHigh.toFixed(0)} mg`;
  document.getElementById('footerStatus').style.background='#20a39e';
  document.getElementById('pathLine').textContent=`${w}kg / ${h}cm / BSA ${bsa.toFixed(2)}m²`;
}
calc();
</script>
''' + COMMON_FOOTER
    write_file("MTX_dose.html", html)


def gen_esr_crp():
    html = COMMON_HEAD.format(title="ESR/CRP 参考值查询", nav_title="ESR/CRP 参考值") + '''
<div class="card">
<h1>ESR / <span>CRP</span></h1>
<div class="sub">红细胞沉降率（Erythrocyte Sedimentation Rate）/ C反应蛋白（C-Reactive Protein）· 儿科参考值</div>

<div class="section-title">📐 输入参数</div>

<div class="input-group">
<label>年龄（岁）</label>
<input type="number" id="age" min="0" max="18" step="0.1" value="6" oninput="calc()">
</div>

<div class="input-group">
<label>性别</label>
<select id="sex" onchange="calc()">
<option value="M">男</option><option value="F">女</option>
</select>
</div>

<div class="input-group">
<label>ESR实测值（mm/h）</label>
<input type="number" id="esr" min="0" max="150" value="15" oninput="calc()">
</div>

<div class="input-group">
<label>CRP实测值（mg/L）</label>
<input type="number" id="crp" min="0" max="300" step="0.1" value="5" oninput="calc()">
</div>

<div class="section-title green">📊 参考范围评估</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:8px">
<div style="background:linear-gradient(135deg,#f0fafa,#e6f5f4);padding:12px;border-radius:12px;text-align:center">
<div style="font-size:0.7rem;color:#64748b;font-weight:700">ESR 参考范围</div>
<div style="font-size:0.65rem;color:#64748b" id="esr_ref">0-10 mm/h</div>
<div style="font-size:1.8rem;font-weight:900;margin:4px 0" id="esr_val" style="color:#22a87e">15</div>
<div id="esr_status" style="display:inline-block;padding:3px 12px;border-radius:12px;font-size:0.7rem;font-weight:800;color:#fff;background:#22a87e">正常</div>
</div>
<div style="background:linear-gradient(135deg,#f0fafa,#e6f5f4);padding:12px;border-radius:12px;text-align:center">
<div style="font-size:0.7rem;color:#64748b;font-weight:700">CRP 参考范围</div>
<div style="font-size:0.65rem;color:#64748b" id="crp_ref">&lt; 8 mg/L</div>
<div style="font-size:1.8rem;font-weight:900;margin:4px 0" id="crp_val" style="color:#22a87e">5.0</div>
<div id="crp_status" style="display:inline-block;padding:3px 12px;border-radius:12px;font-size:0.7rem;font-weight:800;color:#fff;background:#22a87e">正常</div>
</div>
</div>
</div>

<div class="card">
<div class="section-title yellow">📝 儿科ESR参考范围</div>
<table><tr><th>年龄段</th><th>ESR正常上限</th></tr>
<tr><td>新生儿（0-1月）</td><td>0-2 mm/h</td></tr>
<tr><td>1-6月</td><td>4-12 mm/h</td></tr>
<tr><td>6月-2岁</td><td>2-12 mm/h</td></tr>
<tr><td>2-6岁</td><td>2-10 mm/h</td></tr>
<tr><td>6-12岁</td><td>2-10 mm/h</td></tr>
<tr><td>&gt;12岁 男</td><td>3-10 mm/h</td></tr>
<tr><td>&gt;12岁 女</td><td>3-12 mm/h</td></tr></table>

<div class="section-title yellow">📝 儿科CRP参考范围</div>
<table><tr><th>CRP水平</th><th>临床意义</th></tr>
<tr><td style="font-weight:700;color:#22a87e">&lt; 8 mg/L</td><td style="font-weight:700;color:#22a87e">正常</td></tr>
<tr><td>8-20 mg/L</td><td>轻度升高（轻微感染/炎症）</td></tr>
<tr><td style="color:#d4892a;font-weight:700">20-60 mg/L</td><td style="color:#d4892a;font-weight:700">中度升高</td></tr>
<tr><td style="color:#d45050;font-weight:700">&gt; 60 mg/L</td><td style="color:#d45050;font-weight:700">显著升高（细菌感染/严重炎症）</td></tr></table>

<div class="section-title">💡 临床提示</div>
<p style="font-size:0.72rem;color:#64748b">JIA活动期ESR和CRP可升高，但sJIA/MAS危象时可能出现ESR正常而CRP极度升高（铁蛋白↑↑）的反常现象。CRP较ESR更敏感、更特异，但两者应联合评估。</p>
</div>

<script>
function calc(){
  const age=+document.getElementById('age').value;
  const sex=document.getElementById('sex').value;
  const esr=+document.getElementById('esr').value||0;
  const crp=+document.getElementById('crp').value||0;
  let esrMax;
  if(age<0.08)esrMax=2;
  else if(age<0.5)esrMax=12;
  else if(age<2)esrMax=12;
  else if(age<12)esrMax=10;
  else esrMax=sex==='F'?12:10;
  document.getElementById('esr_ref').textContent=`0-${esrMax} mm/h`;
  document.getElementById('esr_val').textContent=esr;
  document.getElementById('esr_val').style.color=esr<=esrMax?"#22a87e":"#d45050";
  let esrLabel,esrC;
  if(esr<=esrMax){esrLabel="正常";esrC="#22a87e";}
  else if(esr<=esrMax*2){esrLabel="轻度升高";esrC="#d4892a";}
  else{esrLabel="显著升高";esrC="#d45050";}
  document.getElementById('esr_status').textContent=esrLabel;document.getElementById('esr_status').style.background=esrC;

  document.getElementById('crp_ref').textContent='< 8 mg/L';
  document.getElementById('crp_val').textContent=crp.toFixed(1);
  let crpLabel,crpC;
  if(crp<8){crpLabel="正常";crpC="#22a87e";}
  else if(crp<20){crpLabel="轻度升高";crpC="#d4892a";}
  else if(crp<60){crpLabel="中度升高";crpC="#e07a2a";}
  else{crpLabel="显著升高";crpC="#d45050";}
  document.getElementById('crp_val').style.color=crpC;
  document.getElementById('crp_status').textContent=crpLabel;document.getElementById('crp_status').style.background=crpC;

  document.getElementById('footerScore').textContent=`E${esr}/C${crp.toFixed(0)}`;
  document.getElementById('footerStatus').textContent=esrLabel+' / '+crpLabel;
  document.getElementById('footerStatus').style.background=(esr>esrMax||crp>=8)?"#d4892a":"#22a87e";
  document.getElementById('pathLine').textContent=`${age}岁${sex==='M'?'男':'女'} · ESR ${esr} mm/h · CRP ${crp} mg/L`;
}
calc();
</script>
''' + COMMON_FOOTER
    write_file("ESR_CRP.html", html)


def gen_chaq():
    domains = [
        ("穿衣与梳理", "Dressing & Grooming", [
            "穿衣、系扣、拉拉链",
            "洗头",
            "洗脸、洗手",
        ]),
        ("起立", "Rising", [
            "从床上/椅子上站起来",
        ]),
        "进食",
        "行走",
        "清洁卫生",
        "伸手取物",
        "握力",
        "日常活动",
    ]
    # Simplified CHAQ with 8 domains, 2-4 items each
    items = [
        ("d1","穿衣与梳理（Dressing & Grooming）",["穿衣系扣拉拉链","洗头","剪指甲"]),
        ("d2","起立（Rising）",["从床上站起来","从椅子上站起来","从马桶上站起来"]),
        ("d3","进食（Eating）",["切肉","端杯子喝水","拧开瓶盖"]),
        ("d4","行走（Walking）",["在平地行走","上楼梯","下楼梯"]),
        ("d5","清洁卫生（Hygiene）",["洗澡擦干身体","上厕所","刷牙"]),
        ("d6","伸手取物（Reach）",["伸手拿高处物品","弯腰捡地上物品"]),
        ("d7","握力（Grip）",["开门","拧开罐头","握笔写字"]),
        ("d8","日常活动（Activities）",["外出玩耍","骑自行车/做运动","和朋友一起玩"]),
    ]

    items_html = ""
    for did, dname, ilist in items:
        items_html += f'<div class="section-title" style="margin-top:14px">{dname}</div>\n'
        for i, item in enumerate(ilist):
            items_html += f'''<div class="click-row" style="display:flex;gap:6px;align-items:center;padding:6px 0;border-bottom:1px solid #f0f5f4">
  <span style="flex:1;font-size:0.75rem;font-weight:500">{item}</span>
  <div style="display:flex;gap:3px">
  <button class="chaq-btn" data-domain="{did}" data-score="0" onclick="pick(this)">无困难<br><small>0</small></button>
  <button class="chaq-btn" data-domain="{did}" data-score="1" onclick="pick(this)">有些困难<br><small>1</small></button>
  <button class="chaq-btn" data-domain="{did}" data-score="2" onclick="pick(this)">很困难<br><small>2</small></button>
  <button class="chaq-btn" data-domain="{did}" data-score="3" onclick="pick(this)">做不到<br><small>3</small></button>
  </div></div>\n'''

    html = COMMON_HEAD.format(title="CHAQ 问卷评分", nav_title="CHAQ 问卷") + f'''
<style>
.chaq-btn{{padding:4px 6px;border:1.5px solid var(--border);border-radius:6px;font-size:0.6rem;font-weight:700;cursor:pointer;background:#f4fafa;color:var(--text2);min-width:52px;text-align:center;transition:all 0.15s;}}
.chaq-btn:hover{{border-color:var(--accent);}}
.chaq-btn.sel{{background:var(--accent);color:#fff;border-color:var(--accent);}}
</style>

<div class="card">
<h1>CHAQ <span>问卷</span></h1>
<div class="sub">Childhood Health Assessment Questionnaire · 儿童健康评估问卷 · 8个功能域</div>

<div style="background:linear-gradient(135deg,#f0fafa,#e6f5f4);padding:10px 14px;border-radius:10px;margin-bottom:12px;font-size:0.72rem;color:#64748b">
<b style="color:#20a39e">评分规则：</b>每个功能域取该域内<b>最高分</b>（0-3），8个域的平均值即为CHAQ残疾指数（0-3）。</div>

{items_html}

<div class="section-title green" style="margin-top:16px">📊 各域得分与总分</div>
<div id="domain_scores" style="display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-top:6px"></div>

<div class="result-box" style="margin-top:12px">
<div class="result-label">CHAQ 残疾指数（0-3）</div>
<div class="result-num" id="score">0.00</div>
<div class="result-status" id="status" style="background:#22a87e">无功能障碍</div>
</div>

<div style="text-align:center;margin-top:8px">
<button class="btn btn-reset" onclick="resetAll()">重置全部</button>
</div>
</div>

<div class="card">
<div class="section-title red">🎯 CHAQ分级</div>
<table><tr><th>CHAQ</th><th>功能障碍程度</th></tr>
<tr><td style="font-weight:700;color:#22a87e">0 – 0.5</td><td style="font-weight:700;color:#22a87e">轻度/无功能障碍</td></tr>
<tr><td style="color:#d4892a;font-weight:700">0.6 – 1.5</td><td style="color:#d4892a;font-weight:700">中度功能障碍</td></tr>
<tr><td style="color:#d45050;font-weight:700">&gt; 1.5</td><td style="color:#d45050;font-weight:700">重度功能障碍</td></tr></table>
</div>

<script>
const domains={{d1:[],d2:[],d3:[],d4:[],d5:[],d6:[],d7:[],d8:[]}};
const domainNames={{d1:"穿衣",d2:"起立",d3:"进食",d4:"行走",d5:"卫生",d6:"取物",d7:"握力",d8:"活动"}};

function pick(btn){{
  const domain=btn.dataset.domain;
  const score=+btn.dataset.score;
  // deselect siblings with same domain+item (same parent div buttons)
  const siblings=btn.parentElement.querySelectorAll('.chaq-btn');
  siblings.forEach(b=>b.classList.remove('sel'));
  btn.classList.add('sel');
  // update domain max
  const row=btn.closest('.click-row');
  const rowBtns=row.querySelectorAll('.chaq-btn.sel');
  let maxInRow=0;
  rowBtns.forEach(b=>{{if(+b.dataset.score>maxInRow)maxInRow=+b.dataset.score;}});
  // recalculate domain max from ALL selected in this domain
  const allDomainBtns=document.querySelectorAll(`.chaq-btn[data-domain="${{domain}}"].sel`);
  let maxD=0;
  allDomainBtns.forEach(b=>{{if(+b.dataset.score>maxD)maxD=+b.dataset.score;}});
  domains[domain]=maxD;
  calc();
}}

function resetAll(){{
  document.querySelectorAll('.chaq-btn.sel').forEach(b=>b.classList.remove('sel'));
  Object.keys(domains).forEach(k=>domains[k]=0);
  calc();
}}

function calc(){{
  const vals=Object.values(domains);
  const allAnswered=vals.every(v=>v!==undefined);
  const answered=vals.filter(v=>v>0||true);
  const sum=vals.reduce((a,b)=>a+b,0);
  const n=vals.length;
  const chaq=sum/n;
  document.getElementById('score').textContent=chaq.toFixed(2);
  document.getElementById('footerScore').textContent=chaq.toFixed(2);
  // domain scores display
  let html='';
  Object.keys(domains).forEach(k=>{{
    const v=domains[k];
    const bg=v===0?'#e6f5f4':v<=1?'#fef3e2':v<=2?'#fde8e8':'#f5dede';
    html+=`<div style="background:${{bg}};padding:6px 10px;border-radius:8px;font-size:0.7rem"><b>${{domainNames[k]}}</b>: ${{v}}</div>`;
  }});
  document.getElementById('domain_scores').innerHTML=html;
  let label,c;
  if(chaq<=0.5){{label="无/轻度障碍";c="#22a87e";}}
  else if(chaq<=1.5){{label="中度障碍";c="#d4892a";}}
  else{{label="重度障碍";c="#d45050";}}
  document.getElementById('status').textContent=label;document.getElementById('status').style.background=c;
  document.getElementById('footerStatus').textContent=label;document.getElementById('footerStatus').style.background=c;
  document.getElementById('pathLine').textContent=Object.keys(domains).map(k=>`${{domainNames[k]}}${{domains[k]}}`).join(' ');
}}
calc();
</script>
''' + COMMON_FOOTER
    write_file("CHAQ.html", html)


# Generate all
print("Generating interactive calculators...")
gen_jadas27()
gen_jadas71()
gen_das28()
gen_cdai()
gen_sdai()
gen_bmi()
gen_bsa()
gen_mtx()
gen_esr_crp()
gen_chaq()
print("\nDone! All 10 calculators generated.")
