# Microsoft｜企业研究

研究问题：Microsoft 365 Copilot 与 Copilot Studio 面向的企业使用者、收费单位和购买前提有何区别？这些差异可能如何影响企业客户扩展使用和微软的收入来源？优先使用官方资料；将价格与许可事实、基于事实的推导、商业判断和仍待验证假设明确区分，不把产品定价直接当成已实现收入或利润。

模式：live；停止原因：error；研究轮次：10

引用关系与摘录位置已做代码校验；语义支持关系、事实分类和缺口关闭是模型判断，未经独立事实核实。

## 事实（来源陈述）

- **c1_1** [supported] 微软官方 Copilot Studio 许可指南在同一对比表中列出 Microsoft 365 Copilot 按每用户每月 30 美元计费（含代理使用），以及 Copilot Studio 的按量付费（Azure 计量）和按容量包授权（每包 25,000 Copilot Credits）两种模式。 [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports）
  依据/推导：该引文来自托管于 microsoft.com 域名的官方许可指南 PDF（vendor_official），直接显示各计费模式并列。但摘录仅为表格片段，未包含购买前提（Azure 订阅/租户）完整表述，故本条只支持“计费模式并列”这一事实。
- **c1_2** [supported] 第三方资料称 Copilot Studio 的计费货币已从“消息”改为“Copilot Credit”，容量按月强制执行且不结转。 [ev_2455574e039ae9be1eeb4886](#ev_2455574e039ae9be1eeb4886)（supports）
  依据/推导：LICENSEWARE Wiki 为第三方来源，原句直接陈述计价单位变更；后半句“capacity enforced monthly without carry-over”出现在 context_after，故仅作为辅助背景，未单独作为独立结论。
- **c1_3** [supported] 第三方分析指出 Copilot Studio 按租户级共享的 Copilot Credits 计价而非按席位，成本取决于代理消耗的额度而非使用人数。 [ev_69933db511a7d22a4dd584c9](#ev_69933db511a7d22a4dd584c9)（supports）
  依据/推导：cloudzero 为第三方来源，原句明确对比“per credit, pooled at the tenant level, not per seat”，与 M365 Copilot 的席位模式形成对照。非官方，不能单独用来关闭要求官方条款的缺口。
- **c1_4** [supported] 第三方文档镜像（GitHub 上的 MicrosoftDocs 仓库）称容量包为订阅制产品，每月初补充 25,000 credits，且每月必须启用按量付费作为超额兜底。 [ev_be5275736ecd2673b69b55cd](#ev_be5275736ecd2673b69b55cd)（supports）
  依据/推导：该页是 Microsoft 文档仓库的 GitHub 镜像，托管在 github.com，按规则判为 third_party，不能视为厂商正式发布页面；摘录明确“必须启用 pay-as-you-go 作为每月兜底”，指向 Azure 订阅计量这一购买前提。
- **c1_5** [supported] 第三方博客称 Copilot Studio 的组织级订阅（按量付费或消息包）必须在租户中启用，Copilot Credits 计量费用计入组织容量/Azure 订阅。 [ev_4e0ed4de864a34274c45b16f](#ev_4e0ed4de864a34274c45b16f)（supports）
  依据/推导：CIAOPS 为第三方博客，原句直接点出租户前提与 Azure 订阅计量，但属二手转述，不能替代官方条款。
- **c2_1** [supported] 微软官方《Microsoft Copilot Studio Licensing Guide》（November 2025）规定：基于 Copilot Studio 构建、面向 Teams、SharePoint 和 Microsoft 365 Copilot 的代理，随 Microsoft 365 Copilot 用户许可证一并提供，不额外收费。 [ev_339bdf875fab188660312b7d](#ev_339bdf875fab188660312b7d)（supports） [ev_3673df720bdda4517b7e7b6a](#ev_3673df720bdda4517b7e7b6a)（supports）
  依据/推导：引文摘自托管于 microsoft.com CDN 的官方许可指南 PDF（vendor_official），脚注5直接陈述“included with the Microsoft 365 Copilot user license at no additional charge”，适用范围限定为 Teams、SharePoint、Microsoft 365 Copilot 三个表面。该摘录为主语范围提供了明确限定，不能外推至其他渠道或外部用户。
- **c2_2** [supported] 同一官方指南对上述含额使用仅规定“受 fair usage 限制”，并声明微软保留随产品演进与使用模式变化而更新上限的权利；该摘录未给出任何具体数值阈值。 [ev_3673df720bdda4517b7e7b6a](#ev_3673df720bdda4517b7e7b6a)（supports）
  依据/推导：官方指南原文“Usage is limited to fair usage limits. Microsoft reserves the right to update the limits…”紧随 USL 身份条件之后，直接支持“有上限但未公布数值”这一事实。这是对证据内容的事实陈述（未列数字），不等同于断言微软永远不会公布阈值。
- **c2_3** [supported] 同一官方指南在计费对比中把 Microsoft 365 Copilot 的 $30/用户/月标注为“Included agent usage”，并以脚注编号指向 fair usage 限制。 [ev_715f3eb3d7b61ff4afca99e5](#ev_715f3eb3d7b61ff4afca99e5)（supports） [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports）
  依据/推导：摘录显示表格行“Microsoft 365 Copilot $30 per user/month Included agent usage1 … Fair Usage Limit4”，属官方指南的标价与脚注结构。仅支持“标价与含额标识”事实，不能推出已实现收入。
- **c2_4** [supported] 微软官方指南上下文将席位含额的适用条件限定为：代理使用者持有 Microsoft 365 Copilot 许可，且代理以该已认证 USL 用户身份运行。 [ev_3673df720bdda4517b7e7b6a](#ev_3673df720bdda4517b7e7b6a)（supports） [ev_935a0e34649f8223ac9ff4f2](#ev_935a0e34649f8223ac9ff4f2)（supports）
  依据/推导：ev_3673df720bdda4517b7e7b6a 的 context_before 原文为“when the user of the agent is licensed with Microsoft 365 Copilot and the agent is operating using the authenticated Microsoft 365 Copilot USL user's identity”；ev_935a0e34649f8223ac9ff4f2 为第三方转载的同段表述，可作交叉印证但非官方来源。身份的限定意味着未持证用户或非认证身份的交互不在含额范围内。
- **c2_5** [supported] 关于 fair usage 的具体阈值，第三方许可分析（LicenseQ）明确称微软不公布确切门槛，并保留更新权利。 [ev_2b4a463b44c816f18025d414](#ev_2b4a463b44c816f18025d414)（supports） [ev_a8a94e42dedbddf77d590df8](#ev_a8a94e42dedbddf77d590df8)（supports）
  依据/推导：LicenseQ 为第三方来源，两句原文直接陈述“does not publish the exact threshold”。该来源与官方指南“受 fair usage 限制、保留更新权”的表述一致，但与任何声称存在公开数值上限的说法相反；本轮未检索到公开数值上限的官方条款。
- **c2_8** [supported] 官方域名托管的 Power Platform 社区论坛中，一位标注为 Microsoft 员工的回帖者称：在 Teams 或 SharePoint 中使用 Copilot Studio 代理无需额外费用，前提是使用为交互式且由用户发起，此时不消耗 Copilot Credits。 [ev_8b335a5d6dfe792d82d57514](#ev_8b335a5d6dfe792d82d57514)（supports）
  依据/推导：该来源 authority 为 vendor_community：官方域名托管、但作者为社区回帖者，不等同于厂商正式发布的许可文档。其内容（交互式、用户发起、Teams/SharePoint）与官方指南方向一致并补充“交互式/用户发起”条件，但仅可作辅助佐证，不能单独用于关闭要求官方条款的缺口。
- **c2_9** [supported] 第三方资料补充称，M365 Copilot 许可下 Copilot Chat、Teams、SharePoint 中的代理使用不计入 Copilot Studio 容量包或计量，但零计费附有条件（身份、触发方式、fair use、CUA 除外）。 [ev_fc79abb7521f8b96f6ef5f71](#ev_fc79abb7521f8b96f6ef5f71)（supports） [ev_f905d26e060d2f79e64e23c9](#ev_f905d26e060d2f79e64e23c9)（supports）
  依据/推导：LICENSEWARE Wiki 与 cloudzero 均为第三方来源，措辞与官方指南一致并补充“CUA 除外”“仅限 B2E”。因非官方，只作对照性证据，不作为条款原文。
- **c3_1** [supported] 微软官方 Microsoft Learn 页面（Standard harness licensing - Microsoft Copilot Studio）称，按量付费（pay-as-you-go）是用 Azure 订阅为 Copilot Studio 付费的一种方式，可让组织在没有许可承诺或预付购买的情况下起步，并在每月月末按代理当月实际使用的 Copilot Credits 数量付费。 [ev_bee02ce5525a79a9fb1fcb29](#ev_bee02ce5525a79a9fb1fcb29)（supports）
  依据/推导：引文出自 learn.microsoft.com 的厂商官方页面，主语是 Copilot Studio 的按量付费方式，明确将 Azure 订阅作为支付载体。仅支持“Azure 订阅支付”这一模式事实，不涉及具体金额。
- **c3_2** [supported] 同一官方页面说明，在 Power Platform 管理中心可通过“计费策略（billing policy）”将环境关联到 Azure 订阅；该计费策略需与 Azure 订阅关联，关联后即通过 Azure 计量开启计费。 [ev_3dc33f3e515e266c56c47bda](#ev_3dc33f3e515e266c56c47bda)（supports） [ev_0f8386aa349ea751d7df3f43](#ev_0f8386aa349ea751d7df3f43)（supports）
  依据/推导：两段引文同出自官方页面，直接陈述“在 Power Platform 管理中心创建与 Azure 订阅关联的计费策略”，构成租户层面的操作前提（需 Azure 订阅、需计费策略）。未说明订阅的计费对象清单细节。
- **c3_3** [supported] 微软官方 Microsoft Learn 页面（Use Capacity Packs vs Pay-as-you-go Billing for Microsoft Copilot Chat）规定：容量包为订阅制产品，每月计费周期开始时补充 25,000 credits；并且每月必须启用 pay-as-you-go 计费作为安全网，以覆盖任何超额用量。 [ev_3d595894cd6911aaf2b2152e](#ev_3d595894cd6911aaf2b2152e)（supports）
  依据/推导：该页面托管于 learn.microsoft.com（vendor_official），但页面标题与内容指向 Microsoft Copilot Chat 的容量包与按量付费计费对比；引文主语为“Copilot Studio Prepaid Capacity packs”的补充规则与“必须启用 pay-as-you-go 作安全网”。应严格保留其页面语境，不将其外推为 Copilot Studio 全部场景或 M365 Copilot 席位的条款。
- **c3_4** [supported] 同一官方页面称，可选地将 Copilot credit policy 与 pay-as-you-go 计费策略配对，以便在预付 credits 用尽时自动进行超额计费；并规定每个租户最多可创建 10 个 Copilot credit policies。 [ev_97087f07fcb63ff1d7799505](#ev_97087f07fcb63ff1d7799505)（supports） [ev_07ff5f0afdea0f470d260aa2](#ev_07ff5f0afdea0f470d260aa2)（supports）
  依据/推导：两段引文同页直接陈述，属官方页面事实。注意措辞为“optionally pair”与“automatic overage billing”，与 ev_3d595894cd6911aaf2b2152e 的“必须启用 pay-as-you-go 作安全网”存在语气差异（必需 vs 可选配对），此处保留两者并作为潜在冲突记录。
- **c3_5** [supported] 第三方文档镜像（GitHub MicrosoftDocs 仓库的 copilot-capacity-packs.md）重复了官方页面的表述：容量包每月补充 25,000 credits，且每月必须启用 pay-as-you-go 计费作为超额兜底。 [ev_be5275736ecd2673b69b55cd](#ev_be5275736ecd2673b69b55cd)（supports） [ev_a49de38d9de863948a87fa24](#ev_a49de38d9de863948a87fa24)（supports）
  依据/推导：两段摘录托管于 github.com，按规则判为 third_party 镜像，不能作为厂商正式发布页面，仅作与官方 learn.microsoft.com 文本的交叉印证。
- **c3_6** [supported] 第三方来源称按量付费须在容量包可用之前处于激活状态，并由全局管理员在 Power Platform 管理中心将 credits 分配到环境；另一第三方来源则称将 Copilot Studio 环境关联到 Azure 订阅即可使用按量付费。 [ev_ad9a87f4cf80e87aab96bd75](#ev_ad9a87f4cf80e87aab96bd75)（supports） [ev_d217285f82cdc0fdc6cd7fdc](#ev_d217285f82cdc0fdc6cd7fdc)（supports）
  依据/推导：两条均为第三方（o365hq、CIAOPS）转述，方向与官方页面一致（Azure 订阅关联 + Power Platform 管理中心分配），但“必须先激活 PAYG 才能用包”的顺序义务未在本轮官方摘录中直接核验到。
- **c4_1** [supported] 微软官方《Microsoft Copilot Studio Licensing Guide》（November 2025）对员工面向（B2E）代理的席位内包含使用仅规定“受 fair usage 限制”，并声明微软保留随产品演进与使用模式变化更新上限的权利；该摘录未给出任何具体数值阈值。 [ev_3673df720bdda4517b7e7b6a](#ev_3673df720bdda4517b7e7b6a)（supports） [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports）
  依据/推导：两段摘录均出自托管于 microsoft.com CDN 的官方许可指南 PDF（vendor_official），直接陈述“Usage is limited to fair usage limits”及保留更新权，全文未出现具体数值。这是对证据内容的陈述（未载明数字），不等于断言微软永不公布阈值。
- **c4_2** [supported] 同一官方指南把席位内包含的适用条件限定为：代理使用者持有 Microsoft 365 Copilot 许可，且代理以该已认证 USL 用户身份运行；含额范围为 Teams、SharePoint、Microsoft 365 Copilot 表面上构建的代理。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_25868af562dd0d2ed0210605](#ev_25868af562dd0d2ed0210605)（supports） [ev_339bdf875fab188660312b7d](#ev_339bdf875fab188660312b7d)（supports）
  依据/推导：官方指南脚注4给出“licensed with Microsoft 365 Copilot … authenticated USL user's identity”的身份条件，脚注5给出 Teams/SharePoint/Microsoft 365 Copilot 的表面范围。该条件以“使用者/身份”为计量基准，但摘录未说明达量统计是按用户还是按租户汇总。
- **c4_3** [supported] 微软官方 Microsoft Learn 页面（Standard harness licensing - Microsoft Copilot Studio）称，若用量超出已购容量，将触发技术性强制执行，可能导致服务被拒绝。 [ev_1cf97f0c464134f53d790214](#ev_1cf97f0c464134f53d790214)（supports）
  依据/推导：引文来自 learn.microsoft.com 官方页面（vendor_official），直接陈述超出“purchased capacity”后的执行后果。限制：主语是已购容量（容量包/容量额度）场景，摘录未把该执行方式与 M365 Copilot 席位内的 fair usage 上限直接挂钩，故不能据此推定席位 fair usage 的超限处理方式。
- **c4_4** [supported] 同一官方 Learn 页面称，持有 Microsoft 365 Copilot 许可的用户在 Copilot Chat、Microsoft Teams 或 SharePoint 中使用代理（经典答案、生成式答案或 Microsoft Graph 租户数据落地）不计入 Copilot Studio 消息包或计量。 [ev_95899b6cf40d7a032858ace6](#ev_95899b6cf40d7a032858ace6)（supports）
  依据/推导：官方页面直接陈述零计费（不计入 pack 或 meter）的范围，但限定于“classic answers / generative answers / Microsoft Graph tenant grounding”这几类用途，且未在该句中提及 fair usage 数值或超限处理。
- **c4_5** [supported] 官方域名托管的 Power Platform 社区问答中，一位标注为 Microsoft 员工的回帖者（Prasad-MSFT）称：若租户启用了 Copilot Studio 计费（credits 或 PAYG），最终用户用量在租户层级计费，代理使用者无需特殊许可。 [ev_57dc177d0ab3247a7f29ac8f](#ev_57dc177d0ab3247a7f29ac8f)（supports）
  依据/推导：该来源 authority 为 vendor_community：托管于 learn.microsoft.com 但作者为社区回帖者，不等同于厂商正式发布的许可文档。其内容指向“租户层级计费”，与席位内按用户身份计费形成对照，但只能作辅助佐证。
- **c5_1** [supported] 微软官方托管于 learn.microsoft.com 的《Supplemental terms of service for enterprise apps and agents》页面开篇仅规定：该应用或代理需持有 Microsoft 365、Microsoft Copilot Studio、Dynamics 365 或 Power Platform 等 Microsoft Online Services 的有效订阅，并受组织 Microsoft 订阅协议（含 Microsoft Product Terms 与数据保护条款）约束；本轮摘录未出现 fair usage 相关条款。 [ev_be27addfb41d2d854c90f2ae](#ev_be27addfb41d2d854c90f2ae)（supports）
  依据/推导：引文为 vendor_official（learn.microsoft.com 法律页），直接陈述订阅前提与管辖协议。摘录仅有该页开头约 1934 字符，未包含 fair usage、计量口径或超限处理内容；因此只能说“本轮摘录未见”，不能断言该页全文不涉 fair usage。
- **c5_3** [supported] 微软官方《Microsoft Copilot Studio Licensing Guide》与 Learn 计费页对席位内代理使用仅规定“受 fair usage 限制”并保留更新上限权利，未给出任何具体数值阈值或算法；官方 Learn 页对“超出已购容量”的表述是触发技术性强制执行、可能导致服务被拒绝，但该表述主语为已购容量（容量包/容量额度），未与 M365 Copilot 席位内 fair usage 直接挂钩。 [ev_3673df720bdda4517b7e7b6a](#ev_3673df720bdda4517b7e7b6a)（supports） [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_1cf97f0c464134f53d790214](#ev_1cf97f0c464134f53d790214)（supports）
  依据/推导：三段均为 vendor_official 摘录。保留原句主语：fair usage 句的主语是员工面向代理的席位内使用；服务拒绝句的主语是超出 purchased capacity，不能把后者移植为 fair usage 的超限处理。
- **c5_5** [supported] 第三方来源称 fair usage 的具体门槛不对外公布、微软保留更新权，并称 M365 Copilot 许可下 Copilot Chat、Teams、SharePoint 的代理使用零计费附有条件（身份、触发方式、fair use、CUA 除外）。 [ev_2b4a463b44c816f18025d414](#ev_2b4a463b44c816f18025d414)（supports） [ev_fc79abb7521f8b96f6ef5f71](#ev_fc79abb7521f8b96f6ef5f71)（supports）
  依据/推导：LicenseQ 与 LicenseWare Wiki 均为 third_party，方向与官方表述一致并补充“CUA 除外”等例外线索，但不能作为条款原文；CUA 例外目前仅此第三方转述支持，无官方原文。
- **c6_1** [supported] 第三方许可资料（LICENSEWARE Wiki）称 Microsoft 365 Copilot 是按用户（per-user）附加许可，必须以 User SL 形式叠加在列明的先决许可（Prerequisite License）之上。 [ev_7167c90735860b7f2afb8b4a](#ev_7167c90735860b7f2afb8b4a)（supports） [ev_389aece00e2d931b4ce5e5e4](#ev_389aece00e2d931b4ce5e5e4)（supports）
  依据/推导：两段摘录同出 wiki.licenseware.io（third_party），原句直接陈述“per-user add-on”与“must sit on top of a listed prerequisite license”。该来源为第三方而非微软正式文档，因此仅作为二手转述记录，不能单独支撑要求官方条款的结论。
- **c6_2** [supported] 该第三方资料引述 Product Terms 的表述：购买所列许可“also require the purchase of a Prerequisite License”；并列举 Microsoft 365 Copilot 的先决许可包括 Microsoft 365 Apps for business/enterprise、Business Basic/Standard/Premium、E3/E5、F1/F3、A1/A3/A5、G3/G5 等，以及 Exchange Online、SharePoint Online、OneDrive 等单件服务。 [ev_75872840a1f4ecd27c63627d](#ev_75872840a1f4ecd27c63627d)（supports） [ev_04cb72d2de1b48e64a584b4d](#ev_04cb72d2de1b48e64a584b4d)（supports）
  依据/推导：摘录的主语是“Product Terms state that…”的转述，而非 Product Terms 原文页面；来源为第三方 wiki。仅支持“该第三方如此转述”的事实，不能作为官方条款原文引用，也不能据此确认先决许可清单的完整性与生效日期。
- **c6_3** [supported] 第三方许可与定价文章（o365hq）同样称 Microsoft 365 Copilot 是附加许可（add-on license），并列出 Microsoft 365 E5/E3/F1/F3、Business Basic/Standard/Premium、Apps for business/enterprise、Office 365 E1/E3/E5/F3 等作为合格基础计划。 [ev_37d9dbe02b1950137794dea6](#ev_37d9dbe02b1950137794dea6)（supports） [ev_bcff011e04cd21c7cb00be57](#ev_bcff011e04cd21c7cb00be57)（supports）
  依据/推导：来源为 o365hq.com（third_party），自述“prices 与 rules 来自微软”，但仍属第三方汇编，非微软正式许可页。支持“该文如此陈述”，与 c6_1/c6_2 方向一致，构成交叉印证而非官方确认。
- **c6_4** [supported] 第三方来源（Orchestry）称：Copilot 不单独出售，只能作为合格基础计划的附加项购买；若用户不在合格订阅上，须先升级基础计划再加购 Copilot。 [ev_946dce0a36ce1a5f13279d59](#ev_946dce0a36ce1a5f13279d59)（supports） [ev_87fa76905700438c3e482fbb](#ev_87fa76905700438c3e482fbb)（supports） [ev_9fd29e9c197ad185a73c53e0](#ev_9fd29e9c197ad185a73c53e0)（supports）
  依据/推导：三条摘录同出 orchestry.com（third_party），原句直接陈述“sold only as an add-on to an eligible base plan”与“先升级基础计划再加 Copilot”。这支持“购买前提含合格基础许可”的定性，但非官方原文。
- **c6_5** [supported] 第三方来源（Orchestry）区分两类 Copilot 附加许可的适用企业用户范围：Microsoft 365 Copilot Business 面向少于 300 席位且使用 Business 计划（Business Basic/Standard/Premium）的组织，席位上限约 300；企业版 Microsoft 365 Copilot 附加项面向 E3/E5 租户且无席位上限。 [ev_59d23c2bc88c1f8d1231af8e](#ev_59d23c2bc88c1f8d1231af8e)（supports） [ev_b5bcae3dea16e74dc14470f5](#ev_b5bcae3dea16e74dc14470f5)（supports） [ev_4dc8e527a95c4faf0cf67ac8](#ev_4dc8e527a95c4faf0cf67ac8)（supports）
  依据/推导：摘录直接陈述“under 300 seats”“no seat ceiling”与基础计划对应关系，主谓与时态（2026 年文章语境）与来源标题一致。仅支持“该第三方如此划分”，不能作为微软官方席位上限或资格条款；亦不支持任何最低席位数要求。
- **c6_6** [supported] 同一第三方来源称：Microsoft 365 Copilot 为按用户每月计费的附加许可，企业版价格为每用户每月 30 美元、按年承诺（annual term）；不含付费 Copilot 体验为默认，免费网页版 Copilot Chat 随合格订阅提供。 [ev_df6406ac549944a098e0ca73](#ev_df6406ac549944a098e0ca73)（supports） [ev_2e1662ea4613766104561886](#ev_2e1662ea4613766104561886)（supports） [ev_cdc87a4ad909fe64ffe42398](#ev_cdc87a4ad909fe64ffe42398)（supports） [ev_1e9f76cf2b6ea6c661f5ef2a](#ev_1e9f76cf2b6ea6c661f5ef2a)（supports）
  依据/推导：摘录直接陈述 $30/user/month 与“annual term”，属标价与合同期事实，来源为第三方；不能推出已实现收入或利润。此前已校验的官方许可指南（ev_5a440717841727e42686e122）亦标注同一 $30/user/month 与 annual 计费单位，可作方向印证，但该官方摘录未展开年度承诺条款原文。
- **c6_7** [supported] 该第三方 wiki 同时提示材料层级：Product Terms 是合同性来源，Microsoft Learn 页面为教育性内容。 [ev_0143166912ecb88fe0a69287](#ev_0143166912ecb88fe0a69287)（supports）
  依据/推导：原句直接陈述两类资料的效力层级，可用于说明为何本轮大量先决许可材料只能作二手转述。注意该判断本身出自第三方 wiki 作者，而非微软表述。
- **c6_9** [supported] 关于“最低席位数”，本轮已校验证据中没有任何一条陈述 Microsoft 365 Copilot 附加许可存在最低席位数门槛；第三方材料只给出 Business 版“至多 300 席位”的上限描述。 [ev_4dc8e527a95c4faf0cf67ac8](#ev_4dc8e527a95c4faf0cf67ac8)（supports） [ev_b5bcae3dea16e74dc14470f5](#ev_b5bcae3dea16e74dc14470f5)（supports）
  依据/推导：本条仅描述证据的覆盖情况：现有摘录涉及席位的是“up to 300”与“no cap”。按规则不得将“未见最低席位要求”解释为该要求不存在，故仅陈述为证据缺口，不作出否定性事实结论。
- **c7_1** [supported] 第三方许可资料（LICENSEWARE Wiki）称 Microsoft 365 Copilot 以每用户附加许可（per-user add-on）形式销售，须作为 User SL 叠加在列明的先决许可之上；该页同处并称现行 Microsoft Learn 页面将该产品称为 Microsoft Copilot，并描述为「available as an add-on plan with one of the licensing prerequisites」。 [ev_c9e53c158964c047e830ea79](#ev_c9e53c158964c047e830ea79)（supports） [ev_6af0e2875999956ff2571b26](#ev_6af0e2875999956ff2571b26)（supports）
  依据/推导：两段摘录同出 wiki.licenseware.io（third_party）。第二句的主语是「该 wiki 转述 Microsoft Learn 页面」，是对 Learn 措辞的二手引用而非 Learn 原文；因此本条只能支持「第三方如此转述」，不能充当 Microsoft Learn 许可页的直接表述。
- **c7_2** [supported] 该第三方 wiki 摘录把先决许可概括为「A listed Microsoft 365, Office 365 or standalone service license (Product Terms)」，并以 Product Terms 作为合同性来源、Learn 页面为教育性内容。 [ev_fb3a95aea3d25159bb5badb6](#ev_fb3a95aea3d25159bb5badb6)（supports） [ev_0143166912ecb88fe0a69287](#ev_0143166912ecb88fe0a69287)（supports）
  依据/推导：摘录为 wiki 信息框式概括，括号内自注来源为 Product Terms，但本条摘录本身不是 Product Terms 原文页；且「Learn 为教育性」这一层级判断出自第三方作者而非微软。故仅支持第三方概括事实。
- **c7_3** [supported] 第三方定价文章（o365hq）称 Microsoft 365 Copilot 为附加许可，并称微软的 license-options 文章列出的合格基础计划多于一般预期，列出 Microsoft 365 E5/E3/F1/F3、Business Basic/Standard/Premium、Apps for business/enterprise、Office 365 E1/E3/E5/F3、Teams Essentials/Enterprise/EEA、Exchange Kiosk 与 Plans 1/2、SharePoint Kiosk 与 Plans 1/2、OneDrive Plans 1/2、Planner Plan 1、Project Plans 3/5、Visio Plans 1/2 及 Clipchamp 等。 [ev_844f483a559a99b3171b3658](#ev_844f483a559a99b3171b3658)（supports）
  依据/推导：来源为 o365hq.com（third_party），自述价格与规则源自微软，但仍是第三方汇编。其「微软 license-options 文章列出」为转述，并非该 Learn 页原文摘录，故不能记为官方直接表述；清单疑有截断（如 Exchange/SharePoint 段落在摘录边界处），完整性无法确认。
- **c7_4** [supported] 第三方来源（Orchestry）称 Microsoft 365 Copilot Business 许可面向少于 300 席位、使用 Business 计划（Business Basic/Standard/Premium）的组织，席位上限「Up to 300」；企业版 Microsoft 365 Copilot 附加项面向 E3/E5 租户且「no seat ceiling」。 [ev_a1dd93632d4ee6ca432f71f9](#ev_a1dd93632d4ee6ca432f71f9)（supports）
  依据/推导：摘录直接陈述席位上限与基础计划对应关系，主语与时态与来源标题一致；来源为 third_party，仅支持「该第三方如此陈述」，不构成微软官方 300 席位上限条款。
- **c7_5** [supported] 第三方资料（TechTarget）称 Microsoft 365 Copilot 于 2023 年 11 月首次发布时要求 300 席位起购，并称「This is no longer the case」，即当前不再设该最低购买量。 [ev_a64aff1fa2abb464ed775caa](#ev_a64aff1fa2abb464ed775caa)（supports）
  依据/推导：原文直接陈述历史最低购量与现状变化，来源为 third_party。该句是否定式陈述（不再有 300 席位起购），但并非微软正式条款原文，也未被官方许可选项页或 Product Terms 摘录核验；且不能由此推出「绝无任何最低席位要求」。
- **c8_1** [supported] 本轮唯一的 Microsoft Learn「License options for Microsoft Copilot」页面相关证据，是第三方 wiki（LICENSEWARE Wiki）参考文献条目对该页的描述：「Prerequisite plan lists; Copilot Chat web-based and work-based. Educational. Effective 2026-09-25.」——它仅说明该页存在先决计划清单与 Copilot Chat 内容，并未给出清单原文或席位数条款。 [ev_e238d62591daa69fa3dd995e](#ev_e238d62591daa69fa3dd995e)（supports）
  依据/推导：ev_e238d62591daa69fa3dd995e 出自 wiki.licenseware.io（third_party），是参考文献条目而非 Learn 页面正文；主语是该第三方对该页的概述。只能支持「第三方如此描述该页」这一事实，不能充当 Learn 原文引用，也不能据以判断清单内容或席位下限。
- **c8_2** [supported] 本轮证据中转述的「先决许可」清单全部来自第三方：LICENSEWARE Wiki 引述 Product Terms 称所列许可「also require the purchase of a Prerequisite License」，并列举 Microsoft 365 Apps for business/enterprise、Business Basic/Standard/Premium、F1/F3/A1/A3/A5/A7/E3/E5/E7/G3/G5/G7、Office 365 F3/A1/A3/A5/E1/E3/E5/G3/G5，以及 Exchange Online、SharePoint Online、OneDrive、Clipchamp、Teams EEA/Enterprise/Essentials、Planner Plan 1、Project Online、Visio Online；o365hq 给出的清单与之部分重合但含 Exchange/SharePoint/OneDrive 的 Kiosk 与分档计划、Project Plans 3/5、Visio Plans 1/2 等。 [ev_958595bf35613f88c3b7c837](#ev_958595bf35613f88c3b7c837)（supports） [ev_04cb72d2de1b48e64a584b4d](#ev_04cb72d2de1b48e64a584b4d)（supports） [ev_37d9dbe02b1950137794dea6](#ev_37d9dbe02b1950137794dea6)（supports） [ev_bcff011e04cd21c7cb00be57](#ev_bcff011e04cd21c7cb00be57)（supports）
  依据/推导：三份来源（LICENSEWARE Wiki、o365hq）均为 third_party，且均为对 Product Terms 或 license-options 文章的二手转述；两份清单在具体计划条目与日期脚注（G3/G5 于 2026-08-01、A7/G7 于 2026-10-01 加入）上不一致且摘录存在截断，完整性无法确认。本条只陈述「第三方如何转述」，不认定清单为官方原文。
- **c8_3** [supported] 本轮证据中没有出现 Microsoft Learn「License options for Microsoft Copilot」页面关于最低席位数要求的任何原文；关于最低席位的直接表述仅见于第三方：TechTarget 称 2023 年 11 月首发时要求 300 席位起购、现已不再如此；Orchestry 称 Business 版「Up to 300」上限、企业版「no seat ceiling」。 [ev_a64aff1fa2abb464ed775caa](#ev_a64aff1fa2abb464ed775caa)（supports） [ev_1e9f76cf2b6ea6c661f5ef2a](#ev_1e9f76cf2b6ea6c661f5ef2a)（supports） [ev_a1dd93632d4ee6ca432f71f9](#ev_a1dd93632d4ee6ca432f71f9)（supports）
  依据/推导：按规则不将「证据中未见」解释为「不存在最低席位要求」；此条仅为证据覆盖情况的事实陈述。300 席「起购下限」与 300 席「Business 版上限」是不同合同维度，三方来源无法相互印证官方口径，冲突保留（见 c8_6）。
- **c8_4** [supported] 官方域名托管的 Microsoft Q&A 问答中，提问者（匿名，2023-09-22）转述其「Microsoft Modern Work Digital Specialist」所称 M365 Copilot 最低购买 300 席位，并询问是否属实；这是用户提问而非微软答复或正式文档。 [ev_46fc73195360c49a44fa23ed](#ev_46fc73195360c49a44fa23ed)（supports）
  依据/推导：该来源 authority 为 vendor_community：托管于 learn.microsoft.com 但作者为社区匿名提问者，内容是对他人口头说法的转述。按规则不得等同厂商正式许可文档，也不能单独关闭要求官方条款的缺口；本条只用于说明「300 席位」说法的流传来源之一，不证明其真实性。
- **c9_1** [supported] 第三方（Orchestry）称 Microsoft 365 Copilot Business 许可面向少于 300 席位、使用 Business 计划（Business Basic/Standard/Premium）的组织，并给出“Seat cap Up to 300”与“~$21 (annual)”的价格-席位对应描述。 [ev_59d23c2bc88c1f8d1231af8e](#ev_59d23c2bc88c1f8d1231af8e)（supports） [ev_4dc8e527a95c4faf0cf67ac8](#ev_4dc8e527a95c4faf0cf67ac8)（supports）
  依据/推导：摘录主语为 Business 版、时态与来源标题一致；来源为 third_party，只能支持“该第三方如此陈述”，不构成微软官方条款原文。$21 仅为标价事实，不能推出已实现收入。
- **c9_2** [supported] 该第三方同段称企业版 Microsoft 365 Copilot 附加项面向 E3/E5 租户且“carries no seat ceiling”，即无席位上限。 [ev_b5bcae3dea16e74dc14470f5](#ev_b5bcae3dea16e74dc14470f5)（supports）
  依据/推导：原文直接陈述“no seat ceiling”，主语是企业版附加项、前提是 E3/E5；第三方来源，仅作转述记录。
- **c9_3** [supported] 另一第三方（o365hq）称“Microsoft's catalog description”将 Microsoft 365 Copilot Business 封顶在 300 席位，与 Business 计划的上限相同。 [ev_166813518580a59f6256b9bd](#ev_166813518580a59f6256b9bd)（supports）
  依据/推导：主语是“微软目录描述”，但本条摘录只是该第三方对目录描述的重述，并非目录或定价页原文；只能支持“该第三方如此转述目录描述”。
- **c9_4** [supported] 第三方（GoSearch）称 Microsoft 365 Copilot Business 服务于在合格 Microsoft 365 商业计划上、席位至多 300 的组织。 [ev_c0d336f062fcce549653b15a](#ev_c0d336f062fcce549653b15a)（supports）
  依据/推导：与 c9_1/c9_3 方向一致，同为 third_party，构成交叉印证而非官方确认。
- **c9_5** [supported] 第三方（GoSearch FAQ）称 Business 档计划（Basic、Standard、Premium）每租户封顶 300 席位，并称超过该阈值的组织必须基于 E3、E5 或等效企业基础许可来授权 Copilot Enterprise，“不存在 Business 层级的规模化路径”。 [ev_1d9855225f2f3116cb81e2a7](#ev_1d9855225f2f3116cb81e2a7)（supports） [ev_b00a44a6daf6f8f84ea505b0](#ev_b00a44a6daf6f8f84ea505b0)（supports）
  依据/推导：这是本轮唯一直接描述超限后处理方式的表述，但主语是 Business 计划席位上限与“必须”迁移的转述，来源为 third_party；原文还自承“once confirmed”等未确认措辞，不能当作官方规则。
- **c9_6** [supported] 第三方（ciotech）称 Business 家族计划合计最多可配置 300 个席位，到第 301 个用户时 Microsoft 365 并不会停止工作，但不能简单再增加 Business 家族许可，成长型企业通常开始把用户迁往 E3/E5 等企业计划。 [ev_286fdf8f77550881b5178118](#ev_286fdf8f77550881b5178118)（supports） [ev_be069ac21d3d5f4c2a1000a6](#ev_be069ac21d3d5f4c2a1000a6)（supports）
  依据/推导：两段同源摘录，主语为 Microsoft 365 Business 家族计划（非专门针对 Copilot Business SKU），超限的处理被描述为“通常”而非强制。不能把该关于基础计划的表述直接移植为 Copilot Business 许可条款。
- **c9_7** [supported] 同一第三方还称 300 席位上限“适用于 Business 家族合计”，且混合许可可行——不必把全部员工迁到 Microsoft 365 E3。 [ev_ea14a30bc5363deb444ee829](#ev_ea14a30bc5363deb444ee829)（supports） [ev_85088fee5d5ef65625153602](#ev_85088fee5d5ef65625153602)（supports）
  依据/推导：原文直接陈述“no, 300 applies across the Business family in total”与“Mixed licensing is possible”。与 c9_5 的“必须迁移”表述方向不一致，冲突在下条保留。
- **c9_8** [supported] 官方域名托管的 Microsoft Q&A 中，匿名提问者（2023-09-22）转述其 Microsoft Modern Work Digital Specialist 称 M365 Copilot 最低购买 300 席位，并询问是否属实；这是用户提问，不是微软答复或正式文档，且指向的是“最低购买量”而非“Business 版上限”。 [ev_28314414cc27dbbe8fa2d7b8](#ev_28314414cc27dbbe8fa2d7b8)（supports）
  依据/推导：来源为 vendor_community，作者为社区匿名提问者，托管平台为官方域名但内容非厂商发布，不得等同正式许可文档；且其所述维度（起购下限）与 Business 版上限不同，不能相互替代。
- **c9_9** [supported] 第三方（TechTarget）称 Microsoft 365 Copilot 2023 年 11 月首发时要求 300 席位起购，并称“This is no longer the case”。 [ev_a64aff1fa2abb464ed775caa](#ev_a64aff1fa2abb464ed775caa)（supports）
  依据/推导：此为“起购下限已取消”的第三方陈述，与 300 席作为 Business 版上限属不同合同维度；未被官方条款核验，也不构成“绝无最低席位要求”的结论。

## 推导

- **c1_6** [supported] 综合上述，Copilot Studio 的收费单位是租户级共享的 Copilot Credits（按容量包或按量付费），其购买/启用前提是租户已有的组织级订阅与 Azure 订阅计量；而 Microsoft 365 Copilot 的收费单位是每用户每月 30 美元的席位。二者计费维度不同：前者随使用量扩展，后者随人数扩展。 [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports） [ev_69933db511a7d22a4dd584c9](#ev_69933db511a7d22a4dd584c9)（supports） [ev_4e0ed4de864a34274c45b16f](#ev_4e0ed4de864a34274c45b16f)（supports） [ev_be5275736ecd2673b69b55cd](#ev_be5275736ecd2673b69b55cd)（supports）
  依据/推导：由官方指南所列并列计费模式与三份第三方对租户级额度、Azure 计量的描述推导。限制：官方摘录未完整覆盖 Azure 订阅前提的正式措辞，Azure 前提主要依赖第三方，因此属推导而非纯官方事实。
- **c2_6** [supported] 综合官方指南：内部代理（employee-facing）使用含于 M365 Copilot 席位的边界是“使用表面（Teams/SharePoint/M365 Copilot）+ 使用者持证 + 代理以该用户已认证身份运行”，且受未公布数值的 fair usage 约束；一旦超出上述任一条件，即不再落入席位含额。 [ev_339bdf875fab188660312b7d](#ev_339bdf875fab188660312b7d)（supports） [ev_3673df720bdda4517b7e7b6a](#ev_3673df720bdda4517b7e7b6a)（supports） [ev_935a0e34649f8223ac9ff4f2](#ev_935a0e34649f8223ac9ff4f2)（supports）
  依据/推导：由官方脚注5的含额范围与脚注4的 fair usage 条件合并推导。限制：官方摘录未在同一段落说明超限后的计费归属（是否转入 Copilot Credits 计量），该环节仍属未决，故本条只描述含额的适用边界。
- **c2_7** [supported] 关于“正式条款原文发布在何处”：本轮证据表明，公平使用与席位含额的表述出现在微软托管于 cdn-dynmedia-1.microsoft.com 的《Microsoft Copilot Studio Licensing Guide》PDF 中，而非独立的公开产品条款页；该 PDF 属厂商官方许可指南类资料。 [ev_715f3eb3d7b61ff4afca99e5](#ev_715f3eb3d7b61ff4afca99e5)（supports） [ev_3673df720bdda4517b7e7b6a](#ev_3673df720bdda4517b7e7b6a)（supports）
  依据/推导：source_metadata 显示该 PDF 的 URL 属 microsoft.com 域名、标题含 “Licensing Guide November 2025”，摘录自带“§PDF page 8§”分页标记。限制：本轮仅核验到该许可指南，未核验是否存在 Product Terms / 服务条款页对同一事项另行规定，故不能断言该指南即为唯一或最高效力的条款载体。
- **c3_7** [supported] 就本问题所问的租户前提与 Azure 前置条件，官方 Learn 页面可支持的要素为：存在 Azure 订阅作为计费载体、在 Power Platform 管理中心创建与该 Azure 订阅关联的计费策略、以及容量包场景下以 pay-as-you-go 作为超额兜底（每租户至多 10 个 Copilot credit policies）。 [ev_bee02ce5525a79a9fb1fcb29](#ev_bee02ce5525a79a9fb1fcb29)（supports） [ev_3dc33f3e515e266c56c47bda](#ev_3dc33f3e515e266c56c47bda)（supports） [ev_3d595894cd6911aaf2b2152e](#ev_3d595894cd6911aaf2b2152e)（supports） [ev_07ff5f0afdea0f470d260aa2](#ev_07ff5f0afdea0f470d260aa2)（supports）
  依据/推导：由三段官方页面事实合并推导。限制：官方摘录未给出“Azure 订阅本身的前置条件”（如订阅类型、计费账户权限、是否需 Azure AD 租户绑定）的条文字句，也未给出超额启用是否为强制性合同义务的正式条款措辞。
- **c3_8** [mixed] 官方页面之间对“pay-as-you-go 用于超额”的性质表述存在张力：一侧称“每月必须启用 pay-as-you-go 作为安全网”，另一侧称可“可选”地将 credit policy 与 pay-as-you-go 配对以实现自动超额计费；证据不足以判定何者构成合同义务。 [ev_3d595894cd6911aaf2b2152e](#ev_3d595894cd6911aaf2b2152e)（supports） [ev_97087f07fcb63ff1d7799505](#ev_97087f07fcb63ff1d7799505)（contradicts）
  依据/推导：两条均出自厂商官方页面，但一处为必需性表述、一处为可选性表述，且可能分属不同产品范围（Copilot Chat 容量包 vs Copilot Studio 容量包与 credit policy 组合）。按规则保留冲突，不以任一表述单方面定性为正式义务。
- **c4_6** [mixed] 就可执行性与计量口径而言，本轮官方来源可支持的是：席位内代理使用有 fair usage 这一上限约束、但无公开数值；达量执行的公开表述指向“超出已购容量则技术性强制（可致服务拒绝）”；而按用户身份（licensed user + authenticated identity）判定是否落入席位含额，按租户层级计量的表述仅见于官方域名托管的社区回帖，非正式条款。 [ev_3673df720bdda4517b7e7b6a](#ev_3673df720bdda4517b7e7b6a)（supports） [ev_1cf97f0c464134f53d790214](#ev_1cf97f0c464134f53d790214)（supports） [ev_57dc177d0ab3247a7f29ac8f](#ev_57dc177d0ab3247a7f29ac8f)（contradicts）
  依据/推导：官方指南以用户持证与认证身份为含额条件，暗示以用户为判定单位；社区回帖则称最终用户用量在租户层级计费。二者分属不同计费情境（席位含额判定 vs 已启用 credits/PAYG 后的计费层级），但现有证据不足以判定 fair usage 本身按用户还是按租户计量，故标为 mixed 并保留张力。
- **c4_7** [supported] 关于“Product Terms 或服务条款页是否给出可执行上限”：本轮证据中，fair usage 的表述载体是微软托管的《Microsoft Copilot Studio Licensing Guide》PDF 与 Microsoft Learn 计费页，未检索到 Product Terms 或独立服务条款页对席位内代理 fair usage 的数值、计量口径与超限处理作出规定。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_1cf97f0c464134f53d790214](#ev_1cf97f0c464134f53d790214)（supports）
  依据/推导：由现有证据的载体类型归纳：相关表述位于官方许可指南与 Learn 计费页，未见 Product Terms 原文。限制：本轮未穷尽检索，故只能表述为“本轮证据中未见”，不能断言此类条款不存在。
- **c5_2** [supported] 该补充条款页把具体服务条款指向 Microsoft Product Terms 与订阅协议，本页本身不作为 fair usage 上限数值、计量口径或超限处理的条款载体；本轮亦未检索到 Product Terms 原文对此作出规定。 [ev_be27addfb41d2d854c90f2ae](#ev_be27addfb41d2d854c90f2ae)（supports） [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports）
  依据/推导：由该页“受订阅协议包括 Microsoft Product Terms 约束”的指引性表述，结合本轮及此前证据中 fair usage 表述仅见于许可指南 PDF 与 Learn 计费页，归纳推导。限制：本轮检索未穷尽，故只表述为“本轮未见”，不能断言 Product Terms 不存在此类条款。
- **c5_4** [mixed] 关于计量口径，官方指南以“代理使用者持 M365 Copilot 许可且代理以该已认证 USL 用户身份运行”作为落入席位含额的判定条件，属按用户身份判定；而“最终用户用量按租户层级计费”的说法仅见于官方域名托管的社区回帖（作者为 Microsoft 员工，但非正式发布文档），本轮仍无官方条款说明 fair usage 本身按用户还是按租户计量。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_57dc177d0ab3247a7f29ac8f](#ev_57dc177d0ab3247a7f29ac8f)（contradicts）
  依据/推导：两份证据分属不同情境（席位含额判定 vs 已启用 credits/PAYG 后的计费层级），方向存在张力；vendor_community 不能单独关闭要求官方条款的缺口，故标为 mixed 并保留冲突。
- **c6_8** [supported] 综合本轮证据：Microsoft 365 Copilot 席位的收费单位是“每用户/月”，其购买前提在方向上是一致的——必须叠加在合格 Microsoft 365/Office 365 基础许可之上，不能单独购买；适用企业用户范围存在“Business 版（<300 席位、Business 基础计划）”与“企业版（E3/E5、无席位上限）”的分野。 [ev_7167c90735860b7f2afb8b4a](#ev_7167c90735860b7f2afb8b4a)（supports） [ev_946dce0a36ce1a5f13279d59](#ev_946dce0a36ce1a5f13279d59)（supports） [ev_59d23c2bc88c1f8d1231af8e](#ev_59d23c2bc88c1f8d1231af8e)（supports） [ev_b5bcae3dea16e74dc14470f5](#ev_b5bcae3dea16e74dc14470f5)（supports）
  依据/推导：由三份互相独立的第三方来源一致陈述推导（席位计费单位、附加前提、Business/企业分流）。限制：三份均为 third_party，无微软许可选项页或 Product Terms 原文核验，因此该推导的证据基座为二手，不能替代官方条款。
- **c7_6** [mixed] 就本轮所问的四项内容，可核验到的公开表述层级是：先决基础许可清单与「按用户附加、不可单独购买」由第三方转述（含对 Product Terms 与 license-options 文章的二手引用）；300 席位上限只见于第三方对 Business 版适用范围的描述；最低席位数的唯一直接表述来自第三方称 2023 年 11 月的 300 席起购已不再适用；而 Microsoft Learn「License options for Microsoft Copilot」或 Copilot 定价页的直接原文，在本轮证据中一条也未出现。 [ev_c9e53c158964c047e830ea79](#ev_c9e53c158964c047e830ea79)（supports） [ev_844f483a559a99b3171b3658](#ev_844f483a559a99b3171b3658)（supports） [ev_a1dd93632d4ee6ca432f71f9](#ev_a1dd93632d4ee6ca432f71f9)（supports） [ev_a64aff1fa2abb464ed775caa](#ev_a64aff1fa2abb464ed775caa)（contradicts） [ev_fb3a95aea3d25159bb5badb6](#ev_fb3a95aea3d25159bb5badb6)（contradicts）
  依据/推导：综合各条转述的方向一致性，同时保留冲突：c6_9 此前已记录本轮之前证据中「未见最低席位门槛」，而 TechTarget 明确称曾要求 300 席位起购后已取消；另有来源把 300 描述为 Business 版上限而非起购下限，两者是不同的合同维度，现有证据无法判定何者构成官方规则。故本条标为 mixed：四项要件均未被官方原文直接表述，缺口未被实质回答。
- **c7_7** [supported] 关于按年承诺条款：本轮证据仅在第三方材料中出现「$30/user/month … annual term」与「~$21 (annual) / $30 (annual)」的价格-期限组合描述，未见任何 Microsoft Learn 许可页或 Copilot 定价页对年度承诺期限作出直接表述。 [ev_a1dd93632d4ee6ca432f71f9](#ev_a1dd93632d4ee6ca432f71f9)（supports）
  依据/推导：由现有证据的载体类型与内容归纳：年度期限仅作为价格表的括号注释出现，属定价事实层面的二手描述，未被条款原文核验。限制：本轮未穷尽检索，故只表述为「本轮证据中未见」，不能断言官方页面未载该条款。
- **c8_5** [supported] 就可核验范围而言：Microsoft 365 Copilot 作为按用户附加许可、须叠加合格基础许可，在本轮仍只有第三方转述支撑（含对 Learn 措辞的二手引用「available as an add-on plan with one of the licensing prerequisites」）；而本轮子问题所问的 Learn「License options for Microsoft Copilot」页面原文——无论是先决基础许可清单本身，还是是否存在最低席位数要求——均未取得。 [ev_958595bf35613f88c3b7c837](#ev_958595bf35613f88c3b7c837)（supports） [ev_e238d62591daa69fa3dd995e](#ev_e238d62591daa69fa3dd995e)（supports）
  依据/推导：由本轮及此前已校验摘录的载体类型归纳：所有清单与席位表述的载体均为 third_party，Learn 页面仅以参考文献条目形式被提及。限制：本轮未穷尽检索，故只表述为「本轮未取得」，不推断该页无相关表述；据此 gap3 不得关闭。
- **c8_6** [mixed] 关于席位数量存在方向性冲突但未被官方裁断：一方（TechTarget）称 300 席最低购量已于发布后取消；另一方（Orchestry）把 300 描述为 Business 版上限、企业版无上限；而 2023 年社区提问则显示当时市场确曾流传 300 席最低购买的说法。现有证据不足以判定微软官方当前是否存在任何最低席位数要求。 [ev_a64aff1fa2abb464ed775caa](#ev_a64aff1fa2abb464ed775caa)（supports） [ev_a1dd93632d4ee6ca432f71f9](#ev_a1dd93632d4ee6ca432f71f9)（contradicts） [ev_46fc73195360c49a44fa23ed](#ev_46fc73195360c49a44fa23ed)（supports）
  依据/推导：三份来源分别来自 third_party 与 vendor_community，均非微软正式条款；300 作「下限」与作「Business 版上限」分属不同维度，不可互相替代。按规则保留冲突，不以任一说法单方面结论化，也不以假设关闭缺口。
- **c9_10** [mixed] 就本轮所问的两项要件：300 席位上限的表述在本轮仅以第三方转述形式出现（Orchestry、o365hq、GoSearch、ciotech），其中 o365hq 明确称其来源是“微软目录描述”，但本轮未取得该目录或 Copilot 定价页原文；超限后的处理方式，第三方之间一说是“必须基于 E3/E5 授权企业版、无 Business 规模化路径”，一说是“混合许可可行、企业通常迁往 E3/E5”。 [ev_b00a44a6daf6f8f84ea505b0](#ev_b00a44a6daf6f8f84ea505b0)（supports） [ev_85088fee5d5ef65625153602](#ev_85088fee5d5ef65625153602)（contradicts） [ev_166813518580a59f6256b9bd](#ev_166813518580a59f6256b9bd)（supports）
  依据/推导：三方来源均非官方，且对“是否强制迁移”给出方向相反的表述；“上限”与“起购下限”也分属不同维度。按规则保留冲突，不单方面定性为官方强制迁移规则。限制：本轮未检索到 Copilot 定价页或 Product Terms 原文。
- **c9_11** [supported] 关于“是否强制迁移至企业版附加项”：本轮没有任何官方条款原文支持“强制迁移”，最接近的表述出自第三方 GoSearch 且带自我保留措辞；因此该问题在官方层面仍未被实质回答。 [ev_b00a44a6daf6f8f84ea505b0](#ev_b00a44a6daf6f8f84ea505b0)（supports） [ev_a1dd93632d4ee6ca432f71f9](#ev_a1dd93632d4ee6ca432f71f9)（supports）
  依据/推导：由证据载体类型归纳：强制迁移说仅见于 third_party，官方来源（Learn 页、许可指南）本轮未被检索到相关条款。限制：只表述为“本轮未见”，不推断官方无此类规定。

## 商业判断

- **c1_8** [supported] 这种“席位费+租户级用量费”的双层结构可能使微软收入同时具备可预测的每用户经常性收入与随代理使用增长的使用量收入；但代理用量收入受内部含额与 fair usage 上限约束，未必随席位数线性放大。 [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports） [ev_69933db511a7d22a4dd584c9](#ev_69933db511a7d22a4dd584c9)（supports）
  依据/推导：基于计费单位事实的商业判断，非已实现收入或利润；价格与容量包标价不能等同于实际收入。限制：缺乏官方使用量数据与转化率证据。
- **c2_11** [supported] 席位内包含受 fair usage 约束的内部代理使用，意味着这部分用量不直接转化为 Copilot Credits 计量收入；企业的代理用量增长若长期停留在席位含额内，微软从该客户获得的增量收入主要仍来自席位扩张，仅当用量或场景越出含额边界时才可能转向容量包/按量计费收入。 [ev_339bdf875fab188660312b7d](#ev_339bdf875fab188660312b7d)（supports） [ev_3673df720bdda4517b7e7b6a](#ev_3673df720bdda4517b7e7b6a)（supports） [ev_69933db511a7d22a4dd584c9](#ev_69933db511a7d22a4dd584c9)（supports）
  依据/推导：基于官方含额与 fair usage 事实的商业判断，不涉及已实现收入或利润，也未量化转化率；$30 标价仅为定价事实。
- **c4_9** [supported] 由于席位内 fair usage 上限未见公开数值且未与 Copilot Credits 计量直接挂钩，企业在席位内扩张内部代理使用的边际成本不可事前精确预测，这既可能抑制企业将高用量场景留在席位内，也可能促使其在用量增长后转向容量包或按量计费，从而把收入从席位费部分转移到用量费；但该转移是否发生及规模缺乏数据，不能等同于已实现收入。 [ev_3673df720bdda4517b7e7b6a](#ev_3673df720bdda4517b7e7b6a)（supports） [ev_95899b6cf40d7a032858ace6](#ev_95899b6cf40d7a032858ace6)（supports）
  依据/推导：基于官方 fair usage 无公开数值与零计费范围事实的商业判断，不涉及已实现收入或利润，也未量化转化率与价格敏感性。
- **c5_6** [supported] 由于官方补充条款页未提供 fair usage 的可执行数值、计量口径与超限处理，企业在规划代理规模化使用时无法事前精确测算席位内用量的边际成本与越界风险，这可能压低企业把高用量场景留在席位内的意愿，并在用量越界后转向容量包或按量计费；该转移规模缺乏数据，不能等同于已实现收入。 [ev_be27addfb41d2d854c90f2ae](#ev_be27addfb41d2d854c90f2ae)（supports） [ev_3673df720bdda4517b7e7b6a](#ev_3673df720bdda4517b7e7b6a)（supports） [ev_1cf97f0c464134f53d790214](#ev_1cf97f0c464134f53d790214)（supports）
  依据/推导：基于官方条款可执行性缺失与超容量强制执行的商业判断，不涉及已实现收入或利润，未量化转化率。
- **c6_11** [supported] 从扩展使用看，M365 Copilot 席位费随“人数”线性放大且必须先有基础许可，因此企业扩展时的增量成本＝基础许可升级＋每席位附加费，这使收入来源以可预测的每用户经常性收入为主；而 Copilot Studio 侧重租户级用量计费，其扩展不要求为每个使用者加购席位。两类产品因此呈现“按人扩展”与“按用量扩展”的不同收入弹性。 [ev_946dce0a36ce1a5f13279d59](#ev_946dce0a36ce1a5f13279d59)（supports） [ev_9fd29e9c197ad185a73c53e0](#ev_9fd29e9c197ad185a73c53e0)（supports） [ev_df6406ac549944a098e0ca73](#ev_df6406ac549944a098e0ca73)（supports） [ev_69933db511a7d22a4dd584c9](#ev_69933db511a7d22a4dd584c9)（supports）
  依据/推导：基于席位计费/基础许可前提事实与既有结论 c1_3（Copilot Studio 租户级共享 credits 计价）的商业判断；$30 仅为标价，不构成收入或利润推断，未量化转化率。
- **c7_8** [supported] 若先决基础许可清单、最低席位与年度承诺只能通过第三方转述获知，企业客户在做席位规模测算与多年度预算时须自行向微软渠道确认合同约束，这会拉长采购决策周期并偏向先做小规模试点；对微软而言，附加许可叠加在基础许可之上意味着席位扩展的收入同时带动基础订阅与附加费两条线，但该判断基于标价与转述的合同结构，不等于已实现收入或利润。 [ev_c9e53c158964c047e830ea79](#ev_c9e53c158964c047e830ea79)（supports） [ev_a1dd93632d4ee6ca432f71f9](#ev_a1dd93632d4ee6ca432f71f9)（supports）
  依据/推导：基于「附加许可须叠基础许可」与「席位/年度信息仅有转述」两项事实的商业判断，不涉及收入或利润推断；采购周期与试点偏好属判断而非已证事实，无量化数据。
- **c8_8** [supported] 在企业采购层面，先决基础许可清单的宽度决定了企业「加购 Copilot」时是否需要先做基础计划升级、进而影响每个席位的实际增量成本结构；清单越宽（含单件服务与低档计划），企业越可能从存量订阅直接加购而不升级主体套件。但由于本轮未取得官方清单原文，企业据以做席位规模与预算测算的仍属转述信息，这会延长确认环节、偏向先小规模试点，并可能使席位扩张的收入同时体现在基础订阅与附加费两条线上；该判断基于标价与转述的许可结构，不等于已实现收入或利润。 [ev_37d9dbe02b1950137794dea6](#ev_37d9dbe02b1950137794dea6)（supports） [ev_958595bf35613f88c3b7c837](#ev_958595bf35613f88c3b7c837)（supports）
  依据/推导：基于「附加许可须叠在合格基础许可之上」「清单宽窄存在第三方不同版本」两项事实的商业判断，未涉及收入或利润推断，也无量化转化率；采购周期与试点偏好属判断而非已证事实。
- **c9_13** [supported] 若 300 席位确为 Copilot Business 的硬上限，则接近该规模的客户在扩容时会被推向 E3/E5 基础许可＋企业版附加项，单席位标价从约 $21 升至 $30（均为标价，非已实现收入），同时带动基础订阅升级；这会提高扩容阶段的客单价，但也可能促使客户在临界规模前提前规划、延后购买或采用混合许可。以上为商业判断，不涉及已实现收入或利润。 [ev_4dc8e527a95c4faf0cf67ac8](#ev_4dc8e527a95c4faf0cf67ac8)（supports） [ev_1d9855225f2f3116cb81e2a7](#ev_1d9855225f2f3116cb81e2a7)（supports） [ev_85088fee5d5ef65625153602](#ev_85088fee5d5ef65625153602)（supports）
  依据/推导：基于第三方给出的标价与席位上限事实的商业判断；价格仅为标价，混合许可以及客户行为均无量化数据支撑。

## 待验证假设

- **c1_7** [unverified] 若企业已为员工购买 M365 Copilot 席位，则内部代理使用可能包含在席位内（第三方称零费率），从而抑制 Copilot Studio Credits 的额外消耗；外部/未授权用户的代理交互才更可能触发按量计费。 [ev_2455574e039ae9be1eeb4886](#ev_2455574e039ae9be1eeb4886)（supports） [ev_9df58eb62473d172cd6dcf1d](#ev_9df58eb62473d172cd6dcf1d)（supports）
  依据/推导：第三方提到“M365 Copilot licensed users 的 Copilot Studio agent use zero-rated”及“internal agent use 含在许可证中”，但缺乏官方条款直接佐证具体边界与 fair usage 限制，故保留为待验证假设。
- **c2_10** [unverified] fair usage 阈值虽未公布，但微软可能在合同或内部计量层面按每用户或每租户的交互量设定软上限，并可能通过限流、要求追加容量包或在续约时调整上限来执行。 [ev_a8a94e42dedbddf77d590df8](#ev_a8a94e42dedbddf77d590df8)（supports）
  依据/推导：仅第三方指出“保留更新权、客户无法预先强制”。官方摘录未披露执行机制，故列为待验证假设，不以假设关闭缺口。
- **c3_9** [unverified] 按量付费与容量包所要求的租户前提可能还包括：组织具备可用的 Azure 订阅与计费权限、环境归属到 Power Platform 管理中心内可管理范围，以及超额时由 Azure 计费账户承接；这些前置条件的具体效力来源可能载于 Product Terms 或 Azure 计费账户条款，而非仅 Learn 操作页。 [ev_3dc33f3e515e266c56c47bda](#ev_3dc33f3e515e266c56c47bda)（supports） [ev_bee02ce5525a79a9fb1fcb29](#ev_bee02ce5525a79a9fb1fcb29)（supports）
  依据/推导：现有证据只展示操作路径（Azure 订阅 + 计费策略），未展示条文字句，故将“前置条件的正式效力来源”列为待验证假设，不以假设关闭缺口。
- **c4_8** [unverified] fair usage 的具体阈值可能不对外公布，且其执行可能依身份、交互类型与用量模式在合同或内部计量层面裁量，超限后可能转为限流、要求追加容量或按量计费。 [ev_3673df720bdda4517b7e7b6a](#ev_3673df720bdda4517b7e7b6a)（supports）
  依据/推导：官方指南只保留更新权而未披露阈值与执行机制，超限处理的具体路径在官方摘录中缺失，故列为待验证假设，不以假设关闭缺口。
- **c6_10** [unverified] Microsoft 365 Copilot 附加许可可能确实不设最低席位数，而按年承诺为主要合同约束；且 Business 版 300 席位上限若被超过，客户可能被要求迁移到企业版附加项。 [ev_4dc8e527a95c4faf0cf67ac8](#ev_4dc8e527a95c4faf0cf67ac8)（supports） [ev_cdc87a4ad909fe64ffe42398](#ev_cdc87a4ad909fe64ffe42398)（supports）
  依据/推导：两项均为对未明示事项的推测：席位下限在证据中缺席，年度承诺的具体条款原文未取得；超过 300 席位后的处理方式亦无证据。故列为待验证假设，不以假设关闭任何缺口。
- **c8_7** [unverified] Microsoft Learn「License options for Microsoft Copilot」页面所列先决计划可能比第三方常见清单更宽（例如包含 Project、Visio、Clipchamp 等单件服务），且该页可能不设最低席位门槛、而以按年承诺为主要合同约束。 [ev_e238d62591daa69fa3dd995e](#ev_e238d62591daa69fa3dd995e)（supports） [ev_37d9dbe02b1950137794dea6](#ev_37d9dbe02b1950137794dea6)（supports） [ev_cdc87a4ad909fe64ffe42398](#ev_cdc87a4ad909fe64ffe42398)（supports）
  依据/推导：第三方称该页「lists more qualifying plans than most people assume」并把 annual term 与价格并列，但均属二手转述，未取得页面原文；故列为待验证假设，不以假设关闭 gap3。
- **c9_12** [unverified] 300 席位上限可能源自 Business 基础计划本身的租户上限（叠加到 Copilot Business 适用范围的延伸），超限后客户可能需为超出部分改用 E3/E5 基础许可并加购企业版 Copilot 附加项；也可能仅需混合许可而不必整体迁移。 [ev_be069ac21d3d5f4c2a1000a6](#ev_be069ac21d3d5f4c2a1000a6)（supports） [ev_85088fee5d5ef65625153602](#ev_85088fee5d5ef65625153602)（supports）
  依据/推导：两项均为对未由官方条款明示事项的推测，且第三方内部存在张力；仅依据第三方对 Business 家族上限的描述，故列为待验证假设，不以假设关闭缺口。

## 证据缺口

- gap0 [open] Microsoft 365 Copilot 与 Copilot Studio 面向的企业使用者、收费单位和购买前提有何区别？这些差异可能如何影响企业客户扩展使用和微软的收入来源？优先使用官方资料；将价格与许可事实、基于事实的推导、商业判断和仍待验证假设明确区分，不把产品定价直接当成已实现收入或利润。
- gap1 [open] 缺少微软官方（非 GitHub 镜像、非第三方博客）对 Copilot Studio 按量付费/容量包所要求的租户前提与 Azure 订阅前置条件的正式条款原文，以及官方对 internal agent use 是否含在 M365 Copilot 席位内、fair usage 上限的具体规定。
- gap2 [open] 缺少微软官方（Product Terms、服务条款或正式许可条款页，而非营销/许可指南 PDF 的摘要脚注）对 fair usage 上限的执行方式与可接受使用量的正式条款原文，包括是否按用户/租户计量、超限后的处理（限流、计费或要求追加容量）以及 CUA 等例外情形。
- gap3 [open] 缺少微软官方（Microsoft 365 企业版许可选项页、Microsoft Product Terms 或 Copilot 定价页原文，而非第三方 wiki/博客）对 Microsoft 365 Copilot 附加许可先决基础许可清单、是否存在最低席位数、按年承诺条款以及 Business 版 300 席位上限的正式表述；本轮相关陈述全部来自 third_party 转述。
- gap4 [open] 缺微软官方条款对 Copilot Business 版 300 席位上限的正式表述及其超限后的处理方式（例如是否强制迁移至企业版附加项），现有证据仅为第三方对 Business 与企业版适用范围的对照描述。

## 问题与检索记录

- q0 / 第 0 轮 / 缺口 初始问题：Microsoft 365 Copilot 与 Copilot Studio 面向的企业使用者、收费单位和购买前提有何区别？这些差异可能如何影响企业客户扩展使用和微软的收入来源？优先使用官方资料；将价格与许可事实、基于事实的推导、商业判断和仍待验证假设明确区分，不把产品定价直接当成已实现收入或利润。
- q1 / 第 1 轮 / 缺口 gap0：微软官方如何说明 Copilot Studio 的计费单位与购买前提（例如按消息/容量包计费所需的 Azure 订阅或租户前提），与 Microsoft 365 Copilot 按用户席位收费的模式相比有何不同？
  Tavily search1：Copilot Studio licensing messages capacity pack；结果 5；错误 无
- q2 / 第 2 轮 / 缺口 gap1：微软官方对 Microsoft 365 Copilot 席位内所含 Copilot Studio 内部代理（internal agent）使用范围与 fair usage 上限是如何规定的？其正式条款原文发布在何处？
  Tavily search2：Microsoft 365 Copilot internal agent use Copilot Studio licensing；结果 5；错误 无
- q3 / 第 3 轮 / 缺口 gap1：微软官方对 Copilot Studio 按量付费与容量包所要求的租户前提和 Azure 订阅前置条件（如计费策略、Azure 订阅绑定、超额启用义务）的正式条文原文是什么？
- q4 / 第 4 轮 / 缺口 gap2：微软官方 Product Terms 或服务条款页是否对 Microsoft 365 Copilot 席位内包含的 Copilot Studio 代理使用量（fair usage）给出可执行的具体上限、计量口径（按用户还是按租户）和超限处理方式？
  Tavily search3：Microsoft Product Terms Copilot Studio agent fair usage；结果 5；错误 无
- q5 / 第 5 轮 / 缺口 gap2：微软官方补充条款页（Supplemental terms of service for enterprise apps and agents）是否对 Microsoft 365 Copilot 席位内 Copilot Studio 代理使用的 fair usage 给出可执行条款（上限数值或算法、按用户或按租户计量、超限后的限流/计费/追加容量处理、CUA 等例外）？
  Tavily search4：Microsoft 365 supplemental terms enterprise agents fair usage；结果 5；错误 无
- q6 / 第 6 轮 / 缺口 gap0：微软官方（Microsoft 365 企业版许可或 Copilot 产品页/许可指南）如何界定 Microsoft 365 Copilot 席位的适用企业用户范围与购买前提（如所需的 M365 基础许可级别、最低席位数、按年承诺）？
  Tavily search5：Microsoft 365 Copilot prerequisites base license；结果 5；错误 无
- q7 / 第 7 轮 / 缺口 gap3：微软官方 Microsoft 365 Copilot 许可页（Microsoft Learn「License options for Microsoft Copilot」或 Copilot 定价页）如何直接表述 M365 Copilot 附加许可的先决基础许可清单、是否存在最低席位数、按年承诺条款以及 Business 版 300 席位上限？
  Tavily search6：Microsoft 365 Copilot licensing prerequisites seat minimum；结果 5；错误 无
- q8 / 第 8 轮 / 缺口 gap3：微软官方 Microsoft Learn「License options for Microsoft Copilot」页面原文如何表述 Microsoft 365 Copilot 附加许可所需的基础许可清单，以及是否存在最低席位数要求？
  Tavily search7：Microsoft Copilot license options prerequisites；结果 5；错误 无
- q9 / 第 9 轮 / 缺口 gap4：微软官方 Microsoft 365 Copilot Business 许可（或 Copilot 定价页）是否明文设定 300 席位上限？若组织席位数超过该上限，官方规定如何处理（是否强制迁移至企业版 E3/E5 附加项）？
  Tavily search8：Microsoft 365 Copilot Business 300 seats limit；结果 5；错误 无
- q10 / 第 10 轮 / 缺口 gap4：微软官方 Microsoft 365 Copilot Business FAQ 页（learn.microsoft.com/en-us/microsoft-365/copilot/copilot-business-faq）是否明文写明 Copilot Business 的 300 席位上限及其达到或超过上限后的官方处理方式？
  Tavily search9：Copilot Business FAQ 300 seats；结果 5；错误 无

## 原文摘录与追溯

<a id="ev_7d1d68228d013e72f6062cf1"></a>
### ev_7d1d68228d013e72f6062cf1

> Microsoft 365 Copilot $30 per user/month Included agent usage1 Pay-as-you-go: unlimited2 License (capacity pack): 25,000 Copilot Credit /pack3

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q1 → 分块 chk_c68aacefe8ad1e6fd48eeabb_13260 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [13714, 13856)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_2455574e039ae9be1eeb4886"></a>
### ev_2455574e039ae9be1eeb4886

> Copilot Studio currency changed from messages to Copilot Credit

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q1 → 分块 chk_76369ce0f3851a65c00a0b8b_10710 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [11247, 11310)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_f6a6c699c377aa3df987621e"></a>
### ev_f6a6c699c377aa3df987621e

> Agents are a second, consumption layer: Copilot Chat agents, SharePoint agents and Copilot Studio agents are metered in Copilot Credits, paid from prepaid capacity packs, pay-as-you-go through an Azure subscription, or a one-year pre-purchase plan.

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q1 → 分块 chk_76369ce0f3851a65c00a0b8b_1530 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [1695, 1943)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_9df58eb62473d172cd6dcf1d"></a>
### ev_9df58eb62473d172cd6dcf1d

> For external agent deployment, a standalone licence is priced at $200 per 25,000 Copilot Credits per month. Pay-as-you-go via Azure is also available. As of September 2025, Copilot Credits replaced the older per-message billing model.

来源：Microsoft Copilot Pricing Explained: Plans, Cost & Licensing (2026 Guide) — https://copilot-experts.com/microsoft-copilot-pricing-guide/

类型：web；读取时间：2026-10-19T08:34:53.971800+00:00；截断：False

问题 q1 → 分块 chk_ac5bf6d7ca3223d80201c6bc_38760 → 来源 src_ac5bf6d7ca3223d80201c6bc；清洗后字符 [38981, 39215)

SHA-256：`7fe833d081a4bedc364caa3ac22c186729714bd1900164aa122d9ec96c067acb`；范围：<body> element; characters 0-41267 of 41267

获取链：运行 23c904aac0c6 → 问题 q3 → 搜索 search1 → https://copilot-experts.com/microsoft-copilot-pricing-guide
检索词：Microsoft 365 Copilot pricing per user；当时的问题：微软官方 Microsoft 365 Copilot 产品页/价目页是否公开标明企业版为每用户每月 30 美元、Copilot Business 为每用户每月约 21 美元（年付），并说明按席位计费与适用版本？

<a id="ev_1dbf5c764a2b1b5f40f3ab0e"></a>
### ev_1dbf5c764a2b1b5f40f3ab0e

> What you pay $360 per user per year (Copilot Business: $252) at the September 2026 list Microsoft's meter on your Azure subscription, $0.01 per message $2,400 per year per pack at list, plus pay-as-you-go for overage

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q1 → 分块 chk_ba995cac346030f043dc84c6_8670 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [9001, 9217)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_be5275736ecd2673b69b55cd"></a>
### ev_be5275736ecd2673b69b55cd

> Replenishment: Copilot Studio capacity packs are subscription products. At the start of every monthly billing period, your 25,000 credits are replenished. You must have pay-as-you-go billing active as a safety net each month to cover any excess usage.

来源：microsoft-365-docs/copilot/pay-as-you-go/copilot-capacity-packs.md at public · MicrosoftDocs/microsoft-365-docs · GitHub — https://github.com/MicrosoftDocs/microsoft-365-docs/blob/public/copilot/pay-as-you-go/copilot-capacity-packs.md

类型：web；读取时间：2026-10-19T08:29:15.341631+00:00；截断：False

问题 q1 → 分块 chk_f8f12eda37b72bebb9444fce_4590 → 来源 src_f8f12eda37b72bebb9444fce；清洗后字符 [4694, 4945)

SHA-256：`a95cb3d5b68b10d3964f7df866ebf3d53a12a749e413633907d8f91d3cbb7bf3`；范围：<main> element; characters 0-13057 of 13057

获取链：运行 d968652bc210 → 问题 q8 → 搜索 search7 → https://github.com/MicrosoftDocs/microsoft-365-docs/blob/public/copilot/pay-as-you-go/copilot-capacity-packs.md
检索词：Copilot Studio capacity pack Azure subscription requirement；当时的问题：微软官方文档是否明确 Copilot Studio 容量包（Copilot Credit 容量包，每包 25,000 信用）与预购 Commit Units 路径在使用代理时同样需要 Azure 订阅，而不仅是按量付费计量需要？

<a id="ev_4e0ed4de864a34274c45b16f"></a>
### ev_4e0ed4de864a34274c45b16f

> Organizational Copilot Studio subscription (Pay‑As‑You‑Go or Message Pack) must be enabled in the tenant. Metered charges (Copilot Credits) are incurred against the organizational capacity / Azure subscription.

来源：Copilot Agents licensing usage update – CIAOPS — https://blog.ciaops.com/2025/12/01/copilot-agents-licensing-usage-update/

类型：web；读取时间：2026-10-19T08:44:11.506662+00:00；截断：False

问题 q1 → 分块 chk_55bc3f900451bb732ad9f33f_2550 → 来源 src_55bc3f900451bb732ad9f33f；清洗后字符 [2789, 2999)

SHA-256：`aff02aa8d8069060cf183230347eebfb4c2b1964a6d577db976f6d7503cefd78`；范围：<main> element; characters 0-8495 of 8495

获取链：运行 c498744f19ea → 问题 q1 → 搜索 search1 → https://blog.ciaops.com/2025/12/01/copilot-agents-licensing-usage-update
检索词：Copilot Studio licensing messages capacity pack；当时的问题：微软官方如何说明 Copilot Studio 的计费单位与购买前提（例如按消息/容量包计费所需的 Azure 订阅或租户前提），与 Microsoft 365 Copilot 按用户席位收费的模式相比有何不同？

<a id="ev_69933db511a7d22a4dd584c9"></a>
### ev_69933db511a7d22a4dd584c9

> Copilot Studio is priced per credit, pooled at the tenant level, not per seat. The cost depends on how your agents consume credits, not how many people interact with them.

来源：Microsoft Copilot Studio Pricing In 2026: Credits, Plans, And Costs — https://www.cloudzero.com/blog/copilot-studio-pricing/

类型：web；读取时间：2026-10-19T08:23:25.388083+00:00；截断：False

问题 q1 → 分块 chk_5de6a402648eeec2266bf20a_3570 → 来源 src_5de6a402648eeec2266bf20a；清洗后字符 [3913, 4084)

SHA-256：`cb19d183bd1edd7576e299f6598b444a3200c932fb28102ca2d84e1e3314d183`；范围：<main> element; characters 0-19388 of 19388

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.cloudzero.com/blog/copilot-studio-pricing
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_3673df720bdda4517b7e7b6a"></a>
### ev_3673df720bdda4517b7e7b6a

> Usage is limited to fair usage limits. Microsoft reserves the right to update the limits as the product evolves, and new usage patterns emerge.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q2 → 分块 chk_c68aacefe8ad1e6fd48eeabb_15300 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [15594, 15737)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_339bdf875fab188660312b7d"></a>
### ev_339bdf875fab188660312b7d

> Agents built on Copilot Studio, for Teams, SharePoint and Microsoft 365 Copilot, are included with the Microsoft 365 Copilot user license at no additional char

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q2 → 分块 chk_c68aacefe8ad1e6fd48eeabb_15300 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [15741, 15900)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_715f3eb3d7b61ff4afca99e5"></a>
### ev_715f3eb3d7b61ff4afca99e5

> Copilot Studio use rights with Microsoft 365 Copilot Plans • MCS Pay-As-You-Go • MCS License (Copilot Credit capacity pack) • Copilot Credit Pre-Purchase Plan Microsoft 365 Copilot $30 per user/month Included agent usage1 Pay-as-you-go: unlimited2 License (capacity pack): 25,000 Copilot Credit /pack3 Pre

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q2 → 分块 chk_c68aacefe8ad1e6fd48eeabb_13260 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [13555, 13860)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_a8a94e42dedbddf77d590df8"></a>
### ev_a8a94e42dedbddf77d590df8

> Employee-facing Copilot Studio usage covered by the Microsoft 365 Copilot User SL is gated by a fair-use limit Microsoft does not publish and explicitly reserves the right to update.

来源：Copilot Studio Licensing | Explained by Licensing Expert — https://licenseq.com/copilot-studio-licensing/

类型：web；读取时间：2026-10-19T08:44:19.697467+00:00；截断：False

问题 q2 → 分块 chk_be03c5b67dd2b4fe8530e90d_9690 → 来源 src_be03c5b67dd2b4fe8530e90d；清洗后字符 [9813, 9995)

SHA-256：`56c234622dddeedd6d7055b85ceb6bdb7bd1df68db79be59a596ab47d1f8fc2d`；范围：<main> element; characters 0-17908 of 17908

获取链：运行 c498744f19ea → 问题 q1 → 搜索 search1 → https://licenseq.com/copilot-studio-licensing
检索词：Copilot Studio licensing messages capacity pack；当时的问题：微软官方如何说明 Copilot Studio 的计费单位与购买前提（例如按消息/容量包计费所需的 Azure 订阅或租户前提），与 Microsoft 365 Copilot 按用户席位收费的模式相比有何不同？

<a id="ev_2b4a463b44c816f18025d414"></a>
### ev_2b4a463b44c816f18025d414

> The catch is “fair usage”. Microsoft does not publish the exact threshold, and reserves the right to update it as patterns emerge.

来源：Copilot Studio Licensing | Explained by Licensing Expert — https://licenseq.com/copilot-studio-licensing/

类型：web；读取时间：2026-10-19T08:44:19.697467+00:00；截断：False

问题 q2 → 分块 chk_be03c5b67dd2b4fe8530e90d_5610 → 来源 src_be03c5b67dd2b4fe8530e90d；清洗后字符 [5926, 6056)

SHA-256：`56c234622dddeedd6d7055b85ceb6bdb7bd1df68db79be59a596ab47d1f8fc2d`；范围：<main> element; characters 0-17908 of 17908

获取链：运行 c498744f19ea → 问题 q1 → 搜索 search1 → https://licenseq.com/copilot-studio-licensing
检索词：Copilot Studio licensing messages capacity pack；当时的问题：微软官方如何说明 Copilot Studio 的计费单位与购买前提（例如按消息/容量包计费所需的 Azure 订阅或租户前提），与 Microsoft 365 Copilot 按用户席位收费的模式相比有何不同？

<a id="ev_935a0e34649f8223ac9ff4f2"></a>
### ev_935a0e34649f8223ac9ff4f2

> Employee-facing usage scenarios (Business to Employee) of Copilot Studio agents and Copilot Studio tools and features that these agents invoke are included in the Microsoft 365 Copilot USL when the user of the agent is licensed with Microsoft 365 Copilot, and the agent operates using the authenticated Microsoft 365 Copilot USL user’s identity. Usage is limited to fair usage limits.

来源：Article - Copilot Agents, Developer T... — https://services.northwestern.edu/TDClient/30/Portal/KB/Article/2879/Copilot-Agents-Developer-Tools-Sharing-Publishing-and-Message-Consumption

类型：web；读取时间：2026-10-19T08:25:23.206842+00:00；截断：False

问题 q2 → 分块 chk_7e9a2016729ec629a6069173_12240 → 来源 src_7e9a2016729ec629a6069173；清洗后字符 [12407, 12791)

SHA-256：`5e7f77f4b6eb7ba1580d3e124bf34f9731f751d8e737a903c4455cdc5db94043`；范围：<main> element; characters 0-14774 of 14774

获取链：运行 d968652bc210 → 问题 q3 → 搜索 search3 → https://services.northwestern.edu/TDClient/30/Portal/KB/Article/2879/Copilot-Agents-Developer-Tools-Sharing-Publishing-and-Message-Consumption
检索词：Microsoft Product Terms Copilot Studio included agent usage；当时的问题：微软官方 Product Terms 或完整许可条款中，Microsoft 365 Copilot 每席位“Included agent usage”对应的具体 Copilot Credit 数量是多少，公平使用限制（fair usage limit）如何定义、触发后有何后果？

<a id="ev_559c66e41ae49989b83bc970"></a>
### ev_559c66e41ae49989b83bc970

> If your users hold the Microsoft 365 Copilot User SL ($30/user/month), they already have Copilot Studio use rights for employee-facing agents , Teams, SharePoint, M365 Copilot, at no extra charge. Agents built for those surfaces, operating under the licensed user’s identity, are covered.

来源：Copilot Studio Licensing | Explained by Licensing Expert — https://licenseq.com/copilot-studio-licensing/

类型：web；读取时间：2026-10-19T08:44:19.697467+00:00；截断：False

问题 q2 → 分块 chk_be03c5b67dd2b4fe8530e90d_5610 → 来源 src_be03c5b67dd2b4fe8530e90d；清洗后字符 [5637, 5925)

SHA-256：`56c234622dddeedd6d7055b85ceb6bdb7bd1df68db79be59a596ab47d1f8fc2d`；范围：<main> element; characters 0-17908 of 17908

获取链：运行 c498744f19ea → 问题 q1 → 搜索 search1 → https://licenseq.com/copilot-studio-licensing
检索词：Copilot Studio licensing messages capacity pack；当时的问题：微软官方如何说明 Copilot Studio 的计费单位与购买前提（例如按消息/容量包计费所需的 Azure 订阅或租户前提），与 Microsoft 365 Copilot 按用户席位收费的模式相比有何不同？

<a id="ev_fc79abb7521f8b96f6ef5f71"></a>
### ev_fc79abb7521f8b96f6ef5f71

> Microsoft Learn states that Microsoft 365 Copilot licensed use of agents in Copilot Chat, Teams or SharePoint does not count against the Copilot Studio pack or meter, but the zero-rating has conditions (identity, trigger, fair use, CUA excluded).

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q2 → 分块 chk_76369ce0f3851a65c00a0b8b_5101 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [5289, 5535)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_f905d26e060d2f79e64e23c9"></a>
### ev_f905d26e060d2f79e64e23c9

> internal agent interactions by licensed users don’t consume Copilot Credits. Classic answers, generative answers, grounding, agent actions, agent flows, all included within Teams, SharePoint, and Copilot Chat, subject to fair usage limits. This only covers employ

来源：Microsoft Copilot Studio Pricing In 2026: Credits, Plans, And Costs — https://www.cloudzero.com/blog/copilot-studio-pricing/

类型：web；读取时间：2026-10-19T08:23:25.388083+00:00；截断：False

问题 q2 → 分块 chk_5de6a402648eeec2266bf20a_4590 → 来源 src_5de6a402648eeec2266bf20a；清洗后字符 [4927, 5190)

SHA-256：`cb19d183bd1edd7576e299f6598b444a3200c932fb28102ca2d84e1e3314d183`；范围：<main> element; characters 0-19388 of 19388

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.cloudzero.com/blog/copilot-studio-pricing
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_8b335a5d6dfe792d82d57514"></a>
### ev_8b335a5d6dfe792d82d57514

> Yes , with Microsoft 365 Copilot licenses , you can use Copilot Studio agents in Teams or SharePoint at no additional cost, as long as the usage is interactive and initiated by the user .

来源：Power Platform Community Forum Thread Details — https://community.powerplatform.com/forums/thread/details/?threadid=bc7d0d19-4921-f111-8342-7ced8dcf6527

类型：web；读取时间：2026-10-19T08:24:49.983894+00:00；截断：False

问题 q2 → 分块 chk_1a66581da9f76a510025eaf3_2040 → 来源 src_1a66581da9f76a510025eaf3；清洗后字符 [2386, 2573)

SHA-256：`f7337cddce4c9ebdb5b2eab78399442aedc3bec6ad4f72b526beb15faa6b880d`；范围：<body> element; characters 0-6584 of 6584

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://community.powerplatform.com/forums/thread/details?threadid=bc7d0d19-4921-f111-8342-7ced8dcf6527
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_bee02ce5525a79a9fb1fcb29"></a>
### ev_bee02ce5525a79a9fb1fcb29

> Pay-as-you-go is a way to pay for Copilot Studio by using an Azure subscription.

来源：Standard harness licensing - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing

类型：web；读取时间：2026-10-19T08:45:20.764545+00:00；截断：False

问题 q3 → 分块 chk_0c9308874a087eda76e3ffa2_3060 → 来源 src_0c9308874a087eda76e3ffa2；清洗后字符 [3166, 3246)

SHA-256：`bd97d5a5eb6b73c5509af73942801a58576a809050ce94f139c18b173ae4f67d`；范围：<main> element; characters 0-7004 of 7004

获取链：运行 c498744f19ea → 问题 q2 → 搜索 search2 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing
检索词：Microsoft 365 Copilot internal agent use Copilot Studio licensing；当时的问题：微软官方对 Microsoft 365 Copilot 席位内所含 Copilot Studio 内部代理（internal agent）使用范围与 fair usage 上限是如何规定的？其正式条款原文发布在何处？

<a id="ev_3dc33f3e515e266c56c47bda"></a>
### ev_3dc33f3e515e266c56c47bda

> In the Power Platform admin center, you can link environments to an Azure subscription by using a billing policy.

来源：Standard harness licensing - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing

类型：web；读取时间：2026-10-19T08:45:20.764545+00:00；截断：False

问题 q3 → 分块 chk_0c9308874a087eda76e3ffa2_3060 → 来源 src_0c9308874a087eda76e3ffa2；清洗后字符 [3521, 3634)

SHA-256：`bd97d5a5eb6b73c5509af73942801a58576a809050ce94f139c18b173ae4f67d`；范围：<main> element; characters 0-7004 of 7004

获取链：运行 c498744f19ea → 问题 q2 → 搜索 search2 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing
检索词：Microsoft 365 Copilot internal agent use Copilot Studio licensing；当时的问题：微软官方对 Microsoft 365 Copilot 席位内所含 Copilot Studio 内部代理（internal agent）使用范围与 fair usage 上限是如何规定的？其正式条款原文发布在何处？

<a id="ev_3d595894cd6911aaf2b2152e"></a>
### ev_3d595894cd6911aaf2b2152e

> You must have pay-as-you-go billing active as a safety net each month to cover any excess usage.

来源：Use Capacity Packs vs Pay-as-you-go Billing for Microsoft Copilot Chat | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/copilot-capacity-packs

类型：web；读取时间：2026-10-19T08:44:14.390633+00:00；截断：False

问题 q3 → 分块 chk_40c65badfe4b5f9302da4ec9_6631 → 来源 src_40c65badfe4b5f9302da4ec9；清洗后字符 [6931, 7027)

SHA-256：`e4cc25355e7cccc38e74ff20c800b4270dbe55c50eb9ac47897ea1a603e60a13`；范围：<main> element; characters 0-18860 of 18860

获取链：运行 c498744f19ea → 问题 q1 → 搜索 search1 → https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/copilot-capacity-packs
检索词：Copilot Studio licensing messages capacity pack；当时的问题：微软官方如何说明 Copilot Studio 的计费单位与购买前提（例如按消息/容量包计费所需的 Azure 订阅或租户前提），与 Microsoft 365 Copilot 按用户席位收费的模式相比有何不同？

<a id="ev_97087f07fcb63ff1d7799505"></a>
### ev_97087f07fcb63ff1d7799505

> You can optionally pair a Copilot credit policy with a pay-as-you-go billing policy for automatic overage billing when prepaid credits run out.

来源：Use Capacity Packs vs Pay-as-you-go Billing for Microsoft Copilot Chat | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/copilot-capacity-packs

类型：web；读取时间：2026-10-19T08:44:14.390633+00:00；截断：False

问题 q3 → 分块 chk_40c65badfe4b5f9302da4ec9_4591 → 来源 src_40c65badfe4b5f9302da4ec9；清洗后字符 [4626, 4769)

SHA-256：`e4cc25355e7cccc38e74ff20c800b4270dbe55c50eb9ac47897ea1a603e60a13`；范围：<main> element; characters 0-18860 of 18860

获取链：运行 c498744f19ea → 问题 q1 → 搜索 search1 → https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/copilot-capacity-packs
检索词：Copilot Studio licensing messages capacity pack；当时的问题：微软官方如何说明 Copilot Studio 的计费单位与购买前提（例如按消息/容量包计费所需的 Azure 订阅或租户前提），与 Microsoft 365 Copilot 按用户席位收费的模式相比有何不同？

<a id="ev_07ff5f0afdea0f470d260aa2"></a>
### ev_07ff5f0afdea0f470d260aa2

> Tenant limit : You can create up to 10 Copilot credit policies per tenant.

来源：Use Capacity Packs vs Pay-as-you-go Billing for Microsoft Copilot Chat | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/copilot-capacity-packs

类型：web；读取时间：2026-10-19T08:44:14.390633+00:00；截断：False

问题 q3 → 分块 chk_40c65badfe4b5f9302da4ec9_4591 → 来源 src_40c65badfe4b5f9302da4ec9；清洗后字符 [4864, 4938)

SHA-256：`e4cc25355e7cccc38e74ff20c800b4270dbe55c50eb9ac47897ea1a603e60a13`；范围：<main> element; characters 0-18860 of 18860

获取链：运行 c498744f19ea → 问题 q1 → 搜索 search1 → https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/copilot-capacity-packs
检索词：Copilot Studio licensing messages capacity pack；当时的问题：微软官方如何说明 Copilot Studio 的计费单位与购买前提（例如按消息/容量包计费所需的 Azure 订阅或租户前提），与 Microsoft 365 Copilot 按用户席位收费的模式相比有何不同？

<a id="ev_0f8386aa349ea751d7df3f43"></a>
### ev_0f8386aa349ea751d7df3f43

> You need to create a billing policy associated with your Azure subscription in Power Platform admin center.

来源：Standard harness licensing - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing

类型：web；读取时间：2026-10-19T08:45:20.764545+00:00；截断：False

问题 q3 → 分块 chk_0c9308874a087eda76e3ffa2_4080 → 来源 src_0c9308874a087eda76e3ffa2；清洗后字符 [4410, 4517)

SHA-256：`bd97d5a5eb6b73c5509af73942801a58576a809050ce94f139c18b173ae4f67d`；范围：<main> element; characters 0-7004 of 7004

获取链：运行 c498744f19ea → 问题 q2 → 搜索 search2 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing
检索词：Microsoft 365 Copilot internal agent use Copilot Studio licensing；当时的问题：微软官方对 Microsoft 365 Copilot 席位内所含 Copilot Studio 内部代理（internal agent）使用范围与 fair usage 上限是如何规定的？其正式条款原文发布在何处？

<a id="ev_ad9a87f4cf80e87aab96bd75"></a>
### ev_ad9a87f4cf80e87aab96bd75

> Pay-as-you-go must be active before a pack can be used, and a Global Administrator allocates the credits to environments in the Power Platform admin center.

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q3 → 分块 chk_ba995cac346030f043dc84c6_5100 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [5335, 5491)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_d217285f82cdc0fdc6cd7fdc"></a>
### ev_d217285f82cdc0fdc6cd7fdc

> Copilot Studio Pay-As-You-Go (PAYG): Link a Copilot Studio environment to an Azure subscription.

来源：Copilot Agents licensing usage update – CIAOPS — https://blog.ciaops.com/2025/12/01/copilot-agents-licensing-usage-update/

类型：web；读取时间：2026-10-19T08:44:11.506662+00:00；截断：False

问题 q3 → 分块 chk_55bc3f900451bb732ad9f33f_1530 → 来源 src_55bc3f900451bb732ad9f33f；清洗后字符 [2019, 2115)

SHA-256：`aff02aa8d8069060cf183230347eebfb4c2b1964a6d577db976f6d7503cefd78`；范围：<main> element; characters 0-8495 of 8495

获取链：运行 c498744f19ea → 问题 q1 → 搜索 search1 → https://blog.ciaops.com/2025/12/01/copilot-agents-licensing-usage-update
检索词：Copilot Studio licensing messages capacity pack；当时的问题：微软官方如何说明 Copilot Studio 的计费单位与购买前提（例如按消息/容量包计费所需的 Azure 订阅或租户前提），与 Microsoft 365 Copilot 按用户席位收费的模式相比有何不同？

<a id="ev_a49de38d9de863948a87fa24"></a>
### ev_a49de38d9de863948a87fa24

> You must have pay-as-you-go billing active as a safety net each month to cover any excess usage.

来源：microsoft-365-docs/copilot/pay-as-you-go/copilot-capacity-packs.md at public · MicrosoftDocs/microsoft-365-docs · GitHub — https://github.com/MicrosoftDocs/microsoft-365-docs/blob/public/copilot/pay-as-you-go/copilot-capacity-packs.md

类型：web；读取时间：2026-10-19T08:29:15.341631+00:00；截断：False

问题 q3 → 分块 chk_f8f12eda37b72bebb9444fce_4590 → 来源 src_f8f12eda37b72bebb9444fce；清洗后字符 [4849, 4945)

SHA-256：`a95cb3d5b68b10d3964f7df866ebf3d53a12a749e413633907d8f91d3cbb7bf3`；范围：<main> element; characters 0-13057 of 13057

获取链：运行 d968652bc210 → 问题 q8 → 搜索 search7 → https://github.com/MicrosoftDocs/microsoft-365-docs/blob/public/copilot/pay-as-you-go/copilot-capacity-packs.md
检索词：Copilot Studio capacity pack Azure subscription requirement；当时的问题：微软官方文档是否明确 Copilot Studio 容量包（Copilot Credit 容量包，每包 25,000 信用）与预购 Commit Units 路径在使用代理时同样需要 Azure 订阅，而不仅是按量付费计量需要？

<a id="ev_0b38cd8a1f64f34d14c759b0"></a>
### ev_0b38cd8a1f64f34d14c759b0

> udio agents and the Microsoft Copilot Studio tools/features invoked by the said agents, are included in the Microsoft 365 Copilot USL when the user of the agent is licensed with Microsoft 365 Copilot and the agent is operating using the authenticated Microsoft 365 Copilot USL user’s identity. Usage is limited to fair usage limits. Microsoft reserves the right to update the limits as the product evolves, and new usage patterns emerge.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q4 → 分块 chk_c68aacefe8ad1e6fd48eeabb_15300 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [15300, 15737)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_25868af562dd0d2ed0210605"></a>
### ev_25868af562dd0d2ed0210605

> 5. Agents built on Copilot Studio, for Teams, SharePoint and Microsoft 365 Copilot, are included with the Microsoft 365 Copilot user license at no additional char

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q4 → 分块 chk_c68aacefe8ad1e6fd48eeabb_15300 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [15738, 15900)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_5a440717841727e42686e122"></a>
### ev_5a440717841727e42686e122

> Microsoft 365 Copilot $30 per user/month Included agent usage1 Pay-as-you-go: unlimited2 License (capacity pack): 25,000 Copilot Credit /pack3 Pre

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q4 → 分块 chk_c68aacefe8ad1e6fd48eeabb_13260 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [13714, 13860)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_0e8ed99788c66b70e0116250"></a>
### ev_0e8ed99788c66b70e0116250

> Employee-facing usage scenarios (Business to Employee) of Copilot Studio agents and Copilot Studio tools and features that these agents invoke are included in the Microsoft 365 Copilot USL when the user of the agent is licensed with Microsoft 365 Copilot, and the agent operates using the authenticated Microsoft 365 Copilot USL user’s identity. Usage is limited to fair usage limits. Microsoft reserves the right to update the limit

来源：Article - Copilot Agents, Developer T... — https://services.northwestern.edu/TDClient/30/Portal/KB/Article/2879/Copilot-Agents-Developer-Tools-Sharing-Publishing-and-Message-Consumption

类型：web；读取时间：2026-10-19T08:25:23.206842+00:00；截断：False

问题 q4 → 分块 chk_7e9a2016729ec629a6069173_12240 → 来源 src_7e9a2016729ec629a6069173；清洗后字符 [12407, 12840)

SHA-256：`5e7f77f4b6eb7ba1580d3e124bf34f9731f751d8e737a903c4455cdc5db94043`；范围：<main> element; characters 0-14774 of 14774

获取链：运行 d968652bc210 → 问题 q3 → 搜索 search3 → https://services.northwestern.edu/TDClient/30/Portal/KB/Article/2879/Copilot-Agents-Developer-Tools-Sharing-Publishing-and-Message-Consumption
检索词：Microsoft Product Terms Copilot Studio included agent usage；当时的问题：微软官方 Product Terms 或完整许可条款中，Microsoft 365 Copilot 每席位“Included agent usage”对应的具体 Copilot Credit 数量是多少，公平使用限制（fair usage limit）如何定义、触发后有何后果？

<a id="ev_1cf97f0c464134f53d790214"></a>
### ev_1cf97f0c464134f53d790214

> If your usage exceeds your purchased capacity, technical enforcement applies and can result in service denial.

来源：Standard harness licensing - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing

类型：web；读取时间：2026-10-19T08:45:20.764545+00:00；截断：False

问题 q4 → 分块 chk_0c9308874a087eda76e3ffa2_5610 → 来源 src_0c9308874a087eda76e3ffa2；清洗后字符 [5695, 5805)

SHA-256：`bd97d5a5eb6b73c5509af73942801a58576a809050ce94f139c18b173ae4f67d`；范围：<main> element; characters 0-7004 of 7004

获取链：运行 c498744f19ea → 问题 q2 → 搜索 search2 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing
检索词：Microsoft 365 Copilot internal agent use Copilot Studio licensing；当时的问题：微软官方对 Microsoft 365 Copilot 席位内所含 Copilot Studio 内部代理（internal agent）使用范围与 fair usage 上限是如何规定的？其正式条款原文发布在何处？

<a id="ev_95899b6cf40d7a032858ace6"></a>
### ev_95899b6cf40d7a032858ace6

> If you have a Microsoft 365 Copilot license, using agents in Copilot Chat, Microsoft Teams, or SharePoint for classic answers , generative answers , or Microsoft Graph tenant grounding doesn't count against the Copilot Studio message pack or meter.

来源：Standard harness licensing - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing

类型：web；读取时间：2026-10-19T08:45:20.764545+00:00；截断：False

问题 q4 → 分块 chk_0c9308874a087eda76e3ffa2_5610 → 来源 src_0c9308874a087eda76e3ffa2；清洗后字符 [5891, 6139)

SHA-256：`bd97d5a5eb6b73c5509af73942801a58576a809050ce94f139c18b173ae4f67d`；范围：<main> element; characters 0-7004 of 7004

获取链：运行 c498744f19ea → 问题 q2 → 搜索 search2 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing
检索词：Microsoft 365 Copilot internal agent use Copilot Studio licensing；当时的问题：微软官方对 Microsoft 365 Copilot 席位内所含 Copilot Studio 内部代理（internal agent）使用范围与 fair usage 上限是如何规定的？其正式条款原文发布在何处？

<a id="ev_57dc177d0ab3247a7f29ac8f"></a>
### ev_57dc177d0ab3247a7f29ac8f

> If your tenant has Copilot Studio billing enabled (credits or PAYG), end-user usage is billed at the tenant level. Users of your agents don't need a special license.

来源：Do users in my organization need individual Copilot licenses to use a published Copilot Studio agent? - Microsoft Q&A — https://learn.microsoft.com/en-us/answers/questions/5662349/do-users-in-my-organization-need-individual-copilo

类型：web；读取时间：2026-10-19T08:45:22.066057+00:00；截断：False

问题 q4 → 分块 chk_68911374ae2077e56fb57ecb_1020 → 来源 src_68911374ae2077e56fb57ecb；清洗后字符 [1444, 1609)

SHA-256：`f33a8e7dadb3a5692cd98107337c39a0efbf0ae1218b40820c3f1229a48aaf8f`；范围：<main> element; characters 0-2627 of 2627

获取链：运行 c498744f19ea → 问题 q2 → 搜索 search2 → https://learn.microsoft.com/en-us/answers/questions/5662349/do-users-in-my-organization-need-individual-copilo
检索词：Microsoft 365 Copilot internal agent use Copilot Studio licensing；当时的问题：微软官方对 Microsoft 365 Copilot 席位内所含 Copilot Studio 内部代理（internal agent）使用范围与 fair usage 上限是如何规定的？其正式条款原文发布在何处？

<a id="ev_4ffabf7a78ce12b594bb3c9c"></a>
### ev_4ffabf7a78ce12b594bb3c9c

> Copilot Credit : Microsoft calls Copilot Credits “the unit that measures agent usage” and the common currency across Copilot Studio capabilities.

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q4 → 分块 chk_76369ce0f3851a65c00a0b8b_3060 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [3277, 3422)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_be27addfb41d2d854c90f2ae"></a>
### ev_be27addfb41d2d854c90f2ae

> This application or agent (“Application”) requires an active subscription to Microsoft Online Services such as Microsoft 365, Microsoft Copilot Studio, Dynamics 365, or Power Platform ("Application Services").

来源：Supplemental terms of service for enterprise apps and agents | Microsoft Learn — https://learn.microsoft.com/en-us/legal/microsoft-365/supplemental-terms

类型：web；读取时间：2026-10-19T08:46:30.642038+00:00；截断：False

问题 q5 → 分块 chk_f923af71e866d68295008068_0 → 来源 src_f923af71e866d68295008068；清洗后字符 [64, 273)

SHA-256：`51f3a904d83b8cb71ed6921c3cb317b4dd71e46ae593cb8e8dd13569866cb23f`；范围：<main> element; characters 0-1934 of 1934

获取链：运行 c498744f19ea → 问题 q4 → 搜索 search3 → https://learn.microsoft.com/en-us/legal/microsoft-365/supplemental-terms
检索词：Microsoft Product Terms Copilot Studio agent fair usage；当时的问题：微软官方 Product Terms 或服务条款页是否对 Microsoft 365 Copilot 席位内包含的 Copilot Studio 代理使用量（fair usage）给出可执行的具体上限、计量口径（按用户还是按租户）和超限处理方式？

<a id="ev_21774cd2475bfddab5eb23a1"></a>
### ev_21774cd2475bfddab5eb23a1

> its will be required for user interaction with production agents EXCEPT when the user has an M365 Copilot license as this license covers agent use. More specifically: Employee-facing usage scenarios (Business to Employee) of Copilot Studio agents and Copilot Studio tools and features that these agents invoke are included in the Microsoft 365 Copilot USL when the user of the agent is licensed with Microsoft 365 Copilot, and the agent operates using the authenticated Microsoft 365 Copilot USL user’s identity. Usage is limited to fair usage limits. Microsoft reserves the right to update the limit

来源：Article - Copilot Agents, Developer T... — https://services.northwestern.edu/TDClient/30/Portal/KB/Article/2879/Copilot-Agents-Developer-Tools-Sharing-Publishing-and-Message-Consumption

类型：web；读取时间：2026-10-19T08:25:23.206842+00:00；截断：False

问题 q5 → 分块 chk_7e9a2016729ec629a6069173_12240 → 来源 src_7e9a2016729ec629a6069173；清洗后字符 [12240, 12840)

SHA-256：`5e7f77f4b6eb7ba1580d3e124bf34f9731f751d8e737a903c4455cdc5db94043`；范围：<main> element; characters 0-14774 of 14774

获取链：运行 d968652bc210 → 问题 q3 → 搜索 search3 → https://services.northwestern.edu/TDClient/30/Portal/KB/Article/2879/Copilot-Agents-Developer-Tools-Sharing-Publishing-and-Message-Consumption
检索词：Microsoft Product Terms Copilot Studio included agent usage；当时的问题：微软官方 Product Terms 或完整许可条款中，Microsoft 365 Copilot 每席位“Included agent usage”对应的具体 Copilot Credit 数量是多少，公平使用限制（fair usage limit）如何定义、触发后有何后果？

<a id="ev_966168a934515567ca58763e"></a>
### ev_966168a934515567ca58763e

> If your users hold the Microsoft 365 Copilot User SL ($30/user/month), they already have Copilot Studio use rights for employee-facing agents , Teams, SharePoint, M365 Copilot, at no extra charge. Agents built for those surfaces, operating under the licensed user’s identity, are covered. The catch is “fair usage”. Microsoft does not publish the exact threshold, and reserves the right to update it as patterns emerge.

来源：Copilot Studio Licensing | Explained by Licensing Expert — https://licenseq.com/copilot-studio-licensing/

类型：web；读取时间：2026-10-19T08:44:19.697467+00:00；截断：False

问题 q5 → 分块 chk_be03c5b67dd2b4fe8530e90d_5610 → 来源 src_be03c5b67dd2b4fe8530e90d；清洗后字符 [5637, 6056)

SHA-256：`56c234622dddeedd6d7055b85ceb6bdb7bd1df68db79be59a596ab47d1f8fc2d`；范围：<main> element; characters 0-17908 of 17908

获取链：运行 c498744f19ea → 问题 q1 → 搜索 search1 → https://licenseq.com/copilot-studio-licensing
检索词：Copilot Studio licensing messages capacity pack；当时的问题：微软官方如何说明 Copilot Studio 的计费单位与购买前提（例如按消息/容量包计费所需的 Azure 订阅或租户前提），与 Microsoft 365 Copilot 按用户席位收费的模式相比有何不同？

<a id="ev_edaeb34567f73cdd92495ad0"></a>
### ev_edaeb34567f73cdd92495ad0

> Microsoft 365 Copilot licensed use of agents in Copilot Chat, Teams or SharePoint does not count against the Copilot Studio pack or meter, but the zero-rating has conditions (identity, trigger, fair use, CUA excluded). Check each agent's configuration before assuming it is free.

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q5 → 分块 chk_76369ce0f3851a65c00a0b8b_5101 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [5317, 5596)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_2ae3d91c26c9f9b3a64fec49"></a>
### ev_2ae3d91c26c9f9b3a64fec49

> If your tenant has Copilot Studio billing enabled (credits or PAYG), end-user usage is billed at the tenant level. Users of your agents don't need a special license. Without te

来源：Do users in my organization need individual Copilot licenses to use a published Copilot Studio agent? - Microsoft Q&A — https://learn.microsoft.com/en-us/answers/questions/5662349/do-users-in-my-organization-need-individual-copilo

类型：web；读取时间：2026-10-19T08:45:22.066057+00:00；截断：False

问题 q5 → 分块 chk_68911374ae2077e56fb57ecb_1020 → 来源 src_68911374ae2077e56fb57ecb；清洗后字符 [1444, 1620)

SHA-256：`f33a8e7dadb3a5692cd98107337c39a0efbf0ae1218b40820c3f1229a48aaf8f`；范围：<main> element; characters 0-2627 of 2627

获取链：运行 c498744f19ea → 问题 q2 → 搜索 search2 → https://learn.microsoft.com/en-us/answers/questions/5662349/do-users-in-my-organization-need-individual-copilo
检索词：Microsoft 365 Copilot internal agent use Copilot Studio licensing；当时的问题：微软官方对 Microsoft 365 Copilot 席位内所含 Copilot Studio 内部代理（internal agent）使用范围与 fair usage 上限是如何规定的？其正式条款原文发布在何处？

<a id="ev_7167c90735860b7f2afb8b4a"></a>
### ev_7167c90735860b7f2afb8b4a

> Microsoft 365 Copilot is licensed as a per-user add-on.

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q6 → 分块 chk_76369ce0f3851a65c00a0b8b_1020 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [1315, 1370)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_389aece00e2d931b4ce5e5e4"></a>
### ev_389aece00e2d931b4ce5e5e4

> Microsoft sells it as a User SL that must sit on top of a listed prerequisite license

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q6 → 分块 chk_76369ce0f3851a65c00a0b8b_1020 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [1371, 1456)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_75872840a1f4ecd27c63627d"></a>
### ev_75872840a1f4ecd27c63627d

> Product Terms state that purchases of listed licenses “also require the purchase of a Prerequisite License”.

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q6 → 分块 chk_76369ce0f3851a65c00a0b8b_5610 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [5795, 5903)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_04cb72d2de1b48e64a584b4d"></a>
### ev_04cb72d2de1b48e64a584b4d

> For Microsoft 365 Copilot, the prerequisites are Microsoft 365 Apps for business or enterprise, Business Basic, Standard or Premium, F1, F3, A1, A3, A5, A7, E3, E5, E7, G3, G5 or G7; Office 365 F3, A1, A3, A5, E1, E3, E5, G3 or G5; Exchange Online; SharePoint Online; OneDrive; Microsoft Clipchamp; Microso

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q6 → 分块 chk_76369ce0f3851a65c00a0b8b_5610 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [5904, 6210)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_37d9dbe02b1950137794dea6"></a>
### ev_37d9dbe02b1950137794dea6

> Microsoft 365 Copilot is an add-on license, and Microsoft's license-options article lists more qualifying plans than most people assume.

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q6 → 分块 chk_ba995cac346030f043dc84c6_510 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [726, 862)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_bcff011e04cd21c7cb00be57"></a>
### ev_bcff011e04cd21c7cb00be57

> For the Microsoft 365 Copilot SKU: Microsoft 365 E5, E3, F1 and F3; Business Basic, Standard and Premium; Apps for business and for enterprise; Office 365 E1, E3, E5 and F3; Teams Essentials, Enterprise and EEA; Exchange Kiosk and Plans 1 and 2; S

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q6 → 分块 chk_ba995cac346030f043dc84c6_510 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [863, 1110)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_1e9f76cf2b6ea6c661f5ef2a"></a>
### ev_1e9f76cf2b6ea6c661f5ef2a

> Microsoft 365 E3, E5, F3, and Business Basic, Standard, or Premium qualify you to add it.

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q6 → 分块 chk_0a86d3d8c098bd281864d073_8670 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [8856, 8945)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_946dce0a36ce1a5f13279d59"></a>
### ev_946dce0a36ce1a5f13279d59

> No. Copilot is sold only as an add-on to an eligible base plan.

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q6 → 分块 chk_0a86d3d8c098bd281864d073_8670 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [9090, 9153)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_87fa76905700438c3e482fbb"></a>
### ev_87fa76905700438c3e482fbb

> If a user isn’t on a qualifying subscription, you upgrade the base plan first, then add Copilot.

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q6 → 分块 chk_0a86d3d8c098bd281864d073_8670 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [9154, 9250)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_59d23c2bc88c1f8d1231af8e"></a>
### ev_59d23c2bc88c1f8d1231af8e

> A Microsoft 365 Copilot Business license is built for organizations under 300 seats sitting on a Business plan.

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q6 → 分块 chk_0a86d3d8c098bd281864d073_4080 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [4106, 4217)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_b5bcae3dea16e74dc14470f5"></a>
### ev_b5bcae3dea16e74dc14470f5

> The enterprise Microsoft 365 Copilot add-on is for E3 and E5 tenants and carries no seat ceiling.

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q6 → 分块 chk_0a86d3d8c098bd281864d073_4080 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [4218, 4315)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_4dc8e527a95c4faf0cf67ac8"></a>
### ev_4dc8e527a95c4faf0cf67ac8

> Base plan required Business Basic, Standard, or Premium E3, E5, or Business Standard/Premium Seat cap Up to 300 ✓ No cap Price per user/month ~$21 (annual) $30 (annual)

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q6 → 分块 chk_0a86d3d8c098bd281864d073_4080 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [4368, 4536)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_9fd29e9c197ad185a73c53e0"></a>
### ev_9fd29e9c197ad185a73c53e0

> Microsoft sells it as an add-on , which means every Copilot seat has to sit on an eligible Microsoft 365 base subscription first.

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q6 → 分块 chk_0a86d3d8c098bd281864d073_2040 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [2473, 2602)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_cdc87a4ad909fe64ffe42398"></a>
### ev_cdc87a4ad909fe64ffe42398

> onth on an annual term.

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q6 → 分块 chk_0a86d3d8c098bd281864d073_2040 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [2040, 2063)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_2e1662ea4613766104561886"></a>
### ev_2e1662ea4613766104561886

> It’s a paid, per-user add-on to an eligible Microsoft 365 subscription that turns on Copilot inside the Office apps and work-based Copilot Chat grounded in your tenant’s data.

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q6 → 分块 chk_0a86d3d8c098bd281864d073_8160 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [8476, 8651)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_df6406ac549944a098e0ca73"></a>
### ev_df6406ac549944a098e0ca73

> It costs $30 per user per month on the enterprise plan and requires a qualifying base license underneath.

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q6 → 分块 chk_0a86d3d8c098bd281864d073_8160 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [8652, 8757)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_0143166912ecb88fe0a69287"></a>
### ev_0143166912ecb88fe0a69287

> Product Terms are the contractual source; Learn pages are educational.

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q6 → 分块 chk_76369ce0f3851a65c00a0b8b_1020 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [1079, 1149)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_c9e53c158964c047e830ea79"></a>
### ev_c9e53c158964c047e830ea79

> Microsoft 365 Copilot is licensed as a per-user add-on. Microsoft sells it as a User SL that must sit on top of a listed prerequisite license, the same subscription meter used for other Microsoft 365 Online Services.

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q7 → 分块 chk_76369ce0f3851a65c00a0b8b_1020 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [1315, 1531)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_6af0e2875999956ff2571b26"></a>
### ev_6af0e2875999956ff2571b26

> Current Microsoft Learn pages call the product Microsoft Copilot and describe it as “available as an add-on plan with one of the licensing prerequisites”.

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q7 → 分块 chk_76369ce0f3851a65c00a0b8b_1530 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [1536, 1690)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_fb3a95aea3d25159bb5badb6"></a>
### ev_fb3a95aea3d25159bb5badb6

> Prerequisite A listed Microsoft 365, Office 365 or standalone service license (Product Terms)

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q7 → 分块 chk_76369ce0f3851a65c00a0b8b_0 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [350, 443)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_844f483a559a99b3171b3658"></a>
### ev_844f483a559a99b3171b3658

> Microsoft 365 Copilot is an add-on license, and Microsoft's license-options article lists more qualifying plans than most people assume. For the Microsoft 365 Copilot SKU: Microsoft 365 E5, E3, F1 and F3; Business Basic, Standard and Premium; Apps for business and for enterprise; Office 365 E1, E3, E5 and F3; Teams Essentials, Enterprise and EEA; Exchange Kiosk and Plans 1 and 2; S

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q7 → 分块 chk_ba995cac346030f043dc84c6_510 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [726, 1110)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_a1dd93632d4ee6ca432f71f9"></a>
### ev_a1dd93632d4ee6ca432f71f9

> A Microsoft 365 Copilot Business license is built for organizations under 300 seats sitting on a Business plan. The enterprise Microsoft 365 Copilot add-on is for E3 and E5 tenants and carries no seat ceiling.

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q7 → 分块 chk_0a86d3d8c098bd281864d073_4080 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [4106, 4315)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_a64aff1fa2abb464ed775caa"></a>
### ev_a64aff1fa2abb464ed775caa

> When Microsoft 365 Copilot was first released in November 2023, it required a 300-seat minimum purchase. This is no longer the case , enabling organizations of all sizes to adopt Copilot.

来源：How does Microsoft 365 Copilot pricing and licensing work? | TechTarget — https://www.techtarget.com/enterprise-software/answer/How-does-Microsoft-365-Copilot-pricing-and-licensing-work

类型：web；读取时间：2026-10-19T08:34:46.912014+00:00；截断：False

问题 q7 → 分块 chk_06093f8213a8a3581da3292f_4590 → 来源 src_06093f8213a8a3581da3292f；清洗后字符 [4916, 5103)

SHA-256：`b99d9f850bdf6cfb1c15ffcd9f72733c150cddb6873d69c5eb6847ad238b8447`；范围：<article> element; characters 0-8761 of 8761

获取链：运行 23c904aac0c6 → 问题 q3 → 搜索 search1 → https://www.techtarget.com/enterprise-software/answer/How-does-Microsoft-365-Copilot-pricing-and-licensing-work
检索词：Microsoft 365 Copilot pricing per user；当时的问题：微软官方 Microsoft 365 Copilot 产品页/价目页是否公开标明企业版为每用户每月 30 美元、Copilot Business 为每用户每月约 21 美元（年付），并说明按席位计费与适用版本？

<a id="ev_958595bf35613f88c3b7c837"></a>
### ev_958595bf35613f88c3b7c837

> Product Terms state that purchases of listed licenses “also require the purchase of a Prerequisite License”. For Microsoft 365 Copilot, the prerequisites are Microsoft 365 Apps for business or enterprise, Business Basic, Standard or Premium, F1, F3, A1, A3, A5, A7, E3, E5, E7, G3, G5 or G7; Office 365 F3, A1, A3, A5, E1, E3, E5, G3 or G5; Exchange Online; SharePoint Online; OneDrive; Microsoft Clipchamp; Microso

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q8 → 分块 chk_76369ce0f3851a65c00a0b8b_5610 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [5795, 6210)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_e238d62591daa69fa3dd995e"></a>
### ev_e238d62591daa69fa3dd995e

> License options for Microsoft Copilot (Microsoft Learn) Prerequisite plan lists; Copilot Chat web-based and work-based. Educational. Effective 2026-09-25.

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:38:05.886144+00:00；截断：False

问题 q8 → 分块 chk_76369ce0f3851a65c00a0b8b_13260 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [13484, 13638)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 23c904aac0c6 → 问题 q7 → 搜索 search4 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；当时的问题：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？

<a id="ev_46fc73195360c49a44fa23ed"></a>
### ev_46fc73195360c49a44fa23ed

> Our Microsoft Modern Work Digital Specialist just informed me that the minimum purchase for M365 Copilot is 300 seats. This about 60 more licenses then we have employees. Is this true?

来源：M365 Copilot licensing question - Microsoft Q&A — https://learn.microsoft.com/en-us/answers/questions/5270940/m365-copilot-licensing-question

类型：web；读取时间：2026-10-19T08:48:59.299737+00:00；截断：False

问题 q8 → 分块 chk_d2d8ac22f5283580437b9a05_0 → 来源 src_d2d8ac22f5283580437b9a05；清洗后字符 [70, 254)

SHA-256：`8d184fed9da7243fedf7638b3685727bea1be6ee40dd63ef22ab0f5f3df845ea`；范围：<main> element; characters 0-6160 of 6160

获取链：运行 c498744f19ea → 问题 q7 → 搜索 search6 → https://learn.microsoft.com/en-us/answers/questions/5270940/m365-copilot-licensing-question
检索词：Microsoft 365 Copilot licensing prerequisites seat minimum；当时的问题：微软官方 Microsoft 365 Copilot 许可页（Microsoft Learn「License options for Microsoft Copilot」或 Copilot 定价页）如何直接表述 M365 Copilot 附加许可的先决基础许可清单、是否存在最低席位数、按年承诺条款以及 Business 版 300 席位上限？

<a id="ev_85cacb9573f93583cd5cfaff"></a>
### ev_85cacb9573f93583cd5cfaff

> You need the Copilot add on plus a qualifying base for each user. Qualifying bases include Microsoft 365 E3, E5, F1, F3 and the Business plans, Office 365 E1, E3, E5 and F3, Microsoft 365 Apps, and standalone Exchange, SharePoint, OneDrive and Teams plans.

来源：Copilot Requirements: Licenses You Need in 2026 | Redress — https://redresscompliance.com/microsoft-copilot-minimum-requirements-what-licenses-are-required

类型：web；读取时间：2026-10-19T08:49:05.219809+00:00；截断：False

问题 q8 → 分块 chk_087483488f8c633def34e448_15810 → 来源 src_087483488f8c633def34e448；清洗后字符 [15990, 16246)

SHA-256：`b7450255bc0b0505a1aa149ba7c62087d02b8aa536ff934a4f4a993832394b35`；范围：<article> element; characters 0-18386 of 18386

获取链：运行 c498744f19ea → 问题 q7 → 搜索 search6 → https://redresscompliance.com/microsoft-copilot-minimum-requirements-what-licenses-are-required
检索词：Microsoft 365 Copilot licensing prerequisites seat minimum；当时的问题：微软官方 Microsoft 365 Copilot 许可页（Microsoft Learn「License options for Microsoft Copilot」或 Copilot 定价页）如何直接表述 M365 Copilot 附加许可的先决基础许可清单、是否存在最低席位数、按年承诺条款以及 Business 版 300 席位上限？

<a id="ev_166813518580a59f6256b9bd"></a>
### ev_166813518580a59f6256b9bd

> The smaller SKU, Microsoft 365 Copilot Business, attaches only to Microsoft 365 Business Basic, Business Standard, Business Premium and Apps for business, and Microsoft's catalog description caps it at 300 seats, the same ceiling as the Business plans, which our 300-license limit guide explains.

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q9 → 分块 chk_ba995cac346030f043dc84c6_1020 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [1274, 1570)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_c0d336f062fcce549653b15a"></a>
### ev_c0d336f062fcce549653b15a

> Microsoft 365 Copilot Business serves organizations with up to 300 seats on a qualifying Microsoft 365 business plan.

来源：Microsoft Copilot Pricing 2026: Plans, Costs, and Total Cost of Ownership | The GoSearch Blog — https://www.gosearch.ai/blog/microsoft-copilot-pricing/

类型：web；读取时间：2026-10-19T08:35:06.473917+00:00；截断：False

问题 q9 → 分块 chk_0a009e6cf67b8f9a039acdd2_8160 → 来源 src_0a009e6cf67b8f9a039acdd2；清洗后字符 [8462, 8579)

SHA-256：`f8e66b7736eec780d00704e605d29cf9e7792f4c495980f18fd18f60e8c96298`；范围：<body> element; characters 0-29481 of 29481

获取链：运行 23c904aac0c6 → 问题 q3 → 搜索 search1 → https://www.gosearch.ai/blog/microsoft-copilot-pricing
检索词：Microsoft 365 Copilot pricing per user；当时的问题：微软官方 Microsoft 365 Copilot 产品页/价目页是否公开标明企业版为每用户每月 30 美元、Copilot Business 为每用户每月约 21 美元（年付），并说明按席位计费与适用版本？

<a id="ev_1d9855225f2f3116cb81e2a7"></a>
### ev_1d9855225f2f3116cb81e2a7

> Business-tier plans (Basic, Standard, Premium) are capped at 300 seats per tenant.

来源：Microsoft Copilot Tiers: Pricing, Licensing, and GoSearch Comparison (2026) - GoSearch FAQs + Answers — https://www.gosearch.ai/faqs/microsoft-copilot-pricing-tiers/

类型：web；读取时间：2026-10-19T08:49:13.789271+00:00；截断：False

问题 q9 → 分块 chk_4a68e699a84dc9714ba3d6cb_7651 → 来源 src_4a68e699a84dc9714ba3d6cb；清洗后字符 [8165, 8247)

SHA-256：`a88c40d120569231be2f1b1e09bfd2f00a6a8744d665e8ce4132e7e65b18a28d`；范围：<body> element; characters 0-16677 of 16677

获取链：运行 c498744f19ea → 问题 q7 → 搜索 search6 → https://www.gosearch.ai/faqs/microsoft-copilot-pricing-tiers
检索词：Microsoft 365 Copilot licensing prerequisites seat minimum；当时的问题：微软官方 Microsoft 365 Copilot 许可页（Microsoft Learn「License options for Microsoft Copilot」或 Copilot 定价页）如何直接表述 M365 Copilot 附加许可的先决基础许可清单、是否存在最低席位数、按年承诺条款以及 Business 版 300 席位上限？

<a id="ev_b00a44a6daf6f8f84ea505b0"></a>
### ev_b00a44a6daf6f8f84ea505b0

> Organizations above that threshold must license Copilot Enterprise against an E3, E5, or equivalent enterprise base license — there’s no Business-tier path at scale, though it’s also where the reported 1,000+/10,000+ seat volume discounts would apply once confirmed.

来源：Microsoft Copilot Tiers: Pricing, Licensing, and GoSearch Comparison (2026) - GoSearch FAQs + Answers — https://www.gosearch.ai/faqs/microsoft-copilot-pricing-tiers/

类型：web；读取时间：2026-10-19T08:49:13.789271+00:00；截断：False

问题 q9 → 分块 chk_4a68e699a84dc9714ba3d6cb_8160 → 来源 src_4a68e699a84dc9714ba3d6cb；清洗后字符 [8248, 8514)

SHA-256：`a88c40d120569231be2f1b1e09bfd2f00a6a8744d665e8ce4132e7e65b18a28d`；范围：<body> element; characters 0-16677 of 16677

获取链：运行 c498744f19ea → 问题 q7 → 搜索 search6 → https://www.gosearch.ai/faqs/microsoft-copilot-pricing-tiers
检索词：Microsoft 365 Copilot licensing prerequisites seat minimum；当时的问题：微软官方 Microsoft 365 Copilot 许可页（Microsoft Learn「License options for Microsoft Copilot」或 Copilot 定价页）如何直接表述 M365 Copilot 附加许可的先决基础许可清单、是否存在最低席位数、按年承诺条款以及 Business 版 300 席位上限？

<a id="ev_be069ac21d3d5f4c2a1000a6"></a>
### ev_be069ac21d3d5f4c2a1000a6

> can operate Microsoft 365 tenants with more than 300 users by licensing additional users with appropriate Enterprise or other eligible plans. Microsoft positions Enterprise plans such as Microsoft 365 E3 and E5 for organizations that need to scale beyond the Business-family limit.

来源：Microsoft 365 Business Premium 300-User Limit Explained — https://www.ciotech.us/microsoft-365-business-premium-300-user-limit/

类型：web；读取时间：2026-10-19T08:51:44.084806+00:00；截断：False

问题 q9 → 分块 chk_9978a488af6c0ff261bbda8c_13770 → 来源 src_9978a488af6c0ff261bbda8c；清洗后字符 [13770, 14051)

SHA-256：`fa9b8e2003589e6790ba9b136fe75e91443115ffbf08060446e843e169f84cf3`；范围：<article> element; characters 0-17170 of 17170

获取链：运行 c498744f19ea → 问题 q9 → 搜索 search8 → https://www.ciotech.us/microsoft-365-business-premium-300-user-limit
检索词：Microsoft 365 Copilot Business 300 seats limit；当时的问题：微软官方 Microsoft 365 Copilot Business 许可（或 Copilot 定价页）是否明文设定 300 席位上限？若组织席位数超过该上限，官方规定如何处理（是否强制迁移至企业版 E3/E5 附加项）？

<a id="ev_286fdf8f77550881b5178118"></a>
### ev_286fdf8f77550881b5178118

> At user 301, Microsoft 365 does not stop working, but you cannot simply add another Business-family license. Growing companies typically begin adding or transitioning users to Microsoft 365 Enterprise plans such as E3 or E5.

来源：Microsoft 365 Business Premium 300-User Limit Explained — https://www.ciotech.us/microsoft-365-business-premium-300-user-limit/

类型：web；读取时间：2026-10-19T08:51:44.084806+00:00；截断：False

问题 q9 → 分块 chk_9978a488af6c0ff261bbda8c_1531 → 来源 src_9978a488af6c0ff261bbda8c；清洗后字符 [1649, 1873)

SHA-256：`fa9b8e2003589e6790ba9b136fe75e91443115ffbf08060446e843e169f84cf3`；范围：<article> element; characters 0-17170 of 17170

获取链：运行 c498744f19ea → 问题 q9 → 搜索 search8 → https://www.ciotech.us/microsoft-365-business-premium-300-user-limit
检索词：Microsoft 365 Copilot Business 300 seats limit；当时的问题：微软官方 Microsoft 365 Copilot Business 许可（或 Copilot 定价页）是否明文设定 300 席位上限？若组织席位数超过该上限，官方规定如何处理（是否强制迁移至企业版 E3/E5 附加项）？

<a id="ev_ea14a30bc5363deb444ee829"></a>
### ev_ea14a30bc5363deb444ee829

> No. Microsoft’s current documentation sets the limit at 300 seats. That limit applies across the Business family in total.

来源：Microsoft 365 Business Premium 300-User Limit Explained — https://www.ciotech.us/microsoft-365-business-premium-300-user-limit/

类型：web；读取时间：2026-10-19T08:51:44.084806+00:00；截断：False

问题 q9 → 分块 chk_9978a488af6c0ff261bbda8c_14790 → 来源 src_9978a488af6c0ff261bbda8c；清洗后字符 [14862, 14984)

SHA-256：`fa9b8e2003589e6790ba9b136fe75e91443115ffbf08060446e843e169f84cf3`；范围：<article> element; characters 0-17170 of 17170

获取链：运行 c498744f19ea → 问题 q9 → 搜索 search8 → https://www.ciotech.us/microsoft-365-business-premium-300-user-limit
检索词：Microsoft 365 Copilot Business 300 seats limit；当时的问题：微软官方 Microsoft 365 Copilot Business 许可（或 Copilot 定价页）是否明文设定 300 席位上限？若组织席位数超过该上限，官方规定如何处理（是否强制迁移至企业版 E3/E5 附加项）？

<a id="ev_85088fee5d5ef65625153602"></a>
### ev_85088fee5d5ef65625153602

> Not necessarily. Mixed licensing is possible.

来源：Microsoft 365 Business Premium 300-User Limit Explained — https://www.ciotech.us/microsoft-365-business-premium-300-user-limit/

类型：web；读取时间：2026-10-19T08:51:44.084806+00:00；截断：False

问题 q9 → 分块 chk_9978a488af6c0ff261bbda8c_14790 → 来源 src_9978a488af6c0ff261bbda8c；清洗后字符 [15045, 15090)

SHA-256：`fa9b8e2003589e6790ba9b136fe75e91443115ffbf08060446e843e169f84cf3`；范围：<article> element; characters 0-17170 of 17170

获取链：运行 c498744f19ea → 问题 q9 → 搜索 search8 → https://www.ciotech.us/microsoft-365-business-premium-300-user-limit
检索词：Microsoft 365 Copilot Business 300 seats limit；当时的问题：微软官方 Microsoft 365 Copilot Business 许可（或 Copilot 定价页）是否明文设定 300 席位上限？若组织席位数超过该上限，官方规定如何处理（是否强制迁移至企业版 E3/E5 附加项）？

<a id="ev_28314414cc27dbbe8fa2d7b8"></a>
### ev_28314414cc27dbbe8fa2d7b8

> Our Microsoft Modern Work Digital Specialist just informed me that the minimum purchase for M365 Copilot is 300 seats. This about 60 more licenses then we have employees. Is this true? If so, is Microsoft deliberately excluding small and medium business?

来源：M365 Copilot licensing question - Microsoft Q&A — https://learn.microsoft.com/en-us/answers/questions/5270940/m365-copilot-licensing-question

类型：web；读取时间：2026-10-19T08:48:59.299737+00:00；截断：False

问题 q9 → 分块 chk_d2d8ac22f5283580437b9a05_0 → 来源 src_d2d8ac22f5283580437b9a05；清洗后字符 [70, 324)

SHA-256：`8d184fed9da7243fedf7638b3685727bea1be6ee40dd63ef22ab0f5f3df845ea`；范围：<main> element; characters 0-6160 of 6160

获取链：运行 c498744f19ea → 问题 q7 → 搜索 search6 → https://learn.microsoft.com/en-us/answers/questions/5270940/m365-copilot-licensing-question
检索词：Microsoft 365 Copilot licensing prerequisites seat minimum；当时的问题：微软官方 Microsoft 365 Copilot 许可页（Microsoft Learn「License options for Microsoft Copilot」或 Copilot 定价页）如何直接表述 M365 Copilot 附加许可的先决基础许可清单、是否存在最低席位数、按年承诺条款以及 Business 版 300 席位上限？

完整来源文本、分块、引用和哈希见同目录 state.json；节点、调用及排序分数见 trace.jsonl。
