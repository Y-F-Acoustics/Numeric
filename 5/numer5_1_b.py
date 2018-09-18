# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 14:39:29 2018

@author: Yuki-F
"""

import numpy as np
import matplotlib.pyplot as plt

#First index
i = 1
x = [0]
y = [0]
xx = [0]
yy = [0]
x.append(0)
xx.append(abs(x[0]+1))
yy.append(abs(y[0]+1))

#Newton method
while (np.abs(np.exp(x[i]**2))+2*np.exp(1)*x[i]+np.exp(1) > 10**(-15)):
    y.append(x[i] - 2*(np.exp(x[i]**2)+2*np.exp(1)*x[i]+np.exp(1))/(2*x[i]*np.exp(x[i]**2)+2*np.exp(1)))
    yy.append(abs(y[i]+1))
    x.append(y[i])
    xx.append(abs(x[i]+1))
    i += 1
    
y.append(x[i] - ((np.exp(x[i]**2)+2*np.exp(1)*x[i]+np.exp(1))/(2*x[i]*np.exp(x[i]**2)+2*np.exp(1)))*2)

#Estimated Answer
print(x)
print(y)

#Substitute
print(np.exp(x[i]**2)+2*np.exp(1)*x[i]+np.exp(1))
print(np.exp(y[i]**2)+2*np.exp(1)*y[i]+np.exp(1))

#Plot real convergence and convergence guideline
plt.plot(xx[1:len(xx)+1], yy[1:len(yy)+1], "r", label="Convergence")
plt.hold(True)
#First order convergence
f = lambda x: x
#Second order convergence
ff = lambda x: x**2
fx = np.linspace(10**(-8), 1)
plt.plot(fx, f(fx), label="x")
plt.hold(True)
plt.plot(fx, ff(fx), label="x^2")
ax = plt.gca()
ax.set_xscale('log')
ax.set_yscale('log')
plt.xlabel('x')
plt.legend()
plt.show()
