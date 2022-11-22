import machine
import utime

led1 = machine.Pin(25,machine.Pin.OUT)

while True:
  led1.toggle()
  utime.sleep(2)
  
  