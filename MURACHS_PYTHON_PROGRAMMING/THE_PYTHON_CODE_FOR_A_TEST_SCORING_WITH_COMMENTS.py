#!/usr/bin/env python
# coding: utf-8

# # THE PYTHON CODE FOR A TEST SCORING
# 
# <br>Hernan Chavez, 2024<br/>
# Ref. Michael Urban, Joel Murach, and Mike Murach. 2016. Murach's Python Programming. Mike Murach & Associates<br/>

# In[1]:


# This is a tutorial  program tht illustrates the use of the while
# and if statements

#initialize variables
counter = 0
score_total = 0
test_score = 0

# get scores
while test_score != 999:
    test_score = int(input("Enter test score: "))
    if test_score >= 0 and test_score <= 100:
        score_total += test_score         # add score to total
        counter += 1                      # add 1 to counter

# calculate average score
#average_score = score_total / counter
#average_score = round(average_score)
average_score = round(                    # implicit continuation
    score_total / counter)                # same results as commented out statements

# display the result
print("======================")
print("Total Score: " + str(score_total)  # implicit continuation
      + "\nAverage Score: " + str(average_score))

