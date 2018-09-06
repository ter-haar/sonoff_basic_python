import network
import config
from machine import Pin, Signal

ap = network.WLAN(network.AP_IF)
ap.active(False)

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(config.WIFI_ESSID, config.WIFI_PASSWORD)

led_pin = Pin(13, Pin.OUT)
led = Signal(led_pin, invert=True)
led.on()
