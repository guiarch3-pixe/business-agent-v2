# V2 复杂案例验证与改进报告

日期：2026-10-19
范围：`.`
性质：真实 API 运行 + 离线回归；结论均为模型评估，不等于独立事实核验。

## 1. 结论摘要

- 原复杂案例第 5 轮中断可定位为：**进程在 Assessment 模型请求期间收到外部 SIGTERM**；现有记录不能确认发送者。该次运行约 187 秒、5/6 轮、4/6 搜索、14/16 页、22/32 模型调用，**没有触达超时或预算上限**，也未写出 `run_error`。退出码 143 与 SIGTERM 一致。
- 已修复导致“同一 PDF 反复追问”的实际能力缺口：网页读取器现在会真正下载并提取文本型 PDF；两份 Microsoft Copilot Studio Licensing Guide 实际提取了 20 页和 21 页，而不是再次搜索。
- 已修复研究质量机制：来源权威分级、片段上下文、重复 Gap 合并、缺口尝试上限、比较目标覆盖平衡、部分无效摘录丢弃、后续轮引用此前证据、Claim 标签与引用一致性归一、SIGTERM 优雅落盘。
- 真实运行 A（空库起步）：10 轮、63 条证据、86 条结论、16 个开放缺口；8 次搜索、33 次网页读取、两份官方 PDF。
- 真实运行 B（复用 A 的资料库）：10 轮、66 条证据、100 条结论、8 个缺口（1 个关闭、7 个开放）；仅 4 次搜索、15 次网页读取，10 轮中 7 轮直接复用已有资料、不发起搜索。
- 离线回归：**205 项全部通过**。
- 质量判断不以轮数、结论数量或“关闭全部 Gap”为依据。两次运行都停在 `round_limit`，并保留了未解决缺口；B 只关闭了 1 个有官方原文支撑的缺口。

## 2. 中断诊断（原案例 `research-4e48c9658442-_grcm5xa`）

证据：

| 项目 | 观察 |
| --- | --- |
| trace | 232 个事件，2026-10-19 07:35:39–07:38:46 UTC |
| 最后事件 | `model_start`（Assessment，第 5 轮），此前 `extract` 已提交 27 证据/31 结论 |
| 终态文件 | 无 `result.json`、无 `report.md`、无 `run_end`、无 `run_error` |
| 运行上限 | 6 轮、6 搜索、16 页、32 模型调用、900 秒 |
| 实际消耗 | 约 187 秒、5 轮、4 搜索、14 页、22 次模型调用 |
| 退出码 | 143 = 128 + SIGTERM |

判断：

- **可以确认**：进程在 Assessment 请求进行中终止；没有触发引擎的超时、预算或错误处理；旧版本没有 SIGTERM 处理器，Python 默认动作会立即终止并绕过 `finally`，因此只有最后一个检查点而没有终态文件。
- **无法确认**：谁发送了 SIGTERM（调用方、终端/会话管理器或其他外部监督进程）。现有日志不足以归因，不能写成“已经证实是超时”。
- **已修复**：CLI 将 SIGTERM/SIGINT 转为异步任务取消；引擎写出 `cancelled` 的 `state.json`/`report.md`/`result.json`，CLI 分别以 143/130 退出。离线子进程测试 `tests/test_v2_signals.py` 验证了 SIGTERM 下终态文件存在。

## 3. 研究质量问题与修复对照

