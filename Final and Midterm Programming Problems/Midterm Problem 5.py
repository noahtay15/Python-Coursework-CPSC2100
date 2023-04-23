# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 16:52:01 2022

@author: Noaht
"""

def dict_invert(d):
    inverted_d = {}
    for i in d.keys(): #goes thorugh each key of the dictionary
        if d[i] in inverted_d: #if the indexed key is in the inverted dict
            inverted_d[d[i]].append(i) #add to inverted_d
        else:
            inverted_d[d[i]] = [i] #else assign the indexed value in inverted d to 
    return inverted_d

d = {1:10, 2:20, 3:30, 4:30}
print(dict_invert(d))
a = {1:10, 2:20, 3:30}
print(dict_invert(a))
b = {0:True, 2:True, 4:True}
print(dict_invert(b))