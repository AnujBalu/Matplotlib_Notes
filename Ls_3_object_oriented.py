import matplotlib.pyplot as plt   # basics of using matplotlib
import numpy as np

x = np.linspace(0,5,10)
y = x**3
fig = plt.figure()   # figure() method creates a empty canvas and that canvas is stored in object called fig
                     # it have defult size and graph ratio.

# fig = plt.figure(figsize=(20,10),dpi=50)   # this method is used to customize the size of graph.
                                             # here 'dpi=' method is used to adjust pixel quality
                                             # 'figsize=' method adjust the ratio of graph

axes = fig.add_axes([0.1, 0.1 ,0.8 ,0.8])  # add_axes() method will set the heigth and width for canvas that we created.
axes.plot(x,y,'g')
axes.set_title("graph")
axes.set_xlabel("x axis")
axes.set_ylabel("y axis")
plt.show()