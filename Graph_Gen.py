import numpy as np
import datetime as dt
import time
import matplotlib.pyplot as plt
from matplotlib import animation
from Therm_Read_Test import Temp_Read #calling thermistor read function

#initalizing graph
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
xs = []
ys = []

def animate(i,xs,ys):
	#reading temperature
	Temp = Temp_Read(1)
	
	#adding x and y to lists
	xs.append(time.strftime('%l:%M:%S'))
	ys.append(Temp)

	#limt x and y list to 20 items
	xs = xs[-20:]
	ys = ys[-20:]

	#Draw x and y list
	ax.clear()
	ax.plot(xs, ys)

	#Format plot
	plt.xticks(rotation=45, ha='right')
	plt.subplots_adjust(bottom=0.30)
	plt.title('Therm_1 Reading vs Time')
	plt.ylabel('Temperature (deg C)')

#set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs,ys), interval=1000)
plt.show()





#print(Temp_Read(1))
