from Therm_Read_Test import Temp_Read
import numpy as np
import time

Temps = [0,0,0,0]

while True:
	for i in range(0,3):
		Temps[i] = Temp_Read(i)
	
	print(str(Temps) + "\r", end="" )
	time.sleep(0.5)
