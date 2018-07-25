# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 17:20:07 2018

@author: Yuki-F
"""

def fl(x):
    digits = 5
    form = '%.'+str(digits-1)+'e'
    return float((form % x))

x = [0.9997, 1.0007, 0.9995, 1.0002, 1.0001, 1.0004,
     1.0005, 0.9998, 0.9996, 1.0004, 1.0004, 1.0004,
     0.9993, 0.9999, 0.9988, 1.0001, 0.9999, 0.9994,
     0.9997, 0.9991, 1.0002, 1.0004, 0.9989, 0.9989,
     1.0000, 1.0009, 1.0006, 0.9993, 0.9997, 1.0001]

#(i) method
xbar = 0

#(ii) method
Xbar = 0

for i in range(0, 30):
    xbar = fl(xbar + x[i])
    Xbar = fl(Xbar + fl(x[i] - 1))
    
#(i) result
xbar = fl(xbar/(i+1))
print(xbar)

#(ii) result
Xbar = fl(fl(Xbar/(i+1)) + 1)
print(Xbar)
