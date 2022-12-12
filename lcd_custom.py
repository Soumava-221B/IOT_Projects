import utime

from machine import I2C,Pin
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

trigger = Pin(21, Pin.OUT)
echo = Pin(20, Pin.IN)

lcd.clear()
lcd.move_to(4,0)
lcd.putstr("Soumava")
lcd.move_to(6,1)
lcd.putstr("Das")
utime.sleep(2)