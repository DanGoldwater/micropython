import machine
import utime
LED = machine.Pin(25, machine.Pin.OUT)
t = 0.2
sensor_temp = machine.ADC(4)
conversion_factor = 3.3 / 65535

sda = machine.Pin(1)
scl = machine.Pin(0)
i2c = machine.I2C(0, sda=sda, scl=scl, freq = 400000)
i2c.writeto(114, '\x7C')
i2c.writeto(114, '\x2D')
i2c.writeto(114, 'Hello World')

while True:
    reading = sensor_temp.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706) / 0.001721
    print(temperature)
    LED.value(1)
    utime.sleep(t)
    LED.value(0)
    utime.sleep(t)
