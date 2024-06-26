#!/usr/bin/env python
# coding: utf-8

# # THE TEST SCORE PROGRAM
# 
# <br>Hernan Chavez, 2024<br/>
# Ref. Michael Urban, Joel Murach, and Mike Murach. 2016. Murach's Python Programming. Mike Murach & Associates

# In[1]:


# display a title
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("=====================")

# get scores from the user and accumulate the total
total_score = 0.                                   # initialize the variable for accumulating scores
total_score += int(input("Enter test score: "))
total_score += int(input("Enter test score: "))
total_score += int(input("Enter test score: "))

# calculate average score
average_score = round(total_score / 3)

# format and display the result
print("=====================")
print("Total Score: ", total_score, 
      "\nAverage Score: ", average_score)
print()
print("Bye")

