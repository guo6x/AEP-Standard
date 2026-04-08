# ⚡️ AEP (Agentic Edge Protocol)

**The Native Physical Execution Standard for LLMs | 专为大模型打造的本地物理执行标准**

[![English](https://img.shields.io/badge/Language-English-blue.svg)](README.md) [![简体中文](https://img.shields.io/badge/语言-简体中文-red.svg)](#)

[![Status: Draft](https://img.shields.io/badge/Status-Draft-orange.svg)]()
[![Hardware: ESP32-S3](https://img.shields.io/badge/Reference_Hardware-ESP32--S3-blue.svg)]()
[![Ecosystem: OpenClaw](https://img.shields.io/badge/Ecosystem-OpenClaw-success.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](#)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> 关键词: `Agentic AI`, `LLM Hardware`, `ESP32 LLM`, `MCP IoT`, `Open Source Protocol`, `大模型物理执行`, `边缘计算`

## 🚨 The Broken Reality：为什么现在的 IoT 是“伪智能”？

目前的智能家居（如 Home Assistant、各类全家桶生态）本质上是**巨型的遥控器与死板的触发器**。
它们建立在 `If-This-Then-That` (IFTTT) 的机械逻辑上，缺乏对用户真实意图和全局上下文的理解。当你正在深度心流状态下写代码时，定时任务依然会像个智障一样突然关掉你的主灯；当你因为生病觉得冷时，温度传感器依然会死板地在 28 度打开冷气。

**脱离了全局上下文的硬件，就是一堆毫无生机的废铁。自动化 ≠ 智能化。**

## 💡 The Vision & Positioning：为什么我们需要 AEP？

如果说近期爆发的 **MCP (Model Context Protocol)** 解决了大模型如何“感知”软件世界的问题，那么 **AEP (Agentic Edge Protocol)** 要解决的就是大模型如何**“干涉”物理世界**的问题。

**目前的行业痛点与我们的差异化：**
我们注意到社区内已经出现了如 `tinymcp`、`esp-mcp` 等优秀的早期探索，试图将 MCP 协议直接引入单片机。但经过实测，这些方案往往需要繁琐的 C++ 编译环境，或者强依赖复杂的 MQTT 消息代理，**对边缘节点来说太重了**。

AEP 的定位截然不同。它是一套专为 Sub-$2（十几块钱以内）极低配单片机设计的**超轻量级物理层影子协议**。我们主张：

* **Ultra-Lightweight (极度轻量)：** 0 依赖，抛弃 MQTT 和复杂的网关。一行纯净的 HTTP/JSON API 代码（甚至只需 MicroPython），就能让 ESP32 瞬间接入大模型网络。
* **Zero-Trust Physical Execution (零信任物理执行)：** 大脑（Agent）在本地电脑/树莓派进行高阶推理，物理节点（ESP32）绝不参与思考，只负责毫秒级的被动执行。
* **LLM Direct Call (大模型直连)：** 直接映射为大模型原生的 Tool-Call 机制，让硬件真正变成 AI 的神经末梢。
* **🔌 即插即用 (Zero-Conf):** 彻底告别静态 IP 与硬编码，设备上电即被网关捕获，拔电即隐身，动态映射大模型工具。

## 🏗 Core Architecture (核心架构设计)

AEP 将整个系统剥离为极其纯粹的两层：

1. **🧠 赛博大脑层 (The Brain)：** 运行在本地（PC/Mac/树莓派）的 Agent 框架，负责融合数字世界的上下文并进行逻辑推理，通过 MCP 协议生成动作意图。
2. **🦾 物理触角层 (The Edge Nodes)：** 散布在桌面的 ESP32/RP2040 节点。它们没有算力焦虑，只需暴露标准的 AEP 接口，毫秒级执行大脑下发的声/光/电/机械指令。

> *[架构图占位符]*

*(目前，我们已基于 Node.js Agent 架构与 ESP32-S3 成功跑通第一版 HTTP API 规范草案，实现了基于自然语言推理的桌面光环境重构。)*

## 🚀 Quick Start & Documentation (极速上手)

AEP 的核心引擎与规范白皮书现已开源发布！让单片机接入大模型只需 3 行核心代码：

- 📄 **阅读宪法级协议规范**：👉 [AEP_Specification_v0.2.md](./docs/AEP_Specification_v0.2.md)
- 🛠️ **获取核心物理引擎 SDK**：👉 [aep_core.py](./src/aep_core.py)
- 💡 **查看 ESP32 实战点灯 Demo**：👉 [examples/esp32_basic/main.py](./examples/esp32_basic/main.py)

## 🤝 Call to Contributors & Hardware Partners (招募与合作)

AEP 目前处于早期的协议起草与 MVP 验证阶段。改变物理世界的交互标准，需要极客先驱们的共同努力。我们正在寻找：

* **💻 开源贡献者：** 欢迎提交 PR，参与制定 AEP 的标准化 JSON 载荷规范、本地鉴权机制与 WebRTC/WebSocket 混合通讯层。详情请查看 [贡献指南](CONTRIBUTING.md)。
* **🧰 官方硬件生态伙伴 (Reference Hardware)：** 我们正在挑选第一批原生支持 AEP 协议的官方推荐开发板。如果您是开源硬件厂商（如 Espressif 乐鑫、Seeed 硅递、M5Stack 等），并拥有带屏幕、传感器阵列的高性能 MCU，欢迎联系我们（请附上设备赞助意向），我们将为您提供深度的底层协议适配，共同抢占 AI 硬件的下一个时代标准。

**Join us. Let's give AI a physical body.**