# 交付物 6 — P2 诊断保护合约符合性审计(G5-DIAGNOSTIC-RISK-ROOTCAUSE-R1)

机器可读版:`rc-step2-contract-audit.json`(含最小复现)。

## 1. 合约与实现的口径对照

| 来源 | 冻结文本 | 口径 |
|---|---|---|
| `r5/online/online-protocol.md`(FROZEN,P2 合约)| "上下文保留 head 20 行 + tail 20 行 + **全部诊断行(逐字)** + 指针 marker;完整原文写入 `<workdir>/.r5-store/<sha16>.txt`(**无损**,可按需 read 恢复)" | **语义**:"全部诊断行"未作操作性定义 |
| `r5/expansion/prereg.md` | "MIN_CHARS=4000,HEAD/TAIL=20,**诊断行保留**,side-store 无损" | 语义(同上) |
| `r5/online/view-store-plugin-template.js`(冻结实现)| `DIAG = /(fail|error|assert|traceback|exception|fatal|denied|not found)/i`;HEAD/TAIL=20(**原始工具输出行号**) | **词面**(8 关键词) |
| `REVIEWER-SHEET.md`(G5 标准)| E1: "a diagnostic line … missing in-context"(示例: error/assert/traceback/exception/fatal) | 语义倾向("appears to be") |
| 论文 M3 句(laTeX §3)| "head (20) and tail (20) windows, **all diagnostic lines verbatim**, and a pointer marker" | 语义读法下作承诺 |

## 2. 逐项符合性

| 合约条款 | 实现行为 | 判定 |
|---|---|---|
| head 20 + tail 20 | 保留(按原始输出行号;内容行 1–17 与 196/197–213)| 符合(但坐标系缺陷见 §3) |
| **全部诊断行(逐字)** | DIAG 8 关键词行 100% 保留(机械 30/30);**不含关键词的语义诊断行不保留**:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`(3 文件 × 4 行) | **语义口径下不符合;词面口径下符合** —— 合约-实现覆盖缺口确认 |
| 指针 marker | 存在;sha16 与 store 一致(30/30);可按需完整恢复 | 符合(恢复完整性 INTACT) |
| side-store 无损 | store == 仓库源文件逐行一致(V1 30/30);sha16 校验一致 | **符合(字节级恢复完整性成立)** |
| 可审计 marker(论文部署合约)| marker 行号用原始输出坐标系,与视图显示的内容坐标系错位 3 行 ⇒ 读者核对得出"18–20 无去向" | **不符合(歧义缺陷;E3 根因)** |
| fail-closed | 插件 try/catch,异常时返回原输出(代码审阅;无反例) | 符合 |

## 3. 触发位置 / 输入输出 / 最小复现

- **触发代码**:`view-store-plugin-template.js` L10(`DIAG` 词表)、L30–33(`diagMid` 仅收 DIAG 行)、
  L36(marker 用 `HEAD+1..n-TAIL` **原始行号** —— 坐标系缺陷点)、L41(折叠装配)。
- **输入**:≥4000 字符 read 输出;含 `} catch (error) {`(词面命中)与
  `return { ok: false, reason: "exhausted_retries" ... }`(词面不命中)各一,均处于中段。
- **实际输出**:catch 行进入 "critical lines retained verbatim" 块;ER 失败返回被静默省略
  (仅存 side-store)。
- **最小复现**(`rc-step2-contract-audit.json` → `minimal_reproduction`,离线纯函数,无模型调用):
  14,871 字符合成输入 → catch 行保留 = true;失败返回保留 = **false**;critical 块含 catch = true、
  含失败返回 = false。

## 4. 裁定

1. **合约覆盖缺口确认**:"全部诊断行"的自然语义读法覆盖 ER 失败返回;冻结实现按 8 关键词词面
   执行,语义诊断行 12 条唯一(120 视图实例)未被直接呈现。实现忠实于其自身词表,缺陷在
   **合约-实现口径差**,不在实现内部一致性。
2. **marker 坐标系缺陷确认**:违反"auditable markers"的实质(可审计性以读者可核对为前提)。
3. **字节恢复完整性确认无损**:side-store == 源文件 30/30,sha 全一致,恢复路径完整。
   ——必须与 §第 1/2 条严格区分:**字节无损 ≠ 即时诊断可见**。
4. **禁止事后改标准**:把"诊断行"追溯定义成 8 关键词词表以使本轮通过 = 事后改标准,禁止。
   合法路径:新冻结修订(插件 v2:扩充词表/结构化失败返回检测 + marker 双坐标系行号)+
   新证据轮;或由研究负责人显式重界定合约(须留痕,见交付物 8)。