| 观察到的现象 | 根因 | 修复 | 离线验证 |
| --- | --- | --- | --- |
| 同一许可指南 PDF 被反复追问 | 读取器只接受 HTML/纯文本；PDF 返回 `unsupported_content_type`，模型只能继续搜索并换措辞新建 Gap | `WebPageReader` 支持文本型 PDF，带 `§PDF page N§` 页标记；不支持 OCR 时返回明确错误 | `test_pdf_text_is_extracted_with_page_provenance`、真实 PDF 提取 20/21 页 |
| 重复 Gap | 只做精确描述去重 | 稳定 `topic` + 字符 n-gram 相似度合并；新结论并入原 Gap | `test_stable_topic_merges_reworded_gaps...`、`test_new_gap_is_merged...` |
| 一个缺口吞掉全部轮次 | 规划器反复选择同一高优先级缺口 | `--gap-attempts`（默认 2）；有其他未尝试缺口时必须切换 | `test_gap_attempt_cap...` |
| 比较两个产品逐渐偏向一个 | 没有覆盖量检查 | 按双方 questions+evidence+claims 统计；一方不足另一方一半且计划未涉及落后方时先校正 | `test_comparison_guard...` 两项 |
| 摘录丢失上下文，产品/条件错配 | 只用 600 字片段，HTML 标题被压平 | 片段前后各 220/180 字上下文；HTML 标题保留；证据携带 `source_title/authority` | `test_passages_carry...` |
| 社区回答被当作官方资料 | 只看域名，不看作者 | `Source.authority` 分级；`learn.microsoft.com/answers` 归 `vendor_community`；官方/PDF 缺口不能用社区或第三方证据关闭 | `test_authority...`、`test_official_pdf_gap...` |
| 缺少 PDF 正文时没有实际获取 | 读取器不支持 PDF | PDF 下载 + pypdf 提取 + 页标记；失败有结构化错误 | 同上 |
| 一条释义型引用杀死整轮 | 任一 quote 不匹配即整批失败 | 部分无效摘录记录并丢弃，合法摘录保留；全部无效才校正/失败 | `test_one_paraphrased_quote...` |
| 后续轮不能引用此前证据 | 引用被限制在本轮命中片段 | 允许引用 `prior_evidence`，但仍必须是真实已校验 ID | `test_assessment_may_cite...` |
| 大量 Claims 导致 `invalid_schema` 终止 | 模型把 supported/mixed/hypothesis 标签与引用写矛盾，恢复预算很快耗尽 | 解析前按引用保守归一；默认恢复次数 2→4；反馈列出 Claim 规则 | `test_model_assessment_labels...` |

## 4. 代码与配置修改

- `enterprise_agent/engine.py`
  - PDF/Gap 质量守卫、来源权威入 payload、上下文、Gap topic/相似度合并、尝试上限、比较平衡、部分摘录丢弃、`prior_evidence`、Claim 归一、数量审计、SIGTERM 相关目录记录。
- `enterprise_agent/schema.py`
  - `Source.authority`；`Gap.topic`/`GapProposal.topic`；`Assessment.normalize_payload` 保守标签归一。
- `enterprise_agent/rag.py`
  - 来源权威分类；HTML 文本清洗；默认片段 600/90（原 400/60）。
- `enterprise_agent/tools/web_reader.py`
  - PDF 内容类型/魔数识别、页标记、最大页数、加密/损坏/无文本错误；标题标记。
- `enterprise_agent/providers/deepseek.py`
  - 在严格 Pydantic 校验前调用 `normalize_payload`（仅实现该钩子的 schema）。
- `enterprise_agent/cli.py`
  - `--gap-attempts`；SIGTERM/SIGINT 转任务取消，保留 143/130 退出码。
- `enterprise_agent/settings.py`
  - `gap_attempts`；恢复调用默认 4。
- `enterprise_agent/ui.py`
  - 暴露缺口尝试轮次。
- `pyproject.toml` / `requirements.lock`
  - 增加 `pypdf`。
- `README.md`
  - PDF、权威分级、Gap 合并、比较平衡、Claim 归一、数量审计、SIGTERM 行为说明。
- 测试新增/修改
  - `tests/test_v2_quality_guards.py`、`tests/test_v2_signals.py`、`tests/test_web_reader.py`。

未修改 V1；未提交或推送代码；未展示、复制或写入 `.env` 密钥。

## 5. 测试结果

```bash
env -u PYTHONPATH .venv/bin/python -m pytest -q -p no:cacheprovider
```

