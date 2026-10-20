# 一致性分析 — G5-DUAL-MODEL-ANNOTATION-R1

数据源:`analysis-stats.json`(由 `scripts/dm_analyze.py` 从 60 个有效单元计算)。
样本:30 份盲审样卷 × 2 Reviewer;verdict 三分类 {PASS, FAIL, UNCERTAIN};本轮 UNCERTAIN 未被使用。

## 1. 基础统计

| 指标 | REVIEWER_A (deepseek-v4-flash) | REVIEWER_B (glm-5.3-flash) |
| --- | --- | --- |
| PASS | 5 | 29 |
| FAIL | 25 | 1 |
| UNCERTAIN | 0 | 0 |
| E1 (diagnostic_loss) | 24 | 0 |
| E2 (critical_change) | 0 | 0 |
| E3 (semantic_ambiguity) | 11 | 1 |
| E4 (pointer_integrity) | 0 | 0 |

- 双模型一致 PASS:**5**(S07、S09、S14、S16、S20)
- 双模型一致 FAIL:**1**(S21;但错误类型不一致:A=E1,B=E3)
- 分歧:**24**(全部为 A=FAIL / B=PASS)

## 2. 一致性指标

### 混淆矩阵(verdict 三分类,行=A,列=B)

| A \ B | PASS | FAIL | UNCERTAIN |
| --- | --- | --- | --- |
| **PASS** | 5 | 0 | 0 |
| **FAIL** | 24 | 1 | 0 |
| **UNCERTAIN** | 0 | 0 | 0 |

### 原始一致率(raw agreement)

po = (5 + 1) / 30 = **0.200**

### Cohen's κ(三分类)

- pe = (5/30)(29/30) + (25/30)(1/30) + 0 = 0.1889
- **κ = (0.200 − 0.1889) / (1 − 0.1889) = 0.0137(几乎为零)**

### PASS / 非 PASS 二分类

| A \ B | PASS | non-PASS |
| --- | --- | --- |
| PASS | 5 | 0 |
| non-PASS | 24 | 1 |

po = 0.200,pe = 0.1889,κ = 0.0137(与三分类相同,因 UNCERTAIN=0 且 B 仅 1 个非 PASS)。

### κ 不稳定性的必要说明(类别极度不均衡)

边缘分布严重偏斜(A:25F/5P;B:1F/29P),pe 接近 0.19 的低位,κ 分母 (1−pe) 小、分子由
两个大单元格之差主导:**混淆矩阵中 ±1~2 个样本的移动即可使 κ 在大范围内摆动**。在此分布下
κ 不具备"机会校正可靠性"的常规解释力,不应引用"κ≈0.014 = 随机一致"这类强表述;描述性结论
以原始一致率 + 混淆矩阵为准:**两位 Reviewer 的 verdict 层一致性实质上很低,分歧集中在
A 检出而 B 未检出的 E1/E3 上**。

## 3. 错误类型层的一致性(非 verdict 层)

- 唯一双 FAIL 样本 S21 的错误类型不一致(A: E1;B: E3),即 verdict 一致 ≠ 理由一致。
- A 报告的 E3 全部指向同一机械可证事实(marker 声明省略自第 21/22 行起,但行 18–20 未展示);
  B 仅在 S21 报告了同一事实 —— B 的 E3 判定与 A 的 E3 判定事实基础相同,只是检出范围不同。

## 4. 与机械核验的对照(摘自 annotation-quality-audit.md §3)

全部 30 份样卷机械层面均存在 (a) 4 行被省略的 `exhausted_retries` 失败返回、(b) 行 18–20 未声明缺口。
- 对 (a):A 检出 24/30,B 检出 0/30。
- 对 (b):A 检出 11/30,B 检出 1/30。
→ 分歧的主因是**两模型对同一客观事实的敏感度差异**,而非对标准的不同解读;但 A 自己也漏检
6 处 (a),说明**没有任何一方可当作 ground truth**。

## 5. 统计口径警告

- 30 份视图仅来自 3 个 evidence run(10/13/7),视图间高度相关;上述一致率/κ 是**视图级**统计,
  **不得**用于推断 30 个独立任务的总体一致性,也不得构造任务级置信区间。
- 主控 Agent 未对 24 个分歧样本做仲裁(未引入第三评审);分歧细节见 disagreement-cases.md。
