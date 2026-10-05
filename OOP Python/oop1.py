# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 20:22:44 2026

@author: DELL
"""

class Laptop:
    def __init__(self,brand,price):
        self.brand=brand
        self.price=price

l1 = Laptop("Apple",1200)
print(l1.brand)
print(l1.price)

print("")

class Car:
    def __init__(self,brand,year):
        self.brand=brand
        self.year=year

c1 = Car("Toyota",2022)
print(c1.brand)
print(c1.year)

"""class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage

v1 = Vehicle(180,15)
v2 = Vehicle(200,18)
v3 = Vehicle(160,20)
v4 = Vehicle(220,12)
v5 = Vehicle(150,22)

print("Max Speed:",v1.max_speed,"Mileage:",v1.mileage)"""

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

b1 = Bus(180,30,45)

print("")
print("Max Speed: ",b1.get_max_speed())
print("Mileage: ",b1.get_mileage())
print("Seating Capacity: ",b1.get_seating_capacity())

b1.set_max_speed(200)
b1.set_mileage(70)
b1.set_seating_capacity(66)
print("")
print("Max Speed: ",b1.get_max_speed())
print("Mileage: ",b1.get_mileage())
print("Seating Capacity: ",b1.get_seating_capacity())