结果：**205 passed**（最终版本）。

覆盖新增点：PDF 提取、权威分级、上下文、重复 Gap/topic 合并、尝试上限、比较平衡、官方/PDF 缺口关闭限制、部分无效引用、跨轮引用、Claim 标签归一、数量审计、SIGTERM 终态。

## 6. 真实运行指标

### 6.1 空库起步（运行 A）

- 目录：`examples/live/validation/runA/research-d968652bc210-e1dl242r/`
- 资料库：`examples/live/validation/kb-empty.sqlite3`（起始为空）
- 预算：10 轮 / 16 搜索 / 40 页 / 70 模型调用 / 300 Embedding / 30 Reranker / 1800 秒 / Gap 尝试 2 / 恢复 2
- 结果：`round_limit`，10 轮，63 证据，86 结论，16 缺口（全开放）
- 来源 28：官方 15、第三方 9、社区 4
- 搜索 8 次（8 credits），网页 33 次；PDF 提取 2 份，共 41 页
- 模型调用 41（含 2 次校正、1 次 invalid_schema 错误）
- Embedding 108 次 / 97,820 tokens；Reranker 17 次 / 174,776 tokens
- 无效摘录丢弃 14 条；Gap 合并 1 个；比较守卫未触发

### 6.2 复用已有资料库（运行 B）

- 目录：`examples/live/validation/runB/research-7ee761cd91fd-wvgpainm/`
- 资料库：同上（A 运行后已有 28 个来源）
- 预算：10 轮 / 16 搜索 / 40 页 / 70 模型调用 / 300 Embedding / 30 Reranker / 1800 秒 / Gap 尝试 2 / 恢复 6
- 结果：`round_limit`，10 轮，66 证据，100 结论，8 缺口（1 关闭、7 开放）
- 来源 21：官方 6、第三方 11、社区 4
- 搜索 4 次（4 credits），网页 15 次；10 轮中 7 轮 coverage 判定资料充足、未搜索；PDF 直接复用 A 的入库文本（0 次新 PDF 读取）
- 模型调用 45（5 次校正，0 次最终模型错误）
- Embedding 25 次 / 12,337 tokens；Reranker 14 次 / 149,021 tokens
- 无效摘录丢弃 15 条；Gap 合并 9 个；比较守卫拒绝 3 次、被模型无视并记录 2 次
- 关闭缺口 `gap2`：Copilot Studio User License 存在、官方标价 $0、与 Copilot Credits 的关系；4 条 resolution claim 均引用官方 PDF/Learn 原文。

### 6.3 复用效果

B 与 A 同样 10 轮，但：

- 搜索 8 → 4；网页 33 → 15；Embedding 调用 108 → 25；Embedding tokens 97,820 → 12,337。
- 说明已有资料库确实被检索复用，而不是每次都重新抓取；未复用部分通过 4 次补搜进入。

## 7. 关键结论逐条核对

核对方法：

1. 所有引用都通过代码的逐字匹配、来源哈希和分块范围校验。
2. 对 `deduction`、`business_judgment`、已关闭缺口的 resolution claims 逐条对照其引用原文。
3. 对金额、百分比、千分位数字做额外人工核对；新增代码事件 `claim_number_not_in_citation` 供后续自动标记。
4. 区分事实、推导、商业判断、假设；价格不被当作收入或利润。

### 7.1 核对通过的关键结论

