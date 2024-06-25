#!/usr/bin/env python
# coding: utf-8

# # WORK WITH STRING DATA
# 
# <br>Hernan Chavez, 2024<br/>
# Ref. Michael Urban, Joel Murach, and Mike Murach. 2016. Murach's Python Programming. Mike Murach & Associates

# In[1]:


# How to assign strings to variablres
first_name = "Bob"    # first_name = Bob
print(first_name)
last_name = 'Smith'   # last_name = Smith
print(last_name)
name = ""             # name = empty string
print(name)
name = "Bob Smith"      # name = Bob Smith
print(name)


# In[2]:


# How to join three strings with the + operator
name = last_name + ", " + first_name  # name is "Smith, Bob"
print(name)


# In[3]:


# How to join a string and a number with the str() function
name = "Bob Smith"
age = 40
message = name + " is " + str(age) + " years old."
print(message)


# In[4]:


# What happens if you don't use the str() function
message = name + " is " + age + "years old."


# In[5]:


# implicit continuation of a string over several coding lines
score_total = 50
average_score = 70
print("Total Score: " 
      + str(score_total) 
      + "\nAverage Score: " 
      + str(average_score))

