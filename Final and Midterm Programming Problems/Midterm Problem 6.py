# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 20:37:54 2022

@author: Noaht
"""

def max_val(t):
    global max
    if isinstance(t, int):
        if t > max:
            max = t
    else:
        for i in t:
            max_val(i)
    return max

for i in range(5):
    max = 0
    if i == 0:
        print(max_val((5, (1, 2), [[1], [2]])))
    elif i == 1:
        print(max_val((5, (1, 2), [[1], [9]])))
    elif i == 2:
        print(max_val(8))
    elif i ==3:
        print(max_val([1, 2, 3, 4]))
    elif i == 4:
        print(max_val((1, 2, 6)))