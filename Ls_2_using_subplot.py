import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,10)
y = x**3
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("graph")
plt.subplot(1,3,1)    #here subplot("row" , "coloum" , "index of graph")
plt.plot(x,y,'r')     #here r = red (graph colour)
plt.subplot(1,3,2)
plt.plot(x,x**2,'b')  #here b = blue (graph colour)
plt.subplot(1,3,3)
plt.plot(x,y,'g')     #here g = green (graph colour)
plt.show()