import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import animation
from Therm_Read_Test import Temp_Read #calling thermistor read function

#initalizing graph
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#need to initiate a 3D cylinder graph
#Next pick 8 3D points on graph to represent thermistors
#then label each point with the therm reading

def animate(i):
	#reading temperature
	Temp = Temp_Read(1)
	
	#scatter points
	theta = 0

	for i in range(0,7):
		x[i] = r*sin(theta)
		y[i] = r*cos(theta)
		z[i] = i*15
		theta = theta + 90

	ax.scatter(x,y,z)

	#plotting cylinder
	x = np.linspace(-1,1,100)
	z = np.linspace(0,3,100)
	Xc, Zc = np.meshgrid(x,z)
	Yc = np.sqrt(1-Xc**2)

	# Draw parameters
	rstride = 20
	cstride = 10
	ax.plot_surface(Xc, Yc, Zc, alpha=0.2, rstride=rstride, cstride=cstride)
	ax.plot_surface(Xc, -Yc, Zc, alpha=0.2, rstride=rstride, cstride=cstride)




	

#set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()





#print(Temp_Read(1))
