from machine import Pin, I2C
from ssd1306 import SSD1306_I2C 
import utime
import random

led = Pin(0,Pin.OUT)
led1 = Pin(1,Pin.OUT)
led2 = Pin(2,Pin.OUT)
led3 = Pin(3,Pin.OUT)



WIDTH = 128
HEIGHT= 80

i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq = 400000)
display = SSD1306_I2C(128, 64, i2c)

def a():
    display.text ("IOT LAB",30,5)
    display.text ("sai krishna",2,20)
    display.text ("1941012909",2,30)
    display.text ("Section : R",2,40)
    display.text ("ITER",2,50)
    display.show()
    display.fill(0)
    utime.sleep(1)
def b():
    for n in range(15,-1,-1):
        a=str👎
        s=bin(n).replace("0b","")
        l=[0,0,0,0]
        s=int(s)
        for j in range(3,-1,-1):
            if(s>0):
                l[j]=s%10
                s=s//10
            led.value(l[0])
            led1.value(l[1])
            led2.value(l[2])
            led3.value(l[3])       
        utime.sleep(0.50)
        display.text("Count Begins",25,15)
        display.text (a,32,30)
        display.show()
        display.fill(0)
def c():
    display.text ("HELLO",2,15)
    display.text ("WISHES YOU  ",0,25)
    display.text ("Happy Diwali !!",0,50)
    display.show()
    display.fill(0)
def d():
    while True:
        l=[0,0,0,0,0,0,0,0]
        l[0]=random.randint(0,1)
        l[1]=random.randint(0,1)
        l[2]=random.randint(0,1)
        l[3]=random.randint(0,1)
        utime.sleep(0.10)
        led.value(l[0])
        led1.value(l[1])
        led2.value(l[2])
        led3.value(l[3])
        
a()
b()
c()
d()