| 结论 | 原文依据 | 判断 |
| --- | --- | --- |
| A `c1_1`：官方指南表把 Microsoft 365 Copilot 列为 $30/用户/月，含 Included agent usage、PAYG、25,000 Credits/包 | 官方许可指南 PDF 原表：`Microsoft 365 Copilot $30 per user/month Included agent usage1 ...` | 事实成立；脚注 1/2/3 的具体口径未被该摘录覆盖 |
| A `c1_2`：随 M365 Copilot 附带的 Copilot Studio 面向已许可用户、内部代理无额外费用；独立许可可发布到外部渠道并允许未获许可用户使用 | 官方定价页两段 FAQ 原文逐字匹配 | 事实成立，产品归属正确 |
| A `c2_3`：容量包按租户、1 包=25,000 Credits、$200/包/月（按年计费）、不结转、耗尽后才计入 PAYG | 官方 PDF 第 4 节三段连续原文 | 事实成立；价格仅标价，不是收入 |
| A `c6_9`：已校验官方摘录中没有分部收入、收入确认或席位/信用与财报科目的对应文字 | 官方 PDF/Learn 摘录 | 正确的否定性发现；未用价格填补收入缺口 |
| A 商业判断（`c3_8`、`c6_11`、`c8_9`、`c9_9`、`c10_8` 等） | 均引用官方条款 + 部分社区/第三方佐证 | 明确标注为判断，未量化金额，未把标价当收入/利润；结论中保留“若/可能”条件 |
| A 社区证据（`c3_7`、`c5_6`、`c10_4` 等） | `learn.microsoft.com/answers`、`techcommunity.microsoft.com` 回帖 | 文本明确写“社区帖/作者为社区用户/非厂商正式文档”，未冒充官方 |
| B 已关闭 `gap2`：Copilot Studio User License 存在、$0、代理运行消耗 Copilot Credits | 官方 PDF `A Copilot Studio User License ($0) is required...`；Learn `... (free of charge)`；官方 Credits/容量包原文 | 关闭依据成立；限制条件也写在 resolution_reason 中 |
| B `c8_6`：预付费档位 3,000 CCCU=$2,850（5%）至 3,000,000 CCCU=$2,400,000（20%），折算 95%–80% | 官方 PDF 档位表原文 + 算术 | 数字与算术均成立；属于推导而非新事实 |
| 价格/收入层级 | 所有 `business_judgment`/`hypothesis` 均写明不构成已实现收入或利润 | 未发现把定价直接当收入或利润的结论 |

### 7.2 发现的问题（保留在验收记录中，不掩盖）

| 结论 | 问题 | 影响 |
| --- | --- | --- |
| A `c1_5` | 写“官方称信用在租户层汇集而非按席位”；`rationale` 承认“租户汇集”来自第三方，官方只支持“按租户范围销售” | **语义过度归因**：引用本身真实，但把第三方措辞写成官方。已在评估提示中新增“不得把 third_party/community 的措辞写成官方称” |
| A `c1_3` | 25,000 Credits、Commit Units 出现在官方页面，但不在该结论引用的三条逐字摘录中（在页面其他段落/上下文） | **引用不完整**：数字真实，但当前 citation 不足以单独支撑该句 |
| A `c2_4` | 20,000/100,000/500,000 ACU 与 5%/10%/15% 折扣在官方 PDF 表格中，但不在所引两条摘录中 | 引用不完整；数字经原始来源核对为真 |
| A `c2_5` | “最高可节省 20%”在同一官方页面的相邻段落，未在所引摘录中 | 引用不完整 |
| A `c5_6` | “18 岁以上”在社区帖子原文中，但所引摘录在 “Busi...” 处截断，未包含该数字 | 引用不完整；来源性质已明确标为社区 |
| A `c7_5` | 商业判断提到“Business 版 300 席上限”，但引用均为官方清单；`rationale` 说明 300 来自第三方、仅作核对提示 | 作为“需核对”的提示可接受，但不是官方事实；不宜在摘要中单独引用 |
| B `c1_3` | “每 Credit 0.01 美元”在官方 PDF 源文本中，但不在所引 PAYG 模式摘录中 | 引用不完整 |
| B `c1_8` | 推导中的“租户集中池”来自第三方（CIAOPS）引用，官方只支持 Credits 计量和租户级销售；结论未逐句标注该来源 | **混合来源推导**：结论方向可成立，但“集中池”不应被读成官方措辞 |
| B `c8_3` | 档 3 文本出现排版混杂：“档3 30,000,000 中的 3,000,000 Credits”；后续档位数字未全部出现在所引摘录中 | 文本/引用质量问题；需以官方表格重新整理后才能作为正式事实引用 |
| B `c9_9` | 讨论第三方 “20.00 美元/包/月”时，引用的第三方摘录只列 2,400/2,520/240，未含 20.00 | 负面对比句的引用不完整；不影响“官方未确认 20.00”的判断 |
| B `c8_4` | 9 档折扣数字在官方 PDF 表格中，但所引摘录被截断，未展示全部档位 | 引用不完整；数字经源文本核对存在 |

