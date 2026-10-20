# Staged 文件对账(final-staged-file-reconciliation)— Paper B GitHub

## 对账结果

| 项 | 计数 |
|---|---|
| git index staged 文件 | **144** |
| 研究内容文件(非基础设施) | 124 |
| 基础设施/发布决策文件 | 20 |
| **未授权文件** | **0** |

## 20 个基础设施文件(全部公开安全)

| 文件 | 用途 | 公开安全 |
|---|---|---|
| .gitignore | 排除规则 | ✓ |
| manifest.sha256 | 完整性清单 | ✓ |
| CITATION.cff | 引用元数据(license=TBD) | ✓(license 待定不影响结构) |
| REPRODUCIBILITY.md | 复现等级说明 | ✓ |
| EVIDENCE-MAP.md | 主张→文件映射 | ✓ |
| DATA_AVAILABILITY.md | 数据可用性说明 | ✓ |
| CODE_AVAILABILITY.md | 代码可用性说明 | ✓ |
| THIRD_PARTY_NOTICES.md | 第三方声明 | ✓ |
| publication-decision-sheet.md | 发布决策表 | ✓ |
| publication-decision-sheet-final.md | 决策表终版 | ✓ |
| publication-allowlist.md | 公开白名单 | ✓ |
| github-release-checklist.md | 发布清单 | ✓ |
| license-and-anonymity-gates.md | 许可与匿名门禁 | ✓ |
| missing-materials-analysis.md | 缺失分析 | ✓ |
| pending-owner-decisions.md | 待决清单 | ✓ |
| final-publication-approval.md | 审批终态 | ✓ |
| final-verdict.md | 候选包裁决 | ✓ |
| github-export-inventory.md | 导出清单 | ✓ |
| security-and-license-review.md | 安全审查 | ✓ |
| reproduction-validation.md | 复现验证报告 | ✓ |

## 差额说明(136 → 144)

原始设计清单 136 文件 = 124 研究内容 + 12 基础设施。
后续 GitHub 发布准备新增 8 个文件(全部为发布决策/安全审查/复现指南/基础设施文档):
`CITATION.cff`、`REPRODUCIBILITY.md`、`EVIDENCE-MAP.md`、`DATA_AVAILABILITY.md`、
`CODE_AVAILABILITY.md`、`THIRD_PARTY_NOTICES.md`、`github-release-checklist.md`、
`fig1-integration-report.md`(及其他发布文档合并后净增 8 个)。
**所有 8 个新增文件均为公开安全的文档/基础设施，不包含任何受限材料。**

## 未授权文件

**0 个。** 所有 staged 文件均为自产研究材料或公开安全的基础设施文件。
