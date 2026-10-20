# 协议修正案 3 — G5-DUAL-MODEL-ANNOTATION-R1(2026-10-19,最终生效)

## 背景(修正案 2 后 Smoke 第三轮,4 单元真实调用,3/4 单元有效)

实测证明修正案 2 的"关闭扩展思考"对真实审核提示**无效**:

- REVIEWER_B:`chat_template_kwargs:{"enable_thinking":false}` 在小提示探针中生效
  (reasoning_tokens≈35),但对约 25K token 的真实审核提示被网关/模板忽略——实测
  `reasoning_tokens=5481–16367`,且 1/4 单元再次 `finish_reason=length` 空内容。
  (证据:`reviewer-b-raw/REVIEWER_B-S01-a1.json`,r3)
- REVIEWER_A:`thinking:{"type":"disabled"}` 生效(响应 text-only),但这造成两 Reviewer
  运行模式不对称(A 直答 / B 带推理)。
- 两端点实测均接受 `max_tokens=32768`(探针 200)。

## 修正内容(最终参数,两 Reviewer 完全对称)

| 参数 | 修正案2值 | **最终值** | 理由 |
| --- | --- | --- | --- |
| 扩展思考 | A 关闭 / B 尝试关闭(无效) | **两模型均保持提供商默认(开启),不做任何参数手术** | 对称;尊重模型真实服务形态 |
| max_tokens | 16384 | **32768** | 容纳推理型模型的长思考;两端点探针接受 |
| 请求超时 | 900 s | **1200 s** | 与更长思考预算匹配 |

- temperature=0.0、Prompt 模板(含修正案 2 的 reviewer_id 填充)、输出 Schema、判定规则、
  重试策略(≤3 次尝试、仅格式/传输原因)全部不变。
- 长推理导致的 `finish_reason=length` 视为格式级失败,由冻结重试策略覆盖(实测 r3 中
  B-S01 第 2 次尝试成功)。

## Smoke 结果的协议有效性处置

修正案 1/2/3 参数不同,故此前各轮 Smoke 原始响应全部归档于 `smoke-failed-attempt-r1/`
(含 r3 的 4 个参数不合最终协议的响应,归档名加 `-r3` 标记),`reviewer-{a,b}-results.jsonl`
清空后**在最终参数下重新执行完整 Smoke(S01、S02 × 两模型)**;通过后协议即冻结为
修正案 3 状态,直接继续 S03–S30,中途不再修改任何参数。
