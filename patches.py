# -*- coding: utf-8 -*-
"""
Created on Mon May 22 22:43:09 2017

@author: mikkun
"""

from matplotlib.patches import Circle, Rectangle
import matplotlib.pyplot as plt
import numpy as np

x=np.random.randn(500)
y=np.random.randn(500)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
sizes = np.empty_like(x)
sizes.fill(20)

coll = CircleCollection(sizes, offsets = (x,y), transOffset = ax.transData,
                        edgecolor = 'red', facecolor = 'cyan')
                        
ax.add_collection(coll)
ax.autoscale_view()

plt.draw()

circ = Circle((0,0), alpha=.7, color='green', radius =1)
ax.add_patch(circ)

rect = Rectangle((1.5,1.5), width=.75, height=.75, color='purple',alpha =.7)
ax.add_patch(rect)
plt.draw()
display(fig)