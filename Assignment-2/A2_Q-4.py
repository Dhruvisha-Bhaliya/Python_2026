#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:06:43 2026

@author: root
"""


class Vehicle:
    pass

class Bus(Vehicle):
    pass

bus = Bus()

print("The object belongs to:",type(bus).__name__)
print(isinstance(bus, Bus))