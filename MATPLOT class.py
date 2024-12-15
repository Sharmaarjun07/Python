import matplotlib.pyplot as plt
plt.plot([-1,-4.5,16,23])
plt.show()
print("________________________")
plt.plot([-1,4.5,16,23],"ob")#ob for dots
plt.show()

print("________________________")
import matplotlib.pyplot as plt
days=range(1,9)
celcius_values=[25.6,24.1,26.7,28.3,27.5,30.5,32.8,33.1]

fig, ax=plt.subplots()
ax.plot(days, celcius_values)
ax.set(xlabel='day',
       ylabel='temperature in celcius',
       title='temperature graph')
plt.show()

#photo..for two values in graphs
import matplotlib. pyplot as plt
days = list (range (1, 9))
celsius_min = [19.6, 24.1, 16.7, 28.3,24.6,30.5,32.8,33.1]
celsius_max = [24.8, 28.9, 31.3, 33.0,34.9,35.6,38.4,39.2]

fig, ax = plt. subplots ()
ax. set (xlabel='Day',
         ylabel='Temperature in celsius',
         title='temperature Graph')

ax.plot(days,celsius_min,
        days,celsius_min, "oy",
        days,celsius_max,
        days,celsius_max,"or")
plt.show()
#photo....for bar plot
import numpy as np
years = [str(year) for year in range (2010, 2021) ]
visitors = (1241, 50927, 162242,222093,
            665004, 2071987, 2460407, 3799215,
            5399000, 5474016,6003672)

plt. bar (years, visitors, color="green")

plt. xlabel ("Years")
plt. ylabel ("Values")
plt. title ("Bar Chart Exampled")
 
plt.plot()
plt.show()
#photo...histogram..(plt.hist)
import matplotlib.pyplot as plt 
import numpy as np
gaussian_numbers = np.random.normal (size=10000)
gaussian_numbers
plt. hist (gaussian_numbers,bins=20)
plt. title ("Gaussian Histogram") 
plt. xlabel ("Value")
plt. ylabel ("Frequency")
plt.show()
#Scatter plot...(plt.scatter)
import matplotlib.pyplot as plt 
import numpy as np
x=np. arange (0,11)
y1 = np. random. randint (2, 7,(11,))
y2 = np. random. randint (9, 14,(11,))
y3 = np. random. randint (15,23,(11,))


plt. scatter (x, y1)
plt. scatter (x, y2,marker='v',color='r')
plt. scatter (x, y3,marker='^',color='m')
plt.title('Scatter plot example')
plt.show()
#Stack plots....
import matplotlib.pyplot as plt
idxes = [ 1, 2, 3, 4, 5, 6, 7, 8, 9]
y1 = [23, 42, 33, 43, 8, 44, 43, 18, 21]
y2 = [9, 31, 25, 14, 17, 17, 42, 22, 28]
y3 = [18, 29, 19, 22, 18, 16, 13, 32, 21]

plt.stackplot(idxes,
y1, y2, y3)
plt.title('Stack Plot Example')
plt.show()
#Pie Chart...(1.1f)  for highlighting 
#