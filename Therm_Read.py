import busio
import numpy as np
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP #library for interfacing with ADC
from adafruit_mcp3xxx.analog_in import AnalogIn #function for reading analong pin
 
#Creataing interpolation arrays for therm, found in therm datasheet
T_C = [0,5,10,15,20,25,30,35,40,45,50,55,60]
RtR = [2.8024,2.2520,1.8216,1.4827,1.2142,1.0000,0.8282,0.6895,0.5770,0.4853,0.4100,0.3479,0.2966]

#Ref resistor in voltage divder
R_ref = 10000

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)
 
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
 
# create an analog input channel on pin 7
#eventually make loop to go through all 8 pins
chan7 = AnalogIn(mcp, MCP.P7)
volt7 = chan7.voltage

#Calculating resitance of thermistor using KCL
R7 = (R_ref*(volt7 - 3.3))/-volt7
R7_ref = R7/R_ref

#interpolating values from datasheet
R7_Temp = np.interp(R7_ref,RtR,T_C)
 
#Displaying results
#print('Raw ADC Value: ', chan7.value)
print('ADC Voltage: ' + str(chan7.voltage) + 'V')
print('R7 =' + str(R7))
print('R_ref =' + str(R7_ref))
print('R7 Temperature =' + str(R7_Temp) + 'C')
