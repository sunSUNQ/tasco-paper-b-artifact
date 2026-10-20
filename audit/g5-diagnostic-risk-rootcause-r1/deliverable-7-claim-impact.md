# 交付物 7 — C1–C15 主张影响清单(G5-DIAGNOSTIC-RISK-ROOTCAUSE-R1)

依据:draft-v1/evidence-mapping.md 主张表(v2 修正版,7 SS + 4 SWL + 2 H + 2 U)+ LaTeX 正文相关表述。
评级:UNCHANGED / NEEDS_QUALIFICATION / NEEDS_CORRECTION / UNSUPPORTED。
**本文档不修改论文正文;正式修订需研究负责人批准。**

## C1–C15 逐条

| # | 主张(摘要) | 原档 | 本轮影响 | 处置 |
|---|---|---|---|---|
| C1 | 三机制 170 case:Input 净收益为零或负 | SS | 审计对象为 M3 的**诊断可见性**,与 input-token 计量口径无关;store 无损、机制行为与论文测量一致 | **UNCHANGED** |
| C2 | 取回/补偿轮次的重发放大是支配性成本 | SS | 同上,轮次放大计量不受影响 | **UNCHANGED** |
| C3 | 安全面 ≈1.7% 低于可测门槛 | SS | M2 门控"diagnostic-bearing outputs are never folded"与 M3 同族使用词面诊断口径;门槛数字本身不受影响,但门控的"诊断"定义须在文中标明词面口径 | **NEEDS_QUALIFICATION**(门控诊断口径注明) |
| C4 | 全部压缩臂 oracle 无退化(未观察到) | SS | oracle 口径(测试命令/文本标记)与本轮发现的"即时诊断可见性"是不同维度;oracle 结果不受影响 | **UNCHANGED**(口径限定:oracle 成功 ≠ 诊断可见性) |
| C5 | 族别结构 | SWL | 无关 | **UNCHANGED** |
| C6 | 无预可观测判别特征 | SWL | 无关 | **UNCHANGED** |
| C7 | 离线普查预测暴露 | SS | 无关 | **UNCHANGED** |
| C8 | σ̂_w=0.155 [0.093,0.197] | SS | 无关 | **UNCHANGED** |
| C9 | 恢复是真实行为且链路完整 | SS | 本轮反向强化:store==源文件 30/30、sha 全一致、C==agent 所见 30/30 —— 恢复完整性获得独立复核 | **UNCHANGED**(证据增强) |
| C10 | 零取回子群正收益但不可事前识别 | SWL | 无关 | **UNCHANGED** |
| C11 | 暴露可泛化(D3 29.5% proxy) | SWL | 无关 | **UNCHANGED** |
| C12 | turn-neutral 静默截断可能有效 | H | **直接受损**:M3 的"静默省略无关键词失败返回"正是该假设的实例形态;假设成立的前提必须加入"诊断信息即时可见性有保证" | **NEEDS_QUALIFICATION**(加前提条件) |
| C13 | 语义保真压缩可行 | H | **直接受损**:冻结实现按词面口径执行"诊断行保留",语义保真未达成(12 唯一诊断行 30 视图全部不可见);可行性主张须降为"在显式诊断可见性合约下待验证" | **NEEDS_QUALIFICATION**(前提收窄;若坚持"语义保真"措辞则 NEEDS_CORRECTION) |
| C14 | "所有压缩策略无效"(全称否定) | U(禁止) | 无关(本就弃用) | **UNCHANGED** |
| C15 | "RDS +7.38% 收益" | U(禁止) | 无关(本就弃用) | **UNCHANGED** |

## C1–C15 之外的正文表述(本轮审计直接命中)

| 位置 | 表述 | 处置 |
|---|---|---|
| 标题/摘要 "Lossless" | 字节级无损(store+恢复)经本轮独立复核**成立** | **UNCHANGED**,但须与"即时诊断可见性"明确区分(修订时在 §3 加一句限定) |
| §3 M3:"all diagnostic lines verbatim" | **语义口径下不成立**(ER 行 12 唯一/120 视图实例未呈现);词面口径下成立但文中未定义口径 | **NEEDS_CORRECTION**:或修机制(插件 v2)后重取证据,或改写为"diagnostic lines (keyword-caliber: fail/error/assert/traceback/exception/fatal/denied/not found) verbatim; non-keyword failure returns recoverable via side store only",并引用本轮缺陷 |
| §3 部署合约 "markers are auditable" | marker 坐标系错位(E3 根因)损害可审计性 | **NEEDS_QUALIFICATION**(注明坐标系缺陷与修复计划) |
| §"Deterministic scaffolding":"reconstruction is byte-exact" | V1/V2 独立复核成立 | **UNCHANGED** |
| 诊断保护证据 "24,648 视图零膨胀;30 样卷"(evidence-mapping L20)| 该证据为 **DIAG 词面口径**的 before==after 计数,不能支持语义口径的"诊断信息保护" | **NEEDS_QUALIFICATION**(口径限定) |

## EVIDENCE_BLOCKED 标记(按冻结接收规则)

冻结接收规则(`final-seal/HUMAN-INPUT-PENDING.md` L37–38)早已预定:"发现 E1/E2 诊断丢失/关键改动
⇒ **EVIDENCE_BLOCKED(返回修正)**"。本轮根因审计在语义口径下确认 E1 型诊断丢失(交付物 2/6),
故:

- **M3 的诊断保护相关安全表述("all diagnostic lines verbatim" 及依赖它的 C12/C13 前提)
  标记 EVIDENCE_BLOCKED**,直至 (i) 插件 v2 冻结 + 新证据轮,或 (ii) 研究负责人批准按词面口径
  改写并显式披露缺陷。
- C1–C11 的计量类主张不受阻断(不同口径);C9 证据反而增强。
- 本清单仅为审计裁定;论文正文的任何修改须研究负责人批准后另行执行。
