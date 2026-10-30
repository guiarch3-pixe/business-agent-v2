# Microsoft｜企业研究

研究问题：Microsoft 365 Copilot 与 Copilot Studio 面向的企业使用者、收费单位和购买前提有何区别？这些差异可能如何影响企业客户扩展使用和微软的收入来源？优先使用官方资料；将价格与许可事实、基于事实的推导、商业判断和仍待验证假设明确区分，不把产品定价直接当成已实现收入或利润。

模式：live；停止原因：error；研究轮次：7

引用关系与摘录位置已做代码校验；语义支持关系、事实分类和缺口关闭是模型判断，未经独立事实核实。

## 事实（来源陈述）

- **c1_1** [supported] 据第三方许可指南，企业在购买 Copilot 前必须先持有符合条件的商业版或企业版基础许可，Copilot 并非可脱离基础订阅单独购买的产品。 [ev_f87733083f65c2d852ecf82d](#ev_f87733083f65c2d852ecf82d)（supports） [ev_1ebea556d7a9f2df48d924e8](#ev_1ebea556d7a9f2df48d924e8)（supports）
  依据/推导：第三方指南 IntuitionLabs 明确陈述购买 Copilot 需先持有符合条件的基础许可；该来源为第三方内容，非微软正式条款，故仅为第三方转述事实，不能单独关闭要求官方文档的缺口。
- **c1_2** [supported] 据第三方许可指南，面向企业的 Copilot 以 E3、E5、Business Standard 和 Business Premium 等基础许可的附加项（add-on）形式提供。 [ev_8dc1a462bcbabea6372dd436](#ev_8dc1a462bcbabea6372dd436)（supports） [ev_f0c7197503136a03358245be](#ev_f0c7197503136a03358245be)（supports）
  依据/推导：LicenseQ 与 IntuitionLabs 均将 Copilot 描述为符合条件基础许可的附加项，与“需先持有基础许可”的前提一致；范围为商业/企业版许可。来源为第三方，非官方正式文档。
- **c1_3** [supported] 据第三方指南，Copilot 的付费方案按每用户每月订阅计费，通常按年计费，即为按用户（用户/席位）而非按用量或其他单位收费。 [ev_24a65cda850e7a8bee7b3595](#ev_24a65cda850e7a8bee7b3595)（supports）
  依据/推导：IntuitionLabs 明确说明所有付费 Copilot 方案均为 per-user, per-month 订阅；该表述支持“按用户/席位”计费，但来源为第三方，不构成官方定价条款。
- **c1_4** [supported] 第三方资料给出的 Microsoft 365 Copilot 标价为公司版每用户每月 30 美元（年付），另有针对 300 用户以下商业租户的每月每用户 21 美元层级（自 2025 年 12 月 1 日起）。 [ev_965dd9a179fc418fa7860d03](#ev_965dd9a179fc418fa7860d03)（supports） [ev_f0c7197503136a03358245be](#ev_f0c7197503136a03358245be)（supports）
  依据/推导：两份第三方指南分别陈述 30 美元与 21 美元的每用户每月标价；此为“标价”事实，不能等同于已实现收入或利润。来源非官方正式定价页，数字需以官方页面核验。
- **c1_5** [supported] 微软官方域名下的 Q&A 用户回帖称 Microsoft 365 Copilot 每用户每月 30 美元，且购买通过需商业执行人员支持的 Lead Status，最小购买规模为 300 席位。 [ev_ffd11ecc2bb84864914d2f1f](#ev_ffd11ecc2bb84864914d2f1f)（supports）
  依据/推导：该内容托管于 learn.microsoft.com 的 Q&A（vendor_community），作者为社区回帖而非微软正式产品/许可文档；其“最小 300 席位”表述与第三方资料中面向小型租户的 21 美元层级存在潜在张力，需官方条款核验，不能视为正式购买门槛。
- **c2_1** [supported] 据 Microsoft Learn 的 Copilot Studio 许可文章，创建和管理代理（即使用 Copilot Studio 进行构建的用户）需要为每个用户购买一个许可，即按用户许可（在 Microsoft 365 管理中心内称为 Copilot Studio User License），并将其分配给单个用户。 [ev_c557f4700e8401b9b8aa89c4](#ev_c557f4700e8401b9b8aa89c4)（supports） [ev_5174ece39a89a0b98f010f9c](#ev_5174ece39a89a0b98f010f9c)（supports）
  依据/推导：原文直接陈述“To create and manage agents with Copilot Studio, you need: A license for each user…per user license”，并在获取步骤中要求选择“Copilot Studio User License”的数量；来源为 vendor_official 的 Microsoft Learn 文章，但该文本身指向《Microsoft Copilot Studio Licensing Guide》作为最完整的许可与计费信息，具体计价单位（消息/容量包）仍需以该指南核验。
- **c2_2** [supported] 据同一篇 Microsoft Learn 文章，组织还需由租户管理员获取一个组织级（租户）许可，且该许可不能分配给单个用户；通过 Microsoft 365 管理中心购买 Copilot Studio 许可后，再购买用户许可为用户开通访问。 [ev_5d2ddf74caa4a658bc155dac](#ev_5d2ddf74caa4a658bc155dac)（supports） [ev_0ee9f3c33cf2fceb119fb539](#ev_0ee9f3c33cf2fceb119fb539)（supports）
  依据/推导：原文区分“tenant license（由租户管理员获取，不能分配给个人）”与“user license”，并说明先购租户许可再购用户许可的流程；这支持 Copilot Studio 存在租户级前提加按用户许可的两层结构，但未说明具体计价（容量/消息包）金额。
- **c2_3** [supported] 据同一篇 Microsoft Learn 文章，使用已发布代理的终端用户不需要特殊许可，任何能访问已发布代理的人都可以与之交互；但租户外部的来宾用户无法访问 Copilot Studio。 [ev_595c2120b9d4c011d7f54407](#ev_595c2120b9d4c011d7f54407)（supports） [ev_f5a66e8106f6e7dbd07f7d8f](#ev_f5a66e8106f6e7dbd07f7d8f)（supports）
  依据/推导：原文明确区分“构建/管理代理者需按用户许可”与“使用代理者无需许可”；并可推出 Copilot Studio 的收费对象是构建者席位数而非代理交互人数，但代理运行本身按消耗计费的部分未在本段证据中出现。
- **c2_4** [supported] 据该 Microsoft Learn 文章，本文面向租户管理员；如需以个人身份注册 Copilot Studio 应参阅“Get access to Copilot Studio”，且文中提示最完整最新的许可与计费信息应参考《Microsoft Copilot Studio Licensing Guide》。 [ev_69a443d625c4905e973b6941](#ev_69a443d625c4905e973b6941)（supports）
  依据/推导：原文直接陈述目标读者与指向官方许可指南的指引；这表明本轮摘录未包含官方许可指南正文，即消息/容量包等计费单位细节仍待核验，故不能据此关闭 gap2。
- **c2_6** [supported] 据第三方许可指南，企业购买 Copilot 前必须先持有符合条件的商业版或企业版基础许可，Copilot 不能脱离基础订阅单独购买。 [ev_f87733083f65c2d852ecf82d](#ev_f87733083f65c2d852ecf82d)（supports） [ev_1ebea556d7a9f2df48d924e8](#ev_1ebea556d7a9f2df48d924e8)（supports）
  依据/推导：第三方 IntuitionLabs 明确陈述基础许可前提；来源为 third_party，且该文语境为 Microsoft 365 Copilot 附加项，不能直接套用为 Copilot Studio 的购买前提，也不能作为厂商正式条款。
- **c3_1** [supported] 据微软《Microsoft Copilot Studio Licensing Guide》（2025 年 11 月版），用户与 Copilot Studio 代理交互或代理代表用户执行任务时会消耗 Copilot Credits，Copilot Credits 是贯穿 Copilot Studio 各项能力的统一计价货币。 [ev_3191e0b91c06073417a97734](#ev_3191e0b91c06073417a97734)（supports） [ev_970f49f4b21e69e442f9aa9b](#ev_970f49f4b21e69e442f9aa9b)（supports）
  依据/推导：原文直接陈述按交互/任务消耗 Copilot Credits，并称其为 common currency；来源为供应方官方 PDF，属于正式许可文档，不是二手转述。
- **c3_2** [supported] 据该指南，Copilot Credits 可通过三种方式获取：Copilot Studio 按用付费计量（pay-as-you-go meter，按实际消耗后付费）、Copilot Studio 许可（即 Copilot Credit 容量包）以及 Copilot Credit 预付费计划（Pre-Purchase Plan）。 [ev_970f49f4b21e69e442f9aa9b](#ev_970f49f4b21e69e442f9aa9b)（supports） [ev_3191e0b91c06073417a97734](#ev_3191e0b91c06073417a97734)（supports）
  依据/推导：原文列举三种获取途径，并说明 pay-as-you-go 为 postpay；这直接回答计价单位问题中的“消息/容量包”部分，即单位是 Copilot Credit 及其容量包，而非 Copilot Studio 自身的按人订阅。
- **c3_3** [supported] 据该指南的对比表，Microsoft 365 Copilot 为每用户每月 30 美元，包含代理使用（含一定额度），并可通过按用付费（无上限）或 Copilot Studio 许可（容量包）按每包 25,000 Copilot Credits 扩展。 [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports）
  依据/推导：原文为表格行数据；仅支持“标价/包含额度”的许可事实，不能推出已实现收入或利润。表述主语为 Microsoft 365 Copilot，非 Copilot Studio 自身定价。
- **c3_4** [supported] 据该指南，Copilot Credit 预付费计划中每个 CCCU（Copilot Credit 承诺单位）价值 1 美元并可折算为 100 Copilot Credits，价格按阶梯折扣：3,000 Credits 为 2,850 美元（5% 折扣）至 3,000,000 Credits 为 2,400,000 美元（20% 折扣）。 [ev_94c3c9036b71c0917ffec552](#ev_94c3c9036b71c0917ffec552)（supports） [ev_19abf275bb24f872ac03af6f](#ev_19abf275bb24f872ac03af6f)（supports）
  依据/推导：原文直接给出换算率与九档阶梯价格表；此为官方标注的预付费价格，属“标价”事实，不等于实际销售金额或收入。
- **c3_5** [supported] 据该指南附录 B，Copilot Studio 内的 AI Tools 能力需要 Copilot Studio 容量，而该容量通过 Copilot Credits 授权。 [ev_bc21f8a13e28b99d53e3f1ff](#ev_bc21f8a13e28b99d53e3f1ff)（supports）
  依据/推导：原文直接陈述 AI Tools 能力依赖以 Copilot Credits 授权的容量，进一步支持 Copilot Credits 为 Copilot Studio 运行侧计价单位。
- **c4_1** [supported] 在微软官方域名 learn.microsoft.com 的 Microsoft Q&A 中，一条社区回帖（非微软正式产品或许可文档）称 Microsoft 365 Copilot 每用户每月 30 美元，通过需要商业执行人员支持的 Lead Status 购买，且最小购买规模为 300 席位。 [ev_ffd11ecc2bb84864914d2f1f](#ev_ffd11ecc2bb84864914d2f1f)（supports） [ev_6a4c3a159214691b845d80f9](#ev_6a4c3a159214691b845d80f9)（supports）
  依据/推导：原文摘录直接包含 30 美元/用户/月、Lead Status 与 300 席位最小购买量的表述，且自称引用“official source for the minimum requirement of 300 seats”。但该内容托管于官方域名的社区问答区，作者与性质为用户回帖（vendor_community），不能等同于厂商发布的正式定价或许可页面，故只能作为社区转述事实，不能关闭要求官方条款的 gap1。
- **c4_2** [supported] 同一 Q&A 回帖称 Microsoft 365 Copilot 不包含在 Microsoft 365 E3 许可中，而是附加服务（additional service）。 [ev_87c60951a53b2dcd25e37154](#ev_87c60951a53b2dcd25e37154)（supports）
  依据/推导：原文明确陈述“not included with Microsoft 365 (M365) E3 licenses; it is an additional s…”，主语为 Microsoft 365 Copilot，范围为 E3 许可之外的附加服务。该来源仍为 vendor_community 回帖，非正式条款；这一陈述也与“需符合条件的基础许可”的第三方说法方向一致，但不构成官方符合条件许可清单。
- **c4_3** [supported] 据第三方许可 wiki（LICENSEWARE Wiki），Microsoft 365 Copilot 以按用户附加项（per-user add-on，User SL）形式授权，必须叠加在所列的前提许可之上，与其他 Microsoft 365 在线服务使用同一订阅计量单位。 [ev_7167c90735860b7f2afb8b4a](#ev_7167c90735860b7f2afb8b4a)（supports） [ev_a6313e81bd7b26eb15a4808d](#ev_a6313e81bd7b26eb15a4808d)（supports）
  依据/推导：原文直接给出“per-user add-on”“must sit on top of a listed prerequisite license”“same subscription meter”。来源为第三方 wiki（third_party），不是微软正式文档，故支持“按用户/席位计费且需前提许可”的第三方转述事实，不能作为官方正式条款。
- **c4_4** [supported] 据该第三方 wiki，前提许可为一项所列的 Microsoft 365、Office 365 或独立服务许可，其依据为 Product Terms。 [ev_fb3a95aea3d25159bb5badb6](#ev_fb3a95aea3d25159bb5badb6)（supports）
  依据/推导：原文表头“Prerequisite”下列出该表述，仅概括类别（Microsoft 365、Office 365 或独立服务许可），未逐项列出具体符合条件的产品清单；且来源为第三方 wiki，标注 Product Terms 但未提供条款正文，不能据此确认正式符合条件许可清单。
- **c4_5** [supported] 据第三方许可指南 LicenseQ，Microsoft 365 Copilot 定价目前分为两档：自 2025 年 12 月 1 日起，面向最多 300 用户的 Business 计划租户提供 Copilot Business，每用户每月 21 美元；另有面向 E3、E5 及更大组织的标准 Microsoft 365 Copilot 附加项，每用户每月 30 美元。 [ev_ff6725a9c148a2b8fc30e268](#ev_ff6725a9c148a2b8fc30e268)（supports）
  依据/推导：原文直接陈述两档与各自价格、用户规模边界（up to 300 users）与生效时间。此为第三方指南（third_party）转述的“标价”事实，非微软官方定价页，不能作为官方标价确认，也绝不能等同于已实现收入或利润。
- **c4_6** [supported] 据第三方博客 GoSearch，Business 层级 300 席位或以下的客户在 2026 年 12 月 31 日前按每用户每月 18 美元付费，低于此前的 21 美元。 [ev_06ec321c1bc48bcb4d7043d8](#ev_06ec321c1bc48bcb4d7043d8)（supports）
  依据/推导：原文直接陈述 18 美元与 21 美元的对比及 300 席位边界、截止日期。来源为第三方博客（third_party），非官方定价页；该数字与 c4_5 的 21 美元在时间段上可能为不同时点的标价，存在需官方核验的张力，不能推出已实现收入。
- **c4_7** [supported] 据同一第三方博客，企业买家承诺 1,000 席位及以上可能自 2026 年 10 月起获得 30% 至 50% 折扣，来源为 The Information 的报道，且该博客称微软尚未在其官方定价页确认这些条款。 [ev_0084c3fbf2dbfaba904d5ebc](#ev_0084c3fbf2dbfaba904d5ebc)（supports）
  依据/推导：原文明确将折扣信息归于媒体报道并指出微软未在官方定价页确认；此为第三方转述的未确认折扣说法，非官方条款，不能作为标价或购买门槛事实。
- **c4_8** [supported] 据第三方许可指南 IntuitionLabs，Microsoft 365 Copilot（Enterprise/Business）标价为每年付 30 美元、按月计费 31.50 美元。 [ev_e16946e98cc6a4fd4790f9f2](#ev_e16946e98cc6a4fd4790f9f2)（supports）
  依据/推导：原文以价格表行形式给出年付与月付两种标价。来源为第三方（third_party），非官方定价页；此为标价事实，不能等同于收入或利润。
- **c4_9** [supported] 据该第三方指南，面向企业客户，Copilot 以附加订阅形式提供，典型价格为每用户每月 30 美元（年付计费），叠加在现有的 Microsoft 365 或 Office 365 许可之上（例如 Enterprise E3/E5 或 Business Standard/Premium 计划）。 [ev_25394e4d74c3b997dcacafe0](#ev_25394e4d74c3b997dcacafe0)（supports）
  依据/推导：原文直接陈述附加订阅性质、30 美元年付标价与基础许可示例（E3/E5、Business Standard/Premium）。来源为第三方，示例清单不能等同于微软官方“符合条件许可清单”，仅可作第三方列举。
- **c5_1** [supported] 据第三方许可 wiki（LICENSEWARE Wiki，非微软正式文档），Microsoft 365 Copilot 以按用户附加项（per-user add-on，User SL）形式授权，必须叠加在一项所列的前提许可之上，与其他 Microsoft 365 在线服务使用同一订阅计量单位。 [ev_7ace5d6faca5eabf1dd72cb4](#ev_7ace5d6faca5eabf1dd72cb4)（supports） [ev_7167c90735860b7f2afb8b4a](#ev_7167c90735860b7f2afb8b4a)（supports） [ev_a6313e81bd7b26eb15a4808d](#ev_a6313e81bd7b26eb15a4808d)（supports）
  依据/推导：原文逐字给出“licensed as a per-user add-on”“must sit on top of a listed prerequisite license”。来源为 third_party 二手 wiki，不能作为微软官方定价页或产品条款，仅支持“按用户/席位计费且需前提许可”的第三方转述事实。
- **c5_2** [supported] 据该第三方 wiki，前提许可仅被概括为“一项所列的 Microsoft 365、Office 365 或独立服务许可（Product Terms）”，摘录未逐项列出具体产品/SKU。 [ev_fb3a95aea3d25159bb5badb6](#ev_fb3a95aea3d25159bb5badb6)（supports）
  依据/推导：原文表头“Prerequisite”下仅有此概括表述；wiki 虽标注引用 Product Terms，但未提供条款正文，因此不能据此确认符合条件许可的具体 SKU 清单，该部分仍属缺口。
- **c5_3** [supported] 据该第三方 wiki 转述，企业定价卡载明“A separate license for a qualifying Microsoft 365 plan is required”，且 Product Terms 将 Copilot for Sales 与 Copilot for Service 列为独立的 User SL。 [ev_811e6c59a19b124192d36cca](#ev_811e6c59a19b124192d36cca)（supports）
  依据/推导：原文为二手转述并附引用编号；主语为 Microsoft 365 Copilot 及其 Sales/Service 变体，范围限于商业许可。属 third_party 转述，非官方条款正文。
- **c5_4** [supported] 据第三方许可博客（Licensing Lore & Law），Microsoft 365 Copilot Business 于 2026 年 6 月被加入 Product Terms，其 Business 许可上限为 300 用户，仅通过 CSP 提供，可购买的前提为已持有 Microsoft 365 Business Basic/Standard/Premium、Microsoft 365 Apps for Business 或 Teams Essentials 的用户。 [ev_50f29e435396a46a2cd45e44](#ev_50f29e435396a46a2cd45e44)（supports）
  依据/推导：原文直接陈述加入时间、300 用户上限、CSP 渠道与前提许可清单。来源为 third_party 博客对 Product Terms 更新的解读，非微软官方条款 PDF 正文；“前提许可清单”与“300 用户上限”在此语境下专指 Copilot Business 档，不能外推到 enterprise 档。
- **c5_5** [supported] 据第三方指南 IntuitionLabs，微软文档表述为购买 Copilot 需“a separate license for a qualifying Microsoft 365 plan is required”，该文并称符合条件的基础许可宽泛地包括任何商业版 Microsoft 365 或 Office 365 计划（business 或 enterprise 层级）。 [ev_dd8fd4d3a596744952d19cee](#ev_dd8fd4d3a596744952d19cee)（supports） [ev_1ebea556d7a9f2df48d924e8](#ev_1ebea556d7a9f2df48d924e8)（supports）
  依据/推导：原文含引号内表述与“Qualifying Plans”概括，但“任何商业版计划”属该第三方作者的概括，并非官方逐项 SKU 清单，不能据此裁定具体 SKU。
- **c5_6** [supported] 在微软官方域名 learn.microsoft.com 的 Microsoft Q&A 社区回帖中，一名用户称其找到“official source”支持 Microsoft 365 Copilot 发布时为每用户每月 30 美元、最低 300 席位的门槛，并附以“Lead Status”购买需商业执行人员支持；该内容作者为社区回帖者，托管于官方域名但非微软发布的正式定价或许可文档。 [ev_ed3321c44ccc6a9f9c21cc34](#ev_ed3321c44ccc6a9f9c21cc34)（supports） [ev_ffd11ecc2bb84864914d2f1f](#ev_ffd11ecc2bb84864914d2f1f)（supports） [ev_6a4c3a159214691b845d80f9](#ev_6a4c3a159214691b845d80f9)（supports）
  依据/推导：原文直接含 30 美元、300 席位、Lead Status 与“official source”自称。按来源性质属 vendor_community 用户回帖，其“官方”自称不等于厂商正式条款，故仅为社区转述事实，时间点为“发布时（2023 年 11 月前后）”。
- **c5_7** [supported] 据第三方博客 GoSearch 的价格表，Microsoft 365 Copilot Business 面向最多 300 席位的 SMB 用户，标价为年付每用户每月 21 美元（截至 2026 年 12 月 31 日促销价 18 美元）、月付每用户每月 25.20 美元；另有 Microsoft 365 Copilot Enterprise 面向企业用户，年付每用户每月 30 美元，前提为 E3 或 E5 等企业许可。 [ev_1c5e8d52ca92ee55e5872952](#ev_1c5e8d52ca92ee55e5872952)（supports） [ev_965dd9a179fc418fa7860d03](#ev_965dd9a179fc418fa7860d03)（supports） [ev_8dc1a462bcbabea6372dd436](#ev_8dc1a462bcbabea6372dd436)（supports）
  依据/推导：原文表格逐项给出层级、用户范围、标价与前提许可。来源为 third_party 博客，属二手“标价”转述，不能等同官方定价页或已实现收入/利润。
- **c5_8** [supported] 现有已校验摘录中不存在微软官方 Microsoft 365 Copilot 定价页或产品条款正文，仅有第三方指南/博客/wiki 与官方域名下的社区回帖。 [ev_ed3321c44ccc6a9f9c21cc34](#ev_ed3321c44ccc6a9f9c21cc34)（supports） [ev_7ace5d6faca5eabf1dd72cb4](#ev_7ace5d6faca5eabf1dd72cb4)（supports） [ev_1c5e8d52ca92ee55e5872952](#ev_1c5e8d52ca92ee55e5872952)（supports）
  依据/推导：逐条核对本轮来源的 source_authority：全部为 third_party 或 vendor_community，无 vendor_official 定价页或条款 PDF。此为对证据构成的陈述，不解释为“官方无此规定”。
- **c6_1** [supported] 据微软《Microsoft Copilot Studio Licensing Guide》（2025 年 11 月版），Copilot Studio 容量包（Copilot Credit capacity pack）标价为每包每月 200 美元，且 1 个容量包 = 25,000 Copilot Credits。 [ev_41d3722308a5dc62841ab0a5](#ev_41d3722308a5dc62841ab0a5)（supports）
  依据/推导：原文逐字给出“Pricing: $200 per pack/month”与“1 capacity pack = 25,000 Copilot Credits”；来源为供应方官方 PDF（vendor_official），属正式许可文档，可作为“标价”事实，不等于已实现收入或利润。
- **c6_2** [supported] 据该指南的许可产品摘要，Microsoft Copilot Studio 的计费配置为 Per Tenant，1 个 Copilot Credit Pack 提供每月 25,000 Copilot Credits。 [ev_003c5df5954edbd9341087ff](#ev_003c5df5954edbd9341087ff)（supports）
  依据/推导：原文摘要表列明 SKU 名称、计费配置（Per Tenant）与每包 25,000 Credits/月；支持容量包为租户级、按月计量的计费单位，但不提供任何实际销售或收入数据。
- **c6_3** [supported] 据该指南的对比表，Microsoft 365 Copilot 标价为每用户每月 30 美元，附带代理使用（included agent usage，含脚注），并可通过按用付费（脚注称无上限）或 Copilot Studio 许可（容量包，每包 25,000 Copilot Credits，附脚注）扩展。 [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports）
  依据/推导：原文表格行直接给出 30 美元/用户/月、Included agent usage 与两种扩展方式；主语为 Microsoft 365 Copilot，不是 Copilot Studio 自身定价。脚注具体内容未在本摘录中出现，故“无上限”与“包含额度”的细则仍不得推断。
- **c6_4** [supported] 该指南规定，若代理使用者本身持有 Microsoft 365 Copilot 许可，且代理通过经身份验证的 Microsoft 365 Copilot 运行，则员工面向场景（Business to Employee）中对 Microsoft Copilot Studio 代理及其所调用工具/功能的使用可包含在 Microsoft 365 Copilot USL 之内。 [ev_8bc2eed8ec3ada195601a770](#ev_8bc2eed8ec3ada195601a770)（supports）
  依据/推导：原文陈述“are included in the Microsoft 365 Copilot USL when the user of the agent is licensed with Microsoft 365 Copilot and the agent is operating using the authenticated Microsoft 365 Copilot…”。此为“included agent usage”适用条件的官方表述之一，但未给出该额度的具体数值或公平使用上限数字。

## 推导

- **c1_6** [supported] 由“需先持有符合条件的基础许可、Copilot 以附加项按用户每月收费”可推导：企业整体采用 Copilot 的授权与支出规模同时取决于基础许可基数与为多少用户叠加 Copilot，而非仅由 Copilot 本身单价决定。 [ev_1ebea556d7a9f2df48d924e8](#ev_1ebea556d7a9f2df48d924e8)（supports） [ev_24a65cda850e7a8bee7b3595](#ev_24a65cda850e7a8bee7b3595)（supports）
  依据/推导：基于 c1_1、c1_2、c1_3 的事实推导：购买前提为已持有基础许可，收费单位为每用户，故总支出随叠加用户数线性增长并叠加在基础许可支出之上。此为推导，非收入结论。
- **c2_5** [supported] 由上述官方陈述可推导：Copilot Studio 的收费结构至少包含“构建者按用户席位许可”与“组织级租户许可”两部分，而代理的终端使用者不按席位计费，因此其使用规模扩展与 M365 Copilot 的“全员按席位叠加”模式在计费对象上不同。 [ev_c557f4700e8401b9b8aa89c4](#ev_c557f4700e8401b9b8aa89c4)（supports） [ev_5d2ddf74caa4a658bc155dac](#ev_5d2ddf74caa4a658bc155dac)（supports） [ev_595c2120b9d4c011d7f54407](#ev_595c2120b9d4c011d7f54407)（supports）
  依据/推导：基于 c2_1、c2_2、c2_3 的官方事实推导：构建者按席位、使用者免许可，故计费随构建者数量而非使用者数量增长；此为推导，且代理运行的消息/容量计费未在证据中出现，不能据此推断收入规模。
- **c3_6** [supported] 由该指南可推导：Copilot Studio 在结算上以 Copilot Credits 为共同单位，购买入口分为后付费计量、容量包许可与阶梯折扣预付费三种，组织可按预计代理使用量选择容量包或预付费以获得折扣，而非单纯按人头订阅计费。 [ev_970f49f4b21e69e442f9aa9b](#ev_970f49f4b21e69e442f9aa9b)（supports） [ev_94c3c9036b71c0917ffec552](#ev_94c3c9036b71c0917ffec552)（supports） [ev_19abf275bb24f872ac03af6f](#ev_19abf275bb24f872ac03af6f)（supports）
  依据/推导：基于 c3_2、c3_4 的事实推导：三者均以 Copilot Credits 计量，只有预付费计划给出阶梯折扣；此为定价机制推导，不涉及实际收入实现。
- **c3_7** [supported] 结合此前官方 Learn 文章的“构建者按用户许可 + 租户级许可”，可推导该指南中的 Copilot Studio 许可（容量包）与按用户许可属于不同层级：前者按 Copilot Credits 容量授权运行与使用，后者授权用户创建/管理代理；二者计价单位不能混同。 [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports） [ev_bc21f8a13e28b99d53e3f1ff](#ev_bc21f8a13e28b99d53e3f1ff)（supports） [ev_970f49f4b21e69e442f9aa9b](#ev_970f49f4b21e69e442f9aa9b)（supports）
  依据/推导：指南将授权运行容量的“MCS License（capacity pack）”与“Copilot Studio use rights with Microsoft 365 Copilot Plans”并列为不同购买路径，且 AI 能力需 Copilot Credits；结合 c2_1、c2_2 的用户许可事实可作出层级区分。此为推导，指南摘录未逐字重申按用户席位条款。
- **c4_10** [mixed] 综合现有转述可推导：Microsoft 365 Copilot 的计费单位是“按用户/席位”的订阅附加项，且存在面向最多 300 用户租户的较低价位层级（第三方称 21 美元，另有 18 美元限期价），这意味着“300 席位最低购买要求”并非对所有租户一刀切，而是与面向小型租户的低价层级并存、需以官方条款说明其适用条件。 [ev_ffd11ecc2bb84864914d2f1f](#ev_ffd11ecc2bb84864914d2f1f)（supports） [ev_ff6725a9c148a2b8fc30e268](#ev_ff6725a9c148a2b8fc30e268)（contradicts） [ev_06ec321c1bc48bcb4d7043d8](#ev_06ec321c1bc48bcb4d7043d8)（contradicts）
  依据/推导：由 c4_1、c4_3 的按席位附加项与 c4_5、c4_6 的小型租户低价层级推导；社区回帖的 300 席位门槛与面向 300 用户以下租户的 21/18 美元层级存在直接张力。双方均为第三方或社区内容，无官方条款可裁定，故标为 mixed 并保留冲突，不据以关闭 gap1。
- **c5_9** [supported] 由现有转述可推导：Microsoft 365 Copilot 的计费单位在各渠道转述中一致为“按用户/席位”的订阅附加项，但其前提许可清单在不同档位下不一致（社区回帖称 E3 不含 Copilot 而为附加服务；第三方博客对 Business 档列出 Business Basic/Standard/Premium、Apps for Business、Teams Essentials；对 Enterprise 档列出 E3/E5），说明“符合条件许可”按档位区分而非单一清单。 [ev_87c60951a53b2dcd25e37154](#ev_87c60951a53b2dcd25e37154)（supports） [ev_50f29e435396a46a2cd45e44](#ev_50f29e435396a46a2cd45e44)（supports） [ev_1c5e8d52ca92ee55e5872952](#ev_1c5e8d52ca92ee55e5872952)（supports） [ev_7ace5d6faca5eabf1dd72cb4](#ev_7ace5d6faca5eabf1dd72cb4)（supports）
  依据/推导：基于 c5_1、c5_2、c5_4、c5_7 的转述事实推导层级结构；此为推导，且缺少官方逐项 SKU 条款，不能据此认定任何清单为正式清单。
- **c5_10** [mixed] 由现有转述可推导：社区回帖所述“300 席位最低购买”与第三方所述“300 用户以下租户 21/18 美元层级”之间的冲突，可用“不同档位/时点”解释——前者指向 2023 年发布时标准附加项的交易门槛，后者指向 2025 年 12 月起存在的 Copilot Business 档（其上限本身即为 300 用户）；两者标价与适用租户规模不同，但该解释仍缺乏官方条款确认。 [ev_ffd11ecc2bb84864914d2f1f](#ev_ffd11ecc2bb84864914d2f1f)（supports） [ev_965dd9a179fc418fa7860d03](#ev_965dd9a179fc418fa7860d03)（contradicts） [ev_50f29e435396a46a2cd45e44](#ev_50f29e435396a46a2cd45e44)（supports）
  依据/推导：回帖给出统一 300 席位门槛；第三方资料给出面向≤300 用户租户的 21 美元档与 Business 档 300 用户上限。二者在“是否存在较低价位层级”上直接冲突，仅能作出部分调和性推导；无官方定价页裁定，故标 mixed 并保留冲突。
- **c6_5** [supported] 由官方指南可推导：Copilot Studio 容量包按租户、按包（每包 25,000 Credits/月）计价 200 美元/月，而按用付费计量为后付费且指南摘录未给出单价，因此除预付费阶梯外，pay-as-you-go 的具体每 Credit 计量单价在现有证据中仍无法确定。 [ev_41d3722308a5dc62841ab0a5](#ev_41d3722308a5dc62841ab0a5)（supports） [ev_970f49f4b21e69e442f9aa9b](#ev_970f49f4b21e69e442f9aa9b)（supports）
  依据/推导：容量包单价与单位已由官方明确；pay-as-you-go 仅被描述为 postpay 计量，摘录未含其单价表，故只能作出“单价缺失”的推导，不能填以估值。

## 商业判断

- **c3_8** [supported] 由于 Copilot Studio 消耗以 Copilot Credits 计量且提供阶梯折扣预付费，企业将代理从试点扩展到大规模使用的边际成本取决于交互量，而非新增终端用户数；这使扩展决策更接近按用量/容量规划，而 Microsoft 365 Copilot 的扩展则随叠加席位数线性增长。 [ev_3191e0b91c06073417a97734](#ev_3191e0b91c06073417a97734)（supports） [ev_19abf275bb24f872ac03af6f](#ev_19abf275bb24f872ac03af6f)（supports） [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports）
  依据/推导：基于官方计费机制的商业判断：Credits 随交互消耗、预付费有折扣；M365 Copilot 为每用户每月标价。此为判断而非预测，指南未披露任何实际消耗量或收入数据。
- **c4_11** [mixed] 若面向小型租户的较低价位层级成立，则 Microsoft 365 Copilot 的收入扩展路径可能呈两层：小型租户以较低单价扩大席位覆盖，大型企业以标准单价叠加于 E3/E5 基础许可；这使得席位数量而非仅单价成为收入扩张的主要驱动，但该判断依赖尚未获官方确认的价位层级。 [ev_ff6725a9c148a2b8fc30e268](#ev_ff6725a9c148a2b8fc30e268)（supports） [ev_25394e4d74c3b997dcacafe0](#ev_25394e4d74c3b997dcacafe0)（supports） [ev_ffd11ecc2bb84864914d2f1f](#ev_ffd11ecc2bb84864914d2f1f)（contradicts）
  依据/推导：基于第三方标价与附加项结构的商业判断，不涉及任何实际收入或利润数据；因价位层级与 300 席位门槛冲突且无官方定价页确认，判断本身标记为 mixed 而非 supported。
- **c5_11** [mixed] 若按档位解释成立，则微软在 Microsoft 365 Copilot 上的席位扩张呈现两层定价：SMB 租户以约 21/18 美元的较低单价扩席（单租户上限 300），大型企业以约 30 美元单价叠加于 E3/E5；这意味着购买门槛应按档位而非统一 300 席位理解，且席位数量是价格机制下的主要扩展变量，但这只是基于未获官方确认标价的商业判断。 [ev_965dd9a179fc418fa7860d03](#ev_965dd9a179fc418fa7860d03)（supports） [ev_50f29e435396a46a2cd45e44](#ev_50f29e435396a46a2cd45e44)（supports） [ev_ed3321c44ccc6a9f9c21cc34](#ev_ed3321c44ccc6a9f9c21cc34)（contradicts）
  依据/推导：依据 c5_4、c5_7、c5_10 作出的商业判断，不涉及任何实际收入、折扣实现或利润数据；因标价未经官方定价页确认且与社区门槛冲突，判断标记 mixed。
- **c6_6** [supported] 由于随 Microsoft 365 Copilot 附带代理使用（在满足许可与身份验证条件时计入 M365 Copilot USL），已在 Copilot 上按席位付费的企业可在不额外购买容量包的情况下试用代理场景，从而降低 Copilot Studio 的初始扩展门槛；但当代理使用超出附带额度或涉及非附带条件场景时，支出将转向 200 美元/月容量包或后付费计量。 [ev_8bc2eed8ec3ada195601a770](#ev_8bc2eed8ec3ada195601a770)（supports） [ev_41d3722308a5dc62841ab0a5](#ev_41d3722308a5dc62841ab0a5)（supports）
  依据/推导：基于官方“附带使用条件”与“容量包 200 美元/月”事实作出的商业判断，不涉及实际消耗量、收入或利润；附带额度的具体上限未获官方数字，故判断限于“门槛与后续计费路径”的定性结构。

## 待验证假设

- **c1_7** [unverified] 社区回帖所述“最小 300 席位”可能仅反映某一时点或某类交易渠道的采购门槛，而非所有企业客户的通用最低购买要求。 [ev_ffd11ecc2bb84864914d2f1f](#ev_ffd11ecc2bb84864914d2f1f)（contradicts） [ev_965dd9a179fc418fa7860d03](#ev_965dd9a179fc418fa7860d03)（contradicts）
  依据/推导：第三方资料提到面向 300 用户以下商业租户的 21 美元层级，与统一 300 席位门槛存在张力；现有证据不足以确认，需官方正式条款验证。
- **c2_7** [unverified] Copilot Studio 除按用户许可外可能还按消息/容量等用量计费，且其是否需要先持有 Microsoft 365 或 Power Platform 基础许可尚不明确，需以官方 Licensing Guide 与产品条款验证。 [ev_69a443d625c4905e973b6941](#ev_69a443d625c4905e973b6941)（supports）
  依据/推导：官方文章提示存在专门的许可指南与用量估算器，但本轮摘录未给出消息/容量计费与基础许可前提的正式表述；此为待验证假设，不能用于关闭 gap2。
- **c3_9** [unverified] Copilot Studio 的购买前提可能包括先持有 Microsoft 365 或 Power Platform 基础许可（例如通过 M365 Copilot 计划附带的 Copilot Studio 使用权），但指南摘录未逐字规定基础许可门槛。 [ev_7d1d68228d013e72f6062cf1](#ev_7d1d68228d013e72f6062cf1)（supports）
  依据/推导：对比表出现“Copilot Studio use rights with Microsoft 365 Copilot Plans”行，暗示存在随基础计划附带的路径，但无独立条款说明是否强制要求基础许可；按规则假设不得用于关闭缺口。
- **c5_12** [unverified] 微软可能已将 300 席位从“统一最低购买量”调整为“Copilot Business 档的租户规模上限”，而标准档可能另有最低购买量要求（或已取消该要求），需官方定价页或 Product Terms 正文验证。 [ev_ffd11ecc2bb84864914d2f1f](#ev_ffd11ecc2bb84864914d2f1f)（supports） [ev_50f29e435396a46a2cd45e44](#ev_50f29e435396a46a2cd45e44)（contradicts）
  依据/推导：回帖的“最低购买 300 席位”与第三方“Business 档上限 300 用户、仅 CSP”在语义上可互换但方向不同；现有证据无法区分，故为待验证假设，不得用于关闭 gap。
- **c6_7** [unverified] 指南脚注中的“Included agent usage”与“Fair Usage Limit”可能对应尚待核实的公平使用上限数值或适用范围，且 pay-as-you-go 计量单价可能以每 Copilot Credit 或每消息计，需以指南脚注与计量页原文验证。 [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports）
  依据/推导：对比表行仅出现脚注标记与“Fair Usage Limit4”字样，摘录未包含脚注正文与单价数字；按规则假设不得用于关闭缺口，故保留为待验证问题。

## 证据缺口

- gap0 [open] Microsoft 365 Copilot 与 Copilot Studio 面向的企业使用者、收费单位和购买前提有何区别？这些差异可能如何影响企业客户扩展使用和微软的收入来源？优先使用官方资料；将价格与许可事实、基于事实的推导、商业判断和仍待验证假设明确区分，不把产品定价直接当成已实现收入或利润。
- gap1 [open] 缺少微软官方（如 Microsoft 365 Copilot 官方定价/许可页面或产品条款 PDF）对以下内容的正式规定：(1) 符合条件的基础许可清单；(2) 按用户/席位计费与最低购买数量的正式条款；(3) 当前官方标价。现有证据均为第三方指南或官方域名下的社区回帖，不能作为厂商正式文档，无法据此确认购买门槛（如 300 席位最低要求是否普遍适用）。
- gap2 [open] 缺少官方资料说明 Copilot Studio 面向的使用者、收费单位（如按消息/容量包还是按用户）及购买前提，以完成与 Microsoft 365 Copilot 的对比并评估对扩展使用与收入来源的影响。
- gap3 [open] 缺少微软官方《Microsoft Copilot Studio Licensing Guide》或产品条款正文，用以正式规定 Copilot Studio 的计价单位（按用户席位与/或消息、容量包）、各档定价，以及是否需要先持有 Microsoft 365 或 Power Platform 基础许可等购买前提。
- gap4 [open] 缺少指南对 pay-as-you-go 计量单价、容量包（每包 25,000 Copilot Credits）单价及 M365 Copilot 所含代理使用额度（included agent usage / fair usage limit）的具体条款原文，无法核实除预付费阶梯外各档的完整标价。
- gap5 [open] 缺少微软官方 Microsoft 365 Copilot 定价页或产品条款正文，用以正式列明符合条件的基础许可清单（具体产品/SKU）及按用户/席位计费条款，以裁定社区回帖的“300 席位最低购买”与第三方所述“300 用户以下租户 21/18 美元层级”之间的冲突。
- gap6 [open] 缺少微软官方 Microsoft 365 Copilot 定价页或 Product Terms 正文中按档位（Copilot Business 与 enterprise 标准档）逐项列出的符合条件基础许可清单（具体产品/SKU），以及各档是否存在最低购买席位或仅设租户规模上限的正式条款。
- gap7 [open] 缺少《Microsoft Copilot Studio Licensing Guide》正文及脚注对 Microsoft 365 Copilot “Included agent usage / Fair Usage Limit”的具体上限数值、计量口径与适用场景的原文条款，无法据此评估附带额度大小及超限后的计费。
- gap8 [open] 缺少该指南中 pay-as-you-go 计量器（Microsoft Copilot Studio pay-as-you-go meter）的每单位（每 Copilot Credit 或每消息）计量单价的原文条款，无法核实后付费计量的完整标价。

## 问题与检索记录

- q0 / 第 0 轮 / 缺口 初始问题：Microsoft 365 Copilot 与 Copilot Studio 面向的企业使用者、收费单位和购买前提有何区别？这些差异可能如何影响企业客户扩展使用和微软的收入来源？优先使用官方资料；将价格与许可事实、基于事实的推导、商业判断和仍待验证假设明确区分，不把产品定价直接当成已实现收入或利润。
- q1 / 第 1 轮 / 缺口 gap0：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？
  Tavily search1：Microsoft 365 Copilot licensing prerequisites per user；结果 5；错误 无
- q2 / 第 2 轮 / 缺口 gap2：微软官方资料如何规定 Copilot Studio 的目标使用者、计费单位（按消息/容量包还是按用户席位）以及购买前提（如是否需要先持有 Microsoft 365 或 Power Platform 基础许可）？
- q3 / 第 3 轮 / 缺口 gap3：微软官方的《Microsoft Copilot Studio Licensing Guide》如何规定 Copilot Studio 的计价单位（按用户席位、消息或容量包）、各档价格，以及购买前提（是否要求先持有 Microsoft 365 或 Power Platform 基础许可）？
  Tavily search2：Copilot Studio licensing guide credits；结果 5；错误 无
- q4 / 第 4 轮 / 缺口 gap1：微软官方的 Microsoft 365 Copilot 定价或许可页面如何正式规定：符合条件的基础许可清单、按用户/席位计费与最低购买数量的条款，以及当前官方标价（包括是否存在面向 300 用户以下租户的较低价位层级）？
  Tavily search3：Microsoft 365 Copilot pricing license prerequisites；结果 5；错误 无
- q5 / 第 5 轮 / 缺口 gap5：微软官方 Microsoft 365 Copilot 定价页或产品条款如何正式列明符合条件的基础许可（具体产品/SKU）、按用户/席位计费条款，以及是否以 300 席位为最低购买门槛或存在面向 300 用户以下租户的较低价位层级？
  Tavily search4：Microsoft 365 Copilot Product Terms license prerequisites；结果 5；错误 无
- q6 / 第 6 轮 / 缺口 gap4：微软《Microsoft Copilot Studio Licensing Guide》对按用量付费（pay-as-you-go）计量单价、容量包（每包 25,000 Copilot Credits）单价，以及随 Microsoft 365 Copilot 附带的代理使用额度（included agent usage 或公平使用上限）具体规定了什么？
- q7 / 第 7 轮 / 缺口 gap6：微软官方 Microsoft 365 Copilot 定价页或 Product Terms 正文是否按档位（Copilot Business 与 enterprise 标准档）逐项列出符合条件的基础许可清单（具体产品/SKU），并为各档分别规定最低购买席位数或租户规模上限？
  Tavily search5：Microsoft 365 Copilot Product Terms qualifying base license；结果 5；错误 无

## 原文摘录与追溯

<a id="ev_f87733083f65c2d852ecf82d"></a>
### ev_f87733083f65c2d852ecf82d

> A customer must already have an eligible Business or Enterprise license before purchasing Copilot.

来源：Microsoft Copilot Pricing & Licensing Guide for Business | IntuitionLabs — https://intuitionlabs.ai/articles/microsoft-copilot-pricing-licensing

类型：web；读取时间：2026-10-19T08:15:06.191815+00:00；截断：False

问题 q1 → 分块 chk_afde016363de9908171654b5_12750 → 来源 src_afde016363de9908171654b5；清洗后字符 [12817, 12915)

SHA-256：`77c7f2f9b7d142b037ae4d67f5e85f026192e164e7bfe91e94befc3343457885`；范围：<main> element; characters 0-45868 of 45868

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://intuitionlabs.ai/articles/microsoft-copilot-pricing-licensing
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_1ebea556d7a9f2df48d924e8"></a>
### ev_1ebea556d7a9f2df48d924e8

> In practical terms, this means Copilot is not a standalone product – it cannot be bought without a base subscription.

来源：Microsoft Copilot Pricing & Licensing Guide for Business | IntuitionLabs — https://intuitionlabs.ai/articles/microsoft-copilot-pricing-licensing

类型：web；读取时间：2026-10-19T08:15:06.191815+00:00；截断：False

问题 q1 → 分块 chk_afde016363de9908171654b5_7650 → 来源 src_afde016363de9908171654b5；清洗后字符 [7722, 7839)

SHA-256：`77c7f2f9b7d142b037ae4d67f5e85f026192e164e7bfe91e94befc3343457885`；范围：<main> element; characters 0-45868 of 45868

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://intuitionlabs.ai/articles/microsoft-copilot-pricing-licensing
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_f0c7197503136a03358245be"></a>
### ev_f0c7197503136a03358245be

> This add-on unlocks Copilot functionality in Office apps for each licensed user. It requires one of the qualifying base licenses listed above.

来源：Microsoft Copilot Pricing & Licensing Guide for Business | IntuitionLabs — https://intuitionlabs.ai/articles/microsoft-copilot-pricing-licensing

类型：web；读取时间：2026-10-19T08:15:06.191815+00:00；截断：False

问题 q1 → 分块 chk_afde016363de9908171654b5_13261 → 来源 src_afde016363de9908171654b5；清洗后字符 [13654, 13796)

SHA-256：`77c7f2f9b7d142b037ae4d67f5e85f026192e164e7bfe91e94befc3343457885`；范围：<main> element; characters 0-45868 of 45868

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://intuitionlabs.ai/articles/microsoft-copilot-pricing-licensing
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_8dc1a462bcbabea6372dd436"></a>
### ev_8dc1a462bcbabea6372dd436

> For business users, Copilot is offered as an add-on for: Microsoft 365 E3 and E5 Microsoft 365 Business Standard and Business Premium

来源：Microsoft 365 Copilot Licensing and Pricing Guide 2026 — https://licenseq.com/microsoft-365-copilot-everything-you-need-to-know/

类型：web；读取时间：2026-10-19T08:15:19.403413+00:00；截断：False

问题 q1 → 分块 chk_4f418ec03cd813ded8121084_6630 → 来源 src_4f418ec03cd813ded8121084；清洗后字符 [6788, 6921)

SHA-256：`4581130125d7b19ca4647196c9a5ca9d8d82c22439d3389dd403086177fd7515`；范围：<main> element; characters 0-21721 of 21721

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://licenseq.com/microsoft-365-copilot-everything-you-need-to-know
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_24a65cda850e7a8bee7b3595"></a>
### ev_24a65cda850e7a8bee7b3595

> All of the paid Copilot offerings are per-user, per-month subscriptions, typically billed annually.

来源：Microsoft Copilot Pricing & Licensing Guide for Business | IntuitionLabs — https://intuitionlabs.ai/articles/microsoft-copilot-pricing-licensing

类型：web；读取时间：2026-10-19T08:15:06.191815+00:00；截断：False

问题 q1 → 分块 chk_afde016363de9908171654b5_13261 → 来源 src_afde016363de9908171654b5；清洗后字符 [13279, 13378)

SHA-256：`77c7f2f9b7d142b037ae4d67f5e85f026192e164e7bfe91e94befc3343457885`；范围：<main> element; characters 0-45868 of 45868

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://intuitionlabs.ai/articles/microsoft-copilot-pricing-licensing
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_965dd9a179fc418fa7860d03"></a>
### ev_965dd9a179fc418fa7860d03

> Since December 1, 2025, Business-plan tenants with up to 300 users buy the dedicated Microsoft 365 Copilot Business tier at $21 per user per month; larger organizations use the standard $30 add-on.

来源：Microsoft 365 Copilot Licensing and Pricing Guide 2026 — https://licenseq.com/microsoft-365-copilot-everything-you-need-to-know/

类型：web；读取时间：2026-10-19T08:15:19.403413+00:00；截断：False

问题 q1 → 分块 chk_4f418ec03cd813ded8121084_6630 → 来源 src_4f418ec03cd813ded8121084；清洗后字符 [6922, 7119)

SHA-256：`4581130125d7b19ca4647196c9a5ca9d8d82c22439d3389dd403086177fd7515`；范围：<main> element; characters 0-21721 of 21721

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://licenseq.com/microsoft-365-copilot-everything-you-need-to-know
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_ffd11ecc2bb84864914d2f1f"></a>
### ev_ffd11ecc2bb84864914d2f1f

> Microsoft 365 Copilot will cost $30 USD per user per month and will be available for purchase via “Lead Status,” which means that support from a Microsoft Commercial Executive is needed to trans

来源：M365 Copilot licensing question - Microsoft Q&A — https://learn.microsoft.com/en-us/answers/questions/5270940/m365-copilot-licensing-question

类型：web；读取时间：2026-10-19T08:14:56.503049+00:00；截断：False

问题 q1 → 分块 chk_d2d8ac22f5283580437b9a05_4080 → 来源 src_d2d8ac22f5283580437b9a05；清洗后字符 [4486, 4680)

SHA-256：`8d184fed9da7243fedf7638b3685727bea1be6ee40dd63ef22ab0f5f3df845ea`；范围：<main> element; characters 0-6160 of 6160

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://learn.microsoft.com/en-us/answers/questions/5270940/m365-copilot-licensing-question
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_69a443d625c4905e973b6941"></a>
### ev_69a443d625c4905e973b6941

> This article is written for tenant administrators. If you want to sign up for Copilot Studio as an individual, see Get access to Copilot Studio .

来源：Assign user licenses and manage access - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing

类型：web；读取时间：2026-10-19T08:15:25.396132+00:00；截断：False

问题 q2 → 分块 chk_51c3f28b8ea860277ab6e489_510 → 来源 src_51c3f28b8ea860277ab6e489；清洗后字符 [533, 678)

SHA-256：`6ef0e4c0f2bf56a37f11a6a016a5afbfa81ef44500f51bac14557a2f4bca1b2f`；范围：<main> element; characters 0-5641 of 5641

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_c557f4700e8401b9b8aa89c4"></a>
### ev_c557f4700e8401b9b8aa89c4

> To create and manage agents with Copilot Studio

来源：Assign user licenses and manage access - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing

类型：web；读取时间：2026-10-19T08:15:25.396132+00:00；截断：False

问题 q2 → 分块 chk_51c3f28b8ea860277ab6e489_510 → 来源 src_51c3f28b8ea860277ab6e489；清洗后字符 [1063, 1110)

SHA-256：`6ef0e4c0f2bf56a37f11a6a016a5afbfa81ef44500f51bac14557a2f4bca1b2f`；范围：<main> element; characters 0-5641 of 5641

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_5d2ddf74caa4a658bc155dac"></a>
### ev_5d2ddf74caa4a658bc155dac

> You can't assign this license to individual users.

来源：Assign user licenses and manage access - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing

类型：web；读取时间：2026-10-19T08:15:25.396132+00:00；截断：False

问题 q2 → 分块 chk_51c3f28b8ea860277ab6e489_1530 → 来源 src_51c3f28b8ea860277ab6e489；清洗后字符 [1532, 1582)

SHA-256：`6ef0e4c0f2bf56a37f11a6a016a5afbfa81ef44500f51bac14557a2f4bca1b2f`；范围：<main> element; characters 0-5641 of 5641

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_595c2120b9d4c011d7f54407"></a>
### ev_595c2120b9d4c011d7f54407

> Users of your agents don't need a special license. After you publish your agent, anyone who can access the published agent can interact with it.

来源：Assign user licenses and manage access - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing

类型：web；读取时间：2026-10-19T08:15:25.396132+00:00；截断：False

问题 q2 → 分块 chk_51c3f28b8ea860277ab6e489_1530 → 来源 src_51c3f28b8ea860277ab6e489；清洗后字符 [1588, 1732)

SHA-256：`6ef0e4c0f2bf56a37f11a6a016a5afbfa81ef44500f51bac14557a2f4bca1b2f`；范围：<main> element; characters 0-5641 of 5641

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_f5a66e8106f6e7dbd07f7d8f"></a>
### ev_f5a66e8106f6e7dbd07f7d8f

> Guest users of your tenant can't access Copilot Studio.

来源：Assign user licenses and manage access - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing

类型：web；读取时间：2026-10-19T08:15:25.396132+00:00；截断：False

问题 q2 → 分块 chk_51c3f28b8ea860277ab6e489_1530 → 来源 src_51c3f28b8ea860277ab6e489；清洗后字符 [1733, 1788)

SHA-256：`6ef0e4c0f2bf56a37f11a6a016a5afbfa81ef44500f51bac14557a2f4bca1b2f`；范围：<main> element; characters 0-5641 of 5641

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_0ee9f3c33cf2fceb119fb539"></a>
### ev_0ee9f3c33cf2fceb119fb539

> After you purchase a Copilot Studio license from the Microsoft 365 admin center, purchase user licenses to give users access

来源：Assign user licenses and manage access - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing

类型：web；读取时间：2026-10-19T08:15:25.396132+00:00；截断：False

问题 q2 → 分块 chk_51c3f28b8ea860277ab6e489_2040 → 来源 src_51c3f28b8ea860277ab6e489；清洗后字符 [2515, 2639)

SHA-256：`6ef0e4c0f2bf56a37f11a6a016a5afbfa81ef44500f51bac14557a2f4bca1b2f`；范围：<main> element; characters 0-5641 of 5641

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_5174ece39a89a0b98f010f9c"></a>
### ev_5174ece39a89a0b98f010f9c

> Look for Copilot Studio User License . Select the number of licenses you need and complete the checkout process.

来源：Assign user licenses and manage access - Microsoft Copilot Studio | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing

类型：web；读取时间：2026-10-19T08:15:25.396132+00:00；截断：False

问题 q2 → 分块 chk_51c3f28b8ea860277ab6e489_2551 → 来源 src_51c3f28b8ea860277ab6e489；清洗后字符 [2775, 2887)

SHA-256：`6ef0e4c0f2bf56a37f11a6a016a5afbfa81ef44500f51bac14557a2f4bca1b2f`；范围：<main> element; characters 0-5641 of 5641

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://learn.microsoft.com/en-us/microsoft-copilot-studio/requirements-licensing
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_3191e0b91c06073417a97734"></a>
### ev_3191e0b91c06073417a97734

> As users interact with Copilot Studio agents, or agents perform tasks on behalf of users, they consume Copilot Credits.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:16:16.101906+00:00；截断：False

问题 q3 → 分块 chk_c68aacefe8ad1e6fd48eeabb_3571 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [3821, 3940)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 34e19ee38a41 → 问题 q3 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Copilot Studio licensing guide credits；当时的问题：微软官方的《Microsoft Copilot Studio Licensing Guide》如何规定 Copilot Studio 的计价单位（按用户席位、消息或容量包）、各档价格，以及购买前提（是否要求先持有 Microsoft 365 或 Power Platform 基础许可）？

<a id="ev_970f49f4b21e69e442f9aa9b"></a>
### ev_970f49f4b21e69e442f9aa9b

> Copilot Credits are the common currency across Copilot Studio capabilities and are available via the Microsoft Copilot Studio pay-as-you-go meter, the Microsoft Copilot Studio license (i.e., Copilot Credit capacity pack) and the

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:16:16.101906+00:00；截断：False

问题 q3 → 分块 chk_c68aacefe8ad1e6fd48eeabb_3571 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [3941, 4169)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 34e19ee38a41 → 问题 q3 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Copilot Studio licensing guide credits；当时的问题：微软官方的《Microsoft Copilot Studio Licensing Guide》如何规定 Copilot Studio 的计价单位（按用户席位、消息或容量包）、各档价格，以及购买前提（是否要求先持有 Microsoft 365 或 Power Platform 基础许可）？

<a id="ev_7d1d68228d013e72f6062cf1"></a>
### ev_7d1d68228d013e72f6062cf1

> Microsoft 365 Copilot $30 per user/month Included agent usage1 Pay-as-you-go: unlimited2 License (capacity pack): 25,000 Copilot Credit /pack3

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:16:16.101906+00:00；截断：False

问题 q3 → 分块 chk_c68aacefe8ad1e6fd48eeabb_13260 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [13714, 13856)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 34e19ee38a41 → 问题 q3 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Copilot Studio licensing guide credits；当时的问题：微软官方的《Microsoft Copilot Studio Licensing Guide》如何规定 Copilot Studio 的计价单位（按用户席位、消息或容量包）、各档价格，以及购买前提（是否要求先持有 Microsoft 365 或 Power Platform 基础许可）？

<a id="ev_94c3c9036b71c0917ffec552"></a>
### ev_94c3c9036b71c0917ffec552

> Each CCCUs is worth $1 and converts to 100 Copilot Credits.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:16:16.101906+00:00；截断：False

问题 q3 → 分块 chk_c68aacefe8ad1e6fd48eeabb_10710 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [10887, 10946)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 34e19ee38a41 → 问题 q3 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Copilot Studio licensing guide credits；当时的问题：微软官方的《Microsoft Copilot Studio Licensing Guide》如何规定 Copilot Studio 的计价单位（按用户席位、消息或容量包）、各档价格，以及购买前提（是否要求先持有 Microsoft 365 或 Power Platform 基础许可）？

<a id="ev_19abf275bb24f872ac03af6f"></a>
### ev_19abf275bb24f872ac03af6f

> Tier Copilot Credits Commit Units (CCCU) Price Discount 1 3,000 $2,850 5% 2 15,000 $14,100 6% 3 30,000 $27,900 7% 4 150,000 $138,000 8% 5 300,000 $270,000 10% 6 750,000 $660,000 12% 7 1,500,000 $1,290,000 14% 8 2,250,000 $1,867,500 17% 9 3,000,000 $2,400,000 20%

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:16:16.101906+00:00；截断：False

问题 q3 → 分块 chk_c68aacefe8ad1e6fd48eeabb_10710 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [10994, 11256)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 34e19ee38a41 → 问题 q3 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Copilot Studio licensing guide credits；当时的问题：微软官方的《Microsoft Copilot Studio Licensing Guide》如何规定 Copilot Studio 的计价单位（按用户席位、消息或容量包）、各档价格，以及购买前提（是否要求先持有 Microsoft 365 或 Power Platform 基础许可）？

<a id="ev_bc21f8a13e28b99d53e3f1ff"></a>
### ev_bc21f8a13e28b99d53e3f1ff

> Access to AI Tools capabilities within Copilot Studio requires Copilot Studio capacity, which is licensed through Copilot Credits.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:16:16.101906+00:00；截断：False

问题 q3 → 分块 chk_c68aacefe8ad1e6fd48eeabb_28050 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [28419, 28549)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 34e19ee38a41 → 问题 q3 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Copilot Studio licensing guide credits；当时的问题：微软官方的《Microsoft Copilot Studio Licensing Guide》如何规定 Copilot Studio 的计价单位（按用户席位、消息或容量包）、各档价格，以及购买前提（是否要求先持有 Microsoft 365 或 Power Platform 基础许可）？

<a id="ev_6a4c3a159214691b845d80f9"></a>
### ev_6a4c3a159214691b845d80f9

> For anyone finding this post via search, here is an official source for the minimum requirement of 300 seats at 30 USD per seat per month for Microsoft 365 CoPilot at launch: SKU and transaction details (for Licensing Solution Providers)

来源：M365 Copilot licensing question - Microsoft Q&A — https://learn.microsoft.com/en-us/answers/questions/5270940/m365-copilot-licensing-question

类型：web；读取时间：2026-10-19T08:14:56.503049+00:00；截断：False

问题 q4 → 分块 chk_d2d8ac22f5283580437b9a05_4080 → 来源 src_d2d8ac22f5283580437b9a05；清洗后字符 [4200, 4437)

SHA-256：`8d184fed9da7243fedf7638b3685727bea1be6ee40dd63ef22ab0f5f3df845ea`；范围：<main> element; characters 0-6160 of 6160

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://learn.microsoft.com/en-us/answers/questions/5270940/m365-copilot-licensing-question
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_87c60951a53b2dcd25e37154"></a>
### ev_87c60951a53b2dcd25e37154

> Microsoft 365 Copilot is not included with Microsoft 365 (M365) E3 licenses; it is an additional s

来源：M365 Copilot licensing question - Microsoft Q&A — https://learn.microsoft.com/en-us/answers/questions/5270940/m365-copilot-licensing-question

类型：web；读取时间：2026-10-19T08:14:56.503049+00:00；截断：False

问题 q4 → 分块 chk_d2d8ac22f5283580437b9a05_0 → 来源 src_d2d8ac22f5283580437b9a05；清洗后字符 [502, 600)

SHA-256：`8d184fed9da7243fedf7638b3685727bea1be6ee40dd63ef22ab0f5f3df845ea`；范围：<main> element; characters 0-6160 of 6160

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://learn.microsoft.com/en-us/answers/questions/5270940/m365-copilot-licensing-question
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_7167c90735860b7f2afb8b4a"></a>
### ev_7167c90735860b7f2afb8b4a

> Microsoft 365 Copilot is licensed as a per-user add-on.

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:17:07.906897+00:00；截断：False

问题 q4 → 分块 chk_76369ce0f3851a65c00a0b8b_1020 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [1315, 1370)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 34e19ee38a41 → 问题 q4 → 搜索 search3 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Microsoft 365 Copilot pricing license prerequisites；当时的问题：微软官方的 Microsoft 365 Copilot 定价或许可页面如何正式规定：符合条件的基础许可清单、按用户/席位计费与最低购买数量的条款，以及当前官方标价（包括是否存在面向 300 用户以下租户的较低价位层级）？

<a id="ev_a6313e81bd7b26eb15a4808d"></a>
### ev_a6313e81bd7b26eb15a4808d

> Microsoft sells it as a User SL that must sit on top of a listed prerequisite license, the same subscription meter used for other Microsoft 365 Online Services.

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:17:07.906897+00:00；截断：False

问题 q4 → 分块 chk_76369ce0f3851a65c00a0b8b_1020 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [1371, 1531)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 34e19ee38a41 → 问题 q4 → 搜索 search3 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Microsoft 365 Copilot pricing license prerequisites；当时的问题：微软官方的 Microsoft 365 Copilot 定价或许可页面如何正式规定：符合条件的基础许可清单、按用户/席位计费与最低购买数量的条款，以及当前官方标价（包括是否存在面向 300 用户以下租户的较低价位层级）？

<a id="ev_fb3a95aea3d25159bb5badb6"></a>
### ev_fb3a95aea3d25159bb5badb6

> Prerequisite A listed Microsoft 365, Office 365 or standalone service license (Product Terms)

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:17:07.906897+00:00；截断：False

问题 q4 → 分块 chk_76369ce0f3851a65c00a0b8b_0 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [350, 443)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 34e19ee38a41 → 问题 q4 → 搜索 search3 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Microsoft 365 Copilot pricing license prerequisites；当时的问题：微软官方的 Microsoft 365 Copilot 定价或许可页面如何正式规定：符合条件的基础许可清单、按用户/席位计费与最低购买数量的条款，以及当前官方标价（包括是否存在面向 300 用户以下租户的较低价位层级）？

<a id="ev_ff6725a9c148a2b8fc30e268"></a>
### ev_ff6725a9c148a2b8fc30e268

> Microsoft 365 Copilot pricing now has two tiers: Copilot Business at $21 per user per month for tenants on Business plans with up to 300 users (since December 1, 2025), and the standard Microsoft 365 Copilot

来源：Microsoft 365 Copilot Licensing and Pricing Guide 2026 — https://licenseq.com/microsoft-365-copilot-everything-you-need-to-know/

类型：web；读取时间：2026-10-19T08:15:19.403413+00:00；截断：False

问题 q4 → 分块 chk_4f418ec03cd813ded8121084_7650 → 来源 src_4f418ec03cd813ded8121084；清洗后字符 [8043, 8250)

SHA-256：`4581130125d7b19ca4647196c9a5ca9d8d82c22439d3389dd403086177fd7515`；范围：<main> element; characters 0-21721 of 21721

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://licenseq.com/microsoft-365-copilot-everything-you-need-to-know
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_06ec321c1bc48bcb4d7043d8"></a>
### ev_06ec321c1bc48bcb4d7043d8

> Business-tier customers with 300 seats or fewer pay $18/user/month through December 31, 2026, down from $21.

来源：Microsoft Copilot Pricing 2026: Plans, Costs, and Total Cost of Ownership | The GoSearch Blog — https://www.gosearch.ai/blog/microsoft-copilot-pricing/

类型：web；读取时间：2026-10-19T08:17:22.901446+00:00；截断：False

问题 q4 → 分块 chk_0a009e6cf67b8f9a039acdd2_27541 → 来源 src_0a009e6cf67b8f9a039acdd2；清洗后字符 [27642, 27750)

SHA-256：`f8e66b7736eec780d00704e605d29cf9e7792f4c495980f18fd18f60e8c96298`；范围：<body> element; characters 0-29481 of 29481

获取链：运行 34e19ee38a41 → 问题 q4 → 搜索 search3 → https://www.gosearch.ai/blog/microsoft-copilot-pricing
检索词：Microsoft 365 Copilot pricing license prerequisites；当时的问题：微软官方的 Microsoft 365 Copilot 定价或许可页面如何正式规定：符合条件的基础许可清单、按用户/席位计费与最低购买数量的条款，以及当前官方标价（包括是否存在面向 300 用户以下租户的较低价位层级）？

<a id="ev_0084c3fbf2dbfaba904d5ebc"></a>
### ev_0084c3fbf2dbfaba904d5ebc

> Enterprise buyers committing to 1,000 or more seats may see discounts of 30% to 50% starting as early as October 2026, according to reporting from The Information — though Microsoft hasn’t confirmed these terms on its own pricing pages yet.

来源：Microsoft Copilot Pricing 2026: Plans, Costs, and Total Cost of Ownership | The GoSearch Blog — https://www.gosearch.ai/blog/microsoft-copilot-pricing/

类型：web；读取时间：2026-10-19T08:17:22.901446+00:00；截断：False

问题 q4 → 分块 chk_0a009e6cf67b8f9a039acdd2_27541 → 来源 src_0a009e6cf67b8f9a039acdd2；清洗后字符 [27751, 27991)

SHA-256：`f8e66b7736eec780d00704e605d29cf9e7792f4c495980f18fd18f60e8c96298`；范围：<body> element; characters 0-29481 of 29481

获取链：运行 34e19ee38a41 → 问题 q4 → 搜索 search3 → https://www.gosearch.ai/blog/microsoft-copilot-pricing
检索词：Microsoft 365 Copilot pricing license prerequisites；当时的问题：微软官方的 Microsoft 365 Copilot 定价或许可页面如何正式规定：符合条件的基础许可清单、按用户/席位计费与最低购买数量的条款，以及当前官方标价（包括是否存在面向 300 用户以下租户的较低价位层级）？

<a id="ev_e16946e98cc6a4fd4790f9f2"></a>
### ev_e16946e98cc6a4fd4790f9f2

> Microsoft 365 Copilot (Enterprise/Business) $30 (annual), $31.50 billed monthly

来源：Microsoft Copilot Pricing & Licensing Guide for Business | IntuitionLabs — https://intuitionlabs.ai/articles/microsoft-copilot-pricing-licensing

类型：web；读取时间：2026-10-19T08:15:06.191815+00:00；截断：False

问题 q4 → 分块 chk_afde016363de9908171654b5_16320 → 来源 src_afde016363de9908171654b5；清洗后字符 [16728, 16807)

SHA-256：`77c7f2f9b7d142b037ae4d67f5e85f026192e164e7bfe91e94befc3343457885`；范围：<main> element; characters 0-45868 of 45868

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://intuitionlabs.ai/articles/microsoft-copilot-pricing-licensing
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_25394e4d74c3b997dcacafe0"></a>
### ev_25394e4d74c3b997dcacafe0

> For business customers, Copilot is offered as an add-on subscription – notably USD $30 per user per month (annual billing) ( [3] ) – on top of an existing Microsoft 365 or Office 365 license (e.g. an Enterprise E3/E5 or Business Standard/Premium plan).

来源：Microsoft Copilot Pricing & Licensing Guide for Business | IntuitionLabs — https://intuitionlabs.ai/articles/microsoft-copilot-pricing-licensing

类型：web；读取时间：2026-10-19T08:15:06.191815+00:00；截断：False

问题 q4 → 分块 chk_afde016363de9908171654b5_1530 → 来源 src_afde016363de9908171654b5；清洗后字符 [1622, 1874)

SHA-256：`77c7f2f9b7d142b037ae4d67f5e85f026192e164e7bfe91e94befc3343457885`；范围：<main> element; characters 0-45868 of 45868

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://intuitionlabs.ai/articles/microsoft-copilot-pricing-licensing
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_7ace5d6faca5eabf1dd72cb4"></a>
### ev_7ace5d6faca5eabf1dd72cb4

> Microsoft 365 Copilot is licensed as a per-user add-on. Microsoft sells it as a User SL that must sit on top of a listed prerequisite license, the same subscription meter used for other Microsoft 365 Online Services. [2] Current Microsoft Learn pages call the product Microsoft Copilot and describe it as

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:17:07.906897+00:00；截断：False

问题 q5 → 分块 chk_76369ce0f3851a65c00a0b8b_1020 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [1315, 1619)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 34e19ee38a41 → 问题 q4 → 搜索 search3 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Microsoft 365 Copilot pricing license prerequisites；当时的问题：微软官方的 Microsoft 365 Copilot 定价或许可页面如何正式规定：符合条件的基础许可清单、按用户/席位计费与最低购买数量的条款，以及当前官方标价（包括是否存在面向 300 用户以下租户的较低价位层级）？

<a id="ev_811e6c59a19b124192d36cca"></a>
### ev_811e6c59a19b124192d36cca

> The enterprise pricing card adds that “A separate license for a qualifying Microsoft 365 plan is required.” [4] Product Terms also list Microsoft 365 Copilot for Sales and Copilot for Service as separate User SLs. [2]

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:17:07.906897+00:00；截断：False

问题 q5 → 分块 chk_76369ce0f3851a65c00a0b8b_2550 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [2929, 3146)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 34e19ee38a41 → 问题 q4 → 搜索 search3 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Microsoft 365 Copilot pricing license prerequisites；当时的问题：微软官方的 Microsoft 365 Copilot 定价或许可页面如何正式规定：符合条件的基础许可清单、按用户/席位计费与最低购买数量的条款，以及当前官方标价（包括是否存在面向 300 用户以下租户的较低价位层级）？

<a id="ev_50f29e435396a46a2cd45e44"></a>
### ev_50f29e435396a46a2cd45e44

> Microsoft 365 Copilot Business is added (at last!) to the June 2026 Product Terms. This rather belated addition follows the 1 March, 2026 launch of the SMB flavour of Microsoft 365 Copilot, which, as you’d expect for a Business license, has a cap of 300 users. This June update gives us information about the availability (just CSP) and the licensing prerequisites – you can buy Microsoft 365 Copilot Business for users already licensed with Microsoft 365 Business Basic/Standard/Premium, Microsoft 365 Apps for Business, or Teams Essentials.

来源：Microsoft 365 Copilot Business in the Product Terms - Licensing Lore & Law — https://www.licensingschool.co.uk/licensing-blog/2026/06/05/microsoft-365-copilot-business-in-the-product-terms

类型：web；读取时间：2026-10-19T08:18:15.936645+00:00；截断：False

问题 q5 → 分块 chk_364c03b09b61a5fee19ca672_0 → 来源 src_364c03b09b61a5fee19ca672；清洗后字符 [54, 596)

SHA-256：`f4c0eda6e258e98e4a454c58d21d28a886dc6d2704c7ea8fe6e75a2972351153`；范围：<article> element; characters 0-1103 of 1103

获取链：运行 34e19ee38a41 → 问题 q5 → 搜索 search4 → https://www.licensingschool.co.uk/licensing-blog/2026/06/05/microsoft-365-copilot-business-in-the-product-terms
检索词：Microsoft 365 Copilot Product Terms license prerequisites；当时的问题：微软官方 Microsoft 365 Copilot 定价页或产品条款如何正式列明符合条件的基础许可（具体产品/SKU）、按用户/席位计费条款，以及是否以 300 席位为最低购买门槛或存在面向 300 用户以下租户的较低价位层级？

<a id="ev_dd8fd4d3a596744952d19cee"></a>
### ev_dd8fd4d3a596744952d19cee

> qualifying Microsoft 365 plan is required” to acquire Copilot ( [10] ). In practical terms, this means Copilot is not a standalone product – it cannot be bought without a base subscription. Qualifying Plans: The eligible base licenses are broadly any commercial Microsoft 365 or Office 365 plan (business or enterprise tier).

来源：Microsoft Copilot Pricing & Licensing Guide for Business | IntuitionLabs — https://intuitionlabs.ai/articles/microsoft-copilot-pricing-licensing

类型：web；读取时间：2026-10-19T08:15:06.191815+00:00；截断：False

问题 q5 → 分块 chk_afde016363de9908171654b5_7650 → 来源 src_afde016363de9908171654b5；清洗后字符 [7650, 7975)

SHA-256：`77c7f2f9b7d142b037ae4d67f5e85f026192e164e7bfe91e94befc3343457885`；范围：<main> element; characters 0-45868 of 45868

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://intuitionlabs.ai/articles/microsoft-copilot-pricing-licensing
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_ed3321c44ccc6a9f9c21cc34"></a>
### ev_ed3321c44ccc6a9f9c21cc34

> For anyone finding this post via search, here is an official source for the minimum requirement of 300 seats at 30 USD per seat per month for Microsoft 365 CoPilot at launch: SKU and transaction details (for Licensing Solution Providers) 7. What is the price for Microsoft 365 Copilot? Microsoft 365 Copilot will cost $30 USD per user per month and will be available for purchase via “Lead Status,” which means that support from a Microsoft Commercial Executive is needed to trans

来源：M365 Copilot licensing question - Microsoft Q&A — https://learn.microsoft.com/en-us/answers/questions/5270940/m365-copilot-licensing-question

类型：web；读取时间：2026-10-19T08:14:56.503049+00:00；截断：False

问题 q5 → 分块 chk_d2d8ac22f5283580437b9a05_4080 → 来源 src_d2d8ac22f5283580437b9a05；清洗后字符 [4200, 4680)

SHA-256：`8d184fed9da7243fedf7638b3685727bea1be6ee40dd63ef22ab0f5f3df845ea`；范围：<main> element; characters 0-6160 of 6160

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://learn.microsoft.com/en-us/answers/questions/5270940/m365-copilot-licensing-question
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

<a id="ev_1c5e8d52ca92ee55e5872952"></a>
### ev_1c5e8d52ca92ee55e5872952

> Microsoft 365 Copilot Business Small and midsize business users, up to 300 seats $21/user/month annual ($18 promo through Dec 31, 2026); $25.20/user/month monthly Qualifying M365 business license $32–$43/user/month, using the examples below Microsoft 365 Copilot Enterprise Enterprise users $30/user/month annual Qualifying enterprise license, such as E3 or E5 $69–$90/user/month before volume discounts

来源：Microsoft Copilot Pricing 2026: Plans, Costs, and Total Cost of Ownership | The GoSearch Blog — https://www.gosearch.ai/blog/microsoft-copilot-pricing/

类型：web；读取时间：2026-10-19T08:17:22.901446+00:00；截断：False

问题 q5 → 分块 chk_0a009e6cf67b8f9a039acdd2_6630 → 来源 src_0a009e6cf67b8f9a039acdd2；清洗后字符 [6672, 7075)

SHA-256：`f8e66b7736eec780d00704e605d29cf9e7792f4c495980f18fd18f60e8c96298`；范围：<body> element; characters 0-29481 of 29481

获取链：运行 34e19ee38a41 → 问题 q4 → 搜索 search3 → https://www.gosearch.ai/blog/microsoft-copilot-pricing
检索词：Microsoft 365 Copilot pricing license prerequisites；当时的问题：微软官方的 Microsoft 365 Copilot 定价或许可页面如何正式规定：符合条件的基础许可清单、按用户/席位计费与最低购买数量的条款，以及当前官方标价（包括是否存在面向 300 用户以下租户的较低价位层级）？

<a id="ev_41d3722308a5dc62841ab0a5"></a>
### ev_41d3722308a5dc62841ab0a5

> • Pricing: $200 per pack/month • Copilot Credit Capacity: 1 capacity pack = 25,000 Copilot Credits

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:16:16.101906+00:00；截断：False

问题 q6 → 分块 chk_c68aacefe8ad1e6fd48eeabb_9180 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [9621, 9719)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 34e19ee38a41 → 问题 q3 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Copilot Studio licensing guide credits；当时的问题：微软官方的《Microsoft Copilot Studio Licensing Guide》如何规定 Copilot Studio 的计价单位（按用户席位、消息或容量包）、各档价格，以及购买前提（是否要求先持有 Microsoft 365 或 Power Platform 基础许可）？

<a id="ev_003c5df5954edbd9341087ff"></a>
### ev_003c5df5954edbd9341087ff

> Copilot Studio License Offer Summary SKU Name Microsoft Copilot Studio Billing Configuration Per Tenant 1 Copilot Credit Pack 25,000 Copilot Credits per month

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:16:16.101906+00:00；截断：False

问题 q6 → 分块 chk_c68aacefe8ad1e6fd48eeabb_9690 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [9963, 10121)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 34e19ee38a41 → 问题 q3 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Copilot Studio licensing guide credits；当时的问题：微软官方的《Microsoft Copilot Studio Licensing Guide》如何规定 Copilot Studio 的计价单位（按用户席位、消息或容量包）、各档价格，以及购买前提（是否要求先持有 Microsoft 365 或 Power Platform 基础许可）？

<a id="ev_5a440717841727e42686e122"></a>
### ev_5a440717841727e42686e122

> Microsoft 365 Copilot $30 per user/month Included agent usage1 Pay-as-you-go: unlimited2 License (capacity pack): 25,000 Copilot Credit /pack3 Pre

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:16:16.101906+00:00；截断：False

问题 q6 → 分块 chk_c68aacefe8ad1e6fd48eeabb_13260 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [13714, 13860)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 34e19ee38a41 → 问题 q3 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Copilot Studio licensing guide credits；当时的问题：微软官方的《Microsoft Copilot Studio Licensing Guide》如何规定 Copilot Studio 的计价单位（按用户席位、消息或容量包）、各档价格，以及购买前提（是否要求先持有 Microsoft 365 或 Power Platform 基础许可）？

<a id="ev_8bc2eed8ec3ada195601a770"></a>
### ev_8bc2eed8ec3ada195601a770

> 4. Employee-facing scenarios (Business to Employee) usage of Microsoft Copilot Studio agents and the Microsoft Copilot Studio tools/features invoked by the said agents, ar

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:16:16.101906+00:00；截断：False

问题 q6 → 分块 chk_c68aacefe8ad1e6fd48eeabb_14790 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [15219, 15390)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 34e19ee38a41 → 问题 q3 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Copilot Studio licensing guide credits；当时的问题：微软官方的《Microsoft Copilot Studio Licensing Guide》如何规定 Copilot Studio 的计价单位（按用户席位、消息或容量包）、各档价格，以及购买前提（是否要求先持有 Microsoft 365 或 Power Platform 基础许可）？

<a id="ev_27a561b5f3ea5211b614cc13"></a>
### ev_27a561b5f3ea5211b614cc13

> Copilot Studio capacity pack Tenant-wide license, 25,000 Copilot Credits per pack $200.00 per pack per month [11]

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:17:07.906897+00:00；截断：False

问题 q6 → 分块 chk_76369ce0f3851a65c00a0b8b_2550 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [2815, 2928)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 34e19ee38a41 → 问题 q4 → 搜索 search3 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Microsoft 365 Copilot pricing license prerequisites；当时的问题：微软官方的 Microsoft 365 Copilot 定价或许可页面如何正式规定：符合条件的基础许可清单、按用户/席位计费与最低购买数量的条款，以及当前官方标价（包括是否存在面向 300 用户以下租户的较低价位层级）？

<a id="ev_d6a2acd5f657e1bea1583915"></a>
### ev_d6a2acd5f657e1bea1583915

> Microsoft 365 Copilot Business is added (at last!) to the June 2026 Product Terms.

来源：Microsoft 365 Copilot Business in the Product Terms - Licensing Lore & Law — https://www.licensingschool.co.uk/licensing-blog/2026/06/05/microsoft-365-copilot-business-in-the-product-terms

类型：web；读取时间：2026-10-19T08:18:15.936645+00:00；截断：False

问题 q7 → 分块 chk_364c03b09b61a5fee19ca672_0 → 来源 src_364c03b09b61a5fee19ca672；清洗后字符 [54, 136)

SHA-256：`f4c0eda6e258e98e4a454c58d21d28a886dc6d2704c7ea8fe6e75a2972351153`；范围：<article> element; characters 0-1103 of 1103

获取链：运行 34e19ee38a41 → 问题 q5 → 搜索 search4 → https://www.licensingschool.co.uk/licensing-blog/2026/06/05/microsoft-365-copilot-business-in-the-product-terms
检索词：Microsoft 365 Copilot Product Terms license prerequisites；当时的问题：微软官方 Microsoft 365 Copilot 定价页或产品条款如何正式列明符合条件的基础许可（具体产品/SKU）、按用户/席位计费条款，以及是否以 300 席位为最低购买门槛或存在面向 300 用户以下租户的较低价位层级？

<a id="ev_5357be5c4fba5741f5c814a6"></a>
### ev_5357be5c4fba5741f5c814a6

> This rather belated addition follows the 1 March, 2026 launch of the SMB flavour of Microsoft 365 Copilot, which, as you’d expect for a Business license, has a cap of 300 users.

来源：Microsoft 365 Copilot Business in the Product Terms - Licensing Lore & Law — https://www.licensingschool.co.uk/licensing-blog/2026/06/05/microsoft-365-copilot-business-in-the-product-terms

类型：web；读取时间：2026-10-19T08:18:15.936645+00:00；截断：False

问题 q7 → 分块 chk_364c03b09b61a5fee19ca672_0 → 来源 src_364c03b09b61a5fee19ca672；清洗后字符 [137, 314)

SHA-256：`f4c0eda6e258e98e4a454c58d21d28a886dc6d2704c7ea8fe6e75a2972351153`；范围：<article> element; characters 0-1103 of 1103

获取链：运行 34e19ee38a41 → 问题 q5 → 搜索 search4 → https://www.licensingschool.co.uk/licensing-blog/2026/06/05/microsoft-365-copilot-business-in-the-product-terms
检索词：Microsoft 365 Copilot Product Terms license prerequisites；当时的问题：微软官方 Microsoft 365 Copilot 定价页或产品条款如何正式列明符合条件的基础许可（具体产品/SKU）、按用户/席位计费条款，以及是否以 300 席位为最低购买门槛或存在面向 300 用户以下租户的较低价位层级？

<a id="ev_669ab71f58c501f2e6a63dc5"></a>
### ev_669ab71f58c501f2e6a63dc5

> This June update gives us information about the availability (just CSP) and the licensing prerequisites – you can buy Microsoft 365 Copilot Business for users already licensed with Microsoft 365 Business Basic/Standard/Premium, Microsoft 365 Apps for Business, or Teams Essentials.

来源：Microsoft 365 Copilot Business in the Product Terms - Licensing Lore & Law — https://www.licensingschool.co.uk/licensing-blog/2026/06/05/microsoft-365-copilot-business-in-the-product-terms

类型：web；读取时间：2026-10-19T08:18:15.936645+00:00；截断：False

问题 q7 → 分块 chk_364c03b09b61a5fee19ca672_0 → 来源 src_364c03b09b61a5fee19ca672；清洗后字符 [315, 596)

SHA-256：`f4c0eda6e258e98e4a454c58d21d28a886dc6d2704c7ea8fe6e75a2972351153`；范围：<article> element; characters 0-1103 of 1103

获取链：运行 34e19ee38a41 → 问题 q5 → 搜索 search4 → https://www.licensingschool.co.uk/licensing-blog/2026/06/05/microsoft-365-copilot-business-in-the-product-terms
检索词：Microsoft 365 Copilot Product Terms license prerequisites；当时的问题：微软官方 Microsoft 365 Copilot 定价页或产品条款如何正式列明符合条件的基础许可（具体产品/SKU）、按用户/席位计费条款，以及是否以 300 席位为最低购买门槛或存在面向 300 用户以下租户的较低价位层级？

<a id="ev_75872840a1f4ecd27c63627d"></a>
### ev_75872840a1f4ecd27c63627d

> Product Terms state that purchases of listed licenses “also require the purchase of a Prerequisite License”.

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:17:07.906897+00:00；截断：False

问题 q7 → 分块 chk_76369ce0f3851a65c00a0b8b_5610 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [5795, 5903)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 34e19ee38a41 → 问题 q4 → 搜索 search3 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Microsoft 365 Copilot pricing license prerequisites；当时的问题：微软官方的 Microsoft 365 Copilot 定价或许可页面如何正式规定：符合条件的基础许可清单、按用户/席位计费与最低购买数量的条款，以及当前官方标价（包括是否存在面向 300 用户以下租户的较低价位层级）？

<a id="ev_04cb72d2de1b48e64a584b4d"></a>
### ev_04cb72d2de1b48e64a584b4d

> For Microsoft 365 Copilot, the prerequisites are Microsoft 365 Apps for business or enterprise, Business Basic, Standard or Premium, F1, F3, A1, A3, A5, A7, E3, E5, E7, G3, G5 or G7; Office 365 F3, A1, A3, A5, E1, E3, E5, G3 or G5; Exchange Online; SharePoint Online; OneDrive; Microsoft Clipchamp; Microso

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:17:07.906897+00:00；截断：False

问题 q7 → 分块 chk_76369ce0f3851a65c00a0b8b_5610 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [5904, 6210)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 34e19ee38a41 → 问题 q4 → 搜索 search3 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Microsoft 365 Copilot pricing license prerequisites；当时的问题：微软官方的 Microsoft 365 Copilot 定价或许可页面如何正式规定：符合条件的基础许可清单、按用户/席位计费与最低购买数量的条款，以及当前官方标价（包括是否存在面向 300 用户以下租户的较低价位层级）？

<a id="ev_551e69a70fcf0f487927f48d"></a>
### ev_551e69a70fcf0f487927f48d

> The enterprise pricing card adds that “A separate license for a qualifying Microsoft 365 plan is required.”

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:17:07.906897+00:00；截断：False

问题 q7 → 分块 chk_76369ce0f3851a65c00a0b8b_2550 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [2929, 3036)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 34e19ee38a41 → 问题 q4 → 搜索 search3 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Microsoft 365 Copilot pricing license prerequisites；当时的问题：微软官方的 Microsoft 365 Copilot 定价或许可页面如何正式规定：符合条件的基础许可清单、按用户/席位计费与最低购买数量的条款，以及当前官方标价（包括是否存在面向 300 用户以下租户的较低价位层级）？

<a id="ev_c9e53c158964c047e830ea79"></a>
### ev_c9e53c158964c047e830ea79

> Microsoft 365 Copilot is licensed as a per-user add-on. Microsoft sells it as a User SL that must sit on top of a listed prerequisite license, the same subscription meter used for other Microsoft 365 Online Services.

来源：Microsoft 365 Copilot licensing | LICENSEWARE Wiki — https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing/

类型：web；读取时间：2026-10-19T08:17:07.906897+00:00；截断：False

问题 q7 → 分块 chk_76369ce0f3851a65c00a0b8b_1020 → 来源 src_76369ce0f3851a65c00a0b8b；清洗后字符 [1315, 1531)

SHA-256：`e5d204a2c8798a0ba9aff82ba3f645e3cc1567355ba6a89537342785a94addb6`；范围：<main> element; characters 0-16076 of 16076

获取链：运行 34e19ee38a41 → 问题 q4 → 搜索 search3 → https://wiki.licenseware.io/wiki/microsoft-365-copilot-licensing
检索词：Microsoft 365 Copilot pricing license prerequisites；当时的问题：微软官方的 Microsoft 365 Copilot 定价或许可页面如何正式规定：符合条件的基础许可清单、按用户/席位计费与最低购买数量的条款，以及当前官方标价（包括是否存在面向 300 用户以下租户的较低价位层级）？

<a id="ev_27734b3a0534a75ed6588c60"></a>
### ev_27734b3a0534a75ed6588c60

> Qualifying Plans: The eligible base licenses are broadly any commercial Microsoft 365 or Office 365 plan (business or enterprise tier).

来源：Microsoft Copilot Pricing & Licensing Guide for Business | IntuitionLabs — https://intuitionlabs.ai/articles/microsoft-copilot-pricing-licensing

类型：web；读取时间：2026-10-19T08:15:06.191815+00:00；截断：False

问题 q7 → 分块 chk_afde016363de9908171654b5_7650 → 来源 src_afde016363de9908171654b5；清洗后字符 [7840, 7975)

SHA-256：`77c7f2f9b7d142b037ae4d67f5e85f026192e164e7bfe91e94befc3343457885`；范围：<main> element; characters 0-45868 of 45868

获取链：运行 34e19ee38a41 → 问题 q1 → 搜索 search1 → https://intuitionlabs.ai/articles/microsoft-copilot-pricing-licensing
检索词：Microsoft 365 Copilot licensing prerequisites per user；当时的问题：Microsoft 365 Copilot 的官方许可与定价页面如何规定其适用的企业使用者范围、收费单位（按用户还是按席位）以及购买前提（如是否要求先持有符合条件的 Microsoft 365 基础许可）？

完整来源文本、分块、引用和哈希见同目录 state.json；节点、调用及排序分数见 trace.jsonl。
