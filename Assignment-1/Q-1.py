# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:16:59 2026

@author: ADMIN
"""

"""
Use Lists when items need to change (add, remove, or modify). Use Tuples when items must stay fixed and unchanged (read-only).
"""

my_list = [10,20]
my_list[0] = 99

my_tuple = (10,20)

print(my_list)
# my_tuple[0] = 99
print(my_tuple[0])