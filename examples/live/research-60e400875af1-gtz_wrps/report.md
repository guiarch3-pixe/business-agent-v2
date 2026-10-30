# Microsoft｜企业研究

研究问题：Microsoft 365 企业版包含哪些协作工具？这些工具通过哪些方式向企业客户交付？优先引用微软官方资料，并区分有来源的事实、推导与待验证假设。

模式：live；停止原因：error；研究轮次：2

引用关系与摘录位置已做代码校验；语义支持关系、事实分类和缺口关闭是模型判断，未经独立事实核实。

## 事实（来源陈述）

- **c1_1** [supported] 二手来源称，多数企业客户购买捆绑的 Microsoft 365 计划（E3、E5），这些计划包含 Microsoft 365 Apps for Enterprise，以及 Exchange Online、SharePoint、Teams 和其他服务。 [ev_de2e09035295644695f04bee](#ev_de2e09035295644695f04bee)（supports） [ev_80d17b485fa95a62f4cc0444](#ev_80d17b485fa95a62f4cc0444)（supports）
  依据/推导：摘录直接陈述了 E3/E5 捆绑内容；但来源为第三方博客（mind-core.com），非微软官方页面，需以微软官方许可文档复核。
- **c1_2** [supported] 二手对比资料显示，Microsoft 365 Business Basic、Business Standard、Business Premium、E3、E5 中均包含 Teams 应用及一对一/群组聊天等协作能力；Business Premium、E3、E5 在 SharePoint 团队站点、SharePoint 通信站点、OneDrive 云存储（1TB 至无限）以及 Stream 智能视频方面均有覆盖。 [ev_dee952eeef57a14de676792d](#ev_dee952eeef57a14de676792d)（supports） [ev_8aa991c496e2ddcff2def619](#ev_8aa991c496e2ddcff2def619)（supports）
  依据/推导：摘录为第三方（Syskit）整理的套餐功能对比表，直接列出各层级勾选项；属二手整理，数字细节（如存储配额）应以微软官方许可条款核实。
- **c1_3** [supported] 一份微软合作伙伴中心中文公告的指标/功能清单中列出了 Exchange 在线版、SharePoint Online、Teams 应用、Teams 会议、Teams 电话、Teams 会议室系统、Viva Connections、Viva Engage、Viva 目标、Viva Insights、Viva Learning、Viva Topics 等协作相关项。 [ev_706132d350b105660f413276](#ev_706132d350b105660f413276)（supports）
  依据/推导：摘录为 learn.microsoft.com 合作伙伴中心公告，属微软官方文档；但该段仅为清单罗列，未直接说明各项与具体套件层级的归属关系，故仅能作为协作工具命名的证据。
- **c1_4** [supported] Microsoft 365 Apps for Enterprise 被描述为包含 OneDrive、Teams 及企业级部署管理功能的桌面应用组件，通常与企业邮件和协作服务一并授权；来源并建议需要详情时参阅微软官方“Buy Microsoft 365 Apps for Enterprise”与“Microsoft 365 Apps for Business”文档。 [ev_8dddbbc4e79d7f94d948a469](#ev_8dddbbc4e79d7f94d948a469)（supports） [ev_6b5e551f8ee7e48724d73e06](#ev_6b5e551f8ee7e48724d73e06)（supports）
  依据/推导：摘录来自第三方博客与 learn.microsoft.com 问答帖，后者仅为指向官方购买页的转引；未提供官方页面原文内容，故不能据此断言官方定义的完整措辞。
- **c1_6** [supported] 二手资料提到 OneDrive for Business 提供 1 TB 个人云存储，并将其列为协作工具之一。 [ev_d9de98ff51aa4cecbe4325c3](#ev_d9de98ff51aa4cecbe4325c3)（supports）
  依据/推导：摘录直接陈述该内容；来源为 learn.microsoft.com 问答社区，但该帖内容本身是用户回答，非微软产品文档，需谨慎对待。

## 推导


## 商业判断


## 待验证假设

- **c1_5** [unverified] Microsoft 365 企业版协作工具可能主要通过三种渠道获取：E3/E5 捆绑套件、单独订阅 Microsoft 365 Apps for Enterprise、以及 Teams 等功能的附加组件（如 Teams 应用在部分层级以 add-on 形式提供）。 [ev_8aa991c496e2ddcff2def619](#ev_8aa991c496e2ddcff2def619)（supports） [ev_dee952eeef57a14de676792d](#ev_dee952eeef57a14de676792d)（supports）
  依据/推导：证据显示 Teams 应用在部分层级为“Available as an add-on”，且存在单独购买 Apps for Enterprise 的讨论，但本轮无微软官方许可/定价页面原文，无法确认完整渠道清单，故列为待验证假设。

## 证据缺口

- gap0 [open] Microsoft 365 企业版包含哪些协作工具？这些工具通过哪些方式向企业客户交付？优先引用微软官方资料，并区分有来源的事实、推导与待验证假设。
- gap1 [open] 需检索微软官方 Microsoft 365 企业版计划对比页（如 microsoft.com 的 E3/E5 计划页）与许可条款，以官方原文确认 Teams、SharePoint、Exchange、OneDrive、Viva 各子项在 E3/E5 中的包含关系及配额。
- gap2 [open] 需确认微软官方明确列出的企业获取渠道：捆配套件（E3/E5）、单独订阅 Microsoft 365 Apps for Enterprise、以及 Teams 等功能的附加组件（add-on），并核实哪些功能在哪些层级仅以附加组件形式提供。
- gap3 [open] 需用微软官方来源核实 Viva（Connections、Engage、Goals、Insights、Learning、Topics）与企业版套件层级的对应关系及是否作为独立/附加许可提供。

## 问题与检索记录

- q0 / 第 0 轮 / 缺口 初始问题：Microsoft 365 企业版包含哪些协作工具？这些工具通过哪些方式向企业客户交付？优先引用微软官方资料，并区分有来源的事实、推导与待验证假设。
- q1 / 第 1 轮 / 缺口 gap0：微软官方资料中，Microsoft 365 企业版明确定义了哪些协作类应用与服务（如 Teams、SharePoint、Exchange、OneDrive、Viva 等），以及这些协作工具面向企业客户的官方许可/获取渠道包括哪些（例如 Microsoft 365 企业版各套件层级、单独订阅或附加组件）？
  Tavily search1：Microsoft 365 Enterprise collaboration apps licensing；结果 5；错误 无
- q2 / 第 2 轮 / 缺口 gap1：微软官方 Microsoft 365 企业版计划对比页（E3/E5）如何列明 Teams、SharePoint、Exchange Online、OneDrive 与 Viva 各组件的包含关系？
  Tavily search2：Microsoft 365 E3 E5 plan comparison；结果 5；错误 无

## 原文摘录与追溯

<a id="ev_de2e09035295644695f04bee"></a>
### ev_de2e09035295644695f04bee

> Most enterprise customers purchase bundled Microsoft 365 plans (E3, E5) that include Microsoft 365 Apps for Enterprise along with Exchange Online, SharePoint, Teams, and other services. Purchasing Apps for Enterprise standalone makes sense for organizations that have other arrangements for email and collaboration services, or that are adding Office application access for users who

来源：What Are Microsoft 365 Apps for Enterprise? | Mindcore — https://mind-core.com/blogs/what-are-microsoft-365-apps-for-enterprise

类型：web；读取时间：2026-10-19T07:16:36.591037+00:00；截断：False

问题 q1 → 分块 chk_d39eff0e26ae6a00cbae5ae2_4080 → 来源 src_d39eff0e26ae6a00cbae5ae2；清洗后字符 [4096, 4479)

SHA-256：`22b1be04a6dcef193364bee0382dcab80ba279d74faa4992d1250a366683a077`；范围：<main> element; characters 0-7327 of 7327

获取链：运行 60e400875af1 → 问题 q1 → 搜索 search1 → https://mind-core.com/blogs/what-are-microsoft-365-apps-for-enterprise
检索词：Microsoft 365 Enterprise collaboration apps licensing；当时的问题：微软官方资料中，Microsoft 365 企业版明确定义了哪些协作类应用与服务（如 Teams、SharePoint、Exchange、OneDrive、Viva 等），以及这些协作工具面向企业客户的官方许可/获取渠道包括哪些（例如 Microsoft 365 企业版各套件层级、单独订阅或附加组件）？

<a id="ev_8aa991c496e2ddcff2def619"></a>
### ev_8aa991c496e2ddcff2def619

> t 365 Business Premium Microsoft 365 E3 Microsoft 365 E5 Create team sites to share information, content, and files throughout your intranet using SharePoint ✓ ✓ ✓ ✓ ✓ Cloud storage per user in OneDrive 1 TB 1 TB 1 TB Unlimited Unlimited Create communication sites in SharePoint ✓ ✓ ✓ ✓ ✓ Engage and inform with intelligent video using Stream ✓ ✓ ✓ ✓ ✓ Connect everyone at your organization through e

来源：Decision: Microsoft 365 Apps For Business Or Enterprise — https://www.syskit.com/blog/the-microsoft-365-apps-decision-business-or-enterprise

类型：web；读取时间：2026-10-19T07:16:43.207056+00:00；截断：False

问题 q1 → 分块 chk_10e49c69fde2a0154a0c4f11_8160 → 来源 src_10e49c69fde2a0154a0c4f11；清洗后字符 [8160, 8560)

SHA-256：`8978af64b48c00b2f73ef231995fcd1a0265b94574c3af9402d2ab9cdb46b153`；范围：<main> element; characters 0-15215 of 15215

获取链：运行 60e400875af1 → 问题 q1 → 搜索 search1 → https://www.syskit.com/blog/the-microsoft-365-apps-decision-business-or-enterprise
检索词：Microsoft 365 Enterprise collaboration apps licensing；当时的问题：微软官方资料中，Microsoft 365 企业版明确定义了哪些协作类应用与服务（如 Teams、SharePoint、Exchange、OneDrive、Viva 等），以及这些协作工具面向企业客户的官方许可/获取渠道包括哪些（例如 Microsoft 365 企业版各套件层级、单独订阅或附加组件）？

<a id="ev_706132d350b105660f413276"></a>
### ev_706132d350b105660f413276

> Exchange 在线版 Intune Microsoft 365 应用 Microsoft 365 Copilot Microsoft Entra ID P1 SharePoint Online 团队 Teams 应用 适合一线员工的 Teams Teams 会议 Teams 电话 Teams 电话通话 已启用 Teams 电话的用户 Teams 会议室系统每月活跃设备 Viva Connections Viva Engage Viva 目标 Viva Insights Viva Learning Viva Topics Windows 365

来源：2026 年 1 月公告 - Partner Center announcements | Microsoft Learn — https://learn.microsoft.com/zh-cn/partner-center/announcements/2026-january

类型：web；读取时间：2026-10-19T07:11:58.581959+00:00；截断：False

问题 q1 → 分块 chk_6283af8b1ac3bd7d0c27dff2_680 → 来源 src_6283af8b1ac3bd7d0c27dff2；清洗后字符 [774, 1050)

SHA-256：`66d5e9f041aea5ee89d1882fb7fc5c3aff7e52b7648be7f4ed7c0efc842bdeb3`；范围：<main> element; characters 0-12428 of 12428

获取链：运行 026f0f9a30cf → 问题 q2 → 搜索 search2 → https://learn.microsoft.com/zh-cn/partner-center/announcements/2026-january
检索词：Microsoft 365 E3 E5 服务说明 site:learn.microsoft.com 协作服务 Exchange Online SharePoint Online OneDrive Teams 许可 订阅 交付渠道 CSP EA；当时的问题：微软官方文档中，Microsoft 365 企业版（E3/E5）的协作相关服务组件（Exchange Online、SharePoint Online、OneDrive for Business、Teams、Viva Engage 等）分别包含在哪些许可套件中，这些服务是通过订阅方式交付还是可通过其他渠道（如 EA、CSP、云服务提供商）获取？

<a id="ev_80d17b485fa95a62f4cc0444"></a>
### ev_80d17b485fa95a62f4cc0444

> Microsoft 365 Apps for Enterprise is a subscription plan that provides the full Microsoft Office desktop application suite — Word, Excel, PowerPoint, Outlook, Access, Publisher — plus OneDrive, Teams, and enterprise-grade deployment and

来源：What Are Microsoft 365 Apps for Enterprise? | Mindcore — https://mind-core.com/blogs/what-are-microsoft-365-apps-for-enterprise

类型：web；读取时间：2026-10-19T07:16:36.591037+00:00；截断：False

问题 q1 → 分块 chk_d39eff0e26ae6a00cbae5ae2_0 → 来源 src_d39eff0e26ae6a00cbae5ae2；清洗后字符 [163, 399)

SHA-256：`22b1be04a6dcef193364bee0382dcab80ba279d74faa4992d1250a366683a077`；范围：<main> element; characters 0-7327 of 7327

获取链：运行 60e400875af1 → 问题 q1 → 搜索 search1 → https://mind-core.com/blogs/what-are-microsoft-365-apps-for-enterprise
检索词：Microsoft 365 Enterprise collaboration apps licensing；当时的问题：微软官方资料中，Microsoft 365 企业版明确定义了哪些协作类应用与服务（如 Teams、SharePoint、Exchange、OneDrive、Viva 等），以及这些协作工具面向企业客户的官方许可/获取渠道包括哪些（例如 Microsoft 365 企业版各套件层级、单独订阅或附加组件）？

<a id="ev_dee952eeef57a14de676792d"></a>
### ev_dee952eeef57a14de676792d

> Microsoft 365 Business Basic Microsoft 365 Business Standard Microsoft 365 Business Premium Microsoft 365 E3 Microsoft 365 E5 Microsoft Teams App ✓ ✓ ✓ Available as an add-on Available as an add-on One-on-one or group chat ✓ ✓ ✓ Available as an add-on Available as an add-on Chat, meet, share files, and use business apps in a shared workspac

来源：Decision: Microsoft 365 Apps For Business Or Enterprise — https://www.syskit.com/blog/the-microsoft-365-apps-decision-business-or-enterprise

类型：web；读取时间：2026-10-19T07:16:43.207056+00:00；截断：False

问题 q1 → 分块 chk_10e49c69fde2a0154a0c4f11_6460 → 来源 src_10e49c69fde2a0154a0c4f11；清洗后字符 [6518, 6860)

SHA-256：`8978af64b48c00b2f73ef231995fcd1a0265b94574c3af9402d2ab9cdb46b153`；范围：<main> element; characters 0-15215 of 15215

获取链：运行 60e400875af1 → 问题 q1 → 搜索 search1 → https://www.syskit.com/blog/the-microsoft-365-apps-decision-business-or-enterprise
检索词：Microsoft 365 Enterprise collaboration apps licensing；当时的问题：微软官方资料中，Microsoft 365 企业版明确定义了哪些协作类应用与服务（如 Teams、SharePoint、Exchange、OneDrive、Viva 等），以及这些协作工具面向企业客户的官方许可/获取渠道包括哪些（例如 Microsoft 365 企业版各套件层级、单独订阅或附加组件）？

<a id="ev_8dddbbc4e79d7f94d948a469"></a>
### ev_8dddbbc4e79d7f94d948a469

> — plus OneDrive, Teams, and enterprise-grade deployment and management features. It is the desktop application component of the enterprise Microsoft 365 experience, typically licensed alongside enterprise email and collaboration services.

来源：What Are Microsoft 365 Apps for Enterprise? | Mindcore — https://mind-core.com/blogs/what-are-microsoft-365-apps-for-enterprise

类型：web；读取时间：2026-10-19T07:16:36.591037+00:00；截断：False

问题 q1 → 分块 chk_d39eff0e26ae6a00cbae5ae2_340 → 来源 src_d39eff0e26ae6a00cbae5ae2；清洗后字符 [340, 578)

SHA-256：`22b1be04a6dcef193364bee0382dcab80ba279d74faa4992d1250a366683a077`；范围：<main> element; characters 0-7327 of 7327

获取链：运行 60e400875af1 → 问题 q1 → 搜索 search1 → https://mind-core.com/blogs/what-are-microsoft-365-apps-for-enterprise
检索词：Microsoft 365 Enterprise collaboration apps licensing；当时的问题：微软官方资料中，Microsoft 365 企业版明确定义了哪些协作类应用与服务（如 Teams、SharePoint、Exchange、OneDrive、Viva 等），以及这些协作工具面向企业客户的官方许可/获取渠道包括哪些（例如 Microsoft 365 企业版各套件层级、单独订阅或附加组件）？

<a id="ev_d9de98ff51aa4cecbe4325c3"></a>
### ev_d9de98ff51aa4cecbe4325c3

> Collaboration Tools: OneDrive for Business: 1 TB of personal cloud storage Micr

来源：Apps for Enterprise Features? - Microsoft Q&A — https://learn.microsoft.com/en-us/answers/questions/5330335/apps-for-enterprise-features

类型：web；读取时间：2026-10-19T07:16:48.153985+00:00；截断：False

问题 q1 → 分块 chk_a68887637f6831356298933a_1360 → 来源 src_a68887637f6831356298933a；清洗后字符 [1681, 1760)

SHA-256：`a8c3dfecafafaa18e129ea918e2a14049c504fed11e16d03756e5642206a9ed2`；范围：<main> element; characters 0-3631 of 3631

获取链：运行 60e400875af1 → 问题 q1 → 搜索 search1 → https://learn.microsoft.com/en-us/answers/questions/5330335/apps-for-enterprise-features
检索词：Microsoft 365 Enterprise collaboration apps licensing；当时的问题：微软官方资料中，Microsoft 365 企业版明确定义了哪些协作类应用与服务（如 Teams、SharePoint、Exchange、OneDrive、Viva 等），以及这些协作工具面向企业客户的官方许可/获取渠道包括哪些（例如 Microsoft 365 企业版各套件层级、单独订阅或附加组件）？

<a id="ev_6b5e551f8ee7e48724d73e06"></a>
### ev_6b5e551f8ee7e48724d73e06

> ps for Enterprise, please kindly refer to these two official documents for more details Buy Microsoft 365 Apps for Enterprise | Microsoft 365 Microsoft 365 Apps for Business | Microsoft 365

来源：Microsoft 365 Apps for Business used in an enterprise - Microsoft Q&A — https://learn.microsoft.com/en-us/answers/questions/5230328/microsoft-365-apps-for-business-used-in-an-enterpr

类型：web；读取时间：2026-10-19T07:16:50.572974+00:00；截断：False

问题 q1 → 分块 chk_a607c453130d2a71d7f0c17e_2380 → 来源 src_a607c453130d2a71d7f0c17e；清洗后字符 [2380, 2569)

SHA-256：`4d010ff078e84ae2ef3c150deb40755de796326ce1a6614982fca26beef50a6f`；范围：<main> element; characters 0-3075 of 3075

获取链：运行 60e400875af1 → 问题 q1 → 搜索 search1 → https://learn.microsoft.com/en-us/answers/questions/5230328/microsoft-365-apps-for-business-used-in-an-enterpr
检索词：Microsoft 365 Enterprise collaboration apps licensing；当时的问题：微软官方资料中，Microsoft 365 企业版明确定义了哪些协作类应用与服务（如 Teams、SharePoint、Exchange、OneDrive、Viva 等），以及这些协作工具面向企业客户的官方许可/获取渠道包括哪些（例如 Microsoft 365 企业版各套件层级、单独订阅或附加组件）？

完整来源文本、分块、引用和哈希见同目录 state.json；节点、调用及排序分数见 trace.jsonl。
