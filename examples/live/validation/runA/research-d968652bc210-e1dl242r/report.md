# Microsoft｜企业研究

研究问题：Microsoft 365 Copilot 与 Copilot Studio 面向的企业使用者、收费单位和购买前提有何区别？这些差异可能如何影响企业客户扩展使用和微软的收入来源？优先使用官方资料；将价格与许可事实、基于事实的推导、商业判断和仍待验证假设明确区分，不把产品定价直接当成已实现收入或利润。

模式：live；停止原因：round_limit；研究轮次：10

引用关系与摘录位置已做代码校验；语义支持关系、事实分类和缺口关闭是模型判断，未经独立事实核实。

## 事实（来源陈述）

- **c1_1** [supported] 微软官方《Microsoft Copilot Studio Licensing Guide》的计费对比表中列出：Microsoft 365 Copilot 为每用户每月 30 美元，包含代理使用额度（被标注为 1），并可选按量付费（被标注为无限量，2）或许可证（容量包）25,000 Copilot Credit/包（被标注为 3）。 [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports）
  依据/推导：该摘录来自微软官方许可指南 PDF（vendor_official），是许可文档的计费对比表内容；但摘录仅呈现表头与单位，未包含脚注 1/2/3 的具体口径，故不能据此断言“按量付费 unlimited”的具体条件或每个席位包含的信用额度数量。价格仅为标价/许可事实，不构成已实现收入或利润。
- **c1_2** [supported] 按微软官方 Copilot Studio 定价页，随 Microsoft 365 Copilot 附带的 Copilot Studio 允许已获许可用户在 Microsoft 365 内使用 Copilot Chat 与 Standard harness 构建并使用内部代理，无需额外费用；而独立的 Copilot Studio 许可则提供额外灵活性，可用 GitHub Copilot harness 构建代理、发布到外部渠道（网站、应用、社交平台），未获许可的用户也可使用代理，并可从不同定价方案中选择。 [ev_d03281f6a8f3b10040fd8adb](#ev_d03281f6a8f3b10040fd8adb)（supports） [ev_0f72de9009f4ebdeb9f3d047](#ev_0f72de9009f4ebdeb9f3d047)（supports）
  依据/推导：两段均为微软官方定价页 FAQ 的连续摘录，直接陈述附带版与独立版的差别。注意：附带版“无需额外费用”以持有 Microsoft 365 Copilot 许可为前提，因此其使用者范围是已获许可用户，而非全体员工。
- **c1_3** [supported] Copilot Studio 官方定价页称，购买前提是客户必须拥有合格的企业版或商业版 Microsoft 365 计划；官方页面另称使用代理需要 Azure 订阅。官方定价页还说明 Copilot Studio 按租户范围销售，包含每包 25,000 Copilot Credits 的容量包，并提供可预付的 Copilot Credit Commit Units 预购方案。 [ev_784627136f29e0b92110aa39](#ev_784627136f29e0b92110aa39)（supports） [ev_8cba532208cb1ca2ecd4daaa](#ev_8cba532208cb1ca2ecd4daaa)（supports） [ev_0f72de9009f4ebdeb9f3d047](#ev_0f72de9009f4ebdeb9f3d047)（supports）
  依据/推导：ev_7846… 与 ev_8cba… 均为微软官方定价页同一区块的连续摘录；“租户范围销售、含 25,000 信用/包、预购 Commit Units”来自 ev_0f72… 的 context_after，属同一询答段落。需注意“Azure 订阅”一句在原文中紧邻按量/预付语境，其是否适用于所有购买路径（含容量包）未在摘录中明确，故不扩大适用范围。
- **c1_4** [supported] 第三方文章（非微软官方）表述：Copilot for Microsoft 365 采用固定按用户许可，Copilot Studio 采用基于 Copilot Credits 的用量计费；前者为每用户每月订阅，前提包括 Microsoft 365 E3、E5、Business Standard 或 Business Premium；后者构建代理免费、运行代理按用量消耗信用，可选容量包或按量付费，容量包起价每月 200 美元/25,000 信用；另一篇第三方文章称 Copilot Studio 按信用计费、在租户层汇集而非按席位。 [ev_5f9c6c0b1525ac6058573928](#ev_5f9c6c0b1525ac6058573928)（supports） [ev_a84c833dd8a8158d3eaad801](#ev_a84c833dd8a8158d3eaad801)（supports） [ev_50b25e4157e22ea241e07a33](#ev_50b25e4157e22ea241e07a33)（supports） [ev_578f724fd92ed7c8f5e49975](#ev_578f724fd92ed7c8f5e49975)（supports） [ev_581bce47940f6aaa85d13f76](#ev_581bce47940f6aaa85d13f76)（supports）
  依据/推导：以上均为 third_party 来源，仅作为与官方材料相互印证的二手陈述，不能称为微软正式文档，也不能单独关闭要求官方条款的缺口。其价格数字（如每用户每月 30 美元、容量包 200 美元）与官方指南表格中的数字方向一致，但第三方表述中的“2026 年 5 月”“$18 促销价”等时点与优惠信息未在官方摘录中确认。
- **c2_1** [supported] 微软官方《Microsoft Copilot Studio Licensing Guide》的许可对比表在“Microsoft 365 Copilot”一行列出：每用户每月 30 美元、包含代理使用额度（标注为 1）、按量付费标注为无限量（标注为 2）、许可证（容量包）为每包 25,000 Copilot Credit（标注为 3）。 [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports） [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports）
  依据/推导：两个版本指南的同一表格摘录一致。但摘录仅含表头数字与脚注编号，脚注 1/2/3 的具体内容未出现在已校验摘录中，因此不能据此断言每席位“包含多少个 Copilot Credit”，也不能给出“unlimited”与公平使用限制的确切定义。该行价格属标价/许可事实，不等于已实现收入。
- **c2_2** [supported] 官方指南称 Copilot Credits 是 Copilot Studio 各项能力的通用计量单位，可通过 Copilot Studio 按量付费计量、Copilot Studio 许可证（即 Copilot Credit 容量包）以及 Copilot Credit 预购方案获得。 [ev_970f49f4b21e69e442f9aa9b](#ev_970f49f4b21e69e442f9aa9b)（supports）
  依据/推导：ev_970f… 直接陈述信用作为通用货币及三条获取渠道；context_after 明示第三条为 Copilot Credit Pre-Purchase Plan。此为计费结构事实，未涉及具体额度数量。
- **c2_3** [supported] 官方指南说明容量包（Copilot Studio License）的适用方式：按租户配置，1 个容量包 = 25,000 Copilot Credits，定价为每信用包每月 200 美元（按年计费），未用信用不结转至下月；建议按租户预期每月消耗量购买，并在信用包耗尽前额外容量推荐启用按量付费计量以保障业务连续性。 [ev_67419540f72b4110f96c4ce1](#ev_67419540f72b4110f96c4ce1)（supports） [ev_2b9e141ce0074ba49ee0902f](#ev_2b9e141ce0074ba49ee0902f)（supports） [ev_376ddd08ecd4747fa61b4b19](#ev_376ddd08ecd4747fa61b4b19)（supports）
  依据/推导：三段摘录同属指南第 4 节“Microsoft Copilot Studio License (Capacity pack)”，连续文本：定价与容量、租户/月度计量、不结转、以及耗尽后才计入按量计量的顺序。价格仅为标价，不构成已实现收入或利润。
- **c2_4** [supported] 官方指南描述 Microsoft Agent 预购方案（Microsoft Agent P3）：为一年期预付选项，客户预付一笔 Agent Commit Units（ACUs）池，可在一年期内任意时点使用；每个 ACU 价值 1 美元的 Copilot Credit 或 Microsoft Foundry 用量，相当于 100 Copilot Credits；定价分档为 20,000 ACU 享 5%、100,000 ACU 享 10%、500,000 ACU 享 15% 折扣。 [ev_4f771c92962baa3167c08336](#ev_4f771c92962baa3167c08336)（supports） [ev_bf78bdec34d2ed9ab4d5364c](#ev_bf78bdec34d2ed9ab4d5364c)（supports） [ev_4f771c92962baa3167c08336](#ev_4f771c92962baa3167c08336)（supports）
  依据/推导：两段为指南预购方案章节的连续摘录：ACU 价值换算与档位折扣表。折扣为标价机制，非已实现收入。
- **c2_5** [supported] 官方 Copilot Studio 定价页在介绍预购方案（含预付 Copilot Credit Commit Units、最高可节省 20%）时称，使用代理需要 Azure 订阅。 [ev_8cba532208cb1ca2ecd4daaa](#ev_8cba532208cb1ca2ecd4daaa)（supports） [ev_215b99e850282a545db0bdc7](#ev_215b99e850282a545db0bdc7)（supports）
  依据/推导：ev_8cba… 与 ev_215b… 为同一段落前后文连续摘录，Azure 订阅要求紧随预购方案与 Commit Units 描述之后。摘录未说明该要求是否同样适用于容量包或仅适用于按量/预购路径，故不扩大适用范围；该页未出现“按量付费必须绑定 Azure”的完整条款文字。
- **c2_8** [supported] 官方指南自述其不取代或不替换 Microsoft Product Terms 中关于使用权的法律文档。 [ev_ebc24156510a771ef0b63cea](#ev_ebc24156510a771ef0b63cea)（supports）
  依据/推导：该摘录来自指南前言性说明，直接表明指南的从属地位；这支持将本指南作为官方说明而非最终法律条款，也说明 Product Terms 仍是关闭 gap1 的关键来源。
- **c3_1** [supported] 微软官方《Microsoft Copilot Studio Licensing Guide》在说明可用性限制时写明：使用受公平使用限制（fair usage limits）约束，微软保留在产品演进并出现新使用模式时更新这些限制的权利。 [ev_3673df720bdda4517b7e7b6a](#ev_3673df720bdda4517b7e7b6a)（supports）
  依据/推导：摘录来自微软官方许可指南 PDF（vendor_official），context_before 指向“用户持有 Microsoft 365 Copilot 许可且代理以该已验证许可用户身份运行”的代理场景。因此该公平使用限制的适用范围应理解为该 Microsoft 365 Copilot USL 场景，不能外推为所有 Copilot Studio 计费路径。原文未给出阈值数字或触发后的具体后果，只能确认“有限制、可调整”的存在性。
- **c3_2** [supported] 微软官方 Microsoft Learn《Billing rates and management》的计费费率表在“Used by Microsoft 365 Copilot licensed user”列下，对经典回答、生成式回答、代理操作、租户图谱 grounding 及代理流操作（每 100 个操作）等特性均标注“No charge”，同时列出相应的 Copilot Credit 消耗参照数。 [ev_0fb7ca088ee9900f8d02961b](#ev_0fb7ca088ee9900f8d02961b)（supports）
  依据/推导：这是官方 Learn 文档表格摘录，属厂商正式运营文档（vendor_official），说明持 Microsoft 365 Copilot 许可用户的这些特性不另收费。但“不收费”是费率口径，不等于每席位包含固定数量的 Copilot Credit；摘录未给出任何“每席位包含 N 个信用”的数字，因此不能用以回答具体额度数量。
- **c3_3** [supported] 同一官方 Learn 页面脚注进一步限定：“No charge”对 Microsoft 365 Copilot 持证用户的包含仅适用于使用“When an agent calls the flow”触发器的代理流；其他触发器的代理流另行计费。 [ev_e1c1dc70ef05d675491e7b64](#ev_e1c1dc70ef05d675491e7b64)（supports）
  依据/推导：摘录 context_after 直接给出该脚注限定，属 vendor_official 表格脚注。它表明“持证用户不计量”的适用边界是有限定条件的，而非全量豁免，但未涉及公平使用限制的阈值或后果。
- **c3_4** [supported] 官方 Learn 页面另称：当预付容量耗尽时，代理流执行将阻止新的运行，而非停用整个代理。 [ev_e1c1dc70ef05d675491e7b64](#ev_e1c1dc70ef05d675491e7b64)（supports）
  依据/推导：摘录直接陈述预付容量耗尽后的执行行为（vendor_official）。该条针对预付容量（容量包等）场景，不能直接等同于公平使用限制触发后的后果；公平使用限制的后果在已校验官方摘录中仍无明文。
- **c3_5** [supported] 第三方许可解读文章称：微软未公布该公平使用限制的确切阈值，并保留在模式出现时更新的权利。 [ev_bacc10ee26fa727620089a9f](#ev_bacc10ee26fa727620089a9f)（supports） [ev_4edded454f4abbb7c0a87db6](#ev_4edded454f4abbb7c0a87db6)（supports）
  依据/推导：两段均为 third_party 来源（许可解读站与高校知识库文章），仅作二手陈述，不能称为微软正式文档。其“未公布确切阈值”的表述与官方指南“保留更新权利”方向一致，但第三方称“未公布”本身不能替代官方条款，也不能作为关闭 gap1/gap4 的依据。
- **c3_7** [supported] 官方域名托管的 Power Platform Community 论坛帖中，用户报告在已登录 Microsoft 365 Copilot 许可、由用户发起交互的情况下，代理执行代理流时收到“InsufficientMcsCredits - The environment does not have sufficient Copilot Credits to run workflows.”错误。 [ev_a0c0976f0b0bb47f0454ecc7](#ev_a0c0976f0b0bb47f0454ecc7)（supports）
  依据/推导：该摘录来自 powerplatform.com 社区论坛（vendor_community：官方域名托管但作者为社区用户），属用户回帖而非微软发布的正式产品或许可文档。它显示持证场景下也可能触发信用不足报错，与“包含使用”的直觉存在张力，但单一用户帖不构成官方条款，也不能据此得出公平使用限制的具体阈值或后果。
- **c4_1** [supported] 微软官方《Microsoft Copilot Studio Licensing Guide》脚注4写明：面向员工的（Business to Employee）场景下，Microsoft Copilot Studio 代理及这些代理调用的 Copilot Studio 工具/功能，当代理使用者持有 Microsoft 365 Copilot 许可、且代理以该已验证的 Microsoft 365 Copilot USL 用户身份运行时，包含在 Microsoft 365 Copilot USL 中；此类使用受公平使用限制约束，微软保留在产品演进和出现新使用模式时更新限制的权利。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports）
  依据/推导：摘录来自微软官方许可指南 PDF（vendor_official），context_before 显示其处于脚注区（前文为预付方案到期与“4. Employee-facing scenarios”）。原文给出的是适用范围与限制存在性，未给出任何 Copilot Credit 数量，也未定义阈值或触发后果。
- **c4_2** [supported] 微软官方 Microsoft Learn《Billing rates and management》页面在费率说明处同样写明：使用受公平使用限制约束，微软保留在产品演进和出现新使用模式时更新限制的权利；该句紧接在“其他触发器的代理流按标准费率消耗 Copilot Credit”的说明之后。 [ev_9d0e356064e2f7be07f5f91f](#ev_9d0e356064e2f7be07f5f91f)（supports）
  依据/推导：ev_9d0e… 为 vendor_official 的 Learn 文档摘录，context_before 指向代理流计费段落。它确认“公平使用限制”与“可更新”的表述存在于官方 Learn 文档，但仍无论值数字，也未说明触发后的具体处置。
- **c4_3** [supported] 第三方文章（非微软官方）转述同一口径：持 Microsoft 365 Copilot User SL 的用户对面向员工的代理（Teams、SharePoint、M365 Copilot 场景，以持证用户身份运行）已含 Copilot Studio 使用权、无需额外费用，但受“公平使用”约束；该文称微软未公布确切阈值并保留更新权利。 [ev_966168a934515567ca58763e](#ev_966168a934515567ca58763e)（supports） [ev_fc03800a5261a44f1b5d5862](#ev_fc03800a5261a44f1b5d5862)（supports）
  依据/推导：两段均出自 licenseq.com（third_party），是对官方条款的二手解读，不能称为微软正式文档；其“未公布阈值”属第三方判断，不能替代 Product Terms 或 Learn 脚注正文。
- **c4_5** [supported] 在已校验的官方摘录中，公平使用限制的触发阈值、判定方式与触发后的具体后果（如降速、阻断运行、转按量计费等）均无明文；官方仅确认存在该限制并保留更新权利，官方 Learn 页面另说明预付容量耗尽时会阻止代理流的新运行，但该条针对预付容量而非公平使用限制。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_9d0e356064e2f7be07f5f91f](#ev_9d0e356064e2f7be07f5f91f)（supports） [ev_e1c1dc70ef05d675491e7b64](#ev_e1c1dc70ef05d675491e7b64)（supports）
  依据/推导：这是对已校验摘录覆盖范围的事实性归纳：两处官方文本只给“有限制、可更新”，容量耗尽条款属另一场景。不得把“容量耗尽阻止新运行”当作公平使用限制的后果，也不得把第三方“未公布阈值”当作官方否定事实。
- **c5_1** [supported] 微软官方 Copilot Studio 定价页 FAQ 仅笼统说明：随 Microsoft 365 Copilot 附带的 Copilot Studio 面向“已获许可用户”，用于在 Microsoft 365 内以 Copilot Chat 与 Standard harness 构建和使用内部代理；该页面并未在第一手官方摘录中列举 Microsoft 365 Copilot 合格基础许可的具体 SKU 清单。 [ev_d03281f6a8f3b10040fd8adb](#ev_d03281f6a8f3b10040fd8adb)（supports） [ev_0f72de9009f4ebdeb9f3d047](#ev_0f72de9009f4ebdeb9f3d047)（supports）
  依据/推导：两段为微软官方定价页 FAQ 连续摘录（vendor_official）。其只界定附带版与独立版的使用者与能力差异，未出现 E3/E5/Business Standard/Business Premium 等 SKU 列表；因此不能把第三方 SKU 清单写成官方事实。
- **c5_2** [supported] 微软官方《Microsoft Copilot Studio Licensing Guide》的许可对比表列出 Microsoft 365 Copilot 为每用户每月 30 美元并含“Included agent usage¹”，但摘录仅给出脚注编号 1/2/3，未含脚注正文；该指南亦自述不取代 Microsoft Product Terms 中的使用权法律文档。 [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports） [ev_ebc24156510a771ef0b63cea](#ev_ebc24156510a771ef0b63cea)（supports）
  依据/推导：ev_7d1d… 为官方指南表格摘录（vendor_official），ev_ebc2… 表明指南从属于 Product Terms。二者共同说明：官方许可指南本身不足以给出“包含代理使用”的数值口径，更不涉及基础许可 SKU 清单。价格属标价事实，不等于已实现收入。
- **c5_3** [supported] 第三方文章（非微软官方）列出 Microsoft 365 Copilot 的合格基础计划包括 Microsoft 365 E5、E3、F1、F3；Business Basic、Business Standard、Business Premium；Apps for business 与 Apps for enterprise；Office 365 E1、E3、E5、F3；Teams Essentials、Enterprise 与 EEA；Exchange、SharePoint、OneDrive、Planner、Project、Visio 等若干计划以及 Clipchamp。 [ev_bcff011e04cd21c7cb00be57](#ev_bcff011e04cd21c7cb00be57)（supports）
  依据/推导：ev_bcff… 出自 o365hq.com（third_party），context_before 提到“Microsoft 的 license-options article”，即该第三方在转述微软文档，但本轮未取得该官方文章原文。故仅作为二手清单记录，不能等同于微软官方文件所列清单。
- **c5_4** [supported] 同一第三方文章称较小的 SKU“Microsoft 365 Copilot Business”仅附加于 Microsoft 365 Business Basic、Business Standard、Business Premium 及 Apps for business，并将其席位上限表述为 300 席。 [ev_166813518580a59f6256b9bd](#ev_166813518580a59f6256b9bd)（supports）
  依据/推导：ev_1668… 为 third_party 来源，引述“微软目录描述”但本轮未取得对应官方页面，故只作为第三方陈述记录；不得据此断言官方条款中的席位上限与附加 SKU 对应关系。
- **c5_5** [supported] 另一第三方对比文章仅给出四个前提 SKU：Microsoft 365 E3、E5、Business Standard、Business Premium。 [ev_e19c2cf61ba4879c180642ba](#ev_e19c2cf61ba4879c180642ba)（supports）
  依据/推导：ev_e19c… 出自 hso.com（third_party），与 ev_bcff… 的清单范围不同（更窄）。两处第三方清单并不完全一致，这一差异本身即说明需以微软官方文件为准，不能任选其一作为官方结论。
- **c5_6** [supported] 官方域名托管的 Microsoft Community Hub 帖子（作者为社区贡献者，非微软发布的产品/许可文档）称合格基础许可包括：M365 Apps for enterprise 或 M365 Apps for business；M365 Business Basic、Business Standard、Business Premium；M365 E3、E5、F1、F3；M365 A1、A3、A5（教职员工）；Office 365 A1、A3、A5（教职员工或 18 岁以上高教学生）等。 [ev_8b455cd49b12e635d47daf94](#ev_8b455cd49b12e635d47daf94)（supports）
  依据/推导：ev_8b45… 来自 techcommunity.microsoft.com（vendor_community）：托管在官方域名，但内容是社区用户发布的技术说明，不能称为微软正式许可文档；其清单含教育版 SKU，与第三方清单互有出入，只能作为待官方确认的参考。
- **c6_1** [supported] 微软官方《Microsoft Copilot Studio Licensing Guide》的计费对比表将 Microsoft 365 Copilot 列示为每用户每月 30 美元，并在“Included agent usage”处标注脚注编号 1，在按量付费处标注“unlimited”及编号 2，在许可证（容量包）处列示每包 25,000 Copilot Credit 并标注编号 3；摘录未给出这些脚注的正文。 [ev_e3dbe5cb2ef0d4c42f067d30](#ev_e3dbe5cb2ef0d4c42f067d30)（supports） [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports）
  依据/推导：两条摘录均来自微软官方许可指南 PDF（vendor_official），分别属于同一文档的不同页面区块（预购换算表与计费对比表）。仅能支持“标价与脚注编号存在”，不能支持任何收入确认口径，也不能支持每席位包含的信用数量；价格属标价事实，不等于已实现收入或利润。
- **c6_2** [supported] 官方指南的 Copilot Credit 预购方案换算表列示：Commit Units（CCCU）按档位换算为 Copilot Credits，1 CCCU = 100 Copilot Credits，并对应若干“monthly MCS licenses（Copilot Credit capacity pack）”×12 个月，例如档位 1 为 3,000 CCCU、300,000 Copilot Credits、1 包×12 个月。 [ev_e3dbe5cb2ef0d4c42f067d30](#ev_e3dbe5cb2ef0d4c42f067d30)（supports）
  依据/推导：此摘录为 vendor_official 的预购换算表，直接陈述单位换算与档位对应关系。它说明信用用量路径具有预付/承诺（commit）结构，但摘录未涉及会计确认时点或收入分摊方式；承诺金额不等于已实现收入。
- **c6_3** [supported] 官方指南自述该文件不取代或不替换 Microsoft Product Terms 中关于使用权的法律文档；因此该指南中的表格与换算数据是许可说明材料，而非最终法律条款，也未包含任何收入确认说明。 [ev_ebc24156510a771ef0b63cea](#ev_ebc24156510a771ef0b63cea)（supports）
  依据/推导：该摘录来自指南前言性说明（vendor_official），直接表明指南的从属地位。因此本轮无法由该指南取得收入确认口径，此点构成缺口而非否定事实。
- **c6_4** [supported] 第三方文章（非微软官方）将 M365 Copilot 许可持有者的内部代理交互描述为“不消耗 Copilot Credits”，并将容量包列为每月 200 美元/25,000 信用、Commit Units 列为通过 Microsoft Azure 预付、最高 20% 折扣、按量付费为 0.01 美元/信用。 [ev_24adff377fb8485a1bfa0dbc](#ev_24adff377fb8485a1bfa0dbc)（supports） [ev_3bb21aa99cb70fd8ce1df4b4](#ev_3bb21aa99cb70fd8ce1df4b4)（supports）
  依据/推导：两条均出自 cloudzero.com（third_party），属二手转述，不能称为微软正式文档或正式定价页；其中的促销价与折扣信息未在官方摘录中确认。第三方对计费结构的描述不构成收入确认口径，也不能单独关闭缺口。
- **c6_5** [supported] 第三方文章（非微软官方）称，Copilot Studio 按量付费计量的是“没有席位的用户”的代理使用，以 Copilot Credits 计入客户自有的 Azure 订阅，预算告警但不封顶；容量包则是租户每月预付 25,000 信用，并且需要其背后存在按量付费计量。 [ev_4ce22fcf3c92e85663a7ba67](#ev_4ce22fcf3c92e85663a7ba67)（supports） [ev_335bc048fbe1377968e559f7](#ev_335bc048fbe1377968e559f7)（supports）
  依据/推导：两条均出自 o365hq.com（third_party），为二手陈述。其“计量计入 Azure 订阅”与官方定价页“使用代理需要 Azure 订阅”方向一致，但“预算不封顶”“容量包需按量作底”等细节未在官方摘录中逐字确认，故不当作官方条款。
- **c6_6** [supported] 第三方资料（Rand Group，非微软官方）提示客户应就自身许可核对具体权益，因为权益（entitlements）会随时间改变。 [ev_b6d70feeea344928917b06c7](#ev_b6d70feeea344928917b06c7)（supports）
  依据/推导：ev_b6d7… 出自 randgroup.com（third_party），是第三方的一般性提醒，不是微软对“每席位包含代理信用额度是否随时间调整”的官方确认。它支持“权益可变”这一方向，但不能作为官方变更依据，也不能据此认定存在具体调整。
- **c6_7** [supported] 官方指南与官方 Learn 文档在涉及 Microsoft 365 Copilot 许可下代理使用权的段落中写明：使用受公平使用限制约束，微软保留在产品演进并出现新使用模式时更新这些限制的权利。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_9d0e356064e2f7be07f5f91f](#ev_9d0e356064e2f7be07f5f91f)（supports）
  依据/推导：两条分别为 vendor_official 的许可指南脚注与 Learn 文档（先前已校验）。它们支持的只是“限制可更新、权益可演进”的存在性表述，未给出额度数字、阈值或具体变更历史，不能据此断言每席位信用额度已随时间调整。
- **c7_1** [supported] 微软官方 Microsoft Learn《License Options for Microsoft Copilot》页面在“Microsoft Copilot”标题下列出 Microsoft 365 计划：Microsoft 365 E7（已包含 Microsoft Copilot）、E5、E3、F1、F3、Business Premium、Business Standard、Business Basic、Apps for Enterprise、Apps for Business；并列出 Office 365 计划：Office 365 E5、E3、E1、F3。 [ev_73ffcca19e7a86bab3fcd561](#ev_73ffcca19e7a86bab3fcd561)（supports）
  依据/推导：摘录来自 learn.microsoft.com 官方页面（vendor_official），为清单式原文，主语为“Microsoft Copilot”页面的计划清单。quote 与 context_before/context_after 显示该清单归在“Microsoft Copilot”下，紧随其后为 F3、Teams 计划、Exchange 计划等条目。注意：原文标题为“Microsoft Copilot”，摘录未在同一段落中直接写明这些计划是“Microsoft 365 Copilot 附加许可的合格前提”，故本条仅支持“官方 license-options 文章列出这些计划”这一事实，不将其直接等同于合格前提的完整官方定义。
- **c7_2** [supported] 官方 Microsoft Learn《Microsoft Copilot requirements》页称：用户需要 Microsoft Copilot 许可和一个合格的前提许可（qualifying prerequisite license），并列计划清单参见《License options for Microsoft Copilot》与 Microsoft Copilot 服务说明；同段说明 Microsoft Copilot 不适用于 Microsoft 365 Apps for enterprise 的设备型许可。 [ev_02fefeab293305ad1b8b615e](#ev_02fefeab293305ad1b8b615e)（supports）
  依据/推导：vendor_official 摘录直接陈述“需 Copilot 许可 + 合格前提许可”，并把具体清单指向对应官方文章。这是官方对“存在合格前提许可清单”的口径确认，但摘录本身未列举 SKU；且主语为“Microsoft Copilot”，不区分 M365 Copilot 与 Copilot Business。
- **c7_4** [supported] 官方 Learn license-options 摘录中未出现教育版 A1/A3/A5 条目；教育版是否属于合格基础许可，本轮官方摘录未覆盖。第三方文章称学术报价对应 A1、A3、A5，官方域名社区帖也称包括 M365 A1/A3/A5（教职员工）与 Office 365 A1/A3/A5，但二者均非微软正式许可文档。 [ev_0d1dd9c8ca4c0e2027af7e9c](#ev_0d1dd9c8ca4c0e2027af7e9c)（supports） [ev_8b455cd49b12e635d47daf94](#ev_8b455cd49b12e635d47daf94)（supports）
  依据/推导：ev_0d1d… 为 third_party（o365hq.com）转述“学术报价附于 A1、A3、A5”；ev_8b45… 为 techcommunity.microsoft.com 的社区贡献者帖子（vendor_community），非微软发布的产品/许可文档。官方摘录 ev_73ff… 的清单在 Office 365 E1 之后进入 Teams 计划，未含 A 系列，但摘录为片段，不足以否定官方页面别处可能列有教育版，故仅表述为“本轮官方摘录未覆盖”。
- **c8_1** [supported] 微软官方《Microsoft Copilot Studio Licensing Guide》把“Copilot Credit 容量包”列为 Copilot Studio 订阅许可（Microsoft Copilot Studio License (Capacity pack)）：按租户配置、1 包 = 25,000 Copilot Credits/月、每包每月 200 美元（按年计费）、未用信用不结转；该节正文未出现“需要 Azure 订阅”的要求，只建议在信用包耗尽前启用按量付费计量以保证业务连续性。 [ev_67419540f72b4110f96c4ce1](#ev_67419540f72b4110f96c4ce1)（supports） [ev_2b9e141ce0074ba49ee0902f](#ev_2b9e141ce0074ba49ee0902f)（supports） [ev_376ddd08ecd4747fa61b4b19](#ev_376ddd08ecd4747fa61b4b19)（supports）
  依据/推导：三段为同一官方 PDF（vendor_official）第 4 节连续文本。原文陈述的是容量包的计价单位、有效期与耗尽后才计入按量计量的顺序，未就 Azure 订阅作出要求或豁免；因此不能把“未提及”读成“不需要”。价格属标价事实，不构成已实现收入或利润。
- **c8_2** [supported] 微软官方 Copilot Studio 定价页在介绍“Pre-purchase plan（预付 Copilot Credit Commit Units，最高约 20% 优惠）”的同一段落后写明“An Azure subscription is required to use agents.”（使用代理需要 Azure 订阅）。 [ev_8cba532208cb1ca2ecd4daaa](#ev_8cba532208cb1ca2ecd4daaa)（supports） [ev_215b99e850282a545db0bdc7](#ev_215b99e850282a545db0bdc7)（supports）
  依据/推导：两段为官方定价页（vendor_official）同一区块的连续摘录：ev_215b… 含预购方案描述并紧接该句，ev_8cba… 为同一句的独立摘录。该句以“使用代理”为主语，并未限定为“仅按量付费”，也未逐项说明容量包与 Commit Units 各自的 Azure 绑定条件，故不能从该页推出排除容量包的结论。
- **c8_3** [supported] 微软官方 Microsoft Learn《Standard harness licensing》在“Copilot Credits prepurchase plan”一节写明：该方案为一年期预付的 Copilot Credits，Copilot Credit Commit Units（CCCUs）池可在微软符合条件的产品间通用；可在 Azure 门户购买，并需要在 Power Platform 管理中心创建与你 Azure 订阅关联的计费策略（billing policy）。 [ev_73b717fd4ad93f190a3759ce](#ev_73b717fd4ad93f190a3759ce)（supports）
  依据/推导：ev_73b7… 为 vendor_official（learn.microsoft.com）的直述：预购 Commit Units 路径的购买与配置明确落在 Azure 门户与 Azure 订阅关联的计费策略上。这是对“Commit Units 路径是否需要 Azure 订阅”最直接的一条官方文本；但它描述的是购买与计费策略配置，未逐字说明“使用代理”是否另需 Azure 订阅。
- **c8_4** [supported] 微软官方 Microsoft Learn《Use Capacity Packs vs Pay-as-you-go Billing for Microsoft Copilot Chat》称：Copilot Studio 容量包是一种预付订阅，为 Copilot Chat 与 SharePoint 代理使用提供信用；每个容量包提供固定数量的 Copilot Credits 可在租户内使用，信用以每包每月 25,000 的数量提供；该摘录未提及容量包需要 Azure 订阅。 [ev_24a0e5a9ebd9f47c5a28d309](#ev_24a0e5a9ebd9f47c5a28d309)（supports）
  依据/推导：ev_24a0… 为 vendor_official 摘录，主语明确是“Microsoft Copilot Studio capacity pack”与 Copilot Chat/SharePoint 代理场景。摘录内容只界定容量包的性质与数量单位，未出现 Azure 订阅要求；这属于“未覆盖”，不等于官方否定 Azure 绑定。
- **c8_5** [supported] 第三方资料（非微软官方）称：容量包是租户级每月 25,000 信用的预付额度，先于按量计量被消耗，超额自动切换到关联 Azure 订阅上的按量付费；“按量付费必须先激活才能使用容量包”；另一处称容量包“需要其背后存在按量付费（pay-as-you-go）”。 [ev_1414eaa69e594715ad449156](#ev_1414eaa69e594715ad449156)（supports） [ev_4ce22fcf3c92e85663a7ba67](#ev_4ce22fcf3c92e85663a7ba67)（supports） [ev_282f584f443f4c65fe1002c8](#ev_282f584f443f4c65fe1002c8)（supports）
  依据/推导：三条均为 third_party（o365hq.com 等），属二手陈述，不能称为微软正式文档。其中“容量包需先有按量付费/Azure 计量作底”的说法与官方“建议在包耗尽前启用按量计量”“预购需 Azure 计费策略”方向相容，但第三方未提供条款级依据，不能单独关闭本缺口。
- **c9_1** [supported] 微软官方《Microsoft Copilot Studio Licensing Guide》对比表在同一 Microsoft 365 Copilot 行内并列三项：每用户每月 30 美元、Included agent usage（脚注1）、Pay-as-you-go: unlimited（脚注2）、License (capacity pack): 25,000 Copilot Credit /pack（脚注3），并在下一段列出“公平使用限制（脚注4）”；摘录仅含脚注编号与文字标签，未含脚注正文。 [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports） [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports）
  依据/推导：两条摘录为同一官方 PDF（vendor_official）同一表格的连续文本，context_after 显示“Pre-Purchase Plan: Depends on the tier3 Fair Usage Limit4”。可见脚注1/2/4 在本指南中均以编号出现，正文未进入已校验摘录，因此该事实只支持“脚注存在及其对应文字标签”，不支持额度数值或定义内容。价格属标价事实，不等于已实现收入。
- **c9_2** [supported] 同一官方指南的脚注4正文（针对员工面向/B2E 场景）写明：Microsoft Copilot Studio 代理及这些代理调用的 Copilot Studio 工具/功能，当代理使用者持有 Microsoft 365 Copilot 许可且代理以该已验证的 Microsoft 365 Copilot USL 用户身份运行，即包含在 Microsoft 365 Copilot USL 中；此类使用受公平使用限制，微软保留随着产品演进和新使用模式出现而更新限制的权利。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_3673df720bdda4517b7e7b6a](#ev_3673df720bdda4517b7e7b6a)（supports） [ev_14bb53ae5f936972c855ce26](#ev_14bb53ae5f936972c855ce26)（supports）
  依据/推导：三段同属官方许可指南（vendor_official）同一脚注段落：ev_0b38… 含完整句与其后“Usage is limited to fair usage limits…”，ev_3673…/ev_14bb… 为其子句的独立切分。context_before 显示该段起于脚注区“4. Employee-facing scenarios”。这是本轮能取得的最接近“公平使用限制”表述的官方原文，但其内容只是“存在限制+可更新”，未给出阈值数字、判定方法或触发后果。
- **c9_3** [supported] 微软官方 Microsoft Learn《Billing rates and management》在代理流按标准费率消耗信用的说明之后同样写明：使用受公平使用限制约束，微软保留在产品演进和新使用模式出现时更新限制的权利。 [ev_9d0e356064e2f7be07f5f91f](#ev_9d0e356064e2f7be07f5f91f)（supports）
  依据/推导：ev_9d0e… 为 vendor_official（learn.microsoft.com）摘录，context_before 指向“其他触发器的代理流按标准费率消耗信用”。它确认同一“限制存在、可更新”的表述也出现在官方运营文档中，但同样无论值或后果定义。
- **c9_4** [supported] 官方 Learn 费率表在“Used by Microsoft 365 Copilot licensed user”列对经典回答、生成式回答、代理操作、租户图谱 grounding、代理流操作（每100个操作）等均标“No charge”，同列给出相应信用消耗参照数；该页脚注另限定“No charge”包含仅适用于使用“When an agent calls the flow”触发器的代理流。 [ev_0fb7ca088ee9900f8d02961b](#ev_0fb7ca088ee9900f8d02961b)（supports） [ev_e1c1dc70ef05d675491e7b64](#ev_e1c1dc70ef05d675491e7b64)（supports）
  依据/推导：两条为 vendor_official 的 Learn 文档表格与脚注。这是官方对“持证用户包含使用”的具体呈现方式：以“不收费/不消耗信用”的方式表达，而非“每席位 N 个 Copilot Credit”的额度数。e1c1… 的 context_after 直接给出触发器的限定条件。
- **c9_5** [supported] 官方 Learn 页面另称：当预付容量耗尽时，代理流执行将阻止新的运行，而非停用整个代理；该条针对预付容量场景，摘录未将其表述为公平使用限制的触发后果。 [ev_e1c1dc70ef05d675491e7b64](#ev_e1c1dc70ef05d675491e7b64)（supports）
  依据/推导：ev_e1c1… 为 vendor_official 直述的“阻断新运行”行为。将其与公平使用限制区分，是因为官方摘录中二者出现在不同语境（一是容量耗尽，一是公平使用限制），不得混用为同一后果定义。
- **c9_6** [supported] 官方域名托管的 Power Platform 社区论坛帖（作者为社区用户，非微软发布的正式文档）中，用户称其在登录 Microsoft 365 Copilot 许可、以用户身份发起交互的情形下，代理执行代理流时报错“InsufficientMcsCredits - The environment does not have sufficient Copilot Credits to run workflows.”，并询问此类交互是否应被席位许可覆盖、是否需特定配置；同帖另有用户提到“这些是运行在 @Nivedipa-MSFT 所述公平使用限制内的简单代理”。 [ev_7cc5b878584f771eb4b892f7](#ev_7cc5b878584f771eb4b892f7)（supports） [ev_99ae51757ddf9d7f42ff49bd](#ev_99ae51757ddf9d7f42ff49bd)（supports）
  依据/推导：两条均来自 community.powerplatform.com（vendor_community）：官方域名托管但内容为社区用户发帖与回帖，不能称为微软正式产品或许可文档。该帖显示持证场景下仍可能出现信用不足报错，并显示社区层面把该问题归因于“公平使用限制”的判断，但均为用户观点，非条款正文，不能用于界定阈值或后果。
- **c9_11** [supported] 已校验官方摘录中，均未出现公平使用限制的阈值数字、判定方法或触发后的具体处置（降级、阻断、转计费）的条款正文；官方指南另自述不取代 Microsoft Product Terms 中的使用权法律文档。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_9d0e356064e2f7be07f5f91f](#ev_9d0e356064e2f7be07f5f91f)（supports） [ev_ebc24156510a771ef0b63cea](#ev_ebc24156510a771ef0b63cea)（supports）
  依据/推导：这是对已校验官方摘录覆盖范围的归纳。指南从属声明（ev_ebc2…，先前已校验）说明脚注正文与 Product Terms 仍是关闭本缺口的关键来源，因此本条不构成对缺口要求的实质回答。
- **c10_1** [supported] 微软官方 Microsoft Learn《Billing rates and management - Microsoft Copilot Studio》在说明代理流按标准费率消耗 Copilot Credit 之后写明：使用受公平使用限制（fair usage limits）约束，微软保留在产品演进、出现新使用模式时更新这些限制的权利。该页摘录未给出阈值数字、判定方法或触发后的具体处置。 [ev_fc583c4e5dba763afe0dbfeb](#ev_fc583c4e5dba763afe0dbfeb)（supports） [ev_9d0e356064e2f7be07f5f91f](#ev_9d0e356064e2f7be07f5f91f)（supports）
  依据/推导：两条摘录均来自 learn.microsoft.com（vendor_official）。ev_fc58… 的 context_before 为代理流按标准费率消耗信用、usage is limited 句，context_after 指向脚注编号 2/3，说明该句处于脚注区而非条款正文。故只支持“存在限制、可更新”，不能据此写出任何判定口径或后果。
- **c10_2** [supported] 同一官方 Learn 页面在“Overage enforcement（超额执行）”一节写明：当消耗超过可用容量时，环境处于超额状态；微软允许一定程度的超额消耗，类似宽限期，以避免阻断业务流程。该条讲的是容量耗尽后的超额处理，语境并非公平使用限制。 [ev_1a78c3e6f0177c1c93127970](#ev_1a78c3e6f0177c1c93127970)（supports）
  依据/推导：ev_1a78… 为 vendor_official 摘录，context_before 显示其属于“§Overage enforcement§ When consumption exceeds available capacity, the environment is in overage.”段。这是官方对“超过容量后如何处置”的唯一明确表述，但其主语是容量（付费容量/信用），不能挪用作公平使用限制的触发后果。
- **c10_3** [supported] 官方 Learn 页面另称：当预付容量耗尽时，代理流执行将阻止新的运行（blocks new runs），而不是停用整个代理。 [ev_e1c1dc70ef05d675491e7b64](#ev_e1c1dc70ef05d675491e7b64)（supports）
  依据/推导：ev_e1c1… 为先前已校验的 vendor_official 摘录，直接陈述预付容量耗尽后的执行行为。它说明官方存在“阻断新运行”这一处置方式，但适用范围是预付容量，而非公平使用限制；不能据此推断公平使用限制也以阻断方式执行。
- **c10_4** [supported] 官方域名托管的 Microsoft Q&A 问答帖（作者为社区用户，非微软发布的正式产品/许可文档）称：对于 Microsoft 365 Copilot API，微软明确执行限流与配额限制，“请求可能被限速或拒绝以保护服务可靠性并保证公平使用”，限制可按用户、按租户或按 API 设定并可随时调整；同帖又称现有材料中只有公平使用控制（功能限制、信用、SCU 容量、限流），但没有简单公布的“每小时 X 次请求”规则。 [ev_16b8d1419a040a935a7f0b36](#ev_16b8d1419a040a935a7f0b36)（supports） [ev_f7baf8ec2601b73fc7fe6904](#ev_f7baf8ec2601b73fc7fe6904)（supports）
  依据/推导：两条均来自 learn.microsoft.com/answers（vendor_community）：托管在官方域名，但内容是社区问答帖，作者不是微软正式发布渠道，不能称为厂商正式文档。其提到“限速或拒绝”的处置形态与官方 Learn 的“超额宽限”一致，但帖子同时承认没有公布具体规则；由于是二手社区表述，不能单独用于关闭 gap15。
- **c10_5** [supported] 第三方许可解读文章（licenseq.com，非微软官方）称：由 Microsoft 365 Copilot User SL 覆盖的员工面向 Copilot Studio 使用受微软未公布、且明确保留更新权利的公平使用限制约束；并称该限制对客户不可执行（unenforceable）。 [ev_fc03800a5261a44f1b5d5862](#ev_fc03800a5261a44f1b5d5862)（supports） [ev_a8a94e42dedbddf77d590df8](#ev_a8a94e42dedbddf77d590df8)（supports）
  依据/推导：两条均为 third_party 来源，是解读性评论，不是微软正式条款；“未公布阈值”“不可执行”属第三方判断，不能当作官方对判定口径的否定事实，也不能替代 Product Terms 正文。
- **c10_9** [supported] 官方域名托管的 Microsoft Q&A 帖中，有用户批评的核心不是“存在限制”，而是“用户被要求管理一项其无权测量的资源”，并呼吁提供可见的用量计量、可见的配额或额度、接近阈值时的预警，以及说明测量对象的清晰文档。 [ev_b7fe757cbefa407e70afb64a](#ev_b7fe757cbefa407e70afb64a)（supports）
  依据/推导：ev_b7fe… 为 vendor_community（社区帖），属用户观点与诉求，不是微软条款，也不能作为“官方未公布阈值”的正式确认；但其内容与官方只给“限制存在”表述的现状相互印证，可作为客户侧可观测性缺失的旁证，不能单独关闭缺口。

## 推导

- **c1_5** [supported] 就可核验的官方材料而言，两者在收费单位上可分：Microsoft 365 Copilot 以“每用户/月”席位为标价单位，Copilot Studio 以“Copilot Credit”用量（容量包、预购 Commit Units 或按量/关联 Azure 的计量）为标价单位，且官方称信用在租户层汇集而非按席位。 [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports） [ev_0f72de9009f4ebdeb9f3d047](#ev_0f72de9009f4ebdeb9f3d047)（supports） [ev_8cba532208cb1ca2ecd4daaa](#ev_8cba532208cb1ca2ecd4daaa)（supports）
  依据/推导：由官方指南表格（席位/月 vs 容量包与按量）及官方定价页（租户级销售、容量包、预购 Commit Units）直接推出计费口径差异。“租户汇集”这一措辞出自第三方（ev_581b…），官方摘录只支持“租户范围销售”，故此处仅作计费单位层面的推导，不外推汇集细节。
- **c1_6** [supported] 使用者范围上，Microsoft 365 Copilot 的附带 Copilot Studio 能力被限定为“已获许可用户”在 Microsoft 365 内构建/使用内部代理；独立 Copilot Studio 许可则允许未获许可用户使用所发布的外部代理，即把使用面从“内部持证员工”扩展到“外部/非持证终端用户”。 [ev_d03281f6a8f3b10040fd8adb](#ev_d03281f6a8f3b10040fd8adb)（supports） [ev_0f72de9009f4ebdeb9f3d047](#ev_0f72de9009f4ebdeb9f3d047)（supports）
  依据/推导：两段官方 FAQ 对比直接给出该差异，属明确推导而非新事实延伸。购买前提方面，官方定价页只笼统称需“合格的企业版或商业版 Microsoft 365 计划”，未列举具体 SKU；具体 SKU 清单仅见第三方（E3/E5/Business Standard/Business Premium），因此不作为官方事实。
- **c2_6** [supported] 在可核验的官方文本范围内，Copilot Studio 的付费路径至少三条并存且相互衔接：容量包（租户级、每包 25,000 信用/月、未用不结转）作为基础容量，耗尽后计入按量付费计量，另有 ACU 预购池可按折扣抵扣信用与 Foundry 用量；因此“扩展成本”取决于租户总信用消耗与所选路径组合，而非席位数量。 [ev_376ddd08ecd4747fa61b4b19](#ev_376ddd08ecd4747fa61b4b19)（supports） [ev_67419540f72b4110f96c4ce1](#ev_67419540f72b4110f96c4ce1)（supports） [ev_4f771c92962baa3167c08336](#ev_4f771c92962baa3167c08336)（supports）
  依据/推导：由“信用包耗尽后才计入按量计量”“容量包按租户月度配置且不结转”“ACU 池预付抵扣”三条官方陈述直接推出路径衔接关系。属明确推导；不含任何收入或利润结论。
- **c3_6** [supported] 就可核验的官方摘录而言，Microsoft 365 Copilot 每席位“Included agent usage”并未以固定 Copilot Credit 数字形式给出：官方文档的处理方式是“持证用户在其身份下运行的内部代理场景不计量（No charge）并辅以公平使用限制与脚注限定”，而非写明“每席位含 N 个信用”。 [ev_3673df720bdda4517b7e7b6a](#ev_3673df720bdda4517b7e7b6a)（supports） [ev_0fb7ca088ee9900f8d02961b](#ev_0fb7ca088ee9900f8d02961b)（supports） [ev_e1c1dc70ef05d675491e7b64](#ev_e1c1dc70ef05d675491e7b64)（supports） [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports）
  依据/推导：由三点推出：许可指南对比表只给脚注编号 1 而非数字（ev_5a44…）；Learn 费率表在持证用户列标 No charge 而非信用额度；公平使用限制条款未给数值。此为对官方文本呈现方式的推导，不等于证明“绝对不存在任何额度条款”——Product Terms 正文与脚注 1/2/4 内容尚未取得，故该推导仅描述已见文本的形态。
- **c4_4** [supported] 就可核验的官方文本而言，Microsoft 365 Copilot 每席位在 Copilot Studio 的“Included agent usage”并非以固定 Copilot Credit 数量表述，而是以“在符合条件（面向员工、以持证用户身份运行）时不计量/包含使用，并受公平使用限制约束、微软可随时更新限制”的方式表述。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_9d0e356064e2f7be07f5f91f](#ev_9d0e356064e2f7be07f5f91f)（supports） [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports）
  依据/推导：由三点推出：官方对比表在“Included agent usage”处只给脚注编号1而无数字（ev_5a44…）；脚注4正文以“included in USL + fair usage limits”表述（ev_0b38…）；Learn 文档重复该限制表述（ev_9d0e…）。此推导只描述已见官方文本的呈现形态，不排除未取得的脚注1/2正文或 Product Terms 中存在数值口径，故不据此关闭缺口。
- **c5_7** [supported] 在已校验证据中，Microsoft 365 Copilot 的合格基础许可 SKU 只出现在第三方与官方域名社区帖中，且各清单范围互不一致（第三方清单含 F1/F3、Office 365、Exchange/SharePoint/OneDrive 等；另一第三方仅列 E3/E5/Business Standard/Business Premium；社区帖另加教育版 A1/A3/A5）；微软官方 vendor_official 摘录仅以“已获许可用户”“合格的企业或商业版 Microsoft 365 计划”笼统表述，未给出 SKU 清单。 [ev_bcff011e04cd21c7cb00be57](#ev_bcff011e04cd21c7cb00be57)（supports） [ev_e19c2cf61ba4879c180642ba](#ev_e19c2cf61ba4879c180642ba)（supports） [ev_8b455cd49b12e635d47daf94](#ev_8b455cd49b12e635d47daf94)（supports） [ev_d03281f6a8f3b10040fd8adb](#ev_d03281f6a8f3b10040fd8adb)（supports）
  依据/推导：由各来源清单范围对比直接推出“仅有二手清单且相互不一致、官方摘录未列 SKU”这一结论。属对证据分布状态的推导，不判断哪份清单正确。
- **c5_8** [supported] 关于合格基础许可与 Copilot Studio 独立许可购买前提的对应关系，已校验官方材料只能支持两点：随 M365 Copilot 附带的 Copilot Studio 以“持有 M365 Copilot 许可且由该已验证用户身份运行”为适用条件；独立 Copilot Studio 许可则带来 GitHub Copilot harness、发布到外部渠道、非持证用户可使用代理等额外能力与定价选项。 [ev_d03281f6a8f3b10040fd8adb](#ev_d03281f6a8f3b10040fd8adb)（supports） [ev_0f72de9009f4ebdeb9f3d047](#ev_0f72de9009f4ebdeb9f3d047)（supports）
  依据/推导：两段官方 FAQ 连续摘录直接给出附带版与独立版差异。该推导不涉及“独立 Copilot Studio 许可是否需先具备特定基础 SKU”这一层，官方摘录中的“合格的企业或商业版 Microsoft 365 计划”亦未细化到 SKU，故不延伸。
- **c6_8** [supported] 就可核验官方材料而言，两条计费路径的单位不同：Microsoft 365 Copilot 以“每用户/月”席位为标价单位并附“包含代理使用”的脚注；Copilot Studio 以 Copilot Credit 用量为单位，经容量包（每包 25,000 信用）、按量（unlimited，受公平使用限制）与预购 Commit Units（1 CCCU = 100 信用）三条渠道取得。 [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports） [ev_e3dbe5cb2ef0d4c42f067d30](#ev_e3dbe5cb2ef0d4c42f067d30)（supports） [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports）
  依据/推导：由官方指南对比表（席位/月 vs 容量包与按量）与预购换算表及公平使用脚注直接推出。属计费单位层面的推导，不含收入确认口径；标价与单位换算不能推出已实现收入或利润。
- **c6_9** [supported] 在已校验的官方摘录中，未出现任何分部收入披露、收入确认（recognition）口径或席位/信用收入与财报科目对应关系的文字；官方材料只提供标价、单位换算与许可结构。 [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports） [ev_e3dbe5cb2ef0d4c42f067d30](#ev_e3dbe5cb2ef0d4c42f067d30)（supports） [ev_ebc24156510a771ef0b63cea](#ev_ebc24156510a771ef0b63cea)（supports）
  依据/推导：这是对已校验官方摘录覆盖范围的归纳：三份官方材料均为许可/定价说明文件，指南并自述从属于 Product Terms。故“收入确认如何对应”在本轮属未被证据覆盖的问题，须保留为开放缺口，不能把标价解释为收入。
- **c7_3** [supported] 就已校验的官方文档而言，Microsoft 365 Copilot 的合格基础许可 SKU 已由微软自身在 Learn 的 license-options 文章中列举，且覆盖 F1/F3、Office 365 E1/E3/E5/F3 以及 Apps for Business/Enterprise；因此此前“仅第三方与社区帖有清单”的情形已部分被官方来源取代。 [ev_73ffcca19e7a86bab3fcd561](#ev_73ffcca19e7a86bab3fcd561)（supports） [ev_02fefeab293305ad1b8b615e](#ev_02fefeab293305ad1b8b615e)（supports）
  依据/推导：由官方清单摘录（ev_73ff…）与官方“合格前提许可、清单见 license-options”说明（ev_02fe…）共同推出。属明确推导：官方来源已覆盖 F1/F3、Office 365 与 Apps 两类。限制：摘录中清单标题为“Microsoft Copilot”，未逐字出现“Microsoft 365 Copilot add-on eligible base licenses”字样；且教育版 A1/A3/A5 未出现在该摘录中，故不能声称官方已确认教育版。
- **c8_6** [supported] 就可核验的官方文本而言，Azure 订阅要求并非只出现在“按量付费”语境：官方 Learn 文档把预购 Commit Units 路径的购买与计费策略明确绑定到 Azure 门户与 Azure 订阅；官方定价页的“使用代理需要 Azure 订阅”一句位于预付 Commit Units 方案段落之后、以“使用代理”为主语。因此“仅按量付费计量需要 Azure 订阅”这一窄口径在官方材料中得不到支持。 [ev_73b717fd4ad93f190a3759ce](#ev_73b717fd4ad93f190a3759ce)（supports） [ev_215b99e850282a545db0bdc7](#ev_215b99e850282a545db0bdc7)（supports） [ev_8cba532208cb1ca2ecd4daaa](#ev_8cba532208cb1ca2ecd4daaa)（supports）
  依据/推导：由两条官方直述推出：预购路径的 Azure 绑定是明文（ev_73b7…），定价页的 Azure 要求不限定计费方式（ev_215b…/ev_8cba…）。属明确推导，但只否定“仅按量付费才需要”这一排他性表述，不等于证明容量包路径也必然强制 Azure 绑定。
- **c8_7** [supported] 对容量包路径，已校验官方摘录只有间接指向而无明文强制条款：官方指南将容量包称为“Copilot Studio 订阅许可”并规定信用包耗尽后计入按量计量，官方 Learn 容量包文章只述其性质而未提 Azure。因此“容量包本身是否同样强制 Azure 订阅”在官方证据中仍属未定，需条款级原文。 [ev_67419540f72b4110f96c4ce1](#ev_67419540f72b4110f96c4ce1)（supports） [ev_376ddd08ecd4747fa61b4b19](#ev_376ddd08ecd4747fa61b4b19)（supports） [ev_24a0e5a9ebd9f47c5a28d309](#ev_24a0e5a9ebd9f47c5a28d309)（supports）
  依据/推导：归纳已见官方文本的覆盖范围：容量包计费机制有明文（ev_6741…、ev_376d…），Azure 要求只在其他段落/其他路径出现（ev_24a0… 未提）。将“耗尽后计入按量计量”读成“容量包依赖 Azure 计量”是对机制的推导，第三方也如此描述，但官方未以条款措辞确认，故不扩写为事实。
- **c8_8** [supported] 官方指南给出容量包与按量付费之间的计量顺序：信用包未被耗尽前，消耗不计入按量付费计量；官方定价页另称 Commit Units 预购可“先选信用额度、管理月度变动用量”并最高约 20% 优惠。三条路径在同一 Copilot Credit 计量体系内衔接，但已校验官方摘录未给出三者之间完整的计量优先级与账单归属规则（如账单落在 MCA/Azure 订阅还是其他渠道）。 [ev_376ddd08ecd4747fa61b4b19](#ev_376ddd08ecd4747fa61b4b19)（supports） [ev_215b99e850282a545db0bdc7](#ev_215b99e850282a545db0bdc7)（supports） [ev_73b717fd4ad93f190a3759ce](#ev_73b717fd4ad93f190a3759ce)（supports）
  依据/推导：“包先于按量”为官方明文（ev_376d…）；预购定位见 ev_215b…；预购购买渠道见 ev_73b7…（Azure 门户 + Azure 订阅关联计费策略）。至于三者的全局优先级与账单归属，官方摘录仅有片段，故明确标注为未覆盖，而非否定其存在。折扣属标价机制，不构成收入结论。
- **c9_7** [supported] 在已校验的官方文本中，脚注1“Included agent usage”并未以固定 Copilot Credit 数量定义：指南对比表在该处只给脚注编号，官方 Learn 则以“持证用户不收费/不受计量的特性清单 + 触发器限定 + 公平使用限制”的形态表述包含关系。 [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports） [ev_0fb7ca088ee9900f8d02961b](#ev_0fb7ca088ee9900f8d02961b)（supports） [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_e1c1dc70ef05d675491e7b64](#ev_e1c1dc70ef05d675491e7b64)（supports）
  依据/推导：由三点推出：对比表在“Included agent usage”后仅有上标1（ev_5a44…）；Learn 费率表对持证用户列 No charge 而非信用额度（ev_0fb7…）；官方包含条款以 USL 包含 + fair usage limits 表述（ev_0b38…），并有触发器限定（ev_e1c1…）。该推导只描述已见官方文本的形态，不排除未取得的脚注1正文或 Product Terms 中另有数值口径。
- **c9_8** [supported] 对脚注2“Pay-as-you-go: unlimited”，已校验证据只能确认该文字标签的存在（与脚注编号同处一行），其“unlimited”的具体条件与是否与公平使用限制挂钩，官方摘录未见定义；第三方称微软不公布公平使用限制的精确阈值并保留更新权利，但这属third_party 解读，不能替代条款正文。 [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports） [ev_bacc10ee26fa727620089a9f](#ev_bacc10ee26fa727620089a9f)（supports）
  依据/推导：ev_5a44… 是官方表格中对“unlimited2”的唯一直接文本支撑，仅给标签；ev_bacc… 出自第三方许可解读站，为二手判断。因此“unlimited 与 fair usage 的关系”在官方证据中仍是未覆盖项，本条只作覆盖范围归纳，不能写成官方定义。
- **c10_6** [supported] 在已校验的官方文本中，公平使用限制与“容量耗尽/超额”是两套不同机制：前者只有“存在限制、微软可更新”的表述，无阈值与后果定义；后者则有明确处置表述（允许类似宽限期的超量消耗，预付容量耗尽时阻止代理流的新运行）。因此不能用超额执行条款回答公平使用限制的判定口径与触发后果。 [ev_fc583c4e5dba763afe0dbfeb](#ev_fc583c4e5dba763afe0dbfeb)（supports） [ev_1a78c3e6f0177c1c93127970](#ev_1a78c3e6f0177c1c93127970)（supports） [ev_e1c1dc70ef05d675491e7b64](#ev_e1c1dc70ef05d675491e7b64)（supports）
  依据/推导：由三条官方摘录的语境对比推出：ev_fc58… 位于代理流计费/脚注段，ev_1a78… 与 ev_e1c1… 位于容量与超额执行段。属明确推导；结论仅限“不能混用”，不主张公平使用限制必然没有后果，只是已校验官方文本未载明。
- **c10_7** [supported] 就可核验证据而言，微软官方渠道（Learn 文档与许可指南）对公平使用限制的表述停留在“使用受公平使用限制约束、微软保留更新权”，属于存在性与可变更性声明，而非判定口径与处置规则；涉及“限速/拒绝”的具体处置只见于官方域名下的社区问答帖（vendor_community），须与厂商正式文档区分。 [ev_fc583c4e5dba763afe0dbfeb](#ev_fc583c4e5dba763afe0dbfeb)（supports） [ev_16b8d1419a040a935a7f0b36](#ev_16b8d1419a040a935a7f0b36)（supports） [ev_f7baf8ec2601b73fc7fe6904](#ev_f7baf8ec2601b73fc7fe6904)（supports）
  依据/推导：由官方 Learn 摘录与社区帖的权威级别对比推出。这是对证据分布状态的归纳，回答的是“是否有官方文件给出判定口径与处置”的现状，而不是宣称官方从未存在此类文件；Product Terms 脚注正文尚未取得，构成缺口而非否定事实。

## 商业判断

- **c3_8** [supported] 对企业客户而言，在官方公平使用限制阈值与触发后果未公开的情况下，把高并发或面向外部渠道的代理运行建立在“M365 Copilot 席位已包含使用”的假设上存在用量与成本不确定性；较稳妥的扩展做法是同时准备独立 Copilot Studio 容量或按量计费通道。 [ev_3673df720bdda4517b7e7b6a](#ev_3673df720bdda4517b7e7b6a)（supports） [ev_e1c1dc70ef05d675491e7b64](#ev_e1c1dc70ef05d675491e7b64)（supports） [ev_a0c0976f0b0bb47f0454ecc7](#ev_a0c0976f0b0bb47f0454ecc7)（supports）
  依据/推导：基于“限制可调整且未公开数值”“容量耗尽会阻断新运行”“社区报告持证场景仍出现信用不足”的事实做商业判断。属判断而非事实，不能作为对微软收入或客户成本的量化结论；标价与不计量机制均不等于已实现收入或利润。
- **c5_9** [supported] 在合格 SKU 清单与“附带版/独立版”的购买前提对应关系未被官方逐一确认前，企业客户若按第三方清单规划席位扩容，可能因实际不合格基础许可而被迫搭配额外基础计划，从而改变单用户实际成本结构；这提示席位与信用两条收费路径的相对吸引力会随客户既有基础许可组合而异。 [ev_bcff011e04cd21c7cb00be57](#ev_bcff011e04cd21c7cb00be57)（supports） [ev_e19c2cf61ba4879c180642ba](#ev_e19c2cf61ba4879c180642ba)（supports） [ev_d03281f6a8f3b10040fd8adb](#ev_d03281f6a8f3b10040fd8adb)（supports）
  依据/推导：基于“二手清单互不一致”“官方仅笼统表述合格计划”的事实作商业判断。属判断而非事实，且不涉及任何已实现收入或利润；标价与许可结构不能推出收入结论。
- **c6_11** [supported] 对企业客户而言，由于席位路径的“包含代理使用”受可更新的公平使用限制约束，而信用路径按租户总量计费（容量包不结转、耗尽后转按量或预购抵扣），扩展开支的可预测性更多取决于租户代理使用总量与所选信用渠道，而非持证人数；这使席位与信用两条路径在客户规模扩张时的成本结构呈不同弹性。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_e3dbe5cb2ef0d4c42f067d30](#ev_e3dbe5cb2ef0d4c42f067d30)（supports） [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports）
  依据/推导：基于“包含使用受可更新公平使用限制”“信用按档位/包与用量计量”的事实作商业判断。属判断而非事实，未量化任何金额，也不涉及已实现收入、利润或收入确认；容量包“不结转”等细节来自先前已校验摘录（ev_6741…），此处不再重复引用。
- **c7_5** [supported] 由于官方 license-options 文章已把 F1/F3、Office 365 计划与 Apps for Business/Enterprise 纳入同一清单，企业客户在规划 M365 Copilot 席位扩容时的“可附加基数”明显宽于“仅 E3/E5/Business”口径；但清单标题为“Microsoft Copilot”，客户仍需就具体附加 SKU（企业版或 Business）逐项核对，以免把 Business 版 300 席上限等限制误用于企业版。 [ev_73ffcca19e7a86bab3fcd561](#ev_73ffcca19e7a86bab3fcd561)（supports） [ev_02fefeab293305ad1b8b615e](#ev_02fefeab293305ad1b8b615e)（supports）
  依据/推导：基于官方清单范围与“需合格前提许可”口径作商业判断。属判断而非事实；不涉及任何已实现收入或利润，标价/许可清单不能推导收入。第三方所述 300 席上限未在官方摘录中确认，故仅作为“需核对”的提示而非事实断言。
- **c8_9** [supported] 若预购 Commit Units 与容量包在实际部署中都需要 Azure 订阅与计费策略，则即使客户已持有 Microsoft 365 Copilot 席位，任何超出席位“包含使用”的代理扩展仍需建立 Azure 账单通道，这会把信用路径的采购纳入云消费治理（预算、成本中心）体系；反之若容量包可脱离 Azure 采购，席位与容量包可构成纯 Microsoft 365 侧的扩展组合。该差异影响客户的采购审批路径而非已实现收入。 [ev_73b717fd4ad93f190a3759ce](#ev_73b717fd4ad93f190a3759ce)（supports） [ev_67419540f72b4110f96c4ce1](#ev_67419540f72b4110f96c4ce1)（supports）
  依据/推导：基于“预购路径明文需 Azure 计费策略”“容量包为订阅许可但 Azure 要求未明文”作商业判断。属判断而非事实，未量化金额，也不把标价当作收入或利润。
- **c9_9** [supported] 就企业采购含义看，若“包含代理使用”以“持证不计量 + 未公开且可更新的公平使用限制”表述，而“按量付费 unlimited”同样受限制制约，则客户无法从公开官方文本推算每席位的等值信用量，扩展规划只能以实测用量与备用信用通道（容量包/按量/预购）作对冲；这构成席位路径与信用路径之间在可预测性上的实质差异。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_9d0e356064e2f7be07f5f91f](#ev_9d0e356064e2f7be07f5f91f)（supports） [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports）
  依据/推导：基于官方“限制存在且可更新”“持证清单不收费”与“按量标注 unlimited 却并列公平使用限制脚注”的事实作商业判断。属判断而非事实，未量化任何金额，也未推出已实现收入或利润；标价与包含机制不能等同于收入确认。
- **c10_8** [supported] 对企业客户而言，在公平使用限制的判定口径与触发后果未被官方文件量化的前提下，只要把高用量或高并发的代理运行建立在“M365 Copilot 席位已包含”之上，就会引入执行层面的不确定性；较稳妥的做法是把预付容量/按量通道作为对冲，并自行做用量监测，因为可核验的官方文字只保证“存在限制且可更新”，不保证任何阈值。 [ev_fc583c4e5dba763afe0dbfeb](#ev_fc583c4e5dba763afe0dbfeb)（supports） [ev_16b8d1419a040a935a7f0b36](#ev_16b8d1419a040a935a7f0b36)（supports） [ev_1a78c3e6f0177c1c93127970](#ev_1a78c3e6f0177c1c93127970)（supports）
  依据/推导：基于“官方仅确认限制存在与可更新”“社区问答称请求可能被限速或拒绝”“官方对超额允许类似宽限期的消耗”作商业判断。属判断而非事实，未量化任何金额，也不把标价或许可结构当作已实现收入或利润。

## 待验证假设

- **c2_7** [unverified] Microsoft 365 Copilot 每席位“包含的代理使用额度”可能并非以固定数量的 Copilot Credit 表示（对比表将其列为脚注 1，而非直接给出数字），而是以“按量付费 unlimited + 公平使用限制”的形式体现；若成立，则席位许可与信用计量之间不存在简单换算。 [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports）
  依据/推导：表格摘录在“Included agent usage1”处仅给脚注编号，其数值口径与公平使用限制定义均未出现在已校验摘录中。该假设不能用于关闭 gap1，仅为解释脚注 1 缺失的可能方向，须以正式 Product Terms 章节验证。
- **c4_6** [unverified] 公平使用限制可能以未公开的内部阈值或使用模式判断执行，触发后可能表现为限制高用量场景（如高并发或外部渠道代理使用）或要求转向独立付费通道；该机制的具体内容需以 Microsoft Product Terms 脚注正文或完整许可指南脚注1/2/4确认。 [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_fc03800a5261a44f1b5d5862](#ev_fc03800a5261a44f1b5d5862)（supports）
  依据/推导：官方只确认限制存在与可更新，第三方提出“高用量场景不被覆盖”的判断（ev_fc03…），二者均未给出阈值或后果定义，故只能作为待验证假设，不能用于回答或关闭缺口。
- **c5_10** [unverified] 独立 Copilot Studio 许可的购买前提可能与 M365 Copilot 的合格基础许可清单并非同一集合——即存在“可作为独立 Copilot Studio 附加前提、但不在 M365 Copilot 合格 SKU 内”的计划，或反之；此差异需以 Microsoft Product Terms 或官方 license-options 文章核实。 [ev_e19c2cf61ba4879c180642ba](#ev_e19c2cf61ba4879c180642ba)（supports） [ev_8b455cd49b12e635d47daf94](#ev_8b455cd49b12e635d47daf94)（supports）
  依据/推导：已校验摘录中，独立 Copilot Studio 的前提仅被笼统表述为“合格的企业或商业版 Microsoft 365 计划”，与 M365 Copilot 的 SKU 清单未在同一官方文本中对齐；二手清单互不一致使该可能性无法排除。仅为待验证假设，不能用于关闭 gap2。
- **c6_10** [unverified] M365 Copilot 每席位“Included agent usage”可能自始未以固定 Copilot Credit 数量定义，而是以“持证场景不计量 + 公平使用限制、微软可更新”的方式表达，从而使额度随产品演进以限制口径而非固定数值调整。 [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports） [ev_0b38cd8a1f64f34d14c759b0](#ev_0b38cd8a1f64f34d14c759b0)（supports） [ev_b6d70feeea344928917b06c7](#ev_b6d70feeea344928917b06c7)（supports）
  依据/推导：对比表在“Included agent usage”处只给脚注编号而无数字，脚注正文与 Product Terms 正文未取得；第三方仅提醒权益会变。故只能作为待验证假设，不能用于回答“是否随时间调整”或关闭 gap3。
- **c7_6** [unverified] 教育版 A1/A3/A5 可能确实属于官方合格的附加前提计划，但仅出现在 license-options 文章未被本轮抓取收录的章节或学术报价页中；需取得该官方页面完整正文以验证。 [ev_0d1dd9c8ca4c0e2027af7e9c](#ev_0d1dd9c8ca4c0e2027af7e9c)（supports） [ev_8b455cd49b12e635d47daf94](#ev_8b455cd49b12e635d47daf94)（supports）
  依据/推导：官方摘录为片段（start 2265、end 2640），清单在 Office 365 项中途截断，无法据此判断后续是否列出 A 系列。第三方与社区帖提供了肯定说法但均非正式文档。故仅为待验证假设，不能用于关闭关于教育版的那部分要求。
- **c8_10** [unverified] 容量包路径可能也需要先建立与 Azure 订阅关联的按量付费计量作为底层通道（第三方如此描述），官方指南“耗尽后计入按量计量”与定价页“使用代理需要 Azure 订阅”可能共同指向这一设计；但这需 Product Terms 或完整许可指南条款确认。 [ev_376ddd08ecd4747fa61b4b19](#ev_376ddd08ecd4747fa61b4b19)（supports） [ev_8cba532208cb1ca2ecd4daaa](#ev_8cba532208cb1ca2ecd4daaa)（supports） [ev_4ce22fcf3c92e85663a7ba67](#ev_4ce22fcf3c92e85663a7ba67)（supports）
  依据/推导：官方两条摘录可作间接支持，第三方作直接陈述但非正式文档，缺少条款级明文，故只能作为待验证假设，不能用于关闭 gap5 的容量包部分。
- **c9_10** [unverified] “unlimited”可能指的是持证场景下按量计量不设信用上限拦截（即在公平使用限制内不计信用），而公平使用限制可能在极端使用模式下以运营方式（如限速、要求专配置或转独立计费）执行而非在文档中给出数值；此推断需以 Product Terms 脚注1/2/4 正文验证。 [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports） [ev_7cc5b878584f771eb4b892f7](#ev_7cc5b878584f771eb4b892f7)（supports）
  依据/推导：官方仅给标签与“限制可更新”表述，社区帖显示持证场景仍可能报信用不足，提示执行机制可能与文档字面不完全一致。二者都不足以确定定义或后果，故只能作待验证假设，不得用于关闭 gap4。
- **c10_10** [unverified] 公平使用限制可能以未公开的内部阈值或使用模式判断执行，触发后可能表现为限流、拒绝请求或要求转向独立计费通道；这一形态与社区帖及第三方解读的描述一致，但仍需 Microsoft Product Terms 脚注正文或完整许可指南脚注 1/2/4 的条款级原文确认。 [ev_16b8d1419a040a935a7f0b36](#ev_16b8d1419a040a935a7f0b36)（supports） [ev_fc03800a5261a44f1b5d5862](#ev_fc03800a5261a44f1b5d5862)（supports）
  依据/推导：官方摘录未给阈值与后果；支持该形态的均为 vendor_community 帖与 third_party 文章。故只能作为待验证假设，不能用于回答或关闭 gap15。

## 证据缺口

- gap0 [open] Microsoft 365 Copilot 与 Copilot Studio 面向的企业使用者、收费单位和购买前提有何区别？这些差异可能如何影响企业客户扩展使用和微软的收入来源？优先使用官方资料；将价格与许可事实、基于事实的推导、商业判断和仍待验证假设明确区分，不把产品定价直接当成已实现收入或利润。
- gap1 [open] 需要微软正式许可条款（Product Terms / 许可指南完整章节）逐条确认：Microsoft 365 Copilot 每席位包含的 Copilot Studio 信用额度数量与“按量付费 unlimited”及公平使用限制（fair usage limit）的具体定义，以及 Copilot Studio 按量计费是否必须绑定 Azure 订阅、容量包与预购 Commit Units 各自的适用条件。这些是判断计费单位与扩展成本的必要依据，现有官方摘录仅为表格片段与 FAQ。
- gap2 [open] 需要微软官方文件明确 Microsoft 365 Copilot 的合格基础许可 SKU 清单（如 E3、E5、Business Standard、Business Premium 等）及其与 Copilot Studio 独立许可购买前提的精确对应关系；目前仅第三方列出具体 SKU，官方摘录仅称“合格的企业或商业版 Microsoft 365 计划”。
- gap3 [open] 需要微软官方渠道（财报分部披露、正式定价/许可页）说明席位制定价与信用用量计费分别如何对应收入确认口径，并核实 M365 Copilot 每席位包含的代理信用额度是否随时间调整；现有材料只有标价，无法支持任何已实现收入或利润判断。
- gap4 [open] 需要 Microsoft Product Terms 或完整许可指南脚注正文，明确“Included agent usage”在 Microsoft 365 Copilot 席位下的具体额度口径（是否为固定 Copilot Credit 数量）以及“按量付费 unlimited”与 fair usage limit 的定义与触发后果；现有官方摘录仅显示脚注编号 1/2，无脚注内容。
- gap5 [open] 需要官方条款明确 Azure 订阅要求的适用边界：Copilot Studio 按量付费是否强制绑定 Azure 订阅，容量包与预购 Commit Units 路径是否同样需要，以及三者之间的计量优先级与账单归属；现有官方定价页仅在预购方案段落附近出现该表述。
- gap6 [open] 需要取得 Microsoft Product Terms 或完整许可指南中脚注1/2/4（included agent usage、pay-as-you-go unlimited、fair usage limit）的正文，以确认是否以固定 Copilot Credit 数量表示额度、公平使用限制的阈值定义及触发后的具体后果（降级、阻断或转计费）；现有官方摘录仅有脚注编号与“受公平使用限制、可更新”的表述。
- gap7 [open] 需要微软官方 license-options 文章或 Microsoft Product Terms 原文，以官方口径确认并列举 Microsoft 365 Copilot 的合格基础许可 SKU 清单（含是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5、及 Apps for business/enterprise 等），取代目前仅有的第三方与社区帖清单。
- gap8 [open] 需要微软官方文件明确独立 Copilot Studio 许可购买前提中“合格的企业或商业版 Microsoft 365 计划”的具体所指，及其与 M365 Copilot 合格 SKU 清单是否为同一集合、是否存在差异（含是否需 Azure 订阅）。
- gap9 [open] 需要微软官方页面确认“Microsoft 365 Copilot Business”与“Microsoft 365 Copilot（企业版）”两个 SKU 各自可附加的基础计划及席位上限（如 300 席），现有说法仅来自第三方转述的目录描述。
- gap10 [open] 需要微软官方财报（10-K/10-Q 分部披露与收入确认政策）或正式定价/许可页，明确 Microsoft 365 Copilot 席位订阅与 Copilot Studio 信用用量（容量包、按量、预购 Commit Units）在收入确认上的口径（订阅按期间确认 vs 用量/承诺按消耗或分摊确认），以及两者归属的报告分部；现有官方材料仅为许可指南与定价页，无任何收入确认文字。
- gap11 [open] 需要微软官方条款或权益变更公告（Product Terms、许可指南历史版本或 Message Center 通知）核实 Microsoft 365 Copilot 每席位包含的代理信用/代理使用额度是否曾随时间调整及调整内容；现有官方摘录只显示“Included agent usage”脚注编号与“微软保留更新公平使用限制的权利”，未含额度数值或变更记录。
- gap12 [open] 需要 Microsoft Learn《License Options for Microsoft Copilot》页面完整正文（或其对应的 Product Terms 章节），以官方口径确认：该清单是否确为 Microsoft 365 Copilot 附加许可的合格基础前提；是否列出教育版 A1/A3/A5（教职员工/学生）以及是否区分 Microsoft 365 Copilot（企业版）与 Microsoft 365 Copilot Business 两 SKU 各自的附加计划范围。现有官方摘录在 Office 365 计划中途截断，且标题为“Microsoft Copilot”。
- gap13 [open] 需要 Microsoft Product Terms 或 Copilot Studio 许可指南中关于“An Azure subscription is required to use agents”的条款级原文（含适用范围限定），以明确该要求是否覆盖容量包（Copilot Credit capacity pack）路径、预购 Commit Units 路径与按量付费路径三者，以及是否存在仅限按量计量的例外语境。
- gap14 [open] 需要微软官方文件（Product Terms、许可指南或 Azure/Power Platform 计费文档）说明容量包、按量付费计量与预购 Commit Units 三者之间的计量优先级与账单归属（账单落在哪一订阅/合同、超额如何切换），现有官方摘录仅有“包耗尽前不计入按量计量”的片段。
- gap15 [open] 需要微软官方文件（Product Terms、服务说明或合规/使用政策页）给出 fair usage limit 的判定口径与触发后果（如限速、阻断运行、要求转独立计费），而非仅“存在限制、微软可更新”的表述。

## 问题与检索记录

- q0 / 第 0 轮 / 缺口 初始问题：Microsoft 365 Copilot 与 Copilot Studio 面向的企业使用者、收费单位和购买前提有何区别？这些差异可能如何影响企业客户扩展使用和微软的收入来源？优先使用官方资料；将价格与许可事实、基于事实的推导、商业判断和仍待验证假设明确区分，不把产品定价直接当成已实现收入或利润。
- q1 / 第 1 轮 / 缺口 gap0：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。
  Tavily search1：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；结果 5；错误 无
- q2 / 第 2 轮 / 缺口 gap1：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。
  Tavily search2：Copilot Studio licensing guide fair usage limit；结果 5；错误 无
- q3 / 第 3 轮 / 缺口 gap1：微软官方 Product Terms 或完整许可条款中，Microsoft 365 Copilot 每席位“Included agent usage”对应的具体 Copilot Credit 数量是多少，公平使用限制（fair usage limit）如何定义、触发后有何后果？
  Tavily search3：Microsoft Product Terms Copilot Studio included agent usage；结果 5；错误 无
- q4 / 第 4 轮 / 缺口 gap4：Microsoft 365 Copilot 每席位在 Copilot Studio 中“Included agent usage”对应的额度是以固定 Copilot Credit 数量表示，还是以“可按量使用但受公平使用限制”的方式表示？官方 Product Terms 或 Learn 许可文档的脚注对“included agent usage”和 fair usage limit 如何定义、触发后有何后果？
- q5 / 第 5 轮 / 缺口 gap2：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？
  Tavily search4：Microsoft 365 Copilot prerequisites eligible plans license requirements；结果 5；错误 无
- q6 / 第 6 轮 / 缺口 gap3：微软官方财报分部披露或正式定价/许可页面中，Microsoft 365 Copilot 的席位制收入与 Copilot Studio 的信用用量（容量包、按量付费、预购 Commit Units）收入分别如何对应收入确认口径，且 M365 Copilot 每席位包含的代理信用额度是否随时间调整？
  Tavily search5：Microsoft 365 Copilot revenue recognition credits；结果 5；错误 无
- q7 / 第 7 轮 / 缺口 gap7：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？
  Tavily search6：Microsoft 365 Copilot license options eligible base licenses；结果 5；错误 无
- q8 / 第 8 轮 / 缺口 gap5：微软官方文档是否明确 Copilot Studio 容量包（Copilot Credit 容量包，每包 25,000 信用）与预购 Commit Units 路径在使用代理时同样需要 Azure 订阅，而不仅是按量付费计量需要？
  Tavily search7：Copilot Studio capacity pack Azure subscription requirement；结果 5；错误 无
- q9 / 第 9 轮 / 缺口 gap4：Microsoft Product Terms 或完整许可指南脚注正文中，Microsoft 365 Copilot 席位下“Included agent usage”（脚注1）是否以固定 Copilot Credit 数量定义，以及“按量付费 unlimited”（脚注2）与 fair usage limit 的定义与触发后果如何表述？
- q10 / 第 10 轮 / 缺口 gap15：微软是否有官方文件（Product Terms、服务说明或公平使用政策页）给出 fairness/fair usage limit 的判定口径与触发后的具体处置（限速、阻断运行或转独立计费），而非仅“存在限制、可更新”的表述？
  Tavily search8：Microsoft Product Terms Copilot Studio fair usage limit；结果 5；错误 无

## 原文摘录与追溯

<a id="ev_5f9c6c0b1525ac6058573928"></a>
### ev_5f9c6c0b1525ac6058573928

> Copilot for Microsoft 365 uses fixed per-user licensing. Copilot Studio uses consumption billing through Copilot Credits.

来源：Microsoft Copilot vs Copilot Studio + Cowork: Key Differences (2026) — https://www.hso.com/blog/microsoft-copilot-vs-studio/

类型：web；读取时间：2026-10-19T08:22:57.302469+00:00；截断：False

问题 q1 → 分块 chk_1f444fdde6bc33ac0db439f8_6630 → 来源 src_1f444fdde6bc33ac0db439f8；清洗后字符 [6776, 6897)

SHA-256：`65de4d548f8e19533fd7392baf56d4b9982c6993445097ad37bed59c7e536b92`；范围：<main> element; characters 0-20914 of 20914

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.hso.com/blog/microsoft-copilot-vs-studio
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_a84c833dd8a8158d3eaad801"></a>
### ev_a84c833dd8a8158d3eaad801

> Organizations pay a monthly subscription per user. Prerequisites include Microsoft 365 E3, E5, Business Standard, or Business Premium.

来源：Microsoft Copilot vs Copilot Studio + Cowork: Key Differences (2026) — https://www.hso.com/blog/microsoft-copilot-vs-studio/

类型：web；读取时间：2026-10-19T08:22:57.302469+00:00；截断：False

问题 q1 → 分块 chk_1f444fdde6bc33ac0db439f8_6630 → 来源 src_1f444fdde6bc33ac0db439f8；清洗后字符 [6936, 7070)

SHA-256：`65de4d548f8e19533fd7392baf56d4b9982c6993445097ad37bed59c7e536b92`；范围：<main> element; characters 0-20914 of 20914

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.hso.com/blog/microsoft-copilot-vs-studio
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_50b25e4157e22ea241e07a33"></a>
### ev_50b25e4157e22ea241e07a33

> Copilot Studio charges based on consumption measured in Copilot Credits. Authoring agents is free. Running agents consumes credits based on usage.

来源：Microsoft Copilot vs Copilot Studio + Cowork: Key Differences (2026) — https://www.hso.com/blog/microsoft-copilot-vs-studio/

类型：web；读取时间：2026-10-19T08:22:57.302469+00:00；截断：False

问题 q1 → 分块 chk_1f444fdde6bc33ac0db439f8_7140 → 来源 src_1f444fdde6bc33ac0db439f8；清洗后字符 [7442, 7588)

SHA-256：`65de4d548f8e19533fd7392baf56d4b9982c6993445097ad37bed59c7e536b92`；范围：<main> element; characters 0-20914 of 20914

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.hso.com/blog/microsoft-copilot-vs-studio
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_578f724fd92ed7c8f5e49975"></a>
### ev_578f724fd92ed7c8f5e49975

> Capacity Packs: Start at $200/month for 25,000 credits

来源：Microsoft Copilot vs Copilot Studio + Cowork: Key Differences (2026) — https://www.hso.com/blog/microsoft-copilot-vs-studio/

类型：web；读取时间：2026-10-19T08:22:57.302469+00:00；截断：False

问题 q1 → 分块 chk_1f444fdde6bc33ac0db439f8_7140 → 来源 src_1f444fdde6bc33ac0db439f8；清洗后字符 [7651, 7705)

SHA-256：`65de4d548f8e19533fd7392baf56d4b9982c6993445097ad37bed59c7e536b92`；范围：<main> element; characters 0-20914 of 20914

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.hso.com/blog/microsoft-copilot-vs-studio
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_7d1d68228d013e72f6062cf1"></a>
### ev_7d1d68228d013e72f6062cf1

> Microsoft 365 Copilot $30 per user/month Included agent usage1 Pay-as-you-go: unlimited2 License (capacity pack): 25,000 Copilot Credit /pack3

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q1 → 分块 chk_c68aacefe8ad1e6fd48eeabb_13260 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [13714, 13856)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_d03281f6a8f3b10040fd8adb"></a>
### ev_d03281f6a8f3b10040fd8adb

> Copilot Studio that’s included with Microsoft 365 Copilot lets the licensed users build and use internal agents within Microsoft 365 using the Copilot Chat and Standard harness at no additional cost.

来源：Microsoft Copilot Studio Plans and Pricing — https://www.microsoft.com/en-us/copilot/pricing/copilot-studio

类型：web；读取时间：2026-10-19T08:23:18.966505+00:00；截断：False

问题 q1 → 分块 chk_0974f6cd66d2bc4ca55c8219_6120 → 来源 src_0974f6cd66d2bc4ca55c8219；清洗后字符 [6207, 6406)

SHA-256：`5c2c49105b6ac9c095aedd95af5f2f3133be5bf6bb7d17561ab15184a704fb32`；范围：<main> element; characters 0-8971 of 8971

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.microsoft.com/en-us/copilot/pricing/copilot-studio
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_0f72de9009f4ebdeb9f3d047"></a>
### ev_0f72de9009f4ebdeb9f3d047

> The standalone Copilot Studio license offers additional flexibility—you can create agents using the GitHub Copilot harness and publish to external channels (like websites, apps, and social platforms), non-licensed users can use the agent, and you can choose from different pricing options.

来源：Microsoft Copilot Studio Plans and Pricing — https://www.microsoft.com/en-us/copilot/pricing/copilot-studio

类型：web；读取时间：2026-10-19T08:23:18.966505+00:00；截断：False

问题 q1 → 分块 chk_0974f6cd66d2bc4ca55c8219_6120 → 来源 src_0974f6cd66d2bc4ca55c8219；清洗后字符 [6407, 6696)

SHA-256：`5c2c49105b6ac9c095aedd95af5f2f3133be5bf6bb7d17561ab15184a704fb32`；范围：<main> element; characters 0-8971 of 8971

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.microsoft.com/en-us/copilot/pricing/copilot-studio
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_784627136f29e0b92110aa39"></a>
### ev_784627136f29e0b92110aa39

> To purchase, customers must have a qualifying Microsoft 365 plan for enterprise or business.

来源：Microsoft Copilot Studio Plans and Pricing — https://www.microsoft.com/en-us/copilot/pricing/copilot-studio

类型：web；读取时间：2026-10-19T08:23:18.966505+00:00；截断：False

问题 q1 → 分块 chk_0974f6cd66d2bc4ca55c8219_1020 → 来源 src_0974f6cd66d2bc4ca55c8219；清洗后字符 [1161, 1253)

SHA-256：`5c2c49105b6ac9c095aedd95af5f2f3133be5bf6bb7d17561ab15184a704fb32`；范围：<main> element; characters 0-8971 of 8971

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.microsoft.com/en-us/copilot/pricing/copilot-studio
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_8cba532208cb1ca2ecd4daaa"></a>
### ev_8cba532208cb1ca2ecd4daaa

> An Azure subscription is required to use agents.

来源：Microsoft Copilot Studio Plans and Pricing — https://www.microsoft.com/en-us/copilot/pricing/copilot-studio

类型：web；读取时间：2026-10-19T08:23:18.966505+00:00；截断：False

问题 q1 → 分块 chk_0974f6cd66d2bc4ca55c8219_1020 → 来源 src_0974f6cd66d2bc4ca55c8219；清洗后字符 [1567, 1615)

SHA-256：`5c2c49105b6ac9c095aedd95af5f2f3133be5bf6bb7d17561ab15184a704fb32`；范围：<main> element; characters 0-8971 of 8971

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.microsoft.com/en-us/copilot/pricing/copilot-studio
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_581bce47940f6aaa85d13f76"></a>
### ev_581bce47940f6aaa85d13f76

> Copilot Studio is priced per credit, pooled at the tenant level, not per seat.

来源：Microsoft Copilot Studio Pricing In 2026: Credits, Plans, And Costs — https://www.cloudzero.com/blog/copilot-studio-pricing/

类型：web；读取时间：2026-10-19T08:23:25.388083+00:00；截断：False

问题 q1 → 分块 chk_5de6a402648eeec2266bf20a_3570 → 来源 src_5de6a402648eeec2266bf20a；清洗后字符 [3913, 3991)

SHA-256：`cb19d183bd1edd7576e299f6598b444a3200c932fb28102ca2d84e1e3314d183`；范围：<main> element; characters 0-19388 of 19388

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.cloudzero.com/blog/copilot-studio-pricing
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_9036678dcdffcc0f616cb84f"></a>
### ev_9036678dcdffcc0f616cb84f

> M365 Copilot is the per-user AI assistant in Word, Excel, and Outlook ($18–$30/user/month). Copilot Studio is the platform for building custom agents.

来源：Microsoft Copilot Studio Pricing In 2026: Credits, Plans, And Costs — https://www.cloudzero.com/blog/copilot-studio-pricing/

类型：web；读取时间：2026-10-19T08:23:25.388083+00:00；截断：False

问题 q1 → 分块 chk_5de6a402648eeec2266bf20a_2550 → 来源 src_5de6a402648eeec2266bf20a；清洗后字符 [2838, 2988)

SHA-256：`cb19d183bd1edd7576e299f6598b444a3200c932fb28102ca2d84e1e3314d183`；范围：<main> element; characters 0-19388 of 19388

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.cloudzero.com/blog/copilot-studio-pricing
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_ebc24156510a771ef0b63cea"></a>
### ev_ebc24156510a771ef0b63cea

> This guide does not supersede, or replace any of the Microsoft Product Terms legal documentation covering use rights.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q1 → 分块 chk_c68aacefe8ad1e6fd48eeabb_2040 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [2500, 2617)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_5a440717841727e42686e122"></a>
### ev_5a440717841727e42686e122

> Microsoft 365 Copilot $30 per user/month Included agent usage1 Pay-as-you-go: unlimited2 License (capacity pack): 25,000 Copilot Credit /pack3 Pre

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q2 → 分块 chk_c68aacefe8ad1e6fd48eeabb_13260 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [13714, 13860)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_970f49f4b21e69e442f9aa9b"></a>
### ev_970f49f4b21e69e442f9aa9b

> Copilot Credits are the common currency across Copilot Studio capabilities and are available via the Microsoft Copilot Studio pay-as-you-go meter, the Microsoft Copilot Studio license (i.e., Copilot Credit capacity pack) and the

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q2 → 分块 chk_c68aacefe8ad1e6fd48eeabb_3571 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [3941, 4169)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_2b9e141ce0074ba49ee0902f"></a>
### ev_2b9e141ce0074ba49ee0902f

> • Pricing: $200 per credit pack/month (billed annually) • Copilot Credit Capacity: 1 capacity pack = 25,000 Copilot Credits

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf

类型：web；读取时间：2026-10-19T08:24:22.210421+00:00；截断：False

问题 q2 → 分块 chk_059af1d4b3d5bf109a6dbb14_27030 → 来源 src_059af1d4b3d5bf109a6dbb14；清洗后字符 [27310, 27433)

SHA-256：`ffd7d5a631e01bb670aef2bd8fa6ae234dcc34b5d3770ccd90bb71beba67c590`；范围：PDF pages 1-21 of 21; characters 0-38941 of 38941

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_67419540f72b4110f96c4ce1"></a>
### ev_67419540f72b4110f96c4ce1

> Capacity packs are offered through the Copilot Studio subscription license. Copilot Credit packs should be purchased for the anticipated number of Copilot Credits the tenant is expected to consume each month. Unused credits do not roll over to the next month.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf

类型：web；读取时间：2026-10-19T08:24:22.210421+00:00；截断：False

问题 q2 → 分块 chk_059af1d4b3d5bf109a6dbb14_27030 → 来源 src_059af1d4b3d5bf109a6dbb14；清洗后字符 [27050, 27309)

SHA-256：`ffd7d5a631e01bb670aef2bd8fa6ae234dcc34b5d3770ccd90bb71beba67c590`；范围：PDF pages 1-21 of 21; characters 0-38941 of 38941

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_376ddd08ecd4747fa61b4b19"></a>
### ev_376ddd08ecd4747fa61b4b19

> Copilot Credit consumption won’t be counted against the pay-as-you-go meter until credit packs have been exhausted.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf

类型：web；读取时间：2026-10-19T08:24:22.210421+00:00；截断：False

问题 q2 → 分块 chk_059af1d4b3d5bf109a6dbb14_27540 → 来源 src_059af1d4b3d5bf109a6dbb14；清洗后字符 [27630, 27745)

SHA-256：`ffd7d5a631e01bb670aef2bd8fa6ae234dcc34b5d3770ccd90bb71beba67c590`；范围：PDF pages 1-21 of 21; characters 0-38941 of 38941

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_215b99e850282a545db0bdc7"></a>
### ev_215b99e850282a545db0bdc7

> Pre-purchase plan Includes prepaid Copilot Credit Commit Units—ideal for organizations who want to choose their credit amount up front and manage variable month-to-month usage. Buy now An Azure subscription is required to use agents.

来源：Microsoft Copilot Studio Plans and Pricing — https://www.microsoft.com/en-us/copilot/pricing/copilot-studio

类型：web；读取时间：2026-10-19T08:23:18.966505+00:00；截断：False

问题 q2 → 分块 chk_0974f6cd66d2bc4ca55c8219_1020 → 来源 src_0974f6cd66d2bc4ca55c8219；清洗后字符 [1382, 1615)

SHA-256：`5c2c49105b6ac9c095aedd95af5f2f3133be5bf6bb7d17561ab15184a704fb32`；范围：<main> element; characters 0-8971 of 8971

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.microsoft.com/en-us/copilot/pricing/copilot-studio
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_4f771c92962baa3167c08336"></a>
### ev_4f771c92962baa3167c08336

> Each ACU is worth $1 of Copilot Credit or Microsoft Foundry usage which is equivalent to 100 Copilot Credits.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf

类型：web；读取时间：2026-10-19T08:24:22.210421+00:00；截断：False

问题 q2 → 分块 chk_059af1d4b3d5bf109a6dbb14_24990 → 来源 src_059af1d4b3d5bf109a6dbb14；清洗后字符 [25195, 25304)

SHA-256：`ffd7d5a631e01bb670aef2bd8fa6ae234dcc34b5d3770ccd90bb71beba67c590`；范围：PDF pages 1-21 of 21; characters 0-38941 of 38941

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_bf78bdec34d2ed9ab4d5364c"></a>
### ev_bf78bdec34d2ed9ab4d5364c

> Microsoft Agent P3 is a one-year pay-upfront option. Customers commit upfront to a pool of Agent Commit Units (ACUs) that can be used at any time during the

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf

类型：web；读取时间：2026-10-19T08:24:22.210421+00:00；截断：False

问题 q2 → 分块 chk_059af1d4b3d5bf109a6dbb14_24990 → 来源 src_059af1d4b3d5bf109a6dbb14；清洗后字符 [25433, 25589)

SHA-256：`ffd7d5a631e01bb670aef2bd8fa6ae234dcc34b5d3770ccd90bb71beba67c590`；范围：PDF pages 1-21 of 21; characters 0-38941 of 38941

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_3673df720bdda4517b7e7b6a"></a>
### ev_3673df720bdda4517b7e7b6a

> Usage is limited to fair usage limits. Microsoft reserves the right to update the limits as the product evolves, and new usage patterns emerge.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q3 → 分块 chk_c68aacefe8ad1e6fd48eeabb_15300 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [15594, 15737)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_3bb21aa99cb70fd8ce1df4b4"></a>
### ev_3bb21aa99cb70fd8ce1df4b4

> If your organization has M365 Copilot licenses, $18/user/month for Copilot Business (≤300 users, promotional through June 30, 2026, standard $21), or $30/user/month for Copilot Enterprise, internal agent interactions by licensed users don’t consume Copilot Credits.

来源：Microsoft Copilot Studio Pricing In 2026: Credits, Plans, And Costs — https://www.cloudzero.com/blog/copilot-studio-pricing/

类型：web；读取时间：2026-10-19T08:23:25.388083+00:00；截断：False

问题 q3 → 分块 chk_5de6a402648eeec2266bf20a_4590 → 来源 src_5de6a402648eeec2266bf20a；清洗后字符 [4738, 5003)

SHA-256：`cb19d183bd1edd7576e299f6598b444a3200c932fb28102ca2d84e1e3314d183`；范围：<main> element; characters 0-19388 of 19388

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.cloudzero.com/blog/copilot-studio-pricing
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_bacc10ee26fa727620089a9f"></a>
### ev_bacc10ee26fa727620089a9f

> Microsoft does not publish the exact threshold, and reserves the right to update it as patterns emerge.

来源：Copilot Studio Licensing | Explained by Licensing Expert — https://licenseq.com/copilot-studio-licensing/

类型：web；读取时间：2026-10-19T08:24:34.136568+00:00；截断：False

问题 q3 → 分块 chk_be03c5b67dd2b4fe8530e90d_5610 → 来源 src_be03c5b67dd2b4fe8530e90d；清洗后字符 [5953, 6056)

SHA-256：`56c234622dddeedd6d7055b85ceb6bdb7bd1df68db79be59a596ab47d1f8fc2d`；范围：<main> element; characters 0-17908 of 17908

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://licenseq.com/copilot-studio-licensing
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_0fb7ca088ee9900f8d02961b"></a>
### ev_0fb7ca088ee9900f8d02961b

> Used by Microsoft 365 Copilot licensed user 1 Classic answer 1 Copilot Credit No charge Generative answer 2 2 Copilot Credits No charge Agent action 4 5 Copilot Credits No charge Tenant graph grounding for messages 10 Copilot Credits No charge Agent flow actions per 100 actions 3 13 Copilot Credits No charge

来源：Billing rates and management - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management

类型：web；读取时间：2026-10-19T08:24:38.367732+00:00；截断：False

问题 q3 → 分块 chk_cb2f65e1f11911dfeee83b3a_1530 → 来源 src_cb2f65e1f11911dfeee83b3a；清洗后字符 [1809, 2118)

SHA-256：`2973a95947631532732204896e8fa6d6e64c656ad43eec6c4e3aa86e72462e8a`；范围：<main> element; characters 0-15979 of 15979

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_e1c1dc70ef05d675491e7b64"></a>
### ev_e1c1dc70ef05d675491e7b64

> When prepaid capacity is exhausted, agent flow enforcement blocks new runs rather than disabling the agent.

来源：Billing rates and management - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management

类型：web；读取时间：2026-10-19T08:24:38.367732+00:00；截断：False

问题 q3 → 分块 chk_cb2f65e1f11911dfeee83b3a_3570 → 来源 src_cb2f65e1f11911dfeee83b3a；清洗后字符 [3874, 3981)

SHA-256：`2973a95947631532732204896e8fa6d6e64c656ad43eec6c4e3aa86e72462e8a`；范围：<main> element; characters 0-15979 of 15979

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_a0c0976f0b0bb47f0454ecc7"></a>
### ev_a0c0976f0b0bb47f0454ecc7

> “InsufficientMcsCredits - The environment does not have sufficient Copilot Credits to run workflows.”

来源：Power Platform Community Forum Thread Details — https://community.powerplatform.com/forums/thread/details/?threadid=bc7d0d19-4921-f111-8342-7ced8dcf6527

类型：web；读取时间：2026-10-19T08:24:49.983894+00:00；截断：False

问题 q3 → 分块 chk_1a66581da9f76a510025eaf3_3570 → 来源 src_1a66581da9f76a510025eaf3；清洗后字符 [3688, 3789)

SHA-256：`f7337cddce4c9ebdb5b2eab78399442aedc3bec6ad4f72b526beb15faa6b880d`；范围：<body> element; characters 0-6584 of 6584

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://community.powerplatform.com/forums/thread/details?threadid=bc7d0d19-4921-f111-8342-7ced8dcf6527
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_4edded454f4abbb7c0a87db6"></a>
### ev_4edded454f4abbb7c0a87db6

> Usage is limited to fair usage limits. Microsoft reserves the right to update the limit

来源：Article - Copilot Agents, Developer T... — https://services.northwestern.edu/TDClient/30/Portal/KB/Article/2879/Copilot-Agents-Developer-Tools-Sharing-Publishing-and-Message-Consumption

类型：web；读取时间：2026-10-19T08:25:23.206842+00:00；截断：False

问题 q3 → 分块 chk_7e9a2016729ec629a6069173_12240 → 来源 src_7e9a2016729ec629a6069173；清洗后字符 [12753, 12840)

SHA-256：`5e7f77f4b6eb7ba1580d3e124bf34f9731f751d8e737a903c4455cdc5db94043`；范围：<main> element; characters 0-14774 of 14774

获取链：运行 d968652bc210 → 问题 q3 → 搜索 search3 → https://services.northwestern.edu/TDClient/30/Portal/KB/Article/2879/Copilot-Agents-Developer-Tools-Sharing-Publishing-and-Message-Consumption
检索词：Microsoft Product Terms Copilot Studio included agent usage；当时的问题：微软官方 Product Terms 或完整许可条款中，Microsoft 365 Copilot 每席位“Included agent usage”对应的具体 Copilot Credit 数量是多少，公平使用限制（fair usage limit）如何定义、触发后有何后果？

<a id="ev_0b38cd8a1f64f34d14c759b0"></a>
### ev_0b38cd8a1f64f34d14c759b0

> udio agents and the Microsoft Copilot Studio tools/features invoked by the said agents, are included in the Microsoft 365 Copilot USL when the user of the agent is licensed with Microsoft 365 Copilot and the agent is operating using the authenticated Microsoft 365 Copilot USL user’s identity. Usage is limited to fair usage limits. Microsoft reserves the right to update the limits as the product evolves, and new usage patterns emerge.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q4 → 分块 chk_c68aacefe8ad1e6fd48eeabb_15300 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [15300, 15737)

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

<a id="ev_9d0e356064e2f7be07f5f91f"></a>
### ev_9d0e356064e2f7be07f5f91f

> to fair usage limits. Microsoft reserves the right to update the limits as the product evolves, and new usage patterns emerge.

来源：Billing rates and management - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management

类型：web；读取时间：2026-10-19T08:24:38.367732+00:00；截断：False

问题 q4 → 分块 chk_cb2f65e1f11911dfeee83b3a_3570 → 来源 src_cb2f65e1f11911dfeee83b3a；清洗后字符 [3570, 3696)

SHA-256：`2973a95947631532732204896e8fa6d6e64c656ad43eec6c4e3aa86e72462e8a`；范围：<main> element; characters 0-15979 of 15979

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_966168a934515567ca58763e"></a>
### ev_966168a934515567ca58763e

> If your users hold the Microsoft 365 Copilot User SL ($30/user/month), they already have Copilot Studio use rights for employee-facing agents , Teams, SharePoint, M365 Copilot, at no extra charge. Agents built for those surfaces, operating under the licensed user’s identity, are covered. The catch is “fair usage”. Microsoft does not publish the exact threshold, and reserves the right to update it as patterns emerge.

来源：Copilot Studio Licensing | Explained by Licensing Expert — https://licenseq.com/copilot-studio-licensing/

类型：web；读取时间：2026-10-19T08:24:34.136568+00:00；截断：False

问题 q4 → 分块 chk_be03c5b67dd2b4fe8530e90d_5610 → 来源 src_be03c5b67dd2b4fe8530e90d；清洗后字符 [5637, 6056)

SHA-256：`56c234622dddeedd6d7055b85ceb6bdb7bd1df68db79be59a596ab47d1f8fc2d`；范围：<main> element; characters 0-17908 of 17908

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://licenseq.com/copilot-studio-licensing
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_fc03800a5261a44f1b5d5862"></a>
### ev_fc03800a5261a44f1b5d5862

> “Fair use” is unenforceable as a customer. Employee-facing Copilot Studio usage covered by the Microsoft 365 Copilot User SL is gated by a fair-use limit Microsoft does not publish and explicitly reserves the right to update.

来源：Copilot Studio Licensing | Explained by Licensing Expert — https://licenseq.com/copilot-studio-licensing/

类型：web；读取时间：2026-10-19T08:24:34.136568+00:00；截断：False

问题 q4 → 分块 chk_be03c5b67dd2b4fe8530e90d_9690 → 来源 src_be03c5b67dd2b4fe8530e90d；清洗后字符 [9770, 9995)

SHA-256：`56c234622dddeedd6d7055b85ceb6bdb7bd1df68db79be59a596ab47d1f8fc2d`；范围：<main> element; characters 0-17908 of 17908

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://licenseq.com/copilot-studio-licensing
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_37e72d770ba645c4780f3faf"></a>
### ev_37e72d770ba645c4780f3faf

> If your organization has M365 Copilot licenses, $18/user/month for Copilot Business (≤300 users, promotional through June 30, 2026, standard $21), or $30/user/month for Copilot Enterprise, internal agent interactions by licensed users don’t consume Copilot Credits. Classic answers, generative answers, grounding, agent actions, agent flows, all included within Teams, SharePoint, and Copilot Chat, subject to fair usage limits.

来源：Microsoft Copilot Studio Pricing In 2026: Credits, Plans, And Costs — https://www.cloudzero.com/blog/copilot-studio-pricing/

类型：web；读取时间：2026-10-19T08:23:25.388083+00:00；截断：False

问题 q4 → 分块 chk_5de6a402648eeec2266bf20a_4590 → 来源 src_5de6a402648eeec2266bf20a；清洗后字符 [4738, 5166)

SHA-256：`cb19d183bd1edd7576e299f6598b444a3200c932fb28102ca2d84e1e3314d183`；范围：<main> element; characters 0-19388 of 19388

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.cloudzero.com/blog/copilot-studio-pricing
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_bcff011e04cd21c7cb00be57"></a>
### ev_bcff011e04cd21c7cb00be57

> For the Microsoft 365 Copilot SKU: Microsoft 365 E5, E3, F1 and F3; Business Basic, Standard and Premium; Apps for business and for enterprise; Office 365 E1, E3, E5 and F3; Teams Essentials, Enterprise and EEA; Exchange Kiosk and Plans 1 and 2; S

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q5 → 分块 chk_ba995cac346030f043dc84c6_510 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [863, 1110)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_166813518580a59f6256b9bd"></a>
### ev_166813518580a59f6256b9bd

> The smaller SKU, Microsoft 365 Copilot Business, attaches only to Microsoft 365 Business Basic, Business Standard, Business Premium and Apps for business, and Microsoft's catalog description caps it at 300 seats, the same ceiling as the Business plans, which our 300-license limit guide explains.

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q5 → 分块 chk_ba995cac346030f043dc84c6_1020 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [1274, 1570)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_e19c2cf61ba4879c180642ba"></a>
### ev_e19c2cf61ba4879c180642ba

> Prerequisites include Microsoft 365 E3, E5, Business Standard, or Business Premium.

来源：Microsoft Copilot vs Copilot Studio + Cowork: Key Differences (2026) — https://www.hso.com/blog/microsoft-copilot-vs-studio/

类型：web；读取时间：2026-10-19T08:22:57.302469+00:00；截断：False

问题 q5 → 分块 chk_1f444fdde6bc33ac0db439f8_6630 → 来源 src_1f444fdde6bc33ac0db439f8；清洗后字符 [6987, 7070)

SHA-256：`65de4d548f8e19533fd7392baf56d4b9982c6993445097ad37bed59c7e536b92`；范围：<main> element; characters 0-20914 of 20914

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.hso.com/blog/microsoft-copilot-vs-studio
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_8b455cd49b12e635d47daf94"></a>
### ev_8b455cd49b12e635d47daf94

> Eligible base licenses include: - M365 Apps for enterprise or M365 Apps for business - M365 Business Basic, Business Standard or Busi

来源：M365 Copilot requirements explained! | Microsoft Community Hub — https://techcommunity.microsoft.com/discussions/microsoft-copilot/m365-copilot-requirements-explained/4400231

类型：web；读取时间：2026-10-19T08:26:38.756547+00:00；截断：False

问题 q5 → 分块 chk_33f6756b411fd62861cb8c0b_1530 → 来源 src_33f6756b411fd62861cb8c0b；清洗后字符 [1997, 2130)

SHA-256：`9bfedd403479c15040ba5d3ddbff161fdd3c62976c1d65b2e10e1cdb54532666`；范围：<main> element; characters 0-5498 of 5498

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://techcommunity.microsoft.com/discussions/microsoft-copilot/m365-copilot-requirements-explained/4400231
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_5d2c5aaa93a0fff55de25039"></a>
### ev_5d2c5aaa93a0fff55de25039

> Microsoft 365 Copilot is sold three ways in 2026: a per-user add-on on top of a qualifying plan, a metered pay-as-you-go option for people without a seat, and Copilot Studio capacity for the agents you build yourself.

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q5 → 分块 chk_ba995cac346030f043dc84c6_0 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [325, 542)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_e3dbe5cb2ef0d4c42f067d30"></a>
### ev_e3dbe5cb2ef0d4c42f067d30

> §PDF page 7§ Microsoft Copilot Studio Licensing Guide | November 2025 P a g e | 7 Copilot Credit Pre-Purchase Plan Value Conversion Tier Copilot Credits Commit Units (CCCU) # of Copilot Credit (1 CCCU = 100 Copilot Credit) # of monthly MCS licenses (Copilot Credit capacity pack) 1 3,000 300,000 1 pack * 12 months 2 15,000 1,500,000 5 packs * 12 months 3 30,000 3,000,000 10 packs * 12 months 4 150,000 15,000,000 50 packs * 12 months 5 300,000 30,000,000 100 packs * 12 months 6 750,000 75,000,000 250 packs * 12 months 7 1,500,000 150,00,000 500 packs * 12 mon

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q6 → 分块 chk_c68aacefe8ad1e6fd48eeabb_11220 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [11257, 11820)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_24adff377fb8485a1bfa0dbc"></a>
### ev_24adff377fb8485a1bfa0dbc

> Enterprise : $30/user/month Annual Includes Copilot Studio. Internal agent interactions by licensed users don’t consume Copilot Credits (classic answers, generative answers, grounding, agent actions) Microsoft Copilot Studio Capacity Packs $200/month Monthly Includes 25,000 credits/month Microsoft Copilot Credit Commit Units (CCCU) Custom Annual Buy credits upfront via Microsoft Azure, up to 20% off, auto PAYG overflow Microsoft Pay-as-you-go $0.01/credit Usage-based Billed thro

来源：Microsoft Copilot Studio Pricing In 2026: Credits, Plans, And Costs — https://www.cloudzero.com/blog/copilot-studio-pricing/

类型：web；读取时间：2026-10-19T08:23:25.388083+00:00；截断：False

问题 q6 → 分块 chk_5de6a402648eeec2266bf20a_4080 → 来源 src_5de6a402648eeec2266bf20a；清洗后字符 [4197, 4680)

SHA-256：`cb19d183bd1edd7576e299f6598b444a3200c932fb28102ca2d84e1e3314d183`；范围：<main> element; characters 0-19388 of 19388

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.cloudzero.com/blog/copilot-studio-pricing
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_4ce22fcf3c92e85663a7ba67"></a>
### ev_4ce22fcf3c92e85663a7ba67

> Pay-as-you-go meters agent use for people without a seat in Copilot Credits on your own Azure subscription; a budget alerts but does not cap. A Copilot Studio capacity pack is 25,000 prepaid credits a month for the tenant and needs pay-as-you-go a

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q6 → 分块 chk_ba995cac346030f043dc84c6_9690 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [10043, 10290)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_335bc048fbe1377968e559f7"></a>
### ev_335bc048fbe1377968e559f7

> What it covers Copilot in the apps, work-grounded Co

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q6 → 分块 chk_ba995cac346030f043dc84c6_8670 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [9218, 9270)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_b6d70feeea344928917b06c7"></a>
### ev_b6d70feeea344928917b06c7

> Always confirm the specifics for your licenses, since entitlements change over time.

来源：Microsoft Copilot Credits explained: usage, costs, and limits | Rand Group — https://www.randgroup.com/insights/copilot/microsoft-copilot-credits-explained-usage-costs-and-limits/

类型：web；读取时间：2026-10-19T08:27:38.972851+00:00；截断：False

问题 q6 → 分块 chk_b1cc9f91fec6eb8dd862d0b2_2550 → 来源 src_b1cc9f91fec6eb8dd862d0b2；清洗后字符 [2893, 2977)

SHA-256：`56fb7ca8ffd57867ccab60603a779f80f6057d2fc2bd06694f5f210eb5310818`；范围：<main> element; characters 0-18567 of 18567

获取链：运行 d968652bc210 → 问题 q6 → 搜索 search5 → https://www.randgroup.com/insights/copilot/microsoft-copilot-credits-explained-usage-costs-and-limits
检索词：Microsoft 365 Copilot revenue recognition credits；当时的问题：微软官方财报分部披露或正式定价/许可页面中，Microsoft 365 Copilot 的席位制收入与 Copilot Studio 的信用用量（容量包、按量付费、预购 Commit Units）收入分别如何对应收入确认口径，且 M365 Copilot 每席位包含的代理信用额度是否随时间调整？

<a id="ev_73ffcca19e7a86bab3fcd561"></a>
### ev_73ffcca19e7a86bab3fcd561

> Microsoft Copilot§ Microsoft 365 plans: Microsoft 365 E7 (includes Microsoft Copilot) Microsoft 365 E5 Microsoft 365 E3 Microsoft 365 F1 Microsoft 365 F3 Microsoft 365 Business Premium Microsoft 365 Business Standard Microsoft 365 Business Basic Microsoft 365 Apps for Enterprise Microsoft 365 Apps for Business Office 365 plans: Office 365 E5 Office 365 E3 Office 365 E1 Off

来源：License Options for Microsoft Copilot | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-licensing

类型：web；读取时间：2026-10-19T08:28:39.841081+00:00；截断：False

问题 q7 → 分块 chk_6cc784f8750c8103456cd299_2040 → 来源 src_6cc784f8750c8103456cd299；清洗后字符 [2265, 2640)

SHA-256：`c4df1e9e82f94278d2aaef4f5f7716b52d1663a7e5b5511f7aab0a53b9c11779`；范围：<main> element; characters 0-6984 of 6984

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-licensing
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_02fefeab293305ad1b8b615e"></a>
### ev_02fefeab293305ad1b8b615e

> Users need a Microsoft Copilot license and a qualifying prerequisite license. For the current list of eligible plans, see License options for Microsoft Copilot and the Microsoft Copilot service description .

来源：Microsoft Copilot requirements | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-copilot-requirements

类型：web；读取时间：2026-10-19T08:26:29.106930+00:00；截断：False

问题 q7 → 分块 chk_2e6ceef6446e768f7e59e4b4_2040 → 来源 src_2e6ceef6446e768f7e59e4b4；清洗后字符 [2341, 2548)

SHA-256：`5f04fc532ff5c1f4d2e19d0141f5c435f00829a4663fda2c23eafaa70e4fd79f`；范围：<main> element; characters 0-11457 of 11457

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-copilot-requirements
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_8c2da60f81aedf9a0ccbd367"></a>
### ev_8c2da60f81aedf9a0ccbd367

> Microsoft’s minimum requirements documentation lists the eligible base subscriptions: Enterprise : Microsoft 365 E3, E5, and F3, plus the Office 365 E1, E3, and E5 equivalents Business : Microsoft 365 Business Basic, Business Standard, and Business Premium Frontline and government : F-tier and GCC plans, with some capabil

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q7 → 分块 chk_0a86d3d8c098bd281864d073_3060 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [3337, 3660)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_844f483a559a99b3171b3658"></a>
### ev_844f483a559a99b3171b3658

> Microsoft 365 Copilot is an add-on license, and Microsoft's license-options article lists more qualifying plans than most people assume. For the Microsoft 365 Copilot SKU: Microsoft 365 E5, E3, F1 and F3; Business Basic, Standard and Premium; Apps for business and for enterprise; Office 365 E1, E3, E5 and F3; Teams Essentials, Enterprise and EEA; Exchange Kiosk and Plans 1 and 2; S

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q7 → 分块 chk_ba995cac346030f043dc84c6_510 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [726, 1110)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_0d1dd9c8ca4c0e2027af7e9c"></a>
### ev_0d1dd9c8ca4c0e2027af7e9c

> Government tenants get it as an add-on to Microsoft 365 G3, G5 and F1 and the Office 365 G and F plans; the academic offer attaches to A1, A3 and A5; our GCC and education pages carry those prices.

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q7 → 分块 chk_ba995cac346030f043dc84c6_1530 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [1571, 1768)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_73b717fd4ad93f190a3759ce"></a>
### ev_73b717fd4ad93f190a3759ce

> This plan is a one-year, prepaid option for Copilot Credits. A pool of Copilot Credit Commit Units (CCCUs) is usable across Microsoft eligible products. You can purchase this option in the Azure portal. You need to create a billing policy associated with your Azure subscription in Power Platform admin center.

来源：Standard harness licensing - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing

类型：web；读取时间：2026-10-19T08:25:26.800558+00:00；截断：False

问题 q8 → 分块 chk_0c9308874a087eda76e3ffa2_4080 → 来源 src_0c9308874a087eda76e3ffa2；清洗后字符 [4207, 4517)

SHA-256：`bd97d5a5eb6b73c5509af73942801a58576a809050ce94f139c18b173ae4f67d`；范围：<main> element; characters 0-7004 of 7004

获取链：运行 d968652bc210 → 问题 q3 → 搜索 search3 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/billing-licensing
检索词：Microsoft Product Terms Copilot Studio included agent usage；当时的问题：微软官方 Product Terms 或完整许可条款中，Microsoft 365 Copilot 每席位“Included agent usage”对应的具体 Copilot Credit 数量是多少，公平使用限制（fair usage limit）如何定义、触发后有何后果？

<a id="ev_10d4d85b6ed5d8ff7ec40d0b"></a>
### ev_10d4d85b6ed5d8ff7ec40d0b

> pack = 25,000 Copilot Credits For additional capacity, it is recommended to sign up for the pay-as-you-go meter to ensure business continuity. Copilot Credit consumption won’t be counted against the pay-as-you-go meter until credit pack capacity packs have been exhausted.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q8 → 分块 chk_c68aacefe8ad1e6fd48eeabb_9690 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [9690, 9962)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_d48c50e2b8428a177f0b6c47"></a>
### ev_d48c50e2b8428a177f0b6c47

> Capacity packs are offered through the Copilot Studio subscription license. Copilot Credit packs should be purchased for the anticipated number of Copilot Credits the tenant is expected to consume each month. Unused credits do not roll over to the next month. • Pricing: $200 per credit pack/month (billed annually) • Copilot Credit Capacity: 1 capacity pack = 25,000 Copilot Credits For additional capacity, it is recommended to sign up for the pay-as-you-go meter to ensure

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf

类型：web；读取时间：2026-10-19T08:24:22.210421+00:00；截断：False

问题 q8 → 分块 chk_059af1d4b3d5bf109a6dbb14_27030 → 来源 src_059af1d4b3d5bf109a6dbb14；清洗后字符 [27050, 27525)

SHA-256：`ffd7d5a631e01bb670aef2bd8fa6ae234dcc34b5d3770ccd90bb71beba67c590`；范围：PDF pages 1-21 of 21; characters 0-38941 of 38941

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_1414eaa69e594715ad449156"></a>
### ev_1414eaa69e594715ad449156

> a prepaid, tenant-wide block of 25,000 Copilot Credits per month, replenished each billing period and drawn first, with overage switching automatically to pay-as-you-go on the connected Azure subscription. Pay-as-you-go must be active before a pack can be used, and a Global Administrator allocates the credits to environments in the Power Platform admin center.

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q8 → 分块 chk_ba995cac346030f043dc84c6_5100 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [5129, 5491)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_282f584f443f4c65fe1002c8"></a>
### ev_282f584f443f4c65fe1002c8

> No; SharePoint agents need only pay-as-you-go billing and meter Copilot Credits on your Azure subscription. A capacity pack is optional prepaid capacity for the same credits.

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q8 → 分块 chk_ba995cac346030f043dc84c6_7650 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [7897, 8071)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_24a0e5a9ebd9f47c5a28d309"></a>
### ev_24a0e5a9ebd9f47c5a28d309

> A Microsoft Copilot Studio capacity pack is a prepaid subscription that provides credits for Copilot Chat and SharePoint agent usage. Each capacity pack provides a fixed number of Copilot Credits that you can use across your tenant. Copilot Credits are the unit of consumption in Microsoft Copilot Chat and SharePoint agents for AI interactions. Credits are available in quantities of 25,000 per month per pack.

来源：Use Capacity Packs vs Pay-as-you-go Billing for Microsoft Copilot Chat | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/copilot-capacity-packs

类型：web；读取时间：2026-10-19T08:29:42.860354+00:00；截断：False

问题 q8 → 分块 chk_40c65badfe4b5f9302da4ec9_510 → 来源 src_40c65badfe4b5f9302da4ec9；清洗后字符 [617, 1028)

SHA-256：`e4cc25355e7cccc38e74ff20c800b4270dbe55c50eb9ac47897ea1a603e60a13`；范围：<main> element; characters 0-18860 of 18860

获取链：运行 d968652bc210 → 问题 q8 → 搜索 search7 → https://learn.microsoft.com/en-us/microsoft-365/copilot/pay-as-you-go/copilot-capacity-packs
检索词：Copilot Studio capacity pack Azure subscription requirement；当时的问题：微软官方文档是否明确 Copilot Studio 容量包（Copilot Credit 容量包，每包 25,000 信用）与预购 Commit Units 路径在使用代理时同样需要 Azure 订阅，而不仅是按量付费计量需要？

<a id="ev_14bb53ae5f936972c855ce26"></a>
### ev_14bb53ae5f936972c855ce26

> udio agents and the Microsoft Copilot Studio tools/features invoked by the said agents, are included in the Microsoft 365 Copilot USL when the user of the agent is licensed with Microsoft 365 Copilot and the agent is operating using the authenticated Microsoft 365 Copilot USL user’s identity.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q9 → 分块 chk_c68aacefe8ad1e6fd48eeabb_15300 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [15300, 15593)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_7cc5b878584f771eb4b892f7"></a>
### ev_7cc5b878584f771eb4b892f7

> icrosoft 365 Copilot licence. However, when the agent tries to execute the agent flow, I receive the following error: “InsufficientMcsCredits - The environment does not have sufficient Copilot Credits to run workflows.” Based on your explanation, my understanding was that this type of interactive, user-initiated flow/action should be covered by the Microsoft 365 Copilot licence and should not require separate Copilot Credits, provided it falls within fair usage. Could you please confirm whether this has changed in the new experience, or whether there is a specific configuration required for ag

来源：Power Platform Community Forum Thread Details — https://community.powerplatform.com/forums/thread/details/?threadid=bc7d0d19-4921-f111-8342-7ced8dcf6527

类型：web；读取时间：2026-10-19T08:24:49.983894+00:00；截断：False

问题 q9 → 分块 chk_1a66581da9f76a510025eaf3_3570 → 来源 src_1a66581da9f76a510025eaf3；清洗后字符 [3570, 4170)

SHA-256：`f7337cddce4c9ebdb5b2eab78399442aedc3bec6ad4f72b526beb15faa6b880d`；范围：<body> element; characters 0-6584 of 6584

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://community.powerplatform.com/forums/thread/details?threadid=bc7d0d19-4921-f111-8342-7ced8dcf6527
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_99ae51757ddf9d7f42ff49bd"></a>
### ev_99ae51757ddf9d7f42ff49bd

> these are simple agents operating within the Fair Use limits described by @Nivedipa-MSFT .

来源：Power Platform Community Forum Thread Details — https://community.powerplatform.com/forums/thread/details/?threadid=bc7d0d19-4921-f111-8342-7ced8dcf6527

类型：web；读取时间：2026-10-19T08:24:49.983894+00:00；截断：False

问题 q9 → 分块 chk_1a66581da9f76a510025eaf3_4591 → 来源 src_1a66581da9f76a510025eaf3；清洗后字符 [4591, 4681)

SHA-256：`f7337cddce4c9ebdb5b2eab78399442aedc3bec6ad4f72b526beb15faa6b880d`；范围：<body> element; characters 0-6584 of 6584

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://community.powerplatform.com/forums/thread/details?threadid=bc7d0d19-4921-f111-8342-7ced8dcf6527
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_1a78c3e6f0177c1c93127970"></a>
### ev_1a78c3e6f0177c1c93127970

> Microsoft allows some level of overage consumption, similar to a grace period, to avoid blocking business processes.

来源：Billing rates and management - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management

类型：web；读取时间：2026-10-19T08:24:38.367732+00:00；截断：False

问题 q10 → 分块 chk_cb2f65e1f11911dfeee83b3a_9690 → 来源 src_cb2f65e1f11911dfeee83b3a；清洗后字符 [9702, 9818)

SHA-256：`2973a95947631532732204896e8fa6d6e64c656ad43eec6c4e3aa86e72462e8a`；范围：<main> element; characters 0-15979 of 15979

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_fc583c4e5dba763afe0dbfeb"></a>
### ev_fc583c4e5dba763afe0dbfeb

> Microsoft reserves the right to update the limits as the product evolves, and new usage patterns emerge.

来源：Billing rates and management - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management

类型：web；读取时间：2026-10-19T08:24:38.367732+00:00；截断：False

问题 q10 → 分块 chk_cb2f65e1f11911dfeee83b3a_3570 → 来源 src_cb2f65e1f11911dfeee83b3a；清洗后字符 [3592, 3696)

SHA-256：`2973a95947631532732204896e8fa6d6e64c656ad43eec6c4e3aa86e72462e8a`；范围：<main> element; characters 0-15979 of 15979

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-messages-management
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_16b8d1419a040a935a7f0b36"></a>
### ev_16b8d1419a040a935a7f0b36

> Requests may be rate-limited or rejected to protect service reliability and ensure fair usage.

来源：CoPilot usage limits - Microsoft Q&A — https://learn.microsoft.com/en-us/answers/questions/5902244/copilot-usage-limits

类型：web；读取时间：2026-10-19T08:30:56.956796+00:00；截断：False

问题 q10 → 分块 chk_986ebc3379bd3b4d6381913a_6631 → 来源 src_986ebc3379bd3b4d6381913a；清洗后字符 [6806, 6900)

SHA-256：`05b2e1b08dfbf933e7ade7133a3d2798f2c22028d8c68f598b7c2f79366951bb`；范围：<main> element; characters 0-8596 of 8596

获取链：运行 d968652bc210 → 问题 q10 → 搜索 search8 → https://learn.microsoft.com/en-us/answers/questions/5902244/copilot-usage-limits
检索词：Microsoft Product Terms Copilot Studio fair usage limit；当时的问题：微软是否有官方文件（Product Terms、服务说明或公平使用政策页）给出 fairness/fair usage limit 的判定口径与触发后的具体处置（限速、阻断运行或转独立计费），而非仅“存在限制、可更新”的表述？

<a id="ev_f7baf8ec2601b73fc7fe6904"></a>
### ev_f7baf8ec2601b73fc7fe6904

> There are fair usage controls (feature limits, credits, SCU capacity, and throttling), but not a simple published “X requests per hour” rule in the provided material.

来源：CoPilot usage limits - Microsoft Q&A — https://learn.microsoft.com/en-us/answers/questions/5902244/copilot-usage-limits

类型：web；读取时间：2026-10-19T08:30:56.956796+00:00；截断：False

问题 q10 → 分块 chk_986ebc3379bd3b4d6381913a_7140 → 来源 src_986ebc3379bd3b4d6381913a；清洗后字符 [7421, 7587)

SHA-256：`05b2e1b08dfbf933e7ade7133a3d2798f2c22028d8c68f598b7c2f79366951bb`；范围：<main> element; characters 0-8596 of 8596

获取链：运行 d968652bc210 → 问题 q10 → 搜索 search8 → https://learn.microsoft.com/en-us/answers/questions/5902244/copilot-usage-limits
检索词：Microsoft Product Terms Copilot Studio fair usage limit；当时的问题：微软是否有官方文件（Product Terms、服务说明或公平使用政策页）给出 fairness/fair usage limit 的判定口径与触发后的具体处置（限速、阻断运行或转独立计费），而非仅“存在限制、可更新”的表述？

<a id="ev_a8a94e42dedbddf77d590df8"></a>
### ev_a8a94e42dedbddf77d590df8

> Employee-facing Copilot Studio usage covered by the Microsoft 365 Copilot User SL is gated by a fair-use limit Microsoft does not publish and explicitly reserves the right to update.

来源：Copilot Studio Licensing | Explained by Licensing Expert — https://licenseq.com/copilot-studio-licensing/

类型：web；读取时间：2026-10-19T08:24:34.136568+00:00；截断：False

问题 q10 → 分块 chk_be03c5b67dd2b4fe8530e90d_9690 → 来源 src_be03c5b67dd2b4fe8530e90d；清洗后字符 [9813, 9995)

SHA-256：`56c234622dddeedd6d7055b85ceb6bdb7bd1df68db79be59a596ab47d1f8fc2d`；范围：<main> element; characters 0-17908 of 17908

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://licenseq.com/copilot-studio-licensing
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_b7fe757cbefa407e70afb64a"></a>
### ev_b7fe757cbefa407e70afb64a

> The issue is not that a limit exists. The issue is that users are being asked to manage a resource that they are not allowed to measure.

来源：CoPilot usage limits - Microsoft Q&A — https://learn.microsoft.com/en-us/answers/questions/5902244/copilot-usage-limits

类型：web；读取时间：2026-10-19T08:30:56.956796+00:00；截断：False

问题 q10 → 分块 chk_986ebc3379bd3b4d6381913a_4590 → 来源 src_986ebc3379bd3b4d6381913a；清洗后字符 [5005, 5141)

SHA-256：`05b2e1b08dfbf933e7ade7133a3d2798f2c22028d8c68f598b7c2f79366951bb`；范围：<main> element; characters 0-8596 of 8596

获取链：运行 d968652bc210 → 问题 q10 → 搜索 search8 → https://learn.microsoft.com/en-us/answers/questions/5902244/copilot-usage-limits
检索词：Microsoft Product Terms Copilot Studio fair usage limit；当时的问题：微软是否有官方文件（Product Terms、服务说明或公平使用政策页）给出 fairness/fair usage limit 的判定口径与触发后的具体处置（限速、阻断运行或转独立计费），而非仅“存在限制、可更新”的表述？

完整来源文本、分块、引用和哈希见同目录 state.json；节点、调用及排序分数见 trace.jsonl。
