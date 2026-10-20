# Paper B — 证据引用映射表(Evidence Mapping)

每一个正文数字 → 冻结产物路径(哈希见各期 file-inventory)。审计脚本:`closure_audit.py`、
`pb_step1_overlap.py`、`pb_step2_strengthen.py` 均可重跑复核。

| 正文数字 | 来源产物 | 校验 |
|---|---|---|
| 20,000 会话 / 2,757,167,294 obs 字符 | r5/step1-scan/osw-scan.json | census 解析重跑一致 |
| view 45.7% / bash 53.0% / test 0.02% | 同上 | 同上 |
| Stage-0 σ̂_w=0.155;CI [0.093,0.197] | r5/paper-b/draft-v1/step2-strengthening.json S1 | Stage-0 24 run 重算 |
| v1: 542 折叠/561,454 字符;Input −7.08%;median −8.67%;35/62/3;81→80 | r4/100case/paired-execution-results.jsonl + verification-and-analysis.json + closure_audit.json | 双口径(ledger/marker)核对 |
| v2: 折叠 2 次;Input +2.89%;median −0.25%;1.02 调用比 | r4/refinement/refinement-paired-results.jsonl + verification-and-analysis.json | 同上 |
| 离线网格 64 组合;0 达标;最高 1.66%;安全阻挡 245 | r4/refinement-r2/grid-results.json + closure_audit.json | 直接读取 |
| P2: 280 markers/123 恢复;Input −23.0%;CI [−40.8,−7.6];18→20 | r5/expansion/expansion-paired-results.jsonl + expansion-analysis.json | 重算一致 |
| 轮次放大 +4.7 调用/+2.4 steps/+50.5K flow(cache +46.3K) | r5/code/r6_turn_amplification.py 输出(120 run 重算) | 可复跑 |
| 恢复 311 视图/43.4% 被恢复/距离中位 4/回灌 352,804 | r5/workload-screening-r1/view-behavior.jsonl + step1-summary.json | 14+123=137 跨口径一致 |
| 逐恢复归因:123 次/回灌中位 2,562 字符/step input 中位 3,515/相关 r=0.033 | r5/paper-b/draft-v1/step2-strengthening.json S3 | events+ledger 重算 |
| D3 第二语料:P2 触发 52,719/缩减 366M(29.5%) | step2-strengthening.json S4(sessions.parquet 离线) | D3-E4 原语 verbatim |
| 样本独立性:170 case 四组两两不相交 | r5/code/pb_step1_overlap.py 输出 | 程序验证 |
| 诊断保护:24,648 视图零膨胀;30 样卷 | r5/step3-replay/replay-results.json + step2-strengthening.json S5 | 计数 + 抽样 |
| σ̂_w(T)=0.258 vs σ̂_w(B)=0.244(不拒绝相等) | step2-strengthening.json S2 | expansion 2-rep 直测 |

# 主张审计 v2(15 条计数修正:6 SS + 4 SWL + 2 H + 2 U = 15)

相对 R1 版修正:①计数明确化(原表 15 行但档位小计未给出,易误读为 14);②C8 因
σ̂_w CI 补强升 SS;③C11 因 D3 跨语料普查升 SWL;④"成功率保持"表述改为"未观察到
退化",并注明非劣效检验未做功效;⑤C9 归类 SS(137/137 链完整 + 逐恢复明细)。
全部反例与负证据保留(N-FIL03 −825%、N-MOD02 零暴露摆动 2×、X-HI-M01 反例等)。

| # | 主张(v2 修正) | 档 |
|---|---|---|
| C1 | 三机制 170 case:Input 净收益为零或为负 | SS |
| C2 | 取回/补偿轮次的上下文重发放大是支配性成本 | SS |
| C3 | 安全面 ≈1.7% 上下文,低于可测门槛 | SS |
| C4 | 全部压缩臂 oracle 无退化(未观察到;非严格非劣效检验) | SS(表述修正) |
| C5 | 族别结构(mutation+/file-review−) | SWL |
| C6 | 无预可观测判别特征分离恢复需求 | SWL |
| C7 | 离线普查预测暴露(非收益) | SS |
| C8 | σ̂_w≈0.155 [0.093,0.197](task bootstrap) | SS(升档:CI 已测) |
| C9 | 恢复是真实行为且链路完整 | SS |
| C10 | 零取回子群正收益但不可事前识别 | SWL |
| C11 | 其他工作负载暴露可能更高(D3:29.5% proxy) | SWL(升档:第二语料已测) |
| C12 | turn-neutral 静默截断可能有效 | H |
| C13 | 语义保真压缩可行 | H |
| C14 | "所有压缩策略无效"(全称否定) | U(禁止) |
| C15 | "RDS +7.38% 收益"(D3-E5 降级口径) | U(禁止) |
