# -*- coding: utf-8 -*-
"""P0-C: docsor.cn 可达性拨测（cron每30分钟）
非200/超时 → 追加 ~/probe_alerts.log（连续失败才告警，用状态文件去重）"""
import subprocess, time, os, datetime

URLS = ['https://docsor.cn/', 'https://docsor.cn/topics/KD.html', 'https://docsor.cn/tools/SLE2K.html']
STATE = os.path.expanduser('~/probe_state.json')
ALERT = os.path.expanduser('~//probe_alerts.log').replace('//', '/')
now = datetime.datetime.now().strftime('%F %T')
state = {'fail_streak': 0}
try:
    import json
    state.update(json.load(open(STATE)))
except Exception:
    pass

fail = 0
for u in URLS:
    r = subprocess.run(['curl', '-sL', '-o', '/dev/null', '-w', '%{http_code}', '--max-time', '20', u],
                       capture_output=True, text=True, timeout=30)
    code = r.stdout.strip()
    if code != '200':
        fail += 1
        print(f'{now} FAIL {u} -> {code}')

state['fail_streak'] = state['fail_streak'] + 1 if fail else 0
if state['fail_streak'] == 3:  # 连续3次(约1.5h)失败才落告警,防抖
    with open(ALERT, 'a') as f:
        f.write(f'{now} docsor.cn 连续{state["fail_streak"]}次拨测失败({fail}/{len(URLS)}异常)\n')
import json as j
j.dump(state, open(STATE, 'w'))
print(f'{now} fail={fail} streak={state["fail_streak"]}')
