#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:02:15 2026

@author: root
"""


class Vehicle:
    def __init__(self,name):
        self.name = name
        
    def display(self):
        print("Vehicle: ",self.name)
        
class Bus(Vehicle):
    def __init__(self,name):
        super().__init__(name)
        
    def seating_capacity(self,capacity=50):
        print("The seating capacity of",self.name,"is",capacity)
        
bus = Bus("Volvo Bus")

bus.display()
bus.seating_capacity()