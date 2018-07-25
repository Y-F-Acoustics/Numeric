# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 17:10:56 2018

@author: Yuki-F
"""

a = 1
b = 1.05

#差が非常に近い
print(b-a)

#引き算の差を大きくする((b+a)(b-a)/(b+a) = (b-a))
print((b**2 - a**2)/(b+a))