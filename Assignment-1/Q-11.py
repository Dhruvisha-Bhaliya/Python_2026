# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 11:32:31 2026

@author: ADMIN
"""

nums = [1,2,3,4,5,6]
chunk_size = 2

chunk = [nums[i : i + chunk_size] for i in range(0, len(nums), chunk_size)]
print(chunk)