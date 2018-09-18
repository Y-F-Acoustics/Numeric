# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 17:33:15 2018

@author: Yuki-F
"""

import numpy as np
import matplotlib.pyplot as plt

#First index
i = 1

#Substitute 0 to each list index[0]
x = [0]
xx = [0]
y = [0]
yy = [0]

#First x value
x.append(-2)

#Newton method(計算したxの値が10**(-15)より小さくなるまで繰り返す)
while (np.abs(np.exp(x[i]**2))+2*np.exp(1)*x[i]+np.exp(1) > 10**(-15)):
    #x_{n}における次のxを計算
    y.append(x[i] - (np.exp(x[i] ** 2) + 2*np.exp(1)*x[i] + np.exp(1))/(2*x[i]*np.exp(x[i]**2)+2*np.exp(1)))
    #実際にx_{n}をxの配列に代入
    x.append(y[i])
    #決定したxの値
    xx.append(abs(x[i]+1))
    #誤差
    yy.append(abs(y[i]+1))
    i += 1
    
#ループを抜け出した際の最後のxを導出
y.append(x[i] - (np.exp(x[i] ** 2) + 2*np.exp(1)*x[i] + np.exp(1))/(2*x[i]*np.exp(x[i]**2)+2*np.exp(1)))

#Estimated Answer
print(x)
print(y)

#Substitute
print(np.exp(x[i]**2) + 2*np.exp(1)*x[i] + np.exp(1))
print(np.exp(y[i]**2) + 2*np.exp(1)*y[i] + np.exp(1))

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
