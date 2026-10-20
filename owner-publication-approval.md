# 负责人审批状态(owner-publication-approval)— Paper B GitHub

日期:2026-10-20

## 当前状态:OWNER_APPROVAL_PENDING

## 审批进度

| 步骤 | 状态 | 阻塞原因 |
|---|---|---|
| Step 1 Staged 文件对账 | ✅ 完成(144 文件,0 未授权) | — |
| Step 2 LICENSE 准备 | ⏳ 等待负责人确认 | 负责人未选择许可证类型(MIT 推荐) |
| Step 3 作者身份核对 | ⏳ 等待负责人提供 | 负责人未提供真实作者名单/单位/邮箱 |
| Step 4 负责人公开授权 | ⏳ 等待负责人签署 | 负责人未确认公开范围与匿名影响 |
| Step 5 发布执行 | ❌ 阻塞 | 上游 Step 2–4 未完成 |

## 阻塞项明细

| # | 阻塞 | 需要负责人提供 |
|---|---|---|
| 1 | LICENSE 类型未确认 | 从 {MIT, Apache-2.0} 中选择;版权归属确认 |
| 2 | 作者信息未提供 | 姓名、单位、通讯邮箱、ORCID(或声明无隶属) |
| 3 | Data/Code Availability 声明未定稿 | 选择 (a) 公开仓库或 (b) 通讯作者提供 |
| 4 | 公开范围未签署 | 确认 GitHub 公开操作(含"此公开可能影响未来双盲投稿选择"的认知) |

## Git 状态

- 本地仓库已初始化;144 文件已 `git add -A` staged
- **无 commit**(需要 Git user.name / user.email,由负责人提供)
- **无 remote**(LICENSE 与作者身份确认前不创建)

## 模板文件就绪(待负责人填入)

- CITATION.cff:authors 字段待填
- paper-emse-final.tex:\author{} 与 \institute{} 待填
- LICENSE-NOTE.md:待替换为正式 LICENSE
- Declarations 段:Data/Code availability 待定稿
