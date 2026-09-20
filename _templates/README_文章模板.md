# MedWiki 深度文章模板 · 使用规范

> 两种文体，按内容体裁选。发布一律走 `tools/publish.py`（自动 sitemap/搜索索引/合规注入/audit 门禁）。

## 文体选择

| | KD考据体 `article_kd_style.html` | TETRA图解体 `article_deck_style.html` |
|---|---|---|
| 适用 | 一个临床问题的深挖（默认模板） | 权威机构发布新指南的全文解读 |
| 形态 | 单线叙事+指南原文逐句对照+证据截图 | deck逐页图解（参考母版 evidence/ev_TETRA_01.html） |
| 成本 | 中 | 高（整部指南工作量，慎选选题） |

## KD体必填块清单（发布前逐项核对）

1. **hero**：kicker 体裁标签 / h1 主标题+副题 / meta 三胶囊（依据·日期·作者）
2. **核心结论卡**：3 秒前置结论
3. **临床问题**：病例引入 + question 卡
4. **正文节**：`section > h2.sec`，编号"一、二、…"；指南对照用表格；截图必须有来源标注；临床主张逐条挂引文
5. **主要参考文献**：每条含 PMID，发布前过 L1 核验（tools/l1_check.py）
6. **术语与截图说明**（note）
7. **相关阅读条（必填）**：站内专题/工具/病例/药物互链 3-5 张——站内转化关键，不许空
8. **页脚签名 + 免责声明**：固定文案勿改

## 硬规则

- ⛔ 术语核验：病名/评分名逐条过 PubMed + 名词委（termonline.cn），查无此名即删
- ⛔ 中国方案与国际方案不同处，必须标"中国方案"+全称
- ⛔ 计算器/评分表数字必须回到原文锚点，WebSearch 摘要不可作依据
- ⛔ 儿童与成人数据必须区分，成人证据外推处显式标注
- ⛔ 表述客观：不用"保证/最佳/根治"等无据措辞（循证、客观）

## TETRA图解体说明

- **活模板 = evidence/ev_TETRA_01.html**（deckdoc 结构：83 页 slide、每页页脚"来源："标注、backtop）
- 做法.macOS：复制 TETRA 源文件 → 替换各页内容与截图 → 保留外壳（fit.js/页脚/免责）
- 工作量大，选题慎入：只用于"整部新指南发布"事件

## 发布流程

```
cp _templates/article_kd_style.html evidence/ev_<主题>_01.html
# 替换占位符 → L1核验 → 医生审校（结构化表单）→
python3 tools/publish.py evidence/ev_<主题>_01.html --title "…" --desc "…" [--push]
```

发布后：首页"最新深度"卡自动计数（CSS counter）；引文自动进月度 L1 cron。
