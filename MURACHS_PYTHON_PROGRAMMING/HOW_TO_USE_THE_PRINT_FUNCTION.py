#!/usr/bin/env python
# coding: utf-8

# # HOW TO USE THE PRINT( ) FUNCTION 
# 
# <br>Hernan Chavez, 2024<br/>
# Ref. Michael Urban, Joel Murach, and Mike Murach. 2016. Murach's Python Programming. Mike Murach & Associates

# In[1]:


# The synthax of the print() function
# print(data[, sep=''][, end='\n'])


# In[2]:


# Three print() functions thast receive one or more arguments
print(19.99)              # 19.99
print("Price:", 19.99)    # Price: 19.99
print(1, 2, 3, 4)         # 1, 2, 3, 4


# In[3]:


# Two ways to get the same result

# A print() function that receives four arguments
score_total = 240
average_score = 80
print("Total Score:", score_total, 
      "\nAverage Score: ", average_score)


# In[4]:


# A print() function that receives one string as the argument
print("Total Score: " + str(score_total) + 
      "\nAverage Score: " + str(average_score))


# In[5]:


# Examples that use the sep and end arguments
print(1, 2, 3, 4, sep=' | ')        # 1 | 2 | 3 | 4
print(1, 2, 3, 4, end='!!!')        # 1 2 3 4!!!

