# Phase 3 测试优化报告

> 测试日期: 2026-04-10
> 测试范围: 全部116个HTML文件
> 状态: ✅ 全部通过

## 审计结果

### ✅ 全部通过项

| 检查项 | 结果 | 说明 |
|--------|------|------|
| UTF-8编码 | ✅ 116/116 | 全部正确 |
| 免责声明 | ✅ 53/53 cases | 全部包含 |
| 禁用蓝色#3b82f6 | ✅ 0违规 | 无蓝色 |
| 病例Tailwind CDN | ✅ 53/53 | 全部加载 |
| 病例Manifest链接 | ✅ 53/53 | PWA离线支持 |
| 病例@media响应式 | ✅ 53/53 | 移动端适配 |
| 索引页@media响应式 | ✅ 9/9 | 全部适配 |
| 内部链接有效性 | ✅ | 所有相对路径正确 |
| GitHub Pages部署 | ✅ 200 OK | 线上可访问 |
| sw.js缓存清单 | ✅ 117 assets | v2 cache |

### 🔧 已修复项（本轮）

| 修复 | 文件数 |
|------|--------|
| PMCID→PMID统一 | 4 (sJIA) |
| 添加tailwindcss+manifest | 4 (AID_FMF, KD×3) |
| 添加manifest链接 | 3 (IgAV) |
| 添加@media响应式 | 4 (2tools+1index+1case) |
| 移除无效外链 | 2 (rituximab, DAS_tool) |
| sw.js重新生成 | 1 (v2, 117 assets) |
| 首页统计更新 | 1 (53 cases/19 tools) |
| 总索引页重写 | 1 (cases/index.html) |

## 页面统计

| 类别 | 数量 |
|------|------|
| 疾病专题 | 11 |
| 药物专页 | 13 |
| 临床工具 | 19 |
| 临床病例 | 53 |
| 病例索引 | 9 |
| 总索引 | 1 |
| 旧工具 | 5 |
| 首页+PWA | 4 |
| **总计** | **116** |

## Commits

- `81e7a66` — 首页统计+总索引页
- `ea20c75` — CSS/PMID/responsive/PWA全面审计修复

---

## 🔒 计算器代码安全规范（2026-04-13 新增）

> **触发原因**：CHAQ得分膨胀至数千、JADAS ESR归一化公式错误（详见 log.md 2026-04-13）
> **适用范围**：所有含 `<script>` 计算逻辑的 `.html` 工具文件

### 规范1：数值初始化（防隐式类型转换）

```javascript
// ❌ 禁止
const domains = { d1: [], d2: [], d3: null };
let score;  // undefined

// ✅ 必须
const domains = { d1: 0, d2: 0, d3: 0 };
let score = 0;
```

**原则**：所有参与算术运算的变量，初始化必须为数字类型 `0`，绝不用 `[]`、`null`、`undefined`、`""`。

### 规范2：reduce 安全模式

```javascript
// ❌ 危险（当数组含非数字时触发字符串拼接）
const sum = vals.reduce((a, b) => a + b, 0);

// ✅ 安全（显式类型转换）
const sum = vals.reduce((a, b) => a + Number(b), 0);
```

### 规范3：公式必须标注文献来源

每个计算器的 `<script>` 块顶部，必须以注释标注原始公式出处：

```javascript
// DAS28-ESR: Prevoo ML et al., Arthritis Rheum 1995;38(1):44-48
// Formula: 0.56*√TJC28 + 0.28*√SJC28 + 0.70*ln(ESR+1) + 0.014*GH
function calc() { ... }
```

### 规范4：上线前必须通过标准case验证

每个计算器必须内置至少1个**已知结果的标准测试用例**，以注释形式保留：

```javascript
// 验证用例: TJC=2, SJC=10, ESR=38, GH=56 → DAS28-ESR = 5.16 (Prevoo Table 3)
// 验证用例: JADAS27 joints=5, PhGA=3.0, PtGA=2.5, ESR=40 → score=12.0 (Consolaro 2009)
```

开发者修改公式后，必须用该用例手动或脚本验证输出一致。

### 规范5：单位标注强制要求

所有涉及检验指标输入的字段，`<label>` 必须标注单位，且与公式所需单位一致：

```html
<!-- ✅ 正确 -->
<label>CRP（C反应蛋白, mg/dL）</label>
<label>CRP（C反应蛋白, mg/L）</label>

<!-- ❌ 禁止 -->
<label>CRP</label>
```

若公式所用单位与国内化验单常见单位不同，必须在输入框下方添加换算提示。

### 规范6：变更记录

修改任何计算器公式时，必须同步更新 `log.md`，记录：
- 修改的文件名和具体公式
- 修改前后对比
- 验证结果
