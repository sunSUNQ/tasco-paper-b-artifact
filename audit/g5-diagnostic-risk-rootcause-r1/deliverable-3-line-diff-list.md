# 交付物 3 — 30 样卷逐行差异清单

每卷给出:C 中保留的内容行标签集合、marker 声明省略范围(原始行号/内容行号)、声明省略区间内未被保留的语义诊断行(逐字)、恢复路径。三 run 的差异结构同型,逐卷列出。

## S01(run `a302a9c1`,marker `5166823c3001d5b3`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/5166823c3001d5b3.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S02(run `a302a9c1`,marker `5166823c3001d5b3`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/5166823c3001d5b3.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S03(run `a302a9c1`,marker `5166823c3001d5b3`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/5166823c3001d5b3.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S04(run `a302a9c1`,marker `5166823c3001d5b3`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/5166823c3001d5b3.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S05(run `a302a9c1`,marker `5166823c3001d5b3`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/5166823c3001d5b3.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S06(run `a302a9c1`,marker `5166823c3001d5b3`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/5166823c3001d5b3.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S07(run `a302a9c1`,marker `5166823c3001d5b3`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/5166823c3001d5b3.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S08(run `a302a9c1`,marker `5166823c3001d5b3`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/5166823c3001d5b3.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S09(run `a302a9c1`,marker `5166823c3001d5b3`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/5166823c3001d5b3.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S10(run `a302a9c1`,marker `5166823c3001d5b3`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/5166823c3001d5b3.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S11(run `ce499899`,marker `0f7965aed9ab2c13`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/0f7965aed9ab2c13.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S12(run `ce499899`,marker `0f7965aed9ab2c13`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/0f7965aed9ab2c13.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S13(run `ce499899`,marker `0f7965aed9ab2c13`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/0f7965aed9ab2c13.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S14(run `ce499899`,marker `0f7965aed9ab2c13`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/0f7965aed9ab2c13.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S15(run `ce499899`,marker `0f7965aed9ab2c13`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/0f7965aed9ab2c13.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S16(run `ce499899`,marker `0f7965aed9ab2c13`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/0f7965aed9ab2c13.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S17(run `ce499899`,marker `0f7965aed9ab2c13`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/0f7965aed9ab2c13.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S18(run `ce499899`,marker `0f7965aed9ab2c13`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/0f7965aed9ab2c13.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S19(run `ce499899`,marker `0f7965aed9ab2c13`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/0f7965aed9ab2c13.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S20(run `ce499899`,marker `0f7965aed9ab2c13`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/0f7965aed9ab2c13.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S21(run `ce499899`,marker `0f7965aed9ab2c13`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/0f7965aed9ab2c13.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S22(run `ce499899`,marker `0f7965aed9ab2c13`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/0f7965aed9ab2c13.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S23(run `ce499899`,marker `0f7965aed9ab2c13`)

- 保留:head 内容行 1–17;critical 23 行(标签 26–186);tail 内容行 196–212 + 结尾 envelope
- marker 声明省略:原始行 21..198 = 内容行 18..195(envelope 偏移 3);声明省略行数 178,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 55:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 100:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 145:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 190:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/0f7965aed9ab2c13.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S24(run `2e2bda50`,marker `bd911b6f26b1d421`)

- 保留:head 内容行 1–17;critical 23 行(标签 27–187);tail 内容行 197–213 + 结尾 envelope
- marker 声明省略:原始行 21..199 = 内容行 18..196(envelope 偏移 3);声明省略行数 179,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 56:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 101:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 146:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 191:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/bd911b6f26b1d421.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S25(run `2e2bda50`,marker `bd911b6f26b1d421`)

- 保留:head 内容行 1–17;critical 23 行(标签 27–187);tail 内容行 197–213 + 结尾 envelope
- marker 声明省略:原始行 21..199 = 内容行 18..196(envelope 偏移 3);声明省略行数 179,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 56:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 101:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 146:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 191:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/bd911b6f26b1d421.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S26(run `2e2bda50`,marker `bd911b6f26b1d421`)

- 保留:head 内容行 1–17;critical 23 行(标签 27–187);tail 内容行 197–213 + 结尾 envelope
- marker 声明省略:原始行 21..199 = 内容行 18..196(envelope 偏移 3);声明省略行数 179,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 56:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 101:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 146:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 191:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/bd911b6f26b1d421.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S27(run `2e2bda50`,marker `bd911b6f26b1d421`)

- 保留:head 内容行 1–17;critical 23 行(标签 27–187);tail 内容行 197–213 + 结尾 envelope
- marker 声明省略:原始行 21..199 = 内容行 18..196(envelope 偏移 3);声明省略行数 179,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 56:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 101:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 146:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 191:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/bd911b6f26b1d421.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S28(run `2e2bda50`,marker `bd911b6f26b1d421`)

- 保留:head 内容行 1–17;critical 23 行(标签 27–187);tail 内容行 197–213 + 结尾 envelope
- marker 声明省略:原始行 21..199 = 内容行 18..196(envelope 偏移 3);声明省略行数 179,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 56:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 101:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 146:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 191:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/bd911b6f26b1d421.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S29(run `2e2bda50`,marker `bd911b6f26b1d421`)

- 保留:head 内容行 1–17;critical 23 行(标签 27–187);tail 内容行 197–213 + 结尾 envelope
- marker 声明省略:原始行 21..199 = 内容行 18..196(envelope 偏移 3);声明省略行数 179,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 56:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 101:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 146:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 191:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/bd911b6f26b1d421.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)

## S30(run `2e2bda50`,marker `bd911b6f26b1d421`)

- 保留:head 内容行 1–17;critical 23 行(标签 27–187);tail 内容行 197–213 + 结尾 envelope
- marker 声明省略:原始行 21..199 = 内容行 18..196(envelope 偏移 3);声明省略行数 179,其中 critical 保留 23 行
- **未被保留的语义诊断行(4 行/卷,仅存于 side-store)**:
  - 内容行 56:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 101:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 146:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
  - 内容行 191:`return { ok: false, reason: "exhausted_retries", attempts: attempt };`
- 其余 broad 探针命中(非诊断,系探针关键词 timeout 误报):8 行/卷
- 恢复路径:store 文件存在=True,sha16 一致=True(agent 可经 `.r5-store/bd911b6f26b1d421.txt` 完整恢复;原实验中 123 次恢复读均为整卷回灌)
