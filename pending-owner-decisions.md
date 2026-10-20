# 待负责人决策事项(pending-owner-decisions)

以下决策完成后,GitHub 候选包可从 CANDIDATE 升级为可发布状态。

| # | 决策 | 影响 | 建议 |
|---|---|---|---|
| 1 | **作者与单位信息** | paper-emse-final.tex 中 `\author{}` 为占位;标题页需要实名(EMSE single-blind)或匿名(双盲) | 按 venue 决定 |
| 2 | **Data availability 终稿** | 选项 (a) 公开仓库 DOI 或 (b) 通讯作者提供 | 建议选 (a),配合 GitHub 包发布 |
| 3 | **Code availability 终稿** | 同上 | 同上 |
| 4 | **TASCO LICENSE 选定** | LICENSE-NOTE.md 占位;建议 MIT 或 Apache-2.0 | 选择并添加 LICENSE 文件 |
| 5 | **HF 语料许可核验** | Thoughtworks/Open-SWE-Traces 页面许可未确认 | 确认后从 B 类升 A 类 |
| 6 | **Springer 模板再分发** | svjour3.cls/spbasic.bst 是否可随开源包发布 | 确认 Springer 模板许可条款 |
| 7 | **Paper B 轨迹发布** | 424 run 轨迹待全量扫描+许可审查;未扫描前不发布 | 如需公开,先执行全量扫描 |
| 8 | **投稿 venue 最终确认** | EMSE(single-blind,实名)vs ESEM 2027(double-blind,匿名) | 影响 paper-emse-final.tex 的作者区 |
| 9 | **G5 独立人工审核** | 完成后可从 PENDING 更新为已完成 | 按冻结协议执行 |

以上决策**互不阻塞**——1–4 影响论文稿,5–7 影响工件包,8 影响投稿渠道,9 影响审计链完整性。
