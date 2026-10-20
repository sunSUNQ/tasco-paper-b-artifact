# Publication Allowlist — Paper B GitHub Candidate

以下文件已通过安全扫描与复现验证,确认可进入公开 GitHub 仓库。

## 允许列表(白名单;每条已通过 41 项校验中的对应检查)

| 路径 | 依据 |
|---|---|
| README.md | 静态文档,无凭据 |
| .gitignore | 排除规则 |
| LICENSE-NOTE.md | 占位声明 |
| paper/paper-emse-final.pdf | 论文终稿 |
| paper/paper-emse-final.tex | 论文源码(无凭据/无内部路径) |
| paper/refs.bib | 已验证文献 |
| paper/ESM_1.pdf | 补充材料 |
| paper/figures/*.pdf ×7 | 彩色矢量图 |
| prereg/*.md + *.json ×6 | 预注册文档 |
| data/*.jsonl + *.json + *.md ×24 | 冻结逐 case 配对数据与冻结分析 |
| mechanisms/*.js + rds-impl/*.js ×8 | 冻结机制源码(已披露缺陷含注记) |
| analysis/*.py ×8 | 论文重算脚本(溯源记录) |
| audit/g5-blind-package/** ×34 | G5 盲审样卷+预检 |
| audit/g5-dual-model-audit-r1/** ×15 | G5 双模型审计 |
| audit/g5-diagnostic-risk-rootcause-r1/** ×19 | G5 根因审计 |
| reproduction/verify.py + __init__.py | 39 项 R1/R2 校验 |
| trajectories/READ-ME-FIRST.md | 发布政策(不含轨迹) |
| manifest.sha256 | 哈希清单 |
| github-export-inventory.md | 导出清单 |
| security-and-license-review.md | 安全审查 |
| reproduction-validation.md | 复现验证报告 |
| pending-owner-decisions.md | 待决策清单 |

## 排除列表(黑名单;已通过 .gitignore + 文件审计确认)

| 排除项 | 原因 |
|---|---|
| mapping.json(G5 封存映射) | C 类 |
| events.jsonl / workdir(424 run) | C 类(待全量扫描) |
| .env / *.key / credentials/ | 凭据 |
| *.log / *.aux / *.out / *.blg | 编译产物 |
| __pycache__/ | 缓存 |
| D3 语料原始轨迹 | C 类(第三方 HF 许可) |
| 旧版论文稿(v1/v2/final2) | 被取代 |
