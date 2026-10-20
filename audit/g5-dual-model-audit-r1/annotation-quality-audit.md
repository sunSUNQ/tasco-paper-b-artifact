# 标注质量审计 — G5-DUAL-MODEL-ANNOTATION-R1

数据源:`annotation-quality-audit.json`(自动化校验器 `scripts/dm_validate.py` 输出)+ `execution-ledger.jsonl`。
性质:机械/规则校验,**不产生任何新判定**。

## 1. Step 4 十项校验结果

| # | 检查项 | 结果 |
| --- | --- | --- |
| 1 | Reviewer A 30/30 覆盖 | PASS(30 单元,0 缺失,0 重复) |
| 2 | Reviewer B 30/30 覆盖 | PASS(30 单元,0 缺失,0 重复) |
| 3 | Sample ID 无缺失/重复 | PASS(S01–S30 × 2) |
| 4 | 输出 Schema 全部合法 | PASS(60/60;12 字段齐全、类型正确) |
| 5 | Verdict 与 Q1–Q4 规则一致 | PASS(60/60;含 FAIL⟺存在 yes、PASS⟺全 no、UNCERTAIN 规则) |
| 6 | E1–E4 分类有效 | PASS(60/60;error_types 与 Q=yes 严格双射) |
| 7 | 证据位置可追溯 | PASS(60/60;凡 Q≠"no" 均有 ≥1 条证据;行号均在合理范围,sha16 已从行号提取中剔除) |
| 8 | 模型身份真实且符合要求 | PASS(60/60 响应 model 字段 = 协议模型ID;详见 model-identity-verification.md) |
| 9 | 无跨 Reviewer 泄漏 | PASS(重建 Prompt 逐字比对:两 Reviewer 模板仅 reviewer_id 填充不同;互不包含对方产物) |
| 10 | 冻结样卷与标准零修改 | PASS(执行前后两次全量校验,35/35 文件 sha256-16 与 file-inventory.json 一致) |

- UNCERTAIN 计数:A=0,B=0(有效的不确定性判定通道未被使用,如实统计)。
- INVALID 计数:0(最终协议下无单元耗尽 3 次尝试)。
- INFRA_BLOCKED:无。

## 2. 执行台账对账

- `ANNOTATION_ATTEMPT` 共 **92 条**(2026-10-19T14:58:23 → 17:38:35),其中 outcome=valid 64 条、invalid 28 条。
- 92 条 = 三轮被协议修正案替代的 Smoke 调用(33 条,含 24 条 invalid 与 4 条被修正案 3 取代的有效调用)+ 最终协议 59 条调用(60 个有效单元,其中 4 个单元各含 1 次格式级重试)。
- 28 条 invalid 全部为格式级(`no_json_extracted` / `reviewer_id_mismatch` / `length` 截断),**无一例依据判定内容重试**。
- 每轮被替代调用的原始响应归档于 `smoke-failed-attempt-r1/`(r1/r2/-r3 标记),结果文件中已清除对应行;台账为追加式,完整保留全部历史。

## 3. 机械证据交叉核验(审计性,非第三评审)

对 30 份样卷的两个高频声明做了逐样本机械核验(`annotation-quality-audit.json` → `mechanical_evidence_checks`):

1. **exhausted_retries 失败返回行**:全部 30 份样卷的 marker 指向原文中均存在 4 行
   `return { ok: false, reason: "exhausted_retries", attempts: attempt };`(run a302/ce49:行标签 55/100/145/190;run 2e2b:56/101/146/191),
   且全部 30 份 in-context 文本中均**不含**字符串 `exhausted_retries`。
   → Reviewer A 对 24 份样本的 E1 判定,其事实基础在机械层面**全部成立**;
   → 但 A 在 6 份样本上未报告该事实(S07、S09、S14、S16、S20 判 PASS,S17 仅报 E3),即 **A 对该机械事实的敏感度为 24/30(80%)**;
   → B 在 30 份上均未报告该事实(**敏感度 0/30**)。
2. **未声明缺口(行 18–20)**:全部 30 份样卷的 marker 声明省略范围自第 21(或 22)行起,而 in-context 头部止于第 17 行,行 18–20 既未展示、也未包含在声明的省略范围内。
   → A 以 E3 报告了 11/30,B 报告了 1/30(S21)。

**含义**:两缺陷在 30/30 样卷机械层面客观存在,但两位 Reviewer 均未完整检出 —— 双模型审核本身也
存在漏检(A>,B≫A)。任何"双模型 PASS"都不能被解释为"样卷无缺陷"。

## 4. 重试与选择性质疑排查

- 重试触发原因均为格式/传输级(见 §2),冻结策略:最多 3 次尝试、逐字相同 prompt、temperature=0。
- 无任何按期望结论的选择性重试;全部尝试(含失败)留痕于台账与原始响应目录。

## 5. 局限声明

- 本审计为**隔离执行的模型评估**,非人工盲审;Reviewer B 所用模型(GLM-5.3-Flash)曾用于 TASCO 研究执行。
- 两个 Reviewer 对机械可证事实的检出均不完整,故双模型审核结论只能用于**发现风险**,不能用于**证明安全**。
- 30 份样卷来自 3 个 evidence run(10/13/7),视图级统计不可解释为任务级安全性(详见 case-cluster-analysis.md)。
