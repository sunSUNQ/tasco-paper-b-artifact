# TASCO-PAPER-B-G5-DUAL-MODEL-FORMAL-ANNOTATION-R1 — 冻结执行协议

- 协议ID: `G5-DUAL-MODEL-ANNOTATION-R1`
- 冻结时间: 2026-10-19(本文件写入后即冻结;执行期间不得修改)
- 证据目录: `research-semantic-compression/r5/paper-b/presubmission/g5-dual-model-audit-r1/`
- 权威审核标准来源: `../g5-blind-package/REVIEWER-SHEET.md`(sha256-16 = `29db78168cfa6ec1`)
- 机械预检来源: `../g5-blind-package/e4-mechanical-preflight.json`(MECHANICAL_ONLY,verdict=PASS,30/30)
- 性质声明: 本轮为**双模型语义盲审(隔离执行的模型评估)**,**不是**人工盲审,**不是** E4 机械预检,不修改 G5 人工审核(HUMAN G5 保持 PENDING)。

---

## 1. Step 0 执行前核对记录(只读)

| 检查项 | 结果 |
| --- | --- |
| Git 状态 | `D:\tasco-temp` 与 `research-semantic-compression` 均非 git 仓库(无 HEAD/工作区状态可查);文件级完整性以 sha256 清单代替 |
| G5 盲审目录 | `../g5-blind-package/`(blind/S01–S30 + REVIEWER-SHEET + E4 预检 + mapping)存在 |
| E4 机械预检 | `e4-mechanical-preflight.json`:verdict=PASS,sequence_ok=true,hold=[],30/30 PASS |
| 样卷聚集 | 3 个 evidence run:a302a9c17cfbaba5=10(S01–S10)、ce499899267508a5=13(S11–S23)、2e2bda501b5f1865=7(S24–S30)。**30 份样卷≠30 个独立任务**;任务级推断受此限制 |
| 既有检查点 | 全库检索无 `dual-model`/`model-reviewer-*` 既有产物,无重复标注风险 |
| 样卷完整性 | `file-inventory.json` 35/35 文件 sha256-16 逐文件复核 **全部匹配**(冻结样卷零修改) |
| 模型可用性 | 两模型均经真实 API 调用验证(见 §3 与 `model-identity-verification.md`) |

## 2. Reviewer 指定与隔离要求

- Reviewer A:DeepSeek V4 Flash(模型ID `deepseek-v4-flash`)
- Reviewer B:GLM-5.3-Flash(模型ID `glm-5.3-flash`)
- 禁止以一个模型模拟另一个;禁止 Mock。
- 每个 Reviewer 单元均为**独立、无状态、单轮**真实 API 调用:新上下文、只含当前样卷材料 + 冻结标准 + 输出 Schema。
- 不向模型提供:TASCO 研究对话、Paper B 结论、R4/R5/R6 归因报告、封存映射(`mapping.json` 全程未打开,含策略身份信息)、另一 Reviewer 的任何结果。
- 已知局限(必须随结果声明):GLM-5.3-Flash 曾用于 TASCO 研究执行,故本轮结论只能称"隔离执行的模型评估"。

## 3. 模型身份冻结(探针证据)

身份探针(真实调用,非标注单元;原始响应存 `model-probe-REVIEWER_A.json` / `model-probe-REVIEWER_B.json`):

| Reviewer | 提供商/端点主机 | 请求 model 字段 | 响应 model 字段 | HTTP | api_style |
| --- | --- | --- | --- | --- | --- |
| REVIEWER_A | api.deepseek.com(DeepSeek 官方 Anthropic 兼容端点) | deepseek-v4-flash | deepseek-v4-flash | 200 | anthropic_messages |
| REVIEWER_B | st8tp3ajl0df3n8b8l8qu.apigateway-cn-beijing.volceapi.com(火山AI网关 OpenAI 兼容端点) | glm-5.3-flash | glm-5.3-flash | 200 | openai_chat |

- 名称→模型ID映射:DeepSeek V4 Flash → `deepseek-v4-flash`;GLM-5.3-Flash → `glm-5.3-flash`。以**响应体 model 字段**为权威身份证据;每标注单元均记录 `response_model_field`。
- 凭据运行时从本地配置加载(env `ANTHROPIC_AUTH_TOKEN` / opencode jsonc),**不写入任何交付物与日志**。

