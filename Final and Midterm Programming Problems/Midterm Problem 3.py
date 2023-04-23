# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 17:52:10 2022

@author: Noaht
"""

def evalQuadratics(a, b, c, x):
    sum = a*x*x + b*x + c
    return sum

def twoQuadratics(a1, b1, c1, x1, a2, b2, c2, x2):
    sum = evalQuadratics(a1, b1, c1, x1) + evalQuadratics(a2, b2, c2, x2)
    return sum

print(evalQuadratics(1, 2, 3, 4))
print(evalQuadratics(5, 6, 7, 8))
print(twoQuadratics(1, 2, 3, 4, 5, 6, 7, 8))