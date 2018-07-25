# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 10:58:39 2018

@author: Yuki-F
"""

def fl(x):
    digits = 5
    form = '%.'+str(digits-1)+'e'
    return float((form % x))