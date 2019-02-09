import numpy as np
import datetime as dt
import time
import matplotlib.pyplot as plt
from matplotlib import animation
from Therm_Read_Test import Temp_Read #calling thermistor read function

#initalizing graph
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#need to initiate a 3D cylinder graph
#Next pick 8 3D points on graph to represent thermistors
#then label each point with the therm reading

def animate(i,xs,ys):
	#reading temperature
	Temp = Temp_Read(1)
	
	#plotting cylinder
	x = np.linspace(-1,1,100)
	z = np.linspace(0,3,100)
	Xc, Zc = np.meshgrid(x,z)
	Yc = np.sqrt(1-Xc**2)


	

#set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs,ys), interval=1000)
plt.show()





#print(Temp_Read(1))
