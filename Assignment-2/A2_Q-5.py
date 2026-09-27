#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 14:12:52 2026

@author: root
"""


class A:
    def show(self):
        print("Class A: Base class Method")
        
class B(A):
    def show(self):
        print("Class B: Overridden method")

class C(A):
    def show(self):
        print("Class C: Overridden  Method")

class D(B, C):
    def show(self):
        print("Class D: Leaf subclass Method")
        super().show()
        
if __name__ == "__main__":
    print("--- Calling d.show() ---")
    d = D()
    d.show()
    
    print("\n--- Method Resolution Order (MRO) ---")
    for cls in D.__mro__:
        print(cls.__name__)