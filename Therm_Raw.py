from Therm_Read_Test import Temp_Read
import numpy as np

Temps = np.zeros(4, dtype=int)

while True:
	for i in range(0,3):
		Temps[i] = Temp_Read(i)
	print(str(Temps) + "/r", end="" )
	time.sleep(0.5)
