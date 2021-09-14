import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,10)
y = x**3

fig,axes = plt.subplots(figsize=(12,3),dpi=100)
axes.plot(x,y,'b')
plt.show()