这些问题说明：**代码能证明“摘录逐字来自原文”，不能证明“结论中的每个数字/主语都来自该摘录”**。本轮新增了 `claim_number_not_in_citation` 事件来暴露此类情况；它不拒绝结论，但会写入 trace 供人工复核。

### 7.3 社区与官方边界

- A 中直接引用社区事实的结论（`c3_7`、`c5_6`、`c10_4` 等）均在文本中写明“社区帖/作者为社区用户/非厂商正式文档”；商业判断引用社区仅作佐证，不把社区说法写成官方事实。
- B 未发现“结论声称官方、但引用全部为社区/第三方”的情况（自动审计只命中一条 hypothesis，它是在说“官方页面可能……待验证”，不是断言）。
- 要求官方/正式/PDF 的缺口有代码级关闭限制；B 的 `gap2` 用官方 PDF/Learn 关闭，符合规则。
- 仍存在模型把第三方解释混入官方推导的情况（`c1_5`、`c1_8`），属于语义层残余风险。

## 8. 独立补查的重要缺口

已实际访问/检索的官方页面：

- `https://learn.microsoft.com/microsoft-copilot-studio/guidance/plan-agent-throughput-rate-limits`
- `https://learn.microsoft.com/en-us/microsoft-copilot-studio/troubleshoot-throttling-errors-agents`
- `https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-quotas`
- `https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-licensing`
- 两份 Microsoft Copilot Studio Licensing Guide PDF（November 2025 20 页；另一版本 21 页）

发现：

- 官方有按 Dataverse 环境/付费档位的 RPM/RPH 配额与节流说明；
- 许可指南只写 “Usage is limited to fair usage limits. Microsoft reserves the right to update the limits…”；
- **没有公开 fair usage 的具体数值阈值或触发后的精确处置**。因此“公平使用上限”相关缺口是真实的资料缺口，不是没有尝试获取。
- 未遇到需要登录才能读取的官方页面。Scribd 等第三方页面存在访问限制，未作为证据使用。

## 9. API 消耗

### 9.1 两次最终研究

| 资源 | 运行 A | 运行 B | 合计 |
| --- | ---: | ---: | ---: |
| DeepSeek 输入 tokens | 415,983 | 504,908 | 920,891 |
| DeepSeek 输出 tokens | 44,142 | 42,838 | 86,980 |
| Embedding tokens | 97,820 | 12,337 | 110,157 |
| Reranker tokens | 174,776 | 149,021 | 323,797 |
| Tavily credits | 8 | 4 | 12 |
| 网页读取 | 33 | 15 | 48 |
| PDF 提取页数 | 41 | 0（复用） | 41 |

### 9.2 全部历史/验证 trace（含失败尝试）

- DeepSeek：输入约 2,009,558 tokens，输出约 220,413 tokens。
- Embedding：约 371,897 tokens；Reranker：约 930,455 tokens。
- Tavily：42 credits；网页读取 160 次；PDF 提取 61 页。
- 明细：`examples/live/validation/usage-summary.json`。
- 另有少量手工连通性/独立补查调用（1 次 DeepSeek、1 次 Tavily 搜索、数个官方页面读取）未计入上述 trace 汇总。

## 10. 未解决问题与边界

