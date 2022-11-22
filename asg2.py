from machine import ADC,Pin
from utime import sleep
SW = ADC(28)
pot1 = ADC(26)     # x axis
pot2 = ADC(27)     # y axis

led1 = machine.Pin(0,machine.Pin.OUT)
led2 = machine.Pin(1, machine.Pin.OUT)
led3 = machine.Pin(2, machine.Pin.OUT)

while True:
    pot_val = pot1.read_u16()
    pot_val2 = pot2.read_u16()
    pot_val3 = SW.read_u16()
    #print(pot_val)
    print(pot_val2)
    print(pot_val3)
    #sleep(0.01)
    
    
    led1.toggle()
    utime.sleep(2)

    led1.value(0)
  
    led2.toggle()
    utime.sleep(2)

    led2.value(0)

    led3.toggle()
    utime.sleep(2)

    led3.value(0)