## 4. 推理参数(冻结)

| 参数 | 值 |
| --- | --- |
| temperature | 0.0 |
| max_tokens | 2048 |
| 请求超时 | 600 s |
| top_p / 其他采样参数 | 不设置(用提供商默认) |
| 每单元调用次数 | 正常 1 次;仅格式/传输失败时按 §7 重试 |

## 5. Prompt 模板(冻结,两 Reviewer 完全一致)

SYSTEM(逐字):

```
You are an independent blind reviewer of compressed context views. You receive exactly one sample: (1) an in-context text that an agent saw, and (2) attached side-store original file(s). Compare them and answer four pre-defined questions. Judge ONLY from the provided materials; do not assume facts about how the material was produced. Output ONLY a single JSON object matching the required schema - no markdown fences, no extra text.
```

USER 模板(逐字;`{...}` 为填充位):

```
## Frozen review criteria (authoritative; do not reinterpret)
Pre-defined error types (from the frozen REVIEWER-SHEET):
- E1 diagnostic_loss: a diagnostic line in the original is missing in-context
- E2 critical_change: a diagnostic line is altered/truncated
- E3 semantic_ambiguity: in-context version introduces ambiguity about the original
- E4 pointer_integrity: pointer does not resolve to the attached original
- PASS: none of the above

Questions:
- Q1 (E1): Is any line of the side-store original(s) that appears to be a diagnostic (error/assert/traceback/exception/fatal) missing from the in-context text?
- Q2 (E2): Is any diagnostic line altered or truncated relative to the original?
- Q3 (E3): Does the in-context version introduce ambiguity about the original content?
- Q4 (E4): Does the in-context pointer resolve to the attached original(s) (sha match)?

Rules:
- The in-context text may contain lines starting with "[VIEW-STORED:" (markers/pointers) and a "[VIEW-STORED critical lines retained verbatim:]" block. Marker lines are pointers, not content; judge the surrounding content.
- The sha16 value in the marker identifies which attached side-store original the in-context text was produced from. For Q1-Q3 compare the in-context content against THAT original.
- Q4 checks: (a) the marker's sha16 equals the sha16 of one attached original; (b) the retained critical lines in-context appear verbatim in that original.
- Diagnostic lines include lines containing or conveying: error, assert, traceback, exception, fatal, throw, catch, fail, stack, warn, and surrounding handling logic that carries the same diagnostic meaning.
- Answer each Q with exactly one of: "yes" | "no" | "uncertain".
- verdict: "PASS" only if all four answers are "no"; "FAIL" if any answer is "yes"; otherwise "UNCERTAIN".
- If you cannot determine an answer from the provided materials, you MUST answer "uncertain" - never default to PASS.
- error_types lists the E-types whose Q answer is "yes" (subset of ["E1","E2","E3","E4"]; empty list if none).
- evidence_locations: line numbers or ranges in the original / in-context that justify each "yes"/"uncertain" answer (e.g. "original:102-104 vs in-context:missing"). At least one location per non-"no" answer.
- reasoning_summary: at most 80 words, conclusion-relevant facts only (which lines were compared, what was found/missing). Do not output a chain-of-thought.

## Output schema (single JSON object, nothing else)
{"sample_id":"SXX","reviewer_id":"REVIEWER_X","verified_model_id":"<the model id you identify as>","Q1":"no","Q2":"no","Q3":"no","Q4":"no","error_types":[],"verdict":"PASS","evidence_locations":["..."],"reasoning_summary":"...","status":"ok"}
- Q1..Q4 in {"yes","no","uncertain"}; error_types subset of ["E1","E2","E3","E4"]; verdict in {"PASS","FAIL","UNCERTAIN"}; status="ok".

## Sample {SAMPLE_ID}
### in-context text (verbatim)
{IN_CONTEXT_TEXT}
### attached side-store originals (verbatim; each labeled by its sha16 file stem)
{ORIGINALS_BLOCK}
```

`{ORIGINALS_BLOCK}` 对样卷 `side_store_originals` **全量**附件(冻结样卷定义),每个按
`#### original sha16={SHA16} (chars={N})\n{STORE_TEXT}` 逐字拼入;不做任何改写、不裁剪、不重排。

