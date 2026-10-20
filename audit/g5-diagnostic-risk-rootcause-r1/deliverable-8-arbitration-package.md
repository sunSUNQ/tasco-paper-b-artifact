# 交付物 8 — 人工仲裁材料(G5-DIAGNOSTIC-RISK-ROOTCAUSE-R1)

**性质:真实人工仲裁包(非模拟、非代填)。** 主控 Agent 已将全部可机械判定的问题判定完毕
(交付物 1–7);剩余**不可由 Agent 单方裁定的治理/语义问题**仅一个,提交研究负责人裁决。

## 待仲裁决策(唯一)

> **Q:冻结合约文本"全部诊断行(逐字)"是否覆盖不含 DIAG 关键词的失败返回行?**
> 例:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`

- **裁定选项 R1(语义口径)**:覆盖 ⇒ 维持本轮审计结论:
  诊断保护缺陷确认,论文 M3 诊断表述 EVIDENCE_BLOCKED,直至插件 v2(扩充词表/结构化检测
  + marker 双坐标系行号)冻结并重取证据;C12/C13 按 NEEDS_QUALIFICATION 收窄。
  与冻结 G5 表 E1 示例精神、冻结接收规则(E1 ⇒ EVIDENCE_BLOCKED)一致;无需改任何历史标准。
- **裁定选项 R2(词面口径显式化)**:不覆盖 ⇒ 须由研究负责人**显式授权**把"诊断行"重界定为
  8 关键词词表(留痕:新冻结文件,注明授权日期与理由),论文 M3 句同步改写为词面口径 +
  "non-keyword failure returns recoverable via side store only",C12/C13 同步收窄。
  ⚠ 此路径改变的是**未来标准**,不得追溯改写 REVIEWER-SHEET/online-protocol 历史,且必须在
  论文中披露词面口径的盲区(否则构成误导性表述)。

两选项均要求论文表述修改;差别在于是否承认"缺陷已发生"。主控 Agent 的审计推荐为 R1
(语义口径为合约文本与 G5 表的自然读法;R2 需要显式授权动作且须披露盲区),但**该推荐不
代替裁决**。

## 仲裁所需证据索引(全部已在本目录,无需重跑)

| 证据 | 文件 |
|---|---|
| 三层还原闭环(V1/V2/V4 30/30)| deliverable-1-three-layer-table.md;rc-step1-reconstruction.json;rc-step1b-events-visibility.json |
| ER 行事实(30 卷 × 4 行)| deliverable-3-line-diff-list.md |
| E1/E3 逐卷核查矩阵 | deliverable-2-defect-verification.md |
| 合约-实现口径对照 + 最小复现 | deliverable-6-contract-compliance.md;rc-step2-contract-audit.json |
| 分歧归因(25:1)| deliverable-4-disagreement-attribution.md |
| 双模型原始判定 | ../g5-dual-model-audit-r1/reviewer-{a,b}-results.jsonl 及 raw 目录 |
| 冻结合约原文 | ../../online/online-protocol.md;../../expansion/prereg.md;../g5-blind-package/REVIEWER-SHEET.md |
| 冻结接收规则(E1⇒EVIDENCE_BLOCKED)| ../final-seal/HUMAN-INPUT-PENDING.md L37–38 |
| 执行对账(92 调用/修正案时序)| step0-execution-audit.json |

## 仲裁执行建议

1. 评审人:研究负责人(或其指定人选,未参与 R4/R5/R6 执行与两轮模型审核者)。
2. 产出物:`review-sheet-arbitration-g5diagnostic.md`(人工撰写),内容 = R1/R2 选择 + 理由 +
   授权范围(是否批准插件 v2 立项、是否批准论文修订稿)。
3. Agent 收到后:机械登记裁定 → 更新 Gate 状态(G5 HUMAN 仍 PENDING 不变;EVIDENCE_BLOCKED
   标记按裁定落位)→ 论文修订另行走稿,不经本审计轮自动执行。

## 明确不做(约束重申)

- 不模拟人工裁定;不代填仲裁文件;不自动修订论文;不自动投稿;不建版本/Tag。
- 若研究负责人超期未裁:维持现状 —— HUMAN G5 = PENDING,论文 M3 诊断表述维持
  EVIDENCE_BLOCKED(冻结接收规则的默认态),不得默认 PASS。
