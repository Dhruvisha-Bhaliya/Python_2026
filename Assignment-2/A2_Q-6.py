#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:27:50 2026

@author: root
"""


class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def display_info(self):
        print(f"Vehicle Info: {self.brand} {self.model}")
        
    def start_engine(self):
        print(f"The {self.brand} {self.model}'s engine is starting...")
        
class Car(Vehicle):
    def __init__(self,brand,model,doors):
        super().__init__(brand,model)
        self.doors = doors
    
    def open_trunk(self):
        print(f"Opening the trunk of the {self.doors}-door {self.model}.")
        
class ElectricCar(Car):
    def __init__(self,brand,model,doors,battery_capacity):
        super().__init__(brand,model,doors)
        self.battery_capacity = battery_capacity
        
    def charge_battery(self):
        print(f"Charging the {self.battery_capacity} kWh battery of the {self.brand} {self.model}...")
        
        
if __name__ == "__main__":
    my_ev = ElectricCar(brand="Tesla", model="Model 3", doors=4, battery_capacity=75)
    
    print("--- Level 1 Methods (Inherited from Vehicle) ---")
    my_ev.display_info()
    my_ev.start_engine()

    print("\n--- Level 2 Methods (Inherited from Car) ---")
    my_ev.open_trunk()

    print("\n--- Level 3 Methods (Defined in ElectricCar) ---")
    my_ev.charge_battery()
        