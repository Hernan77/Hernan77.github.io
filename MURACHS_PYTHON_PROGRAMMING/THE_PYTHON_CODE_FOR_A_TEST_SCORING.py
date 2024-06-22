#!/usr/bin/env python
# coding: utf-8

# # THE PYTHON CODE FOR A TEST SCORING
# 
# <br>Hernan Chavez, 2024<br/>
# Ref. Michael Urban, Joel Murach, and Mike Murach. 2016. Murach's Python Programming. Mike Murach & Associates<br/>

# In[1]:


counter = 0
score_total = 0
test_score = 0

while test_score != 999:
    test_score = int(input("Enter test score: "))
    if test_score >= 0 and test_score <= 100:
        score_total += test_score
        counter += 1
        
average_score = round(score_total / counter)

print("Total Score: " + str(score_total) \
      + "\nAverage Score: " + str(average_score))

