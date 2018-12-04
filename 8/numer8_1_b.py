# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:50:49 2018

@author: Yuki-F
"""

import numpy as np
import matplotlib.pyplot as plt

#Change sample points
n = 11

#Determine function
f = lambda x: -1 + (2/(1 + 16 * x ** 2))

#ここでデータのサンプリングを調整
x = -1 * np.cos(-1 * np.pi * np.arange(0, n)/(n-1))
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
plt.title('-1 + (2/(1 + 16 * x ** 2))')
plt.savefig('8_1_b.png', dpi=1200)