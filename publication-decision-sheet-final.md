# 发布审批材料终态(publication-decision-sheet 终态)— Paper B GitHub

> ## 终态:**PUBLICATION_OWNER_ACTION_REQUIRED**

(本地候选包技术就绪——39 项复现校验全 PASS;**但 5 项阻塞决策(D1–D5)须由负责人完成后方可公开发布**。不自动投稿、不自动创建远程仓库、不自动选择 LICENSE。)

## 阻塞决策链(按依赖顺序)

```
D1 venue 确认(EMSE 或其他)
  └→ D2 作者信息填入
      └→ D3 Data Availability 定稿
          └→ D4 Code Availability 定稿
              └→ D5 LICENSE 选定
                  └→ 可创建远程仓库 + push
```

## 非阻塞但建议完成

| 项 | 说明 |
|---|---|
| D6 HF 语料许可核验 | 影响 data/THIRD-PARTY.md 措辞 |
| D7 Springer 模板确认 | 影响投稿包是否含模板文件 |
| D8 轨迹全量扫描 | 影响是否加入 trajectories/ |
| D9 G5 人工审核 | 影响论文 Limitations 声明强度 |

## 技术就绪度(已验证,无需重做)

| 项 | 状态 |
|---|---|
| 复现验证 | 39 PASS / 0 FAIL / 4 UNAVAILABLE |
| manifest | 130 条,0 mismatch |
| 隔离测试 | exit 0 |
| 安全扫描 | 凭据 0 泄漏;隐私 0 风险 |
| 论文编译 | 12 页,0 undefined,0 error |
| 图表 | 7 张彩色矢量图 + 4 表 |
| Supplement | ESM_1.pdf 5 页 |
| 底部收尾条 | 图 1 已闭合(4 条全宽边框) |

## 候选包完整性

129 文件(含 5 份发布审批报告);manifest.sha256 覆盖 100%;冻结证据零改动。

完成后 **STOP**,等待负责人完成 D1–D5 决策。
