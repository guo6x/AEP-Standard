# Tasks
- [x] Task 1: 更新 AEP 协议规范文档 (Update AEP Specification)
  - [x] SubTask 1.1: 在 UDP 心跳包规范中增加 `auth_required` 字段的说明。
  - [x] SubTask 1.2: 在 HTTP 动作下发规范中增加 `Authorization: Bearer <token>` 请求头的要求说明。
- [x] Task 2: 在核心引擎中实现鉴权 (`src/aep_core.py`)
  - [x] SubTask 2.1: 为 `AEPNode.__init__` 方法添加 `auth_token` 可选参数，默认为 None。
  - [x] SubTask 2.2: 更新 `_broadcast_heartbeat` 方法，在载荷中加入 `"auth_required": bool(self.auth_token)`。
  - [x] SubTask 2.3: 修改 `listen` 方法中的 HTTP 请求解析逻辑，提取并校验 `Authorization` 请求头。
  - [x] SubTask 2.4: 针对无效的 Token 或缺失 Token 的请求，返回 401 Unauthorized 响应。
- [x] Task 3: 更新示例代码 (`examples/esp32_basic/main.py`)
  - [x] SubTask 3.1: 在示例中展示如何初始化带有 `auth_token` 的 `AEPNode` 实例。

# Task Dependencies
- Task 2 depends on Task 1
- Task 3 depends on Task 2
