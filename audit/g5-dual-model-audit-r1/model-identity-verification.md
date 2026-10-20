# 模型身份验证报告 — G5-DUAL-MODEL-ANNOTATION-R1

任务:证明 60 个标注单元由指定真实模型生成,名称→模型ID映射有可验证记录。
结论:**通过** —— 所有 92 次 API 调用与全部 60 个有效标注单元的提供商响应 model 字段均与协议模型ID一致;无 Mock、无代调、无静默回退。

## 1. 名称→模型ID映射(冻结于协议 §3)

| Reviewer 指定名称 | 协议模型ID | 提供商端点(主机) | api_style |
| --- | --- | --- | --- |
| DeepSeek V4 Flash(Reviewer A) | `deepseek-v4-flash` | `api.deepseek.com`(DeepSeek 官方 Anthropic 兼容端点) | anthropic_messages |
| GLM-5.3-Flash(Reviewer B) | `glm-5.3-flash` | `st8tp3ajl0df3n8b8l8qu.apigateway-cn-beijing.volceapi.com`(火山AI网关 OpenAI 兼容端点) | openai_chat |

## 2. 身份探针(标注前,真实调用)

原始证据:`model-probe-REVIEWER_A.json`、`model-probe-REVIEWER_B.json`(HTTP 200)。

| Reviewer | 请求 model 字段 | 响应体 model 字段 | 判定 |
| --- | --- | --- | --- |
| REVIEWER_A | deepseek-v4-flash | **deepseek-v4-flash** | MATCH |
| REVIEWER_B | glm-5.3-flash | **glm-5.3-flash** | MATCH |

## 3. 逐单元身份(权威证据:API 响应体 model 字段)

- REVIEWER_A:30/30 单元 `response_model_field_api == "deepseek-v4-flash"`(自动化校验零例外)。
- REVIEWER_B:30/30 单元 `response_model_field_api == "glm-5.3-flash"`(自动化校验零例外)。
- 执行台账 92 次 `ANNOTATION_ATTEMPT` 记录中出现的 model 字段仅两个值:
  `{deepseek-v4-flash, glm-5.3-flash}`,与协议映射一一对应;时间跨度 2026-10-19T14:58:23 → 17:38:35。

## 4. 模型自报身份(verified_model_id,辅助证据)的发现

两个模型在全部 60 个有效单元中自报 `verified_model_id` 均为 `"unknown"`(协议修正案 2 允许该诚实回答)。
**模型不可靠知晓自身身份**;早期 Smoke 轮中曾出现 `"gpt-4o"`、`"claude-sonnet-4.5"`、
`"independent-blind-reviewer"` 等错误自报(证据:`smoke-failed-attempt-r1/`)。
因此身份判定**只采用 API 响应体 model 字段**为权威,自报字段仅作记录。此发现本身具有方法论价值:
模型身份审计必须依赖提供商响应,不能依赖模型自述。

## 5. 端点与凭据安全

- 凭据运行时加载:Reviewer A 来自环境变量 `ANTHROPIC_AUTH_TOKEN`;Reviewer B 来自本地
  opencode 配置(`~/.config/opencode/opencode.jsonc` 的火山网关 apiKey)。**未写入任何交付物、日志或原始响应**。
- 台账仅记录端点主机名与模型ID,不含 key、不含完整 URL 查询串。

## 6. 参数与调用形态(最终协议,修正案 3)

| 参数 | REVIEWER_A | REVIEWER_B |
| --- | --- | --- |
| temperature | 0.0 | 0.0 |
| max_tokens | 32768 | 32768 |
| 超时 | 1200 s | 1200 s |
| 扩展思考 | 提供商默认(开启) | 提供商默认(开启) |
| 每单元调用 | 独立无状态单轮 | 独立无状态单轮 |

两 Reviewer 参数完全对称;无针对单一模型的门槛调整。

## 7. 用量(提供商返回;网关不回传成本,按纪律不折算金额)

| 范围 | Reviewer | 调用数 | 输入 tokens | 输出 tokens | cache read |
| --- | --- | --- | --- | --- | --- |
| 全部尝试(含被替代 Smoke 轮) | A | 46 | 934,200 | 308,706 | 343,936 |
| 全部尝试 | B | 46 | 1,234,837 | 551,366 | 126,400 |
| **最终协议 60 有效单元 + 格式重试** | A | 32 | 829,716 | 244,959 | 85,376 |
| **最终协议** | B | 31 | 854,965 | 429,149 | 0 |

最终协议下有效标注 60 单元;格式/传输级重试共 4 次(A: S11、S21 各 1 次;B: S01(最终 Smoke)、S05 各 1 次),全部为 `length`/JSON 解析类失败,与判定内容无关。

## 8. 身份验证结论

| 检查 | 结果 |
| --- | --- |
| 真实 API 调用(非 Mock) | PASS(200 响应、真实 usage、墙钟时延合理) |
| 指定模型 = 响应模型 | PASS(92/92 调用、60/60 有效单元) |
| 名称→ID 映射可验证 | PASS(协议 §3 + 探针 + 逐单元记录) |
| 无模型回退/代调 | PASS(台账仅出现两个协议模型ID) |
| 非对称参数/门槛 | 无(对称) |
