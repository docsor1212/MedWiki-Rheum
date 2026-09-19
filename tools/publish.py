#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""publish.py — MedWiki 新文章一键发布
用法: python3 tools/publish.py <article.html> --title "标题" --desc "一句话简介" [--push]
行为: 复制文章到 evidence/ → 自动合规注入(inject.py) → 索引卡片 → 首页时间线
      → sitemap → 搜索索引 → log.md → 验收(audit.py, FAIL即中止) →(--push) commit+push
"""
import argparse, shutil, os, sys, json, subprocess, datetime

os.chdir(os.path.expanduser("~/MedWiki-Rheum"))
ap = argparse.ArgumentParser()
ap.add_argument("file")
ap.add_argument("--title", required=True)
ap.add_argument("--desc", required=True)
ap.add_argument("--name", default=None, help="发布文件名，默认取源文件名")
ap.add_argument("--push", action="store_true")
a = ap.parse_args()
name = a.name or os.path.basename(a.file)
today = datetime.date.today().isoformat()
rel = "evidence/" + name

shutil.copy(a.file, os.path.join("evidence", name))

# ---- 自动合规注入(骨架/旧域/share/SW/免责; 自包含文章自动走bare模式) ----
r = subprocess.run([sys.executable, "tools/inject.py", rel], capture_output=True, text=True)
print(r.stdout.strip())
if r.returncode != 0:
    sys.exit("inject 失败:\n" + r.stderr)

p = "evidence/index.html"; s = open(p, encoding="utf-8").read()
anchor = "<!--PUBLISH:CARDS-->"
assert anchor in s, "evidence/index.html 缺少发布标记"
card = ("\n  <a class=\"ev-card\" href=\"%s\">\n    <div style=\"font-weight:600;margin-bottom:4px;\">%s</div>\n"
        "    <div style=\"font-size:13px;color:#666;margin-bottom:6px;\">%s</div>\n"
        "    <span class=\"pmid-tag\">%s</span>\n    <span class=\"disease-tag\">新发布</span>\n  </a>") % (name, a.title, a.desc, today)
s = s.replace(anchor, anchor + card, 1)
open(p, "w", encoding="utf-8", newline="\n").write(s)

p = "index.html"; s = open(p, encoding="utf-8").read()
anchor = "<div class=\"timeline\">"
assert anchor in s, "index.html 缺少时间线"
entry = ("\n    <div class=\"tl-item\">\n      <div class=\"tl-date\">%s</div>\n"
         "      <div class=\"tl-text\"><b>%s</b> — %s <a href=\"evidence/%s\">阅读全文</a></div>\n    </div>") % (today, a.title, a.desc, name)
s = s.replace(anchor, anchor + entry, 1)
open(p, "w", encoding="utf-8", newline="\n").write(s)

p = "sitemap.xml"; s = open(p, encoding="utf-8").read()
u = "  <url><loc>https://docsor.cn/evidence/%s</loc></url>\n" % name
if name not in s:
    s = s.replace("</urlset>", u + "</urlset>")
    open(p, "w", encoding="utf-8", newline="\n").write(s)

p = "assets/search-index.json"
try:
    entries = json.load(open(p, encoding="utf-8"))
except Exception:
    entries = []
if not any(e.get("u") == rel for e in entries):
    entries.append({"t": a.title, "u": rel, "c": "循证证据"})
    open(p, "w", encoding="utf-8", newline="\n").write(json.dumps(entries, ensure_ascii=False, indent=1))

p = "log.md"; s = open(p, encoding="utf-8").read()
entry = "\n## %s — 新增：%s\n- 文件：%s\n- 简介：%s\n" % (today, a.title, rel, a.desc)
anchor2 = "\n---\n"
s = s.replace(anchor2, "\n" + entry + anchor2, 1)
open(p, "w", encoding="utf-8", newline="\n").write(s)

# ---- 验收: audit不过不发布 ----
import re
r = subprocess.run([sys.executable, "tools/audit.py", "--quiet", rel], capture_output=True, text=True)
print(r.stdout.strip())
if re.search(r'^\[FAIL', r.stdout, flags=re.M):
    sys.exit("audit FAIL — 已保留工作区改动供修查, 未 commit/push")

print("published:", name)
if a.push:
    os.system("git add -A && git commit -m \"publish: %s\" && git push origin master" % a.title)
