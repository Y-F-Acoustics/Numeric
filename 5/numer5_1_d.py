# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 17:02:35 2018

@author: Yuki-F
"""

import numpy as np
import matplotlib.pyplot as plt

#First index
i = 1

#Substitute 0 to each list index[0]
x = [0]
xx = [0]

#First x value
x.append(-2)
xx.append(np.exp(x[i]**2) + 2*np.exp(1)*x[i] + np.exp(1))

#Newton method(計算したxの値が10**(-15)より小さくなるまで繰り返す)
while (np.abs(np.exp(x[i]**2))+2*np.exp(1)*x[i]+np.exp(1) > 10**(-15)):
    #x_{n}における次のxを計算
    x.append(x[i] - 2*(np.exp(x[i]**2)+2*np.exp(1)*x[i]+np.exp(1))/(2*x[i]*np.exp(x[i]**2)+2*np.exp(1)))
    
    #式の値を代入
    xx.append(np.exp(x[i]**2) + 2*np.exp(1)*x[i] + np.exp(1))
    
    #インデックスを次へ
    i += 1
    
#ループを抜け出した際の最後のxを導出
x.append(x[i] - 2*(np.exp(x[i]**2)+2*np.exp(1)*x[i]+np.exp(1))/(2*x[i]*np.exp(x[i]**2)+2*np.exp(1)))

#式の値を代入
xx.append(np.exp(x[i]**2) + 2*np.exp(1)*x[i] + np.exp(1))

#Estimated Answer
print(x[i+1])

#Substitute
print(np.exp(x[i+1]**2) + 2*np.exp(1)*x[i+1] + np.exp(1))

#Plot real convergence
plt.plot(x[1:len(x)+1], xx[1:len(xx)+1], "r", label="Convergence")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()