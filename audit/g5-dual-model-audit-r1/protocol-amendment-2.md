# 协议修正案 2 — G5-DUAL-MODEL-ANNOTATION-R1(2026-10-19)

## 背景(修正案 1 后 Smoke Test 第二轮,4 单元 × ≤3 次尝试 = 11 次真实调用)

输出预算扩大后两模型均可产出 JSON,但暴露 3 个机械问题:

1. **reviewer_id 占位符照抄**:Schema 示例中的 `"reviewer_id":"REVIEWER_X"` 被两模型逐字复制,
   触发 `reviewer_id_mismatch`(所有尝试)。
2. **REVIEWER_B 推理循环**:`glm-5.3-flash` 默认思考在 4/6 次尝试中耗尽 16384 输出预算
   (`reasoning_tokens≈16.4K`,`finish_reason=length`,`content` 为空),不可靠。
3. **verified_model_id 自报噪声**:出现 `"unknown"`、`"gpt-4o"`、`"claude-sonnet-4.5"`、
   `"independent-blind-reviewer"` 等——模型不可靠知晓自身身份(该发现本身记录于
   model-identity-verification.md;权威身份始终为 API 响应体 model 字段)。

## 修正内容

| # | 项 | 修正 | 性质 |
| --- | --- | --- | --- |
| 1 | Prompt 模板 Schema 行 | `"reviewer_id":"REVIEWER_X"` → 每单元按 Reviewer 填充实际ID(`REVIEWER_A`/`REVIEWER_B`);其余模板文字零改动 | 占位符填充修复(模板级) |
| 2 | verified_model_id 指示 | Schema 行注释改为 `<the model id you identify as; write "unknown" if you cannot know>`(英文逐字入模板);校验降级为"非空字符串" | 辅助证据语义澄清 |
| 3 | 扩展思考 | **两 Reviewer 对称关闭扩展思考**(各自提供商的原生参数):A = anthropic-compat `thinking:{"type":"disabled"}`(探针 200,text-only);B = 网关 `chat_template_kwargs:{"enable_thinking":false}`(探针 200,reasoning_tokens≈35,content 干净)。max_tokens 维持 16384、timeout 900s 不变 | 消除推理循环;保持对称 |

- temperature=0.0、判定规则、Q1–Q4/E1–E4 定义、重试策略(≤3 次尝试、仅格式/传输原因)、样本与
  哈希、隔离要求**全部不变**。
- 第二轮 Smoke 失败原始响应归档于 `smoke-failed-attempt-r1/`(文件名含 `-r2` 标记的为本轮),
  results.jsonl 中 INVALID 行再次清除并留台账。
- 修正后重跑 Smoke Test;通过条件不变(HTTP 200、响应 model 字段=协议模型ID、Schema 合法、
  verdict 与 Q1–Q4 自洽)。

## 已知并接受的局限(随结果声明)

- 关闭扩展思考后,Reviewer 以直接作答模式运行;复杂样本判定深度可能受限,由 UNCERTAIN 选项兜底。
- 两提供商的"关闭思考"参数机制不同(官方 anthropic-compat 参数 vs 网关 chat_template_kwargs),
  语义等价(均为"跳过扩展推理"),已探针验证并在 model-identity-verification.md 记录。
