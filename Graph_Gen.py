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

xs = np.zeros(8, dtype=int)
ys = np.zeros(8, dtype=int)
zs = np.zeros(8, dtype=int)


def animate(i,xs,ys,zs):
	#reading temperature
	Temp = Temp_Read(1)
	
	#scatter points
	theta = 0
	r = 1

	for i in range(0,7):
		xs[i] = r*np.sin(theta)
		ys[i] = r*np.cos(theta)
		zs[i] = i*15
		theta = theta + (np.pi/2)

	ax.scatter(xs,ys,zs)

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
ani = animation.FuncAnimation(fig, animate, fargs = (xs, ys, zs), interval=1000)
plt.show()





#print(Temp_Read(1))
