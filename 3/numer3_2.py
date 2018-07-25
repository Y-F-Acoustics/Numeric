# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 17:14:15 2018

@author: Yuki-F
"""

import numpy as np

a = 2 * 10**200
b = 5 * 10**200

#オーバフロー
print(np.sqrt(float(a) * float(b)))

#対策後
k = max([float(np.abs(a)), float(np.abs(b))])
print(k * np.sqrt((a/k) * (b/k)))