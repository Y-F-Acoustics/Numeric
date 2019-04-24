# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 11:19:05 2018

@author: Yuki-F
"""

#Linear Regression analysis for TALL and WEIGHT

import numpy as np
import matplotlib.pyplot as plt

#data
x = [166, 157, 160, 162, 151, 158, 162, 165, 161, 162, 158, 160, 163, 159, 158]
y = [ 53,  47,  48,  50,  41,  48,  47,  51,  43,  49,  49,  46,  47,  47,  50]

p = np.polyfit(x, y, 1) #determine coefficients
xx = np.linspace(150, 170, 200)
yy = np.polyval(p, xx)

plt.plot(x, y, 'ro', label = 'Data') #Data plot
plt.hold(True)
plt.plot(xx, yy, 'm', label = 'Regression line') #Interpolation
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.xlim(150, 170)

#Answer to (b)
ans = np.polyval(p, 164)
print(ans)