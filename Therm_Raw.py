from Therm_Read_Test import Temp_Read
import numpy as np

while true:
	for i in range(0,3):
		Temps(i) = Temp_Read(i)
	print(Temps) 
