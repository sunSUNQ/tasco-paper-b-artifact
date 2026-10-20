# 最终裁决 — Paper B GitHub 候选包(2026-10-20)

> ## 终态：**GITHUB_ARTIFACT_CANDIDATE_READY**

（CANDIDATE_READY = 本地候选包已准备完成并通过 39 项自动校验；**不等于可公开发布**——发布前须关闭 §三 的待决策项。）

## 验收逐项

| 验收标准 | 结果 |
|---|---|
| 论文主要结论可重算 | ✓ 39 项 R1/R2 校验 PASS;全部主文数字与冻结值一致 |
| 168/404/424 口径一致 | ✓ verify.py 逐项断言通过 |
| 三机制(M1/M2/M3)数据完整 | ✓ 200+60+120 = 380 run + 24 Stage-0 + 20 smoke = 424 |
| C1–C15 映射 | ✓ c1-c15-count-audit.json + evidence-mapping.md 在包内 |
| G4/G5 审计边界 | ✓ G4 双口径对账;G5 模型辅助限定声明 |
| 冻结数据与派生统计不混淆 | ✓ 双口径显式分离;X 残差声明;D3 分母精确化 |
| 独立复现 | ✓ 隔离目录 exit 0 |
| 无内部绝对路径泄漏(verify.py 层面) | ✓ verify.py 仅使用包内相对路径 |
| 无凭据泄漏 | ✓ 7 模式扫描 0 命中 |
| 论文编译 | ✓ paper-emse-final.pdf 12 页 |
| ESM_1 补充材料 | ✓ 5 页含 S-A…S-H |
| 安全扫描 | ✓ 无凭据/隐私/受限材料 |

## 129 文件清单

见 `manifest.sha256`(128 条 + 自身排除);`github-export-inventory.md` 按目录分类。

## 排除清单

见 `missing-materials-analysis.md`:paper-b/ 研究目录 407 文件中,278 个未纳入文件全部属于同名副本/中间审计/设计变体/旧版论文——**核心结论复现材料零遗漏**。

## 待负责人决策(9 项;互不阻塞)

见 `pending-owner-decisions.md`:作者信息、Data/Code availability 终稿、LICENSE 选定、HF 许可核验、Springer 模板再分发、轨迹发布决策、投稿 venue 确认、G5 人工审核。

## 残余限制

- 独立人工 G5 审核 PENDING(正文已如实声明)
- HF 语料许可待核验(数据获取指令已在 data/THIRD-PARTY.md)
- 424 原始轨迹待全量扫描后决定是否发布(trajectories/READ-ME-FIRST.md 已声明)

## 约束遵守

无新实验;无冻结件改动(引用既有终验);无 commit/push/Tag/Release/DOI;未投稿;Paper A 零改动。
