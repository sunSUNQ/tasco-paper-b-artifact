# G5-E4-MECHANICAL-PREFLIGHT-R1 — 报告

**MECHANICAL_ONLY — 本结果不计入 G5 人工审核;G5 状态仍为 HUMAN_INPUT_PENDING**

## 范围与约束执行

- 仅 E4 机械完整性;**未执行 E1–E3 语义判断;未填写人工评审表;未查看人工结论**
- 冻结样卷零改动;无版本/Tag;哈希算法 = SHA256(UTF-8),marker/store 标识 = 前 16 位

## 逐样本结果(30/30 PASS;完整证据见 e4-mechanical-preflight.json)

| 检查 | 结果 |
|---|---|
| E4.1 样本 ID S01–S30 连续唯一 | ✓ |
| E4.2 marker sha16 提取(每样本 1 个) | ✓ 30/30 |
| E4.3 marker sha16 = store 文件名 = sha256(内容)[:16] | ✓ 30/30 全部一致 |
| E4.4 store 文件存在于映射 run 的 `.r5-store/` | ✓ 30/30 |
| E4.5 逐字包含:in-context 全部非 marker 行 ⊆ 原文行集 | ✓ 30/30 |
| E4.6 mapping 完整 + blind 文件哈希复算一致 | ✓ 30/30 |
| E4.7 跨 case 泄漏(store 文件仅解析于映射 run) | ✓ 无泄漏 |

## 过程缺陷修复留痕(1 项,非数据问题)

- **D-fix-1(预检脚本校准)**:哈希复算初版使用 `ensure_ascii=False`,与生成时的
  默认 `ensure_ascii=True` 序列化不一致 → 30 样本误报 FAIL;修正为与生成侧相同的
  规范化后全部 PASS。**存储内容与 marker 自始至终一致 —— 这是审计工具缺陷,非样卷
  缺陷。**

## 两项披露(非 HOLD 事项,如实记录)

1. **样卷聚集**:30 份样卷来自 3 个 evidence run(a302a9…×10、ce4998…×13、
   2e2bda…×7 —— 对应 3 个 case 的多 marker 视图事件)。G5 盲审的诊断保护结论
   **覆盖范围为这 3 个 case 的视图,非全 100-case 多样性**;扩展样卷需新采样批次。
2. **哈希校准**:见 D-fix-1。

## G5 状态(不变)

**HUMAN_INPUT_PENDING** —— E4 机械预检不替代人工评审;Q1–Q3 语义判断与最终
Verdict 仍待两名独立人工评审人完成(材料分发就绪)。
