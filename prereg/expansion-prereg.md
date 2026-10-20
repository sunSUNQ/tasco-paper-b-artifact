# TASCO-R5-P2-EXPANSION-R1 — 预注册(Step 0,FROZEN at write,先于任何模型调用)

## 1. 计量审计结论(基于 R5 10 对冻结证据)

| 项 | 定义(本轮冻结) |
|---|---|
| **Input(主指标)** | 非缓存输入 Token(api_reported,step_finish 求和;**不含** cache_read) |
| Cache read | 单列,不入主指标 |
| Flow 总量 | input+output+reasoning+cache_read(**次指标**;已知随会话长度/轮数增长) |
| 恢复读取 | 属标准 API 调用,其 Token 已含于所在 run 的 Token 统计;另记录次数/目标/输出字符/所在 step(归因近似,如实标注) |
| Marker/恢复/补偿链 | VIEW-STORED marker 数、.r5-store 文件数与字节、恢复读取次数与字符、恢复后工具调用序列 |
| 零暴露 case 波动 | R5 10 对已证:N-MOD02(markers=0)flow 摆动 2×;N-MOD03 +14.5%;N-XS −49.6% —— **方差基线与 P2 无关,不得归因机制** |
| 口径方向一致性 | R5 10 对中 input 与 flow 异号 4/10(cache 随轮数效应)—— 本轮以 Input 为主判据,Flow 仅作成本核对 |

## 2. 收益定义(冻结)

- 臂内聚合:每 case 每臂先对 2 次重复取均值(arm_mean_input);
- **InputBenefit(case) = (arm_mean_B − arm_mean_T) / arm_mean_B**;
- case 级配对统计(case 等权;**60 次重复观察不作为 60 个独立任务**);
- 稳健统计:median、win/loss/tie(>±1%)、case 级 Bootstrap 95% CI(10,000 次)、
  剔除最大单 case 的敏感性;
- 主指标未达 5% 工程目标时,按族/层/暴露分层寻找受限正收益子群(不全局外推)。

## 3. 样本(冻结,30 全新 case,与 R5 10 对及历史 case 不重叠)

分层变量(运行前可计算,非运行时标签):**predicted_view_volume** = case 作用域内
≥4K 字符文件的总字符数(文件审查=目标文件;模块分析=模块目录;TDD/跨规格=相关文件集)。

| 层 | 判定 | n |
|---|---|---:|
| 高暴露 | predicted_view_volume ≥ 20,000 chars | 12 |
| 普通暴露 | 4,000–20,000 | 12 |
| 低/无暴露 | < 4,000 | 6 |

层用于诊断分层,**不作运行时门控输入**。

## 4. 执行设计(冻结)

- 30 case × {B, T} × 2 reps = **120 run 上限**;分两批(10 case/40 run 质量门 → 20 case/80 run)
- 顺序:case 级种子乱序 × AB/BA 臂序平衡;每 run 全新仓库副本
- 模型:opencode + 火山AI网关/glm-5.3-flash;T 臂注入 view-store 插件(MIN_CHARS=4000,
  HEAD/TAIL=20,诊断行保留,side-store 无损)
- 重试:仅基础设施失败 ≤2 次/单元,留痕
- 超时:20 min/run

## 5. 质量门(第一批后检查,任一失败 ⇒ HOLD)

模型身份 40/40;Token 三项非零;side-store 文件 sha 与 marker 一致;恢复链完整
(marker→store 路径→恢复读取);无跨 case 状态泄漏(工作目录隔离);oracle 可执行。

## 6. 停止规则(冻结)

内容丢失/错误恢复/跨 case 混淆/计量不可信/机制性正确性问题 ⇒ 立即 HOLD。
基础设施失败率 >20% ⇒ HALT。不扩大预算,不中途调参。

## 7. 判定预注册(Step 5)

- **P2_READY_FOR_POWERED_AB**:case 等权平均 InputBenefit ≥ +5%,median ≥ 0,
  正收益不依赖单 case,无 P2 可归因正确性回归,恢复链完整,低暴露层无系统性开销
- **P2_SCOPE_RESTRICTED_CANDIDATE**:平均未达 5% 但存在稳健正收益子群(层/族/暴露),
  建议限定范围验证
- **P2_REFINE_REQUIRED**:方向为正但暴露/补偿结构需再调
- **P2_NEGATIVE**:稳健负收益
- **HOLD**:证据/安全问题
- Flow 五问(离群归因)必须作答;不做样本删除
- 5% 为工程晋级目标,非统计显著性证明
