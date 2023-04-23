# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 18:33:15 2022

@author: Noaht
"""

def uniqueValues(aDict):
    keysL = []
    keyDict = {}

    for key in list(aDict.keys()):
        if aDict[key] not in keyDict:
            keyDict[aDict[key]] = 1

        else:
            keyDict[aDict[key]] += 1

    for keyInkeyDict in keyDict.keys():
        if keyDict[keyInkeyDict] == 1:
            for keyInaDict in aDict.keys():
                if aDict[keyInaDict] == keyInkeyDict:
                    keysL.append(keyInaDict)
    return sorted(keysL)

aDict = {1:1, 3:2, 6:0, 7:0, 8:4, 10:0}
print(uniqueValues(aDict))

aDict2 = {1: 1, 2: 1, 3: 1}
print(uniqueValues(aDict2))
