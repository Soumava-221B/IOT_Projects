from machine import Pin, PWM
from time import sleep

servoPin = PWM(Pin(15))
servoPin.freq(50)

def servo(degree):
    if degree > 180: degrees = 180
    if degree < 0: degrees = 0
    
    maxDuty=9000
    minDuty=1000
    
    newDuty=minDuty+(maxDuty-minDuty)*(degree/180)
    servoPin.duty_u16(int(newDuty))

while True:
    for degree in range(0,180,1):
        servo(degree)
        sleep(0.001)
        print("increasing -- "+str(degree))
    for degree in range(180, 0, -1):
        servo(degree)
        sleep(0.001)
        print("decreasing --"+str(degree))