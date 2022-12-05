from machine import Pin, PWM
import utime

C4 = 262
G3 = 294
A3 = 349
B3 = 330
C2 = 392
C1 = 524
G2 = 440
G1 = 466

melody = [C4,C4,G3,A3,B3,C4,C4,C4,C2,A3,C4,C4,C1,G2,A3,B3,G3,G1,G2,A3,C2,A3]

buzzer = PWM(Pin(16))

while True:
    def tone(pin,frequency,duration):
        pin.freq(frequency)
        pin.duty_u16(30000)
        utime.sleep_ms(duration)
        pin.duty_u16(0)
    
    for note in melody:
        tone(buzzer,note,250)
        utime.sleep_ms(350)