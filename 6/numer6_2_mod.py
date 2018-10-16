# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 14:04:29 2018

@author: Yuki-F
"""

import numpy as np
import scipy.linalg as linalg
import time as t
import matplotlib.pyplot as plt

#initialize the lists
E_time = np.zeros(401)
E_time_LU = np.zeros(401)

#Repeat numer6_2 400 times
for n in range(1, 401):
    #Generate A using random number
    A = np.random.rand(n, n)
    
    #Start time measurement
    s_time = t.time()
    
    #Power method(Repeat 150 times)
    for i in range(0, 150):
        b = np.random.rand(n, 1)
        x = linalg.solve(A, b)
        
    #Stop time measurement and substitute
    E_time[n] = t.time() - s_time
    
    #LU decompositon
    LU = linalg.lu_factor(A)
    
    #Start time measurement
    s_time = t.time()
    
    #LU solve(Repeat 150 times)
    for i in range(0, 150):
        b = np.random.rand(n, 1)
        x = linalg.lu_solve(LU, b)
        
    #Stop time measurement and substitute
    E_time_LU[n] = t.time() - s_time
    
#Plot time curves
plt.plot(E_time, label = 'Power method')
#plt.hold(True)
plt.plot(E_time_LU, label = 'LU decomposition')
plt.legend()
plt.xlabel('Size')
plt.ylabel('Time(s)')
plt.xlim(1, 401)
plt.show()
