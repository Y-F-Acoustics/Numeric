# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 10:51:40 2018

@author: Yuki-F
"""

#Least square method

import numpy as np
import matplotlib.pyplot as plt

n = 11

#Determine function model
f = lambda x: (x-1)*(x-2)
x = np.linspace(0, 2, n)

#apply noise
noise = 0.25 * (np.random.rand(1, n) - 0.5)
y = f(x) + noise

#Determine function
p = np.polyfit(x, y.T, 2)
xx = np.linspace(0, 2, 200)
yy = np.polyval(p, xx)

#plot data
plt.plot(x, y.T, 'ro', label = 'Sample') #Sample points
plt.hold(True)
plt.plot(xx, yy, '--', label = 'Determined function') #Interpolation
plt.hold(True)
plt.plot(xx, f(xx), label = 'Model function') #model function
plt.xlabel('x')
plt.ylabel('y')
plt.legend()