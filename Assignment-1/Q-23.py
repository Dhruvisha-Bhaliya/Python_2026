# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:09:16 2026

@author: ADMIN
"""

tuple1 = (10,20,30,40)
temp_list = list(tuple1)
temp_list[1] = 25
tuple1 = tuple(temp_list)
print(tuple1)