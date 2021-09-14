import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,5,10)
y = x**3

fig,axes = plt.subplots(figsize=(12,3),dpi=100)
axes.plot(x,y,'b',alpha=0.5)      # 'alpha=' function used for transparency
axes.plot(x+10,'r.-')             # 'r.-' and 'g--' gives different type of lines('r'&'g' represents red and green color
axes.plot(x*10,'g--')
axes.plot(y*2,color='black')       # colours can be set by 1)'r','g','b' 2)'color=' method
axes.plot(x+y,color='#FFFF00')     # giving colour to line using RBG colour code ['#FFFF00' - yellow colour]
axes.set_title('graph')

plt.show()