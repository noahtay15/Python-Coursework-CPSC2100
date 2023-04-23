# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 20:00:13 2022

@author: Noaht
"""

def deep_reverse(L):
    newL = L[:]
    for i in newL:
        i.reverse()
    newL.reverse()
    return newL

L =  L = [[1, 2], [3, 4], [5, 6, 7]]
print(deep_reverse(L))