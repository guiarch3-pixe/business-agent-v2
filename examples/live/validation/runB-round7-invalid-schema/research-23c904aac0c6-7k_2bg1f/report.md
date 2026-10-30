# Microsoft｜企业研究

研究问题：Microsoft 365 Copilot 与 Copilot Studio 面向的企业使用者、收费单位和购买前提有何区别？这些差异可能如何影响企业客户扩展使用和微软的收入来源？优先使用官方资料；将价格与许可事实、基于事实的推导、商业判断和仍待验证假设明确区分，不把产品定价直接当成已实现收入或利润。

模式：live；停止原因：error；研究轮次：7

引用关系与摘录位置已做代码校验；语义支持关系、事实分类和缺口关闭是模型判断，未经独立事实核实。

## 事实（来源陈述）

- **c1_1** [supported] 第三方资料称 Microsoft 365 Copilot 采用按用户（按席位）的固定订阅收费，企业版约为每用户每月 30 美元。 [ev_5f9c6c0b1525ac6058573928](#ev_5f9c6c0b1525ac6058573928)（supports） [ev_77397efc85e48e36f7737925](#ev_77397efc85e48e36f7737925)（supports） [ev_43c3e2796f6955566107f0fb](#ev_43c3e2796f6955566107f0fb)（supports）
  依据/推导：三份第三方来源均陈述按用户/席位计费的固定订阅，并给出约 30 美元/用户/月的标价。属第三方转述的标价事实，非微软官方价目页，也未证明已实现收入。
- **c1_2** [supported] Microsoft 365 Copilot 是附加许可证（add-on），不能单独购买，必须叠加在合格的基础 Microsoft 365 计划之上；官方托管社区帖与第三方资料均如此陈述。 [ev_ad7a9de3061285191a6ddee2](#ev_ad7a9de3061285191a6ddee2)（supports） [ev_a65486f21fa17854e6c1f967](#ev_a65486f21fa17854e6c1f967)（supports） [ev_37d9dbe02b1950137794dea6](#ev_37d9dbe02b1950137794dea6)（supports）
  依据/推导：ev_ad7a9de…为 techcommunity.microsoft.com 托管的用户回帖（vendor_community），其作者观点不等同于厂商正式许可文档；第三方来源提供相同描述，构成交叉印证。
- **c1_3** [supported] 微软官方 Copilot Studio 定价页（在其产品描述语境下）写明：购买 Microsoft 365 Copilot 需要客户拥有符合条件的企业版或商业版 Microsoft 365 计划。 [ev_26e332f23a50ac329142b1d5](#ev_26e332f23a50ac329142b1d5)（supports）
  依据/推导：此句出自 microsoft.com 官方 Copilot Studio 定价页，位于介绍 Microsoft 365 Copilot 相关条目的上下文；仅支持“需有合格 Microsoft 365 计划”这一购买前提，不外推到具体点位价格。
- **c1_4** [supported] 据第三方资料，企业版附加项面向 E3/E5 租户，商务版 Copilot Business 面向基础计划为 Business Basic/Standard/Premium 且少于 300 席的组织；合格基础计划还包括 E3、E5、F1、F3、Apps for business/enterprise、Office 365 系列等更广清单。 [ev_a1dd93632d4ee6ca432f71f9](#ev_a1dd93632d4ee6ca432f71f9)（supports） [ev_abf036c5a23bda035de11180](#ev_abf036c5a23bda035de11180)（supports） [ev_bcff011e04cd21c7cb00be57](#ev_bcff011e04cd21c7cb00be57)（supports）
  依据/推导：三份第三方来源对基础计划与席位上限制描述基本一致；但均为二手转述，未与微软官方许可选项页核对，故仅作为第三方陈述保留。
- **c1_5** [supported] 按第三方资料，Copilot Business 与微软 365 Copilot 企业版标价分别约为每用户每月 21 美元（年付）和 30 美元（年付），且默认没有任何 Microsoft 365 计划包含付费 Copilot 体验。 [ev_4dc8e527a95c4faf0cf67ac8](#ev_4dc8e527a95c4faf0cf67ac8)（supports） [ev_abf036c5a23bda035de11180](#ev_abf036c5a23bda035de11180)（supports）
  依据/推导：仅为第三方列出的标价与许可前提，属于定价事实而非收入事实；且价格时点/版本需官方价目页确认。
- **c2_1** [supported] 微软官方 Learn 站的“License Options for Microsoft Copilot”页面在「Microsoft Copilot Business」条目下列出的基础计划为：Microsoft 365 Business Premium、Microsoft 365 Business Standard、Microsoft 365 Business Basic、Microsoft 365 Apps for Business 以及 Microsoft Teams Essentials。 [ev_44c41a1f06ca3f69d980dea4](#ev_44c41a1f06ca3f69d980dea4)（supports）
  依据/推导：该摘录来自 learn.microsoft.com 官方页面（vendor_official），逐字列出 Copilot Business 条目下的基础计划。注意：该页为“Microsoft Copilot”许可选项页，条目名为「Microsoft Copilot Business」，与第三方所称“Microsoft 365 Copilot Business”在命名上不完全一致，此处只按原文陈述其列示内容，不外推等同于第三方描述的产品 SKU。
- **c2_2** [supported] 同一官方 Learn 页面在「Microsoft Copilot」条目下列出的 Microsoft 365 计划包括：Microsoft 365 E7（含 Microsoft Copilot）、E5、E3、F1、F3、Business Premium、Business Standard、Business Basic、Apps for Enterprise、Apps for Business。 [ev_44c41a1f06ca3f69d980dea4](#ev_44c41a1f06ca3f69d980dea4)（supports）
  依据/推导：原文直接列举，包含 E3/E5/F1/F3 与 Apps for business/enterprise。E7 一项原文标注“includes Microsoft Copilot”，说明该条本身可能已含 Copilot，不能把 E7 简单当作可叠加附加项的基础计划。
- **c2_3** [supported] 同一官方 Learn 页面的条目还列出 Office 365 计划（Office 365 E5、E3、E1、F3）以及 Teams 计划（Teams Enterprise、Teams EEA、Teams Essentials）、Exchange 计划等，作为该条目下的可列基础计划。 [ev_44c41a1f06ca3f69d980dea4](#ev_44c41a1f06ca3f69d980dea4)（supports）
  依据/推导：摘录末尾列出 Office 365 E5/E3/E1/Off…（截断处紧接 F3）及 Microsoft Teams plans、Exchange plans；Office 365 F3 由 context_after 明确给出。截断部分无法确认是否含更多 Office 365 变体，故不作扩写。
- **c2_4** [supported] 第三方资料称 Microsoft 365 Copilot Business 仅附加于 Business Basic/Standard/Premium 与 Apps for business，并称微软目录描述将其上限定为 300 席；另一份第三方资料同样称 Copilot Business 仅附着 Business 计划且上限 300 席，并把 300 席与 Business 计划本身的上限相比较。 [ev_166813518580a59f6256b9bd](#ev_166813518580a59f6256b9bd)（supports） [ev_ae4581162fef64fba033cc93](#ev_ae4581162fef64fba033cc93)（supports）
  依据/推导：两段均出自第三方博客，作者转述“微软目录描述”但未给出官方链接原文；只能作为第三方转述的 300 席说法，不能据此认定官方条款已确认席位上限制。
- **c2_5** [contradicted] 本轮官方 Learn 页面摘录中并未出现“300 席上限”的表述，其 Copilot Business 条目仅列出基础计划清单。 [ev_44c41a1f06ca3f69d980dea4](#ev_44c41a1f06ca3f69d980dea4)（contradicts）
  依据/推导：这是关于证据覆盖范围的陈述：所检索到的官方许可选项页段落不含席位数上限内容。按规则，缺失证据不等于否定事实，故该项不用于否定 300 席说法，只说明官方来源尚未覆盖；状态标为 contradicted 仅表示与“第三方所称出自微软目录”的归因存在张力，需以原始目录描述核实。
- **c2_6** [supported] 第三方资料对合格基础计划的描述比官方 Learn 页面列示的更广，额外包括 Office 365 的 E1/E3/E5/F3 之外的 Teams Essentials/Enterprise/EEA、Exchange Kiosk 与 Plan 1/2、SharePoint Kiosk 与 Plan 1/2、OneDrive Plan 1/2、Planner、Project、Visio、Clipchamp 等单件 SKU；另一第三方资料仅列 E3/E5/F3、Business 三档与 Office 365 E1/E3/E5 等。 [ev_bcff011e04cd21c7cb00be57](#ev_bcff011e04cd21c7cb00be57)（supports） [ev_8c2da60f81aedf9a0ccbd367](#ev_8c2da60f81aedf9a0ccbd367)（supports）
  依据/推导：两份第三方来源的清单彼此不一致（一份极宽、一份较窄），且后者自称转述“微软最低要求文档”。引用其内容仅作为第三方陈述；第三方清单不能替代官方条款原文，二者冲突需以官方许可选项页/服务描述原文判定。
- **c3_1** [supported] 第三方资料称 Microsoft 365 Copilot 企业版附加项按每用户每月 30 美元、以年付承诺计价，需叠加在 Microsoft 365 E3、E5、Business Standard 或 Business Premium 等基础计划之上。 [ev_71d7fa6b4619c6ad40ffcc4b](#ev_71d7fa6b4619c6ad40ffcc4b)（supports） [ev_74be97792a22799d0ea44e1d](#ev_74be97792a22799d0ea44e1d)（supports） [ev_61755e1b2a2c6509b0363a8c](#ev_61755e1b2a2c6509b0363a8c)（supports）
  依据/推导：三份第三方来源一致陈述企业版约 30 美元/用户/月、年付；这仅是二手转述的标价与计费口径，不是微软官方价目页或产品条款原文，也不代表已实现收入。
- **c3_2** [supported] 第三方资料称 Microsoft 365 Copilot Business 面向不超过 300 席（或少于 300 用户）的组织，标准价约每用户每月 21 美元（年付），部分来源另列促销价 18 美元及按月计费 25.20 美元等变体。 [ev_5d151648c373cbe3ec065244](#ev_5d151648c373cbe3ec065244)（supports） [ev_ed396faee6afd96e8864ddb1](#ev_ed396faee6afd96e8864ddb1)（supports） [ev_47484136605be3d4f1ab5784](#ev_47484136605be3d4f1ab5784)（supports） [ev_3f0153d66ec7a2ad996d1d35](#ev_3f0153d66ec7a2ad996d1d35)（supports）
  依据/推导：多份第三方来源在 21 美元标准价上一致，但促销价截止日期（来源分别写 2026 年 9 月 30 日与 12 月 31 日）与生效说法互相冲突，保留冲突；价格均非官方条款。
- **c3_3** [supported] 本轮检索到的证据全部来自第三方博客与指南，没有任何一条摘录出自微软官方产品页、价目页、官方 PDF 或产品条款。 [ev_71d7fa6b4619c6ad40ffcc4b](#ev_71d7fa6b4619c6ad40ffcc4b)（supports） [ev_5d151648c373cbe3ec065244](#ev_5d151648c373cbe3ec065244)（supports） [ev_a9509426fa1e28de1db7d64b](#ev_a9509426fa1e28de1db7d64b)（supports）
  依据/推导：source_metadata 显示本轮来源均为 oran、o365hq、copilot-experts、gosearch、hso 等第三方站点（authority=third_party）；不把第三方转述称为微软官方标价。
- **c3_4** [unverified] 微软官方 Learn 的许可选项页（prior_evidence）仅列出 Copilot Business/Copilot 对应的基础计划清单，未在该摘录中出现 30 美元/21 美元的标价或“按席位计费”的明确条款表述。 [ev_44c41a1f06ca3f69d980dea4](#ev_44c41a1f06ca3f69d980dea4)（supports）
  依据/推导：该官方摘录内容限于计划资格列示，价格与计费单位未见于已校验片段；缺失证据不等于官方未公布价格，故只记为未验证覆盖范围。
- **c4_1** [supported] 本轮检索到的三份来源均为第三方站点（orchestry.com、hso.com、copilot-experts.com）的博客/指南，没有任何摘录出自 microsoft.com 的 Microsoft 365 Copilot 企业版官方定价页。 [ev_71d7fa6b4619c6ad40ffcc4b](#ev_71d7fa6b4619c6ad40ffcc4b)（supports） [ev_74be97792a22799d0ea44e1d](#ev_74be97792a22799d0ea44e1d)（supports） [ev_cb240676d64d8516aab9c323](#ev_cb240676d64d8516aab9c323)（supports）
  依据/推导：source_metadata 显示三份来源 authority 均为 third_party；prior_evidence 中唯一的 vendor_official 条目为 learn.microsoft.com 许可选项页与 Copilot Studio 定价页，均非 microsoft.com 的 M365 Copilot 企业版定价页。因此本轮无法直接核验该官方页面原文，此为证据覆盖范围陈述，不构成对页面内容的否定。
- **c4_2** [supported] 第三方资料称 Microsoft 365 Copilot 企业版附加项按每用户每月 30 美元、以年付承诺计价，并需叠加在 Microsoft 365 E3、E5、Business Standard 或 Business Premium 等合格基础计划之上。 [ev_71d7fa6b4619c6ad40ffcc4b](#ev_71d7fa6b4619c6ad40ffcc4b)（supports） [ev_74be97792a22799d0ea44e1d](#ev_74be97792a22799d0ea44e1d)（supports） [ev_cb240676d64d8516aab9c323](#ev_cb240676d64d8516aab9c323)（supports）
  依据/推导：三份第三方来源在 30 美元/用户/月与“需合格基础计划”上一致；但均为二手转述，不能等同微软官方定价页原文，也不能推出已实现收入或利润。
- **c4_3** [supported] 微软官方托管的 Copilot Studio 定价页写明：购买 Microsoft 365 Copilot 需客户拥有符合条件的企业版或商业版 Microsoft 365 计划。 [ev_26e332f23a50ac329142b1d5](#ev_26e332f23a50ac329142b1d5)（supports）
  依据/推导：该句出自 microsoft.com 官方 Copilot Studio 定价页（vendor_official），但语境是 Copilot Studio 定价页上的 Microsoft 365 Copilot 条目，只能支持“购买需有合格 Microsoft 365 计划”这一前提，不能据此认定 M365 Copilot 企业版定价页本身写有 30 美元或按席位计费。
- **c5_1** [supported] 微软官方《Microsoft Copilot Studio Licensing Guide》写明 Copilot Studio 的用量以 Copilot Credits 计量，可通过三种方式获得：Microsoft Copilot Studio 按用量付费计量表（pay-as-you-go）、Microsoft Copilot Studio 许可证（即 Copilot Credit 容量包）以及 Copilot Credit 预购计划。 [ev_74051b80b3a8d2af897e5dd6](#ev_74051b80b3a8d2af897e5dd6)（supports）
  依据/推导：原文直接陈述 Copilot Credits 为跨 Copilot Studio 能力的通用计量货币及其三种获取渠道。来源为 cdn-dynmedia-1.microsoft.com 托管的厂商官方 PDF（vendor_official），但摘录止于“and the”，第三种渠道由 context_after 补足，故仅陈述三类渠道名称，不引申价格。
- **c5_2** [supported] 同一官方许可指南的许可证摘要写明：Copilot Studio 许可证 SKU 的计费配置为“按租户（Per Tenant）”，容量包为每包每月 25,000 Copilot Credits。 [ev_d87ecf9adc80c628b6a88870](#ev_d87ecf9adc80c628b6a88870)（supports）
  依据/推导：原文逐字给出“Billing Configuration Per Tenant”与“25,000 Copilot Credits per month”。此为官方 PDF 对计费单位的陈述，支持“容量按租户计费”而非“按终端用户席位计费”；但该页日期标注为 October 2026，版本时点需注意。
- **c5_3** [supported] 同一官方指南写明：使用 Copilot Studio 构建和管理代理的每个用户都需要一个 Copilot Studio User License（$0），即作者侧用户许可标价为零。 [ev_d87ecf9adc80c628b6a88870](#ev_d87ecf9adc80c628b6a88870)（supports）
  依据/推导：原文“A Copilot Studio User License ($0) is required for each user that builds and manages agents”直接陈述。需注意其适用范围是“构建和管理代理的用户（作者）”，不能外推为使用代理的终端用户也按此 $0 席位计费。
- **c5_4** [supported] 微软官方许可指南的对照表中，Microsoft 365 Copilot 一栏为“$30 per user/month”，并列出“Included agent usage”，下接按用量付费（无限量）、许可证（容量包：每包 25,000 Copilot Credits）和预购计划等选项。 [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports）
  依据/推导：原文直接列出 $30 per user/month 并置于“Copilot Studio use rights with Microsoft 365 Copilot Plans”的上下文（context_before），说明该 $30 是 Microsoft 365 Copilot 计划的每用户标价，并附带一定的代理用量包含额度。此为本轮首次由厂商官方 PDF 直接支持的 30 美元/用户/月标价，但仅指标价，不等于已实现收入；容量包价格与预购折扣在摘录中被截断，不作陈述。
- **c5_5** [supported] 第三方博客称 Copilot Studio 按信用点（credit）计费、在租户层级汇总，而非按席位计费，成本取决于代理消耗的信用点而非使用人数。 [ev_d1dc73ce2233ff3803f9f60c](#ev_d1dc73ce2233ff3803f9f60c)（supports）
  依据/推导：cloudzero.com 第三方博客的直接陈述，与官方指南“Per Tenant”计费配置方向一致，可作为交叉印证，但本身不是厂商正式文档，不能单独支撑计费条款。
- **c5_6** [supported] 第三方资料称 Copilot Studio 已包含在所有 Microsoft 365 Copilot 许可证内用于内部代理使用，外部代理部署则需独立许可证，标价为每 25,000 Copilot Credits 每月 200 美元；并称自 2025 年 9 月起 Copilot Credits 取代了旧的按消息计费模式。 [ev_010bb475f18cd0facb1d4350](#ev_010bb475f18cd0facb1d4350)（supports）
  依据/推导：copilot-experts.com 第三方指南的陈述。其中“包含于 M365 Copilot 许可”“200 美元/25,000 Credits/月”“2025 年 9 月切换计费单位”均需官方条款核实；官方 PDF 摘录中对应位置为截断或未出现具体金额，故此处只作第三方陈述。
- **c5_7** [supported] 第三方资料称 Copilot Studio 租户容量包标价为每年 2,400 美元（一次性预付）、按年按月计 2,520 美元、或单月承诺 240 美元/月，作者工具用的 Copilot Studio User License 标价为 0 美元。 [ev_e0a050a8f91feb72529bed19](#ev_e0a050a8f91feb72529bed19)（supports） [ev_7a665bca240fe219b0300714](#ev_7a665bca240fe219b0300714)（supports）
  依据/推导：o365hq.com 第三方博客的两个片段分别给出容量包年价与“每包每年 2,400 美元标价+超额按用量付费”，以及 User License 为 0。属第三方转述的标价，不是官方价目页，也未证明已实现收入。
- **c5_8** [supported] 第三方文档镜像（GitHub 上 MicrosoftDocs/microsoft-365-docs 的容量包 Markdown）称：容量包是按月订阅，每月补充 25,000 信用点，且必须同时启用按用量付费作为超额兜底，或再叠加更多容量包；每个容量包是租户级许可证。 [ev_a6050c902b6bef2d33adf91b](#ev_a6050c902b6bef2d33adf91b)（supports） [ev_76f0e8bb40a574dcddc7fec9](#ev_76f0e8bb40a574dcddc7fec9)（supports）
  依据/推导：该来源为 GitHub 上的微软文档仓库页面，被标注 authority=third_party，因此只作为第三方托管的文档镜像引用，不能称为厂商正式条款；内容与官方 PDF 的“按租户容量包”方向一致。
- **c5_9** [supported] 微软官方 Licensing Guide 明确写出：若客户已购买容量包，则在容量包耗尽前，Copilot Credit 的消耗不会计入按用量付费计量表。 [ev_d87ecf9adc80c628b6a88870](#ev_d87ecf9adc80c628b6a88870)（supports）
  依据/推导：该句位于 ev_d87ecf9… 的 context_before 中，属于同一官方 PDF 同一页面的连续上下文；用于说明容量包与按用量付费的先后抵扣关系，不涉及金额。
- **c6_1** [supported] 微软官方 Copilot Studio 定价页写明：Copilot Studio 以租户级（tenant-wide）许可证形式销售，包含每包 25,000 Copilot Credits 的 Copilot Credit 容量包，标价为每包每月 200.00 美元。 [ev_8a26c7115c3d298fa2df5872](#ev_8a26c7115c3d298fa2df5872)（supports）
  依据/推导：原文逐字给出「tenant-wide license」「25,000 Copilot Credits each」「$200.00 /pack/month」。来源为 microsoft.com/en-us/copilot/pricing/copilot-studio（vendor_official）。原文未说明该 200 美元是否含税、是否需年付承诺，也未说明是否以持有 Microsoft 365 Copilot 许可为前置条件，不作外推。
- **c6_2** [supported] 微软官方《Microsoft Copilot Studio Licensing Guide》（2025 年 11 月版）同样列出：每包每月 200 美元，1 个容量包等于 25,000 Copilot Credits；并写明容量包应按租户预计的月度 Copilot Credits 消耗量购买，未用完的 credits 不结转到下月。 [ev_41d3722308a5dc62841ab0a5](#ev_41d3722308a5dc62841ab0a5)（supports）
  依据/推导：摘录直接给出定价与容量换算，「未结转」由同一页面 context_before 给出。此为厂商官方 PDF 的标价陈述，仅支持标价事实，不能推出已实现收入。
- **c6_3** [supported] 另一份微软官方《Microsoft Copilot Studio Licensing Guide》（PDF 内页标注 October 2026）表述为：每 credit pack 每月 200 美元（按年计费，billed annually），1 个容量包等于 25,000 Copilot Credits。 [ev_2b9e141ce0074ba49ee0902f](#ev_2b9e141ce0074ba49ee0902f)（supports）
  依据/推导：原文为「$200 per credit pack/month (billed annually)」，与 c6_1/c6_2 的 200 美元单价一致，但新增「按年计费」口径。两份官方 PDF 的版本日期标注不同（November 2025 与 October 2026），计费周期的准确表述与生效时点仍需以官方条款确认。
- **c6_4** [supported] 微软官方许可指南的对照表在 Microsoft 365 Copilot 一栏列出「License (capacity pack): 25,000 Copilot Credit /pack」以及「Pre-Purchase Plan: Depends on the tier」，但本轮已校验摘录在金额与折扣处被截断，未见预购计划的具体折扣率。 [ev_2ae85ce7550530d842a58dd6](#ev_2ae85ce7550530d842a58dd6)（supports） [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports）
  依据/推导：仅陈述摘录中出现的内容：容量包的容量描述与预购计划「取决于层级」字样。摘录在「Pre」处截断，不能据此认定官方未公布折扣，也不能填出任何折扣数字。
- **c6_5** [supported] 第三方博客 cloudzero.com 称：按用量付费为每 credit 0.01 美元，经 Microsoft Azure 计费；容量包为每包每月 200 美元（约合 0.008 美元/credit，称比按用量付费便宜约 25%）；预购计划为 Copilot Credit Commit Units（CCCU），按年通过 Azure 预购，最高约 20% 折扣，超额自动走按用量付费。 [ev_edc791ed50dfe849a951d8c6](#ev_edc791ed50dfe849a951d8c6)（supports） [ev_a6c70ef6d47fae8a5fd57c7d](#ev_a6c70ef6d47fae8a5fd57c7d)（supports） [ev_2c9013d57779ffc70891ffd9](#ev_2c9013d57779ffc70891ffd9)（supports）
  依据/推导：三处均出自同一第三方站点（third_party），为作者自述价格表；本轮未在任何厂商官方摘录中检得 0.01 美元/credit 的按用量付费单价或 20% 折扣的官方条款，故仅作第三方陈述保留，不能替代官方条款。
- **c6_6** [supported] 第三方指南 copilot-experts.com 称：面向外部代理部署，另需独立许可证，标价为每 25,000 Copilot Credits 每月 200 美元，按租户级许可证销售；同一来源另称预购容量包可为可预测用量节省最高约 20%。 [ev_bf9bf15cff0c52b2feb4e258](#ev_bf9bf15cff0c52b2feb4e258)（supports） [ev_a4a9a29791f8f6aa493415b6](#ev_a4a9a29791f8f6aa493415b6)（supports） [ev_0f8c290625073de6c006ca00](#ev_0f8c290625073de6c006ca00)（supports）
  依据/推导：均为 copilot-experts.com 第三方指南的语句。其「外部代理部署需独立许可」与「200 美元/25,000 Credits/月」数字与官方容量包单价相同，但在官方摘录中未见「外部部署独立许可」这一单独定价条目，故外部部署的独立许可价格仍属第三方说法。
- **c6_7** [supported] 第三方博客 o365hq.com 称：租户容量包标价为每年 2,400 美元（一次性预付）、按年按月计费 2,520 美元，或单月承诺 240 美元/月；作者工具用的 Copilot Studio User License 为 0 美元。 [ev_e0a050a8f91feb72529bed19](#ev_e0a050a8f91feb72529bed19)（supports）
  依据/推导：第三方转述的标价，来源为 o365hq.com（third_party）。其 2,400 美元/年（即 200 美元/月）与官方 200 美元/包/月一致，但「2,520 美元按年按月计」「240 美元单月承诺」两种口径未在官方摘录中出现，不能等同官方条款。

## 推导

- **c1_6** [supported] 由于 Copilot 席位必须叠加在合格基础计划上，企业客户每启用一个最终用户实际承担的是“基础许可 + Copilot 附加费”的组合成本，而非单一的 30 美元；这抬高了人均增量支出并可能抑制席位的全员铺开。 [ev_43c3e2796f6955566107f0fb](#ev_43c3e2796f6955566107f0fb)（supports） [ev_77397efc85e48e36f7737925](#ev_77397efc85e48e36f7737925)（supports） [ev_ad7a9de3061285191a6ddee2](#ev_ad7a9de3061285191a6ddee2)（supports）
  依据/推导：从“附加项 + 必须已有基础许可”的明确前提推导出组合成本结构；“可能抑制铺开”为基于成本结构的推导，非已观测结果。
- **c2_7** [mixed] 就可核验的官方来源而言，E3/E5/F1/F3、Business Basic/Standard/Premium、Apps for Business/Enterprise 与 Office 365 系列均出现在官方 Learn 许可选项页所列基础计划中；「Copilot Business 仅限 Business 系列」这一更窄的范围只在第三方资料中出现，官方页面反而把 Teams Essentials 等也列入 Copilot Business 条目。 [ev_44c41a1f06ca3f69d980dea4](#ev_44c41a1f06ca3f69d980dea4)（supports） [ev_166813518580a59f6256b9bd](#ev_166813518580a59f6256b9bd)（contradicts）
  依据/推导：由 c2_1–c2_3 与 c2_4 直接比较得出：官方清单覆盖范围确认前一组计划，但官方条目对 Copilot Business 的列示范围（含 Teams Essentials）与第三方“仅 Business 三档+Apps”说法相冲突。保留冲突，不裁决；且官方页条目名为「Microsoft Copilot Business」，与第三方所指 SKU 名称一致性仍待核实。
- **c4_4** [unverified] 就现有证据看，“按每用户每月计费、30 美元/用户/月、需具备合格基础 M365 计划”三项内容均有第三方转述或官方页面（但非该定价页）的间接支撑，然而“microsoft.com 的 M365 Copilot 企业版定价页上明确写明”这一页面级事实仍未被任何已校验摘录直接证实。 [ev_77397efc85e48e36f7737925](#ev_77397efc85e48e36f7737925)（supports） [ev_26e332f23a50ac329142b1d5](#ev_26e332f23a50ac329142b1d5)（supports）
  依据/推导：将内容层面（价格与前提）与出处层面（具体官方页面是否写明）分离：内容有二手支撑，页面归属无原文支撑。缺失证据不得解释为官方页面未写明，故标记 unverified。
- **c5_10** [supported] 按官方指南，两者的收费单位结构不同：Microsoft 365 Copilot 以“每用户每月”的席位标价（并附带一定代理用量），Copilot Studio 的容量以“每租户、每包 25,000 Copilot Credits/月”计费并另有按用量付费与预购计划；终端使用代理的人员并不因此需要单独的按席位 Copilot Studio 许可，只有构建/管理代理的用户需要 0 美元的作者许可。 [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports） [ev_d87ecf9adc80c628b6a88870](#ev_d87ecf9adc80c628b6a88870)（supports） [ev_74051b80b3a8d2af897e5dd6](#ev_74051b80b3a8d2af897e5dd6)（supports）
  依据/推导：由 c5_1–c5_4 直接比较得出：席位计费与租户容量/按用量计费是两套不同计量口径。需注意官方摘录未明确说明“无 M365 Copilot 许可的租户能否单独购买 Copilot Studio 容量包”，该购买前置条件仍不完整。
- **c5_11** [supported] 既然 Copilot Studio 的容量按租户汇总、以信用点消耗计量，企业扩展代理使用时的边际成本取决于代理调用量而非启用人数，这使得代理规模化的成本可预测性低于按席位定价的 Copilot 席位，企业需以容量包+按用量付费兜底的方式管理超额风险。 [ev_a6050c902b6bef2d33adf91b](#ev_a6050c902b6bef2d33adf91b)（supports） [ev_d1dc73ce2233ff3803f9f60c](#ev_d1dc73ce2233ff3803f9f60c)（supports） [ev_74051b80b3a8d2af897e5dd6](#ev_74051b80b3a8d2af897e5dd6)（supports）
  依据/推导：从“租户级信用点计量+超额需按用量付费兜底”推导出成本随用量波动；这是基于计费结构的推导，非已观测的企业支出数据。
- **c6_8** [mixed] 在容量包单价上，官方定价页、两份官方许可指南与第三方来源方向一致，均为 200 美元对应 25,000 Copilot Credits 的一包一个月；差异集中在计费周期口径：官方 November 2025 版只写 /pack/month，October 2026 版写 /month (billed annually)，第三方则给出年付 2,400 美元与按月计 2,520/240 美元的多种口径。 [ev_8a26c7115c3d298fa2df5872](#ev_8a26c7115c3d298fa2df5872)（supports） [ev_2b9e141ce0074ba49ee0902f](#ev_2b9e141ce0074ba49ee0902f)（supports） [ev_e0a050a8f91feb72529bed19](#ev_e0a050a8f91feb72529bed19)（supports） [ev_41d3722308a5dc62841ab0a5](#ev_41d3722308a5dc62841ab0a5)（contradicts）
  依据/推导：由 c6_1–c6_3、c6_7 对比得出：单价（200 美元/25,000 Credits）无冲突，但计费周期存在口径差异，且两份官方 PDF 的日期标注本身不一致。按规则保留冲突，不裁决，不将第三方年价视作官方条款。
- **c6_9** [mixed] 按用量付费的每 credit 单价、预购计划的折扣条件与外部代理部署的独立许可价格，本轮仅在第三方来源中出现（0.01 美元/credit、最高约 20% 折扣、200 美元/25,000 Credits/月的外部部署独立许可），官方摘录未覆盖这些金额与折扣条款，故无法以官方原文核验。 [ev_edc791ed50dfe849a951d8c6](#ev_edc791ed50dfe849a951d8c6)（supports） [ev_bf9bf15cff0c52b2feb4e258](#ev_bf9bf15cff0c52b2feb4e258)（supports） [ev_2ae85ce7550530d842a58dd6](#ev_2ae85ce7550530d842a58dd6)（contradicts）
  依据/推导：这是证据覆盖层面的推导：官方摘录在预购金额与折扣处被截断（c6_4），三个具体金额/折扣均只有 third_party 支撑。缺失官方原文不等于官方未公布，故不能声称官方无此价格，也不能将第三方数字升格为官方标价。

## 商业判断

- **c5_12** [supported] 就收入含义而言，席位模式使微软的 Copilot 收入随启用用户数线性增长且较可预测，而 Copilot Studio 的租户容量包+按用量付费模式使收入与客户代理实际消耗挂钩，更接近用量型收入；两者叠加可在同一客户上形成“席位订阅+消费型容量”的双层收入结构。 [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports） [ev_74051b80b3a8d2af897e5dd6](#ev_74051b80b3a8d2af897e5dd6)（supports） [ev_7a665bca240fe219b0300714](#ev_7a665bca240fe219b0300714)（supports）
  依据/推导：基于已陈述的两种计费结构的商业判断，不是微软披露的收入或利润数据；标价不能推出已实现收入，用量型收入的实现取决于实际消耗。
- **c6_10** [supported] 从计费结构看，容量包以「每租户、每包 25,000 Credits/月、200 美元」为标价、未用 credits 不结转，且官方建议以按用量付费作超额兜底，意味着 Copilot Studio 的客户支出与代理实际信用点消耗挂钩；这使微软在代理侧的收费更接近用量型而非席位型，但标价本身不能推出已实现收入或利润。 [ev_41d3722308a5dc62841ab0a5](#ev_41d3722308a5dc62841ab0a5)（supports） [ev_8a26c7115c3d298fa2df5872](#ev_8a26c7115c3d298fa2df5872)（supports）
  依据/推导：基于官方标价与「不结转+超额走按用量付费」的计费规则作出商业判断；本轮无微软披露的 Copilot Studio 实际收入/消耗数据，不将定价等同于收入。

## 待验证假设

- **c1_7** [unverified] 若企业按实际使用率精细分配 Copilot 席位（而非全员配发），微软来自 Copilot 的每客户增量收入增长可能慢于席位名义价格所暗示的水平。 [ev_43c3e2796f6955566107f0fb](#ev_43c3e2796f6955566107f0fb)（supports）
  依据/推导：第三方提到为不使用功能的员工分配席位是主要隐性成本，但本轮无使用率/激活率数据，也无微软官方收入披露，故仅为待验证假设。
- **c2_8** [unverified] 300 席上限可能出自 Microsoft 365 管理中心的订阅目录/购买页描述或 Business 系列计划自身 300 用户上限的继承，而非许可选项文章正文；需以官方目录或产品条款原文验证。 [ev_166813518580a59f6256b9bd](#ev_166813518580a59f6256b9bd)（supports） [ev_ae4581162fef64fba033cc93](#ev_ae4581162fef64fba033cc93)（supports）
  依据/推导：第三方称“微软目录描述”且把上限类比 Business 计划 300 许可上限，属推断性表述；本轮无官方目录/条款原文，无法证实，仅作待验证假设，不能用于关闭缺口。
- **c5_13** [unverified] 若企业已持有 Microsoft 365 Copilot 许可，其包含的内部代理用量额度可能降低客户另行购买 Copilot Studio 容量包的意愿，从而使微软在既有 Copilot 客户上的代理侧增量收入低于独立容量包标价所暗示的水平。 [ev_5a440717841727e42686e122](#ev_5a440717841727e42686e122)（supports） [ev_010bb475f18cd0facb1d4350](#ev_010bb475f18cd0facb1d4350)（supports）
  依据/推导：官方对照表列有“Included agent usage”，第三方称内部代理使用已包含在 M365 Copilot 许可内，但包含额度的具体数量、超限后的计费以及客户实际购买行为均无证据，故仅为待验证假设。
- **c6_11** [unverified] 若客户已持有 Microsoft 365 Copilot 许可并获得「Included agent usage」额度，其可用于内部代理的包含用量可能减少客户另行购买容量包或预购档位的规模，使微软在既有 Copilot 客户上的容量包收入低于按代理总消耗量估算的水平。 [ev_2ae85ce7550530d842a58dd6](#ev_2ae85ce7550530d842a58dd6)（supports） [ev_a6c70ef6d47fae8a5fd57c7d](#ev_a6c70ef6d47fae8a5fd57c7d)（supports）
  依据/推导：官方对照表只在 Microsoft 365 Copilot 行出现「Included agent usage」，额度数量、超限计费规则与客户实际采购行为均无证据，故为待验证假设，不能用于关闭缺口。

## 证据缺口

- gap0 [open] Microsoft 365 Copilot 与 Copilot Studio 面向的企业使用者、收费单位和购买前提有何区别？这些差异可能如何影响企业客户扩展使用和微软的收入来源？优先使用官方资料；将价格与许可事实、基于事实的推导、商业判断和仍待验证假设明确区分，不把产品定价直接当成已实现收入或利润。
- gap1 [open] 需微软官方 Microsoft 365 Copilot 许可/价目页（官方 PDF 或产品条款）原文，以核验按席位计费、企业版 30 美元/用户/月与 Copilot Business 约 21 美元/用户/月的官方标价及版本与生效时间；本轮仅依赖第三方转述与社区帖。
- gap2 [open] 需微软官方合格基础许可证完整清单（含 E3/E5/F1/F3、Business 系列、Apps、Office 365 与单件 SKU）及 Copilot Business 300 席上限的官方条款来源；目前该细节仅见于第三方博客。
- gap3 [open] 需微软官方 Copilot Studio 定价页/产品条款原文，核验以下金额与计费规则：容量包标价（第三方称 2,400 美元/年或 240 美元/月）、每 25,000 Copilot Credits 的按用量付费单价、外部代理部署的独立许可价格（第三方称 200 美元/25,000 Credits/月）、预购计划折扣与 Copilot Credit 各能力的兑换费率；当前官方 PDF 摘录在这些金额处被截断。
- gap4 [open] 需微软官方条款原文说明：购买 Copilot Studio 容量包或按用量付费是否以持有 Microsoft 365 Copilot 许可或合格基础 Microsoft 365 计划为前提，以及“包含于 M365 Copilot 许可的内部代理用量额度”具体为多少、超限后如何计费；目前仅有官方对照表的“Included agent usage”字样与第三方说法，购买前置条件未被官方条款完整覆盖。
- gap5 [open] 需微软官方文档确认 Copilot Studio 计费单位从按消息切换为 Copilot Credits 的生效时间与适用范围（第三方称 2025 年 9 月起）；本轮官方 PDF 不同版本日期标注不一（November 2025 与 October 2026），版本与生效时间需以官方条款核实。

## 问题与检索记录

- q0 / 第 0 轮 / 缺口 初始问题：Microsoft 365 Copilot 与 Copilot Studio 面向的企业使用者、收费单位和购买前提有何区别？这些差异可能如何影响企业客户扩展使用和微软的收入来源？优先使用官方资料；将价格与许可事实、基于事实的推导、商业判断和仍待验证假设明确区分，不把产品定价直接当成已实现收入或利润。
- q1 / 第 1 轮 / 缺口 gap0：Microsoft 365 Copilot 面向企业最终用户时的许可与收费单位是什么（按人/按席位），其购买前提要求哪些基础许可？
- q2 / 第 2 轮 / 缺口 gap2：微软官方许可文档中，Microsoft 365 Copilot（含 Copilot Business）的合格基础许可证清单具体包含哪些计划，是否包含 E3/E5/F1/F3、Business Basic/Standard/Premium、Apps for business/enterprise 与 Office 365 系列，以及 Copilot Business 是否存在 300 席上限？
- q3 / 第 3 轮 / 缺口 gap1：微软官方 Microsoft 365 Copilot 产品页/价目页是否公开标明企业版为每用户每月 30 美元、Copilot Business 为每用户每月约 21 美元（年付），并说明按席位计费与适用版本？
  Tavily search1：Microsoft 365 Copilot pricing per user；结果 5；错误 无
- q4 / 第 4 轮 / 缺口 gap1：在微软官方 microsoft.com 的 Microsoft 365 Copilot 企业版定价页上，是否明确写明按每用户每月计费、价格为 30 美元/用户/月，并说明需要具备合格的基础 Microsoft 365 计划？
  Tavily search2：Microsoft 365 Copilot Enterprise pricing per user；结果 5；错误 无
- q5 / 第 5 轮 / 缺口 gap0：微软官方对 Copilot Studio 的计费单位（按消息包/租户容量还是按用户席位）、定价层级以及购买前提（是否必须拥有 Microsoft 365 Copilot 许可）是如何规定的？它与 Microsoft 365 Copilot 按席位叠加基础计划的模式有何不同？
- q6 / 第 6 轮 / 缺口 gap3：微软官方 Copilot Studio 定价页或产品条款中，容量包（25,000 Copilot Credits/包）的官方标价、按用量付费的每单位 Credit 单价、外部代理部署的独立许可价格，以及预购计划的折扣条件分别是什么？
  Tavily search3：Copilot Studio pricing capacity pack credits；结果 5；错误 无
- q7 / 第 7 轮 / 缺口 gap4：微软官方条款是否规定购买 Copilot Studio 容量包或启用按用量付费，必须以持有 Microsoft 365 Copilot 许可或某个合格基础 Microsoft 365 计划为前提？Microsoft 365 Copilot 许可“包含的代理用量”具体额度及超限计费方式是什么？
  Tavily search4：Copilot Studio prerequisites Microsoft 365 Copilot license capacity pack；结果 5；错误 无

## 原文摘录与追溯

<a id="ev_43c3e2796f6955566107f0fb"></a>
### ev_43c3e2796f6955566107f0fb

> A Microsoft 365 Copilot license runs about $30 per user per month on the enterprise plan, but that sticker price is the easy part of the decision. You can’t buy Copilot on its own. It’s an add-on that sits on top of a qualifying Microsoft 365 plan, so the seat you’re really paying for is the base license plus Copilot.

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q1 → 分块 chk_0a86d3d8c098bd281864d073_0 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [109, 428)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_a1dd93632d4ee6ca432f71f9"></a>
### ev_a1dd93632d4ee6ca432f71f9

> A Microsoft 365 Copilot Business license is built for organizations under 300 seats sitting on a Business plan. The enterprise Microsoft 365 Copilot add-on is for E3 and E5 tenants and carries no seat ceiling.

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q1 → 分块 chk_0a86d3d8c098bd281864d073_4080 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [4106, 4315)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_4dc8e527a95c4faf0cf67ac8"></a>
### ev_4dc8e527a95c4faf0cf67ac8

> Base plan required Business Basic, Standard, or Premium E3, E5, or Business Standard/Premium Seat cap Up to 300 ✓ No cap Price per user/month ~$21 (annual) $30 (annual)

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q1 → 分块 chk_0a86d3d8c098bd281864d073_4080 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [4368, 4536)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_5f9c6c0b1525ac6058573928"></a>
### ev_5f9c6c0b1525ac6058573928

> Copilot for Microsoft 365 uses fixed per-user licensing. Copilot Studio uses consumption billing through Copilot Credits.

来源：Microsoft Copilot vs Copilot Studio + Cowork: Key Differences (2026) — https://www.hso.com/blog/microsoft-copilot-vs-studio/

类型：web；读取时间：2026-10-19T08:22:57.302469+00:00；截断：False

问题 q1 → 分块 chk_1f444fdde6bc33ac0db439f8_6630 → 来源 src_1f444fdde6bc33ac0db439f8；清洗后字符 [6776, 6897)

SHA-256：`65de4d548f8e19533fd7392baf56d4b9982c6993445097ad37bed59c7e536b92`；范围：<main> element; characters 0-20914 of 20914

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.hso.com/blog/microsoft-copilot-vs-studio
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_cb240676d64d8516aab9c323"></a>
### ev_cb240676d64d8516aab9c323

> Organizations pay a monthly subscription per user. Prerequisites include Microsoft 365 E3, E5, Business Standard, or Business Premium. Cost: $30 per user per month (as of May 2026)

来源：Microsoft Copilot vs Copilot Studio + Cowork: Key Differences (2026) — https://www.hso.com/blog/microsoft-copilot-vs-studio/

类型：web；读取时间：2026-10-19T08:22:57.302469+00:00；截断：False

问题 q1 → 分块 chk_1f444fdde6bc33ac0db439f8_6630 → 来源 src_1f444fdde6bc33ac0db439f8；清洗后字符 [6936, 7116)

SHA-256：`65de4d548f8e19533fd7392baf56d4b9982c6993445097ad37bed59c7e536b92`；范围：<main> element; characters 0-20914 of 20914

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.hso.com/blog/microsoft-copilot-vs-studio
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_77397efc85e48e36f7737925"></a>
### ev_77397efc85e48e36f7737925

> It’s a paid, per-user add-on to an eligible Microsoft 365 subscription that turns on Copilot inside the Office apps and work-based Copilot Chat grounded in your tenant’s data. It costs $30 per user per month on the enterprise plan and requires a qualifying base license underneath.

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q1 → 分块 chk_0a86d3d8c098bd281864d073_8160 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [8476, 8757)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_abf036c5a23bda035de11180"></a>
### ev_abf036c5a23bda035de11180

> None include the paid Copilot experience by default. Microsoft 365 E3, E5, F3, and Business Basic, Standard, or Premium qualify you to add it.

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q1 → 分块 chk_0a86d3d8c098bd281864d073_8670 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [8803, 8945)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_a65486f21fa17854e6c1f967"></a>
### ev_a65486f21fa17854e6c1f967

> No. Copilot is sold only as an add-on to an eligible base plan. If a user isn’t on a qualifying subscription, you upgrade the base plan first, then add Copilot.

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q1 → 分块 chk_0a86d3d8c098bd281864d073_8670 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [9090, 9250)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_ad7a9de3061285191a6ddee2"></a>
### ev_ad7a9de3061285191a6ddee2

> Microsoft 365 Copilot is an add-on license, therefore to assign the add-on, there needs to be a base license first.

来源：M365 Copilot requirements explained! | Microsoft Community Hub — https://techcommunity.microsoft.com/discussions/microsoft-copilot/m365-copilot-requirements-explained/4400231

类型：web；读取时间：2026-10-19T08:26:38.756547+00:00；截断：False

问题 q1 → 分块 chk_33f6756b411fd62861cb8c0b_1530 → 来源 src_33f6756b411fd62861cb8c0b；清洗后字符 [1881, 1996)

SHA-256：`9bfedd403479c15040ba5d3ddbff161fdd3c62976c1d65b2e10e1cdb54532666`；范围：<main> element; characters 0-5498 of 5498

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://techcommunity.microsoft.com/discussions/microsoft-copilot/m365-copilot-requirements-explained/4400231
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_26e332f23a50ac329142b1d5"></a>
### ev_26e332f23a50ac329142b1d5

> Microsoft 365 Copilot may not be available for all markets and languages. To purchase, customers must have a qualifying Microsoft 365 plan for enterprise or business.

来源：Microsoft Copilot Studio Plans and Pricing — https://www.microsoft.com/en-us/copilot/pricing/copilot-studio

类型：web；读取时间：2026-10-19T08:23:18.966505+00:00；截断：False

问题 q1 → 分块 chk_0974f6cd66d2bc4ca55c8219_1020 → 来源 src_0974f6cd66d2bc4ca55c8219；清洗后字符 [1087, 1253)

SHA-256：`5c2c49105b6ac9c095aedd95af5f2f3133be5bf6bb7d17561ab15184a704fb32`；范围：<main> element; characters 0-8971 of 8971

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.microsoft.com/en-us/copilot/pricing/copilot-studio
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_5d2c5aaa93a0fff55de25039"></a>
### ev_5d2c5aaa93a0fff55de25039

> Microsoft 365 Copilot is sold three ways in 2026: a per-user add-on on top of a qualifying plan, a metered pay-as-you-go option for people without a seat, and Copilot Studio capacity for the agents you build yourself.

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q1 → 分块 chk_ba995cac346030f043dc84c6_0 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [325, 542)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_37d9dbe02b1950137794dea6"></a>
### ev_37d9dbe02b1950137794dea6

> Microsoft 365 Copilot is an add-on license, and Microsoft's license-options article lists more qualifying plans than most people assume.

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q1 → 分块 chk_ba995cac346030f043dc84c6_510 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [726, 862)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_bcff011e04cd21c7cb00be57"></a>
### ev_bcff011e04cd21c7cb00be57

> For the Microsoft 365 Copilot SKU: Microsoft 365 E5, E3, F1 and F3; Business Basic, Standard and Premium; Apps for business and for enterprise; Office 365 E1, E3, E5 and F3; Teams Essentials, Enterprise and EEA; Exchange Kiosk and Plans 1 and 2; S

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q1 → 分块 chk_ba995cac346030f043dc84c6_510 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [863, 1110)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_955cafd059b1d3ef325d1142"></a>
### ev_955cafd059b1d3ef325d1142

> §Microsoft Copilot Business§ Microsoft 365 Bus

来源：License Options for Microsoft Copilot | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-licensing

类型：web；读取时间：2026-10-19T08:28:39.841081+00:00；截断：False

问题 q2 → 分块 chk_6cc784f8750c8103456cd299_1530 → 来源 src_6cc784f8750c8103456cd299；清洗后字符 [2084, 2130)

SHA-256：`c4df1e9e82f94278d2aaef4f5f7716b52d1663a7e5b5511f7aab0a53b9c11779`；范围：<main> element; characters 0-6984 of 6984

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-licensing
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_44c41a1f06ca3f69d980dea4"></a>
### ev_44c41a1f06ca3f69d980dea4

> §Microsoft Copilot Business§ Microsoft 365 Business Premium Microsoft 365 Business Standard Microsoft 365 Business Basic Microsoft 365 Apps for Business Microsoft Teams Essentials §Microsoft Copilot§ Microsoft 365 plans: Microsoft 365 E7 (includes Microsoft Copilot) Microsoft 365 E5 Microsoft 365 E3 Microsoft 365 F1 Microsoft 365 F3 Microsoft 365 Business Premium Microsoft 365 Business Standard Microsoft 365 Business Basic Microsoft 365 Apps for Enterprise Microsoft 365 Apps for Business Office 365 plans: Office 365 E5 Office 365 E3 Office 365 E1 Off

来源：License Options for Microsoft Copilot | Microsoft Learn — https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-licensing

类型：web；读取时间：2026-10-19T08:28:39.841081+00:00；截断：False

问题 q2 → 分块 chk_6cc784f8750c8103456cd299_2040 → 来源 src_6cc784f8750c8103456cd299；清洗后字符 [2084, 2640)

SHA-256：`c4df1e9e82f94278d2aaef4f5f7716b52d1663a7e5b5511f7aab0a53b9c11779`；范围：<main> element; characters 0-6984 of 6984

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://learn.microsoft.com/en-us/microsoft-365/copilot/microsoft-365-copilot-licensing
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_166813518580a59f6256b9bd"></a>
### ev_166813518580a59f6256b9bd

> The smaller SKU, Microsoft 365 Copilot Business, attaches only to Microsoft 365 Business Basic, Business Standard, Business Premium and Apps for business, and Microsoft's catalog description caps it at 300 seats, the same ceiling as the Business plans, which our 300-license limit guide explains.

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q2 → 分块 chk_ba995cac346030f043dc84c6_1020 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [1274, 1570)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_ae4581162fef64fba033cc93"></a>
### ev_ae4581162fef64fba033cc93

> Copilot Business attaches only to the Business plans and is capped at 300 seats.

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q2 → 分块 chk_ba995cac346030f043dc84c6_9690 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [9788, 9868)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_8c2da60f81aedf9a0ccbd367"></a>
### ev_8c2da60f81aedf9a0ccbd367

> Microsoft’s minimum requirements documentation lists the eligible base subscriptions: Enterprise : Microsoft 365 E3, E5, and F3, plus the Office 365 E1, E3, and E5 equivalents Business : Microsoft 365 Business Basic, Business Standard, and Business Premium Frontline and government : F-tier and GCC plans, with some capabil

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q2 → 分块 chk_0a86d3d8c098bd281864d073_3060 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [3337, 3660)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_65d8291d35618ac53f28d8dc"></a>
### ev_65d8291d35618ac53f28d8dc

> A Microsoft 365 Copilot Business license is built for organizations under 300 seats sitting on a Business plan. The enterprise Microsoft 365 Copilot add-on is for E3 and E5 tenants and carries no seat ceiling. Copilot Business Microsoft 365 Copilot (enterprise) Base plan required Business Basic, Standard, or Premium E3, E5, or Business Standard/Premium Seat cap Up to 300 ✓ No cap Price per user/month ~$21 (annual) $30 (annual) Best fit SMBs standardizing on Business plans Enterprises and large, mixed tenants

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q2 → 分块 chk_0a86d3d8c098bd281864d073_4080 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [4106, 4619)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_71d7fa6b4619c6ad40ffcc4b"></a>
### ev_71d7fa6b4619c6ad40ffcc4b

> For enterprise organizations, the Microsoft 365 Copilot add-on is $30 per user per month , on an annual commitment, added to a base plan like Microsoft 365 E3, E5, Business Standard, or Business Premium.

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q3 → 分块 chk_0a86d3d8c098bd281864d073_511 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [868, 1071)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_a7bd00cc78bd13b3459627d8"></a>
### ev_a7bd00cc78bd13b3459627d8

> The enterprise Microsoft 365 Copilot add-on is for E3 and E5 tenants and carries no seat ceiling. Copilot Business Microsoft 365 Copilot (enterprise) Base plan required Business Basic, Standard, or Premium E3, E5, or Business Standard/Premium Seat cap Up to 300 ✓ No cap Price per user/month ~$21 (annual) $30 (annual)

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q3 → 分块 chk_0a86d3d8c098bd281864d073_4080 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [4218, 4536)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_74be97792a22799d0ea44e1d"></a>
### ev_74be97792a22799d0ea44e1d

> The standard enterprise price for Microsoft 365 Copilot is $30 per user, per month , billed annually.

来源：Microsoft Copilot Pricing Explained: Plans, Cost & Licensing (2026 Guide) — https://copilot-experts.com/microsoft-copilot-pricing-guide/

类型：web；读取时间：2026-10-19T08:34:53.971800+00:00；截断：False

问题 q3 → 分块 chk_ac5bf6d7ca3223d80201c6bc_8670 → 来源 src_ac5bf6d7ca3223d80201c6bc；清洗后字符 [8757, 8858)

SHA-256：`7fe833d081a4bedc364caa3ac22c186729714bd1900164aa122d9ec96c067acb`；范围：<body> element; characters 0-41267 of 41267

获取链：运行 23c904aac0c6 → 问题 q3 → 搜索 search1 → https://copilot-experts.com/microsoft-copilot-pricing-guide
检索词：Microsoft 365 Copilot pricing per user；当时的问题：微软官方 Microsoft 365 Copilot 产品页/价目页是否公开标明企业版为每用户每月 30 美元、Copilot Business 为每用户每月约 21 美元（年付），并说明按席位计费与适用版本？

<a id="ev_ed396faee6afd96e8864ddb1"></a>
### ev_ed396faee6afd96e8864ddb1

> Note: From 1 December 2025, Microsoft permanently reduced the Copilot Business (SMB) rate from $30 to $21/user/month for organizations under 300 users.

来源：Microsoft Copilot Pricing Explained: Plans, Cost & Licensing (2026 Guide) — https://copilot-experts.com/microsoft-copilot-pricing-guide/

类型：web；读取时间：2026-10-19T08:34:53.971800+00:00；截断：False

问题 q3 → 分块 chk_ac5bf6d7ca3223d80201c6bc_8670 → 来源 src_ac5bf6d7ca3223d80201c6bc；清洗后字符 [8975, 9126)

SHA-256：`7fe833d081a4bedc364caa3ac22c186729714bd1900164aa122d9ec96c067acb`；范围：<body> element; characters 0-41267 of 41267

获取链：运行 23c904aac0c6 → 问题 q3 → 搜索 search1 → https://copilot-experts.com/microsoft-copilot-pricing-guide
检索词：Microsoft 365 Copilot pricing per user；当时的问题：微软官方 Microsoft 365 Copilot 产品页/价目页是否公开标明企业版为每用户每月 30 美元、Copilot Business 为每用户每月约 21 美元（年付），并说明按席位计费与适用版本？

<a id="ev_62720d3836860a05f1745c90"></a>
### ev_62720d3836860a05f1745c90

> The paid business plan (Copilot Business) for SMBs under 300 users starts from $18/user/month (promotional annual rate through September 2026), with standard pricing at $21/user/month. The enterprise add-on for larger organizations is $30/user/month.

来源：Microsoft Copilot Pricing Explained: Plans, Cost & Licensing (2026 Guide) — https://copilot-experts.com/microsoft-copilot-pricing-guide/

类型：web；读取时间：2026-10-19T08:34:53.971800+00:00；截断：False

问题 q3 → 分块 chk_ac5bf6d7ca3223d80201c6bc_33660 → 来源 src_ac5bf6d7ca3223d80201c6bc；清洗后字符 [34007, 34257)

SHA-256：`7fe833d081a4bedc364caa3ac22c186729714bd1900164aa122d9ec96c067acb`；范围：<body> element; characters 0-41267 of 41267

获取链：运行 23c904aac0c6 → 问题 q3 → 搜索 search1 → https://copilot-experts.com/microsoft-copilot-pricing-guide
检索词：Microsoft 365 Copilot pricing per user；当时的问题：微软官方 Microsoft 365 Copilot 产品页/价目页是否公开标明企业版为每用户每月 30 美元、Copilot Business 为每用户每月约 21 美元（年付），并说明按席位计费与适用版本？

<a id="ev_5d151648c373cbe3ec065244"></a>
### ev_5d151648c373cbe3ec065244

> Microsoft 365 Copilot Business serves organizations with up to 300 seats on a qualifying Microsoft 365 business plan. Copilot price: $21 per user per month with an annual commitment (standard rate).

来源：Microsoft Copilot Pricing 2026: Plans, Costs, and Total Cost of Ownership | The GoSearch Blog — https://www.gosearch.ai/blog/microsoft-copilot-pricing/

类型：web；读取时间：2026-10-19T08:35:06.473917+00:00；截断：False

问题 q3 → 分块 chk_0a009e6cf67b8f9a039acdd2_8160 → 来源 src_0a009e6cf67b8f9a039acdd2；清洗后字符 [8462, 8660)

SHA-256：`f8e66b7736eec780d00704e605d29cf9e7792f4c495980f18fd18f60e8c96298`；范围：<body> element; characters 0-29481 of 29481

获取链：运行 23c904aac0c6 → 问题 q3 → 搜索 search1 → https://www.gosearch.ai/blog/microsoft-copilot-pricing
检索词：Microsoft 365 Copilot pricing per user；当时的问题：微软官方 Microsoft 365 Copilot 产品页/价目页是否公开标明企业版为每用户每月 30 美元、Copilot Business 为每用户每月约 21 美元（年付），并说明按席位计费与适用版本？

<a id="ev_a3c783fa2d8ad8fe8173a177"></a>
### ev_a3c783fa2d8ad8fe8173a177

> Microsoft 365 Copilot Business Small and midsize business users, up to 300 seats $21/user/month annual ($18 promo through Dec 31, 2026); $25.20/user/month monthly Qualifying M365 business license

来源：Microsoft Copilot Pricing 2026: Plans, Costs, and Total Cost of Ownership | The GoSearch Blog — https://www.gosearch.ai/blog/microsoft-copilot-pricing/

类型：web；读取时间：2026-10-19T08:35:06.473917+00:00；截断：False

问题 q3 → 分块 chk_0a009e6cf67b8f9a039acdd2_6630 → 来源 src_0a009e6cf67b8f9a039acdd2；清洗后字符 [6672, 6867)

SHA-256：`f8e66b7736eec780d00704e605d29cf9e7792f4c495980f18fd18f60e8c96298`；范围：<body> element; characters 0-29481 of 29481

获取链：运行 23c904aac0c6 → 问题 q3 → 搜索 search1 → https://www.gosearch.ai/blog/microsoft-copilot-pricing
检索词：Microsoft 365 Copilot pricing per user；当时的问题：微软官方 Microsoft 365 Copilot 产品页/价目页是否公开标明企业版为每用户每月 30 美元、Copilot Business 为每用户每月约 21 美元（年付），并说明按席位计费与适用版本？

<a id="ev_61755e1b2a2c6509b0363a8c"></a>
### ev_61755e1b2a2c6509b0363a8c

> Microsoft 365 Copilot Enterprise Enterprise users $30/user/month annual Qualifying enterprise license, such as E3 or E5

来源：Microsoft Copilot Pricing 2026: Plans, Costs, and Total Cost of Ownership | The GoSearch Blog — https://www.gosearch.ai/blog/microsoft-copilot-pricing/

类型：web；读取时间：2026-10-19T08:35:06.473917+00:00；截断：False

问题 q3 → 分块 chk_0a009e6cf67b8f9a039acdd2_6630 → 来源 src_0a009e6cf67b8f9a039acdd2；清洗后字符 [6913, 7032)

SHA-256：`f8e66b7736eec780d00704e605d29cf9e7792f4c495980f18fd18f60e8c96298`；范围：<body> element; characters 0-29481 of 29481

获取链：运行 23c904aac0c6 → 问题 q3 → 搜索 search1 → https://www.gosearch.ai/blog/microsoft-copilot-pricing
检索词：Microsoft 365 Copilot pricing per user；当时的问题：微软官方 Microsoft 365 Copilot 产品页/价目页是否公开标明企业版为每用户每月 30 美元、Copilot Business 为每用户每月约 21 美元（年付），并说明按席位计费与适用版本？

<a id="ev_a9509426fa1e28de1db7d64b"></a>
### ev_a9509426fa1e28de1db7d64b

> Yes. Copilot for Microsoft 365 requires a $30 per user monthly subscription. Microsoft introduced a new Copilot Business SKU for organizations with fewer than 300 users, priced at $21/user/month.

来源：Microsoft Copilot vs Copilot Studio + Cowork: Key Differences (2026) — https://www.hso.com/blog/microsoft-copilot-vs-studio/

类型：web；读取时间：2026-10-19T08:22:57.302469+00:00；截断：False

问题 q3 → 分块 chk_1f444fdde6bc33ac0db439f8_18360 → 来源 src_1f444fdde6bc33ac0db439f8；清洗后字符 [18448, 18643)

SHA-256：`65de4d548f8e19533fd7392baf56d4b9982c6993445097ad37bed59c7e536b92`；范围：<main> element; characters 0-20914 of 20914

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.hso.com/blog/microsoft-copilot-vs-studio
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_3f0153d66ec7a2ad996d1d35"></a>
### ev_3f0153d66ec7a2ad996d1d35

> Microsoft 365 Copilot Business: $252 per user per year paid up front ($21 a month), $264.60 billed monthly ($22.05 a month), or $25.20 a month on a one-month commitment.

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q3 → 分块 chk_ba995cac346030f043dc84c6_2041 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [2122, 2291)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_47484136605be3d4f1ab5784"></a>
### ev_47484136605be3d4f1ab5784

> Microsoft 365 Copilot Business (add-on) ~$21 / user / month, annual (promo $18 ended June 30, 2026) Organizations under 300 seats

来源：Microsoft 365 Copilot license: cost and who needs one — https://www.orchestry.com/insight/microsoft-365-copilot-license-cost

类型：web；读取时间：2026-10-19T08:28:37.267123+00:00；截断：False

问题 q3 → 分块 chk_0a86d3d8c098bd281864d073_1530 → 来源 src_0a86d3d8c098bd281864d073；清洗后字符 [1648, 1777)

SHA-256：`56dd0ab9a55b52b513458d39cf9b9cbf1b90710e50ff9410c4aa418c6ef274d3`；范围：<main> element; characters 0-11135 of 11135

获取链：运行 d968652bc210 → 问题 q7 → 搜索 search6 → https://www.orchestry.com/insight/microsoft-365-copilot-license-cost
检索词：Microsoft 365 Copilot license options eligible base licenses；当时的问题：微软官方 license-options 文章或 Microsoft Product Terms 是否以正式文档列出 Microsoft 365 Copilot 的合格基础许可 SKU 清单（是否包含 F1/F3、Office 365 计划、教育版 A1/A3/A5 及 Apps for Business/Enterprise）？

<a id="ev_5a440717841727e42686e122"></a>
### ev_5a440717841727e42686e122

> Microsoft 365 Copilot $30 per user/month Included agent usage1 Pay-as-you-go: unlimited2 License (capacity pack): 25,000 Copilot Credit /pack3 Pre

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q5 → 分块 chk_c68aacefe8ad1e6fd48eeabb_13260 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [13714, 13860)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_d87ecf9adc80c628b6a88870"></a>
### ev_d87ecf9adc80c628b6a88870

> Copilot Studio License Offer Summary SKU Name Microsoft Copilot Studio Billing Configuration Per Tenant 1 Capacity Pack 25,000 Copilot Credits per month The Microsoft Copilot Studio license subscription can be provisioned here. • Creating and Managing agents: A Copilot Studio User License ($0) is required for each user that builds and manages agents with Copilot Studio.

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf

类型：web；读取时间：2026-10-19T08:24:22.210421+00:00；截断：False

问题 q5 → 分块 chk_059af1d4b3d5bf109a6dbb14_27540 → 来源 src_059af1d4b3d5bf109a6dbb14；清洗后字符 [27746, 28118)

SHA-256：`ffd7d5a631e01bb670aef2bd8fa6ae234dcc34b5d3770ccd90bb71beba67c590`；范围：PDF pages 1-21 of 21; characters 0-38941 of 38941

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_74051b80b3a8d2af897e5dd6"></a>
### ev_74051b80b3a8d2af897e5dd6

> As users interact with Copilot Studio agents, or agents perform tasks on behalf of users, they consume Copilot Credits. Copilot Credits are the common currency across Copilot Studio capabilities and are available via the Microsoft Copilot Studio pay-as-you-go meter, the Microsoft Copilot Studio license (i.e., Copilot Credit capacity pack) and the

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q5 → 分块 chk_c68aacefe8ad1e6fd48eeabb_3571 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [3821, 4169)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_a6050c902b6bef2d33adf91b"></a>
### ev_a6050c902b6bef2d33adf91b

> At the start of every monthly billing period, your 25,000 credits are replenished. You must have pay-as-you-go billing active as a safety net each month to cover any excess usage. Alternatively, you can top up with more capacity packs.

来源：microsoft-365-docs/copilot/pay-as-you-go/copilot-capacity-packs.md at public · MicrosoftDocs/microsoft-365-docs · GitHub — https://github.com/MicrosoftDocs/microsoft-365-docs/blob/public/copilot/pay-as-you-go/copilot-capacity-packs.md

类型：web；读取时间：2026-10-19T08:29:15.341631+00:00；截断：False

问题 q5 → 分块 chk_f8f12eda37b72bebb9444fce_4590 → 来源 src_f8f12eda37b72bebb9444fce；清洗后字符 [4766, 5001)

SHA-256：`a95cb3d5b68b10d3964f7df866ebf3d53a12a749e413633907d8f91d3cbb7bf3`；范围：<main> element; characters 0-13057 of 13057

获取链：运行 d968652bc210 → 问题 q8 → 搜索 search7 → https://github.com/MicrosoftDocs/microsoft-365-docs/blob/public/copilot/pay-as-you-go/copilot-capacity-packs.md
检索词：Copilot Studio capacity pack Azure subscription requirement；当时的问题：微软官方文档是否明确 Copilot Studio 容量包（Copilot Credit 容量包，每包 25,000 信用）与预购 Commit Units 路径在使用代理时同样需要 Azure 订阅，而不仅是按量付费计量需要？

<a id="ev_76f0e8bb40a574dcddc7fec9"></a>
### ev_76f0e8bb40a574dcddc7fec9

> First, you must buy a capacity pack for your tenant. Each capacity pack is a tenant license tha

来源：microsoft-365-docs/copilot/pay-as-you-go/copilot-capacity-packs.md at public · MicrosoftDocs/microsoft-365-docs · GitHub — https://github.com/MicrosoftDocs/microsoft-365-docs/blob/public/copilot/pay-as-you-go/copilot-capacity-packs.md

类型：web；读取时间：2026-10-19T08:29:15.341631+00:00；截断：False

问题 q5 → 分块 chk_f8f12eda37b72bebb9444fce_4590 → 来源 src_f8f12eda37b72bebb9444fce；清洗后字符 [5095, 5190)

SHA-256：`a95cb3d5b68b10d3964f7df866ebf3d53a12a749e413633907d8f91d3cbb7bf3`；范围：<main> element; characters 0-13057 of 13057

获取链：运行 d968652bc210 → 问题 q8 → 搜索 search7 → https://github.com/MicrosoftDocs/microsoft-365-docs/blob/public/copilot/pay-as-you-go/copilot-capacity-packs.md
检索词：Copilot Studio capacity pack Azure subscription requirement；当时的问题：微软官方文档是否明确 Copilot Studio 容量包（Copilot Credit 容量包，每包 25,000 信用）与预购 Commit Units 路径在使用代理时同样需要 Azure 订阅，而不仅是按量付费计量需要？

<a id="ev_010bb475f18cd0facb1d4350"></a>
### ev_010bb475f18cd0facb1d4350

> Copilot Studio is included with all Microsoft 365 Copilot licences for internal agent use. For external agent deployment, a standalone licence is priced at $200 per 25,000 Copilot Credits per month. Pay-as-you-go via Azure is also available. As of September 2025, Copilot Credits replaced the older per-message billing model. Pre-purchase capacity packs offer up to 20% savings for predictable usage.

来源：Microsoft Copilot Pricing Explained: Plans, Cost & Licensing (2026 Guide) — https://copilot-experts.com/microsoft-copilot-pricing-guide/

类型：web；读取时间：2026-10-19T08:34:53.971800+00:00；截断：False

问题 q5 → 分块 chk_ac5bf6d7ca3223d80201c6bc_38760 → 来源 src_ac5bf6d7ca3223d80201c6bc；清洗后字符 [38890, 39290)

SHA-256：`7fe833d081a4bedc364caa3ac22c186729714bd1900164aa122d9ec96c067acb`；范围：<body> element; characters 0-41267 of 41267

获取链：运行 23c904aac0c6 → 问题 q3 → 搜索 search1 → https://copilot-experts.com/microsoft-copilot-pricing-guide
检索词：Microsoft 365 Copilot pricing per user；当时的问题：微软官方 Microsoft 365 Copilot 产品页/价目页是否公开标明企业版为每用户每月 30 美元、Copilot Business 为每用户每月约 21 美元（年付），并说明按席位计费与适用版本？

<a id="ev_d1dc73ce2233ff3803f9f60c"></a>
### ev_d1dc73ce2233ff3803f9f60c

> One important note before the table: questions about Copilot Studio pricing per user are misleading. Copilot Studio is priced per credit, pooled at the tenant level, not per seat. The cost depends on how your agents consume credits, not how many people interact with them.

来源：Microsoft Copilot Studio Pricing In 2026: Credits, Plans, And Costs — https://www.cloudzero.com/blog/copilot-studio-pricing/

类型：web；读取时间：2026-10-19T08:23:25.388083+00:00；截断：False

问题 q5 → 分块 chk_5de6a402648eeec2266bf20a_3570 → 来源 src_5de6a402648eeec2266bf20a；清洗后字符 [3812, 4084)

SHA-256：`cb19d183bd1edd7576e299f6598b444a3200c932fb28102ca2d84e1e3314d183`；范围：<main> element; characters 0-19388 of 19388

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.cloudzero.com/blog/copilot-studio-pricing
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_7a665bca240fe219b0300714"></a>
### ev_7a665bca240fe219b0300714

> A named user on a qualifying plan People without a seat who use agents in Copilot Chat or SharePoint Tenants with steady agent traffic What you pay $360 per user per year (Copilot Business: $252) at the September 2026 list Microsoft's meter on your Azure subscription, $0.01 per message $2,400 per year per pack at list, plus pay-as-you-go for overage

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q5 → 分块 chk_ba995cac346030f043dc84c6_8670 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [8866, 9217)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_e0a050a8f91feb72529bed19"></a>
### ev_e0a050a8f91feb72529bed19

> On our Copilot Studio page , the tenant capacity pack lists at $2,400 per year paid up front, $2,520 per year billed monthly, or $240 a month on a one-month commitment; the separate Copilot Studio User License for access to the authoring tool lists at $0.

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q5 → 分块 chk_ba995cac346030f043dc84c6_4591 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [4816, 5071)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_6ee903e2371f8dec030d6873"></a>
### ev_6ee903e2371f8dec030d6873

> o capacity pack is 25,000 prepaid credits a month for the tenant and needs pay-as-you-go active behind it; the user license lists at $0.

来源：Microsoft 365 Copilot Licensing and Pricing 2026 — https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026

类型：web；读取时间：2026-10-19T08:26:42.979227+00:00；截断：False

问题 q5 → 分块 chk_ba995cac346030f043dc84c6_10200 → 来源 src_ba995cac346030f043dc84c6；清洗后字符 [10200, 10336)

SHA-256：`b827ac6d51ec9bebf4d04da07f538436c7bab59c2dde54716299cf1e5ceab89a`；范围：<main> element; characters 0-13398 of 13398

获取链：运行 d968652bc210 → 问题 q5 → 搜索 search4 → https://o365hq.com/blog/microsoft-365-copilot-licensing-and-pricing-2026
检索词：Microsoft 365 Copilot prerequisites eligible plans license requirements；当时的问题：微软官方文件列出的 Microsoft 365 Copilot 合格基础许可 SKU 具体有哪些（如 E3、E5、Business Standard、Business Premium 等），以及这些合格计划与 Copilot Studio 独立许可购买前提之间的对应关系是什么？

<a id="ev_8a26c7115c3d298fa2df5872"></a>
### ev_8a26c7115c3d298fa2df5872

> Copilot Studio is sold as tenant-wide license which includes Copilot Credit capacity packs of 25,000 Copilot Credits each, priced at $200.00 /pack/month.

来源：Microsoft Copilot Studio Plans and Pricing — https://www.microsoft.com/en-us/copilot/pricing/copilot-studio

类型：web；读取时间：2026-10-19T08:23:18.966505+00:00；截断：False

问题 q6 → 分块 chk_0974f6cd66d2bc4ca55c8219_6631 → 来源 src_0974f6cd66d2bc4ca55c8219；清洗后字符 [6748, 6901)

SHA-256：`5c2c49105b6ac9c095aedd95af5f2f3133be5bf6bb7d17561ab15184a704fb32`；范围：<main> element; characters 0-8971 of 8971

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.microsoft.com/en-us/copilot/pricing/copilot-studio
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_41d3722308a5dc62841ab0a5"></a>
### ev_41d3722308a5dc62841ab0a5

> • Pricing: $200 per pack/month • Copilot Credit Capacity: 1 capacity pack = 25,000 Copilot Credits

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q6 → 分块 chk_c68aacefe8ad1e6fd48eeabb_9180 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [9621, 9719)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_2b9e141ce0074ba49ee0902f"></a>
### ev_2b9e141ce0074ba49ee0902f

> • Pricing: $200 per credit pack/month (billed annually) • Copilot Credit Capacity: 1 capacity pack = 25,000 Copilot Credits

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf

类型：web；读取时间：2026-10-19T08:24:22.210421+00:00；截断：False

问题 q6 → 分块 chk_059af1d4b3d5bf109a6dbb14_27030 → 来源 src_059af1d4b3d5bf109a6dbb14；清洗后字符 [27310, 27433)

SHA-256：`ffd7d5a631e01bb670aef2bd8fa6ae234dcc34b5d3770ccd90bb71beba67c590`；范围：PDF pages 1-21 of 21; characters 0-38941 of 38941

获取链：运行 d968652bc210 → 问题 q2 → 搜索 search2 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/ai/Microsoft-Copilot-Studio-Licensing-Guide.pdf
检索词：Copilot Studio licensing guide fair usage limit；当时的问题：微软官方《Microsoft Copilot Studio Licensing Guide》（Product Terms 许可指南）中，Microsoft 365 Copilot 每席位具体包含多少个 Copilot Credit（代理使用额度）？其“按量付费（标为 unlimited）”和公平使用限制（fair usage limit）的确切定义是什么，并说明 Copilot Studio 按量计费是否必须绑定 Azure 订阅，以及容量包与预购 Commit Units 各自的适用条件。

<a id="ev_a6c70ef6d47fae8a5fd57c7d"></a>
### ev_a6c70ef6d47fae8a5fd57c7d

> Capacity packs cost $200/month for 25,000 Copilot Credits ($0.008/credit, ~25% cheaper than PAYG), pooled across every agent in the tenant.

来源：Microsoft Copilot Studio Pricing In 2026: Credits, Plans, And Costs — https://www.cloudzero.com/blog/copilot-studio-pricing/

类型：web；读取时间：2026-10-19T08:23:25.388083+00:00；截断：False

问题 q6 → 分块 chk_5de6a402648eeec2266bf20a_5610 → 来源 src_5de6a402648eeec2266bf20a；清洗后字符 [5910, 6049)

SHA-256：`cb19d183bd1edd7576e299f6598b444a3200c932fb28102ca2d84e1e3314d183`；范围：<main> element; characters 0-19388 of 19388

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.cloudzero.com/blog/copilot-studio-pricing
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_edc791ed50dfe849a951d8c6"></a>
### ev_edc791ed50dfe849a951d8c6

> Microsoft Pay-as-you-go $0.01/credit Usage-based Billed thro

来源：Microsoft Copilot Studio Pricing In 2026: Credits, Plans, And Costs — https://www.cloudzero.com/blog/copilot-studio-pricing/

类型：web；读取时间：2026-10-19T08:23:25.388083+00:00；截断：False

问题 q6 → 分块 chk_5de6a402648eeec2266bf20a_4080 → 来源 src_5de6a402648eeec2266bf20a；清洗后字符 [4620, 4680)

SHA-256：`cb19d183bd1edd7576e299f6598b444a3200c932fb28102ca2d84e1e3314d183`；范围：<main> element; characters 0-19388 of 19388

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.cloudzero.com/blog/copilot-studio-pricing
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_bf9bf15cff0c52b2feb4e258"></a>
### ev_bf9bf15cff0c52b2feb4e258

> For external agent deployment, a standalone licence is priced at $200 per 25,000 Copilot Credits per month.

来源：Microsoft Copilot Pricing Explained: Plans, Cost & Licensing (2026 Guide) — https://copilot-experts.com/microsoft-copilot-pricing-guide/

类型：web；读取时间：2026-10-19T08:34:53.971800+00:00；截断：False

问题 q6 → 分块 chk_ac5bf6d7ca3223d80201c6bc_38760 → 来源 src_ac5bf6d7ca3223d80201c6bc；清洗后字符 [38981, 39088)

SHA-256：`7fe833d081a4bedc364caa3ac22c186729714bd1900164aa122d9ec96c067acb`；范围：<body> element; characters 0-41267 of 41267

获取链：运行 23c904aac0c6 → 问题 q3 → 搜索 search1 → https://copilot-experts.com/microsoft-copilot-pricing-guide
检索词：Microsoft 365 Copilot pricing per user；当时的问题：微软官方 Microsoft 365 Copilot 产品页/价目页是否公开标明企业版为每用户每月 30 美元、Copilot Business 为每用户每月约 21 美元（年付），并说明按席位计费与适用版本？

<a id="ev_0f8c290625073de6c006ca00"></a>
### ev_0f8c290625073de6c006ca00

> Pre-purchase capacity packs offer up to 20% savings for predictable usage.

来源：Microsoft Copilot Pricing Explained: Plans, Cost & Licensing (2026 Guide) — https://copilot-experts.com/microsoft-copilot-pricing-guide/

类型：web；读取时间：2026-10-19T08:34:53.971800+00:00；截断：False

问题 q6 → 分块 chk_ac5bf6d7ca3223d80201c6bc_38760 → 来源 src_ac5bf6d7ca3223d80201c6bc；清洗后字符 [39216, 39290)

SHA-256：`7fe833d081a4bedc364caa3ac22c186729714bd1900164aa122d9ec96c067acb`；范围：<body> element; characters 0-41267 of 41267

获取链：运行 23c904aac0c6 → 问题 q3 → 搜索 search1 → https://copilot-experts.com/microsoft-copilot-pricing-guide
检索词：Microsoft 365 Copilot pricing per user；当时的问题：微软官方 Microsoft 365 Copilot 产品页/价目页是否公开标明企业版为每用户每月 30 美元、Copilot Business 为每用户每月约 21 美元（年付），并说明按席位计费与适用版本？

<a id="ev_a4a9a29791f8f6aa493415b6"></a>
### ev_a4a9a29791f8f6aa493415b6

> This is sold as a tenant-wide licence and priced at $200 per 25,000 Copilot Credits per month .

来源：Microsoft Copilot Pricing Explained: Plans, Cost & Licensing (2026 Guide) — https://copilot-experts.com/microsoft-copilot-pricing-guide/

类型：web；读取时间：2026-10-19T08:34:53.971800+00:00；截断：False

问题 q6 → 分块 chk_ac5bf6d7ca3223d80201c6bc_27540 → 来源 src_ac5bf6d7ca3223d80201c6bc；清洗后字符 [27932, 28027)

SHA-256：`7fe833d081a4bedc364caa3ac22c186729714bd1900164aa122d9ec96c067acb`；范围：<body> element; characters 0-41267 of 41267

获取链：运行 23c904aac0c6 → 问题 q3 → 搜索 search1 → https://copilot-experts.com/microsoft-copilot-pricing-guide
检索词：Microsoft 365 Copilot pricing per user；当时的问题：微软官方 Microsoft 365 Copilot 产品页/价目页是否公开标明企业版为每用户每月 30 美元、Copilot Business 为每用户每月约 21 美元（年付），并说明按席位计费与适用版本？

<a id="ev_2c9013d57779ffc70891ffd9"></a>
### ev_2c9013d57779ffc70891ffd9

> Microsoft Copilot Credit Commit Units (CCCU) Custom Annual Buy credits upfront via Microsoft Azure, up to 20% off, auto PAYG overflow

来源：Microsoft Copilot Studio Pricing In 2026: Credits, Plans, And Costs — https://www.cloudzero.com/blog/copilot-studio-pricing/

类型：web；读取时间：2026-10-19T08:23:25.388083+00:00；截断：False

问题 q6 → 分块 chk_5de6a402648eeec2266bf20a_4080 → 来源 src_5de6a402648eeec2266bf20a；清洗后字符 [4486, 4619)

SHA-256：`cb19d183bd1edd7576e299f6598b444a3200c932fb28102ca2d84e1e3314d183`；范围：<main> element; characters 0-19388 of 19388

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.cloudzero.com/blog/copilot-studio-pricing
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_2ae85ce7550530d842a58dd6"></a>
### ev_2ae85ce7550530d842a58dd6

> License (capacity pack): 25,000 Copilot Credit /pack3 Pre

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q6 → 分块 chk_c68aacefe8ad1e6fd48eeabb_13260 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [13803, 13860)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

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

<a id="ev_784627136f29e0b92110aa39"></a>
### ev_784627136f29e0b92110aa39

> To purchase, customers must have a qualifying Microsoft 365 plan for enterprise or business.

来源：Microsoft Copilot Studio Plans and Pricing — https://www.microsoft.com/en-us/copilot/pricing/copilot-studio

类型：web；读取时间：2026-10-19T08:23:18.966505+00:00；截断：False

问题 q7 → 分块 chk_0974f6cd66d2bc4ca55c8219_1020 → 来源 src_0974f6cd66d2bc4ca55c8219；清洗后字符 [1161, 1253)

SHA-256：`5c2c49105b6ac9c095aedd95af5f2f3133be5bf6bb7d17561ab15184a704fb32`；范围：<main> element; characters 0-8971 of 8971

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://www.microsoft.com/en-us/copilot/pricing/copilot-studio
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_7d1d68228d013e72f6062cf1"></a>
### ev_7d1d68228d013e72f6062cf1

> Microsoft 365 Copilot $30 per user/month Included agent usage1 Pay-as-you-go: unlimited2 License (capacity pack): 25,000 Copilot Credit /pack3

来源：Microsoft Copilot Studio Licensing Guide — https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf

类型：web；读取时间：2026-10-19T08:23:09.224597+00:00；截断：False

问题 q7 → 分块 chk_c68aacefe8ad1e6fd48eeabb_13260 → 来源 src_c68aacefe8ad1e6fd48eeabb；清洗后字符 [13714, 13856)

SHA-256：`0dec03292bc72d202e038d882ae2f67decae7f19e9841edecae89ea2b4f9d87c`；范围：PDF pages 1-20 of 20; characters 0-41269 of 41269

获取链：运行 d968652bc210 → 问题 q1 → 搜索 search1 → https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/bade/documents/products-and-services/en-us/microsoft-365/Microsoft-Copilot-Studio-Licensing-Guide-November-2025-PUB.pdf
检索词：Microsoft 365 Copilot Copilot Studio licensing pricing prerequisites；当时的问题：Microsoft 365 Copilot 与 Copilot Studio 在面向的企业使用者、收费单位（按用户席位还是按消息/容量计费）和购买前提（所需的基础许可或订阅）上分别是什么？请以微软官方许可与定价文档为准，说明两者的差异。

<a id="ev_dbb6eddb314a4ebb7c598dc0"></a>
### ev_dbb6eddb314a4ebb7c598dc0

> Each capacity pack is a tenant license tha

来源：microsoft-365-docs/copilot/pay-as-you-go/copilot-capacity-packs.md at public · MicrosoftDocs/microsoft-365-docs · GitHub — https://github.com/MicrosoftDocs/microsoft-365-docs/blob/public/copilot/pay-as-you-go/copilot-capacity-packs.md

类型：web；读取时间：2026-10-19T08:29:15.341631+00:00；截断：False

问题 q7 → 分块 chk_f8f12eda37b72bebb9444fce_4590 → 来源 src_f8f12eda37b72bebb9444fce；清洗后字符 [5148, 5190)

SHA-256：`a95cb3d5b68b10d3964f7df866ebf3d53a12a749e413633907d8f91d3cbb7bf3`；范围：<main> element; characters 0-13057 of 13057

获取链：运行 d968652bc210 → 问题 q8 → 搜索 search7 → https://github.com/MicrosoftDocs/microsoft-365-docs/blob/public/copilot/pay-as-you-go/copilot-capacity-packs.md
检索词：Copilot Studio capacity pack Azure subscription requirement；当时的问题：微软官方文档是否明确 Copilot Studio 容量包（Copilot Credit 容量包，每包 25,000 信用）与预购 Commit Units 路径在使用代理时同样需要 Azure 订阅，而不仅是按量付费计量需要？

完整来源文本、分块、引用和哈希见同目录 state.json；节点、调用及排序分数见 trace.jsonl。
