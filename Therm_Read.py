import busio
import time
import numpy as np
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP #library for interfacing with ADC
from adafruit_mcp3xxx.analog_in import AnalogIn #function for reading analong pin
 
#Creataing interpolation arrays for therm, found in therm datasheet
T_C = [60,55,50,45,40,35,30,25,20,15,10,5,0]
RtR = [0.2966,0.3479,0.4100,0.4853,0.5770,0.6895,0.8282,1.0000,1.2142,1.4827,1.8216,2.2520,2.8024]

#Ref resistor in voltage divder
R_div = 10E3

#Creating R_Temp array
R_Temp = [0,0,0,0,0,0,0,0]

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
 
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)
 
# create the mcp object
mcp = MCP.MCP3008(spi, cs)
 
#Displaying results
#print('Raw ADC Value: ', chan7.value)
#print('ADC Voltage: ' + str(chan7.voltage) + 'V')
#print('R7 =' + str(R7))
#print('R_ref =' + str(R7_ref))

while True:
 # create an analog input channel on pin 7
 #eventually make loop to go through all 8 pins
 for i in range(0,7):
 	#setting analog call string based on pin number for loop
 	chan_call = str("mcp, MCP.P%d" %i)
 	#creating pin vector from analog input
 	chan[i+1] = AnalogIn(chan_call)
 	#converting raw data to voltage for volt array
 	if chan[i+1] == 0:
 		R_temp[i+1] = str("Thermistor Error")
 	else:
		volt[i+1] = chan[i+1].voltage
 		#converting voltage to resesitance using KCL
 		R[i+1] = (R_div*(volt[i+1] - 0.4125))/-volt[i+1]
 		#finding refrence fraction
 		R_ref = R[i+1]/R_div
 		#interpolating values from datasheet
 		R_temp[i+1] = np.interp(R_ref[i+1],RtR,T_C)

 #Displaying Values
 print('R0 Temperature =' + str(R_temp[1]) + 'C\r', end="")
 print('R1 Temperature =' + str(R_temp[2]) + 'C\r', end="")
 print('R2 Temperature =' + str(R_temp[3]) + 'C\r', end="")
 print('R3 Temperature =' + str(R_temp[4]) + 'C\r', end="")
 print('R4 Temperature =' + str(R_temp[5]) + 'C\r', end="")
 print('R5 Temperature =' + str(R_temp[6]) + 'C\r', end="")
 print('R6 Temperature =' + str(R_temp[7]) + 'C\r', end="")
 print('R7 Temperature =' + str(R_temp[8]) + 'C\r', end="")
 time.sleep(0.1)
