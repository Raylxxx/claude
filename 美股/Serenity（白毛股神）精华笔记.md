---
title: Serenity（白毛股神）精华笔记
aliases: [白毛股神, Serenity, aleabitoreddit]
tags: [美股, 博主研究, AI供应链, 光通信, 存储]
account: "@aleabitoreddit"
coverage: 2025-10 至 2026-10
created: 2026-10-07
source: 公开网页搜索结果（非原帖全文）
---

# Serenity（白毛股神）精华笔记

> [!warning] 先读这里：这份笔记的来源和局限
> - **不是她的全部帖子。** 内容来自网页搜索：搜索结果里出现的原帖摘要、媒体报道、第三方分析和战绩统计。大约只覆盖她全部发帖的一小部分，而且偏向「被大量转发、引起话题」的帖子。
> - **原文多为节选。** 英文引用是搜索摘要里的片段，常被截断（以 … 结尾）。中文是我的翻译和转述，不是她的原话。
> - **日期是推算的。** X 的帖子编号里编码了发帖时间，日期由编号换算而来（UTC），可信度高。少数条目没有找到原帖链接，会标明「原帖未定位」。
> - **股价和收益**多是她本人或第三方的说法，我没有逐一核实。
> - 她本人在简介里写明：**所有内容都不构成投资建议**，她可能持有所讨论的股票。

## 目录

