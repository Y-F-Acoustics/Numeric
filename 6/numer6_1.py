# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 19:45:51 2018

@author: Yuki-F
"""

#Solve linear equation.
import numpy as np

A = np.array([[2, 4, 6, 8, 10],
              [3, 8, 7, 6, 2],
              [5, 7, 21, 44, 25]])
b = np.array([[6], [15], [24]])

piA = np.linalg.pinv(A)

#find x that has he feature shown Ax = b
x = np.dot(piA, b)

#print answer
print(x)

print(np.dot(A, x))

#condition number
print(np.linalg.cond(A))