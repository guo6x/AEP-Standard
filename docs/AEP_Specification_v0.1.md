\# Agentic Edge Protocol (AEP) v0.1 Specification



AEP (Agentic Edge Protocol) 是专为大语言模型 (LLM) 直接驱动物理世界边缘设备而设计的“零信任、超轻量” JSON 协议。



\## 核心设计哲学

1\. \*\*去中心化与解耦\*\*：大模型无需理解底层硬件（如 GPIO、PWM），仅需下发高度抽象的意图 (Intent)。

2\. \*\*极简网络层\*\*：基于原生 HTTP/Socket，完全无视上层复杂的鉴权与长连接机制，支持跨局域网代理穿透与 Fire-and-Forget（发后即忘）机制。



\---



\## 1. 动作下发协议 (Action Payload)

\*\*方向\*\*: `LLM Gateway -> Edge Node`

\*\*格式\*\*: `POST /` (原生 JSON 载荷)

\*\*说明\*\*: 大模型决定干涉物理世界时，向边缘节点发送的标准指令格式。



```json

{

&#x20; "action": "turn\_on",

&#x20; "parameters": {

&#x20;   "color": "green",

&#x20;   "brightness": 80

&#x20; }

}
(注：parameters 为可选字段，供复杂机械结构如舵机角度、电机转速传参使用)

2. 状态回执协议 (Response Payload)
方向: Edge Node -> LLM Gateway
说明: 边缘节点物理执行后的标准回执。AEP 采用强阻断机制，极端网络环境下触发超时即视为指令已送达的 Fire-and-Forget 状态。

JSON
{
  "status": "success",
  "action_executed": "turn_on",
  "msg": "Physical hardware activated."
}
