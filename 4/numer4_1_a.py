# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 11:09:04 2018

@author: Yuki-F
"""

import numpy as np
import matplotlib.pyplot as plt

#微分前
f = lambda x: np.exp(2 * x)

#微分後
g = lambda x: 2 * np.exp(2 * x)

#xの値
x = 1

N = np.zeros(11)
df = np.zeros(11)
#各hの数値における導関数の値を格納
for k in range(1, 11):
    N[k] = 10 ** k
    h = 1 / N[k]
    df[k] = (f(x+h) - f(x))/h
    
#誤差の計算
err = abs(df - g(x))


#両対数プロット
plt.plot(N, err)
ax = plt.gca()
ax.set_yscale('log')
ax.set_xscale('log')
plt.xlabel('N')
plt.ylabel('Error')