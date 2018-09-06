from machine import Pin, Signal

relay_pin = Pin(12, Pin.OUT)
relay = Signal(relay_pin, invert=False)
relay.on()
