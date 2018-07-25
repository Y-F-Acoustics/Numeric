# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 13:14:20 2018

@author: Yuki-F
"""

#割られる数x
x = 1

#割った回数
i = 0

#繰り返しで割る
while x != 0:
    i = i + 1
    x = x / 10

#割った回数の表示    
print(i)

#1-xと1が等しいか確認
print(1-x == 1)