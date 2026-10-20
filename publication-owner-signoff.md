# Paper B GitHub Artifact — 负责人签批清单(publication-owner-signoff)

**日期**:2026-10-20 · **基线**:`papers/paper-b-github-candidate/`(129 文件 + manifest,39 PASS / 0 FAIL / 4 UNAVAILABLE)
**终态**:OWNER_SIGNOFF_READY(全部信息已组织完毕,等待负责人逐项签批;签批完成前不投稿、不 push、不创建远程仓库)

---

## D1 投稿 venue 与匿名要求

- **当前状态**:未确认。Paper B 当前稿使用 "TASCO Research Group" 组名,非双盲格式。
- **推荐**:EMSE(Springer 期刊,single-blind,滚动投稿)。依据:主题完美对口、无匿名化工作量、数据可用性要求与本文 Artifacts 一一对应。
- **须负责人填写**:
  - 投稿 venue:____________
  - 如为 double-blind venue:是否执行匿名改写? 是 / 否
- **完成条件**:venue 确认后,作者区按对应格式填写。

## D2 作者信息

- **当前状态**:占位 `[AUTHORS TO BE PROVIDED BY THE RESEARCH LEAD]`。
- **须负责人填写**:
  - 作者名单与顺序:____________
  - 单位(部门/城市/国家):____________
  - 通讯作者邮箱:____________
  - ORCID:____________
- **EMSE 规则**:无机构隶属者仅填城市+国家;LLM 不可署名。
- **完成条件**:标题页无占位符。

## D3 Data Availability

- **当前状态**:占位含两个选项 (a)/(b),由负责人选择。
- **事实基础**:完整证据链(424 轨迹/协议/脚本/审计链)已哈希冻结,索引 1,889 文件。
- **须负责人填写**:
  - 选择:__________(a) 公开仓库 DOI / (b) 通讯作者提供
  - 如选 (a):仓库 URL:____________
  - 发布时间:录用后 / 即时
- **完成条件**:paper-emse-final.tex Declarations 段无占位符。

## D4 Code Availability

- **当前状态**:占位,选项同 D3。
- **事实基础**:analysis/ + mechanisms/ + reproduction/ 共 ~30 文件,全部自产。
- **须负责人填写**:
  - 选择:__________(a) 随 Data Availability 同仓库 / (b) 通讯作者提供
  - 发布范围:全部代码 / 仅 reproduction verify
- **完成条件**:Declarations 段无占位符。

## D5 TASCO LICENSE

- **当前状态**:LICENSE-NOTE.md 占位;包内 .py/.js/.md 许可未选。
- **候选方案(依赖兼容性已核验)**:
  | 方案 | 兼容 | 特点 |
  |---|---|---|
  | MIT | ✓ 所有依赖 | 最宽松;允许商用 |
  | Apache-2.0 | ✓ 所有依赖 | 专利授权;含变更声明义务 |
  | CC-BY-4.0(仅数据/图表) | ✓ | 仅覆盖非代码件 |
  | **不推荐**:GPL/AGPL | — | 对 opencode(AGPL)有传染风险;EMSE 不要求 |
- **须负责人填写**:
  - 选择:____________
  - 版权归属:____________
- **完成条件**:LICENSE 文件存在且为所选许可证全文。

---

## 附:D6–D9(非阻塞,维持现状即可投稿)

| 项 | 当前状态 | 后续动作 |
|---|---|---|
| D6 HF 语料许可 | 待核验(HF 页面本轮不可达) | 在 HF 页面确认许可条款;**原始语料不转载**,仅聚合计数 |
| D7 Springer 模板 | svjour3.cls + spbasic.bst 在投稿包内;Springer 模板通常允许随投稿分发 | 投稿前确认 Springer LaTeX 使用条款 |
| D8 轨迹公开 | trajectories/READ-ME-FIRST.md 声明"待全量扫描+许可审查";**默认不公开** | 如需公开:全量扫描(0 命中)→ 负责人批准 → 加入包 |
| D9 G5 人工审核 | PENDING(正文已如实声明 model-assisted;audit chain 完整) | 指派人工评审人或维持 PENDING |

---

## 页数与 manifest 口径说明

| 项 | 解释 |
|---|---|
| **11→12 页** | 10 页双栏(svjour3 twocolumn)是 Full Revision R1 编译结果;追加 §5.6(G5 案例)+ §6(适用边界)+ §8(Threats 扩写)后重新编译为 12 页——增量全部绑定新内容,无文字填充 |
| **manifest 135 vs 130** | 135 = 包内**全部文件**(含 reproduction/verify.py + __init__.py + .gitignore 等工程文件);130 = "论文交付物"口径(排除编译日志/__pycache__/.gitignore)。差异 5 文件均为基础设施,非内容差异 |
| **168/404/424** | 168 = 168 个 disjoint tasks(8 Stage-0 + 100 M1 + 30 M2 + 30 M3);404 = 380 配对 run + 24 Stage-0 baseline;424 = 404 + 20 smoke pairs。三者分母不同、互不混淆 |

---

## 签批

| # | 决策 | 签名 | 日期 |
|---|---|---|---|
| D1 | 投稿 venue | ____________ | ______ |
| D2 | 作者信息 | ____________ | ______ |
| D3 | Data Availability | ____________ | ______ |
| D4 | Code Availability | ____________ | ______ |
| D5 | TASCO LICENSE | ____________ | ______ |

全部签批后:一次最终编译(更新 Declarations 段)→ 人工目视复核 → 可创建远程仓库并 push。
