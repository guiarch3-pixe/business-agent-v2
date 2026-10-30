# Microsoft｜企业研究

研究问题：Microsoft 365 Copilot 与 Copilot Studio 面向的企业使用者、收费单位和购买前提有何区别？这些差异可能如何影响企业客户扩展使用和微软的收入来源？优先使用官方资料；将价格与许可事实、基于事实的推导、商业判断和仍待验证假设明确区分，不把产品定价直接当成已实现收入或利润。

模式：live；停止原因：round_limit；研究轮次：10

引用关系与摘录位置已做代码校验；语义支持关系、事实分类和缺口关闭是模型判断，未经独立事实核实。

## 事实（来源陈述）

- **c1_1** [supported] 根据微软官方《Copilot Studio 许可指南》，Copilot Credits 是 Copilot Studio 各能力通用的计价货币；用户与 Copilot Studio 代理交互或代理代为执行任务时会消耗 Credits，单次响应或动作扣减的 credit 数量取决于任务复杂度。 [ev_74051b80b3a8d2af897e5dd6](#ev_74051b80b3a8d2af897e5dd6)（supports） [ev_a18f5996ee251d00634e7981](#ev_a18f5996ee251d00634e7981)（supports）
  依据/推导：官方 PDF 原文直接陈述 Credits 为通用货币及其消耗机制；引用来源为厂商官方许可指南，主语为 Copilot Studio，不外推至 Microsoft 365 Copilot。
- **c1_2** [supported] 官方许可指南列出 Copilot Credits 的三种获取/计费方式：Microsoft Copilot Studio 按需付费计量器（pay-as-you-go meter）、Microsoft Copilot Studio 许可（即 Copilot Credit 容量包 capacity pack），以及 Copilot Credit 预付费计划（Pre-Purchase Plan）。 [ev_a18f5996ee251d00634e7981](#ev_a18f5996ee251d00634e7981)（supports） [ev_74051b80b3a8d2af897e5dd6](#ev_74051b80b3a8d2af897e5dd6)（supports）
  依据/推导：两处官方原文一致列举三种方式，属定价/计费结构事实，不涉及实际收入。
- **c1_3** [supported] 按需付费计量器（PAYG）允许组织按账单月内代理实际消耗的 Copilot Credits 后付费，无需前期许可承诺，官方标注价格为每 Copilot Credit 0.01 美元。 [ev_471052c0e61e2ff67d379148](#ev_471052c0e61e2ff67d379148)（supports）
  依据/推导：官方许可指南原文同时给出模式（后付费、无前期承诺）与标价；此为标价事实，不能推出已实现收入或利润。
- **c1_4** [supported] 微软 Copilot Studio 定价页面称 Copilot Studio 以租户级（tenant-wide）许可方式销售，包含容量为每包 25,000 Copilot Credits 的容量包，标价 200.00 美元/包/月；代理完成的动作或响应按实际用量扣减不同数量的 Credits。 [ev_3d08d4e65e776471cd8e1448](#ev_3d08d4e65e776471cd8e1448)（supports）
  依据/推导：厂商官方定价页面原文直接陈述容量包规格与标价；原文另有第三方资料称存在标价为 0 的“Copilot Studio User License”可访问创作工具，但本轮官方摘录未覆盖该条目，故不纳入本结论。
- **c1_5** [supported] 官方许可指南的对比表中，Microsoft 365 Copilot 为每用户每月 30 美元，并包含代理用量（included agent usage）；而 Copilot Studio 相关选项为按需付费（表中标注 unlimited，附脚注）、容量包许可（25,000 Copilot Credits/包，附脚注）及预付费计划（依档位，附脚注），并提及 Fair Usage Limit 公平使用限制。 [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports）
  依据/推导：官方原文字面列出两种收费单位：M365 Copilot 按用户/月包含代理用量，Copilot Studio 走 Credits 容量包/PAYG/预付费。摘录取自表格行列拼接，脚注内容不完整，故“unlimited”等细节不作细节断言；主语须限定为对应行所属产品。
- **c1_6** [supported] 第三方博客 CIAOPS 称，要让未被分配许可的用户与代理对话，租户管理员须配置 Copilot Studio 订阅，方式包括预付费的 Copilot Studio Message Pack（如每包每月 25,000 Credits，未获许可用户的交互从该集中池中消耗）或按需付费（将 Copilot Studio 环境关联 Azure 订阅，按实际消耗通过 Azure 每月计费）。 [ev_25e499216e10d9f4ef563fae](#ev_25e499216e10d9f4ef563fae)（supports）
  依据/推导：第三方来源，仅作为与官方描述（Centers/容量包/PAYG）一致的旁证，不能视作厂商正式许可条款；“Message Pack”为第三方措辞，官方称 Copilot Credit capacity pack。
- **c1_7** [supported] 第三方博客 CIAOPS 称，个人 M365 Copilot 许可覆盖其自身的创建与使用，但不覆盖其他访问高级、租户数据接地（tenant-grounded）内容的用户的消耗。 [ev_cd190fc6dc77296711cbd2ff](#ev_cd190fc6dc77296711cbd2ff)（supports）
  依据/推导：仅代表第三方作者观点，不能当作微软正式条款；但与该来源上文及官方“M365 Copilot 含代理用量”的表述需结合解读，故仅作为待官方确认的旁证。
- **c2_1** [supported] 微软官方《Copilot Studio 许可指南》的对比表中，Microsoft 365 Copilot 一行为每用户每月 30 美元，并标注“Included agent usage”（含代理用量），同表还并列列出 Copilot Studio 按需付费、容量包许可（25,000 Copilot Credits/包）与预付费计划等选项；但该摘录仅含表格字面与脚注编号，未展开“所含代理用量”的具体额度与边界。 [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports）
  依据/推导：厂商官方 PDF 原文直接显示 M365 Copilot 标价及“Included agent usage”字样，主语限定为 M365 Copilot 行；脚注1/2/3/4 内容未在摘录中出现，故不能断言额度、是否限本人、是否覆盖未获许可用户。
- **c2_2** [supported] 第三方许可解读博客（LicenseQ）称，持有 Microsoft 365 Copilot User SL（30 美元/用户/月）的用户已随许可获得 Copilot Studio 使用权，可用于面向员工的代理，以及在 Teams、SharePoint、M365 Copilot 等界面下、以该已许可用户身份运行的代理，无需额外付费。 [ev_559c66e41ae49989b83bc970](#ev_559c66e41ae49989b83bc970)（supports）
  依据/推导：原文明确写出该说法，但来源为第三方解读而非微软正式条款，且其限定为“employee-facing agents”与“licensing user’s identity”，不能扩展为覆盖未获许可用户。
- **c2_3** [supported] 同一第三方博客称，上述随 M365 Copilot 附带的使用受“fair usage（公平使用）”约束，微软未公布确切阈值并保留更新权；该文提醒不要据此规划高用量场景。 [ev_559c66e41ae49989b83bc970](#ev_559c66e41ae49989b83bc970)（supports）
  依据/推导：原文后续句直接陈述公平使用的存在与不透明性；官方摘录仅在第4条脚注位置出现“Fair Usage Limit”，细节未展开，故阈值与条款边界仍属未证实。
- **c2_4** [supported] 第三方博客 CIAOPS 称，单一的 M365 Copilot 许可不包含可供租户内未获许可用户使用的 Copilot Studio 消息容量池；该许可授予的权利是在无额外费用下为自己使用而创建和管理内部流程代理、并由本人访问使用这些代理。 [ev_191520cb2091a0e531ed020b](#ev_191520cb2091a0e531ed020b)（supports） [ev_026e2353f40c6d25e51e17a9](#ev_026e2353f40c6d25e51e17a9)（supports）
  依据/推导：引文以“Confirmation: Correct”形式给出结论与权利范围，但属第三方作者观点，不能充当微软正式许可条款；与 ev_559c66e41ae49989b83bc970 方向一致（限本人使用），未见官方原文直接佐证。
- **c2_5** [supported] 第三方博客 CIAOPS 称，个人 M365 Copilot 许可覆盖其自身创建与使用，但不覆盖其他访问高级、租户数据接地内容的用户的消耗；未获许可同事的消耗被视为组织级成本，须由单独的 Copilot Studio 组织订阅承担。 [ev_cd190fc6dc77296711cbd2ff](#ev_cd190fc6dc77296711cbd2ff)（supports） [ev_026e2353f40c6d25e51e17a9](#ev_026e2353f40c6d25e51e17a9)（supports）
  依据/推导：第三方连续表述，两处引文互相印证“本人覆盖/他人不覆盖”的边界；仍非厂商正式文档。
- **c2_6** [supported] 微软 Q&A 社区（learn.microsoft.com 托管，回答者为标注 Microsoft External Staff 的 Prasad-MSFT）的答复称：若租户已启用 Copilot Studio 计费（credits 或 PAYG），最终用户的使用在租户级计费，代理使用者无需特殊许可；若无租户计费，最终用户可能需要单独的 Copilot 许可才能访问该代理。 [ev_57dc177d0ab3247a7f29ac8f](#ev_57dc177d0ab3247a7f29ac8f)（supports）
  依据/推导：属官方域名托管的社区问答答复，作者标注为微软外部人员，但按规程不等同于厂商正式产品/许可文档，仅作辅助证据；其表述与第三方“未获许可用户需租户级计费”方向一致。
- **c3_1** [supported] 微软官方《Copilot Studio 许可指南》脚注第 4 条明确：面向员工的场景（Business to Employee）中，Microsoft Copilot Studio 代理及其调用的 Copilot Studio 工具/功能的使用量，在“代理使用者持有 Microsoft 365 Copilot 许可”且“代理以该已认证 M365 Copilot USL 用户身份运行”时，计入 Microsoft 365 Copilot USL 之中；使用受公平使用上限（fair usage limits）约束，微软保留随产品演进更新上限的权利。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports）
  依据/推导：直接引用官方 PDF 原文，主语与限定条件（B2E 场景、许可用户、认证身份、公平使用）均取自引文及上下文（前文为“Pre-Purchase Plan … See Pre-Purchase Plan pricing tiers here. 4.”）。
- **c3_2** [supported] 同一官方指南脚注第 5 条称：基于 Copilot Studio 构建、面向 Teams、SharePoint 与 Microsoft 365 Copilot 的代理，随 Microsoft 365 Copilot 用户许可附带，不额外收费。 [ev_25868af562dd0d2ed0210605](#ev_25868af562dd0d2ed0210605)（supports）
  依据/推导：官方原文直接陈述“included with the Microsoft 365 Copilot user license at no additional charge”；原文未在该句给出具体额度数值。
- **c3_3** [supported] 官方对比表将 Microsoft 365 Copilot 列为 30 美元/用户/月，标注“Included agent usage1”，同表 Copilot Studio 侧为按需付费（脚注2）、许可/容量包（25,000 Copilot Credit/包，脚注3）、预付费计划（依档位，脚注3），并单列 Fair Usage Limit（脚注4）；但该表摘录本身只出现脚注编号，未在表格字面上写明随附容量的具体额度数值。 [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports）
  依据/推导：官方表格字面事实；须注意这是 M365 Copilot 行与 Copilot Studio 侧并列，不能把 Copilot Studio 的 25,000 Credits/包 读作 M365 Copilot 随附额度。
- **c3_4** [supported] 第三方高校知识库文章在引述微软规则时称：员工面向场景下 Copilot Studio 代理及其工具的使用量计入 M365 Copilot USL，条件是代理使用者持有 M365 Copilot 许可且代理以该已认证 USL 用户身份运行，并受公平使用限制、微软保留更新权；该文前文另称“用户与生产代理交互需要 Copilot Credits，除非用户持有 M365 Copilot 许可覆盖代理使用”。 [ev_935a0e34649f8223ac9ff4f2](#ev_935a0e34649f8223ac9ff4f2)（supports）
  依据/推导：第三方（大学 IT 知识库）转述，与官方脚注4措辞高度一致，可作旁证但不能替代官方原文。
- **c3_5** [supported] 第三方 Wiki（LICENSEWARE）称：未获 Copilot 许可的人使用代理会消耗 credits，其引用的费率页示例只为代理服务对象中的 100 名未获许可用户计费（该代理同时服务 50 名已许可用户）；并称 Microsoft Learn 表示持 M365 Copilot 许可在 Copilot Chat、Teams、SharePoint 中使用代理不计入 Copilot Studio 容量包或计量器，但该“零计费”附有条件（身份、触发方式、公平使用、排除 CUA）。 [ev_af5185b58ee678d3e7aef6e4](#ev_af5185b58ee678d3e7aef6e4)（supports） [ev_fc79abb7521f8b96f6ef5f71](#ev_fc79abb7521f8b96f6ef5f71)（supports）
  依据/推导：第三方二手转述，其原文标注引用 learn.microsoft.com 链接；本轮未取得该 Learn 页面原文，故仅作方向性旁证，不能据此关闭官方条款缺口。
- **c3_6** [supported] 第三方 Wiki 的条目摘要另列出：M365 Copilot 为按用户附加订阅（User SL）叠加计量化代理用量，前置条件为已列明的 Microsoft 365/Office 365 或独立服务许可，容量包为每包每月 25,000 Copilot Credits。 [ev_66568c743ae007c496b4533f](#ev_66568c743ae007c496b4533f)（supports）
  依据/推导：第三方摘要文字；其“前置条件”表述为概括，未见官方条款逐字对应，仅作背景，不用于界定随附额度。
- **c4_1** [supported] 微软官方 Microsoft Learn 页面《Standard harness licensing - Microsoft Copilot Studio》原文称：持有 Microsoft 365 Copilot 许可的用户在 Copilot Chat、Microsoft Teams 或 SharePoint 中使用代理时，针对 classic answers（经典答案）、generative answers（生成式答案）或 Microsoft Graph tenant grounding（租户数据接地），不计入 Copilot Studio message pack 或计量器（meter）。 [ev_95899b6cf40d7a032858ace6](#ev_95899b6cf40d7a032858ace6)（supports）
  依据/推导：vendor_official 的 Learn 页面原文直接陈述零计费场景，主语为“持 M365 Copilot 许可的用户”与指定三个界面；引文未给出公平使用、触发方式或 CUA 排除等附加条件，本轮摘录也未展开，故不将这些条件写成该事实。
- **c4_2** [supported] 上述官方 Learn 原文紧接着举例：当 Microsoft 365 Copilot 许可用户在 Microsoft 365 服务或应用中使用代理时，classic answers、generative answers 或 Microsoft Graph tenant grounding 不会消耗容量（原文以“For example”引出该例）。 [ev_95899b6cf40d7a032858ace6](#ev_95899b6cf40d7a032858ace6)（supports）
  依据/推导：取自同一引文的 context_after，说明零计费仅覆盖所列三类能力/答案类型，不覆盖其他代理行为；该限制对判断“是否仅限特定触发与答案类型”重要，但仍属字面限定而非完整条件清单。
- **c4_3** [supported] 官方《Copilot Studio 许可指南》脚注规定：面向员工的场景（Business to Employee）中，Copilot Studio 代理及其调用的工具/功能使用量计入 Microsoft 365 Copilot USL，条件是代理使用者持有 Microsoft 365 Copilot 许可、且代理以该已认证 USL 用户身份运行；使用受公平使用上限（fair usage limits）约束，微软保留随产品演进更新上限的权利。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports）
  依据/推导：引用此前已校验的官方 PDF 摘录；此处“身份”维度（使用者持证 + 以该用户身份认证运行）由官方条款直接给出，是问题中“身份条件”的唯一官方字面支撑。
- **c4_4** [supported] 第三方 Wiki（LICENSEWARE）转述 Microsoft Learn 费率页称：M365 Copilot 许可在 Copilot Chat、Teams、SharePoint 中使用代理不计入容量包或计量器，但该零计费附有条件（身份、触发方式、公平使用、排除 Computer-Using Agents）；并称未获许可用户使用代理会消耗 credits，且费率页示例只为某代理的 100 名未获许可用户计费（该代理同时服务 50 名已许可用户）。 [ev_fc79abb7521f8b96f6ef5f71](#ev_fc79abb7521f8b96f6ef5f71)（supports） [ev_8e4ac1633098e933fbaff23c](#ev_8e4ac1633098e933fbaff23c)（supports） [ev_dab8e0c5567387bd76c1ea4a](#ev_dab8e0c5567387bd76c1ea4a)（supports）
  依据/推导：third_party 二手转述，其链接指向 learn.microsoft.com 但本轮未取得该费率页原文；仅作条件清单方向性旁证，不能替代官方条款，故不据此断言 CUA 排除或触发方式等细节。
- **c4_5** [supported] 第三方 2026 定价文章称：代理交互在 Copilot Chat、Teams 和 SharePoint 内不（另行计量）；连接计费策略（connected billing policy）内的未获许可用户则按计量收费；并将“在 Copilot Chat 或 SharePoint 中使用代理但无席位的人”列为按用量计费的对象。 [ev_a2c571d68f9943a013d2da85](#ev_a2c571d68f9943a013d2da85)（supports） [ev_93e76e6d6ee250fa46dbb28a](#ev_93e76e6d6ee250fa46dbb28a)（supports）
  依据/推导：third_party 来源，与官方 Learn 零计费条款和第三方 Wiki 的未许可用户计费方向一致，可作旁证；其“connected billing policy”等措辞为第三方概括，非厂商正式条款原文。
- **c5_1** [supported] 微软官方《Copilot Studio 许可指南》（2026年10月版）载明：Copilot Credit 容量包（capacity pack）通过 Copilot Studio 订阅许可销售；每包价格为 200 美元/月（按年计费），每包容量为 25,000 Copilot Credits；未使用的额度不会结转到下个月，建议按租户每月预计消耗的 Credits 数量购买。 [ev_c05542491d40e826f23e8c8a](#ev_c05542491d40e826f23e8c8a)（supports） [ev_28551c4a7bf7fcced4a5c374](#ev_28551c4a7bf7fcced4a5c374)（supports） [ev_2b9e141ce0074ba49ee0902f](#ev_2b9e141ce0074ba49ee0902f)（supports）
  依据/推导：原文直接给出容量包规格、计价单位与“billed annually”的计费方式，主语为 Microsoft Copilot Studio 的 capacity pack；这仅为标价事实，不推断已实现收入或利润。
- **c5_2** [supported] 同一官方指南的11月版对容量包给出相同规格与价格：通过 Copilot Studio 订阅许可提供，每包 200 美元/月，1 个容量包 = 25,000 Copilot Credits，未使用 credits 不结转，并建议另设 pay-as-you-go 计量器以保证业务连续性——credits 未耗尽前消耗不计入 PAYG 计量。 [ev_8dd171278e8f01404354694a](#ev_8dd171278e8f01404354694a)（supports） [ev_c3b106414c41ffadca235ae5](#ev_c3b106414c41ffadca235ae5)（supports） [ev_41d3722308a5dc62841ab0a5](#ev_41d3722308a5dc62841ab0a5)（supports） [ev_f4a973b7dc16323e83c460c3](#ev_f4a973b7dc16323e83c460c3)（supports）
  依据/推导：两版官方 PDF 对容量包的包价、容量、不结转规则表述一致，可互证；11月版未在句中标明“billed annually”，故年度计费细节仅以10月版表述为准。
- **c5_3** [supported] 官方指南对预付费计划（Copilot Credit Pre-Purchase Plan）仅载明其性质：为组织提供一年期、一次性预付（pay-upfront）购买 Copilot Credits 的选项，并按档位提供折扣；客户购买的是 Copilot Credit Commit Units（CCCU）池，每个 CCCU 价值 1 美元、可换算 100 Copilot Credits。 [ev_6384dfc393693ccb31745e72](#ev_6384dfc393693ccb31745e72)（supports）
  依据/推导：原文明确写出预付、一年期、按档折扣与 CCCU 换算率，但未在摘录中列出各档位的具体名称、金额或折扣幅度，故不对档位价格作断言。
- **c5_4** [supported] 官方《Copilot Studio 许可指南》对比表将“Copilot Credit Pre-Purchase Plan”一栏的价格标注为“Depends on the tier”（取决于档位），并在同表单列“Fair Usage Limit”一项，但表内仅出现脚注编号，摘录未展开各档位数值与公平使用限制的具体条款。 [ev_a00c24a535eaedb78a612de4](#ev_a00c24a535eaedb78a612de4)（supports） [ev_6f17a4fe98ba2630e223ac27](#ev_6f17a4fe98ba2630e223ac27)（supports）
  依据/推导：官方表格字面事实：预付费计划价格“依档位”而未给出档位明细；Fair Usage Limit 仅以条目/脚注编号形式出现。不能据此断言档位数量或公平使用条款内容。
- **c5_5** [supported] 微软官方 Learn 文章《Use Capacity Packs vs Pay-as-you-go Billing for Microsoft Copilot Chat》称：Copilot Studio 容量包是一种预付费订阅，提供用于 Copilot Chat 与 SharePoint 代理用量的 credits，租户内共享；每包每月提供 25,000 credits 的购买数量。 [ev_032bbbc4df3151bb3f1edcb3](#ev_032bbbc4df3151bb3f1edcb3)（supports） [ev_17c1117b96d2617043b1790c](#ev_17c1117b96d2617043b1790c)（supports）
  依据/推导：官方 Learn 原文确认包容量与预付费性质；该页摘录未给出包价数字，故此处不写价格，避免与许可指南价格混用。
- **c5_6** [supported] 第三方来源对容量包价格存在与官方不一致的表述：第三方博客 CloudZero 称“预付费容量包每 25,000 credits 每月 200 美元”；第三方站点 o365hq 称 Copilot Studio 容量包标价为每年 2,400 美元一次性预付、按年分摊月付时每年 2,520 美元、或单月承诺时每月 240 美元；第三方 Wiki LICENSEWARE 则按每包每月 25,000 Credits、20.00 美元的口径列示（摘录被截断）。 [ev_448ccee7c6af8bf2cd1c0961](#ev_448ccee7c6af8bf2cd1c0961)（supports） [ev_e0a050a8f91feb72529bed19](#ev_e0a050a8f91feb72529bed19)（supports） [ev_913bc5f4729001583f2fa939](#ev_913bc5f4729001583f2fa939)（supports） [ev_2b9e141ce0074ba49ee0902f](#ev_2b9e141ce0074ba49ee0902f)（supports）
  依据/推导：三份 third_party 的价格口径彼此不一（200/月、240/月或2,400–2,520/年、20.00/包月），与官方许可证指南“200 美元/包/月（按年计费）”存在张力和可能的计价口径差异（年付折扣 vs 月付溢价）；按规程保留冲突，仅陈述第三方各自说了什么，不判定孰对，也不能以第三方数据替代官方条款。
- **c6_1** [supported] 微软官方《Copilot Studio 许可指南》脚注（第4条）原文规定：面向员工的场景（Business to Employee）中，Copilot Studio 代理及其调用的工具/功能用量，在“代理使用者持有 Microsoft 365 Copilot 许可”且“代理以该已认证 Microsoft 365 Copilot USL 用户身份运行”时计入 Microsoft 365 Copilot USL；使用受公平使用上限约束，微软保留随产品演进更新上限的权利。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports）
  依据/推导：官方 PDF 原文直接给出身份条件（使用者持证 + 以该用户认证身份运行）与公平使用限定，主语限定为 M365 Copilot USL 参与的员工面向场景；不据此断言未获许可用户的处理方式。
- **c6_2** [supported] 同一官方指南脚注（第5条）称：基于 Copilot Studio 构建、面向 Teams、SharePoint 与 Microsoft 365 Copilot 的代理，随 Microsoft 365 Copilot 用户许可附带，不额外收费。 [ev_25868af562dd0d2ed0210605](#ev_25868af562dd0d2ed0210605)（supports）
  依据/推导：官方原文直接陈述随附性；该句本身未给出额度数值，也未说明未获许可用户的处理。
- **c6_3** [supported] 官方对比表将 Microsoft 365 Copilot 列为 30 美元/用户/月并标注“Included agent usage1”，Copilot Studio 侧并列按需付费、容量包（25,000 Copilot Credits/包）与预付费计划，并单列 Fair Usage Limit；但摘录仅呈现表格字面与脚注编号，未在字面上写明随附容量的具体额度或“仅限本人”的表述。 [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports）
  依据/推导：官方表格字面事实；脚注1/2/3/4 内容在本轮摘录中未展开，故不能把“Included agent usage”的边界与 Copilot Studio 容量包规格混同。
- **c6_4** [supported] 官方许可指南开头声明：该指南不取代、也不替换 Microsoft Product Terms 中涵盖使用权的法律文件。 [ev_ebc24156510a771ef0b63cea](#ev_ebc24156510a771ef0b63cea)（supports）
  依据/推导：官方原文自述其效力低于 Product Terms，故判断“未获许可用户须由租户级计费承接”这类约束，需以 Product Terms 或正式计费条款为准，本指南脚注不足以单独定案。
- **c6_5** [supported] 第三方博客 CIAOPS 称：单一 M365 Copilot 许可不包含可供租户内未获许可用户使用的 Copilot Studio 消息容量池；该许可仅授予本人在无额外费用下创建/管理内部流程代理并本人访问使用的权利，未获许可同事的消耗属组织级成本，须由单独的 Copilot Studio 组织订阅承担。 [ev_026e2353f40c6d25e51e17a9](#ev_026e2353f40c6d25e51e17a9)（supports）
  依据/推导：第三方作者观点，与官方脚注的身份条件方向一致，但不能替代厂商正式条款，不能单独关闭要求官方条款的缺口。
- **c6_6** [supported] 微软 Q&A 社区答复（learn.microsoft.com 托管，回答者标注为 Microsoft External Staff 的 Prasad-MSFT）称：若租户已启用 Copilot Studio 计费（credits 或 PAYG），最终用户使用在租户级计费、代理使用者无需特殊许可；若无租户计费，最终用户可能需要单独的 Copilot 许可才能访问该代理。 [ev_57dc177d0ab3247a7f29ac8f](#ev_57dc177d0ab3247a7f29ac8f)（supports）
  依据/推导：官方域名托管的社区回帖，作者标注微软外部人员，但按规程不等同于厂商正式产品/许可文档，仅为旁证。
- **c6_7** [supported] Power Platform 社区论坛帖（官方域名托管，回答者为 Microsoft Employee 的 Nivedipa-MSFT）称：持有 Microsoft 365 Copilot 许可可在 Teams 或 SharePoint 中使用 Copilot Studio 代理且无需额外费用，前提是使用为交互式且由该用户发起；由已许可用户在 M365 内触发的 Power Automate 流、操作、工具与高级连接器亦含在内，此情形不消耗 Copilot Credits。 [ev_8b335a5d6dfe792d82d57514](#ev_8b335a5d6dfe792d82d57514)（supports）
  依据/推导：社区回帖而非正式许可文档；其“由用户发起、交互式”的限定与“仅限已许可用户本人”方向一致，可作为辅助证据，不单独定案。
- **c6_8** [supported] 第三方 Wiki（LICENSEWARE）转述 Microsoft Learn 费率页称：未获许可用户使用代理会消耗 credits，示例只为某代理的 100 名未获许可用户计费（该代理同时服务 50 名已许可用户）；并称 M365 Copilot 许可在 Copilot Chat、Teams、SharePoint 中使用代理不计入容量包或计量器，但该零计费附条件（身份、触发方式、公平使用、排除 CUA）。该 Wiki 同时列出容量包为 25,000 Copilot Credits/包/月。 [ev_af5185b58ee678d3e7aef6e4](#ev_af5185b58ee678d3e7aef6e4)（supports） [ev_fc79abb7521f8b96f6ef5f71](#ev_fc79abb7521f8b96f6ef5f71)（supports） [ev_66568c743ae007c496b4533f](#ev_66568c743ae007c496b4533f)（supports）
  依据/推导：第三方二手转述，其原文标注引用 learn.microsoft.com 但本轮未取得该费率页原文，仅作方向性旁证；不能把其转述当作官方条款原文。
- **c7_1** [supported] 微软官方 Microsoft Learn 页面《Standard harness licensing - Microsoft Copilot Studio》原文称：持有 Microsoft 365 Copilot 许可的用户在 Copilot Chat、Microsoft Teams 或 SharePoint 中使用代理时，针对 classic answers、generative answers 或 Microsoft Graph tenant grounding，不计入 Copilot Studio message pack 或计量器（meter）。 [ev_95899b6cf40d7a032858ace6](#ev_95899b6cf40d7a032858ace6)（supports） [ev_69fb0940a0671f4663533f19](#ev_69fb0940a0671f4663533f19)（supports）
  依据/推导：vendor_official 的 Learn 页面原文直接陈述零计费场景，主语限定为持 M365 Copilot 许可的用户与三个指定界面；引文与紧接的例句（context_after）都把范围限定在 classic answers、generative answers、Microsoft Graph tenant grounding 三类能力，未提及其他代理行为。
- **c7_2** [supported] 同一 Learn 页面的紧接举例说明：Microsoft 365 Copilot 许可用户在 Microsoft 365 服务或应用中使用代理时，classic answers、generative answers 或 Microsoft Graph tenant grounding 属于“zero-rated usage（零计费用量）”，并称该 M365 Copilot 许可“includes these features（包含这些功能）”；摘录在此处截断，未展开更多条件。 [ev_69fb0940a0671f4663533f19](#ev_69fb0940a0671f4663533f19)（supports）
  依据/推导：取自该官方段落的 context_after 字面；摘录止于“includes these feat...”，因此对“包含哪些功能、是否另有附加限制”不作文本之外的补充断言。
- **c7_3** [supported] 官方《Copilot Studio 许可指南》脚注（第4条）规定：面向员工的场景（Business to Employee）中，Copilot Studio 代理及其调用的工具/功能用量，在“代理使用者持有 Microsoft 365 Copilot 许可”且“代理以该已认证 Microsoft 365 Copilot USL 用户身份运行”时计入 Microsoft 365 Copilot USL；使用受公平使用上限（fair usage limits）约束，微软保留随产品演进更新上限的权利。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports）
  依据/推导：此前已校验的 vendor_official 官方 PDF 摘录，直接给出身份条件与公平使用条款；这是本轮“身份界定”条件唯一的官方字面来源，主语为 M365 Copilot USL 参与的员工面向场景。
- **c7_4** [supported] 官方《Copilot Studio 许可指南》脚注（第5条）称：基于 Copilot Studio 构建、面向 Teams、SharePoint 与 Microsoft 365 Copilot 的代理，随 Microsoft 365 Copilot 用户许可附带，不额外收费；该句本身未给出随附额度数值，也未说明未获许可用户的处理方式。 [ev_25868af562dd0d2ed0210605](#ev_25868af562dd0d2ed0210605)（supports）
  依据/推导：官方原文直接陈述随附性，可与 Learn 页面零计费表述互为印证；但脚注本身未载明额度或未许可用户条款。
- **c7_5** [supported] 第三方 Wiki（LICENSEWARE，third_party）转述 Microsoft Learn 费率页称：M365 Copilot 许可在 Copilot Chat、Teams、SharePoint 中使用代理不计入容量包或计量器，但该“零计费”附有条件（身份、触发方式、公平使用、排除 Computer-Using Agents）；并称未获许可用户使用代理会消耗 credits，费率页示例只为某代理的 100 名未获许可用户计费（该代理同时服务 50 名已许可用户）。 [ev_b0013918677d3356944c0895](#ev_b0013918677d3356944c0895)（supports） [ev_0a1f12af93d3fbc02f823ca5](#ev_0a1f12af93d3fbc02f823ca5)（supports） [ev_fc79abb7521f8b96f6ef5f71](#ev_fc79abb7521f8b96f6ef5f71)（supports）
  依据/推导：third_party 二手转述，原文标注引用 learn.microsoft.com，但本轮取得的官方 Learn 摘录未覆盖触发方式、CUA 排除与 100 名未许可用户示例；按规程仅作方向性旁证，不能当作官方条款原文。
- **c7_6** [supported] 第三方 2026 定价文章（o365hq，third_party）称：已许可用户在 Copilot Chat、Teams 和 SharePoint 内的代理交互不消耗 Copilot Credits；处于“connected billing policy（连接计费策略）”内的未获许可用户则按计量收费，并把“在 Copilot Chat 或 SharePoint 中使用代理但无 M365 Copilot 席位的人”列为按用量计费对象。 [ev_d7fd53462aa8d644b4fd607b](#ev_d7fd53462aa8d644b4fd607b)（supports）
  依据/推导：third_party 概括，与官方 Learn 零计费条款和第三方 Wiki 的未许可用户计费方向一致；其“connected billing policy”等措辞为第三方表述，非厂商条款原文，示例数字亦未给出。
- **c8_1** [supported] 微软官方《Copilot Studio 许可指南》（2025年11月版 PDF）载明：Copilot Credit 预付费计划（Pre-Purchase Plan）提供一年期、一次性预付购买 Copilot Credits 并按档位折扣；客户购买 Copilot Credit Commit Units（CCCU）池，每个 CCCU 价值 1 美元、折算 100 Copilot Credits。 [ev_6384dfc393693ccb31745e72](#ev_6384dfc393693ccb31745e72)（supports） [ev_e7f728cc95661ada112dc727](#ev_e7f728cc95661ada112dc727)（supports）
  依据/推导：官方 PDF 原文直接陈述计划性质与 CCCU 换算率；此为许可/计价机制事实，不推出已实现收入或利润。
- **c8_2** [supported] 同一官方指南列出“Copilot Credit Pre-Purchase Plan Pricing Tiers”表，共 9 档：档1 3,000 CCCU 价格 2,850 美元（5% 折扣）；档2 15,000 CCCU、14,100 美元（6%）；档3 30,000 CCCU、27,900 美元（7%）；档4 150,000 CCCU、138,000 美元（8%）；档5 300,000 CCCU、270,000 美元（10%）；档6 750,000 CCCU、660,000 美元（12%）；档7 1,500,000 CCCU、1,290,000 美元（14%）；档8 2,250,000 CCCU、1,867,500 美元（17%）；档9 3,000,000 CCCU、2,400,000 美元（20%）。 [ev_56dfd86c47ac3d6e08df5b62](#ev_56dfd86c47ac3d6e08df5b62)（supports） [ev_e7f728cc95661ada112dc727](#ev_e7f728cc95661ada112dc727)（supports）
  依据/推导：官方 PDF 表格原文逐档给出 CCCU 数量、承诺金额与折扣率；金额为标价/承诺金额事实，非已实现收入；档位内容取自同一表格的连续摘录，未作外推。
- **c8_3** [supported] 官方指南的另一表格“Copilot Credit Pre-Purchase Plan Value Conversion”按档位给出 CCCU 对应关系：档1 3,000 CCCU＝300,000 Copilot Credits＝1 个容量包×12 个月；档2 15,000 CCCU＝1,500,000 Credits＝5 包×12 个月；档3 30,000,000 中的 3,000,000 Credits＝10 包×12 个月；档4 150,000 CCCU＝15,000,000 Credits＝50 包×12 个月；档5 300,000 CCCU＝30,000,000 Credits＝100 包×12 个月；档6 750,000 CCCU＝75,000,000 Credits＝250 包×12 个月；档7 1,500,000 CCCU＝500 包×12 个月；档8 2,250,000 CCCU＝750 包×12 个月；档9 3,000,000 CCCU＝1,000 包×12 个月。 [ev_4b959f26c83df458f524be40](#ev_4b959f26c83df458f524be40)（supports）
  依据/推导：原文逐档给出 CCCU→Credits→等价容量包×12 个月的换算；摘录对档3 的 Credits 数字有排版混杂，故该档数值表述保守，但包数对应关系（10 包×12 个月）在摘录中明确。此为换算关系事实，不推断收入。
- **c8_4** [supported] 微软官方《Copilot Studio 许可指南》（2026年10月版 PDF）以 Pre-Purchase Plan（P3）条目载明：一年期预付；购买 Credits 池自动扣减余额；若用量超过可用 credits，可另购 Copilot Credits 或转为按需（pay-as-you-go）计费；未用尽 credits 在年度期末失效；并列出折扣档位从档1 300,000 Credits 的 5% 至档9 300,000,000 Credits 的 20%（中间档为 6%、7%、8%、10%、12%、14%、17%）。 [ev_a3b65c2ec57e21989f91c97b](#ev_a3b65c2ec57e21989f91c97b)（supports）
  依据/推导：官方 PDF 原文直接给出有效期、超量处理与未用额度失效规则，以及按 Credits 计的 9 档折扣；该表以 Credits 而非 CCCU 表示档位数量，与 11 月版的 CCCU 表为同一计划的不同版面表述，两者按 1 CCCU＝100 Credits 换算一致。
- **c8_5** [supported] 官方指南在“credits 不结转”一节中明确：预付费计划预购的 CCCU 在一年期期末失效，并指引查看 Pre-Purchase Plan 的定价档位。 [ev_2eee67abb8bb61271fd0bc66](#ev_2eee67abb8bb61271fd0bc66)（supports）
  依据/推导：官方原文直接陈述未用 CCCU 的到期处理，与 2026 年 10 月版“Unused credits expire at the end of the annual term”一致，可互证。
- **c8_7** [supported] 第三方许可解读（LicenseQ）称：P3 为年度预付、分档折扣最高 20%，2025 年 10 月推出，购买一年期 CCCU 池，折扣从 3,000 CCCU（2,850 美元、5%）至 3,000,000 CCCU（240 万美元、20%）。 [ev_263ae0f13e9424788378f7d0](#ev_263ae0f13e9424788378f7d0)（supports）
  依据/推导：第三方来源，数字与官方档位表两端一致，可作旁证；不能替代官方原文，也不单独关闭缺口。
- **c8_8** [supported] 第三方来源（Rand Group、SAMexpert）对预付费计划给出概括性描述：一年期预付、提供 credits 池与基于量的折扣、未用预付 credits 在年度期末失效、超出余额需另购 credits 或转按需计费；且 1 CCCU＝1 美元＝100 credits，共 9 个折扣档。 [ev_c835b27e9f6ab62bee59209d](#ev_c835b27e9f6ab62bee59209d)（supports） [ev_f07d750c732f78afea191918](#ev_f07d750c732f78afea191918)（supports）
  依据/推导：两份第三方来源的概括与官方条款方向一致，但均未在本轮摘录中列出逐档金额，仅作旁证；SAMexpert 文中“3 levels”字样对应的是 Agent Pre-Purchase Plan，而非 Copilot Credit P3，不应混用。
- **c9_1** [supported] 微软官方 Copilot Studio 定价页面（microsoft.com/en-us/copilot/pricing/copilot-studio）原文写：使用 Copilot Credit packs 时，客户预付费用（pay up front），价格为 200.00 美元/包/月，对应 25,000 Copilot Credits；该页面并被摘录为“Copilot Credit pack 与 pay-as-you-go meter 之间没有产品内功能或能力差异，唯一差别是付款方式”。 [ev_82638d6dd87bf3b75ec2fb8e](#ev_82638d6dd87bf3b75ec2fb8e)（supports）
  依据/推导：vendor_official 的官方定价页面原文直接给出 200.00 美元/包/月的预付口径；引文与紧接的 context_after 均未在字面写出“年”“月付溢价”或“单月承诺价”，故不补充。
- **c9_2** [supported] 官方《Copilot Studio 许可指南》（2026年10月版）在同一段中对容量包的表述为：Pricing: $200 per credit pack/month (billed annually)；Copilot Credit Capacity: 1 capacity pack = 25,000 Copilot Credits，并建议为额外容量开通 pay-as-you-go 计量器以保证业务连续性。 [ev_abf7951d9d970f459397f5ec](#ev_abf7951d9d970f459397f5ec)（supports） [ev_f4a973b7dc16323e83c460c3](#ev_f4a973b7dc16323e83c460c3)（supports）
  依据/推导：官方 PDF 原文以“billed annually（按年计费）”标注 200 美元/包/月；主语为 Copilot Studio 容量包，不涉及 M365 Copilot 条件。
- **c9_3** [supported] 官方《Copilot Studio 许可指南》（2025年11月版）对同一容量包仅写“• Pricing: $200 per pack/month”，未在该句标注“billed annually”。 [ev_bd71a95b07e175b0920d6d89](#ev_bd71a95b07e175b0920d6d89)（supports）
  依据/推导：官方 PDF 字面差异：11 月版缺“billed annually”字样，说明官方资料内部对计费周期的表述并不完全统一；该差异在摘录层面可确认，但其成因（版本更新或表述省略）无法从摘录判断。
- **c9_4** [supported] 第三方站点 o365hq 称，Copilot Studio 页面上租户容量包标价为：每年 2,400 美元一次性预付、按年计费但按月账单时为每年 2,520 美元、或单月承诺时每月 240 美元；并称其“What you pay”一栏按清单价写毎包每年 2,400 美元、超额走 pay-as-you-go。 [ev_e0a050a8f91feb72529bed19](#ev_e0a050a8f91feb72529bed19)（supports） [ev_697d9f2ff22fe19ca05eae8f](#ev_697d9f2ff22fe19ca05eae8f)（supports）
  依据/推导：third_party 来源，其原文自述是转述微软 Copilot Studio 页面；三个数字（2,400/年预付、2,520/年月付、240/月单月承诺）是该第三方口径，本轮未取得官方页面同时呈现这三档的原文。
- **c9_5** [supported] 第三方博客 CloudZero 将容量包列为“Microsoft Copilot Studio Capacity Packs $200/month Monthly Includes 25,000 credits/month”，即按 200 美元/月、每月计费的口径表述。 [ev_cf7723ab96f1ed24abf6f375](#ev_cf7723ab96f1ed24abf6f375)（supports）
  依据/推导：third_party 来源，标签为“Monthly”，与官方许可指南“billed annually”并列展示了另一口径；仅说明第三方如何表述，不判定其准确性。
- **c10_1** [supported] 微软官方《Copilot Studio 许可指南》原文载明：每个使用 Copilot Studio 构建和管理代理的用户都需要一个 Copilot Studio User License，标价为 0 美元；并建议将租户许可与用户许可作为同一笔交易获取以简化入门。 [ev_414550a10cb2870ee7771428](#ev_414550a10cb2870ee7771428)（supports）
  依据/推导：vendor_official 官方 PDF 原文直接以“（$0）”标明 Copilot Studio User License 及其用于构建/管理代理的用途，主语为该 User License，非 M365 Copilot 许可；引文上下文另见“Billing Configuration Per Tenant 1 Capacity Pack 25,000 Copilot Credits per month”，说明用户许可与租户级容量包是分开的两项。
- **c10_2** [supported] 微软官方 Microsoft Learn 页面《Standard harness licensing - Microsoft Copilot Studio》原文称：使用 Copilot Studio 需要以下配置之一，即 Copilot Studio 用户许可（免费），由管理员在 Microsoft 管理中心将其分配给制作者；并注明需先有 Copilot Studio 租户预付费 Copilot Credit 包订阅，才能获得该用户许可。 [ev_0e46d1aecb63917607fc726e](#ev_0e46d1aecb63917607fc726e)（supports）
  依据/推导：vendor_official 官方 Learn 原文直接给出“免费”与获取前提（先有租户预付费容量包订阅）；context_after 明确该前提，表明用户许可本身虽 0 价，但以租户级容量订阅为前置条件。此为许可机制事实，不推断收入。
- **c10_3** [supported] 官方《Copilot Studio 许可指南》原文称：Copilot Credit 消耗在容量包耗尽之前不会计入 pay-as-you-go 计量器。 [ev_376ddd08ecd4747fa61b4b19](#ev_376ddd08ecd4747fa61b4b19)（supports）
  依据/推导：vendor_official 原文直接陈述各计费方式的扣减顺序（容量包先、PAYG 后），可用于界定用户许可与容量包/PAYG 的计费关系；该句主语为 Copilot Credit 消耗，不涉及按用户席位的计价。
- **c10_4** [supported] 微软官方 Copilot Studio 定价页面称：Copilot Studio 以租户级许可方式销售，包含每包 25,000 Copilot Credits 的容量包，标价 200.00 美元/包/月；代理完成的动作或响应按实际用量扣减不同数量 Credits；此外还提供 pay-as-you-go 计量器。 [ev_8a26c7115c3d298fa2df5872](#ev_8a26c7115c3d298fa2df5872)（supports）
  依据/推导：vendor_official 定价页原文直接给出容量包的标价与规格及 PAYG 的存在；该句未提及独立的用户许可条目，故仅支持“容量包+PAYG 为官方定价页所列付费项”，不据此否认用户许可存在。
- **c10_5** [supported] 第三方博客 holgerimbery 称：为构建和管理代理，每个用户需要一个 Copilot Studio User License（无额外费用），并建议租户许可与用户许可一并获取以简化入门。 [ev_1a462d3fb49390770df08970](#ev_1a462d3fb49390770df08970)（supports）
  依据/推导：third_party 来源，表述与官方 PDF 与 Learn 页面方向一致，可作旁证；不能替代厂商正式条款，也不单独用于关闭缺口。
- **c10_6** [supported] 第三方站点 o365hq 称：在其所引 Copilot Studio 页面上，租户容量包标价为每年 2,400 美元一次性预付、2,520 美元/年按月账单或 240 美元/月单月承诺；而用于访问创作工具的独立 Copilot Studio User License 标价为 0 美元。 [ev_e36ef05ec22cde0fe87b0ab1](#ev_e36ef05ec22cde0fe87b0ab1)（supports） [ev_e0a050a8f91feb72529bed19](#ev_e0a050a8f91feb72529bed19)（supports）
  依据/推导：third_party 来源，其中“User License 标价 0 美元”与官方两处原文一致，可作旁证；其容量包三档数字仍属第三方口径，未在本轮官方摘录中出现，故不据此确立价格。

## 推导

- **c1_8** [supported] 由官方事实可推导：Copilot Studio 的主要收费单位是按用量计费的 Copilot Credits（容量包/预付费/PAYG），而非按最终用户席位数；代理面向未获许可用户使用时，消耗从租户集中池中扣除，成本随代理调用量而非用户人数线性变化。 [ev_a18f5996ee251d00634e7981](#ev_a18f5996ee251d00634e7981)（supports） [ev_3d08d4e65e776471cd8e1448](#ev_3d08d4e65e776471cd8e1448)（supports） [ev_25e499216e10d9f4ef563fae](#ev_25e499216e10d9f4ef563fae)（supports）
  依据/推导：以官方 Credits 计费结构为主，第三方说明未获许可用户消耗池的模式作为补充；推导限于计费单位层面，不推断具体金额或收入。
- **c1_9** [supported] 由官方对比表可推导：Microsoft 365 Copilot 的每用户每月 30 美元许可自身包含一定代理用量，与 Copilot Studio 的 Credits 容量包式许可并存，二者可组合采购；但摘录未说明容量包与预付费计划的具体细则，故付费单位两者的对应关系仍待补充官方条款确认。 [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports）
  依据/推导：推导基于表格行，脚注不全，限定额度关系不确定；不能以第三方说法代替官方条款。
- **c2_7** [supported] 综合可推导：本轮证据只支持“M365 Copilot 的 30 美元/用户/月许可含某种随附代理用量，且该权益与已许可用户自身身份绑定、不构成可供未获许可用户共享的容量池”；证据不支持将其理解为覆盖未获许可用户，但覆盖范围（仅本人 vs 是否含租户内共享场景）的正式界定仍缺官方原文。 [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports） [ev_559c66e41ae49989b83bc970](#ev_559c66e41ae49989b83bc970)（supports） [ev_026e2353f40c6d25e51e17a9](#ev_026e2353f40c6d25e51e17a9)（supports） [ev_57dc177d0ab3247a7f29ac8f](#ev_57dc177d0ab3247a7f29ac8f)（supports）
  依据/推导：以官方“含代理用量”字面为锚，叠加两份第三方与一份社区答复的“限本人/不覆盖未许可用户”一致方向；未获许可用户的容量问题是“未被证实”而非“被官方否认”，不做反向断言。
- **c3_7** [supported] 就可确认的边界可推导：M365 Copilot 每用户许可的随附代理用量并非“可任意共享的容量池”，其免费覆盖以“使用者本人持证 + 代理以该持证用户身份认证运行 + 限于员工面向场景 + 受公平使用上限”为条件；代理若由未获许可用户使用，则不满足该身份条件，因而落在随附范围之外，需由租户级 Copilot Studio 计费（容量包/PAYG）承接。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_25868af562dd0d2ed0210605](#ev_25868af562dd0d2ed0210605)（supports） [ev_191520cb2091a0e531ed020b](#ev_191520cb2091a0e531ed020b)（supports） [ev_026e2353f40c6d25e51e17a9](#ev_026e2353f40c6d25e51e17a9)（supports）
  依据/推导：以官方脚注4/5的身份与场景限定为锚，叠加第三方关于“不构成供未获许可用户使用的容量池”的一致表述。推导仅限“是否在随附范围内”，不断言官方是否明文禁止个别未获许可用户交互（该点官方摘录未覆盖，属未证实而非否定）。
- **c3_8** [supported] 关于“随附容量额度是多少”：官方摘录只给出“Included agent usage”标签与脚注编号，脚注4/5 均以“公平使用上限”而非明确数值界定额度；因此无法从本轮官方证据推出一个具体的随附 Copilot Studio 容量数值，只能确认额度受 Fair Usage Limit 约束且官方保留调整权。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports）
  依据/推导：对官方原文作“未载明”的判断，属对证据缺口的推导性陈述，不等于官方否认存在额度；未用第三方的 25,000 Credits/包（那是 Copilot Studio 容量包规格）冒充 M365 Copilot 随附额度。
- **c4_6** [supported] 综合本轮官方 Learn 摘录与官方许可指南脚注可推导：零计费的条件至少包含（a）使用者本人持有 Microsoft 365 Copilot 许可并以该身份运行代理（身份维度，来自许可指南脚注）；（b）使用限于 Copilot Chat、Teams、SharePoint 三个界面与 classic answers、generative answers、Microsoft Graph tenant grounding 等能力（界面与能力维度，来自 Learn 原文）；（c）受公平使用上限约束且微软可调整（来自许可指南脚注）。未获许可用户不在这一身份条件内，因此其使用按逐用户消耗 credits 计量，官方 Learn 摘录本身未给出费率页的计价示例口径。 [ev_95899b6cf40d7a032858ace6](#ev_95899b6cf40d7a032858ace6)（supports） [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_8e4ac1633098e933fbaff23c](#ev_8e4ac1633098e933fbaff23c)（supports） [ev_dab8e0c5567387bd76c1ea4a](#ev_dab8e0c5567387bd76c1ea4a)（supports）
  依据/推导：身份与公平使用条件取自官方许可指南，界面/能力范围取自官方 Learn 页面；示例口径（100 名未许可用户）仅有第三方转述，故推导止于“按未许可用户计费”，不断言具体费率或示例数字为官方原文。
- **c4_7** [mixed] 关于“触发方式”与“是否排除 Computer-Using Agents”：本轮取得的官方 Learn 摘录只限定界面与答案/接地能力，未出现触发方式（如代理流由何种触发器启动）或 CUA 排除条款；触及这两点的只有第三方 Wiki 的转述。因此这两项条件在官方证据中仍属未展开，不能断言官方已确认或已否认。 [ev_fc79abb7521f8b96f6ef5f71](#ev_fc79abb7521f8b96f6ef5f71)（supports） [ev_95899b6cf40d7a032858ace6](#ev_95899b6cf40d7a032858ace6)（contradicts）
  依据/推导：第三方转述声称存在触发与 CUA 条件，而本轮官方 Learn 页面摘录未载明这些条件，构成证据冲突/空缺而非官方否认；按规程保留冲突，标为 mixed，不以假设关闭缺口。
- **c5_7** [supported] 可推导：容量包与预付费计划是两个不同层面的商业机制——容量包是“按包、按月补充、不结转”的经常性订阅容量（官方：200 美元/包/月，25,000 credits/包），预付费计划是“一年期、一次性预付、按档折扣”的承诺用量池（以 1 CCCU = 1 美元 = 100 credits 换算）；因此企业若需求稳定且量大，预付计划在单位成本上具折扣空间，若需求波动则容量包+PAYG 更灵活。 [ev_2b9e141ce0074ba49ee0902f](#ev_2b9e141ce0074ba49ee0902f)（supports） [ev_c3b106414c41ffadca235ae5](#ev_c3b106414c41ffadca235ae5)（supports） [ev_6384dfc393693ccb31745e72](#ev_6384dfc393693ccb31745e72)（supports）
  依据/推导：推导基于两份官方条款的字面机制（时间跨度、付款方式、换算率、不结转），未凭空补出档位金额；档位折扣的具体幅度未获官方摘录证实，故“折扣空间”只作定性表述。
- **c5_8** [supported] 关于 Fair Usage Limit：本轮官方摘录仅能确认该限制作为许可指南对比表中的独立条目存在（脚注编号形式），并对 M365 Copilot 随附代理用量注明“使用受公平使用上限约束、微软保留更新权”；官方摘录未给出预付费计划或容量包在 Fair Usage Limit 下的具体数值阈值、计量口径或超限后果，因此无法从现有官方证据推出任何具体约束条款。 [ev_a00c24a535eaedb78a612de4](#ev_a00c24a535eaedb78a612de4)（supports） [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports）
  依据/推导：前段为官方表格字面（该条目仅指 M365 Copilot 随附用量，不能外推为容量包/预付计划的价格条款）。对“未载明”的判断属证据缺口陈述，不等于官方否认存在具体条款。
- **c6_9** [supported] 综合官方脚注与第三方/社区一致方向可推导：M365 Copilot 随附代理用量并非可供未获许可用户共享的容量池，其免费覆盖以“使用者本人持 M365 Copilot 许可 + 代理以该持证用户认证身份运行 + 员工面向场景 + 受公平使用上限”为条件；未获许可用户使用代理不满足该身份条件，因而不在随附范围内，须由租户级 Copilot Studio 计费（容量包或 PAYG）承接。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_25868af562dd0d2ed0210605](#ev_25868af562dd0d2ed0210605)（supports） [ev_026e2353f40c6d25e51e17a9](#ev_026e2353f40c6d25e51e17a9)（supports） [ev_57dc177d0ab3247a7f29ac8f](#ev_57dc177d0ab3247a7f29ac8f)（supports）
  依据/推导：以官方脚注的身份与场景限定为锚，叠加两份第三方与一份社区答复方向一致的表述。推导止于“是否在随附范围内”；官方摘录未逐字写出“仅限本人、未获许可用户不得使用随附用量”的禁止性措辞，故该禁止性表述仍属未获官方明文证实而非官方否认。
- **c6_10** [mixed] 关于本轮问题的直接答案边界：现有官方证据可确认随附权益绑定“已许可用户，以该用户身份运行”这一条件，但未能提供官方原文逐字规定“未获许可用户不得通过随附用量访问代理、须由租户级 Credits 计费承接”的禁止/强制计费条款；该禁止性规定目前只有第三方与社区答复支撑，且官方指南自述不取代 Product Terms，因此该缺口尚不能以官方条款关闭。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_ebc24156510a771ef0b63cea](#ev_ebc24156510a771ef0b63cea)（supports） [ev_fc79abb7521f8b96f6ef5f71](#ev_fc79abb7521f8b96f6ef5f71)（contradicts）
  依据/推导：对证据状态的判断：官方脚注给出身份条件（支持“限本人”方向），但未出现禁止未获许可用户使用随附用量或强制租户级计费的明文；LICENSEWARE 转述 Learn 费率页声称存在该计费口径，本轮未取得该页原文，构成待补的官方原文缺口，保留不关闭。
- **c7_7** [supported] 由官方原文可确认的零计费条件至少包括：（a）身份——使用者本人持有 Microsoft 365 Copilot 许可，代理以该已许可用户身份运行（许可指南脚注4）；（b）界面——限于 Copilot Chat、Microsoft Teams、SharePoint；（c）能力范围——限于 classic answers、generative answers、Microsoft Graph tenant grounding 三类（Learn 页面）；（d）公平使用——受 fair usage limits 约束且微软可更新上限（许可指南脚注4）。 [ev_95899b6cf40d7a032858ace6](#ev_95899b6cf40d7a032858ace6)（supports） [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_25868af562dd0d2ed0210605](#ev_25868af562dd0d2ed0210605)（supports）
  依据/推导：身份与公平使用取自官方许可指南脚注，界面与能力范围取自官方 Learn 页面，两处均为 vendor_official；这是把两份官方资料拼合的推导，不引入第三方内容。
- **c7_8** [mixed] 关于“触发方式”与“是否排除 Computer-Using Agents”：本轮取得的官方 Learn 摘录与官方许可指南摘录均未出现触发器类型（如代理流由“When an agent calls the flow”启动）或 CUA 排除条款；触及这两点的只有第三方 Wiki 转述。因此这两项条件在官方证据中仍属未展开，既不能断言官方已确认，也不能断言官方已否认。 [ev_b0013918677d3356944c0895](#ev_b0013918677d3356944c0895)（supports） [ev_95899b6cf40d7a032858ace6](#ev_95899b6cf40d7a032858ace6)（contradicts）
  依据/推导：第三方转述声称存在触发与 CUA 条件，而两份官方摘录均未载明；按规程保留冲突并标为 mixed，不以假设关闭。
- **c7_9** [mixed] 关于“未获许可用户逐用户计费及示例”：官方 Learn 摘录只给出“已许可用户零计费”的正面规则，未出现未获许可用户的计费口径；官方许可指南脚注4/5以“已许可用户身份”为随附条件，未获许可用户不满足该身份条件，因此不在随附范围之内，需由租户级 Copilot Studio 计费（容量包或 PAYG）承接。至于“逐用户计量”的示例（100 名未许可用户与 50 名已许可用户的对比），本轮仅有第三方 Wiki 转述，未取得官方原文数字。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_25868af562dd0d2ed0210605](#ev_25868af562dd0d2ed0210605)（supports） [ev_0a1f12af93d3fbc02f823ca5](#ev_0a1f12af93d3fbc02f823ca5)（supports） [ev_95899b6cf40d7a032858ace6](#ev_95899b6cf40d7a032858ace6)（contradicts）
  依据/推导：“不在随附范围内”由官方身份条件推导；但官方摘录未载明未许可用户的计费示例与逐用户计量口径，且第三方声称 Learn 费率页有该示例，构成待补的官方原文缺口，故整体标为 mixed，不据此关闭缺口。
- **c8_6** [supported] 由官方档位表可推导最低承诺门槛：预付费计划最低档为 3,000 CCCU（＝300,000 Credits，标价 2,850 美元，5% 折扣），最高档为 3,000,000 CCCU（＝300,000,000 Credits，标价 2,400,000 美元，20% 折扣）；折扣率随承诺量单调上升，相当于承诺金额约 95% 至 80% 的名义价值。此为按官方表内数字的换算，非实际成交价或收入。 [ev_56dfd86c47ac3d6e08df5b62](#ev_56dfd86c47ac3d6e08df5b62)（supports） [ev_a3b65c2ec57e21989f91c97b](#ev_a3b65c2ec57e21989f91c97b)（supports） [ev_4b959f26c83df458f524be40](#ev_4b959f26c83df458f524be40)（supports）
  依据/推导：推导全部基于两份官方 PDF 的表内数字与 CCCU=1 美元=100 Credits 的官方换算；仅对“档位门槛与折扣梯度”作推导，不外推为收入、利润或客户实际支付意愿。
- **c9_6** [supported] 由两份官方原文可推导：官方定价页与官方许可指南（2026年10月版）的 200.00 美元/包/月 是同一标价，区别仅在页面未写计费周期、指南写明“按年计费”；若按年计费，200×12＝2,400 美元/包/年，与第三方 o365hq 的“2,400 美元/年预付”数字在算术上一致。 [ev_82638d6dd87bf3b75ec2fb8e](#ev_82638d6dd87bf3b75ec2fb8e)（supports） [ev_abf7951d9d970f459397f5ec](#ev_abf7951d9d970f459397f5ec)（supports） [ev_e0a050a8f91feb72529bed19](#ev_e0a050a8f91feb72529bed19)（supports）
  依据/推导：推导为算术换算与原文对照：200 美元/月×12 的乘法不依赖第三方，第三方仅提供“2,400/年”这一表述的对照；不能由此推出 2,520/年或 240/月 也是官方同页内容。
- **c9_7** [mixed] 关于 2,520 美元/年（月付）与 240 美元/月（单月承诺）：本轮官方证据中没有任何官方页面或条款摘录出现这两个数字，因此无法确认它们属于“官方同页不同呈现”；从结构上看，2,400/2,520/240 恰好构成“预付折扣—按年分摊月付溢价—单月承诺含溢价”的常见三档形态，但这是对第三方口径的模式识别，而非官方证据。 [ev_e0a050a8f91feb72529bed19](#ev_e0a050a8f91feb72529bed19)（supports） [ev_82638d6dd87bf3b75ec2fb8e](#ev_82638d6dd87bf3b75ec2fb8e)（contradicts）
  依据/推导：第三方提出三档口径，本轮取得的官方定价页与许可指南摘录只出现 200/包/月（及“billed annually”），未见 2,520 或 240，构成缺口而非官方否定；按规程保留冲突并标为 mixed。
- **c9_8** [unverified] 关于第三方 LICENSEWARE 的 20.00 美元/包/月 口径：本轮取得的该 Wiki 摘录在“20.00 per pack”前后被截断（紧接为“[11] Packs can also fund Copilot Chat through Copilot credit policies, up to 10 per tenant.”），既未显示所在列名，也未显示单位周期，因此不能确认它指容量包标价，更不能与官方的 200 美元/包/月直接对照判定为“更低标价”或“折扣层级”。 [ev_66568c743ae007c496b4533f](#ev_66568c743ae007c496b4533f)（supports） [ev_82638d6dd87bf3b75ec2fb8e](#ev_82638d6dd87bf3b75ec2fb8e)（contradicts）
  依据/推导：该 Wiki 同段摘要另称容量包为“25,000 Copilot Credits per pack per month”但未在该摘录中给出 $200；20.00 的小数格式与官方 200.00 不同，可能是其他计量单位（如按 Credits 或按其他参数）或截断导致的误读，属待验证而非事实。
- **c9_9** [mixed] 综合判断：现有官方证据支持“官方定价页的 $200.00/包/月 与官方许可指南的 $200/包/月（按年计费）是同一标价”，并支持 2,400 美元/年可作为该标价的年度算术结果；但官方摘录中未出现月付溢价 2,520 美元/年、单月承诺 240 美元/月或 20.00 美元/包/月 的任何原文，因此“这些第三方口径是否属于官方同页的不同承诺周期或折扣层级”仍无官方证据可判。 [ev_82638d6dd87bf3b75ec2fb8e](#ev_82638d6dd87bf3b75ec2fb8e)（supports） [ev_abf7951d9d970f459397f5ec](#ev_abf7951d9d970f459397f5ec)（supports） [ev_e0a050a8f91feb72529bed19](#ev_e0a050a8f91feb72529bed19)（contradicts）
  依据/推导：前半由两份官方原文支撑（同一 200 美元标价、按年计费）；后半为对缺口的判断，第三方三档口径未被官方确认也未被官方否认，故整体标 mixed，不以假设关闭缺口。
- **c10_7** [supported] 由官方原文可推导：Copilot Studio User License 是独立于 Credits 计费之外的一项“按制作者、0 标价”的访问许可，它本身不附带可用容量；实际代理运行与交互的计量仍由 Copilot Credits 承担，其获取渠道为租户级容量包（25,000 Credits/包/月，官方标价 200.00 美元/包/月）、Copilot Credit 预付费计划或 pay-as-you-go 计量器。 [ev_414550a10cb2870ee7771428](#ev_414550a10cb2870ee7771428)（supports） [ev_0e46d1aecb63917607fc726e](#ev_0e46d1aecb63917607fc726e)（supports） [ev_8a26c7115c3d298fa2df5872](#ev_8a26c7115c3d298fa2df5872)（supports） [ev_74051b80b3a8d2af897e5dd6](#ev_74051b80b3a8d2af897e5dd6)（supports）
  依据/推导：用户许可的存在与 0 价来自两份 vendor_official 原文；Credits 作为通用计价货币及三种获取渠道来自官方许可指南原文。推导仅限结构关系（谁免费、谁按量计费），不推断客户实际支出规模或微软收入。
- **c10_8** [supported] 关于计费顺序可推导：由于官方明确 Credits 消耗在容量包耗尽前不计入 PAYG，且建议将租户许可与用户许可同一笔交易获取，因此 0 价用户许可的“免费”是指创作工具的访问不单独计费，而非代理运行免费；代理运行先由已购容量包扣减、超出后转 PAYG，预付费计划则为一年期预付池，机制上与前两者并列。 [ev_376ddd08ecd4747fa61b4b19](#ev_376ddd08ecd4747fa61b4b19)（supports） [ev_414550a10cb2870ee7771428](#ev_414550a10cb2870ee7771428)（supports） [ev_0e46d1aecb63917607fc726e](#ev_0e46d1aecb63917607fc726e)（supports）
  依据/推导：扣减顺序与同笔交易建议均出自官方原文；预付费计划并列关系引自此前已校验的官方许可指南（ev_a18f5996ee251d00634e7981）。推导不平移为容量额度数值，也不涉及 M365 Copilot 随附用量。

## 商业判断

- **c1_10** [supported] 从扩展使用看，按 Credits 用量计费使 Copilot Studio 的低频/试点部署门槛较低（PAYG 无前期承诺），但高频代理规模化后成本随消耗增长、且公平使用限制可能约束无限用量预期；M365 Copilot 的每用户 30 美元则把成本绑定到席位规模并附带代理用量，适合先按人铺开。对企业客户意味着“按人”与“按调用量”并行的成本结构，需分场景选择。 [ev_471052c0e61e2ff67d379148](#ev_471052c0e61e2ff67d379148)（supports） [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports）
  依据/推导：商业判断，基于官方计费模式事实；未使用标价推算收入或利润，公平使用限制细节未在本轮摘录中展开。
- **c2_8** [mixed] 若随附用量确按“许可用户本人身份”运行，则企业扩展代理到未获许可用户时，实际增量成本主要落在租户级 Copilot Studio 计费（Credits 容量包或 PAYG）上，而非增购 M365 Copilot 席位；这会降低“按人铺开 M365 Copilot”对大规模非员工使用场景的覆盖价值，企业更可能采取“员工席位 + 租户级容量”的组合。 [ev_026e2353f40c6d25e51e17a9](#ev_026e2353f40c6d25e51e17a9)（supports） [ev_57dc177d0ab3247a7f29ac8f](#ev_57dc177d0ab3247a7f29ac8f)（supports） [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（contradicts）
  依据/推导：商业判断，依据第三方与社区答复的方向；官方 PDF 仅给“Included agent usage”标签而未界定边界，构成未闭合的冲突点，故标为 mixed；不据此推算收入或利润。
- **c3_9** [supported] 对客户扩展与微软收入的含义：若随附权益按“已许可用户身份 + 公平使用”封顶，则企业把代理扩展到呼叫中心、外部合作方等未获许可人群时，增量支出落在租户级 Credits（容量包或 PAYG）而非增购 M365 Copilot 席位；这会把上述规模场景的价值捕获从“按席位”转向“按用量”，并使公平使用的模糊上限成为客户做容量规划时必须预留余量的风险项。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_af5185b58ee678d3e7aef6e4](#ev_af5185b58ee678d3e7aef6e4)（supports）
  依据/推导：商业判断，基于官方身份/公平使用限定与第三方“未获许可用户消耗 credits”的方向；不把标价当作已实现收入或利润，公平使用具体阈值未证实。
- **c4_8** [supported] 对扩展使用与收入来源的含义：由于零计费被限定在“已许可用户身份 + 指定界面与答案类型 + 公平使用”，企业把代理开放给未获许可人群（如一线外部用户）时，容量支出落在租户级 Copilot Studio 计费（容量包或 PAYG）而非增购席位；这使得客户端成本会随未许可用户规模上升，并让公平使用的模糊上限成为容量规划需留余量的风险项。该判断只涉计费结构，不涉及已实现收入或利润。 [ev_95899b6cf40d7a032858ace6](#ev_95899b6cf40d7a032858ace6)（supports） [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_8e4ac1633098e933fbaff23c](#ev_8e4ac1633098e933fbaff23c)（supports）
  依据/推导：商业判断，基于官方身份/界面/公平使用限定与第三方对未许可用户消耗 credits 的一致方向；未把标价当作收入或利润，公平使用阈值未证实。
- **c5_9** [supported] 对客户扩展使用与微软收入来源的含义：由于容量包按月补充且不结转，用量估算偏高会造成已购容量浪费、偏低则溢出到 PAYG；预付费计划以一年期承诺换取档位折扣，把支出前置为承诺。这使企业在扩容时需在“承诺折扣/预付现金流”与“按月弹性/潜在超支”之间权衡，而微软则同时获得订阅式经常性收入（容量包）与预付承诺现金流（预付计划）两类来源；此为计费结构层面的判断，不等同于已实现收入或利润。 [ev_c3b106414c41ffadca235ae5](#ev_c3b106414c41ffadca235ae5)（supports） [ev_6384dfc393693ccb31745e72](#ev_6384dfc393693ccb31745e72)（supports）
  依据/推导：商业判断，仅以官方机制事实（不结转、按月、一年期预付、按档折扣）为依据；不引用任何标价推算收入规模或利润率。
- **c7_10** [supported] 对扩展使用与收入结构的含义：零计费被同时限定在“已许可用户本人身份 + 三个指定界面 + 三类答案/接地能力 + 公平使用上限”之内，企业把代理开放给未获许可人群时，容量支出会转向租户级 Copilot Studio 计费（容量包或 PAYG）而非增购席位；同时公平使用上限不透明，会迫使客户在容量规划中预留余量。该判断仅涉计费结构，不涉及已实现收入或利润。 [ev_95899b6cf40d7a032858ace6](#ev_95899b6cf40d7a032858ace6)（supports） [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_0a1f12af93d3fbc02f823ca5](#ev_0a1f12af93d3fbc02f823ca5)（supports）
  依据/推导：商业判断，基于官方身份/界面/能力/公平使用四项限定；未把标价当作收入或利润，公平使用阈值未证实，第三方对未许可用户计费的描述仅作方向印证。
- **c8_9** [supported] 就本轮 q8 的具体问题而言，官方许可指南的档位表已同时给出各档 CCCU 区间、承诺金额、折扣率/折后价、最低门槛（3,000 CCCU）、一年有效期与未用额度期末失效规则，因此“档位明细”这一层已由官方原文覆盖；尚缺的是微软订购/定价页面上的实际下单口径（例如各档是否可拆分、按年计费的具体出账方式、不同协议/项目下的价格差异），这会使客户在换算实际采购价时仍需与微软或合作伙伴确认。 [ev_56dfd86c47ac3d6e08df5b62](#ev_56dfd86c47ac3d6e08df5b62)（supports） [ev_a3b65c2ec57e21989f91c97b](#ev_a3b65c2ec57e21989f91c97b)（supports） [ev_2eee67abb8bb61271fd0bc66](#ev_2eee67abb8bb61271fd0bc66)（supports）
  依据/推导：商业判断，基于官方档位表与有效期条款的字面覆盖范围；未把承诺标价当作收入或利润，也明确指出订购页面口径未在本轮取得。
- **c9_10** [supported] 对企业采购的含义：若官方确实以“200 美元/包/月、按年计费”为基准，则年付 2,400 美元/包可视为基准清单价；月付溢价与单月承诺若存在，等于对短期弹性的加价，会抬高试点期（用量不稳定、不愿年度承诺）客户的单位成本，并促使其在短期试用时转向 pay-as-you-go 而非容量包。此为计费结构判断，不涉及已实现收入或利润。 [ev_82638d6dd87bf3b75ec2fb8e](#ev_82638d6dd87bf3b75ec2fb8e)（supports） [ev_e0a050a8f91feb72529bed19](#ev_e0a050a8f91feb72529bed19)（supports） [ev_f4a973b7dc16323e83c460c3](#ev_f4a973b7dc16323e83c460c3)（supports）
  依据/推导：商业判断，基于官方 200 美元/包/月与按年计费事实、官方建议的 PAYG 作为额外容量连续性方案；月付溢价的具体数字仅有第三方口径，故以“若存在”条件化表述，不把标价当作收入。
- **c10_9** [supported] 对客户扩展使用与微软收入结构的含义：0 标价用户许可降低了“让更多制作者进入 Copilot Studio 开发”的进入门槛，但真正的成本随代理运行用量增长，需买容量包、预付费池或挂 PAYG，因而企业的支出曲线取决于代理调用规模而非制作者人数；对微软而言这使得 Copilot Studio 侧的收入主要来自按用量的容量与计量，而制作者席位本身不构成收入项。此为计费结构判断，不涉及已实现收入或利润。 [ev_414550a10cb2870ee7771428](#ev_414550a10cb2870ee7771428)（supports） [ev_8a26c7115c3d298fa2df5872](#ev_8a26c7115c3d298fa2df5872)（supports） [ev_376ddd08ecd4747fa61b4b19](#ev_376ddd08ecd4747fa61b4b19)（supports）
  依据/推导：商业判断，基于官方“用户许可 0 价+容量包 200 美元/包/月+PAYG 兜底”的计费结构；未把标价当作收入或利润，也未据第三方容量包三档口径作数量化推算。

## 待验证假设

- **c1_11** [unverified] 假设：多数企业会以 M365 Copilot 席位覆盖内部员工、再用 Copilot Studio Credits（容量包或 PAYG）承接面向外部未许可用户的代理场景，从而形成“席位+用量”双层支出；这一采购组合对微软收入的相对贡献仍有待验证。 [ev_25e499216e10d9f4ef563fae](#ev_25e499216e10d9f4ef563fae)（supports）
  依据/推导：基于第三方对未许可用户需另购 capacity 的描述提出待验证假设，不能作为结论，也不用于关闭缺口。
- **c2_9** [unverified] 假设：微软对“随附代理用量”的正式条款会以公平使用上限与已许可用户身份为约束，且未获许可用户规模使用必须由租户级 Copilot Studio 计费承接，从而使该部分收入从“按席位”转向“按用量”。 [ev_559c66e41ae49989b83bc970](#ev_559c66e41ae49989b83bc970)（supports）
  依据/推导：基于第三方对公平使用的描述提出，尚待官方条款确认；不作为结论，也不用于关闭缺口。
- **c3_10** [unverified] 假设：微软在正式产品条款中会以“公平使用上限为动态、不公开数值”的方式维持随附额度，且将未获许可用户访问统一定义为必须由租户级计费承接；若未来条款允许一定比例的未获许可用户交互共享随附用量，则上述“席位+容量”双层结构的收入含义需重新评估。 [ev_191520cb2091a0e531ed020b](#ev_191520cb2091a0e531ed020b)（supports）
  依据/推导：待验证假设，仅由第三方表述支撑，不能作为结论，也不用于关闭缺口。
- **c4_9** [unverified] 假设：Microsoft Learn 费率页原文以脚注或示例形式列明触发方式限制、Computer-Using Agents 排除，以及未获许可用户逐用户计费示例；若这些条件被官方确认，则企业可据此把部分代理交互稳定归入零计费，从而降低对租户级 Credits 的依赖。 [ev_fc79abb7521f8b96f6ef5f71](#ev_fc79abb7521f8b96f6ef5f71)（supports）
  依据/推导：待验证假设，仅由第三方转述支撑，不作为结论，也不用于关闭缺口。
- **c5_10** [unverified] 假设：LICENSEWARE 所述的 20.00 美元/包/月与 o365hq 所述的 2,400/2,520/240 美元口径，可能对应不同的计费周期、折扣或促销层级（例如年度承诺与单月承诺之差），而非与官方 200 美元/包/月直接矛盾；需以官方预付费计划档位表与容量包订购页原文核实后确认。 [ev_913bc5f4729001583f2fa939](#ev_913bc5f4729001583f2fa939)（supports） [ev_e0a050a8f91feb72529bed19](#ev_e0a050a8f91feb72529bed19)（supports）
  依据/推导：仅为解释第三方价格差异的待验证假设，不作为结论，也不用于关闭缺口。
- **c7_11** [unverified] 假设：Microsoft Learn 费率页（requirements-messages-management 或 billing-licensing）原文的脚注确会列明触发方式限制（如仅“When an agent calls the flow”启动的代理流）、Computer-Using Agents 排除，以及未获许可用户逐用户计费的示例数字；若被官方确认，企业可据此把部分代理交互稳定归入零计费。 [ev_b0013918677d3356944c0895](#ev_b0013918677d3356944c0895)（supports） [ev_0a1f12af93d3fbc02f823ca5](#ev_0a1f12af93d3fbc02f823ca5)（supports）
  依据/推导：仅由第三方转述支撑的待验证假设，不作为结论，也不用于关闭缺口。
- **c9_11** [unverified] 假设：o365hq 所称的 2,400 美元/年预付、2,520 美元/年按月账单、240 美元/月单月承诺，可能分别对应官方订购页在“年度承诺预付 / 年度承诺月付 / 月度承诺”下的展示口径（体现预付折扣与月付溢价），而 LICENSEWARE 的 20.00 美元/包/月 可能是摘录截断或不同计量口径所致。该假设需以官方 Copilot Studio 订购页原文核实。 [ev_e0a050a8f91feb72529bed19](#ev_e0a050a8f91feb72529bed19)（supports） [ev_913bc5f4729001583f2fa939](#ev_913bc5f4729001583f2fa939)（supports）
  依据/推导：待验证假设，仅由第三方与截断摘录支撑，不作为结论，也不用于关闭缺口。
- **c10_10** [unverified] 假设：官方订购页会把 Copilot Studio User License 作为与租户容量包并列的 0 价 SKU 列出，且实际下单时用户许可必须依附于某个租户容量订阅（或预付费/PAYG 计费前提），因此“免费”在采购流程中体现为零金额行项而非可独立下单的免费产品；该细节仍需官方订购页或产品条款原文核实。 [ev_0e46d1aecb63917607fc726e](#ev_0e46d1aecb63917607fc726e)（supports）
  依据/推导：待验证假设，仅由 Learn 页面“需先有租户预付费容量包订阅才能获得该用户许可”一句支撑其前置关系；不作为结论，也不用于关闭缺口。

## 证据缺口

- gap0 [open] Microsoft 365 Copilot 与 Copilot Studio 面向的企业使用者、收费单位和购买前提有何区别？这些差异可能如何影响企业客户扩展使用和微软的收入来源？优先使用官方资料；将价格与许可事实、基于事实的推导、商业判断和仍待验证假设明确区分，不把产品定价直接当成已实现收入或利润。
- gap1 [open] 需要微软官方文档明确 Copilot Studio 各购买路径（capacity pack、pre-purchase plan、pay-as-you-go）在容量包与预付费计划的档位/价格、以及 Fair Usage Limit 的具体约束条款；本轮官方摘录仅有表格脚注引用未展开，无法确认付费单位细则。
- gap2 [resolved] 需要官方条款确认 Copilot Studio User License（创作工具访问）是否存在及其是否标价 0，以及与 Copilot Credits 容量的关系；本轮仅第三方提及，官方摘录未覆盖。
  模型评估关闭：gap2 的三项要求均已由官方原文覆盖：存在性（官方许可指南 ev_414550a10cb2870ee7771428 与 Learn 页面 ev_0e46d1aecb63917607fc726e 均陈述 Copilot Studio User License 用于构建/管理代理的制作者）；标价为 0（前者写明“（$0）”，后者写明“free of charge”）；与 Copilot Credits 计费的关系（用户许可本身不附带容量，代理运行消耗 Copilot Credits，获取方式为容量包、预付费计划或 PAYG；容量包耗尽前不计入 PAYG，ev_376ddd08ecd4747fa61b4b19）。故以 c10_1、c10_2、c10_7、c10_8 关闭。限制：本轮官方证据未给出 Copilot Studio User License 与 M365 Copilot 随附用量之间的关联条款，也未在官方订购页面上展示该 0 价行项与下单前置条件，后者作为同一 topic 的新缺口保持开放；第三方 o365hq 与 holgerimbery 的 0 价表述仅作旁证。；依据结论：c10_1, c10_2, c10_7, c10_8
- gap3 [open] 需要微软官方许可指南或产品条款原文展开“Included agent usage”对应的脚注，明确 M365 Copilot 每用户许可随附的 Copilot Studio 容量额度、使用身份限制（是否仅限该许可用户本人运行代理），以及是否允许未获许可用户通过该随附用量访问代理。本轮官方摘录仅有表格标签与脚注编号，边界由第三方与社区答复补充，不能单独关闭。
- gap4 [open] LICENSEWARE Wiki 引用的 Microsoft Learn 计费/费率页（learn.microsoft.com）原文未取得：需该页面确认“M365 Copilot 许可在 Copilot Chat、Teams、SharePoint 中使用代理不计入容量包或计量器”的条件清单（身份、触发方式、公平使用、是否排除 Computer-Using Agents）及未获许可用户逐用户计费的示例口径。
- gap5 [open] 需要微软官方原文列出 Copilot Credit Pre-Purchase Plan 的各档位（CCCU 数量区间/承诺金额）与对应折扣率或折后单价，以及最低承诺门槛、有效期与未用尽 CCCU 的处理规则；本轮官方摘录仅称“依档位”“一年期、预付、按档折扣”，未给出档位明细。
- gap6 [open] 需要微软官方订购/定价页面原文核实容量包的实际计价口径（200 美元/包/月按年计费是否对应 2,400 美元/年，是否存在 240 美元/月单月承诺价或 20.00 美元/包月的其他口径），以解释官方许可指南与第三方来源之间的价格不一致。
- gap7 [open] 需取得 LICENSEWARE Wiki 所引用的“20.00 per pack”条款的完整上下文或其所引微软官方原文，确认该 20.00 美元口径的计量对象与周期（是容量包单价的其他呈现、按 Credits 计的单位费率，还是检索摘录被截断导致的误读）；本轮该 Wiki 摘录在“20.00 per pack”前后被截断，无法判断其含义。

## 问题与检索记录

- q0 / 第 0 轮 / 缺口 初始问题：Microsoft 365 Copilot 与 Copilot Studio 面向的企业使用者、收费单位和购买前提有何区别？这些差异可能如何影响企业客户扩展使用和微软的收入来源？优先使用官方资料；将价格与许可事实、基于事实的推导、商业判断和仍待验证假设明确区分，不把产品定价直接当成已实现收入或利润。
- q1 / 第 1 轮 / 缺口 gap0：Copilot Studio 的官方许可与计费单位是什么？例如按“消息包/容量”（messages、Copilot Credits 或容量包）计费与按席位计费分别适用于哪些使用场景，购买前提有哪些？
- q2 / 第 2 轮 / 缺口 gap0：微软官方如何定义 Microsoft 365 Copilot 许可（每用户每月 30 美元）所附带、可用于 Copilot Studio 代理的容量权益及其边界（是否仅限该用户自身使用、是否覆盖未获许可用户）？
  Tavily search1：Microsoft 365 Copilot licensing guide agent usage；结果 5；错误 无
- q3 / 第 3 轮 / 缺口 gap3：微软官方许可文档（Copilot Studio Licensing Guide 或 Product Terms）如何界定 Microsoft 365 Copilot 每用户许可中“Included agent usage”的具体范围：随附的 Copilot Studio 容量额度是多少、是否仅限该持证用户本人运行代理使用、以及未获许可用户通过该随附用量访问代理是否被允许？
  Tavily search2：Microsoft 365 Copilot included agent usage Copilot Studio credits；结果 5；错误 无
- q4 / 第 4 轮 / 缺口 gap4：微软官方 Microsoft Learn 计费/费率页（billing rates and management 或 requirements-messages-management）如何规定：持有 Microsoft 365 Copilot 许可的用户在 Copilot Chat、Teams、SharePoint 中使用 Copilot Studio 代理时不计入容量包或计量的具体条件（身份、触发方式、公平使用限制、是否排除 Computer-Using Agents），以及对未获许可用户的逐用户计费口径？
  Tavily search3：Copilot Studio billing rates M365 Copilot agents；结果 5；错误 无
- q5 / 第 5 轮 / 缺口 gap1：微软官方 Copilot Studio 定价或计费文档中，Copilot Credit 容量包（capacity pack）与预付费计划（Pre-Purchase Plan）各自的档位与价格是多少，对应的 Fair Usage Limit 条款又作了哪些具体约束？
- q6 / 第 6 轮 / 缺口 gap3：微软官方 Microsoft 365 Copilot 许可文档（Product Terms 或 Copilot Studio 许可指南的“Included agent usage”脚注1完整定义）是否明确规定：随附的 Copilot Studio 代理用量只能由持证用户本人以自己身份运行，未获许可用户不得通过该随附用量访问代理、须由租户级 Credits 计费承接？
- q7 / 第 7 轮 / 缺口 gap4：Microsoft Learn 的 Copilot Studio 计费/费率页（requirements-messages-management 或 billing-licensing）对“持 Microsoft 365 Copilot 许可的用户在 Copilot Chat、Teams、SharePoint 中使用代理不计入容量包或计量器”给出了哪些具体条件（身份界定、触发方式、公平使用限制、是否排除 Computer-Using Agents），以及对未获许可用户如何按逐用户口径计费并给出示例？
  Tavily search4：Microsoft Learn Copilot Studio billing licensing metering agents；结果 5；错误 无
- q8 / 第 8 轮 / 缺口 gap5：微软官方的预付费计划（Copilot Credit Pre-Purchase Plan）定价或订购页面是否列出了各档位（tier）的具体承诺金额或 CCCU 数量区间、对应的折扣率或折后单价，以及最低承诺门槛、有效期限和未用尽 CCCU 的处理规则？
- q9 / 第 9 轮 / 缺口 gap6：微软官方 Copilot Studio 订购/定价页面如何标示容量包（Copilot Credit capacity pack）的计价周期？2,400 美元/年、240 美元/月与 20.00 美元/包/月这些第三方口径，与官方许可指南“200 美元/包/月（按年计费）”是同一标价的不同呈现，还是不同承诺周期或折扣层级的差异？
- q10 / 第 10 轮 / 缺口 gap2：微软官方许可指南或 Copilot Studio 定价/许可页面是否载有一项独立的 Copilot Studio User License（用于访问 Copilot Studio 创作工具），其标价是否为 0，以及它与 Copilot Credits 容量包/预付费计划/按需计费在计费关系上如何界定？

## 原文摘录与追溯

<a id="ev_74051b80b3a8d2af897e5dd6"></a>
### ev_74051b80b3a8d2af897e5dd6

> As users interact with Copilot Studio agents, or agents perform tasks on behalf of users, they consume Copilot Credits. Copilot Credits are the common currency across Copilot Studio capabilities and are available via the Microsoft Copilot Studio pay-as-you-go meter, the Microsoft Copilot Studio license (i.e., Copilot Credit capacity pack) and the

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q1 → 分块 chk_c68aacefe8ad1e6fd48eeabb_3571 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [3821, 4169)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_a18f5996ee251d00634e7981"></a>
### ev_a18f5996ee251d00634e7981

> Copilot Credits are offered through the Microsoft Copilot Studio pay-as-you-go meter, the Microsoft Copilot Studio license (i.e., Copilot Credit capacity pack) and the Copilot Credit Pre-Purchase Plan.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q1 → 分块 chk_c68aacefe8ad1e6fd48eeabb_7650 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [7661, 7862)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_471052c0e61e2ff67d379148"></a>
### ev_471052c0e61e2ff67d379148

> The Copilot Studio pay-as-you-go meter enables organizations to postpay based on the actual number of Copilot Credits consumed by agents in a billing month. No up-front license commitment is required, allowing organizations to scale usage and ensure business continuity for critical business processes with flexibility, scalability, season

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q1 → 分块 chk_c68aacefe8ad1e6fd48eeabb_7650 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [7911, 8250)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_3d08d4e65e776471cd8e1448"></a>
### ev_3d08d4e65e776471cd8e1448

> Copilot Studio is sold as tenant-wide license which includes Copilot Credit capacity packs of 25,000 Copilot Credits each, priced at $200.00 /pack/month. Whenever an action or response is completed by an agent, a varying number of Copilot Credits will be billed depending on the specific usage. Copilot Studio is also available as a pay-as-you-go meter in addition to the existing Copilot Credit capacity packs.

来源：Microsoft Copilot Studio Plans and Pricing — https://www.microsoft.com/en-us/copilot/pricing/copilot-studio

类型：web；读取时间：2026-10-19T08:23:18.966505+00:00；截断：False

问题 q1 → 分块 chk_0974f6cd66d2bc4ca55c8219_6631 → 来源 src_0974f6cd66d2bc4ca55c8219；清洗后字符 [6748, 7159)

SHA-256：`5c2c49105b6ac9c095aedd95af5f2f3133be5bf6bb7d17561ab15184a704fb32`；范围：<main> element; characters 0-8971 of 8971

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.microsoft.com/en-us/copilot/pricing/copilot-studio
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_5a440717841727e42686e122"></a>
### ev_5a440717841727e42686e122

> Microsoft 365 Copilot $30 per user/month Included agent usage1 Pay-as-you-go: unlimited2 License (capacity pack): 25,000 Copilot Credit /pack3 Pre

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q1 → 分块 chk_c68aacefe8ad1e6fd48eeabb_13260 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [13714, 13860)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_cd190fc6dc77296711cbd2ff"></a>
### ev_cd190fc6dc77296711cbd2ff

> Your personal M365 Copilot license covers your creation and use, but not the consumption of others who are accessing premium, tenant-grounded data.

来源：Copilot Agents licensing usage update – CIAOPS — https://blog.ciaops.com/2025/12/01/copilot-agents-licensing-usage-update/

类型：web；读取时间：2026-10-19T08:44:11.506662+00:00；截断：False

问题 q1 → 分块 chk_55bc3f900451bb732ad9f33f_3570 → 来源 src_55bc3f900451bb732ad9f33f；清洗后字符 [3685, 3832)

SHA-256：`aff02aa8d8069060cf183230347eebfb4c2b1964a6d577db976f6d7503cefd78`；范围：<main> element; characters 0-8495 of 8495

获取链：运行 c498744f19ea → 问题 q1 → 搜索 search1 → https://blog.ciaops.com/2025/12/01/copilot-agents-licensing-usage-update
检索词：Copilot Studio licensing messages capacity pack；当时的问题：微软官方如何说明 Copilot Studio 的计费单位与购买前提（例如按消息/容量包计费所需的 Azure 订阅或租户前提），与 Microsoft 365 Copilot 按用户席位收费的模式相比有何不同？

<a id="ev_25e499216e10d9f4ef563fae"></a>
### ev_25e499216e10d9f4ef563fae

> To enable the unlicensed users to chat with your agent, the tenant administrator must set up one of the following Copilot Studio subscriptions : Copilot Studio Message Pack (Pre-paid Capacity): Purchase packs of Copilot Credits (e.g., 25,000 credits per pack/month). The unlicensed users’ interactions are consumed from this central pool. Copilot Studio Pay-As-You-Go (PAYG): Link a Copilot Studio environment to an Azure subscription. The interactio

来源：Copilot Agents licensing usage update – CIAOPS — https://blog.ciaops.com/2025/12/01/copilot-agents-licensing-usage-update/

类型：web；读取时间：2026-10-19T08:44:11.506662+00:00；截断：False

问题 q1 → 分块 chk_55bc3f900451bb732ad9f33f_1530 → 来源 src_55bc3f900451bb732ad9f33f；清洗后字符 [1680, 2130)

SHA-256：`aff02aa8d8069060cf183230347eebfb4c2b1964a6d577db976f6d7503cefd78`；范围：<main> element; characters 0-8495 of 8495

获取链：运行 c498744f19ea → 问题 q1 → 搜索 search1 → https://blog.ciaops.com/2025/12/01/copilot-agents-licensing-usage-update
检索词：Copilot Studio licensing messages capacity pack；当时的问题：微软官方如何说明 Copilot Studio 的计费单位与购买前提（例如按消息/容量包计费所需的 Azure 订阅或租户前提），与 Microsoft 365 Copilot 按用户席位收费的模式相比有何不同？

<a id="ev_4121ec907c1140a3f3eae833"></a>
### ev_4121ec907c1140a3f3eae833

> a prepaid, tenant-wide block of 25,000 Copilot Credits per mo

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q1 → 分块 chk_ba995cac346030f043dc84c6_4591 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [5129, 5190)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_191520cb2091a0e531ed020b"></a>
### ev_191520cb2091a0e531ed020b

> No Included Message Capacity with a Single M365 Copilot License Confirmation: Correct. Your individual Microsoft 365 Copilot license does not include a pool of Copilot Studio message capacity that can be used by other users in t

来源：Copilot Agents licensing usage update – CIAOPS — https://blog.ciaops.com/2025/12/01/copilot-agents-licensing-usage-update/

类型：web；读取时间：2026-10-19T08:44:11.506662+00:00；截断：False

问题 q2 → 分块 chk_55bc3f900451bb732ad9f33f_0 → 来源 src_55bc3f900451bb732ad9f33f；清洗后字符 [372, 600)

SHA-256：`aff02aa8d8069060cf183230347eebfb4c2b1964a6d577db976f6d7503cefd78`；范围：<main> element; characters 0-8495 of 8495

获取链：运行 c498744f19ea → 问题 q1 → 搜索 search1 → https://blog.ciaops.com/2025/12/01/copilot-agents-licensing-usage-update
检索词：Copilot Studio licensing messages capacity pack；当时的问题：微软官方如何说明 Copilot Studio 的计费单位与购买前提（例如按消息/容量包计费所需的 Azure 订阅或租户前提），与 Microsoft 365 Copilot 按用户席位收费的模式相比有何不同？

<a id="ev_026e2353f40c6d25e51e17a9"></a>
### ev_026e2353f40c6d25e51e17a9

> not include a pool of Copilot Studio message capacity that can be used by other users in the tenant who are unlicensed. Your License Rights: Your M365 Copilot license grants you the right to: Create and manage Copilot Studio agents for internal workflows at no extra charge for your own usage. Access and use those agents yourself without incurring additional usage costs. The Consumption: The consumption of your unlicensed colleagues is considered an organizational-level cost that must be covered by a separate organizational subscription for Copilot Studio.

来源：Copilot Agents licensing usage update – CIAOPS — https://blog.ciaops.com/2025/12/01/copilot-agents-licensing-usage-update/

类型：web；读取时间：2026-10-19T08:44:11.506662+00:00；截断：False

问题 q2 → 分块 chk_55bc3f900451bb732ad9f33f_510 → 来源 src_55bc3f900451bb732ad9f33f；清洗后字符 [510, 1071)

SHA-256：`aff02aa8d8069060cf183230347eebfb4c2b1964a6d577db976f6d7503cefd78`；范围：<main> element; characters 0-8495 of 8495

获取链：运行 c498744f19ea → 问题 q1 → 搜索 search1 → https://blog.ciaops.com/2025/12/01/copilot-agents-licensing-usage-update
检索词：Copilot Studio licensing messages capacity pack；当时的问题：微软官方如何说明 Copilot Studio 的计费单位与购买前提（例如按消息/容量包计费所需的 Azure 订阅或租户前提），与 Microsoft 365 Copilot 按用户席位收费的模式相比有何不同？

<a id="ev_559c66e41ae49989b83bc970"></a>
### ev_559c66e41ae49989b83bc970

> If your users hold the Microsoft 365 Copilot User SL ($30/user/month), they already have Copilot Studio use rights for employee-facing agents , Teams, SharePoint, M365 Copilot, at no extra charge. Agents built for those surfaces, operating under the licensed user’s identity, are covered.

来源：Copilot Studio Licensing | Explained by Licensing Expert — https://licenseq.com/copilot-studio-licensing/

类型：web；读取时间：2026-10-19T08:24:34.136568+00:00；截断：False

问题 q2 → 分块 chk_be03c5b67dd2b4fe8530e90d_5610 → 来源 src_be03c5b67dd2b4fe8530e90d；清洗后字符 [5637, 5925)

SHA-256：`56c234622dddeedd6d7055b85ceb6bdb7bd1df68db79be59a596ab47d1f8fc2d`；范围：<main> element; characters 0-17908 of 17908

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://licenseq.com/copilot-studio-licensing
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_57dc177d0ab3247a7f29ac8f"></a>
### ev_57dc177d0ab3247a7f29ac8f

> If your tenant has Copilot Studio billing enabled (credits or PAYG), end-user usage is billed at the tenant level. Users of your agents don't need a special license.

来源：Do users in my organization need individual Copilot licenses to use a published Copilot Studio agent? - Microsoft Q&A — https://learn.microsoft.com/en-us/answers/questions/5662349/do-users-in-my-organization-need-individual-copilo

类型：web；读取时间：2026-10-19T08:45:22.066057+00:00；截断：False

问题 q2 → 分块 chk_68911374ae2077e56fb57ecb_1020 → 来源 src_68911374ae2077e56fb57ecb；清洗后字符 [1444, 1609)

SHA-256：`f33a8e7dadb3a5692cd98107337c39a0efbf0ae1218b40820c3f1229a48aaf8f`；范围：<main> element; characters 0-2627 of 2627

获取链：运行 c498744f19ea → 问题 q2 → 搜索 search2 → https://learn.microsoft.com/en-us/answers/questions/5662349/do-users-in-my-organization-need-individual-copilo
检索词：Microsoft 365 Copilot internal agent use Copilot Studio licensing；当时的问题：微软官方对 Microsoft 365 Copilot 席位内所含 Copilot Studio 内部代理（internal agent）使用范围与 fair usage 上限是如何规定的？其正式条款原文发布在何处？

<a id="ev_7d1d68228d013e72f6062cf1"></a>
### ev_7d1d68228d013e72f6062cf1

> Microsoft 365 Copilot $30 per user/month Included agent usage1 Pay-as-you-go: unlimited2 License (capacity pack): 25,000 Copilot Credit /pack3

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q3 → 分块 chk_c68aacefe8ad1e6fd48eeabb_13260 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [13714, 13856)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_0b38cd8a1f64f34d14c759b0"></a>
### ev_0b38cd8a1f64f34d14c759b0

> udio agents and the Microsoft Copilot Studio tools/features invoked by the said agents, are included in the Microsoft 365 Copilot USL when the user of the agent is licensed with Microsoft 365 Copilot and the agent is operating using the authenticated Microsoft 365 Copilot USL user’s identity. Usage is limited to fair usage limits. Microsoft reserves the right to update the limits as the product evolves, and new usage patterns emerge.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q3 → 分块 chk_c68aacefe8ad1e6fd48eeabb_15300 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [15300, 15737)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_25868af562dd0d2ed0210605"></a>
### ev_25868af562dd0d2ed0210605

> 5. Agents built on Copilot Studio, for Teams, SharePoint and Microsoft 365 Copilot, are included with the Microsoft 365 Copilot user license at no additional char

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q3 → 分块 chk_c68aacefe8ad1e6fd48eeabb_15300 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [15738, 15900)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_935a0e34649f8223ac9ff4f2"></a>
### ev_935a0e34649f8223ac9ff4f2

> Employee-facing usage scenarios (Business to Employee) of Copilot Studio agents and Copilot Studio tools and features that these agents invoke are included in the Microsoft 365 Copilot USL when the user of the agent is licensed with Microsoft 365 Copilot, and the agent operates using the authenticated Microsoft 365 Copilot USL user’s identity. Usage is limited to fair usage limits.

来源：Article - Copilot Agents, Developer T... — https://services.northwestern.edu/TDClient/30/Portal/KB/Article/2879/Copilot-Agents-Developer-Tools-Sharing-Publishing-and-Message-Consumption

类型：web；读取时间：2026-10-19T08:25:23.206842+00:00；截断：False

问题 q3 → 分块 chk_7e9a2016729ec629a6069173_12240 → 来源 src_7e9a2016729ec629a6069173；清洗后字符 [12407, 12791)

SHA-256：`5e7f77f4b6eb7ba1580d3e124bf34f9731f751d8e737a903c4455cdc5db94043`；范围：<main> element; characters 0-14774 of 14774

获取链：运行 d968652bc210 → 问题 q3 → 搜索 search3 → https://services.northwestern.edu/TDClient/30/Portal/KB/Article/2879/Copilot-Agents-Developer-Tools-Sharing-Publishing-and-Message-Consumption
检索词：Microsoft Product Terms Copilot Studio included agent usage；当时的问题：微软官方 Product Terms 或完整许可条款中，Microsoft 365 Copilot 每席位“Included agent usage”对应的具体 Copilot Credit 数量是多少，公平使用限制（fair usage limit）如何定义、触发后有何后果？

<a id="ev_af5185b58ee678d3e7aef6e4"></a>
### ev_af5185b58ee678d3e7aef6e4

> Agents used by people without a Copilot license draw credits. One worked example on the rates page bills only the 100 unlicensed users of an agent that also serves 50 licensed users.

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q3 → 分块 chk_76369ce0f3851a65c00a0b8b_5101 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [5101, 5283)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_fc79abb7521f8b96f6ef5f71"></a>
### ev_fc79abb7521f8b96f6ef5f71

> Microsoft Learn states that Microsoft 365 Copilot licensed use of agents in Copilot Chat, Teams or SharePoint does not count against the Copilot Studio pack or meter, but the zero-rating has conditions (identity, trigger, fair use, CUA excluded).

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q3 → 分块 chk_76369ce0f3851a65c00a0b8b_5101 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [5289, 5535)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_66568c743ae007c496b4533f"></a>
### ev_66568c743ae007c496b4533f

> Microsoft 365 Copilot licensing 8 facts · Microsoft Publisher Microsoft Licensed as Per user add-on (User SL) plus metered agent usage Metrics User SL , Copilot Credit , Copilot Studio message , Copilot Credit Commit Unit Prerequisite A listed Microsoft 365, Office 365 or standalone service license (Product Terms) Capacity pack 25,000 Copilot Credits per pack per month

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q3 → 分块 chk_76369ce0f3851a65c00a0b8b_0 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [128, 499)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_95899b6cf40d7a032858ace6"></a>
### ev_95899b6cf40d7a032858ace6

> If you have a Microsoft 365 Copilot license, using agents in Copilot Chat, Microsoft Teams, or SharePoint for classic answers , generative answers , or Microsoft Graph tenant grounding doesn't count against the Copilot Studio message pack or meter.

来源：Standard harness licensing - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing

类型：web；读取时间：2026-10-19T08:56:19.777985+00:00；截断：False

问题 q4 → 分块 chk_0c9308874a087eda76e3ffa2_5610 → 来源 src_0c9308874a087eda76e3ffa2；清洗后字符 [5891, 6139)

SHA-256：`bd97d5a5eb6b73c5509af73942801a58576a809050ce94f139c18b173ae4f67d`；范围：<main> element; characters 0-7004 of 7004

获取链：运行 7ee761cd91fd → 问题 q2 → 搜索 search1 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing
检索词：Microsoft 365 Copilot licensing guide agent usage；当时的问题：微软官方如何定义 Microsoft 365 Copilot 许可（每用户每月 30 美元）所附带、可用于 Copilot Studio 代理的容量权益及其边界（是否仅限该用户自身使用、是否覆盖未获许可用户）？

<a id="ev_8e4ac1633098e933fbaff23c"></a>
### ev_8e4ac1633098e933fbaff23c

> Agents used by people without a Copilot license draw credits.

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q4 → 分块 chk_76369ce0f3851a65c00a0b8b_5101 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [5101, 5162)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_dab8e0c5567387bd76c1ea4a"></a>
### ev_dab8e0c5567387bd76c1ea4a

> One worked example on the rates page bills only the 100 unlicensed users of an agent that also serves 50 licensed users.

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q4 → 分块 chk_76369ce0f3851a65c00a0b8b_5101 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [5163, 5283)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_a2c571d68f9943a013d2da85"></a>
### ev_a2c571d68f9943a013d2da85

> Not for agent interactions inside Copilot Chat, Teams and SharePoint. Unlicensed users inside a connected billing policy are metered.

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q4 → 分块 chk_ba995cac346030f043dc84c6_7650 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [7709, 7842)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_93e76e6d6ee250fa46dbb28a"></a>
### ev_93e76e6d6ee250fa46dbb28a

> People without a seat who use agents in Copilot Chat or SharePoint

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q4 → 分块 chk_ba995cac346030f043dc84c6_8670 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [8900, 8966)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_a00c24a535eaedb78a612de4"></a>
### ev_a00c24a535eaedb78a612de4

> MCS Pay-As-You-Go • MCS License (Copilot Credit capacity pack) • Copilot Credit Pre-Purchase Plan

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q5 → 分块 chk_c68aacefe8ad1e6fd48eeabb_13260 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [13616, 13713)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_6f17a4fe98ba2630e223ac27"></a>
### ev_6f17a4fe98ba2630e223ac27

> Pay-as-you-go: unlimited2 License (capacity pack): 25,000 Copilot Credit /pack3 Pre

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q5 → 分块 chk_c68aacefe8ad1e6fd48eeabb_13260 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [13777, 13860)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_c05542491d40e826f23e8c8a"></a>
### ev_c05542491d40e826f23e8c8a

> nse (Capacity pack) Capacity packs are offered through the Copilot Studio subscription license.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf

类型：web；读取时间：2026-10-19T08:24:22.210421+00:00；截断：False

问题 q5 → 分块 chk_059af1d4b3d5bf109a6dbb14_27030 → 来源 src_059af1d4b3d5bf109a6dbb14；清洗后字符 [27030, 27125)

SHA-256：`ffd7d5a631e01bb670aef2bd8fa6ae234dcc34b5d3770ccd90bb71beba67c590`；范围：PDF pages 1-21 of 21; characters 0-38941 of 38941

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_28551c4a7bf7fcced4a5c374"></a>
### ev_28551c4a7bf7fcced4a5c374

> Copilot Credit packs should be purchased for the anticipated number of Copilot Credits the tenant is expected to consume each month. Unused credits do not roll over to the next month.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf

类型：web；读取时间：2026-10-19T08:24:22.210421+00:00；截断：False

问题 q5 → 分块 chk_059af1d4b3d5bf109a6dbb14_27030 → 来源 src_059af1d4b3d5bf109a6dbb14；清洗后字符 [27126, 27309)

SHA-256：`ffd7d5a631e01bb670aef2bd8fa6ae234dcc34b5d3770ccd90bb71beba67c590`；范围：PDF pages 1-21 of 21; characters 0-38941 of 38941

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_2b9e141ce0074ba49ee0902f"></a>
### ev_2b9e141ce0074ba49ee0902f

> • Pricing: $200 per credit pack/month (billed annually) • Copilot Credit Capacity: 1 capacity pack = 25,000 Copilot Credits

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf

类型：web；读取时间：2026-10-19T08:24:22.210421+00:00；截断：False

问题 q5 → 分块 chk_059af1d4b3d5bf109a6dbb14_27030 → 来源 src_059af1d4b3d5bf109a6dbb14；清洗后字符 [27310, 27433)

SHA-256：`ffd7d5a631e01bb670aef2bd8fa6ae234dcc34b5d3770ccd90bb71beba67c590`；范围：PDF pages 1-21 of 21; characters 0-38941 of 38941

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_f4a973b7dc16323e83c460c3"></a>
### ev_f4a973b7dc16323e83c460c3

> For additional capacity, it is recommended to sign up for the pay-as-you-go meter to ensure §PDF page 16§ Microsoft Copilot Studio Licensing Guide | October 2026 P a g e | 16 business continuity.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf

类型：web；读取时间：2026-10-19T08:24:22.210421+00:00；截断：False

问题 q5 → 分块 chk_059af1d4b3d5bf109a6dbb14_27030 → 来源 src_059af1d4b3d5bf109a6dbb14；清洗后字符 [27434, 27629)

SHA-256：`ffd7d5a631e01bb670aef2bd8fa6ae234dcc34b5d3770ccd90bb71beba67c590`；范围：PDF pages 1-21 of 21; characters 0-38941 of 38941

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_8dd171278e8f01404354694a"></a>
### ev_8dd171278e8f01404354694a

> Copilot Credit capacity packs are offered through the Copilot Studio subscription license.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q5 → 分块 chk_c68aacefe8ad1e6fd48eeabb_9180 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [9336, 9426)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_c3b106414c41ffadca235ae5"></a>
### ev_c3b106414c41ffadca235ae5

> Copilot Credit capacity packs should be purchased for the anticipated number of Copilot Credits your tenant is expected to consume each month. Unused credits do not roll over to the next month.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q5 → 分块 chk_c68aacefe8ad1e6fd48eeabb_9180 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [9427, 9620)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_41d3722308a5dc62841ab0a5"></a>
### ev_41d3722308a5dc62841ab0a5

> • Pricing: $200 per pack/month • Copilot Credit Capacity: 1 capacity pack = 25,000 Copilot Credits

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q5 → 分块 chk_c68aacefe8ad1e6fd48eeabb_9180 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [9621, 9719)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_6384dfc393693ccb31745e72"></a>
### ev_6384dfc393693ccb31745e72

> 3. Copilot Credit Pre-Purchase Plan The Copilot Credit Pre-Purchase Plan offers organizations a one-year, pay-upfront purchase option for Copilot Credits at tiered discounts.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q5 → 分块 chk_c68aacefe8ad1e6fd48eeabb_4590 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [4980, 5154)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_032bbbc4df3151bb3f1edcb3"></a>
### ev_032bbbc4df3151bb3f1edcb3

> A Microsoft Copilot Studio capacity pack is a prepaid subscription that provides credits for Copilot Chat and SharePoint agent usage.

来源：Use Capacity Packs vs Pay-as-you-go Billing for Microsoft Copilot Chat | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/copilot-capacity-packs

类型：web；读取时间：2026-10-19T08:29:42.860354+00:00；截断：False

问题 q5 → 分块 chk_40c65badfe4b5f9302da4ec9_510 → 来源 src_40c65badfe4b5f9302da4ec9；清洗后字符 [617, 750)

SHA-256：`e4cc25355e7cccc38e74ff20c800b4270dbe55c50eb9ac47897ea1a603e60a13`；范围：<main> element; characters 0-18860 of 18860

获取链：运行 d968652bc210 → 问题 q8 → 搜索 search7 → https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/copilot-capacity-packs
检索词：Copilot Studio capacity pack Azure subscription requirement；当时的问题：微软官方文档是否明确 Copilot Studio 容量包（Copilot Credit 容量包，每包 25,000 信用）与预购 Commit Units 路径在使用代理时同样需要 Azure 订阅，而不仅是按量付费计量需要？

<a id="ev_17c1117b96d2617043b1790c"></a>
### ev_17c1117b96d2617043b1790c

> Credits are available in quantities of 25,000 per month per pack.

来源：Use Capacity Packs vs Pay-as-you-go Billing for Microsoft Copilot Chat | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/copilot-capacity-packs

类型：web；读取时间：2026-10-19T08:29:42.860354+00:00；截断：False

问题 q5 → 分块 chk_40c65badfe4b5f9302da4ec9_510 → 来源 src_40c65badfe4b5f9302da4ec9；清洗后字符 [963, 1028)

SHA-256：`e4cc25355e7cccc38e74ff20c800b4270dbe55c50eb9ac47897ea1a603e60a13`；范围：<main> element; characters 0-18860 of 18860

获取链：运行 d968652bc210 → 问题 q8 → 搜索 search7 → https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/copilot-capacity-packs
检索词：Copilot Studio capacity pack Azure subscription requirement；当时的问题：微软官方文档是否明确 Copilot Studio 容量包（Copilot Credit 容量包，每包 25,000 信用）与预购 Commit Units 路径在使用代理时同样需要 Azure 订阅，而不仅是按量付费计量需要？

<a id="ev_448ccee7c6af8bf2cd1c0961"></a>
### ev_448ccee7c6af8bf2cd1c0961

> §Prepaid capacity packs ($200/month per 25,000 credits)§ Two prepaid options for organizations needing standalone Copilot Studio licensing .

来源：Microsoft Copilot Studio Pricing In 2026: Credits, Plans, And Costs — https://www.cloudzero.com/blog/copilot-studio-pricing/

类型：web；读取时间：2026-10-19T08:59:03.845217+00:00；截断：False

问题 q5 → 分块 chk_5de6a402648eeec2266bf20a_5610 → 来源 src_5de6a402648eeec2266bf20a；清洗后字符 [5769, 5909)

SHA-256：`cb19d183bd1edd7576e299f6598b444a3200c932fb28102ca2d84e1e3314d183`；范围：<main> element; characters 0-19388 of 19388

获取链：运行 7ee761cd91fd → 问题 q4 → 搜索 search3 → https://www.cloudzero.com/blog/copilot-studio-pricing
检索词：Copilot Studio billing rates M365 Copilot agents；当时的问题：微软官方 Microsoft Learn 计费/费率页（billing rates and management 或 requirements-messages-management）如何规定：持有 Microsoft 365 Copilot 许可的用户在 Copilot Chat、Teams、SharePoint 中使用 Copilot Studio 代理时不计入容量包或计量的具体条件（身份、触发方式、公平使用限制、是否排除 Computer-Using Agents），以及对未获许可用户的逐用户计费口径？

<a id="ev_e0a050a8f91feb72529bed19"></a>
### ev_e0a050a8f91feb72529bed19

> On our Copilot Studio page , the tenant capacity pack lists at $2,400 per year paid up front, $2,520 per year billed monthly, or $240 a month on a one-month commitment; the separate Copilot Studio User License for access to the authoring tool lists at $0.

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q5 → 分块 chk_ba995cac346030f043dc84c6_4591 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [4816, 5071)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_913bc5f4729001583f2fa939"></a>
### ev_913bc5f4729001583f2fa939

> 0.00 per pack. [11] Packs can also fund Copilot Chat through Copilot credit policies, up to 10 per tenant.

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q5 → 分块 chk_76369ce0f3851a65c00a0b8b_7650 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [7650, 7756)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_1d48176a7131ec7f475a3f8a"></a>
### ev_1d48176a7131ec7f475a3f8a

> Copilot Credit Pre-Purchase Plan (P3) : “a one-year, prepaid option for Copilot Credits”, drawn down as Copilot Credit Commit Units across eligible products.

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q5 → 分块 chk_76369ce0f3851a65c00a0b8b_7650 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [8033, 8190)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_ebc24156510a771ef0b63cea"></a>
### ev_ebc24156510a771ef0b63cea

> This guide does not supersede, or replace any of the Microsoft Product Terms legal documentation covering use rights.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q6 → 分块 chk_c68aacefe8ad1e6fd48eeabb_2040 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [2500, 2617)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_17739cb3661f1be01e959e1f"></a>
### ev_17739cb3661f1be01e959e1f

> y must procure and enable Copilot Studio capacity (either Message Packs or Pay-As-You-Go metering) in your tenant.

来源：Copilot Agents licensing usage update – CIAOPS — https://blog.ciaops.com/2025/12/01/copilot-agents-licensing-usage-update/

类型：web；读取时间：2026-10-19T08:44:11.506662+00:00；截断：False

问题 q6 → 分块 chk_55bc3f900451bb732ad9f33f_3570 → 来源 src_55bc3f900451bb732ad9f33f；清洗后字符 [3570, 3684)

SHA-256：`aff02aa8d8069060cf183230347eebfb4c2b1964a6d577db976f6d7503cefd78`；范围：<main> element; characters 0-8495 of 8495

获取链：运行 c498744f19ea → 问题 q1 → 搜索 search1 → https://blog.ciaops.com/2025/12/01/copilot-agents-licensing-usage-update
检索词：Copilot Studio licensing messages capacity pack；当时的问题：微软官方如何说明 Copilot Studio 的计费单位与购买前提（例如按消息/容量包计费所需的 Azure 订阅或租户前提），与 Microsoft 365 Copilot 按用户席位收费的模式相比有何不同？

<a id="ev_8b335a5d6dfe792d82d57514"></a>
### ev_8b335a5d6dfe792d82d57514

> Yes , with Microsoft 365 Copilot licenses , you can use Copilot Studio agents in Teams or SharePoint at no additional cost, as long as the usage is interactive and initiated by the user .

来源：Power Platform Community Forum Thread Details — https://community.powerplatform.com/forums/thread/details/?threadid=bc7d0d19-4921-f111-8342-7ced8dcf6527

类型：web；读取时间：2026-10-19T08:24:49.983894+00:00；截断：False

问题 q6 → 分块 chk_1a66581da9f76a510025eaf3_2040 → 来源 src_1a66581da9f76a510025eaf3；清洗后字符 [2386, 2573)

SHA-256：`f7337cddce4c9ebdb5b2eab78399442aedc3bec6ad4f72b526beb15faa6b880d`；范围：<body> element; characters 0-6584 of 6584

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://community.powerplatform.com/forums/thread/details?threadid=bc7d0d19-4921-f111-8342-7ced8dcf6527
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_69fb0940a0671f4663533f19"></a>
### ev_69fb0940a0671f4663533f19

> For example, when Microsoft 365 Copilot licensed users use agents in M

来源：Standard harness licensing - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing

类型：web；读取时间：2026-10-19T08:56:19.777985+00:00；截断：False

问题 q7 → 分块 chk_0c9308874a087eda76e3ffa2_5610 → 来源 src_0c9308874a087eda76e3ffa2；清洗后字符 [6140, 6210)

SHA-256：`bd97d5a5eb6b73c5509af73942801a58576a809050ce94f139c18b173ae4f67d`；范围：<main> element; characters 0-7004 of 7004

获取链：运行 7ee761cd91fd → 问题 q2 → 搜索 search1 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing
检索词：Microsoft 365 Copilot licensing guide agent usage；当时的问题：微软官方如何定义 Microsoft 365 Copilot 许可（每用户每月 30 美元）所附带、可用于 Copilot Studio 代理的容量权益及其边界（是否仅限该用户自身使用、是否覆盖未获许可用户）？

<a id="ev_b0013918677d3356944c0895"></a>
### ev_b0013918677d3356944c0895

> Employee-facing agent use is “No charge” when the user holds a Microsoft 365 Copilot license and the agent runs under that user’s identity. This is subject to fair-use limits, applies to agent flows only when started by the “When an agent calls the flow” trigger, and excludes Computer-Using Agents.

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q7 → 分块 chk_76369ce0f3851a65c00a0b8b_4590 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [4796, 5095)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_0a1f12af93d3fbc02f823ca5"></a>
### ev_0a1f12af93d3fbc02f823ca5

> Agents used by people without a Copilot license draw credits. One worked example on the r

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q7 → 分块 chk_76369ce0f3851a65c00a0b8b_4590 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [5101, 5190)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_d7fd53462aa8d644b4fd607b"></a>
### ev_d7fd53462aa8d644b4fd607b

> §Do licensed users consume Copilot Credits?§ Not for agent interactions inside Copilot Chat, Teams and SharePoint. Unlicensed users inside a connected billing policy are metered.

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q7 → 分块 chk_ba995cac346030f043dc84c6_7650 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [7664, 7842)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_56dfd86c47ac3d6e08df5b62"></a>
### ev_56dfd86c47ac3d6e08df5b62

> Copilot Credit Pre-Purchase Plan Pricing Tiers Tier Copilot Credits Commit Units (CCCU) Price Discount 1 3,000 $2,850 5% 2 15,000 $14,100 6% 3 30,000 $27,900 7% 4 150,000 $138,000 8% 5 300,000 $270,000 10% 6 750,000 $660,000 12% 7 1,500,000 $1,290,000 14% 8 2,250,000 $1,867,500 17% 9 3,000,000 $2,400,000 20%

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q8 → 分块 chk_c68aacefe8ad1e6fd48eeabb_10710 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [10947, 11256)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_e7f728cc95661ada112dc727"></a>
### ev_e7f728cc95661ada112dc727

> purchase option for Copilot Credits at tiered discounts. Customers purchase a pool of Copilot Credit Commit Units (CCCUs) that automatically covers the usage of Copilot Credit. Each CCCUs is worth $1 and converts to 100 Copilot Credits.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q8 → 分块 chk_c68aacefe8ad1e6fd48eeabb_10710 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [10710, 10946)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_4b959f26c83df458f524be40"></a>
### ev_4b959f26c83df458f524be40

> 7,500 17% 9 3,000,000 $2,400,000 20% §PDF page 7§ Microsoft Copilot Studio Licensing Guide | November 2025 P a g e | 7 Copilot Credit Pre-Purchase Plan Value Conversion Tier Copilot Credits Commit Units (CCCU) # of Copilot Credit (1 CCCU = 100 Copilot Credit) # of monthly MCS licenses (Copilot Credit capacity pack) 1 3,000 300,000 1 pack * 12 months 2 15,000 1,500,000 5 packs * 12 months 3 30,000 3,000,000 10 packs * 12 months 4 150,000 15,000,000 50 packs * 12 months 5 300,000 30,000,000 100 packs * 12 months 6 750,000 75,000,000 250 packs * 12 months 7 1,500,000 150,00,000 500 packs * 12 mon

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q8 → 分块 chk_c68aacefe8ad1e6fd48eeabb_11220 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [11220, 11820)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_a3b65c2ec57e21989f91c97b"></a>
### ev_a3b65c2ec57e21989f91c97b

> 2. Copilot Credit Pre-Purchase Plan (P3) Copilot Credit P3 is a one-year pay-upfront purchase option for Copilot Credits. Customers purchase a pool of Copilot Credits, which automatically deduct the Copilot Credit P3 balance. If usage exceeds the available number of credits, customers can purchase additional Copilot Credits or be billed on a pay-as-you-go basis. Unused credits expire at the end of the annual term. Copilot Credit Pre-Purchase Plan (P3) Pricing Tiers Tier Copilot Credits Discount 1 300,000 5

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf

类型：web；读取时间：2026-10-19T08:24:22.210421+00:00；截断：False

问题 q8 → 分块 chk_059af1d4b3d5bf109a6dbb14_22950 → 来源 src_059af1d4b3d5bf109a6dbb14；清洗后字符 [23039, 23550)

SHA-256：`ffd7d5a631e01bb670aef2bd8fa6ae234dcc34b5d3770ccd90bb71beba67c590`；范围：PDF pages 1-21 of 21; characters 0-38941 of 38941

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_2eee67abb8bb61271fd0bc66"></a>
### ev_2eee67abb8bb61271fd0bc66

> 3. Copilot Credits offered via the Copilot Studio license monthly subscription (1 credit pack = 25,000 Copilot Credits) do not roll over to the next month. The CCCU pre-purchased via Copilot Credit Pre-Purchase Plan expire at the end of the annual term. See Pre-Purchase Plan pricing tiers here.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q8 → 分块 chk_c68aacefe8ad1e6fd48eeabb_14790 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [14923, 15218)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_263ae0f13e9424788378f7d0"></a>
### ev_263ae0f13e9424788378f7d0

> 3. Copilot Credit Pre-Purchase Plan (P3), annual upfront, tiered discount up to 20%. Launched October 2025. You buy a one-year pool of Copilot Credit Commit Units (CCCUs); each CCCU equals $1 of credit consumption, i.e. 100 credits. Discount tiers run from 5% at 3,000 CCCUs ($2,850) up to 20% at 3,000,000 CCCUs ($2.4m).

来源：Copilot Studio Licensing | Explained by Licensing Expert — https://licenseq.com/copilot-studio-licensing/

类型：web；读取时间：2026-10-19T08:24:34.136568+00:00；截断：False

问题 q8 → 分块 chk_be03c5b67dd2b4fe8530e90d_3570 → 来源 src_be03c5b67dd2b4fe8530e90d；清洗后字符 [3724, 4045)

SHA-256：`56c234622dddeedd6d7055b85ceb6bdb7bd1df68db79be59a596ab47d1f8fc2d`；范围：<main> element; characters 0-17908 of 17908

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://licenseq.com/copilot-studio-licensing
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_c835b27e9f6ab62bee59209d"></a>
### ev_c835b27e9f6ab62bee59209d

> The Copilot Credit Pre-Purchase Plan is a one-year, pay-upfront option that provides a pool of credits and volume-based discounts. Unused prepaid credits expire at the end of the annual term, and usage above the available balance may require additional credits or pay-as-you-go billing.

来源：Microsoft Copilot Credits explained: usage, costs, and limits | Rand Group — https://www.randgroup.com/insights/copilot/microsoft-copilot-credits-explained-usage-costs-and-limits/

类型：web；读取时间：2026-10-19T08:57:54.999976+00:00；截断：False

问题 q8 → 分块 chk_b1cc9f91fec6eb8dd862d0b2_5101 → 来源 src_b1cc9f91fec6eb8dd862d0b2；清洗后字符 [5413, 5699)

SHA-256：`56fb7ca8ffd57867ccab60603a779f80f6057d2fc2bd06694f5f210eb5310818`；范围：<main> element; characters 0-18567 of 18567

获取链：运行 7ee761cd91fd → 问题 q3 → 搜索 search2 → https://www.randgroup.com/insights/copilot/microsoft-copilot-credits-explained-usage-costs-and-limits
检索词：Microsoft 365 Copilot included agent usage Copilot Studio credits；当时的问题：微软官方许可文档（Copilot Studio Licensing Guide 或 Product Terms）如何界定 Microsoft 365 Copilot 每用户许可中“Included agent usage”的具体范围：随附的 Copilot Studio 容量额度是多少、是否仅限该持证用户本人运行代理使用、以及未获许可用户通过该随附用量访问代理是否被允许？

<a id="ev_f07d750c732f78afea191918"></a>
### ev_f07d750c732f78afea191918

> Copilot Credit Pre-Purchase Plan (P3) Annual commitment 1 Copilot Credit Commit Unit (CCCU) = $1 = 100 credits, 9 discount levels

来源：Agent 365 Licensing: What It Covers and Costs | SAMexpert Guide — https://samexpert.com/agent-365/

类型：web；读取时间：2026-10-19T08:56:12.232593+00:00；截断：False

问题 q8 → 分块 chk_0f0c14c47570636d69289d70_14790 → 来源 src_0f0c14c47570636d69289d70；清洗后字符 [14841, 14970)

SHA-256：`69d5dc0e8353abe89a0a5b43d298438be9c78da9a3834c4c5ac8d787282f0c2d`；范围：<main> element; characters 0-24649 of 24649

获取链：运行 7ee761cd91fd → 问题 q2 → 搜索 search1 → https://samexpert.com/agent-365
检索词：Microsoft 365 Copilot licensing guide agent usage；当时的问题：微软官方如何定义 Microsoft 365 Copilot 许可（每用户每月 30 美元）所附带、可用于 Copilot Studio 代理的容量权益及其边界（是否仅限该用户自身使用、是否覆盖未获许可用户）？

<a id="ev_abf7951d9d970f459397f5ec"></a>
### ev_abf7951d9d970f459397f5ec

> • Pricing: $200 per credit pack/month (billed annually)

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf

类型：web；读取时间：2026-10-19T08:24:22.210421+00:00；截断：False

问题 q9 → 分块 chk_059af1d4b3d5bf109a6dbb14_27030 → 来源 src_059af1d4b3d5bf109a6dbb14；清洗后字符 [27310, 27365)

SHA-256：`ffd7d5a631e01bb670aef2bd8fa6ae234dcc34b5d3770ccd90bb71beba67c590`；范围：PDF pages 1-21 of 21; characters 0-38941 of 38941

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_bd71a95b07e175b0920d6d89"></a>
### ev_bd71a95b07e175b0920d6d89

> • Pricing: $200 per pack/month

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q9 → 分块 chk_c68aacefe8ad1e6fd48eeabb_9180 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [9621, 9651)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_82638d6dd87bf3b75ec2fb8e"></a>
### ev_82638d6dd87bf3b75ec2fb8e

> With Copilot Credit packs, a customer pays up front ( $200.00 /pack/month for 25,000 Copilot Credits).

来源：Microsoft Copilot Studio Plans and Pricing — https://www.microsoft.com/en-us/copilot/pricing/copilot-studio

类型：web；读取时间：2026-10-19T08:23:18.966505+00:00；截断：False

问题 q9 → 分块 chk_0974f6cd66d2bc4ca55c8219_7650 → 来源 src_0974f6cd66d2bc4ca55c8219；清洗后字符 [7979, 8081)

SHA-256：`5c2c49105b6ac9c095aedd95af5f2f3133be5bf6bb7d17561ab15184a704fb32`；范围：<main> element; characters 0-8971 of 8971

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.microsoft.com/en-us/copilot/pricing/copilot-studio
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_697d9f2ff22fe19ca05eae8f"></a>
### ev_697d9f2ff22fe19ca05eae8f

> $2,400 per year per pack at list, plus pay-as-you-go for overage

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q9 → 分块 chk_ba995cac346030f043dc84c6_8670 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [9153, 9217)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_cf7723ab96f1ed24abf6f375"></a>
### ev_cf7723ab96f1ed24abf6f375

> Microsoft Copilot Studio Capacity Packs $200/month Monthly Includes 25,000 credits/month

来源：Microsoft Copilot Studio Pricing In 2026: Credits, Plans, And Costs — https://www.cloudzero.com/blog/copilot-studio-pricing/

类型：web；读取时间：2026-10-19T08:59:03.845217+00:00；截断：False

问题 q9 → 分块 chk_5de6a402648eeec2266bf20a_4080 → 来源 src_5de6a402648eeec2266bf20a；清洗后字符 [4397, 4485)

SHA-256：`cb19d183bd1edd7576e299f6598b444a3200c932fb28102ca2d84e1e3314d183`；范围：<main> element; characters 0-19388 of 19388

获取链：运行 7ee761cd91fd → 问题 q4 → 搜索 search3 → https://www.cloudzero.com/blog/copilot-studio-pricing
检索词：Copilot Studio billing rates M365 Copilot agents；当时的问题：微软官方 Microsoft Learn 计费/费率页（billing rates and management 或 requirements-messages-management）如何规定：持有 Microsoft 365 Copilot 许可的用户在 Copilot Chat、Teams、SharePoint 中使用 Copilot Studio 代理时不计入容量包或计量的具体条件（身份、触发方式、公平使用限制、是否排除 Computer-Using Agents），以及对未获许可用户的逐用户计费口径？

<a id="ev_414550a10cb2870ee7771428"></a>
### ev_414550a10cb2870ee7771428

> Creating and Managing agents: A Copilot Studio User License ($0) is required for each user that builds and manages agents with Copilot Studio.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf

类型：web；读取时间：2026-10-19T08:24:22.210421+00:00；截断：False

问题 q10 → 分块 chk_059af1d4b3d5bf109a6dbb14_27540 → 来源 src_059af1d4b3d5bf109a6dbb14；清洗后字符 [27976, 28118)

SHA-256：`ffd7d5a631e01bb670aef2bd8fa6ae234dcc34b5d3770ccd90bb71beba67c590`；范围：PDF pages 1-21 of 21; characters 0-38941 of 38941

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_0e46d1aecb63917607fc726e"></a>
### ev_0e46d1aecb63917607fc726e

> To use Copilot Studio, you need one of the following configurations: Copilot Studio user license (free of charge). The admin assigns this license to the maker in the Microsoft Admin Center .

来源：Standard harness licensing - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing

类型：web；读取时间：2026-10-19T08:56:19.777985+00:00；截断：False

问题 q10 → 分块 chk_0c9308874a087eda76e3ffa2_1530 → 来源 src_0c9308874a087eda76e3ffa2；清洗后字符 [1923, 2113)

SHA-256：`bd97d5a5eb6b73c5509af73942801a58576a809050ce94f139c18b173ae4f67d`；范围：<main> element; characters 0-7004 of 7004

获取链：运行 7ee761cd91fd → 问题 q2 → 搜索 search1 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing
检索词：Microsoft 365 Copilot licensing guide agent usage；当时的问题：微软官方如何定义 Microsoft 365 Copilot 许可（每用户每月 30 美元）所附带、可用于 Copilot Studio 代理的容量权益及其边界（是否仅限该用户自身使用、是否覆盖未获许可用户）？

<a id="ev_376ddd08ecd4747fa61b4b19"></a>
### ev_376ddd08ecd4747fa61b4b19

> Copilot Credit consumption won’t be counted against the pay-as-you-go meter until credit packs have been exhausted.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf

类型：web；读取时间：2026-10-19T08:24:22.210421+00:00；截断：False

问题 q10 → 分块 chk_059af1d4b3d5bf109a6dbb14_27540 → 来源 src_059af1d4b3d5bf109a6dbb14；清洗后字符 [27630, 27745)

SHA-256：`ffd7d5a631e01bb670aef2bd8fa6ae234dcc34b5d3770ccd90bb71beba67c590`；范围：PDF pages 1-21 of 21; characters 0-38941 of 38941

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_8a26c7115c3d298fa2df5872"></a>
### ev_8a26c7115c3d298fa2df5872

> Copilot Studio is sold as tenant-wide license which includes Copilot Credit capacity packs of 25,000 Copilot Credits each, priced at $200.00 /pack/month.

来源：Microsoft Copilot Studio Plans and Pricing — https://www.microsoft.com/en-us/copilot/pricing/copilot-studio

类型：web；读取时间：2026-10-19T08:23:18.966505+00:00；截断：False

问题 q10 → 分块 chk_0974f6cd66d2bc4ca55c8219_6631 → 来源 src_0974f6cd66d2bc4ca55c8219；清洗后字符 [6748, 6901)

SHA-256：`5c2c49105b6ac9c095aedd95af5f2f3133be5bf6bb7d17561ab15184a704fb32`；范围：<main> element; characters 0-8971 of 8971

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.microsoft.com/en-us/copilot/pricing/copilot-studio
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_1a462d3fb49390770df08970"></a>
### ev_1a462d3fb49390770df08970

> To build and manage agents, a Copilot Studio User License (at no additional cost) is required for each user.

来源：Copilot Studio licensing — https://holgerimbery.blog/copilot-studio-licensing259

类型：web；读取时间：2026-10-19T08:37:25.859591+00:00；截断：False

问题 q10 → 分块 chk_f14c765af66c5d72ec26c793_4080 → 来源 src_f14c765af66c5d72ec26c793；清洗后字符 [4498, 4606)

SHA-256：`c73829c507edcda46c85c636cc929b9b5299bdd573aa8711a1ada905c861958c`；范围：<main> element; characters 0-21658 of 21658

获取链：运行 23c904aac0c6 → 问题 q6 → 搜索 search3 → https://holgerimbery.blog/copilot-studio-licensing259
检索词：Copilot Studio pricing capacity pack credits；当时的问题：微软官方 Copilot Studio 定价页或产品条款中，容量包（25,000 Copilot Credits/包）的官方标价、按用量付费的每单位 Credit 单价、外部代理部署的独立许可价格，以及预购计划的折扣条件分别是什么？

<a id="ev_e36ef05ec22cde0fe87b0ab1"></a>
### ev_e36ef05ec22cde0fe87b0ab1

> the separate Copilot Studio User License for access to the authoring tool lists at $0

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q10 → 分块 chk_ba995cac346030f043dc84c6_4591 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [4985, 5070)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

完整来源文本、分块、引用和哈希见同目录 state.json；节点、调用及排序分数见 trace.jsonl。
