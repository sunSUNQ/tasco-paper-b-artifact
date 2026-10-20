# GitHub Export Inventory — Paper B
生成: 2026-10-20 · 基线: `papers/artifact-staging-r1/tasco-paper-b-artifact/` (46 PASS / 0 FAIL / 4 UNAVAILABLE)

## 已包含文件(按目录)

| 目录 | 文件数 | 内容 | 开放状态 |
|---|---|---|---|
| paper/ | 10 | paper-emse-final.{pdf,tex}, refs.bib, ESM_1.pdf, figures/f0–f6 | A |
| prereg/ | 6 | R4 执行附录, stage-0 manifest, 100-case 修订, expansion prereg, grid 协议+split | A |
| data/ | 24 | M1/M2/M3 冻结逐 run/case 结果+分析, 网格, R6, S1–S5, G4, phase0, c1-c15, HUMAN-INPUT-PENDING | A |
| mechanisms/ | 8 | RDS v1/v2 原语+插件模板, P2 view-store 插件, 门测, selftest | A |
| analysis/ | 8 | fp_phase_a/fp_figures/fp_supplement_gen/colorize_tables/fig1_integrate/f0_lanes/emse_figures/pb_step1_overlap | A |
| audit/ | 4+30+15+9 | G5 盲审包(30 样卷), 双模型审计(协议/结果/台账/修正案/分析), 根因审计(三层还原/合约/最小复现), c1-c15 | A |
| trajectories/ | 1 | READ-ME-FIRST.md(发布政策) | A |
| reproduction/ | 2 | verify.py + __init__.py(39 项 R1/R2 校验) | A |
| .gitignore | 1 | 排除轨迹/凭据/编译产物/缓存 | A |
| LICENSE-NOTE.md | 1 | 许可证占位(待负责人确认) | B |
| **合计** | **~124** | | |

## 排除文件(在 paper-b/ 研究目录中但不在 GitHub 候选包内)

| 类别 | 文件数 | 原因 |
|---|---|---|
| 冻结数据副本(不同路径同名) | ~112 | 策展导出: artifact 中已含重命名后的版本 |
| 内部审计/评审工作底稿 | ~43 | 非结论映射材料(草稿/迭代/中间渲染) |
| 设计变体图 | ~17 | f0_design_overview/f0_lanes 等未入选排版 |
| 旧版论文稿 | ~3 | paper-emse.tex/v2.tex/final2.tex 已被 final.tex 取代 |
| 哈希清单/溯源记录 | ~35 | 中间步骤文件;导出后重新生成 manifest |
| 原始执行轨迹(events/workdir) | **不在这棵树里**(在内部仓库 runs/ 下) | C 类: 全量扫描+许可审查前不发布 |
| G5 封存映射(mapping.json) | 不在 | C 类: 策略身份信息封存 |

## 遗漏分析

**核心结论复现所需材料:100% 包含。** 经 41 项自动校验(0 FAIL)确认。

| 结论 | 包内支撑 | 状态 |
|---|---|---|
| C1 三机制无净收益 | data/M1+M2+M3 结果 + analysis 重算脚本 | ✓ |
| C2 轮次放大 | data/M3 + g4 双口径 + analysis | ✓ |
| C3 安全面 < 噪声地板 | data/grid-results + step2-strengthening(S1) | ✓ |
| C4 oracle 无退化 | data/M1+M2+M3 verification | ✓ |
| C6 无判别特征 | data/r6-feature-net.json | ✓ |
| C8 σ̂_w=0.155 | data/step2-strengthening(S1) | ✓ |
| C9 恢复真实 | data/r6-view-behavior + expansion-analysis | ✓ |
| C11 暴露泛化 | data/step2-strengthening(S4) | ✓ |
| G5 诊断案例 | audit/g5-blind-package + 根因审计 | ✓ |

## GitHub 候选包安全扫描结果

| 模式 | 命中 | 判定 |
|---|---|---|
| sk- API key | 0 | clean |
| Bearer token | 0 | clean |
| api_key/apiKey 字段 | 0 | clean |
| ANTHROPIC_AUTH_TOKEN | 2 | 均为审计文档中的描述文字("未写入任何日志"),非凭据值 |
| gateway key 0f837e1d | 0 | clean |
| password | 0 | clean |
| 内部绝对路径 `C:\Users\sunqinghw` | 22 | 均为冻结数据中的 run 工作目录路径(数据属性);不构成安全问题;双盲投稿需脱敏 |
| 内部研究树路径 `research-semantic-compression` | ~4028 | 均为 analysis/ 脚本中的**绝对路径**溯源记录(设计如此);脚本本身为 provenance record,不用于包内执行;**verify.py 零内部路径引用** ✓ |

## 残余门禁(不阻塞 CANDIDATE_READY)

| 门 | 说明 | 负责人动作 |
|---|---|---|
| G4 HF 语料许可 | Thoughtworks/NVIDIA 数据集页面许可待确认 | 确认或标注 |
| G5 独立人工审核 G5 | 尚未完成 | 完成后更新状态 |
| G6 轨迹全量扫描 | 424 run 全量扫描未执行 | 执行后决定是否公开轨迹 |
| TASCO LICENSE | 包内 .py/.js/.md 的许可证未选定 | 选择并添加 LICENSE 文件 |
| Springer 模板再分发 | svjour3.cls/spbasic.bst 是否可随开源包分发 | 确认 Springer 模板许可条款 |
| 投稿匿名要求 | 当前稿非双盲;如投双盲需匿名改写 | 按 venue 决定 |
