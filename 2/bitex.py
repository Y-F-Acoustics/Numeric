# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 13:58:17 2018

@author: Yuki-F
"""

def bitex(n):
    c = ""
    
    if n < 1 and n > 0:
        while n < 1:
            n = n * 2
    
        n = n - 1
    
        for j in range(0, 52):
        
            if n >= 0.5:
                c += str(1)
                n = n - 0.5
            else:
                c += str(0)
            
        n = n * 2
        
    return c 