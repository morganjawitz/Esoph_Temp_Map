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

#creating initial temp plot locations in 3D
theta = 0
r = 1
for i in range(0,7):
	xs[i] = r*np.sin(theta) #defining x points of thermistor points
	ys[i] = r*np.cos(theta) #defining y points of thermistor points
	zs[i] = i*15 #z steps for thermistors
	theta = theta + (np.pi/2) #rotation for cylinderical points


def animate(i,xs,ys,zs):
	#reading temperature
	#Temp = Temp_Read(1)


	ax.scatter(xs,ys,zs) #plotting thermistor points

	#plotting temp annotations
	#label = str('%d' %Temp)
	

	for p in range(0,7):
		Temp = Temp_Read(p) #reading temperature
		
		ax.text(xs[p],ys[p],zs[p], '%.2f' %Temp).remove() #removing the old temp plot
		ax.text(xs[p],ys[p],zs[p], '%.2f' %Temp) #plotting temp at points

	#plotting cylinder
	x = np.linspace(-1,1,100)
	z = np.linspace(0,105,100)
	Xc, Zc = np.meshgrid(x,z)
	Yc = np.sqrt(1-Xc**2)

	# Draw parameters
	rstride = 20
	cstride = 10
	#ax.plot_surface(Xc, Yc, Zc, alpha=0.2, rstride=rstride, cstride=cstride)
	#ax.plot_surface(Xc, -Yc, Zc, alpha=0.2, rstride=rstride, cstride=cstride)
	ax.plot_wireframe(Xc,Yc, Zc, rstride = rstride, cstride = cstride)
	ax.plot_wireframe(Xc,-Yc, Zc, rstride = rstride, cstride = cstride)
	




	

#set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs = (xs, ys, zs), interval=1000)
plt.show()





#print(Temp_Read(1))
