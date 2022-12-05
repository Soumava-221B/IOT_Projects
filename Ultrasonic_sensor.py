from machine import Pin, I2C, PWM
from ssd1306 import SSD1306_I2C
import utime

WIDTH = 128
HEIGHT = 64

i2c = I2C(0, scl = Pin(17), sda = Pin(16), freq=400000)
display = SSD1306_I2C(WIDTH, HEIGHT, i2c)


trigger = Pin(21, Pin.OUT)
echo = Pin(20, Pin.IN)


MID = 1500000
MIN = 1000000
MAX = 2000000

pwm = PWM(Pin(15))

pwm.freq(50)
pwm.duty_ns(MID)

def ultra():
   trigger.low()
   utime.sleep_us(2)
   trigger.high()
   utime.sleep_us(5)
   trigger.low()
   while echo.value() == 0:
       signaloff = utime.ticks_us()
   while echo.value() == 1:
       signalon = utime.ticks_us()
       
   timepassed = signalon - signaloff
   distance = (timepassed * 0.0343) / 2
   distance = "{:.1f}".format(distance)
   
   print(distance + " cm")
   
   return str(distance)



print("fok")
ngf = ultra()
print(ngf)
while True:
    display.text(ultra(),0,0)
    display.show()
    display.fill(0)
    utime.sleep(1)
    
    pwm.duty_ns(MIN)
    utime.sleep(1)
    pwm.duty_ns(MID)
    utime.sleep(1)
    pwm.duty_ns(MAX)
    utime.sleep(1)