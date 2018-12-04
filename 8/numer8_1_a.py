# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:38:56 2018

@author: Yuki-F
"""

#Lagrange interpolation

import numpy as np
import matplotlib.pyplot as plt

n = 11

#Determine function
f = lambda x: -1 + (2/(1 + 16 * x ** 2))
x = np.linspace(-1, 1, n)
y = f(x)

#Determine coefficients
p = np.polyfit(x, y, n-1)
xx = np.linspace(-1, 1, 200)
yy = np.polyval(p, xx)

#Plot data
plt.plot(x, y, 'ro') #Sampled data
#plt.hold(True)
plt.plot(xx, yy, 'm') #Polynominal interpolation
#plt.hold(True)
plt.plot(xx, f(xx)) #Original function
plt.xlabel('x')
plt.ylabel('y')
plt.title('-1 + (2/(1 + 16 * x ** 2))')
plt.savefig('plot.png', dpi=1200)