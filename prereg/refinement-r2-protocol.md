# TASCO-R4 REFINEMENT-R2 — 离线资格校准协议(OFFLINE-FIRST,FROZEN at write)

## 阶段定义

- **A 离线校准**:解析冻结 100-Case B 臂轨迹 → 候选折叠事件表;70/30 族分层划分
  (seed 20261017);参数网格 R×D×M 离线回放;校准集选 ≤3 候选点。
- **B 资格验收**:保留集(30 case,未参与调参)独立验收。GO 门槛:①高价值内容误折叠
  = 0(并完整审计全部实际候选);②≥1/3 保留 case 产生安全折叠候选;③预计上下文
  Token 减少占比 ≥ ~2%;④门控特征全部运行时可得;⑤参数邻域稳定;⑥锚点/恢复/回退/
  安全测试全过。任一不满足 ⇒ OFFLINE_NO_SAFE_MEASURABLE_EXPOSURE + STOP。
- **C 条件式 30 对在线验证**:仅 B 通过后执行;全新 30 case(不与 100-Case/R1 重叠);
  主指标 = Input Token 配对收益;不得作为正式统计显著性结论。

## A3 安全约束(门控设计,先于数据可见冻结)

1. 重复次数不单独构成折叠理由;
2. read 内容默认保护(目标文件与规格/文档读取绝对保护;仅 100% 重复且 marker 可恢复的
   再交付按参数进入候选);
3. 含诊断(Traceback/ERROR/error)的输出一律不折叠(E7-unsafe 保护);
4. 非 read 输出须 ≥最小字符且重复率达标(噪声型),内容型(低重复)不折叠;
5. 门控跳过采用时仍调用原语完成锚点注册(v2 语义);
6. 不使用 benchmark 任务族标签;特征仅限运行时可得(工具名/路径/会话内计数/内容统计)。

## 网格(冻结)

R ∈ {2,3,4,never}(read 第 N 次交付起可折叠)× D ∈ {0,0.2,0.3,0.4}(非 read 重复率阈值)
× M ∈ {0,500,1000,2000}(最小字符)= 64 组合;全部标注 opportunity proxy。

## 判定口径(三选一)

OFFLINE_NO_SAFE_MEASURABLE_EXPOSURE / R2_DIAGNOSTIC_COMPLETE_GO_FORMAL_CANDIDATE /
R2_DIAGNOSTIC_COMPLETE_REFINE_AGAIN
