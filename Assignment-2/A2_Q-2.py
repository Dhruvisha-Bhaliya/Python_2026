#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 13:49:49 2026

@author: root
"""


class Vehicle:
        def __init__(self,max_speed,mileage):
            self.max_speed = max_speed
            self.mileage = mileage
        
        def set_max_speed(self,max_speed):
            self.max_speed = max_speed
            
        def get_max_speed(self):
            return self.max_speed
        
        def set_mileage(self,mileage):
            self.mileage = mileage
            
        def get_mileage(self):
            return self.mileage
        
class Bus(Vehicle):
       def __init__(self,max_speed,mileage,seating_capacity):
           super().__init__(max_speed,mileage)
           self.seating_capacity = seating_capacity
        
       def set_seating_capacity(self,seating_capacity):
            self.seating_capacity = seating_capacity
        
       def get_seating_capacity(self):
            return self.seating_capacity

bus = Bus(120,10,50)

print("Bus Max Speed:", bus.get_max_speed(), "km/h")
print("Bus Mileage:", bus.get_mileage(), "km/l")
print("Bus Seating Capacity:", bus.get_seating_capacity(), "seats")

bus.set_max_speed(150)
bus.set_mileage(12)
bus.set_seating_capacity(60)

print("\nAfter Updating Bus Details:")
print("Bus Max Speed:", bus.get_max_speed(), "km/h")
print("Bus Mileage:", bus.get_mileage(), "km/l")
print("Bus Seating Capacity:", bus.get_seating_capacity(), "seats")