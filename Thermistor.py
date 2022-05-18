from math import *
import machine
import utime
#This is written using information from the datasheet found at
# https://resources.kitronik.co.uk/pdf/3006-2k2-thermistor-datasheet.pdf
#For the 4.7k thermistor, the following values are correct:
#B25/85 = 3997
#Rref is the resistance of the thermistor
#R0 is the resistance of the resistor in the voltage divider



A1 = 3.354016E-3
B1 = 2.569355E-4
C1 = 2.626311E-6
D1 = 0.675278E-7
Rref = 4700
V0 = 3.3
R0 = 10000

def ResistanceFromV(V):
    return R0 * ((V0 / V) -1)


def TempFromR(R):
    t1 =  1 / (A1 + B1 * log(R / Rref) + C1 * log(R / Rref) ** 2 + D1 * log(R / Rref) **3 )
    return t1 -273.15


sensor_in = machine.ADC(0)
conversion_factor = 3.3 / 65536

def GetTemp():
    Vin = sensor_in.read_u16() * conversion_factor
    Res = ResistanceFromV(Vin)
    temperature = TempFromR(Res)
    return temperature

#while True:
 #   temp = GetTemp()
  #  print(temp)
   # utime.sleep(2)