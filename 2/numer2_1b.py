# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 13:18:42 2018

@author: Yuki-F
"""

import numpy as np

#x = 1
x = float(1)

#繰り返しの回数
i = 0

#無限大
inf = float("inf")

#無限大と等しくなるまで繰り返す
while x != inf:
    i += 1
    x *= (10**2)
    
#繰り返し回数の表示    
print(i)

#xの表示(初めてinfとなった数値)
print(x)

#infの一つ前に戻す
x = x * (10**(-2))

#計算結果
print(x)
