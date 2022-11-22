from machine import Pin, PWM
from utime import sleep

dot = 0.25
dash = 1
gap = 0.25
ON = 1
OFF = 0

led = Pin(0,Pin.OUT)
buzzer = PWM(Pin(3))

while True:
    
    for i in range(0,3):
        led.value(ON)
        sleep(dot)
        led.value(OFF)
        sleep(dot)
    
    sleep(gap)
    for i in range(0,3):
        led.value(ON)
        sleep(dash)
        led.value(OFF)
        sleep(dash)
        
    sleep(gap)
    
    for i in range(0,3):
        led.value(ON)
        sleep(dot)
        led.value(OFF)
        sleep(dot)
        
    sleep(gap)
  