1. **开放缺口**：A 16 个、B 7 个；集中在 Product Terms 脚注、公平使用阈值、合格 SKU 的官方完整清单、收入确认口径。没有用宣传或定价填补。
2. **语义核验**：代码不能证明一段摘录在语义上充分支持结论；`c1_5`/`c1_8` 的过度归因和数字引用不完整就是例子。最终报告保留这些问题。
3. **公平使用上限**：官方未公开具体数值；只能保留开放缺口和可检验假设。
4. **比较平衡**：B 的比较守卫被模型无视 2 次（已记录 `plan_guard_overridden`）；机制能提醒和留痕，但不能强制模型改变推理。
5. **模型波动**：A/B 使用 `deepseek-flash`，同样的提示会产生不同的计划和结论；B 的 100 条结论不意味着比 A 的 86 条更可靠。
6. **跨进程续跑**：仍未实现；中断后只能从保存的 state/trace 人工分析，不能从原进程继续。
7. **OCR/登录页面**：文本型 PDF 已支持；扫描件、需要登录的页面仍不支持。
8. **成本**：只记录了 token/调用/credits，没有把未公开的单价换算成金额；不应把“预算上限”表述为金额上限。

## 11. 产物索引

- 最终成功运行：
  - `examples/live/validation/runA/research-d968652bc210-e1dl242r/`
  - `examples/live/validation/runB/research-7ee761cd91fd-wvgpainm/`
- 失败/中间尝试（保留用于复查）：
  - `runA-first-network-error/`：DeepSeek 瞬时 network_error。
  - `runA-second-quote-abort/`：释义型引用导致整轮中止（修复前）。
  - `runA-third-citation-abort/`：跨轮引用被旧校验拒绝（修复前）。
  - `runB-round7-invalid-schema/`、`runB-round10-schema-abort/`：Claim 标签/引用矛盾耗尽恢复预算（修复前）。
- API 明细：`examples/live/validation/usage-summary.json`
- 暂停点交接：`examples/live/validation/HANDOFF.md`
- 最终回归：`env -u PYTHONPATH .venv/bin/python -m pytest -q -p no:cacheprovider` → 205 passed

## 12. 用户端 Sticker Mule 运行：研究质量失败与后续修复

运行目录：runs/research-7392c07dae2d-ddxpv8qg/。用户问题为“企业目前商业链路，哪些链路可以接入定制化agent？”

- 运行在 9 轮、36 次 DeepSeek 调用、7 次 Tavily 搜索、24 次网页读取后停止；保留 24 条证据、49 条 Claim、7 个开放缺口。停止原因是 budget_model_calls，不是研究完成。
- 本次入库的 7 个来源全部为第三方；Trace 显示部分 Sticker Mule 官方 URL 返回 http_error。结论主要重复说明第三方来源不能证明官方做法、未找到官方 AI/Agent 披露，以及第三方所述订单设计流程；未形成可靠的端到端业务流程图。
- 已确认的代码根因之一：此前来源权威分类的厂商域名规则主要写死 Microsoft。即便 stickermule.com 页面成功读取，也会误标为第三方。另一个任务层缺口是未要求流程类研究先映射交易步骤，导致规划反复围绕 AI 招聘信息与官方披露缺失展开。
- 后续修复：厂商来源分类增加企业名与注册域名匹配启发式，并在资料库初始化时升级符合规则的旧来源；官方资料 Gap 的向量检索只把厂商官方来源交给后续覆盖判断；流程/Agent 接入类目标要求先调查端到端流程，并将内部未知信息标为待核实假设。
- 新增 4 项离线回归测试，覆盖通用企业域名识别、官方来源检索过滤、流程目标规划提示和流程结论提示。当前全量测试 209 passed，依赖检查通过。
- 修复后的真实研究尚未重跑。以上改动目前只通过离线测试；不能据此宣称 Sticker Mule 研究质量已通过实测，也不应把这次原失败运行计作成功验收。重跑会消耗真实 API 配额。
