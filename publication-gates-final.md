# GitHub 发布检查清单与终态(publication-gates-final)— Paper B GitHub Artifact

## 终态

> ## **PUBLICATION_OWNER_APPROVAL_REQUIRED**

(本地候选包 100% 就绪——git init + 144 文件 staged + 39 项复现校验全 PASS;**但 LICENSE 未确认、作者未填入，不满足 push 前置条件**。不自动创建远程仓库、不 push、不投稿。)

## 已完成

| 项 | 状态 |
|---|---|
| 候选包构建 | ✓ 129 文件 + manifest(142 条)|
| 复现验证 | ✓ 39 PASS / 0 FAIL / 4 UNAVAILABLE |
| 隔离测试 | ✓ exit 0 |
| 安全扫描(Git 级) | ✓ 凭据 0 泄漏；内部路径为冻结数据属性 |
| Git 本地仓库 | ✓ `git init` + `git add -A`(144 文件 staged)|
| GitHub 名称可用性 | 已尝试检查(网络受限，结果不确定)|
| README/LICENSE-NOTE/CITATION.cff 等 | ✓ 全部就位 |

## 待负责人完成(按序)

| # | 动作 | 解除什么 |
|---|---|---|
| 1 | 确认投稿 venue(EMSE / ESEM 2027 / 其他) | 决定匿名格式 |
| 2 | 填入作者信息(标题页 `\author{}` + `\institute{}`) | 论文标题页 |
| 3 | 定稿 Data/Code Availability 声明 | Declarations 段 |
| 4 | 选择 TASCO LICENSE(MIT / Apache-2.0) | 添加 LICENSE 文件；git commit |
| 5 | 确认 Springer 模板再分发条款 | 决定 svjour3.cls 是否随包 |
| 6 | 确认 HF 语料许可 | data/THIRD-PARTY.md 措辞 |
| 7 | 人工目视复核 PDF(paper-emse-final.pdf 12 页) | 排版确认 |
| 8 | 创建远程仓库 + push + 设 Public | 公开发布 |
| 9 | G5 人工审核(可选，独立于发布) | HUMAN G5 gate |

## 发布条件(未满足项)

| 条件 | 当前状态 |
|---|---|
| LICENSE 已批准 | ✗ 占位 |
| 作者已填入 | ✗ 占位 |
| 白名单已签署 | ✗ 清单已生成，未签署 |
| 许可/安全问题 | ✓ 无未关闭安全/许可障碍(HF 待核验为 B 类，不阻塞本地) |
| 复现验证 | ✓ 39/0/4 |

## Git 状态

- `git init` 完成;144 文件已 `git add -A` staged
- **无 commit**(需要作者身份——由负责人在 git config 中设置后执行)
- **无 remote**(LICENSE 批准前不创建)
- 这是有意设计：**commit 留给负责人执行**，确保作者身份与 LICENSE 决策一致
