# 许可与匿名门禁(license-and-anonymity-gates)— Paper B GitHub 发布

## 许可门禁

| 门 | 内容 | 当前状态 | 解除条件 |
|---|---|---|---|
| L1 TASCO 代码 LICENSE | 包内 .py/.js/.md 文件的许可证未选定 | LICENSE-NOTE.md 占位 | 负责人选择 MIT/Apache-2.0/其他 → 添加 LICENSE 文件 |
| L2 Springer 模板再分发 | svjour3.cls + spbasic.bst 随投稿包分发 | 通常允许(Springer 模板公共下载);如需确认,查 Springer LaTeX 使用条款 | 确认或删除模板文件 |
| L3 HF Thoughtworks 语料 | 许可未核验(HF 页面本轮不可达) | 获取指令在 data/THIRD-PARTY.md;原始数据不转载 | 确认 HF 页面许可条款 |
| L4 HF Open-SWE-Traces 语料 | 同上 | 同上 | 同上 |
| L5 opencode CLI 引用 | AGPL-3.0 公开工具;仅版本引用,不重分发代码 | 无障碍 | 无 |

## 匿名门禁

| 门 | 内容 | 当前状态 | 解除条件 |
|---|---|---|---|
| A1 作者匿名 | Paper B 当前稿使用 "TASCO Research Group"(组名,非个人);EMSE single-blind 不要求匿名 | 无障碍(EMSE);如投双盲需改写 | 确认 venue 后执行 |
| A2 工件匿名 | 包内 README 引用 "TASCO" 品牌与内部路径;双盲投稿需匿名镜像 | EMSE single-blind 不要求;双盲需脱敏 | 按 venue 决定 |
| A3 G5 审计匿名 | G5 使用 "TASCO" 品牌 + 内部路径(冻结审计链);论文中已声明为 model-assisted audit | EMSE single-blind 不要求脱敏 | 同上 |

## 结论

- **EMSE(single-blind)**:无匿名阻塞;仅 L1(LICENSE)+ D2(作者)+ D3/D4(声明)待填。
- **ESEM 2027(double-blind)**:需匿名化全包(A1+A2+A3)+ 改写作者区;工作量约 1–2 天。
