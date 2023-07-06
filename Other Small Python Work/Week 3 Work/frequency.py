# -*- coding: utf-8 -*-
"""
@author: NoahT
"""
def countFreq(file):
    freqDic = {}
    for line in file:
        for word in line.split():
            word = word.lower()
            word = ''.join(filter(str.isalnum, word))
            if word not in freqDic:
                freqDic[word] = 1
            else:
                freqDic[word]+= 1
    return freqDic
    
def convertToList(dic):
    myList = list(dic.items())
    myList.sort(key=lambda x: x[0])
    return myList

def printList(lis):
    for i in lis:
        print(str(i[0]), "("+ str(i[1])+")")
    
s = str(input("Enter the name of the file including the file type.\n" +
              "Example: Gettysburg.txt\n"))
file = open(s, "r")
myDict = countFreq(file)
li = convertToList(myDict)
printList(li)
file.close()