- [[#一、人物速览]]
- [[#二、核心投资框架]]
- [[#三、战绩：自报 vs 第三方统计]]
- [[#四、股票索引]]
- [[#五、帖子时间线]]
- [[#六、主题小结]]
- [[#七、来源]]

---

## 一、人物速览

| 项目 | 内容 |
|---|---|
| 账号 | Serenity，[@aleabitoreddit](https://x.com/aleabitoreddit)，2025 年 7 月注册 X |
| 自我介绍 | 「AI/Semi Supply Chains Research」（AI 与半导体供应链研究），「只在 X 发帖，小心假号」 |
| 背景（第三方说法） | 前 Reddit WallStreetBets 用户（u/AleaBito），自称做过 RISC-V 基金会和 AI 研究科学家，现在「交易没人注意到的瓶颈」 |
| 出圈经历 | 据报道，在 WSB 发了一篇 $AXTI 供应链长文后被版主封号，之后 AXTI 大涨 |
| 粉丝增长 | 2026 年 5 月约 40 万（Bloomberg），2026 年 8 月约 100 万 |
| 语言 | 主要用英文。她提到中文帖的评论数常常是英文帖的几十倍（2026-09-20） |

---

## 二、核心投资框架

**「瓶颈理论」（Chokepoint Theory）**：不买 Nvidia、微软这类人人都知道的 AI 赢家，而是**沿着供应链往上游找**：大公司离不开、产能又卡脖子的那个小环节。

```
AI 需求 → 大厂（NVDA / GOOGL / MSFT / AMZN）→ 光模块（LITE、AAOI）
       → 激光器 / 光芯片 → 外延片（IQE）→ 衬底材料（AXTI、Soitec）→ 设备（Aixtron、Veeco）
```

几个反复出现的思路：

1. **「瓶颈中的瓶颈」**：越上游、供应商越少、市值越小，弹性越大。典型例子是磷化铟衬底（$AXTI）。
2. **类比 HBM 和 NAND 的涨价周期**：她认为光通信元件（InP、激光器）会重演存储芯片「缺货 → 涨价 → 厂商利润暴增」的剧本。
3. **抢在机构轮动之前**：先布局小市值的上游公司，等机构顺着供应链买进来。
4. **看远期业绩，忍受短期波动**：她的很多判断以 2027 年下半年为业绩拐点。2026 年 7 月大回撤时，她的解释是「论点没错，只是时间还没到」。
5. **催化剂驱动**：NVIDIA GTC、欧盟芯片法案 2.0、ECOC 光通信展会、财报等。

---

## 三、战绩：自报 vs 第三方统计

### 她自己公布的收益（无法审计）

| 日期 | 自报收益 |
|---|---|
| 2026-02-21 | 年初至今 **+316.4%** |
| 2026-02-24 | 年初至今 **+412.72%** |
| 2026-03 中旬 | **+943%**，主要靠 $AXTI（$12 → $48）和 $SNDK（$220 → $772） |
| 其他时点 | 第三方汇总：不同时间截图在 +501% 到 +1,116% 之间 |
| 2026-07 | 披露约 **−49.4% 的回撤**（约 1.4 倍杠杆，底层持仓跌约 35%） |

### 第三方统计（更客观）

| 来源 | 结论 |
|---|---|
| **Quantral 评分** | 评了 **274 条**判断，**59.5% 正确**，在他们的 6 个月榜单排第 2。单季度（Q2）就有 179 条可评分的判断，是榜单中位数的 4 倍 |
| **独立校准** | 30 天方向准确率约 **61%**。严格标准（30 天内 ±10%）命中 41%。60 天内出现 20%+ 有利走势的比例为 54% |
| **fxcryptobots 回测 v3** | 2025-07-02 至 2026-05-17，**383 只**被看多的股票，共 5,126 次提及。在首次提及日等权买入，平均收益 **+25.60%**；同期买半导体 ETF（XSD）是 **+62.93%**，平均跑输 **37.32 个百分点**。**只有 21.1% 跑赢板块**，约 20 只显示出真实选股能力 |
| 最大赢家 | $AXTI **+711%**，$SNDK **+516%**（回测口径） |

> [!tip] 怎么理解这两组数字
> 她的**重点推荐**（高信心、写过长文的）表现很好，但她**提到的股票数量非常多**。如果把每只都买一遍，整体反而跑输半导体 ETF。
> 跟着她的时候，应该只关注她**反复论证、明确说是高信心**的那几只，不要看到她提什么就买什么。

---

## 四、股票索引

指向性：**看多** / **看空** / **中性** / **复盘**（回顾自己之前的判断）。日期写作「月-日」：10～12 月是 2025 年，其余是 2026 年，可以在第五部分按日期找到对应帖子。

> [!note] 关于「看空」
> 在能找到的公开资料里，她**几乎没有看空某只股票的帖子**。第三方统计也显示她以看多为主，例如 AAOI 下跌期间是 16 次看多、0 次看空。

| 代码 | 公司 | 所属环节 | 指向性 | 帖子日期 |
|---|---|---|---|---|
| $AXTI | AXT Inc. | 磷化铟（InP）衬底 | 看多（核心） | 12-29、12-30、01-02、02-10、05-10、07-29 |
| $LITE | Lumentum | 光模块 / 激光器 | 看多（核心） | 12-22、12-23、04-07、07-02、10-02 |
| $AAOI | Applied Optoelectronics | 光模块（垂直整合） | 看多（核心） | 12-23、02-27、06-01 ×2、06-05 |
| $SNDK | SanDisk 闪迪 | NAND 存储 | 看多 | 01-30、02-24、03-10、04-07、08-04 |
| $SOI | Soitec | 光子 SOI 衬底 | 看多（核心） | 03-01、03-13、03-16、04-14、04-16、04-21 |
| $SIVE | Sivers Semiconductors | CPO 用 CW 激光光源 | 看多（最高信心之一） | 03-17、04-01 前后、05-22、05-27 |
| $IQE | IQE plc | 化合物半导体外延 | 看多 | 02-27、04-12、04-22 |
| $TSEM | Tower Semiconductor | 硅光代工 | 看多（「最安全」） | 03-13、04-06 |
| $COHR | Coherent | 光通信全链条 | 看多（「最安全」） | 02-24、03-13、04-08 |
| $MRVL | Marvell | 定制 ASIC / 光互连 | 看多（中长期） | 12-31、02-07、04-08、04-09、09-20 |
| $XFAB | X-Fab | 硅光 + 功率半导体代工 | 看多 | 05-27、05-28、06-03 |
| $HPS.A | Hammond Power | 数据中心变压器 | 看多 | 04-06、04-07、04-09 |
| $NBIS | Nebius | AI 云（Neocloud） | 看多（核心） | 10-12、10-17、11-15、06-03、09-24 |
| $ALAB | Astera Labs | AI 互连芯片 | 看多 | 10-12、06-12 |
| $RKLB | Rocket Lab | 航天 | 看多 | 10-12、06-12 |
| $TSM | 台积电 | 晶圆代工 | 看多 | 10-12、04-09、06-12 |
| $MU / 三星 / SK 海力士 | 存储三巨头 | DRAM / HBM | 看多 | 02-24、03-10、08-04 |
| $RPI | Raspberry Pi | 边缘计算硬件 | 看多 | 2026-02、03-31 |
| $CRDO | Credo | 高速互连 | 看多 | 02-09 |
| Aixtron / $VECO | Aixtron、Veeco | MOCVD 设备 | 看多 | 02-27、02-28 |
| Phison / Macronix | 群联、旺宏 | NAND 控制器 / NOR | 看多（持有） | 01-30、2026-09 |
| LeaderDrive | 绿的谐波（688017） | 机器人谐波减速器 | 看多 | 06-08 |

---

## 五、帖子时间线

### 2025 年 10 月

#### 2025-10-03 · 期权卖方波段策略
> [!summary] 概述
> - **涉及股票**：$NBIS、$HIMS、$CIFR、$RKLB、$TGT、$AMZN
> - **指向性**：复盘（策略展示）
> - **一句话**：用 100 万美元本金卖期权做波段，5 天实现约 2 万美元利润，折合年化 183%+

**内容**：「我写了一个卖期权的波段策略，上周用 100 万美元本金，5 天实现 2 万美元利润……我都是**事前**给出具体仓位，不是事后补的。」各股盈利：$NBIS +5.52K、$CIFR +5.24K、$RKLB +3.8K、$HIMS +1.43K、$TGT +1.3K、$AMZN +1.22K。

🔗 [原帖](https://x.com/aleabitoreddit/status/1974167533226955118) · 标签：#股票/NBIS #股票/RKLB

#### 2025-10-12 · 第一次公开「高信心持仓清单」⭐
> [!summary] 概述
> - **涉及股票**：$RKLB、$TSM、$HOOD、$BTC、$NBIS、$ALAB，外加 1 只「1000% 潜力股」
> - **指向性**：看多
> - **一句话**：6 只最高信心长线持仓，按买入先后排序，注明了何时、为什么建立信心

**内容**：「这是我第一次公布高信心清单：6 只最高信心的多头，加 1 只新的 1000% 潜力股🚀。」清单中的买入价 → 当时价格：$RKLB（$16 → $28）、$TSM（$120 → $245）、$HOOD（$11.27 → $18）、$BTC（$3k → $57k）、$NBIS（$28 → $99）、$ALAB（$55 → $95）。

**后续**：她在 2026-06-12 复盘时说，$ALAB 从 $97 涨到 $372，$NBIS、$RKLB、$TSM 也表现很好。

🔗 [原帖](https://x.com/aleabitoreddit/status/1977495210063286491) · 标签：#股票/NBIS #股票/ALAB #股票/RKLB #股票/TSM

#### 2025-10-17 · Nebius 对比 Oklo
> [!summary] 概述
> - **涉及股票**：$NBIS、$OKLO
> - **指向性**：看多 NBIS
> - **一句话**：Nebius 市值快追上 Oklo，但 Oklo 还没有收入，Nebius 明年 ARR 预计 40～60 亿美元

🔗 [原帖](https://x.com/aleabitoreddit/status/1979210275011146008) · 标签：#股票/NBIS

### 2025 年 11 月

#### 2025-11-15 · Nebius 暴跌后机构反而加仓
> [!summary] 概述
> - **涉及股票**：$NBIS
> - **指向性**：看多
> - **一句话**：NBIS 上个月跌 33.61%，市值只剩 210 亿美元，但 13F 显示机构持股比例从 38.36% 升到 44.6%

**内容**：「Nebius 上个月暴跌 −33.61%，市值跌到 210 亿美元。但新的 13F 数据显示机构持股上升：38.36% → 44.6%（+6.24%），Fintel 的数据接近 46.3%。Nebius 是一家 210 亿美元市值的全栈 Neocloud……」

**后续**：2026-06-03 她说 NBIS 从 $84 涨到 $260，是整个 Neocloud 板块的第一名。

🔗 [原帖](https://x.com/aleabitoreddit/status/1989608255371579717) · 标签：#股票/NBIS

### 2025 年 12 月

#### 2025-12-22 · $LITE 论点：AI 里隐藏的垄断 ⭐
> [!summary] 概述
> - **涉及股票**：$LITE（对比 $MU、$TSM）
> - **指向性**：看多
> - **一句话**：Lumentum 今年已涨 316%，但到 2027 年可能涨 1000%+；每一颗 Google TPU 里都有它

**内容**：「$LITE 论点：AI 里隐藏的垄断。Lumentum 年初至今涨了 316%，但到 2027 年可能涨 1000%+。美光（3,000 亿美元）和台积电（1.5 万亿美元）处在每一颗 TPU/GPU 的核心，$LITE 也一样，但它市值只有 260 亿美元。在 Google 的每一颗 TPU 里……」

**后续**：她在 2026-06-12 说 LITE 从 $330 涨到 $904；2026-06-16 说 LITE 市值从 260 亿美元涨到 744.7 亿美元。

🔗 [原帖](https://x.com/aleabitoreddit/status/2003019490871869644) · 标签：#股票/LITE

#### 2025-12-23 · AAOI 和 LITE 的不同敞口
> [!summary] 概述
> - **涉及股票**：$AAOI、$LITE、$GOOGL、$NVDA、$MSFT、$AMZN
> - **指向性**：看多
> - **一句话**：发论点当天 AAOI 涨 24%、LITE 涨 5%；InP 会像 HBM 一样，成为 2026 年的瓶颈

**内容**：「从 BOM（物料清单）分析看，LITE（270 亿美元）押的是 Google TPU Ironwood（因为 OCS 光交换），同时受益于 NVDA 和所有 ASIC。AAOI（25 亿美元）押的是微软 MAIA 和亚马逊 Trainium 的放量。**InP 会像 HBM 一样，成为 2026 年的瓶颈。**」

🔗 [原帖](https://x.com/aleabitoreddit/status/2003259964526330053) · 标签：#股票/AAOI #股票/LITE

#### 2025-12-29 · AXTI 瓶颈中的瓶颈
> [!summary] 概述
> - **涉及股票**：$AXTI、SMTOY（住友电工）
> - **指向性**：看多（核心论点）
> - **一句话**：全球 60～70% 以上的磷化铟衬底由 AXTI（7 亿美元市值）和住友电工控制，整个 AI 产业可能被它们卡住

**内容**：标题「"Bottleneck within a Bottleneck": Indium Phosphide $AXTI」（瓶颈中的瓶颈：磷化铟）。核心论点：光模块用的激光器离不开磷化铟衬底，而这个市场高度集中。

🔗 [原帖](https://x.com/aleabitoreddit/status/2005485130958430440) · 标签：#股票/AXTI

#### 2025-12-30 · AXTI：关键材料的博弈论
> [!summary] 概述
> - **涉及股票**：$AXTI
> - **指向性**：看多
> - **一句话**：WSB 那篇帖子说 AXTI 是半开玩笑，但 InP 的极端瓶颈和供应冲击是认真的；用历史上关键材料涨价的案例做类比

**内容**：「我发 WSB 帖子时，说 $AXTI 是半开玩笑，但极端瓶颈和 InP 供应冲击不是玩笑。这是一个关于关键材料博弈论的判断。看历史上的瓶颈：1. 镝：涨约 2,300%（2010～11 年从约 $100/kg 涨到 $2,400/kg）2. 钕……」

🔗 [原帖](https://x.com/aleabitoreddit/status/2005918544924664315) · 标签：#股票/AXTI

#### 2025-12-31 · Marvell
> [!summary] 概述
> - **涉及股票**：$MRVL、$MSFT
> - **指向性**：看多（中长期）
> - **一句话**：「终于认真研究了 MRVL」，微软 Maia 放量带来的收入是 MRVL 2025 财年营收的两倍

**内容**（据第三方转述）：「来自 Maia 放量的收入，简直是 $MRVL 2025 财年营收的两倍。」模型估算 2027 年 Marvell 能从微软 Maia 拿到 100～120 亿美元收入。

🔗 [原帖](https://x.com/aleabitoreddit/status/2006301094394335399) · 标签：#股票/MRVL

### 2026 年 1 月

#### 2026-01-02 · InP 衬底短缺与「价差套利」
> [!summary] 概述
> - **涉及股票**：$AXTI、$NVDA、$COHR、$LITE
> - **指向性**：看多
> - **一句话**：InP 和光学元件会变成「下一个 HBM」；起因是 NVDA 垄断了 COHR、LITE 的 EML 激光器产能

**内容**：「市场研究显示，InP 和光学元件会像 HBM 那样出现短缺和涨价狂潮。最初的瓶颈是 $NVDA 垄断了 $COHR 到 $LITE 的 EML 产能……」

🔗 [原帖](https://x.com/aleabitoreddit/status/2007202015940931878) · 标签：#股票/AXTI

#### 2026-01-30 · 闪迪财报后的受益者：群联、旺宏
> [!summary] 概述
> - **涉及股票**：$SNDK、群联（8299.TW）、旺宏（2337.TW）、Kioxia
> - **指向性**：看多（她持有群联、旺宏）
> - **一句话**：闪迪把 NAND 晶圆转向企业级 SSD，消费级留下的空缺由群联、旺宏填补

**内容**：「闪迪财报后，我持有的几个受益者：群联和旺宏。就像南亚科（1 年涨 1,035.96%）填补了美光、海力士、三星留下的传统 DRAM 空缺，群联也在用库存填补闪迪留下的 NAND 空缺……」她还提到闪迪向 Kioxia 支付 11.65 亿美元购买制造服务。

🔗 [原帖](https://x.com/aleabitoreddit/status/2017097752535322767) · 标签：#股票/SNDK

### 2026 年 2 月

#### 2026-02-07 · 回复网友：喜欢 Marvell，但目前没持有
> [!summary] 概述
> - **涉及股票**：$MRVL、$MSFT
> - **指向性**：看多，但当时未持有
> - **一句话**：MRVL 和微软 ASIC 放量绑定很深，还沾上了光互连（收购 Celestial 之后）；Maia 200 据报推迟约 6 个月

🔗 [原帖](https://x.com/aleabitoreddit/status/2019962908864925941) · 标签：#股票/MRVL

#### 2026-02-07 · AI 瓶颈全景图（Semivision 总结）
> [!summary] 概述
> - **涉及股票**：三星、SK 海力士、$MU、$SNDK、Kioxia、$TSM、$GLW、$INTC、Ibiden、$LITE、$AVGO、$COHR、$MRVL
> - **指向性**：看多（框架梳理）
> - **一句话**：把 AI 各环节的瓶颈和对应公司列成一张图

**内容**：HBM4 → 三星、海力士、美光；HBF → 闪迪、Kioxia；Base Die → 台积电；玻璃基板 → 康宁、英特尔、Ibiden；光学 → LITE、AVGO、COHR、MRVL；电力……

🔗 [原帖](https://x.com/aleabitoreddit/status/2020088575203721520) · 标签：#框架

#### 2026-02-09 · Credo：恐慌时买入一周涨 52%
> [!summary] 概述
> - **涉及股票**：$CRDO
> - **指向性**：看多（复盘）
> - **一句话**：$95 恐慌时买入，一周涨 52.6%；指引从 3.4 亿上调到 4.06 亿美元，大幅超预期

🔗 [原帖](https://x.com/aleabitoreddit/status/2020975054411137326) · 标签：#股票/CRDO

#### 2026-02-10 · 7N 高纯铟价格暴涨
> [!summary] 概述
> - **涉及股票**：$AXTI、$GOOGL
> - **指向性**：看多
> - **一句话**：7N 高纯铟突破每公斤 1,000 美元，三个月内抛物线上涨；中国控制 70%+ 供应链

🔗 [原帖](https://x.com/aleabitoreddit/status/2021028247476289890) · 标签：#股票/AXTI

#### 2026-02（具体日期未定位）· Raspberry Pi 交易点子
> [!summary] 概述
> - **涉及股票**：$RPI
> - **指向性**：看多
> - **一句话**：「好玩的交易点子：做多树莓派」，理由是 Openclaw / Picoclaw / Nanobot 等 AI 小设备的需求，加上囤货

**后续**：她预测营收增长 55%，分析师只预期 14%，实际是 58%。见 03-31。

标签：#股票/RPI

#### 2026-02-21 · 年初至今 +316.4% 的交易复盘
> [!summary] 概述
> - **涉及股票**：$GLXY、$SMCI、$IREN、$AVAV、$CVX 等
> - **指向性**：复盘
> - **一句话**：年初做税损收割后的反弹波段，再炒委内瑞拉相关股（Gold Reserve、AVAV、CVX 期权）

🔗 [原帖](https://x.com/aleabitoreddit/status/2025112091967811613)

#### 2026-02-24 · 年初至今 +412.72%，最喜欢的瓶颈多头 ⭐
> [!summary] 概述
> - **涉及股票**：三星、SK 海力士、$SNDK、$MU、$SIMO、$LITE、$COHR……
> - **指向性**：看多
> - **一句话**：收益主要来自选对板块、每周吃 Jane Street 算法的波动，再加一点运气；最喜欢的两大方向是存储和光通信

**内容**：「年初至今 412.72%。大部分靠选对板块、每周利用 Jane Street 的算法交易，再加一点运气。瓶颈多头里，目前最喜欢：1. 存储：三星、海力士、$SNDK、$MU、$SIMO 2. 光通信：$LITE、$COHR……」

🔗 [原帖](https://x.com/aleabitoreddit/status/2026341976942195152) · 标签：#股票/SNDK #股票/LITE

#### 2026-02-27 · IQE 深度分析
> [!summary] 概述
> - **涉及股票**：$IQE、LandMark、$IREN、$CRWV
> - **指向性**：看多
> - **一句话**：IQE 是全球最大的独立化合物半导体外延代工厂，市值只有 1.79 亿美元，而同类的 LandMark 估值 35 亿美元

**内容**：IQE 按反应炉数量和产能算是全球最大的独立外延代工厂，但被低利润的无线业务和短期资金压力拖累，估值处于困境水平。它的 Aixtron 反应炉可以兼做 GaAs/InP，每台改造成本约 50～150 万美元，需要几个月到一年。传导链：$AXTI → $IQE → $LITE → $GOOGL TPU。

**后续**：2026-04-12 她说 IQE 年初至今涨了 600%+。

🔗 [原帖](https://x.com/aleabitoreddit/status/2027318568728273305) · 标签：#股票/IQE

#### 2026-02-27 · AAOI 营收 10 倍，资金会往上游设备轮动
> [!summary] 概述
> - **涉及股票**：$AAOI、$LITE、$COHR、Aixtron（AIXA）、$VECO
> - **指向性**：看多
> - **一句话**：AAOI 预计到 2027 年光模块营收增长 10 倍，ARR 43 亿美元，而市值只有 55 亿；LITE 和 COHR 可能已经拥挤，资金会轮动到上游的「ASML 型」设备商

**内容**：Aixtron 在 InP MOCVD 设备上约占 75% 份额。

🔗 [原帖](https://x.com/aleabitoreddit/status/2027480850397573567) · 标签：#股票/AAOI

#### 2026-02-28 · MOCVD 设备商的「迷你 ASML 周期」
> [!summary] 概述
> - **涉及股票**：Aixtron（$AIXXF，37 亿美元）、$VECO（18.5 亿美元）
> - **指向性**：看多
> - **一句话**：光通信扩产会带来设备资本开支周期，Aixtron 和 Veeco 会受益

🔗 [原帖](https://x.com/aleabitoreddit/status/2027830093247300016)

### 2026 年 3 月

#### 2026-03-01 · Soitec 是硅光版的 AXTI ⭐
> [!summary] 概述
> - **涉及股票**：$SOI（Soitec，$SLOIF）、$AXTI、$POET
> - **指向性**：看多
> - **一句话**：做 800G/1.6T 和 CPO 绕不开两家：AXT 供应 InP，Soitec 供应光子 SOI 衬底；拐点在 2027 年底到 2028 年

**内容**：她还提到 POET 账上有 4 亿美元现金，但更偏好 Soitec，会把仓位集中到 Soitec。

🔗 [原帖](https://x.com/aleabitoreddit/status/2028203665430057068) · 标签：#股票/SOI

#### 2026-03-10 · NAND 价格失控
> [!summary] 概述
> - **涉及股票**：$SNDK、$MU、三星、SK 海力士
> - **指向性**：看多
> - **一句话**：NAND 价格已经失控上涨，供给缺乏弹性，存储厂最受益

**内容**：引用群联 CEO 在 Digitimes 上的话：NAND 价格因供给收紧而飙升。

🔗 [原帖](https://x.com/aleabitoreddit/status/2031272426961776663) · 标签：#股票/SNDK

#### 2026-03-13 · 光通信论点总览：「最安全」的三只
> [!summary] 概述
> - **涉及股票**：$TSEM、$SOI、$COHR
> - **指向性**：看多（偏稳健）
> - **一句话**：发过的光通信供应链股大多涨了 100～400%+；「最安全」的多头是 Tower、Soitec、Coherent，属于能长期复利的公司

**内容**：Tower：2028 年市盈率只有十几倍，70%+ 产能已被预订，是 NVDA 的架构合作伙伴，「光通信界的纯正台积电」。Coherent：从材料、衬底、激光器到光模块全都做。

🔗 [原帖](https://x.com/aleabitoreddit/status/2032577275439485080) · 标签：#股票/TSEM #股票/SOI #股票/COHR

#### 2026-03-16 · Soitec 5 天涨 44%
> [!summary] 概述
> - **涉及股票**：$SOI
> - **指向性**：看多（复盘）
> - **一句话**：发论点 5 天，Soitec 涨了 44.3%，「这是市场在实时给下一个关键光通信公司重新定价」

🔗 [原帖](https://x.com/aleabitoreddit/status/2033512244244529396) · 标签：#股票/SOI

#### 2026-03-17 · Sivers 单日涨 73.78%：下一个 LITE？
> [!summary] 概述
> - **涉及股票**：$SIVE、$LITE
> - **指向性**：看多
> - **一句话**：Sivers 当天涨 73.78%，市值 2.31 亿美元；LITE 的激光器受益于当前的光通信瓶颈，Sivers 的激光器则面向下一代 CPO

🔗 [原帖](https://x.com/aleabitoreddit/status/2033695716938551350) · 标签：#股票/SIVE

#### 2026-03-17 · 光通信超级周期来了
> [!summary] 概述
> - **涉及股票**：$NVDA、$SOI、$SIVE
> - **指向性**：看多
> - **一句话**：NVDA 正在推动 CPO 和硅光的下一次飞跃，现在只是接近拐点；Soitec、Sivers 是供应链里的卡脖子环节

🔗 [原帖](https://x.com/aleabitoreddit/status/2034056688693875036)

#### 2026-03-18 前后 · 自报 +943% 登上 X 热搜
> [!summary] 概述
> - **涉及股票**：$AXTI、$SNDK
> - **指向性**：复盘
> - **一句话**：X 热门话题报道她晒出 943% 收益，主要来自 AXTI（$12 → $48）和 SNDK（$220 → $772），同期标普 500 只涨 1～2%

🔗 [X 热门话题](https://x.com/i/trending/2034331623664095415)

#### 2026-03-26 · 「什么时候才肯承认我的论点是对的？」
> [!summary] 概述
> - **涉及股票**：$AXTI、$IQE、$SIVE、$LITE
> - **指向性**：复盘
> - **一句话**：做多的这些光通信股过去几个月涨了 100～1000%，回应质疑者

🔗 [原帖](https://x.com/aleabitoreddit/status/2037027934125346976)

#### 2026-03-30 · 「我抓准了机构的瓶颈轮动」
> [!summary] 概述
> - **涉及股票**：$SNDK、三星、海力士、$MU、$AAOI、$AXTI、$LITE、$COHR
> - **指向性**：看多（轮动判断）
> - **一句话**：存储股只吃到尾段 → 光通信抢在机构前面 → 现在又在加仓硅光（SiPh）

🔗 [原帖](https://x.com/aleabitoreddit/status/2038440978777034988)

#### 2026-03-31 · Raspberry Pi 财报后涨 44.76%
> [!summary] 概述
> - **涉及股票**：$RPI
> - **指向性**：看多（论点验证）
> - **一句话**：财报后单日涨 44.76%（次日再涨 27.43%）；2027 年市盈率只有 11～13 倍，前瞻增速 58%，远高于预期的 14%

🔗 [原帖](https://x.com/aleabitoreddit/status/2038965788724560093) · 标签：#股票/RPI

### 2026 年 4 月

#### 2026-04-01 前后 · Sivers：最高信心的新兴股（第三方长文）
> [!summary] 概述
> - **涉及股票**：$SIVE、$POET、$MRVL、$AVGO
> - **指向性**：看多（最高信心）
> - **一句话**：Sivers 市值约 2.9 亿美元，「严重错误定价」，因为它掌握下一代 CPO 的 CW 激光光源；还可能被博通收购，以此卡住 Marvell 的供应链

**内容**（据 Singularity Research 的长文转述）：传导链「$SIVE → 赢下订单 → $POET → Celestial → $MRVL」。营收预测：2026～2027 年约为 0，亏损约 5,000 万美元；2028 年 5 亿美元；2029 年 10 亿美元。

**后续**：2026-05-25，Singularity Research 说 Sivers 自文章发布后涨了约 700%。

🔗 [Singularity Research](https://x.com/SingularityRes/status/2039192597227549100) · [后续](https://x.com/SingularityRes/status/2059014327118794769) · 标签：#股票/SIVE

#### 2026-04-06 · 别用 2025～26 年营收给 CPO 公司估值
> [!summary] 概述
> - **涉及股票**：$TSEM、$AEHR、$SIVE、$SOI、稳懋（Win Semi）
> - **指向性**：看多（估值方法）
> - **一句话**：Tower 在 $115 时，远期市盈率会压缩到 16～18 倍，增长情景下是 10～12 倍；CPO 公司要看远期

**后续**：她说 Tower 后来涨到约 $200。

🔗 [原帖](https://x.com/aleabitoreddit/status/2041038963859931593) · 标签：#股票/TSEM

#### 2026-04-06 · 新瓶颈：变压器和开关柜 ⭐
> [!summary] 概述
> - **涉及股票**：$HPS.A（Hammond Power）、$AMZN、$MSFT
> - **指向性**：看多（交易点子）
> - **一句话**：在 184 加元做多 Hammond（约 15 亿美元市值）；干式变压器是多年瓶颈，预计会像 NAND 一样涨价

**内容**：Hammond 在干式变压器（约 23% 份额，多年瓶颈）、开关柜（2～3 年瓶颈）、液浸式变压器（5 年瓶颈）都有布局，2025 年订单积压同比增长 122%。

🔗 [原帖](https://x.com/aleabitoreddit/status/2041168871168545115) · 标签：#股票/HPS

#### 2026-04-07 · 多年瓶颈让人睡得安稳
> [!summary] 概述
> - **涉及股票**：$HPS.A、$SNDK、$LITE
> - **指向性**：看多
> - **一句话**：从 Hammond 到闪迪再到 LITE，都是多年瓶颈，即使市场波动，一年后需求依然会很极端

🔗 [原帖](https://x.com/aleabitoreddit/status/2041519692985344500) · 标签：#股票/SNDK #股票/LITE

#### 2026-04-08 · Coherent 和 Marvell 是半导体界的「德勤」
> [!summary] 概述
> - **涉及股票**：$COHR、$MRVL
> - **指向性**：看多
> - **一句话**：这两家「什么都做」，但没人说得清它们做什么；都是未来一年很扎实的盈利型多头，**50～100% 涨幅是合理预期**

🔗 [原帖](https://x.com/aleabitoreddit/status/2041963517071519963) · 标签：#股票/MRVL #股票/COHR

#### 2026-04-09 · 30 只喜欢的美股
> [!summary] 概述
> - **涉及股票**：$INTC、$MRVL、$TSM、$COHR 等 30 只
> - **指向性**：看多
> - **一句话**：INTC 是「美国代工的希望、国家安全」；MRVL 靠未来的 Maia ASIC 和 CPO 等附加业务扩大营收

🔗 [原帖](https://x.com/aleabitoreddit/status/2042187668931616964) · 标签：#股票/MRVL

#### 2026-04-09 · Hammond 只涨了 17%
> [!summary] 概述
> - **涉及股票**：$HPS.A、$POWL
> - **指向性**：看多（自嘲）
> - **一句话**：「不是我所有的股票都能一周涨三位数」；Powell（POWL）是另一只不错的开关柜多头

🔗 [原帖](https://x.com/aleabitoreddit/status/2042345236354265271) · 标签：#股票/HPS

#### 2026-04-12 · IQE 年初至今涨 600%+
> [!summary] 概述
> - **涉及股票**：$IQE
> - **指向性**：复盘
> - **一句话**：当初很多人说 IQE 是「拉高出货」，现在年初至今涨 600%+，机构随后也买入了

🔗 [原帖](https://x.com/aleabitoreddit/status/2043315043455176826) · 标签：#股票/IQE

#### 2026-04-14 / 04-16 / 04-21 · Soitec 一个月涨 64% → 140%
> [!summary] 概述
> - **涉及股票**：$SOI、$SIVE、$ALRIB（Riber）、$RPI
> - **指向性**：复盘
> - **一句话**：Soitec 发论点后一个月涨 64%，后来扩大到 140%（年初至今 +302%）；这是她第 16 只发过小论点、年内翻倍的股票

**内容**：她引用 Soitec 副总裁的话：「Soitec 的光子 SOI 产品用在 100% 的下一代 AI 数据中心里。」

🔗 [04-14](https://x.com/aleabitoreddit/status/2044077799338881108) · [04-16](https://x.com/aleabitoreddit/status/2044822095931306149) · [04-21](https://x.com/aleabitoreddit/status/2046408704573292659) · 标签：#股票/SOI

#### 2026-04-22 · 机构跟进 IQE，瑞典媒体唱空 SIVE
> [!summary] 概述
> - **涉及股票**：$IQE、$SIVE、$AXTI
> - **指向性**：看多
> - **一句话**：UBS、Point72 等机构在她发论点后买入 IQE；她很有信心机构也会跟进 SIVE

🔗 [原帖](https://x.com/aleabitoreddit/status/2046906948088435024) · 标签：#股票/IQE #股票/SIVE

### 2026 年 5 月

#### 2026-05-10 · 「还记得我去年的 AXTI 瓶颈判断吗？」
> [!summary] 概述
> - **涉及股票**：$AXTI
> - **指向性**：复盘（论点验证）
> - **一句话**：英特磊（IntelliEPI）CEO 在 Q1 财报会上说「InP 衬底短缺是整个 AI 基础设施的瓶颈」，比她晚了一年

🔗 [原帖](https://x.com/aleabitoreddit/status/2053270948414099915) · 标签：#股票/AXTI

#### 2026-05-22 · Sivers 是 CPO 的「造王者」
> [!summary] 概述
> - **涉及股票**：$SIVE、$MRVL、世芯（Alchip）、创意（GUC）、O-Net、Jabil
> - **指向性**：看多
> - **一句话**：从 Lightmatter、Celestial、Ayar 到 Marvell 的 ASIC 生态，Sivers 都是光源供应商；O-Net 和 Jabil 在量产

🔗 [原帖](https://x.com/aleabitoreddit/status/2057720796613873805) · 标签：#股票/SIVE

#### 2026-05-27 · X-Fab：单日暴涨 70%+，Bloomberg 报道 ⭐
> [!summary] 概述
> - **涉及股票**：$XFAB、$NVDA、$NVTS、$POWI、$SOI
> - **指向性**：看多（她已建仓）
> - **一句话**：X-Fab 市值 12.8 亿美元，兼有硅光和功率半导体，欧盟芯片法案 2.0 是催化剂；发帖当天股价最多涨 76%

**内容**：「$XFAB（光子 + 功率半导体）是一个有意思的多头，市值 12.8 亿美元，我已经建仓。欧盟芯片法案 2.0 是欧洲光通信公司的催化剂。> 通过 NVTS、POWI 间接受益于 NVDA 的 800V 直流电源 > 硅光/CPO 方面，NVDA 正在评估量产 > 美国唯一的大规模 SiC 代工厂 > 关键的 MEMS 代工厂 > 市净率约 1.29……」

🔗 [原帖](https://x.com/aleabitoreddit/status/2059537337324085541) · [Bloomberg 报道](https://www.bloomberg.com/news/articles/2026-05-27/popular-x-account-sparks-massive-rally-in-little-known-chipmaker) · 标签：#股票/XFAB

#### 2026-05-27 · SIVE、SOI、XFAB 都在欧盟产业政策蓝图里
> [!summary] 概述
> - **涉及股票**：$SIVE、$SOI、$XFAB、$IQE
> - **指向性**：看多
> - **一句话**：她的欧洲多头（除了 IQE）都被列入了指导欧盟立法的产业政策蓝图，可能获得芯片法案 2.0 的资金

🔗 [原帖](https://x.com/aleabitoreddit/status/2059561586956837085)

#### 2026-05-28 · 回应 Reuters 和 Bloomberg 的报道
> [!summary] 概述
> - **涉及股票**：$XFAB、$NVDA、$NOK
> - **指向性**：看多
> - **一句话**：感谢比较中立的报道，但希望媒体多关注结构性论点，而不是股价

🔗 [原帖](https://x.com/aleabitoreddit/status/2059848338028241193) · 标签：#股票/XFAB

### 2026 年 6 月

#### 2026-06-01 · AAOI 是美股最喜欢的光通信股 ⭐
> [!summary] 概述
> - **涉及股票**：$AAOI、$AMZN、$MSFT
> - **指向性**：看多
> - **一句话**：$28 小仓位试探，$70 财报后加到高信心，现在 $150；「如果你想找下一个 SNDK，就是它」

**内容**：「$AAOI 是我目前在美股最喜欢的光通信标的。去年在 $28 小仓位做多，当时猜他们在给亚马逊和微软送样认证。财报后在约 $70 建立高信心，因为他们宣布了 1.6T 和超大客户的批量订单……现在 $150。」同一天她说 AAOI 当日涨 20.1%：「我认为 2027 年上半年到下半年会是光通信公司的巨大拐点，现在进入 2026 下半年，只是稍微早了一点。」

🔗 [原帖 1](https://x.com/aleabitoreddit/status/2061252644195504239) · [原帖 2](https://x.com/aleabitoreddit/status/2061498698098708676) · 标签：#股票/AAOI

#### 2026-06-03 · 欧洲科技主权一揽子计划发布
> [!summary] 概述
> - **涉及股票**：$XFAB、$SIVE
> - **指向性**：看多
> - **一句话**：6 月 3 日欧盟发布科技主权计划，包含优先支持光通信的芯片法案 2.0；X-Fab 和 Sivers 都被点名

**内容**：她估计光通信相关股会在法案发布后 3～15 个月内逐步受益。

🔗 [原帖](https://x.com/aleabitoreddit/status/2062045895500419101)

#### 2026-06-03 · Nebius 是 Neocloud 之王
> [!summary] 概述
> - **涉及股票**：$NBIS、$IREN、$CRWV
> - **指向性**：复盘（论点验证）
> - **一句话**：去年写了 Neocloud 板块论点，最后集中押 Nebius；从 $84 涨到 $260，是板块第一

🔗 [原帖](https://x.com/aleabitoreddit/status/2062116398210703462) · 标签：#股票/NBIS

#### 2026-06-05 · 从 $28 一路加仓 AAOI
> [!summary] 概述
> - **涉及股票**：$AAOI
> - **指向性**：看多
> - **一句话**：800G/1.6T 光模块需求太大，觉得「执行到位的话翻倍甚至三倍是必然的」

🔗 [原帖](https://x.com/aleabitoreddit/status/2062697638500462639) · 标签：#股票/AAOI

#### 2026-06-07 · 自述投资风格
> [!summary] 概述
> - **涉及股票**：$AXTI、$RPI、$SIVE、$IQE
> - **指向性**：方法论
> - **一句话**：风格本质上是主观判断，基于「市场还不知道的东西」，很多是对非结构化信息的推测，也是人生经验的积累

🔗 [原帖](https://x.com/aleabitoreddit/status/2063465386960736396)

#### 2026-06-08 · 绿的谐波：中国机器人零部件龙头
> [!summary] 概述
> - **涉及股票**：绿的谐波（688017）、$TSLA（Optimus 供应链）
> - **指向性**：看多
> - **一句话**：研究过很多机器人和特斯拉 Optimus 供应商，绿的谐波非常独特，不是做低毛利组装或低价值零件

**补充**（06-09）：她说之前唯一推荐过的 A 股是中际旭创（Innolight），已经涨到历史新高。

🔗 [原帖](https://x.com/aleabitoreddit/status/2063851425462173726) · [06-09](https://x.com/aleabitoreddit/status/2064221488878846124)

#### 2026-06-12 · 2025 年高信心股复盘
> [!summary] 概述
> - **涉及股票**：$ALAB、$LITE、$AAOI、$NBIS、$RKLB、$TSM
> - **指向性**：复盘
> - **一句话**：ALAB $97 → $372，LITE $330 → $904，AAOI $30 → $175；那时她几乎没有粉丝

🔗 [原帖](https://x.com/aleabitoreddit/status/2065289672356745561)

#### 2026-06-16 · 市值对比：2025 年 → 现在
> [!summary] 概述
> - **涉及股票**：$AAOI、$LITE、$AXTI
> - **指向性**：复盘
> - **一句话**：AAOI 20 亿 → 153.7 亿美元，Lumentum 260 亿 → 744.7 亿，AXT 5 亿 → 72.4 亿

🔗 [原帖](https://x.com/aleabitoreddit/status/2066785056031670657)

#### 2026-06-23 · 暴跌日：AI 芯片股集体重挫
> [!summary] 概述
> - **涉及股票**：$IQE −13.6%、$AXTI −12.6%、$SNDK −12.5%、$MU −11.8%、$AAOI −11.2%、$SIVE −11.7%、$TSEM −10.2%、$MRVL −8.3%、$LITE −7.6% 等
> - **指向性**：复盘（风险事件）
> - **一句话**：「今天有谁的组合是绿的吗？」存储、光通信、韩国和台湾股一起大跌

🔗 [原帖](https://x.com/aleabitoreddit/status/2069445918114697463)

#### 2026-06-25 · 「分散化亏损」：坦承大回撤 ⚠️
> [!summary] 概述
> - **涉及股票**：$AXTI、$SOI、$AAOI，以及 CPO 相关的 Foci、Msscorp
> - **指向性**：复盘（反思）
> - **一句话**：最近大回撤，CPO 相关跌得最狠；自嘲策略是「分散化亏损」，承认某类仓位太重了

🔗 [原帖](https://x.com/aleabitoreddit/status/2069967746377662587)

### 2026 年 7 月

#### 2026-07-02 · 光通信 vs 量子计算
> [!summary] 概述
> - **涉及股票**：$LITE、$NVDA、$POET
> - **指向性**：看多光通信
> - **一句话**：光通信有真实营收，是 NVDA 推动的架构变革，量子计算几乎没有营收；据 POET 股东会，LITE 未来 2 年产能已售罄，可能持续到 2029 年

🔗 [原帖](https://x.com/aleabitoreddit/status/2072726120706007465) · 标签：#股票/LITE

#### 2026-07-03 · 讽刺 SemiAnalysis
> [!summary] 概述
> - **涉及股票**：光通信板块
> - **指向性**：看多（反驳空头）
> - **一句话**：SemiAnalysis 先发文唱衰 CPO 进度和光通信估值，引发暴跌（NVDA、分析师和光通信公司都反驳了），等光通信股跌了 40～60% 后，又推出机构版光通信 ETF

🔗 [原帖](https://x.com/aleabitoreddit/status/2072936659369517341)

#### 2026-07-07 · 无差别抛售与基本面无关
> [!summary] 概述
> - **涉及股票**：$NBIS、$MRVL、$INTC、$SNDK、$AMD、$SIVE、$MU、$LITE
> - **指向性**：看多（持股不动）
> - **一句话**：这些股今天一起跌 4～10%+，可能和各自基本面无关，而是流动性稀薄下的无差别抛售

🔗 [原帖](https://x.com/aleabitoreddit/status/2074494514061017508)

#### 2026-07（原帖未定位）· 披露 −49.4% 回撤
> [!summary] 概述
> - **涉及股票**：存储、光通信、机器人、上游半导体
> - **指向性**：复盘（风险披露）
> - **一句话**：约 1.4 倍杠杆，底层持仓跌约 35%，账户回撤约 49.4%；她认为原因是韩国大量保证金账户被强平引发的流动性和杠杆踩踏，而不是基本面变坏

**内容**（据第三方汇总）：「如果我预计营收拐点在 2027 年下半年，而现在还是 2026 年，那我的论点就不算错。」她强调自己持股周期更长，对波动的容忍度更高。

> [!danger] 值得记住的教训
> 即使是选股很准的人，**加了杠杆**之后，一次板块级暴跌就能让账户腰斩。

#### 2026-07-29 · AXTI 和 Lumentum 签长期供货协议
> [!summary] 概述
> - **涉及股票**：$AXTI、$LITE
> - **指向性**：看多（论点验证）
> - **一句话**：Lumentum 支付 4,350 万美元押金，预订 AXT 的 InP 衬底产能

🔗 [原帖](https://x.com/aleabitoreddit/status/2082578803189268855) · 标签：#股票/AXTI #股票/LITE

### 2026 年 8 月

#### 2026-08-04 · 存储 2027 年产能已售罄
> [!summary] 概述
> - **涉及股票**：SK 海力士、$MU、三星、$SNDK、Kioxia
> - **指向性**：看多
> - **一句话**：三大厂 2027 年 DRAM/HBM 产能已经卖完；闪迪、三星、美光当年的 NAND 产能也卖完了；客户只能拿到所需量的 60～70%

**内容**：业内认为 2027 年会是存储短缺最严重的时候。

🔗 [原帖](https://x.com/aleabitoreddit/status/2084468063228060092) · 标签：#股票/SNDK

#### 2026-08-06（第三方统计）· AAOI 从高点跌 62% 时一路看多
> [!summary] 概述
> - **涉及股票**：$AAOI
> - **指向性**：看多（逆势坚持）
> - **一句话**：AAOI 从 6 月高点跌了 62%，她期间发了 16 次看多、0 次看空；8 月 6 日财报后，股价从低点反弹 80%

来源：Quantral 评分。标签：#股票/AAOI

### 2026 年 9 月

#### 2026-09 上旬（原帖未定位）· NOR Flash 涨价
> [!summary] 概述
> - **涉及股票**：晶豪科（ESMT）、华邦、兆易创新、旺宏
> - **指向性**：看多
> - **一句话**：高容量 NOR（256Mb 以上）下半年可能再涨 90～110%；她认为相对体量受益最大的是晶豪科（ESMT），TrendForce 则点名华邦、兆易创新、旺宏。「让 ASP 涨价游戏继续吧。」

来源：Serenity 追踪网站（2026-09-14 更新）。

#### 2026-09-20 · ECOC 光通信展期间
> [!summary] 概述
> - **涉及股票**：$LITE、$MRVL、$SIVE
> - **指向性**：中性（闲聊）
> - **一句话**：大家都在关注中美会谈和 ECOC 展会上的 LITE、MRVL、SIVE；她吐槽中文帖评论 2,000+，英文帖只有 50 条

🔗 [原帖](https://x.com/aleabitoreddit/status/2101730902615486643)

#### 2026-09-24 · Nebius 逆势上涨
> [!summary] 概述
> - **涉及股票**：$NBIS、$IREN、$CRWV
> - **指向性**：看多
> - **一句话**：板块下跌时 Nebius 还涨了 6%，相对表现很强；当初顶着批评把 Neocloud 仓位集中到 Nebius

🔗 [原帖](https://x.com/aleabitoreddit/status/2103139052363133062) · 标签：#股票/NBIS

### 2026 年 10 月

#### 2026-10-02 · Lumentum CEO：2027 年只能满足 30% 需求
> [!summary] 概述
> - **涉及股票**：$LITE
> - **指向性**：看多
> - **一句话**：引用 Lumentum CEO 的话：随着 2027 年 CPO/NPO 到来，供给会比需求少 70%，只能满足 30%，要到 2029～2030 年才平衡

🔗 [原帖](https://x.com/aleabitoreddit/status/2105943565918703696) · 标签：#股票/LITE

---

## 六、主题小结

### 1. 光通信（她最核心的方向）
- **主线**：AI 数据中心的光互连需求暴增 → 激光器产能不够 → 上游衬底、外延、设备也跟着紧张。
- **从下游到上游的标的**：LITE、AAOI、COHR（光模块）→ SIVE（CPO 光源）→ TSEM、XFAB（硅光代工）→ IQE（外延）→ AXTI、SOI（衬底）→ Aixtron、VECO（设备）。
- **时间判断**：她多次说 2027 年下半年才是真正的业绩拐点，2026 年属于提前布局。

### 2. 存储
- **主线**：AI 推动存储「超级周期」，产能售罄、涨价、长约预付。
- **标的**：SNDK、MU、三星、SK 海力士，延伸到群联、旺宏、NOR Flash。
- 第三方资料称：她的闪迪仓位约占组合 5%（存储总配置约 35%），信心 8/10。

### 3. 和你关注的股票的关系
- **闪迪（SNDK）**：是她回测里第二大赢家（+516%），她认为 NAND 短缺会持续到 2027～2028 年。
- **Marvell（MRVL）**：她一直**中长期看多**，理由是微软 Maia ASIC 放量和光互连。但她的定位是「扎实的盈利型多头，一年 50～100% 合理」，**不算她最高信心的核心仓**。2026 年 2 月她还说过暂时没持有。

### 4. 跟踪时要注意
1. 她**提到的股票非常多**（10 个月 383 只），整体等权买入反而跑输半导体 ETF。只看她反复论证的高信心标的。
2. 她用**杠杆**，波动极大，2026 年 7 月回撤近一半。
3. 她的帖子本身会**带动小盘股暴涨**（X-Fab 单日 +76%）。看到帖子再追，往往买在情绪高点。
4. 自报收益**无法审计**，第三方统计的准确率约 60%。

---

## 七、来源

**原帖**：见各条目里的 🔗 链接（x.com/aleabitoreddit/status/…）

**媒体报道和第三方分析**：
- [Bloomberg – X-Fab Rises After Serenity Post on X（2026-05-27）](https://www.bloomberg.com/news/articles/2026-05-27/popular-x-account-sparks-massive-rally-in-little-known-chipmaker)
- [Invezz – X-FAB climbs sharply after viral social media-driven buying surge](https://invezz.com/news/2026/05/27/x-fab-climbs-sharply-after-viral-social-media-driven-buying-surge/)
- [Bitget – Serenity: Photonics stocks may benefit 3–15 months after EU CHIPS Act](https://www.bitget.com/news/detail/12560605442409)
- [Quantral – Who is aleabitoreddit? Serenity's graded record](https://quantral.com/blog/who-is-aleabitoreddit)
- [fxcryptobots – Serenity Backtest v3: 383 BULL Picks vs XSD](https://fxcryptobots.com/research-aleabit-backtest-v3)
- [Singularity Research – Inside the Mind of Serenity](https://singularityresearchfund.substack.com/p/inside-the-mind-of-serenity-aleabitoreddit)
- [BearSavings – Who Is Serenity (@aleabitoreddit)?](https://www.bearsavings.com/blog/who-is-serenity-aleabitoreddit/)
- [KuCoin – Who Is Serenity? AI Supply Chain Guru](https://www.kucoin.com/blog/Who-Is-Serenity_)
- [Futu – Understanding the investment logic of Serenity](https://news.futunn.com/en/post/73854711/who-is-serenity-understanding-the-investment-logic-of-the-godfather)
- [moomoo – The "AI Chokepoint": Who is Serenity](https://www.moomoo.com/community/feed/the-ai-chokepoint-who-is-serenity-and-what-is-on-116679539425286)
- [moomoo – @aleabitoreddit 背景](https://www.moomoo.com/community/feed/here-s-the-backstory-on-the-twitter-account-aleabitoreddit-x-116401268326405)
- [Serenity Tracker（leopoldstocks.com）](https://leopoldstocks.com/)
- [Serenity Tracker – $SNDK](https://serenitytrades.com/universe/sndk)
- [X 热门话题 – Trader Serenity Posts 943% Returns](https://x.com/i/trending/2034331623664095415)
- [Lookonchain – Meet the new stock legend: Serenity](https://x.com/lookonchain/status/2060291742910619878)
