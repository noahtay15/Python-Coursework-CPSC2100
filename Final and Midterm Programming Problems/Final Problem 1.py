# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 16:34:17 2022

@author: Noaht
"""

def laceStrings(s1, s2):
    s3 = []
    smaller = min(s1, s2)
    larger = max(s1, s2)
    for i in range(len(larger)):
        if i < len(smaller): 
            s3.append(s1[i])
            s3.append(s2[i])
        elif i >= len(smaller):
            for i in range(len(smaller), len(larger)):
                s3.append(larger[i])
    s3 = ''.join(s3)
    return s3

st1 = 'abcd'
st2 = 'efghi'
print(laceStrings(st1, st2))
print(laceStrings(st2, st1))      
    
    