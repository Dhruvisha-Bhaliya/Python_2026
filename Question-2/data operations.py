# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 13:57:16 2026

@author: DELL
"""

import pandas as pd
laptops = pd.read_csv('laptops.csv')
print(laptops.head())

# Q1: Apple laptops with Model Name "MacBook Pro"
result1 = laptops[(laptops['Brand'] == 'Apple')&(laptops['Model Name'] == "MacBook Pro")]
print(result1)

# Q2: Laptops having Windows Operating System
result2 = laptops[laptops['Operating System'].str.contains('Windows')]
print(result2)

# Q3: Laptops with 16GB RAM and MacOS
result3 = laptops[(laptops['RAM (GB)'] == 16) & (laptops['Operating System'] == "macOS")]
print(result3)

# Q4: Average price of Dell laptops
dell_avg_price = laptops[laptops['Brand'] == 'Dell']['Price (USD)'].mean()
print('Average: $%.2f' % dell_avg_price)

# Q5: Model Name wise average price of Apple laptops
apple_laptops = laptops[laptops['Brand'] == 'Apple']
apple_model_avg_price = apple_laptops.groupby('Model Name')['Price (USD)'].mean()
print(apple_model_avg_price)
 
# Q6: Comparative data of laptop brands
import matplotlib.pyplot as plt
laptops['Brand'].value_counts().plot(kind='bar')
plt.title('Laptop Count by Brand')
plt.show()

# Q7: Relationship between RAM and Price
plt.scatter(laptops['RAM (GB)'],laptops['Price (USD)'])
plt.xlabel('RAM (GB)')
plt.ylabel('Price (USD)')
plt.title('RAM vs Price')
plt.show()

# Q8: Relationship between Screen size and Price
plt.scatter(laptops['Inches'],laptops['Price (USD)'])
plt.xlabel('Screen Size (Inches)')
plt.ylabel('Price (USD)')
plt.title('Screen Size vs Price')
plt.show()

# Q9: Price distribution
laptops['Price (USD)'].plot(kind='hist')
plt.xlabel('Price (USD)')
plt.title('Price Distribution')
plt.show()

# Q10: Contribution of RAM types, explode the LOWEST slice
ram_counts = laptops['RAM (GB)'].value_counts()
ram_counts.plot(kind='pie',autopct='%.1f%%')
plt.show()