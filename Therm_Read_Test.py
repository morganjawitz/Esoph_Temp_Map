import busio
import time
import numpy as np
import digitalio
import board
import adafruit_mcp3xxx.mcp3008 as MCP #library for interfacing with ADC
from adafruit_mcp3xxx.analog_in import AnalogIn #function for reading analong pin


def Temp_Read()

 
	#Creataing interpolation arrays for therm, found in therm datasheet
	T_C = [60,55,50,45,40,35,30,25,20,15,10,5,0]
	RtR = [0.2966,0.3479,0.4100,0.4853,0.5770,0.6895,0.8282,
			1.0000,1.2142,1.4827,1.8216,2.2520,2.8024]

	#Ref resistor in voltage divder
	R_div = 10E3

	#Creating R_Temp array
	R_temp = [0,0,0,0,0,0,0,0]

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
 	for i in range(0,8):
 		#setting analog call string based on pin number for loop
 	
 		#creating pin object from analog input
 		#pin_num = str(MCP) + ".P" + str(i)
 		#chan = AnalogIn(mcp, pin_num) #need to find way to loop through pin number
 	
 		#creating array of pin values
 		pin0 = AnalogIn(mcp, MCP.P0)
 		pin1 = AnalogIn(mcp, MCP.P1)
 		pin2 = AnalogIn(mcp, MCP.P2)
 		pin3 = AnalogIn(mcp, MCP.P3)
 		pin4 = AnalogIn(mcp, MCP.P4)
 		pin5 = AnalogIn(mcp, MCP.P5)
 		pin6 = AnalogIn(mcp, MCP.P6)
 		pin7 = AnalogIn(mcp, MCP.P7)
 		chan = [pin0,pin1,pin2,pin3,pin4,pin5,pin6,pin7]
 	
		#converting to voltage
 		volt = chan[i].voltage
 		#print(chan.voltage)
 		#converting raw data to voltage
 		if volt == 0:
 			R_temp[i] = 0000
 		else:
 			#converting voltage to resesitance using KCL
 			R = (R_div*(volt - 3.3))/-volt #should be 0.4125 not 3.3 when all thermistors wired in
 			#finding refrence fraction
 			R_ref = R/R_div
 			#interpolating values from datasheet
 			R_temp[i] = np.interp(R_ref,RtR,T_C)

 	#Displaying Values

 	temps = np.around(R_temp, decimals=2)
 
 	print(str(temps) + "\r", end="")

 	time.sleep(0.5)

 	return temps

Temp_Read()

Print(temps)
