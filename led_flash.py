from machine import Pin, Timer
LED = Pin(25, Pin.OUT)

tim = Timer()
def Flash_Led(timer):
  global LED
  LED.toggle()
tim.init(freq = 2.0, mode = Timer.PERIODIC, callback = Flash_Led)