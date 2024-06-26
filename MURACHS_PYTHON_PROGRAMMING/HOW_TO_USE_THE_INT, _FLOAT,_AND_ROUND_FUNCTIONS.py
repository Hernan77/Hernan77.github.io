#!/usr/bin/env python
# coding: utf-8

# # HOW TO USE THE INT(), FLOAT(), AND ROUND() FUNCTIONS 
# 
# <br>Hernan Chavez, 2024<br/>
# Ref. Michael Urban, Joel Murach, and Mike Murach. 2016. Murach's Python Programming. Mike Murach & Associates

# In[3]:


# Code that causes an exception
x = 15
y = "5"
z = x + y   # TypeError: can't add an int to a str


# In[4]:


# How  using the int() function fixes the exception
x = 15
y = "5"
z = x + int(y)     # z is 20
z


# In[5]:


# Code that gets an int value from the user
quantity = input("Enter the quantity: ")   # quantity is str type
quantity = int(quantity)                   # quantity is int type
quantity


# In[6]:


# How to use chaining to get the int value in one statement
quantity = int(input("Enter the quantity: "))
quantity


# In[7]:


# Code that gets a float value from the user
price = input("Enter the price: ")
price = float(price)
price


# In[8]:


# How to use chaining to get the float value in one statement
price = float(input("Enter the price: "))
price


# In[9]:


# Code that use the round() function
miles_driven = 150
gallons_used = 5.875
mpg = miles_driven / gallons_used    # mpg = 25.53191489361702
mpg = round(mpg, 2)                  # mpg = 25.53
mpg


# In[10]:


# How to combine the last two statements
mpg = round(miles_driven / gallons_used, 2)
mpg

