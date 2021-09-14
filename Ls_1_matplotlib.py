import matplotlib.pyplot as plt   # basics of using matplotlib
import numpy as np

x = np.linspace(0,5,10)
y = x**3

print(x)
print(y)
plt.plot(x,y)          # it is used to plot the x and y value in graph
plt.show()              # plt.show is used to display the graph in window screen