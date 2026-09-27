#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 13:45:09 2026

@author: root
"""


class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        
vehicle1 = Vehicle(180,15)
vehicle2 = Vehicle(200,18)
vehicle3 = Vehicle(160, 20)
vehicle4 = Vehicle(220, 12)
vehicle5 = Vehicle(150, 22)

print("Vehicle 1 - Max Speed:", vehicle1.max_speed, "km/h, Mileage:", vehicle1.mileage, "km/l")
print("Vehicle 2 - Max Speed:", vehicle2.max_speed, "km/h, Mileage:", vehicle2.mileage, "km/l")
print("Vehicle 3 - Max Speed:", vehicle3.max_speed, "km/h, Mileage:", vehicle3.mileage, "km/l")
print("Vehicle 4 - Max Speed:", vehicle4.max_speed, "km/h, Mileage:", vehicle4.mileage, "km/l")
print("Vehicle 5 - Max Speed:", vehicle5.max_speed, "km/h, Mileage:", vehicle5.mileage, "km/l")
