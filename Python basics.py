# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 13:30:48 2026

@author: DELL
"""

counter = 0
while counter < 10:
    counter = counter + 3
    print("Python Loops")

txt = "Hello, Welcome Python"
x = txt.index("Welcome")
print(x)

for i in 'Dhruvisha':
    if i == 't':
        pass
    print('Letter: ',i)
    
b = "Hello World!"
print(b[2:5])

print("Hello World!")
print("Welcome")

"""name = input("Enter Your name: ")
print("Hello",name)"""

x = 3
y = 5
print(x ** y)

x = 17
y = 2
print(x // y)

number = int(input("Enter a number: "))
if number%2 == 0:
    print("Even")
else:
    print("Odd")
    
n = int(input("Enter the number: "))
if n == 10:
    print("Equal to 10")
elif n == 20:
    print("Equal to 20")
elif n == 30:
    print("Equal to 30")
else:
    print("NOT Equal")
    
fruits = ["apple","banana","cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


gfg = "geeksforgeeks"
gfg = "".join(reversed(gfg))
print(gfg)

var1 = "Hello World!"
print("Updated String: ",var1[:6] + 'Python')

s = "hellopython"
print(s.capitalize())

print("string slicing: ", s[-5])