from machine import Pin, Timer
led = Pin(25, Pin.OUT)
timer1 = Timer()
timer2 = Timer()

button1 = machine.Pin(14, Pin.IN, Pin.PULL_DOWN)

def blinky():
    timer1.init(freq=2.5, mode=Timer.PERIODIC, callback=blink)

def blink(timer):
    led.toggle()
    
def turnoff(timer):
    led.value(0)
    blinky()
    
blinky()


while True:
    if button1.value():
        timer1.deinit()
        led.value(1)
        timer2.init(mode=Timer.ONE_SHOT, period=4000, callback=turnoff)
        
        
        
