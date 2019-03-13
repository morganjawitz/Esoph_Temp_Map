import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib import cm
import matplotlib
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
z = np.linspace(0,99,100)
y = np.sqrt(r**2-x**2)
#Xc,Zc,Yc = np.meshgrid(x,y,z) this didn't work
Xc, Zc = np.meshgrid(x,z)
Yc = np.sqrt(r**2-Xc**2)

#print(Xc)
#print(Xc[:,49])
#print(Zc)

#print(Xc.shape)
#print(Yc)
#print(Zc)


# Draw parameters
rstride = 10
cstride = 10


def animate(i,xs,ys,zs,Xc,Zc,Yc,x,y,z):
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


	#listing the cordinates with the T matrix where known temps are for positive Yc plot
	T0 = [x[49],z[0],Temps[0]]
	T1 = [x[99],z[15],Temps[1]]
	T2 = [x[49],z[30],Temps[2]]
	T3 = [x[0],z[45],Temps[3]]
	T4 = [x[49],z[60],Temps[4]]
	#T4 = [x[49],z[60],45] #testing the color map
	T5 = [x[99],z[75],Temps[5]]
	T6 = [x[49],z[90],Temps[6]]
	#T6 = [x[49],z[90],38] #testing the color map
	T7 = [x[0],z[99],Temps[7]]
	BC1 = [x[0],z[0],Temps[2]]
	BC2 = [x[0],z[30],Temps[2]]
	BC3 = [x[0],z[90],Temps[6]]
	BC4 = [x[0],z[99],Temps[7]]
	BC5 = [x[99],z[0],Temps[2]]
	BC6 = [x[99],z[30],Temps[2]]
	BC7 = [x[99],z[90],Temps[6]]
	BC8 = [x[99],z[99],Temps[7]]

	#setting known points and temperature values for interp.
	points_x = [BC1[0],BC2[0],BC3[0],BC4[0],BC5[0],BC6[0],BC7[0],BC8[0],T0[0],T1[0],T2[0],T3[0],T4[0],T5[0],T6[0],T7[0]]
	
	points_z = [BC1[1],BC2[1],BC3[1],BC4[1],BC5[1],BC6[1],BC7[1],BC8[1],T0[1],T1[1],T2[1],T3[1],T4[1],T5[1],T6[1],T7[1]]

	values = [BC1[2],BC2[2],BC3[2],BC4[2],BC5[2],BC6[2],BC7[2],BC8[2],T0[2],T1[2],T2[2],T3[2],T4[2],T5[2],T6[2],T7[2]]



	#interpolating Temps
	T = griddata((points_x, points_z), values, (Xc, Zc), method='linear')
	#print(T)

	#setting color map from Temperature
	color_dim = T #selecting temp points to be used for color scalig
	minn,maxx = 15, 50 #setting min and max values of high and low temps
	norm = matplotlib.colors.Normalize(minn,maxx) #normalizing the values
	m = plt.cm.ScalarMappable(norm=norm, cmap= 'coolwarm') #applying normalized values to colormap
	m.set_array([]) #creating array
	fcolors = m.to_rgba(color_dim) #setting array to Temp



	# Draw parameters
	rstride = 10
	cstride = 10

	#removing surface plots
	for c, s in enumerate(surf_list):
		s.remove() #removing the surfs from the plot
	surf_list[:] = [] #clearing surf_list to make room for new surfs

	if np.average(Temps) <= 20:
		color = 'b'
	elif np.average(Temps) >= 38:
		color = 'r'
	else:
		color = 'g'

	
	#fcolors = m.to_rgba(Temp_Map_Pos)

	#plot the surface with new colors, adding new elements to surf_list to be plotted
	surf1 = ax.plot_surface(Xc, Yc, Zc, alpha=0.4, rstride=rstride, cstride=cstride, facecolors = fcolors, vmin=minn, vmax=maxx, shade=False, linewidth=0, antialiased=False)
	surf2 = ax.plot_surface(Xc, -Yc, Zc, alpha=0.4, rstride=rstride, cstride=cstride, facecolors = fcolors, vmin=minn, vmax=maxx, shade=False, linewidth=0, antialiased=False)
	
	cbar = ax.figure.colorbar(surf1)
	#adding the new surf plots to surf_list
	surf_list.append(surf1)
	surf_list.append(surf2)

	
	

#set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs = (xs, ys, zs, Xc, Zc, Yc, x, y, z), interval=1000)
plt.show()





#print(Temp_Read(1))
