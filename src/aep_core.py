# aep_core.py - Agentic Edge Protocol Core Engine v0.2
import socket
import json
import time
import _thread

try:
    import network
except ImportError:
    network = None

class AEPNode:
    """AEP 边缘节点核心引擎。提供极简 API，带绝对超时防卡死机制。"""
    def __init__(self, node_id, port=80, auth_token=None):
        self.node_id = node_id
        self.port = port
        self.auth_token = auth_token
        self.capabilities = {}
        self.schema = {}
        print(f"[AEP Core] Node '{self.node_id}' initialized. Auth required: {bool(self.auth_token)}")

    def register_action(self, action_name, callback_func, schema=None):
        self.capabilities[action_name] = callback_func
        if schema:
            self.schema[action_name] = schema
        else:
            self.schema[action_name] = {"type": "object", "properties": {}}
        print(f"[AEP Core] Capability registered: {action_name}")

    def _broadcast_heartbeat(self):
        udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        except Exception:
            pass

        ip = "127.0.0.1"
        if network is not None:
            try:
                wlan = network.WLAN(network.STA_IF)
                if wlan.active():
                    ip = wlan.ifconfig()[0]
            except Exception:
                pass

        while True:
            payload = {
                "node_id": self.node_id,
                "ip_address": ip,
                "auth_required": bool(self.auth_token),
                "capabilities": self.schema
            }
            try:
                udp.sendto(json.dumps(payload).encode('utf-8'), ('255.255.255.255', 8888))
            except Exception as e:
                pass
            time.sleep(5)

    def listen(self):
        try:
            _thread.start_new_thread(self._broadcast_heartbeat, ())
            print("[AEP Core] Zero-Conf UDP Broadcast started on port 8888.")
        except Exception as e:
            print(f"[AEP Core] Failed to start heartbeat thread: {e}")

        addr = socket.getaddrinfo('0.0.0.0', self.port)[0][-1]
        s = socket.socket()
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(addr)
        s.listen(1)
        print(f"\n[AEP Core Listening] {self.node_id} is waiting for Cyber Brain commands...\n")

        while True:
            try:
                cl, addr = s.accept()
                cl.settimeout(2.0) # 绝对护城河：防止残缺连接卡死

                try:
                    request = cl.recv(4096).decode('utf-8', 'ignore')
                    response_data = {"status": "error", "msg": "Invalid Protocol"}
                    status_code = "200 OK"

                    if 'POST' in request and '\r\n\r\n' in request:
                        headers_part, body = request.split('\r\n\r\n', 1)
                        
                        # 校验鉴权
                        is_authorized = True
                        if self.auth_token:
                            is_authorized = False
                            for line in headers_part.split('\r\n'):
                                if line.lower().startswith('authorization:'):
                                    parts = line.split()
                                    if len(parts) == 3 and parts[1].lower() == "bearer" and parts[2] == self.auth_token:
                                        is_authorized = True
                                        break

                        if not is_authorized:
                            status_code = "401 Unauthorized"
                            response_data = {"status": "error", "msg": "Unauthorized"}
                            print(f"[{addr[0]}] ⚠️ Unauthorized access attempt")
                        elif body:
                            try:
                                payload = json.loads(body)
                                action = payload.get("action")
                                params = payload.get("parameters", {})

                                if action in self.capabilities:
                                    print(f"[{addr[0]}] ⚡ Executing Intent: {action}")
                                    self.capabilities[action](params)
                                    response_data = {"status": "success", "action_executed": action}
                                else:
                                    print(f"⚠️ Unknown action: {action}")
                            except Exception as parse_err:
                                print(f"JSON Error: {parse_err}")

                    body_str = json.dumps(response_data)
                    response = f"HTTP/1.1 {status_code}\r\nContent-Type: application/json\r\nContent-Length: {len(body_str)}\r\nConnection: close\r\n\r\n{body_str}"
                    cl.send(response.encode('utf-8'))

                except OSError:
                    pass
                finally:
                    cl.close() # 绝对护城河：死活必关

            except Exception as e:
                print(f"Fatal loop error: {e}")