#!/usr/bin/env python
# coding: utf-8

# # ARITHMETIC EXPRESSIONS TO ASSIGNMENT STATEMENTS
# 
# <br>Hernan Chavez, 2024<br/>
# Ref. Michael Urban, Joel Murach, and Mike Murach. 2016. Murach's Python Programming. Mike Murach & Associates

# In[1]:


# Code that calculates sales tax
subtotal = 200.00
tax_percent = .05
tax_amount = subtotal * tax_percent  # 10.0
grand_total = subtotal + tax_amount  # 210.0
print(tax_amount)
print(grand_total)


# In[2]:


# Code that calculates the perimeters of as rectangle
width = 4.25
length = 8.5
perimieter = (2 * width) + (2 * length)  # (8.5 + 17) = 25.5
print(perimieter)


# In[3]:


# Two ways to increment the number in a variable
counter = 0
counter = counter + 1  # counter = 1
print(counter)
counter += 1           # counter = 2
print(counter)


# In[4]:


# Code that adds two numbers to a variable
score_total = 0      # score_total = 0
print(score_total)
score_total += 70    # score_total = 70
print(score_total)
score_total += 80    # score_total = 150
print(score_total)


# In[5]:


# More statements that user the compound assignment operators
total = 1000.0
total += 100.0   # total = 1100.0
print(total)
counter = 10
counter -= 1     # counter = 9
print(counter)
price = 100
price *= .8       # price = 80.0
print(price)


# In[6]:


# A floating-point result that isn't precise
subtotal = 74.95         # subtotal = 74.95
print(subtotal)
tax = subtotal * .1      # tax = 7.495000000000001
print(tax)

