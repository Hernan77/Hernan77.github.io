#!/usr/bin/env python
# coding: utf-8

# # THREE PYTHON DATA TYPES
# 
# <br>Hernan Chavez, 2024<br/>
# Ref. Michael Urban, Joel Murach, and Mike Murach. 2016. Murach's Python Programming. Mike Murach & Associates<br/>

# In[1]:


# Code that initializes variables and assigns data to them
firt_name = "Mike"    # sets first_name to a str of "Mike"
quantity1 = 3         # sets quantity1 to an int value of 3
quantity2 = 5         # sets quantity2 to an int value of 5
list_price = 19.99    # sets list_price to a float value of 19.99


# In[2]:


# Code that assigns new data to the variables above
firt_name = "Joel"     # sets first_name to a str of "Joel"
quantity1 = 10         # sets quantity1 to an int value of 10
quantity1 = quantity2  # sets quantity1 to an int value of 5
quantity1 = "15"       # sets quantity1 to a str of "15", not an int of 15


# In[3]:


# Code that causes an error because of incorrect case
quantity1 = Quantity2  # NmeError: 'Quantity2' is not defined

