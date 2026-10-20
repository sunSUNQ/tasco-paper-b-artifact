# 安全与许可审查 — Paper B GitHub Candidate (2026-10-20)

## 凭据扫描

| 模式 | 命中 | 判定 |
|---|---|---|
| sk- API key | 0 | clean |
| Bearer token | 0 | clean |
| api_key/apiKey | 0 | clean |
| ANTHROPIC_AUTH_TOKEN | 2(均为审计文档描述文字,非值) | ✓ 不构成泄漏 |
| 网关 key 0f837e1d | 0 | clean |
| password | 0 | clean |

## 内部路径

- `research-semantic-compression`: ~4028 处,**全部在 analysis/ 溯源脚本中**——这些脚本引用内部绝对路径是设计如此(provenance record),verify.py 不依赖它们。
- `C:\Users\sunqinghw`: 22 处,全部在冻结数据 JSONL 中(run 工作目录记录)——数据属性,非活动依赖。
- **verify.py 零内部路径引用** ✓。

## 隐私

- 原始轨迹(events.jsonl)不在包内 ✓
- 个人身份信息:无 ✓
- G5 封存映射:不在包内 ✓

## 第三方许可

| 依赖 | 许可 | 状态 |
|---|---|---|
| HF Thoughtworks/OSW-Traces 语料 | 页面不可达待核验 | B 类 |
| opencode CLI | AGPL-3.0 | 仅引用,不重分发 |
| svjour3.cls / spbasic.bst | Springer LaTeX 模板 | 需单独确认再分发条款 |
| matplotlib / numpy | BSD/MIT | 开源,无障碍 |

## Git 元数据

- 无 .git 目录 ✓
- 无 git 历史 ✓
- 无符号链接 ✓
- 无隐藏文件 ✓

## 结论

- 凭据零泄漏 ✓
- 隐私无风险 ✓
- 内部路径:溯源脚本已声明;verify.py 独立 ✓
- 第三方许可:HF 待核验(B 类);模板待确认(B 类)
- 无 HOLD 级安全问题
