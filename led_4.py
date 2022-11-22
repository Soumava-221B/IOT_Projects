import machine
import utime

led1 = machine.Pin(0,machine.Pin.OUT)
led2 = machine.Pin(1, machine.Pin.OUT)
led3 = machine.Pin(2, machine.Pin.OUT)
led4 = machine.Pin(3, machine.Pin.OUT)


while True:
  #led1.toggle()
  #utime.sleep(2)

  led1.value(1)
  
  #led2.toggle()
  #utime.sleep(2)

  led2.value(1)

  #led3.toggle()
  #utime.sleep(2)

  led3.value(1)

  #led4.toggle()
  #utime.sleep(2)

  led4.value(1)