# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:11:10 2026

@author: ADMIN
"""

tuple1 = (("a",23),("b",37),("c",11),("d",29))
sorted_tuple = tuple(sorted(tuple1, key=lambda x: x[1]))
print(sorted_tuple)