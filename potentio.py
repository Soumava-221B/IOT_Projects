from machine import ADC,Pin
from utime import sleep
SW = ADC(28)
pot1 = ADC(26)     # x axis
pot2 = ADC(27)     # y axis

while True:
    pot_val = pot1.read_u16()
    pot_val2 = pot2.read_u16()
    pot_val3 = SW.read_u16()
    #print(pot_val)
    print(pot_val2)
    print(pot_val3)
    sleep(0.01)