import machine
import utime
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from machine import Pin
LED = machine.Pin(25, machine.Pin.OUT)
button1 = machine.Pin(14, Pin.IN, Pin.PULL_DOWN)
button2 = machine.Pin(13, Pin.IN, Pin.PULL_DOWN)
heater = machine.Pin(11, Pin.OUT)
SignalLED = machine.Pin(12, Pin.OUT)
t = .15
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / 65535
#Set-up for the screen
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS) 
target = 20
margin = 1.5
heater.value(0)
SignalLED.value(0)

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721
    lcd.clear()
    lcd.putstr("Target: {targ:.4} C".format(targ = str(target)))
    lcd.putstr("\nTemp: {temp:.4} C".format(temp = str(temperature)))
    LED.value(1)
    utime.sleep(t)
    LED.value(0)
    if button1.value():
        target += 1
        utime.sleep(.2)
    if button2.value():
        target -= 1
        utime.sleep(.2)
    if temperature > target:
        heater.value(1)
        SignalLED.value(1)
    if temperature < target - margin:
        heater.value(0)
        SignalLED.value(0)
    
    
        
    #utime.sleep(t)