## 6. 输出 Schema 与判定一致性规则(冻结)

字段:`sample_id, reviewer_id, verified_model_id, Q1, Q2, Q3, Q4, error_types, verdict, evidence_locations, reasoning_summary, status`。

- `Q1..Q4 ∈ {"yes","no","uncertain"}`;`error_types ⊆ {E1,E2,E3,E4}`;`verdict ∈ {PASS,FAIL,UNCERTAIN}`;`status="ok"`。
- 一致性:E1∈error_types ⟺ Q1="yes";E2⟺Q2="yes";E3⟺Q3="yes";E4⟺Q4="yes"。
- verdict 规则:任一 Q="yes" → FAIL;全部 "no" → PASS;否则(≥1 个 uncertain 且无 yes)→ UNCERTAIN。
- UNCERTAIN 是有效的不确定性判定,**不计为安全 PASS**。
- `verified_model_id` 为模型自报(辅助证据);权威身份 = API 响应体 model 字段,逐单元记录。

## 7. 错误处理与重试策略(冻结)

仅以下情形允许重试,最多 2 次(每单元总计 ≤3 次尝试),重试使用**逐字相同**的冻结 prompt 与参数:

1. 传输错误/超时/HTTP≠200;
2. 输出不是合法 JSON 或不符合 Schema;
3. verdict 与 Q1–Q4 规则不一致(格式级不一致)。

**禁止**依据判定内容(如结果不合预期)选择性重试。3 次均失败 → 该单元 `status=INVALID`,保留原始响应,计入 AUDIT_INCOMPLETE 候选。运行器支持断点续跑:已存在合法结果(status∈{ok,invalid})的单元自动跳过,避免重复标注。

## 8. 样本顺序与哈希(冻结)

执行顺序:S01→S30(两 Reviewer 同序)。样卷 sha256-16(与 file-inventory.json 一致,执行时逐单元复核):

| 样卷 | sha256-16 | 样卷 | sha256-16 | 样卷 | sha256-16 |
| --- | --- | --- | --- | --- | --- |
| S01 | b140c19cc52ead58 | S11 | 462d22a2180fe6a9 | S21 | bf78d5fb5c19366e |
| S02 | 702936d00c727f80 | S12 | f56e41538de043fe | S22 | 9543a1ca85d52e6f |
| S03 | 546a4e0fa8d4d3f1 | S13 | 678e1c34d367c0f4 | S23 | 585709309b85d153 |
| S04 | 1686496e9fb7ef05 | S14 | 83523839af7b0a42 | S24 | b4c95eae698fc618 |
| S05 | a446e1877e3cee08 | S15 | ee5786832c861b48 | S25 | 69601772ea333ba0 |
| S06 | a36e8fee8eff9c70 | S16 | 59d7d65736442d06 | S26 | 553860265581ff36 |
| S07 | dca184f3e7d0e8d9 | S17 | ced83f04317336a8 | S27 | cbc0f2ba3147ab1e |
| S08 | 206a508ae879e130 | S18 | f129503c72902954 | S28 | 5554024b8acc1e45 |
| S09 | 59f56af36b2961a0 | S19 | 9473874c14e08f99 | S29 | 2ac6dfd7861583fd |
| S10 | 01074c259530aa88 | S20 | 009549a940611d30 | S30 | 510ee4cab91dbcca |

执行前/后均重跑完整性校验(35/35 匹配)方为有效。

## 9. Smoke Test(冻结)

先用 S01、S02 对两模型执行;判定通过条件:HTTP 200、响应 model 字段与协议模型ID一致、输出合法 JSON 且符合 Schema、verdict 与 Q1–Q4 自洽。通过后协议不变继续 S03–S30;S01/S02 的结果**直接纳入最终结果,不重复调用**。

## 10. 交付物与禁改项

交付物写入本目录(见任务书清单,共 13 项)。禁改:冻结样卷、REVIEWER-SHEET、E4 预检、mapping.json、历史研究证据;不写 `review-sheet-answers-A/B.md`;HUMAN G5 保持 PENDING;不自动宣称 FINAL_SUBMISSION_READY。
