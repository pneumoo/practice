# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np
plt.close()

xmax = 2
ymax = 1
axscl = 1.25

#Create a regularly-spaced x and y meshgrid
x = np.arange(-xmax, xmax, xmax/200)
y = np.arange(-ymax, ymax, ymax/200)
xx,yy = np.meshgrid(x,y)

# SOME COOL SURFACES TO PLOT:
#z = np.cos(xx)*np.cos(yy)*np.exp(-0.25*(xx**2 + yy**2)**0.5)
#z = np.exp(-yy/5) * np.cos(xx)
#z = xx*yy*(xx**2 - yy**2)/(xx**2 + yy**2)
#z = 2*(xx**2)*yy/(xx**4 + yy**2)
#z = np.sin(xx**2 + yy**2)/(xx**2 + yy**2)
#z = np.sin(np.pi*xx)/np.pi*xx * np.sin(np.pi*yy)/np.pi*yy
#z = np.sin(xx)/xx * np.sin(yy)/yy
z = np.sin(xx)*np.sin(xx+(yy*3.14159))

zmag = np.abs(z).max()  #finds maximum z magnitude for use with plotting  


# SINGLE PLOT ++++++++++
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(xx, yy, z, cmap=cm.jet)
#cset = ax.contourf(xx, yy, z, zdir='z', offset=-zmag*axscl, cmap=cm.coolwarm)
#cset = ax.contourf(xx, yy, z, zdir='x', offset=-xmax*axscl, cmap=cm.coolwarm)
#cset = ax.contourf(xx, yy, z, zdir='y', offset=ymax*axscl, cmap=cm.coolwarm)

ax.set_xlabel('Time')
ax.set_xlim(-xmax*axscl, xmax*axscl)
ax.set_ylabel('I-V Phase shift')
ax.set_ylim(-ymax*axscl, ymax*axscl)
ax.set_zlabel('Power')
ax.set_zlim(-zmag*axscl, zmag*axscl)

# SUBPLOTTING +++++++++++++
#fig = plt.figure()
## PLOT SURFACE IN SUBPLOT 1
#ax = fig.add_subplot(1, 3, 1, projection='3d')
#ax.plot_surface(xx, yy, z, cmap=cm.coolwarm)

## PLOT CONTOURS IN SUBPLOT 2
#ax = fig.add_subplot(1, 3, 2, projection='3d')
#cset = ax.contour(xx, yy, z, zdir='z', offset=-zmax, cmap=cm.coolwarm)
#cset = ax.contour(xx, yy, z, zdir='x', offset=-xmax, cmap=cm.coolwarm)
#cset = ax.contour(xx, yy, z, zdir='y', offset=ymax, cmap=cm.coolwarm)




plt.show()



