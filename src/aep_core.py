# aep_core.py - Agentic Edge Protocol Core Engine v0.1
import socket
import json

class AEPNode:
    """AEP 边缘节点核心引擎。提供极简 API，带绝对超时防卡死机制。"""
    def __init__(self, node_id, port=80):
        self.node_id = node_id
        self.port = port
        self.capabilities = {}
        print(f"[AEP Core] Node '{self.node_id}' initialized.")

    def register_action(self, action_name, callback_func):
        self.capabilities[action_name] = callback_func
        print(f"[AEP Core] Capability registered: {action_name}")

    def listen(self):
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

                    if 'POST' in request and '\r\n\r\n' in request:
                        body = request.split('\r\n\r\n')[1]
                        if body:
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
                    response = f"HTTP/1.1 200 OK\r\nContent-Type: application/json\r\nContent-Length: {len(body_str)}\r\nConnection: close\r\n\r\n{body_str}"
                    cl.send(response.encode('utf-8'))
                    
                except OSError:
                    pass 
                finally:
                    cl.close() # 绝对护城河：死活必关

            except Exception as e:
                print(f"Fatal loop error: {e}")