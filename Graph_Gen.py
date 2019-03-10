import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import cm
from Therm_Read_Test import Temp_Read #calling thermistor read function
from scipy.interpolate import griddata

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

#print(xs)
#print(ys)
#print(zs)

#plotting cylinder
x = np.linspace(-r,r,100)
z = np.linspace(0,105,100)
#y = np.sqrt(r**2-x**2)
#Xc,Zc,Yc = np.meshgrid(x,y,z) this didn't work
Xc, Zc = np.meshgrid(x,z)
Yc = np.sqrt(r**2-Xc**2)

#print(Xc.shape)
#print(Yc)
#print(Zc)


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


	# Building temperature matrix 100x100
	Tx,Ty = np.meshgrid[0:1:100j, 0:1:100j]
	#listing the cordinates with the T matrix where known temps are for positive Yc plot
	points_pos = np.matrix('0 49; 14 99; 49 0; 64 49; 79 99; 99 0' )
	points_pos_x = [0,14,49,64,79,99]
	points_pos_y = [49,99,0,49,99,0]
	points_neg = np.matrix('14 99; 29 49; 49 0; 79 99; 94 49; 99 0')

	#listing values of known temps
	values_pos = (Temps[0],Temps[1],Temps[3],Temps[4],Temps[5],Temps[7])
	values_neg = (Temps[2],Temps[1],Temps[2],Temps[4],Temps[6],Temps[7])

	#interpolating Temps
	Temp_Map_Pos = griddata((points_pos_X, points_pos_y), values_pos, (Tx, Ty), method = 'linear')
	print(Temp_Map_Pos)





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
plt.show()






#print(Temp_Read(1))
