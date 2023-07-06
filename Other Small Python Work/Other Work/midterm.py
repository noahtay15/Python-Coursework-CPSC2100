#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Noah Taylor
"""
dic = {}
with open("Justices.txt") as file:
    while True:
        line = file.readline()
        if not line:
            break
        # split each line by comma & get president name
        names = line.split(',')[2]
        #print(names) #remember to delete
        if names not in dic:
            dic[names] = 1
        else:
            dic[names] += 1
            
sorted_dic = dict(sorted(dic.items(), key=lambda x: x[0].split()[-1]))
print(sorted_dic)


with open("JusticesbyPres.txt","w") as file:
    # write the data into the file
    for name, judges in sorted_dic.items():
        line = f"{name} : {judges}\n"
        file.write(line)

       