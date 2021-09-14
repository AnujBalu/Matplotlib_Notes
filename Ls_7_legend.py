import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,10)
y = x**3

fig,axes = plt.subplots(figsize=(12,3),dpi=100)
axes.plot(x,y,'b',label='x&y')     # 'label=' function will be plotted in graph using legend() method

axes.legend()           # this legend method will locate the label automatically in graph

# to customize the location in legend() method

# axes.legend(loc=0)    # let matplotlib decide the optimal location
# axes.legend(loc=1)    # upper right cornor
# axes.legend(loc=2)    # upper left cornor
# axes.legend(loc=3)    # lower left cornor
# axes.legend(loc=4)    # lower right cornor

plt.show()