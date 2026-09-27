# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 13:06:17 2026

@author: DELL
"""

import pandas as pd
# import matplotlib.pyplot as plt

# print(laptops.head())
# print(laptops.dtypes)
# print(laptops.shape)

# Q1: Display information of laptops having brand "Apple"
laptops = pd.read_csv('laptops.csv')
apple_laptops = laptops[laptops['Brand'] == 'Apple']
print(apple_laptops)

# Q2: Display information of laptops having Touchscreen
touchscreen_laptops = laptops[laptops['Touchscreen'] == 'Yes']
print(touchscreen_laptops)

# Q3: Display information of laptop having Touchscreen and 8GB RAM
touch_8gb = laptops[(laptops['Touchscreen'] == 'Yes') & (laptops['RAM (GB)'] == 8)]
print(touch_8gb)

# Q4: Calculate the average price of Apple laptops
apple_avg_price = apple_laptops['Price (USD)'].mean()
print("Average price of Apple Laptops: $%.2f" %apple_avg_price)

# Q5: Count the Model Name wise Apple laptops
apple_model_counts = apple_laptops['Model Name'].value_counts()
print(apple_model_counts)

# Q6: Represent categorical data of laptops graphically for laptop Category
import matplotlib.pyplot as plt
laptops['Category'].value_counts().plot(kind='bar')
plt.title('Laptop Count by Category')
plt.show()

#  Q7: Influence of Category on Price (boxplot)
laptops.boxplot(column='Price (USD)', by='Category', grid=False)
plt.suptitle('')
plt.show()

# Q8: Brand-wise count (bar chart)
laptops['Brand'].value_counts().plot(kind='bar')
plt.title('Laptop count by Brand')
plt.show()

# Q9: Operating System frequency (bar chart)
laptops['Operating System'].value_counts().plot(kind='bar')
plt.title('Os frequency')
plt.show()

# Q10: Brand contribution (pie chart) with top brand exploded
brand_counts = laptops['Brand'].value_counts()
brand_counts.plot(kind='pie',autopct='%.1f%%')
plt.title('Brand Contribution')
plt.show()