# 协议修正案 1 — G5-DUAL-MODEL-ANNOTATION-R1(2026-10-19)

## 背景

Step 3 Smoke Test(S01、S02 × 两 Reviewer,共 4 单元 × 3 次尝试 = 12 次真实调用)全部 `INVALID`,
失败原因**纯机械**:两个指定模型均为推理模型,思考内容消耗了全部 2048 输出预算:

- REVIEWER_A(deepseek-v4-flash,anthropic_messages):响应含 `thinking` 块,`output_tokens=2048`,
  未产出最终 JSON 文本(stop_reason 截断)。证据:`reviewer-a-raw/REVIEWER_A-S0{1,2}-a{1..3}.json`
- REVIEWER_B(glm-5.3-flash,openai_chat):`completion_tokens_details.reasoning_tokens=2046–2048`,
  `finish_reason=length`,`content` 为空。证据:`reviewer-b-raw/REVIEWER_B-S0{1,2}-a{1..3}.json`

模型身份本身两单元均验证正确(`response_model_field` = 协议模型ID)。上述 12 次失败的原始响应与
台账记录完整保留(`smoke-failed-attempt-r1/` + `execution-ledger.jsonl` 追加记录),**未依据任何判定
内容进行选择性重试**(未产生任何 verdict)。

## 修正内容(仅参数,不动 Prompt 模板、Schema、判定规则、重试规则、样本与标准)

| 参数 | 原值 | 新值 | 理由 |
| --- | --- | --- | --- |
| max_tokens | 2048 | **16384** | 为两模型默认开启的思考过程留出预算,保证最终 JSON 完整输出 |
| 请求超时 | 600 s | **900 s** | 与更大输出预算匹配 |

- 两 Reviewer 采用**完全对称**的处理:均保持提供商默认推理行为(不针对单个模型关闭 thinking;
  探针记录:DeepSeek anthropic-compat 接受 `thinking.disabled`,火山网关对 glm-5.3-flash 拒绝该参数、
  仅接受 `chat_template_kwargs.enable_thinking=false` —— 为避免非对称参数手术,不采用)。
- temperature=0.0、Prompt 模板、输出 Schema、verdict 一致性规则、重试上限(3 次尝试)均不变。

## 生效与追溯

- 本修正案自写入起生效;`dual-model-audit-protocol.md` §4 参数表以本文件为准(协议正文不回改)。
- 修正后重跑 Smoke Test(S01、S02);此前 INVALID 结果行从 `reviewer-{a,b}-results.jsonl` 清除
  (清除动作记录于本文件与台账),原始失败响应归档于 `smoke-failed-attempt-r1/`。
