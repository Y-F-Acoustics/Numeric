# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:30:43 2018

@author: Yuki-F
"""

import numpy as np
import matplotlib.pyplot as plt

#微分前
f = lambda x: np.exp(2 * x)

x = 1

N = np.zeros(12)
df = np.zeros(12)
for k in range(1, 12):
    N[k] = 10 ** k
    h = 1/N[k]
    df[k] = (f(x+h) - f(x))/h
    
DF = np.zeros(12)
for k in range(1, 11):
    DF[k] = df[k]-df[k+1]
    
#絶対値
dif = abs(DF)

#両対数プロット
plt.plot(N, dif)
ax = plt.gca()
ax.set_yscale('log')
ax.set_xscale('log')
plt.xlim((10, 10**10))
plt.xlabel('N')
plt.ylabel('Absolute value of F(h)-F(h/10)')