# 最终发布审批材料(publication-decision-sheet 终态文件)— Paper B GitHub

## 终态

> ## **PUBLICATION_OWNER_ACTION_REQUIRED**

(本地候选包已准备完成——129 文件、39 项复现校验全 PASS;**但公开发布需负责人完成 §决策表中的 D1–D5 五项阻塞决策**。不自动投稿、不自动创建远程仓库。)

## 发布决策表(详细版见 publication-decision-sheet.md)

| 决策 | 阻塞? | 负责人须做 |
|---|---|---|
| D1 投稿 venue | **是**(链式起点) | 确认 venue → 决定匿名格式 |
| D2 作者信息 | **是** | 填入实名+单位+邮箱 |
| D3 Data Availability | **是** | 确认 (a)/(b) 选项 |
| D4 Code Availability | **是** | 确认发布范围 |
| D5 TASCO LICENSE | **是** | 选择许可证类型 |
| D6 HF 语料许可 | 否 | 核验 HF 页面许可 |
| D7 Springer 模板 | 否 | 确认或删除模板文件 |
| D8 轨迹发布 | 否 | 维持不公开或审批 |
| D9 G5 人工审核 | 否 | 指派人工评审人或维持 PENDING |

## 技术就绪度(已验证,无需重做)

| 项 | 状态 |
|---|---|
| 复现验证 | 39 PASS / 0 FAIL / 4 UNAVAILABLE |
| manifest | 123 条,0 mismatch |
| 隔离测试 | exit 0(两包均通过) |
| 安全扫描 | 0 凭据泄漏;内部路径已声明 |
| 论文编译 | 12 页,0 undefined,0 error |
| 图表 | 7 张彩色矢量图 + 4 表 |
| Supplement | ESM_1.pdf 5 页 |

## 候选包文件清单

129 文件(见 manifest.sha256);分 7 目录:

| 目录 | 文件 |
|---|---|
| paper/ | 10(终稿 PDF/Tex + refs + ESM + 7 图) |
| prereg/ | 6 |
| data/ | 24 |
| mechanisms/ | 8 |
| analysis/ | 8 |
| audit/ | 68(G5 盲审 34 + 双模型 15 + 根因 19) |
| trajectories/ | 1 |
| reproduction/ | 2 |
| root | 11(README + .gitignore + LICENSE-NOTE + manifest + 5 份报告 + ESM + LICENSE 占位) |
