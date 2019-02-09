import numpy as np
from matplotlib import pyplot as pyplot
from matplotlib import animation
from Therm_Read_Test import Temp_Read #calling thermistor read function

for i in range(10)
	y = Temp_read(1)
	pyplot.scatter(i,y)
	pyplot.pause(0.05)
pyplot.show()

#print(Temp_Read(1))
