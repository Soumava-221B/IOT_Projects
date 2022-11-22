from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time
import utime
import machine

WIDTH = 128
HEIGHT = 64

i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=400000)

display = SSD1306_I2C(128, 64, i2c)

led1 = machine.Pin(25,machine.Pin.OUT)
# if display.inver(1)
# display.

while True:
    
    display.text("Hello Friend",8,0)
    display.text("It's a good day",8,14)
    display.text("to code.",8,28)
    display.show()
    display.fill(0)
    
    led1.toggle()
    if led1.value() == 1:
        display.text("LED 1 ON",8,14)
        display.show()
    else:
        display.fill(0)
        display.show()
        
    utime.sleep(2)
        
    
    
    