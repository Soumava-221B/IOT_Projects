from machine import Pin
import utime

sensor_pir = Pin(28, Pin.IN)
led = Pin(15, Pin.OUT)
#buzzer = Pin(16, Pin.OUT)

In2=Pin(4,Pin.OUT)  
In1=Pin(3,Pin.OUT)  
EN_B=Pin(2,Pin.OUT)

EN_B.high()
# Forward
def move_forward():
    In2.high()
    In1.low()
    
#Stop
def stop():
    In2.low()
    In1.low()

def pir_handler(pin):
    print("Motion detected")
    for i in range(50):
        move_forward()
        led.toggle()
        #buzzer.toggle()
        utime.sleep_ms(100)
        
    
sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

while True:
    led.toggle()
    utime.sleep(5)
    stop()