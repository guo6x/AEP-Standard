# ⚡️ AEP (Agentic Edge Protocol)
**The Native Physical Execution Standard for LLMs | 专为大模型打造的本地物理执行标准**

[![Status: Draft](https://img.shields.io/badge/Status-Draft-orange.svg)]()
[![Hardware: ESP32-S3](https://img.shields.io/badge/Reference_Hardware-ESP32--S3-blue.svg)]()
[![Ecosystem: Omni-Context](https://img.shields.io/badge/Ecosystem-Omni--Context-success.svg)]()

## 🚨 The Broken Reality：为什么现在的 IoT 是“伪智能”？

目前的智能家居（如 Home Assistant、各类全家桶生态）本质上是**巨型的遥控器与死板的触发器**。
它们建立在 `If-This-Then-That` (IFTTT) 的机械逻辑上，缺乏对用户真实意图和全局上下文（Omni-Context）的理解。当你正在深度心流状态下写代码时，定时任务依然会像个智障一样突然关掉你的主灯；当你因为生病觉得冷时，温度传感器依然会死板地在 28 度打开冷气。

**脱离了全局上下文的硬件，就是一堆毫无生机的废铁。自动化 ≠ 智能化。**

## 💡 The Vision：让大模型长出“物理神经”

如果说近期爆发的 **MCP (Model Context Protocol)** 解决了大模型如何“感知”软件世界的问题，那么 **AEP (Agentic Edge Protocol)** 要解决的就是大模型如何**“干涉”物理世界**的问题。

AEP 是一套极轻量级、AI-Native 的边缘设备控制规范。我们主张：
* **Zero-Trust Physical Execution (零信任物理执行)：** 抛弃臃肿的中心化网关和封闭的云端生态。
* **LLM Direct Call (大模型直连)：** 让任何一块成本不到 10 元的单片机（如 ESP32），都能通过极简的协议，直接听懂大模型的 JSON 语义指令。
* **Context-Aware (上下文感知)：** 硬件不再是孤岛，而是作为 Omni-Context（全能上下文中枢）的物理切片，根据主人的实时状态（专注、休息、甚至情绪）做出动态响应。

## 🏗 Core Architecture (核心架构设计)

AEP 将整个系统剥离为极其纯粹的两层：
1.  **🧠 赛博大脑层 (The Brain)：** 运行在本地（PC/Mac/树莓派）的 Agent 框架，负责融合数字世界的上下文并进行逻辑推理，通过 MCP 协议生成动作意图。
2.  **🦾 物理触角层 (The Edge Nodes)：** 散布在桌面的 ESP32/RP2040 节点。它们没有算力焦虑，只需暴露标准的 AEP 接口，毫秒级执行大脑下发的声/光/电/机械指令。

*(目前，我们已基于 Node.js Agent 架构与 ESP32-S3 成功跑通第一版 HTTP API 规范草案，实现了基于自然语言推理的桌面光环境重构。)*

## 🤝 Call to Contributors & Hardware Partners (招募与合作)

AEP 目前处于早期的协议起草与 MVP 验证阶段。改变物理世界的交互标准，需要极客先驱们的共同努力。我们正在寻找：

* **💻 开源贡献者：** 欢迎提交 PR，参与制定 AEP 的标准化 JSON 载荷规范、本地鉴权机制与 WebRTC/WebSocket 混合通讯层。
* **🧰 官方硬件生态伙伴 (Reference Hardware)：** 我们正在挑选第一批原生支持 AEP 协议的官方推荐开发板。如果您是开源硬件厂商（如 Espressif 乐鑫、Seeed 硅递、M5Stack 等），并拥有带屏幕、传感器阵列的高性能 MCU，欢迎联系我们（请附上设备赞助意向），我们将为您提供深度的底层协议适配，共同抢占 AI 硬件的下一个时代标准。

**Join us. Let's give AI a physical body.**
