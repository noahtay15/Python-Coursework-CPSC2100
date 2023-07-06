# -*- coding: utf-8 -*-
"""
@author: NoahT
"""

import pickle

def openDat():
    infile = open("LargeCitiesDict.dat", "rb")
    dictionary = pickle.load(infile)
    infile.close()
    return dictionary

def searchState(st, di):
    if st in di:
        cities = di.get(st)
        if cities == []:
            print("There are no major cities in", st)
        else: 
            if len(cities) == 1:
                print("There is", len(cities), "large city in", st +":")
            else:
                print("There are", len(cities), "large cities in", st +":")
            for i in range(len(cities)):
                print(str(i+1) + ")", cities[i])
    else:
        print("That state does not exist")
    

citiesDict = openDat()
state = str(input("Enter the state you want to search for\n")).title()
cities = searchState(state, citiesDict)