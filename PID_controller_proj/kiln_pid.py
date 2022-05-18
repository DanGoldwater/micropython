import machine
import utime
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
from PID import PID
# led = Pin(25, Pin.OUT)
# timer = Timer()

LED = machine.Pin(25, machine.Pin.OUT)
button1 = machine.Pin(14, Pin.IN, Pin.PULL_DOWN)
button2 = machine.Pin(11, Pin.IN, Pin.PULL_DOWN)
button3 = machine.Pin(15, Pin.IN, Pin.PULL_DOWN)
heater = machine.Pin(10, Pin.OUT)
SignalLED = machine.Pin(13, Pin.OUT)
t = .2

conversion_factor = 3.3 / 65535
#Set-up for the screen
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS) 
target = 24 # Target Temperature
margin = 1 # Margin for feedback loop
BacklightTime = 2000 # Time before backlight turns off
heater.value(0) #Initialise these as off
SignalLED.value(0)


pid = PID(
    Kp=1,
    Ki=.1,
    Kd=.05, 
    scale='ms',
    sample_time=10)

def temp_to_voltage():
    return None

def voltage_to_temp():
    return None

def get_current_reading():
    return None

def get_current_output():
    return pid(get_current_reading())

while True:
    tempNow = Thermistor.GetTemp()
    Tarray = UpdateTarray(tempNow, Tarray)
    temperature = sum(Tarray) / len(Tarray)
    #temperature = Thermistor.GetTemp()
    lcd.clear()
    PrimeBacklight()
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
    if button3.value():
        PrimeBacklight()
    if temperature > target:
        heater.value(0)
        SignalLED.value(0)
    if temperature < target - margin:
        heater.value(1)
        SignalLED.value(1)