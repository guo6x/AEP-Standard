# ⚡️ AEP (Agentic Edge Protocol)

**The Native Physical Execution Standard for LLMs**

[![English](https://img.shields.io/badge/Language-English-blue.svg)](#) [![简体中文](https://img.shields.io/badge/语言-简体中文-red.svg)](README_zh-CN.md)

[![Status: Draft](https://img.shields.io/badge/Status-Draft-orange.svg)]()
[![Hardware: ESP32-S3](https://img.shields.io/badge/Reference_Hardware-ESP32--S3-blue.svg)]()
[![Ecosystem: OpenClaw](https://img.shields.io/badge/Ecosystem-OpenClaw-success.svg)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](#)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> Keywords: `Agentic AI`, `LLM Hardware`, `ESP32 LLM`, `MCP IoT`, `Open Source Protocol`, `Physical Execution`, `Edge Computing`

## 🚨 The Broken Reality: Why is current IoT "Pseudo-Smart"?

Current smart home systems (like Home Assistant and various proprietary ecosystems) are essentially **giant remote controls and rigid triggers**.
They are built on the mechanical logic of `If-This-Then-That` (IFTTT) and lack an understanding of the user's true intentions and global context. When you are in a deep flow state coding, a scheduled task might stupidly turn off your main light; when you are sick and feeling cold, a temperature sensor will still rigidly turn on the AC at 28°C.

**Hardware disconnected from global context is just a pile of lifeless scrap metal. Automation ≠ Intelligence.**

## 💡 The Vision & Positioning: Why do we need AEP?

If the recently booming **MCP (Model Context Protocol)** solved how LLMs "perceive" the software world, then **AEP (Agentic Edge Protocol)** is here to solve how LLMs **"interfere" with the physical world**.

**Current Industry Pain Points & Our Differentiation:**
We noticed early excellent explorations in the community like `tinymcp` and `esp-mcp` attempting to bring the MCP protocol directly to microcontrollers. However, our tests showed these solutions often require cumbersome C++ compilation environments or strongly rely on complex MQTT message brokers, which are **too heavy for edge nodes**.

AEP's positioning is completely different. It is an **ultra-lightweight physical layer shadow protocol** designed specifically for Sub-$2 (extremely low-end) microcontrollers. We advocate:

* **Ultra-Lightweight:** 0 dependencies, abandoning MQTT and complex gateways. A single line of pure HTTP/JSON API code (even just MicroPython) enables an ESP32 to instantly join the LLM network.
* **Zero-Trust Physical Execution:** The "Brain" (Agent) performs high-level reasoning on a local PC/Raspberry Pi. The physical node (ESP32) never participates in thinking; it is only responsible for millisecond-level passive execution.
* **LLM Direct Call:** Directly mapped to the LLM's native Tool-Call mechanism, truly turning hardware into the AI's nerve endings.

## 🏗 Core Architecture

AEP strips the entire system down to two extremely pure layers:

1. **🧠 The Cyber Brain Layer:** An Agent framework running locally (PC/Mac/Raspberry Pi) that integrates the context of the digital world, performs logical reasoning, and generates action intents via the MCP protocol.
2. **🦾 The Physical Tentacle Layer (Edge Nodes):** ESP32/RP2040 nodes scattered on your desk. They have no computational anxiety, only needing to expose standard AEP interfaces to execute acoustic/optical/electrical/mechanical commands from the brain in milliseconds.

> *[Architecture Diagram Placeholder]*

*(Currently, based on the Node.js Agent architecture and ESP32-S3, we have successfully run the first draft of the HTTP API specification, achieving natural language reasoning-based desktop lighting environment reconstruction.)*

## 🚀 Quick Start & Documentation

AEP's core engine and specification whitepaper are now open-source! Connecting a microcontroller to an LLM requires only 3 lines of core code:

- 📄 **Read the Protocol Specification**: 👉 [AEP_Specification_v0.1.md](./docs/AEP_Specification_v0.1.md)
- 🛠️ **Get the Core Physical Engine SDK**: 👉 [aep_core.py](./src/aep_core.py)
- 💡 **Check out ESP32 Blink Demo**: 👉 [examples/esp32_basic/main.py](./examples/esp32_basic/main.py)

## 🤝 Call to Contributors & Hardware Partners

AEP is currently in the early stages of protocol drafting and MVP validation. Changing the standard of physical world interaction requires the joint efforts of geek pioneers. We are looking for:

* **💻 Open Source Contributors:** PRs are welcome! Join us in defining AEP's standardized JSON payload specification, local authentication mechanisms, and WebRTC/WebSocket hybrid communication layer. Check our [Contributing Guidelines](CONTRIBUTING.md).
* **🧰 Official Hardware Partners (Reference Hardware):** We are selecting the first batch of official recommended development boards with native AEP protocol support. If you are an open-source hardware vendor (e.g., Espressif, Seeed Studio, M5Stack) with high-performance MCUs equipped with screens and sensor arrays, please contact us (include your device sponsorship intent). We will provide deep protocol adaptation to jointly seize the next era's standard for AI hardware.

**Join us. Let's give AI a physical body.**