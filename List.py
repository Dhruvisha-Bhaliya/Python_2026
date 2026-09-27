# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:31:43 2026

@author: DELL
"""

thislist = ["apple","banana","cherry"]
print(thislist)
print(thislist.index("cherry"))

# List slicing

listt = [1,2,3,4,5,6,7,8]
listt = listt[::2] + listt[1::2]
#print(list)

print(listt[::4])

# List Constructor

thiss = list(("apple","banana","cherry"))
print(thiss)


thisdictionaries = {
    "brand": "Ford",
    "model": "MyStang",
    "year":"1964"
    }

print(thisdictionaries)
print(thisdictionaries["brand"])