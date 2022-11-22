from machine import Pin
import time

led = machine.Pin(0,machine.Pin.OUT)
button = machine.Pin(12, Pin.IN, Pin.PULL_DOWN)

while True:
    
    if button.value():
        led.toggle() 
        time.sleep(0.5)