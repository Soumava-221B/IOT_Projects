import machine
import utime

led0 = machine.Pin(0,machine.Pin.OUT)
led1 = machine.Pin(1, machine.Pin.OUT)
led2 = machine.Pin(2, machine.Pin.OUT)
led3 = machine.Pin(3, machine.Pin.OUT)
led4 = machine.Pin(4, machine.Pin.OUT)
led5 = machine.Pin(5, machine.Pin.OUT)
led6 = machine.Pin(6, machine.Pin.OUT)

D1 = 0x08                                   #(00001000)  (8)
D2 = 0x22                                   #(00100010)  (34)
D3 = 0x2A                                   #(00101010)  (42)
D4 = 0x55                                   #(01010101)  (85)
D5 = 0x5D                                   #(01011101)  (93)
D6 = 0x77                                   #(01110111)  (119)

while True:
  led1.toggle()
  utime.sleep(2)  
  
  led2.toggle()
  utime.sleep(2)

  led3.toggle()
  utime.sleep(2)

  led4.toggle()
  utime.sleep(2)