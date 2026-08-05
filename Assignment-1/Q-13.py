# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:35:07 2026

@author: ADMIN
"""

list1 = [1,2,3]
list2 = [2,3,4]

common = list(set(list1) & set(list2))
print(common)