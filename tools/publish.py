#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""publish.py — MedWiki 新文章一键发布
用法: python3 tools/publish.py <article.html> --title "标题" --desc "一句话简介" [--push]
行为: 复制文章到 evidence/ → 索引卡片 → 首页时间线 → sitemap → log.md →(--push) commit+push
"""
import argparse, shutil, os, sys, datetime

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

shutil.copy(a.file, os.path.join("evidence", name))

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
u = "  <url><loc>https://docsor1212.github.io/MedWiki-Rheum/evidence/%s</loc></url>\n" % name
if name not in s:
    s = s.replace("</urlset>", u + "</urlset>")
    open(p, "w", encoding="utf-8", newline="\n").write(s)

p = "log.md"; s = open(p, encoding="utf-8").read()
entry = "\n## %s — 新增：%s\n- 文件：evidence/%s\n- 简介：%s\n" % (today, a.title, name, a.desc)
anchor2 = "\n---\n"
s = s.replace(anchor2, "\n" + entry + anchor2, 1)
open(p, "w", encoding="utf-8", newline="\n").write(s)

print("published:", name)
if a.push:
    os.system("git add -A && git commit -m \"publish: %s\" && git push origin master" % a.title)
