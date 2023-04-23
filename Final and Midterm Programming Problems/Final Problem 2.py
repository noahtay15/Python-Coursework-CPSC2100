# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 18:16:33 2022

@author: Noaht
"""

def prime_list(N):
    primeNums = []
    for i in range(2, N):
        for j in range(2, i):
            if i % j == 0:
                break
        else: 
            primeNums.append(i)
    return primeNums


print(prime_list(20))
