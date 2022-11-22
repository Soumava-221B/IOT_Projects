from machine import Pin
import utime

LEDS = [0,1,2,3]
L = [0,0,0,0]

for i in range(4):
    L[i] = Pin(LEDS[i], Pin.OUT)
    
while True:
    for i in range(4):
        L[i].value(1)
        utime.sleep(0.5)
        L[i].value(0)