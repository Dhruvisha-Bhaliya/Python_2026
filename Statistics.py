# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 07:35:59 2026

@author: DELL
"""

import numpy as np
import statistics

x = np.array([1,2,3,4])
print(x.shape)
print(x)
y = np.zeros((2,3,4))
print(y.shape)
print(y)

y.shape = (3,8)
print(y)

li = [1,2,3,3,2,2,2,1]
print(end="")
print(statistics.mean(li))

print(statistics.mode(li))

print(statistics.median(li))

print(statistics.median_low(li))

print(statistics.median_high(li))

print(statistics.median_grouped(li))

sample = [12,3,4,5]

print( (statistics.stdev(sample)))