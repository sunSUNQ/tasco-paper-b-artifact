# GitHub Release Checklist — Paper B Artifact

发布前逐项确认。全部打勾后方可 push。

## 前置决策(负责人完成)

- [ ] D1 投稿 venue 已确认(决定匿名格式)
- [ ] D2 作者信息已填入 paper-emse-final.tex 标题页
- [ ] D3 Data Availability 声明已定稿
- [ ] D4 Code Availability 声明已定稿
- [ ] D5 LICENSE 文件已添加(如 MIT/Apache-2.0)
- [ ] D6 HF 语料许可已核验并在 THIRD-PARTY.md 中更新

## 技术检查(自动可验证)

- [ ] `python -m reproduction.verify` 输出 39 PASS / 0 FAIL / 4 UNAVAILABLE
- [ ] manifest.sha256 覆盖全部文件(排除 .gitignore 中的排除项),0 mismatch
- [ ] .gitignore 正确排除:trajectories/*.jsonl、.env、*.key、__pycache__、*.aux、*.log、*.out
- [ ] paper/paper-emse-final.pdf 与 paper-emse-final.tex 对应(同版本编译)
- [ ] ESM_1.pdf 为最新 supplement 版本
- [ ] figures/ 7 张图与正文引用一致(f0 或 fig1-final + f1–f6)
- [ ] 无 .git 目录
- [ ] 无 __pycache__
- [ ] 无 .env
- [ ] 无 mapping.json(G5 封存映射)
- [ ] 无原始 events.jsonl(424 run)

## 内容检查(人工)

- [ ] README 复现指南三步内可达(环境→数据→重跑)
- [ ] 论文每条主结论在 README 中有对应的包内文件引用
- [ ] G5 诊断案例声明"model-assisted; human review pending"
- [ ] 无"首次/唯一/最佳"等未经比较的排他性措辞
- [ ] 无内部绝对路径 `research-semantic-compression` 或 `C:\Users\sunqinghw` 泄漏(verify.py 层面已确认;数据文件中的冻结记录路径属数据属性)
- [ ] F1/F2/F3 失败机制表述为"mechanism interpretation supported by trajectories",非"proven causal"

## 最终确认(负责人签署)

- [ ] 我已审阅 GitHub 候选包全部 129 个文件
- [ ] 我确认所有数据/代码可按所选 LICENSE 公开
- [ ] 我确认论文结论与包内数据一致
- [ ] 我授权创建远程仓库并 push(或指定他人执行)

签署人:____________ 日期:____________
