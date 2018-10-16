# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 09:07:48 2018

@author: Yuki-F
"""

import numpy as np
import scipy.linalg as linalg

A = [[3, 2, 1],
     [2, 3, 2],
     [1, 2, 3]]

b = [[6],
     [15],
     [24]]

#Power Method
x = np.linalg.solve(A, b)

print(x)

print(np.dot(A, x))

#Cholesky decomposition
U = linalg.cholesky(A)

#calculate p
p = linalg.solve(U.T, b)

#solve
x = linalg.solve(U, p)
print(x)

print(np.dot(A, x))

#print condition number of A
print(np.linalg.cond(A))