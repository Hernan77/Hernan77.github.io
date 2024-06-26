#!/usr/bin/env python
# coding: utf-8

# # HOW TO USE THE INPUT( ) FUNCTION 
# 
# <br>Hernan Chavez, 2024<br/>
# Ref. Michael Urban, Joel Murach, and Mike Murach. 2016. Murach's Python Programming. Mike Murach & Associates

# In[1]:


# Code that gets string input from the user
first_name = input("Enter your first name: ")
print("Hello, " + first_name + "!")


# In[2]:


# Another way to get input from user
print("What is your first name?")
first_name = input()
print("Hello, " + first_name + "!")


# In[3]:


# Code that attempts to get numeric input from the user
score_total = 0
score = input("Enter your score: ")
score_total += score                  # causes an error because score is a string


# In[4]:


score_total = 0
score = input("Enter your score: ")
score_total += int(score)
print(score_total)

