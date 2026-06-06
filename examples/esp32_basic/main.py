import network
import time
import machine
import neopixel
import sys

# 把 src 目录加到系统路径中以便引入 aep_core (在真实单片机里，通常把 aep_core.py 放在同级目录)
try:
    from aep_core import AEPNode
except ImportError:
    print("Please ensure aep_core.py is uploaded to the device.")
    sys.exit(1)

SSID = "YOUR_WIFI_SSID"
PASSWORD = "YOUR_WIFI_PASSWORD"

try:
    pin = machine.Pin(48, machine.Pin.OUT)
    np = neopixel.NeoPixel(pin, 1)
    np[0] = (0, 0, 0)
    np.write()
except Exception:
    pass

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
    ip = wlan.ifconfig()[0]
    print('\n[WiFi Ready] IP Address:', ip)
    return ip

# --- 开发者自定义物理动作 ---
def physical_light_on(params):
    np[0] = (0, 20, 0)
    np.write()

def physical_light_off(params):
    np[0] = (0, 0, 0)
    np.write()

# --- AEP 节点注册与启动 ---
try:
    connect_wifi()
    node = AEPNode(node_id="esp32_neo_01")

    # 注册带 Schema 的动作，供网关自动发现
    turn_on_schema = {
        "type": "object",
        "properties": {
            "color": { "type": "string" },
            "brightness": { "type": "integer" }
        }
    }
    node.register_action("turn_on", physical_light_on, schema=turn_on_schema)
    node.register_action("turn_off", physical_light_off) # 使用默认空 schema

    node.listen()
except KeyboardInterrupt:
    print("\n[System] Exited.")