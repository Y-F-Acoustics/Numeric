# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 17:02:13 2018

@author: Yuki-F
"""

import numpy as np
import matplotlib.pyplot as plt

#Before differential
f = lambda x: np.exp(2*x)

#After diferential
g = lambda x: 2 * np.exp(2*x)

x = 1
nerr = np.zeros(16)
N = np.zeros(16)
df = np.zeros(16)

for k in range(1, 16):
    N[k] = 10 ** k
    h = 1/N[k]
    df[k] = (f(x+h)-f(x))/h
    
#error calculation
err = abs(df-g(x))

    
#error estimate
for i in range(1, 15):
    nerr[i+1] = abs(df[i+1] - df[i])/9
    
#plot error
plt.plot(N[1:15], err[1:15], label = 'Error')
plt.hold(True)
plt.plot(N[2:15], nerr[2:15], label = 'Estimated eroor')
ax = plt.gca()
ax.set_xscale('log')
ax.set_yscale('log')
plt.xlabel('N')
plt.ylabel('Error')
plt.legend()