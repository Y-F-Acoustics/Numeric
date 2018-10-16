# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 13:34:58 2018

@author: Yuki-F
"""

import numpy as np
import scipy.linalg as linalg
import time as t

A = np.random.rand(400, 400)

#Start time measurement
start_time = t.time()

#Power method
for i in range(0, 150):
    b = np.random.rand(400, 1)
    x = np.linalg.solve(A, b)
    
#Stop time measurement and show elappsed time
stop_time = t.time()
print(x)
print('経過時間は'+ str(stop_time-start_time) +'秒です．')


#LU decomposition
LU = linalg.lu_factor(A)

#Start time measurement
start_time = t.time()

#LU solve
for i in range(0, 150):
    b = np.random.rand(400, 1)
    x = linalg.lu_solve(LU, b)
    
#Stop time measurement and show elappsed time
stop_time = t.time()
print(x)
print('経過時間は'+ str(stop_time-start_time) +'秒です．')
  