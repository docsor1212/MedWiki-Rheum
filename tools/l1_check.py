# -*- coding: utf-8 -*-
"""P0-B: L1引文月度核验+撤稿监测（固化版，供cron调用）
输出: ~/l1_reports/YYYY-MM.json；异常时追加 ~/l1_alerts.log"""
import re, glob, json, subprocess, time, io, os, datetime
from collections import Counter

ROOT = os.path.expanduser('~/MedWiki-Rheum')
os.chdir(ROOT)
NOW = datetime.date.today()
REPORT = os.path.expanduser(f'~/l1_reports/{NOW:%Y-%m}.json')
ALERT = os.path.expanduser('~/l1_alerts.log')
os.makedirs(os.path.dirname(REPORT), exist_ok=True)

def curl_json(url):
    r = subprocess.run(['curl', '-sg', url], capture_output=True, text=True, timeout=60)
    time.sleep(0.4)
    try: return json.loads(r.stdout)
    except Exception: return None

LI = re.compile(r'<li>([^<]*(?:<i>[^<]*</i>[^<]*)*?)</li>')
TAG = re.compile(r'<[^>]+>')
cited = []
for p in sorted(glob.glob('topics/*.html') + glob.glob('drugs/*.html') + glob.glob('evidence/*.html')):
    h = io.open(p, encoding='utf-8-sig').read()
    for li in LI.finditer(re.sub(r'<script.*?</script>|<style.*?</style>', '', h, flags=re.S)):
        txt = TAG.sub('', li.group(1))
        m = re.search(r'PMID[:\s]*(\d{4,8})', txt)
        j = re.search(r'<i>([^<]+)</i>\.?\s*\.?\s*(\d{4})', li.group(1))
        if m:
            cited.append({'page': p.replace(os.sep, '/'), 'txt': txt[:110],
                          'journal': j.group(1).strip() if j else '', 'year': j.group(2) if j else '',
                          'pmid': m.group(1)})

pmids = sorted({c['pmid'] for c in cited})
summary, detail = {}, {}
ghost, ymismatch = [], []
retracted = []
for i in range(0, len(pmids), 40):
    d = curl_json(f'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id={",".join(pmids[i:i+40])}')
    if not d: continue
    res = d.get('result', {})
    for uid in res.get('uids', []):
        rec = res[uid]
        summary[uid] = (rec.get('pubdate','')[:4], rec.get('source',''))
        pts = [p for p in rec.get('pubtype', []) if 'etract' in p]
        if pts:
            retracted.append({'pmid': uid, 'pubtypes': pts})
    time.sleep(0.4)

for c in cited:
    a = summary.get(c['pmid'])
    if not a:
        ghost.append(c); continue
    probs = []
    if c['year'] and a[0] and c['year'] != a[0]: probs.append(f"年份 页{c['year']}/实{a[0]}")
    if probs: ymismatch.append({**c, 'probs': probs})

report = {'date': str(NOW), 'total': len(cited), 'unique_pmids': len(pmids),
          'ok': len(cited) - len(ghost) - len(ymismatch),
          'year_mismatch': len(ymismatch), 'ghost': len(ghost), 'retracted': retracted,
          'mismatch_detail': ymismatch, 'ghost_detail': ghost, 'retracted_detail': retracted}
io.open(REPORT, 'w', encoding='utf-8', newline='').write(json.dumps(report, ensure_ascii=False, indent=1))
print(f"[{NOW}] 引文{report['total']}条(唯一{len(pmids)}) OK={report['ok']} 年份不符={len(ymismatch)} 幽灵={len(ghost)} 撤稿={len(retracted)}")
print('报告:', REPORT)
if ymismatch or ghost or retracted:
    with io.open(ALERT, 'a', encoding='utf-8') as f:
        f.write(f"{NOW} mismatch={len(ymismatch)} ghost={len(ghost)} retracted={len(retracted)}\n")
    for x in ymismatch: print('  [YM]', x['page'], x['pmid'], x['probs'])
    for x in retracted: print('  [RETRACTED]', x['pmid'], x['pubtypes'])
