#!/usr/bin/env python
# coding: utf-8

# # THE MILES PER GALLON PROGRAM
# 
# <br>Hernan Chavez, 2024<br/>
# Ref. Michael Urban, Joel Murach, and Mike Murach. 2016. Murach's Python Programming. Mike Murach & Associates

# In[1]:


# The code

# display a title
print("The Miles Per Gallon program")
print()

# get inoput from the user
miles_driven = float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t\t"))

# calculate and round miles per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg, 2)

# display the result
print()
print("Miles per Gallon:\t\t" + str(mpg))
print()
print("Bye")

