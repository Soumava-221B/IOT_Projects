from machine import Pin, I2C, PWM
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
import utime

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

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
   utime.sleep_us(1)
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

   if distance < 10:
       led2.value(1)
   else:
       led2.value(0)

led1 = Pin(18,Pin.OUT)
led2 = Pin(13,Pin.OUT)


while True:
    led2.value(1)
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Distance: "+ultra()+"cm")
    utime.sleep(0.5)
    
    pwm.duty_ns(MIN)
    utime.sleep(0)
    pwm.duty_ns(MID)
    utime.sleep(0.5)
    pwm.duty_ns(MAX)
    utime.sleep(0.5)