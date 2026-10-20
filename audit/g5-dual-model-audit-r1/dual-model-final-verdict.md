# 双模型审核终局结论 — G5-DUAL-MODEL-ANNOTATION-R1

## 终局判定

> ## **DIAGNOSTIC_RISK_FOUND**

依据实际审核结果(60/60 有效单元 + 机械证据交叉核验),本轮双模型语义盲审**发现系统性诊断信息丢失风险**;
同时审核执行本身完整、身份可证、无泄漏(执行层面等同于"DUAL_MODEL_AUDIT_WITH_DISAGREEMENTS"状态,
被上 stronger 结论涵盖)。**不是** PASS;**不是** AUDIT_INCOMPLETE;**不是** AUDIT_INVALID。

## 三条证据线的区分(任务书 §九 要求)

### 1. 双模型语义审核结果(本轮,真实调用)

- REVIEWER_A(deepseek-v4-flash):**25 FAIL / 5 PASS / 0 UNCERTAIN**;错误类型 E1×24、E3×11。
- REVIEWER_B(glm-5.3-flash):**1 FAIL / 29 PASS / 0 UNCERTAIN**;错误类型 E3×1。
- verdict 一致率 0.200,κ=0.0137(类别极度不均衡,κ 不具常规解释力,见 agreement-analysis.md §2)。
- 24 例分歧全部为 A=FAIL / B=PASS;唯一双 FAIL(S21)错误类型亦不一致(E1 vs E3)。
- 两位 Reviewer 相互隔离(独立无状态单轮调用;无跨 Reviewer 泄漏,机械校验通过)。
- **双方对客观缺陷均不完整检出**(对缺陷 (a):A 24/30,B 0/30;对缺陷 (b):A 11/30,B 1/30),
  因此"任一模型 PASS"或"双模型 PASS"都不构成安全证明。

### 2. 机械 E4 验证结果(既有,E4-MECHANICAL-PREFLIGHT)

- E4 预检 30/30 PASS;本轮执行前后两次复核冻结包 35/35 文件 sha256-16 一致(零修改)。
- **E4 PASS 与本轮发现不矛盾**:E4.5 的逐字包含检查方向是"in-context 行 ⊆ 原文行",
  **不检查"原文诊断行 ⊆ in-context"**,故机械预检通过不能排除 E1 诊断丢失。本轮结果恰填补了这一盲区。

### 3. 原 G5 人工审核状态

- **HUMAN G5 保持 PENDING,未做任何修改。** 本轮结果未写入 `review-sheet-answers-A/B.md` 或任何
  人工评审文件;双模型结果仅存于本目录专用文件。
- 修改人工审核协议需研究负责人明确授权;本轮未获该授权,亦未寻求。

## 发现的核心事实(供论文引用)

1. **缺陷 (a) — E1 诊断丢失,系统性**:全部 30 份样卷的 marker 指向原文中存在 4 行
   `return { ok: false, reason: "exhausted_retries", attempts: attempt };`(a302/ce49: 行 55/100/145/190;
   2e2b: 行 56/101/146/191),30 份 in-context 全部缺失该字符串。此为逐样本机械核验结论
   (`annotation-quality-audit.json` → `mechanical_evidence_checks`),Reviewer A 以 E1 报告了其中 24 份。
2. **缺陷 (b) — 未声明缺口(E3 事实基础)**:全部 30 份样卷 marker 声明省略自第 21/22 行起,
   但行 18–20 既未展示亦未包含在声明省略范围内;A 以 E3 报告 11 份,B 报告 1 份(S21)。
3. 两个缺陷在 3 个 evidence run 中同型出现(10/13/7 聚集),指向**压缩机制的系统性行为**,
   而非单样本偶发;视图级统计不得解释为任务级结论(case-cluster-analysis.md)。

## 对 Paper B 的含义(不自动改写科研结论)

- view-store 压缩机制存在可复现的"关键诊断行被静默省略 + 缺口未声明"问题;
  E4 机械预检(方向性包含检查)对此不敏感。
- 任何依赖"压缩后视图保留完整诊断信息"的论文表述,在引用本轮证据后**不能维持原样**;
  具体改写由研究负责人决定,本轮不修改 `final-seal`、不创建版本/Tag、不投稿 arXiv、
  **不宣称 FINAL_SUBMISSION_READY**。

## 仲裁建议(未执行)

- 24 个分歧样本保留双方原始判断(disagreement-cases.md)。
- 若需仲裁:建议争议包 = S01 + S21 + S24(三个 run 各一)+ 机械核验附录,交由未参与本轮的
  第三模型或人工评审;主控 Agent 未自行仲裁、未调用第三模型。

## 交付物完整性

本目录 13 项交付物齐全;`hashes.sha256` 覆盖全部文件(自身除外)。协议演变全程留痕
(`dual-model-audit-protocol.md` + 修正案 1/2/3),92 次 API 调用全部入台账,密钥零泄漏。
