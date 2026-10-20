# 交付物 9 — 最终风险裁决(G5-DIAGNOSTIC-RISK-ROOTCAUSE-R1)

**裁决日期**:2026-10-19 · **性质**:离线证据链审计(零新模型调用、零冻结件改动)

> ## 最终裁决:**DIAGNOSTIC_DEFECT_CONFIRMED**

(非 REVIEWER_DISAGREEMENT_UNRESOLVED —— 分歧已全因归并,见交付物 4;非 ANNOTATION_FALSE_POSITIVE
—— 无一例幻觉证据;非 AUDIT_INCOMPLETE —— 三层还原 30/30 闭环,核查矩阵全覆盖。)

## 1. 五个任务问题的答案

| # | 问题 | 裁定 |
|---|---|---|
| 1 | E1/E3 缺陷是否真实 | **真实**。E1(语义口径):12 条唯一诊断行(3 文件 × 4 行 `exhausted_retries` 失败返回)在 30/30 视图中不可见、仅存 side-store;E3:marker 原始行号与显示内容行号错位(offset=3)造成真实的可审计性/歧义缺陷。二者均为**机制级、确定性、跨 3 run 同型** |
| 2 | 缺失发生阶段 | **in-context 构造阶段(插件折叠)**。原始工具输出完好(=store=仓库源文件,V1 30/30);side-store 无损(sha 全一致);盲审样卷忠实(C==agent 实际所见,V4 逐字节 30/30)。根因:插件 `DIAG` 8 关键词词表覆盖缺口 + marker 单坐标系行号(代码行 L10/L30–33/L36) |
| 3 | 25 FAIL vs 1 FAIL 成因 | 三重标准歧义(诊断行定义 / 可见性 vs 可恢复性 / marker 坐标系)× 两模型不同默认解释:A=可见性优先+语义口径(检出 24/30、11/30,漏检 6);B=可恢复性优先+词面口径(E1 检出 0/30,E3 1/30)。无幻觉、无舞弊;详证交付物 4 |
| 4 | 是否影响 Paper B 安全主张 | 影响 M3 诊断保护表述与 C12/C13(见 §3);**不影响** C1–C11 计量主张;字节无损/恢复完整性主张经独立复核**反而增强**(C9) |
| 5 | 修订与投稿处置 | M3 诊断表述 **EVIDENCE_BLOCKED**(按冻结接收规则 HUMAN-INPUT-PENDING L37–38);两条合法出路见交付物 8(R1 语义口径维持缺陷认定→插件 v2+新证据轮;R2 研究负责人显式授权词面口径重界定+论文披露盲区)。未批准前:不投稿、不宣称 FINAL_SUBMISSION_READY |

## 2. 执行有效性(Step 0 要点)

- 92 次调用 = **60 有效**(R4 终版 Smoke 4 + R5 主阶段 56)+ **32 非终选**(R1/R2 Smoke 24 次
  invalid(格式)+ R3 Smoke 4 次 valid 被修正案 3 替代 + R5 主阶段 4 次格式重试的失败尝试)。
  全部留痕于台账与 raw 归档;选择规则 = 最终冻结协议下每单元首次有效尝试;无按判定内容重试。
- 修正案时序:修正案 1 先于任何 verdict 可见;修正案 2/3 晚于被替代轮(含 verdict 文本但 Schema
  不合法)输出可见 —— 56/60 单元全程处于最终协议零改动环境,S01/S02 重跑方向一致,事实基线
  协议无关。时序瑕疵如实记录,不影响结论(详见 step0-execution-audit.json)。
- 零改动核验:G5 冻结包 35/35 sha256-16 复核一致;g5-dual-model-audit-r1 全目录对照其
  hashes.sha256 逐文件一致(上轮证据未被触碰)。

## 3. 对论文的具体裁定(不自动执行)

| 表述 | 裁定 |
|---|---|
| 标题/摘要 "Lossless" | 成立(字节级),UNCHANGED;修订时须加"字节无损 ≠ 即时诊断可见"限定 |
| §3 M3 "all diagnostic lines verbatim" | **EVIDENCE_BLOCKED**(语义口径不成立;词面口径未在文中定义) |
| §3 "markers are auditable" | NEEDS_QUALIFICATION(坐标系缺陷) |
| "reconstruction is byte-exact" | 成立(独立复核),UNCHANGED |
| C4(oracle 无退化) | UNCHANGED(口径=oracle 成功,非诊断可见性) |
| C12 / C13 | NEEDS_QUALIFICATION(前提收窄;若坚持"语义保真"措辞则 C13 升为 NEEDS_CORRECTION) |
| 诊断保护证据 "24,648 视图零膨胀" | NEEDS_QUALIFICATION(该证据为 DIAG 词面口径 before==after 计数,不支持语义口径) |
| C1–C3,C5–C11,C14–C15 | UNCHANGED |

## 4. 分歧样本抽查(S01 / S21 / S24,仲裁建议包核心)

- **S01**:A=FAIL(E1,ER 行 55/100/145/190)vs B=PASS。机械:ER 行在 store、不在视图(真);
  B 的 PASS 依据"可恢复+词面无漏"——词面口径下自洽,语义口径下漏检。
- **S21**:A=FAIL(E1)vs B=FAIL(E3)。verdict 一致;依据不同事实(A:ER 行;B:坐标歧义),
  两者皆真 —— 错误类型层分歧归因于标准歧义,非事实错误。
- **S24**:A=FAIL(E1,ER 行 56/101/146/191)vs B=PASS("non-diagnostic and recoverable via
  the pointer")。B 漏检 (a) 且以可恢复性豁免可见性 —— 其 reasoning_summary 原文在案。

## 5. 交付物与留痕

| 交付物 | 文件 |
|---|---|
| 1 三层对照表 | deliverable-1-three-layer-table.md |
| 2 E1/E3 核查报告 | deliverable-2-defect-verification.md |
| 3 逐行差异清单 | deliverable-3-line-diff-list.md |
| 4 分歧归因 | deliverable-4-disagreement-attribution.md |
| 5 聚集分析 | deliverable-5-cluster-analysis.md |
| 6 合约符合性审计 | deliverable-6-contract-compliance.md + rc-step2-contract-audit.json |
| 7 C1–C15 影响清单 | deliverable-7-claim-impact.md |
| 8 人工仲裁材料 | deliverable-8-arbitration-package.md |
| 9 终局裁决+哈希 | 本文件 + hashes.sha256 |
| 机器可读证据 | step0-execution-audit.json;rc-step1-reconstruction.json;rc-step1b-events-visibility.json;rc-step2-contract-audit.json |

## 6. 状态落位

- HUMAN G5:**PENDING(不变)**;双模型审核 = 隔离执行的模型评估(非人工)。
- 论文 Gate:按冻结接收规则,诊断保护表述进入 **EVIDENCE_BLOCKED(默认态,直至仲裁 R1/R2 落定)**。
- 本轮无在线实验、无标注模型重调用、无冻结件/历史证据修改、无论文正文改动、无投稿、无版本/Tag。

**STOP。**
