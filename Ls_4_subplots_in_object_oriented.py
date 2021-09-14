import matplotlib.pyplot as plt   # basics of using matplotlib
import numpy as np

x = np.linspace(0,5,10)
y = x**3


# These are the steps that we used in our Ls_3_object_oriented.py  programme

#fig = plt.figure()
#axes = fig.add_axes([0.1, 0.1 ,0.8 ,0.8])
#axes.plot(x,y,'g')
#axes.set_title("graph")
#axes.set_xlabel("x axis")
#axes.set_ylabel("y axis")



fig,axes = plt.subplots(nrows= 1, ncols=10)  # in these programme we are not using figure() and axes() method because
                                            # when we apply subplots() method figure() and axes() will automatically
                                            # adjust and set
for i in axes:
    i.plot(x,y,'b')
    i.set_xlabel('x axis')
    i.set_ylabel('y axis')
    i.set_title('neet graph')

fig
#plt.tight_layout()
plt.show()