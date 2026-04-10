# Local Authentication Mechanism Spec

## Why
目前 AEP (Agentic Edge Protocol) 在局域网内是完全开放的，任何知道设备 IP 和端口的节点都可以通过 HTTP POST 请求控制物理设备。为了保证基础的安全性，防止局域网内的恶意请求或误操作控制设备，需要引入极轻量级的本地鉴权机制，同时保持协议的简单性。

## What Changes
- 在 `AEPNode` 初始化时增加可选的 `auth_token` 参数。
- 在设备发现的 UDP 广播中，增加 `auth_required: true/false` 标识，告知网关该设备需要鉴权。
- 在 HTTP 请求处理逻辑中，解析并校验 HTTP Header 中的 `Authorization: Bearer <token>`。
- 如果鉴权失败，拒绝执行指令并返回 HTTP 401 Unauthorized。
- 更新协议规范文档 `AEP_Specification_v0.2.md` 以包含鉴权规范。
- 更新示例代码以演示如何开启鉴权。

## Impact
- Affected specs: 动作下发协议 (Action Payload), 设备发现 (Zero-Conf Auto-Discovery)
- Affected code: 
  - `src/aep_core.py`
  - `docs/AEP_Specification_v0.2.md`
  - `examples/esp32_basic/main.py`

## ADDED Requirements
### Requirement: Token-based Authentication
The system SHALL provide a lightweight token-based authentication mechanism.

#### Scenario: Authorized Request
- **WHEN** user sends an HTTP POST request with a valid `Authorization: Bearer <token>` header
- **THEN** the edge node executes the action and returns HTTP 200 OK

#### Scenario: Unauthorized Request
- **WHEN** user sends an HTTP POST request without a token or with an invalid token
- **THEN** the edge node rejects the request, does not execute the action, and returns HTTP 401 Unauthorized
