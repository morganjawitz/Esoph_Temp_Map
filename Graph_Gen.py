import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import cm
from Therm_Read_Test import Temp_Read #calling thermistor read function

#initalizing graph
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Initiate a 3D cylinder graph
# Next pick 8 3D points on graph to represent thermistors
# Then label each point with the therm reading

xs = np.zeros(8, dtype=int)
ys = np.zeros(8, dtype=int)
zs = np.zeros(8, dtype=int)
Temps = np.zeros(8, dtype=int)

#creating initial temp plot locations in 3D
theta = 0
r = 3
D = r*2
for i in range(0,8):
	xs[i] = r*np.sin(theta) #defining x points of thermistor points
	ys[i] = r*np.cos(theta) #defining y points of thermistor points
	zs[i] = i*15 #z steps for thermistors
	theta = theta + (np.pi/2) #rotation for cylinderical points

ann_list = [] #generating empty annotations list
surf_list = [] #generating empty surface list

#print(ys)
#print(zs)

#plotting cylinder
x = np.linspace(-r,r,100)
z = np.linspace(0,105,100)
Xc, Zc = np.meshgrid(x,z)
Yc = np.sqrt(r**2-Xc**2)


# Draw parameters
rstride = 10
cstride = 10


def animate(i,xs,ys,zs,Xc,Zc,Yc):
	#reading temperature
	#Temp = Temp_Read(1)


	ax.scatter(xs,ys,zs,c='black') #plotting thermistor points


	for c, a in enumerate(ann_list):
		a.remove() #removing current annotations
	ann_list[:] = [] #reseting annotation list before making new annotations
	

	for p in range(0,8):
		Temp = Temp_Read(p) #reading temperature
		Temps[p] = Temp_Read(p)
		
		if Temp <= 20: #labling temp points to indicate if they are too hot or too cold
			ann = ax.text(xs[p],ys[p],zs[p], '%.2f' %Temp, color = 'blue') #plotting temp at points
		elif Temp >= 38:
			ann = ax.text(xs[p],ys[p],zs[p], '%.2f' %Temp, color = 'red')
		else:
			ann = ax.text(xs[p],ys[p],zs[p], '%.2f' %Temp, color = 'black')


		ann_list.append(ann) #adding new annotation to ann_list



	#setting colormap
	#colors = cm.ScalarMappable(cmap = "coolwarm").to_rgba(Temps)

	# Draw parameters
	rstride = 10
	cstride = 10

	#removing surface plots
	for c, s in enumerate(surf_list):
		s.remove() #removing the surfs from the plot
	surf_list[:] = [] #clearing surf_list to make room for new surfs

	

	
	#colors = cm.coolwarm(T/float(T.max()))

	#plot the surface with new colors, adding new elements to surf_list to be plotted
	surf1 = ax.plot_surface(Xc, Yc, Zc, alpha=0.2, rstride=rstride, cstride=cstride, cmap = cm.coolwarm, linewidth=0, antialiased=False)
	surf2 = ax.plot_surface(Xc, -Yc, Zc, alpha=0.2, rstride=rstride, cstride=cstride, cmap = cm.coolwarm, linewidth=0, antialiased=False)
	
	#adding the new surf plots to surf_list
	surf_list.append(surf1)
	surf_list.append(surf2)

	
	

#set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs = (xs, ys, zs, Xc, Zc, Yc), interval=1000)
ax.set_ztickss(np.arange(min(z), max(z)+1, 1))
plt.show()






#print(Temp_Read(1))
