# 验证暂停点 / 交接记录

日期：2026-10-19（UTC）
状态：**真实运行 A、B 均已完成并落盘；离线回归 205 项通过；最终逐条核对报告已完成。** 最终报告见 `examples/live/validation/REPORT.md`。

## 已完成的运行

| 运行 | 资料库 | 停止原因 | 轮次 | 证据 | 结论 | 缺口 | 搜索/网页 | 模型调用 |
| --- | --- | --- | ---: | ---: | ---: | ---: | --- | --- |
| `runA`（空库起步） | `kb-empty.sqlite3`（起始为空） | `round_limit` | 10 | 63 | 86 | 16（全开放） | 8 搜索 / 33 页 | 41（含 2 次校正） |
| `runB`（复用已有库） | 同上（A 运行后已有 28 来源） | `round_limit` | 10 | 66 | 100 | 8（1 已关闭，7 开放） | 4 搜索 / 15 页 | 45（5 恢复） |

- A 产物：`examples/live/validation/runA/research-d968652bc210-e1dl242r/`
- B 产物：`examples/live/validation/runB/research-7ee761cd91fd-wvgpainm/`
- 两轮 `state.json` 均通过 `ResearchState` 校验，`report.md`、`result.json`、`trace.jsonl` 齐全。
- 复用证据：B 的 10 轮中有 7 轮 coverage 直接判定资料足够、不发起搜索；搜索 4 次、网页 15 页，明显少于空库 A 的 8 次/33 页。B 的 PDF 正文来自 A 已入库资料，未重复抓取。
- PDF：A 实际抓取并提取两份官方 Copilot Studio Licensing Guide（20/21 页，41k/39k 字符），`§PDF page N§` 标记已进入来源文本。
- 合并/防重复：A 合并 1 个重复缺口；B 合并 9 个同义缺口（含 topic 相同但措辞不同的情况）。
- 比较平衡：B 触发 3 次 `plan_guard_rejected`、2 次 `plan_guard_overridden`；最终缺口推进覆盖到双方，但守卫被模型无视 2 次，说明提示词约束仍需人工复核。
- 部分无效引用：A 丢弃 14 条、B 丢弃 15 条非逐字摘录，合法摘录仍进入证据链，未因此中止整个研究。

## 已完成的代码/测试修改

- 网页读取器支持文本型 PDF（pypdf），带页标记和明确的扫描件/损坏 PDF 错误；HTML 标题保留为 `§标题§`。
- 来源权威分级：`vendor_official` / `vendor_community` / `third_party` / `research_material` / `demo`；`learn.microsoft.com/answers` 归为社区。
- 要求官方/正式/PDF 的缺口不能仅凭社区、第三方或 HTML 证据关闭。
- 检索片段和证据携带前后文，降低产品/许可条件错配。
- 同一缺口按稳定 `topic` 或文本相似度合并；`--gap-attempts` 防止一个缺口吞掉全部轮次。
- 比较型目标按双方 questions+evidence+claims 覆盖量做 2 倍失衡检查（一次校正，再次违规则记录并继续）。
- 部分无效摘录只丢弃无效项；全部无效才进入校正/失败。
- 后续轮可引用此前已校验 evidence（`prior_evidence`）。
- 模型输出的 Claim 标签与引用矛盾时做保守归一（supported+仅反证→contradicted/mixed；无引用 fact→hypothesis/unverified；hypothesis 强制 unverified），写入 `claim_normalized`。
- CLI 对 SIGTERM/SIGINT 做任务取消，写出 `cancelled` 终态并保留 143/130 退出码；有子进程测试。
- 回归：`env -u PYTHONPATH .venv/bin/python -m pytest -q -p no:cacheprovider` → **205 passed**。
- 数量审计：新增 `claim_number_not_in_citation` 事件，标记金额/百分比/千分位数字未被所引摘录覆盖的情况。
- 修改文件：`enterprise_agent/{engine,schema,rag,settings,cli,ui}.py`、`providers/deepseek.py`、`tools/web_reader.py`、`pyproject.toml`、`requirements.lock`、`README.md`、新增/修改 `tests/`。

## 中断诊断（原复杂案例 `research-4e48c9658442-_grcm5xa`）

- trace：232 个事件，07:35:39–07:38:46 UTC；最后事件是第 5 轮 `model_start`（Assessment），此前 `extract` 已保存 27 证据/31 结论。
- 无 `run_error`、无 `timeout`、无 `run_end`、无 `result.json`；state.json 停在 extract 检查点。
- 该次上限：6 轮/6 搜索/16 页/32 模型调用/900 秒。实际约 187 秒、5 轮、4 搜索、14 页、22 次模型调用，均未触顶。
- 退出码 143 = SIGTERM。结论：**进程在 Assessment 的同步/异步 HTTP 等待期间被外部 SIGTERM 终止；发送者无法从现有记录确认**（不是已证实的超时或预算停止）。旧代码没有 SIGTERM 处理，默认终止绕过 `finally`，因此没有终态文件；现已修复并有离线子进程测试。

## 独立补查（重要缺口）

- 已独立抓取并检索官方 Microsoft Learn 的：
  - `microsoft-copilot-studio/guidance/plan-agent-throughput-rate-limits`
  - `microsoft-copilot-studio/troubleshoot-throttling-errors-agents`
  - `microsoft-copilot-studio/requirements-quotas`
- 结果：官方有按环境/付费档位的 RPM/RPH 配额与节流说明；许可指南仅写 “Usage is limited to fair usage limits… 保留更新权”，**没有公开 fair usage 的具体数值或触发阈值**。因此相关开放缺口是真实资料缺口，不是未尝试获取。
- 未遇到登录墙；Scribd 等第三方页面有访问限制，未作为证据。

## 已完成（恢复后）

1. 逐条核对 A/B 的关键结论与原始引文，细节见 `REPORT.md` 第 7 节；已标记：
   - A `c1_5` 的官方归因过度；
   - A `c1_3`/`c2_4`/`c2_5`/`c5_6`、B `c1_3`/`c8_3`/`c8_4`/`c9_9` 的“数字存在于原文、未被所引摘录覆盖”；
   - 社区来源均标注为社区；未发现把社区证据写成官方的事实结论；
   - 未发现把定价直接当收入或利润。
2. 最终验收报告已写入 `examples/live/validation/REPORT.md`。
3. 已清理临时 PDF 和失败运行的归档数据库；保留 `runA/`、`runB/`、失败运行目录、`usage-summary.json`。

## API 消耗快照

`examples/live/validation/usage-summary.json` 已更新，包含全部历史与验证 trace。汇总（含失败尝试，不含手工小测试）：

- DeepSeek：输入约 2,009,558 tokens，输出约 220,413 tokens。
- Embedding：约 371,897 tokens；Reranker：约 930,455 tokens。
- Tavily：42 credits；网页读取：160 次；PDF 提取：61 页。

最终 A+B 两次研究本身：DeepSeek 输入 920,891 / 输出 86,980 tokens；Embedding 110,157 tokens；Reranker 323,797 tokens；Tavily 12 credits；网页 48 次。
