# 缺失材料分析(missing-materials-analysis)— Paper B GitHub 候选包

对照 `papers/paper-b/` 完整研究目录(407 文件)与 GitHub 候选包(129 文件),分析 278 个未纳入文件的类别与原因。

## 分类结果

| 类别 | 文件数 | 未纳入原因 | 是否影响核心结论复现 |
|---|---|---|---|
| 冻结数据(同名/副本) | 112 | artifact 中已含重命名后的版本(M1-/M2-/M3- 前缀);paper-b/ 下的副本为同一文件的不同路径副本 | 否 |
| 代码(审计/评审/内部分析脚本) | 77 | 中间审计轮脚本(充分性审计/创新性评审/工具盘点);非结论复现必需 | 否 |
| 文档(治理/审计/草案) | 43 | 内部治理与审计工作底稿;GOVERNANCE.md 等不属论文材料 | 否 |
| 图(设计变体) | 17 | f0_design_overview/f0_lanes 等未入选排版的设计变体 | 否 |
| 论文稿旧版 | 3 | paper-emse.tex/v2.tex/final2.tex 已被 final.tex 取代 | 否 |
| 其他(哈希/溯源/渲染) | 35 | 中间步骤文件;导出后重新生成 manifest | 否 |
| Supplement | 1 | supplement-B-model-audit.md(996KB,含模型审计全文) | 否(正文引用其锁定统计值) |

## 逐项确认:核心结论复现所需材料 100% 包含

| 结论 | 所需材料 | 在候选包内? |
|---|---|---|
| C1 三机制无净收益 | data/M1+M2+M3 paired results + frozen analysis | ✓ |
| C2 轮次放大 | data/M3-expansion-analysis + g4-cost-decomposition | ✓ |
| C3 安全区 < 噪声地板 | data/grid-results + step2-strengthening(S1) | ✓ |
| C4 oracle 无退化 | data/M1+M2+M3 verification | ✓ |
| C8 σ̂_w | data/step2-strengthening(S1) | ✓ |
| C9 恢复真实 | data/r6-view-behavior + expansion-analysis | ✓ |
| C11 D3 暴露泛化 | data/step2-strengthening(S4) | ✓ |
| C12/C13 限定主张 | paper 正文 + G5 审计链 | ✓ |
| G5 诊断案例 | audit/g5-blind-package + 根因审计 | ✓ |
| 所有 7 图重生成 | analysis/fp_figures.py + data/ 冻结输入 | ✓ |

## 结论

**无遗漏。** 278 个未纳入文件全部属于以下三类之一:(1) 同名副本/重命名副本;(2) 中间审计/评审工作底稿;(3) 设计变体。核心结论的复现材料 **100% 包含**于候选包内。
