# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 11:31:46 2018

@author: Yuki-F
"""

def fl(x):
    digits = 5
    form = '%.'+str(digits-1)+'e'
    return float((form % x))

a = 6.1651
b = 6.1653

#Mean
ans_a = fl(fl(a+b)/2)
ans_b = fl(fl(a) + fl(b - a) / 2)
ans_c = (a + b) / 2

#Print mean answer
print(ans_a)
print(ans_b)
print(ans_c)