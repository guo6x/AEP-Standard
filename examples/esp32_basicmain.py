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
except Exception as e:
    print(f"NeoPixel initialization failed: {e}")

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(SSID, PASSWORD)
        while not wlan.isconnected():
            time.sleep(1)
    print('\n[WiFi Ready] IP Address:', wlan.ifconfig()[0])
    return wlan.ifconfig()[0]

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
    node.register_action("turn_on", physical_light_on)
    node.register_action("turn_off", physical_light_off)
    node.listen()
except KeyboardInterrupt:
    print("\n[System] Exited.")