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

print(xs)
print(ys)
print(theta)
print(zs)

#plotting cylinder
x = np.linspace(-r,r,100)
z = np.linspace(0,105,100)
Xc, Zc = np.meshgrid(x,z)
Yc = np.sqrt(r**2-Xc**2)

# Draw parameters
rstride = 20
cstride = 10
	
#plotting the original surface plot
surf1 = ax.plot_surface(Xc, Yc, Zc, alpha=0.2, rstride=rstride, cstride=cstride, cmap=cm.coolwarm, linewidth=0, antialiased=False)
surf2 = ax.plot_surface(Xc, -Yc, Zc, alpha=0.2, rstride=rstride, cstride=cstride, cmap=cm.coolwarm, linewidth=0, antialiased=False)

def animate(i,xs,ys,zs,Xc,Zc,Yc,surf1,surf2):
	#reading temperature
	#Temp = Temp_Read(1)


	ax.scatter(xs[1,8],ys[1,8],zs[1,8],c='black') #plotting thermistor points

	#plotting temp annotations
	#label = str('%d' %Temp)

	for c, a in enumerate(ann_list):
		a.remove() #removing current annotations
	ann_list[:] = [] #reseting annotation list before making new annotations
	

	for p in range(0,8):
		Temp = Temp_Read(p) #reading temperature
		Temps[p] = Temp_Read(p)
		ann = ax.text(xs[p],ys[p],zs[p], '%.2f' %Temp) #plotting temp at points
		ann_list.append(ann) #adding new annotation to ann_list



	#setting colormap
	#colors = cm.ScalarMappable(cmap = "coolwarm").to_rgba(Temps)

	# Draw parameters
	rstride = 20
	cstride = 10
	
	#removing the surf plots before replotting
	#surf1.remove() 
	#surf2.remove()

	#plot the surface with new colors
	#surf1 = ax.plot_surface(Xc, Yc, Zc, alpha=0.2, rstride=rstride, cstride=cstride, cmap=cm.coolwarm, linewidth=0, antialiased=False)
	#surf2 = ax.plot_surface(Xc, -Yc, Zc, alpha=0.2, rstride=rstride, cstride=cstride, cmap=cm.coolwarm, linewidth=0, antialiased=False)


	#ax.plot_wireframe(Xc,Yc, Zc, rstride = rstride, cstride = cstride)
	#ax.plot_wireframe(Xc,-Yc, Zc, rstride = rstride, cstride = cstride)

	
	

#set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs = (xs, ys, zs, Xc, Zc, Yc, surf1, surf2), interval=1000)
plt.show()





#print(Temp_Read(1))
