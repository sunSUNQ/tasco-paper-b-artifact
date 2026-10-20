# 交付物 4 — 双模型分歧归因报告(G5-DIAGNOSTIC-RISK-ROOTCAUSE-R1)

数据:60 个有效标注单元 + rc-step1 机械还原(30/30 闭环)+ rc-step2 合约审计。
主控 Agent 仅归纳,不仲裁;可判定问题已全部机械判定,残留语义/治理问题移交人工仲裁包(交付物 8)。

## 分歧概览

24 例 verdict 分歧(全部 A=FAIL / B:PASS)+ 1 例 verdict 一致但错误类型分歧(S21:A=E1,B=E3)。

## 问题 1:DeepSeek 是否识别了 GLM 漏检的真实缺口?

**是,两类均为机械可证的真实缺口:**

| 事实 | 机械核验 | A 检出 | B 检出 |
|---|---|---|---|
| (a) 4 行 `exhausted_retries` 失败返回未在视图呈现(仅存 side-store) | 30/30 卷成立 | 24/30(E1) | 0/30 |
| (b) marker 行号坐标系错位(raw 21..198/199 vs 内容 18..195/196) | 30/30 卷成立 | 11/30(E3) | 1/30(S21) |

A 的 E1 证据逐卷核实为真(无幻觉;行号、文本全部对得上,A 的证据原文如
"original:55,100,145,190 vs in-context:missing … only covered by the omitted pointer" 与机械事实一致)。

## 问题 2:DeepSeek 是否把合法外置行为误判为缺陷?

**未发现事实层面的误判,但存在标准层面的归类选择:**

- A 从未主张"不可恢复"或"原文损坏";其 E1 证据明确承认省略行"only covered by the omitted
  21..198 pointer"。A 判 FAIL 的依据是 G5 表 Q1 的**可见性口径**("missing from the in-context
  text"),且按语义读法定义"诊断行"(与冻结表 E1 示例 error/assert/… 的意图一致)。
- 因此 A 的 FAIL = "语义诊断行当前不可见"(真)+ "该情形按语义标准计为 E1"(标准选择)。
  前者机械为真;后者是 Q1 标准歧义下的合理一侧(见问题 4)。

## 问题 3:GLM 是否过度依赖 marker 可恢复性而忽略当前可见性?

**是,其 PASS 推理呈现一致的模式(证据:reviewer-b-results.jsonl reasoning_summary):**

- S04:"lines 18-20 … non-diagnostic and **recoverable via pointer**, so no ambiguity";
- S24:"they are non-diagnostic and **the pointer recovers the full original unambiguously**";
- S30:"recoverable via the store … No diagnostic loss, alteration, ambiguity, or pointer failure"。
- B 逐卷核对了 catch/lastError/error-return 块保留(全部属实),随即得出"every catch/
  error-handling line in the omitted range is retained"——它把"诊断行"按 **DIAG 关键词口径**(
  error 等词面)执行,因而系统性错过不含关键词的失败返回(ER 行 0/30 检出)。
- 即:B 的判定函数 ≈ 「关键词口径诊断行保留 + 指针可恢复 ⇒ PASS」,而 G5 表 Q1 问的是
  可见性口径。**B 系统性地把"可恢复"当作"未丢失"**。

## 问题 4:Q1–Q4 标准是否存在歧义?

**存在,三处,且全部被本轮实测触发:**

1. **"诊断行"无操作性定义**。G5 表给出示例词(error/assert/traceback/exception/fatal)但未定义
   边界;`return { ok:false, reason:"exhausted_retries" }` 属于语义诊断、词面不匹配。A 按语义、
   B 按词面 ⇒ E1 分歧 24 例的直接原因。
2. **可见性与可恢复性未分离**。Q1 问"missing from the in-context text"(可见),E4 问指针可解析
   (可恢复);当省略行已声明且可恢复时,评审人是否仍应判 E1?表未规定。B 选择了"可恢复 ⇒ 不算
   缺失";A 选择了"不可见即缺失"。⇒ 分歧的第二来源。
3. **marker 行号坐标系未定义**。评审人无从知道 marker 的 "21..198" 是原始工具输出行号(含 3 行
   envelope)而非显示的内容行号 ⇒ A 判 E3(缺口歧义)、B 多数卷忽略之。⇒ E3 分歧来源。

三处歧义均为**冻结标准的固有属性**,本轮不得追溯改写标准;处置见交付物 8(仲裁包)。

## 问题 5:协议修正案是否可能影响结论?

- 修正案 1–3 均为机械性(输出预算/超时/占位符填充/推理参数),**审核标准、Prompt 判据文本、
  Schema、判定规则零改动**(逐字比对见 g5-dual-model-audit-r1 各修正案)。
- 时序事实(rc-step0-execution-audit.json):修正案 1 写于任何含 verdict 输出可见之前;
  修正案 2/3 写于 R2/R3 Smoke 输出(含 verdict 文本但 Schema 不合法、被整体替代)之后。
  **56/60 单元(S03–S30)完全在最终冻结协议下执行,期间协议零改动**;S01/S02 在最终协议下
  重新执行,其方向与被替代轮次一致(A FAIL、B PASS),未见参数驱动的判定翻转。
- E1/E3 的事实基础与协议版本无关(机械核验独立成立)。**结论:修正案未 materially 影响本轮
  结论;时序瑕疵作为协议卫生事项如实记录。**

## 附:两模型共同的证据定位精度瑕疵(不影响 verdict)

- A 曾把 tail 行(196)列入 critical 证据;B 曾把 196–198 归入 critical 块(实际属 tail)。
  critical/tail 边界归因误差两侧均有,均不改变其 Q1–Q4 结论结构。

## 归因结论

25:1 的分歧不是噪声,而是**三重标准歧义 × 两模型不同的默认解释**的确定性结果:
A = 可见性优先 + 语义诊断口径;B = 可恢复性优先 + 词面诊断口径。两个口径各自内部自洽,
分歧可在冻结标准的歧义处完全解释;不存在幻觉驱动的分歧,也不存在一方"舞弊"式偏差。
