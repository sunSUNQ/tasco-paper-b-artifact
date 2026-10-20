# 发布决策表(publication-decision-sheet)— Paper B GitHub Artifact

日期:2026-10-20 · 基线:`papers/paper-b-github-candidate/`(129 文件,39 PASS / 0 FAIL / 4 UNAVAILABLE)
**本表集中整理全部待决事项,不代替负责人签署声明。**

## 决策总览

| # | 决策 | 阻塞公开发布? | 当前证据 | 建议决策 | 负责人须确认 |
|---|---|---|---|---|---|
| D1 | 投稿 venue 与匿名要求 | **是**(决定作者区格式与工件匿名化) | Paper B 当前稿非双盲;EMSE 已核验 single-blind;ESEM 2027 为 double-anonymous | EMSE(journal, single-blind, 滚动投稿) | 确认 venue;如双盲需匿名改写 |
| D2 | 作者信息 | **是**(论文标题页) | 占位 `[AUTHORS TO BE PROVIDED]` | 提供实名/单位/通讯邮箱 | 作者名单+顺序+ORCID |
| D3 | Data Availability | **是**(EMSE 强制;缺则退回) | Artifacts A–G 段内容齐全但格式为非标准 | 改写为 Springer 标准 Data Availability Statement 声明段 | 确认选项 (a) 公开 DOI 或 (b) 通讯作者提供 |
| D4 | Code Availability | **是**(同上) | mechanisms/ + analysis/ + reproduction/ 已在包内 | 声明"代码随文发布"或"联系通讯作者" | 确认发布范围 |
| D5 | TASCO LICENSE | **是**(公开仓库必须有 LICENSE 文件) | LICENSE-NOTE.md 占位 | 建议 MIT 或 Apache-2.0 | 选择许可证类型 |
| D6 | HF 数据许可 | **否**(原始数据不转载,仅给获取指令) | data/THIRD-PARTY.md 给出 HF 链接 + "verify on dataset page" | 在 HF 页面确认两数据集许可后在 README 补注 | 核验 Thoughtworks/OSW-Traces 页面许可条款 |
| D7 | Springer 模板再分发 | **否**(svjour3.cls 仅用于本地编译,正式排版由出版社) | svjour3.cls + spbasic.bst 在投稿包内 | 确认 Springer 模板允许随投稿源码分发(通常允许) | 如担忧可删除模板文件(审稿人可用公共模板重编译) |
| D8 | 原始轨迹公开 | **否**(默认不公开,README 已声明) | trajectories/READ-ME-FIRST.md 政策文件 | 维持不公开;全量扫描+许可审查完成后再评估 | 是否执行全量扫描;扫描结果是否满足发布条件 |
| D9 | G5 人工审核 | **否**(正文已如实声明 model-assisted + human pending) | HUMAN-INPUT-PENDING.md;G5 协议+盲审包+审计链完整 | 如需完成,按冻结 G5 协议执行人工评审 | 指派人工评审人或确认维持 PENDING |

## 阻塞分析

- **阻塞公开发布的决策**:D1(venue)→ D2(作者)→ D3/D4(声明)→ D5(LICENSE)——四项形成链式依赖:venue 决定匿名→决定作者格式→决定声明措辞→决定 LICENSE。
- **不阻塞但建议完成的决策**:D6(HF 许可)、D7(Springer 模板)、D8(轨迹)、D9(G5 人工审核)。

## 建议执行顺序

1. D1:确认 venue → 确定匿名格式
2. D5:选择 LICENSE → 添加 LICENSE 文件
3. D2:填写作者信息
4. D3/D4:定稿可用性声明
5. D6/D7:核验许可与模板
6. D8/D9:按需执行
7. 最终目视复核 → 创建远程仓库 → push
