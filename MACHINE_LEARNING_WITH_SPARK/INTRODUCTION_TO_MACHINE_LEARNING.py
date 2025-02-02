#!/usr/bin/env python
# coding: utf-8

# # INTRODUCTION TO MACHINE LEARNING
# 
# Hernan Carlos Chavez Paura Garcia<br>
# Feb 1st, 2025<br>
# Singh, Pramod. Machine Learning with PySpark: With Natural Language Processing and Recommender Systems. Apress, 2018.

# ## INTRODUCTION TO MACHINE LEARNING
# 
# We can categorize machine learning into four categories:
# 
# * SUPERVISED MACHINE LEARNING
# * UNSUPERVISED MACHINE LEARNING
# * SEMI-SUPERVISED MACHINE LEARNING
# * REINFORCEMENT LEARNING

# ## SUPERVISED MACHINE LEARNING
# 
# The methodology that is used sometimes varies based on the kind of output the model is trying to predict.  If the target label is a categorical type, then it falls under the Classification category; and if the target feature is a numerical value, it would fall under then Regression category. Some of the supervised ML algorithms are the following:
# 
# 1. Linear Regression
# 2. Logistic Regression
# 3. Support Vector Machines
# 4. Naive Bayesian Classifier
# 5. Decision Trees
# 6. Ensembling Methods

# ## UNSUPERVISED MACHINE LEARNING
# 
# The algorithms used in unsupervised learning are:
# 
# 1. Clustering Algorithms (K-Means, Hierarchical)
# 2. Anomaly Detection
# 3. Dimensionality Reduction Techniques
# 4. Topic Modeling
# 5. Association Rile Mining
# 
# The whole idea of Unsuprvised learning is to discover and find out the patterns rather than making predictions. So, unsupervised learning is different from supervised in mainly two aspects:
# 
# 1. There is no labeled training data and no predictions.
# 2. The perfromance of models in unsupervised learning cannot be evaluated as there are no labels or correct answers.

# ## SEMI-SUPERVISED LEARNING
# 
# The semi-supervised learning can be used on a small portion of labelled data to train the model and then use it for labelling the other reamining part of data, which can then be used for other purposes. This is also known as Pseudo-labelling as its labels the unlabeled data.
# 
# The next step in semi-supervised learning is to retrain the model on the entire labeled dataset. The advantage that it offers is that the model gets trained on a bigger dataset, which was not the case earlier, and is now more robuts and better at predictions. The other advantage is that semi-supervised learning saves a lot of effort and time that could go to manually label the data. The flipside of doing all this is that it's difficult to get high performance on the pseudo-labeling as it uses a small part of the labeled data to make predictions. However, it is still better option rather than manually labeling the data, which can be very expensive and time consuming at the same time.   

# ## REINFORCEMENT LEARNING
# 
# Let's break reinforcement learning down to individual elements uisng a visualization.
# 
# 
# <br/><br/><center>Fig. 1 Reinforcement Learning</center>
# 
# <center><img src="MACHINE_LEARNING_WITH_SPARK_IMAGES/INTRODUCTION_TO_MACHINE_LEARNING_1.png" width="600"></center><br/><br/>
# 
# * **Autonomous Agent**: This is the main character in this whole learning process who is responsible for taking action. If it is a game, the agent makes the moves to finish or reach the end goal.
# 
# * **Actions**: These are the sets of possible steps that the agent can take in order to move forward in the task. Each action will have some effect on the state of the agent and can result in either a reward or a penalty. For example, in a game of Tennis, actions might be to serve, return, move left or right, etc.
# 
# * **Reward**: This is the key to making progress in reinforcement learning. Rewards enable the agent to take actions based on it's positive rewards or penalties. It is a feedback mechanism that differentiates it from traditional supervised and unsupervised learning techniques.
# 
# * **Environment**: This is the territory in which the agent gets to play in. Environment decided whether the actions that the agent takes result in rewards or penalties.
# 
# * **State**: The position the agent is in at any given point of time defines the state of the agent. To move forward or reach the end goal, the agent has to keep changing states in a positive direction to maximize the rewards.
# 
# The unique thing about Reinforcement Learning is that there is a feedback mechanism that drives the next behavior of the agent based on maximizing the total discounted reward. Some of the prominent applications that use Reinforcement Learning are self-driving cars, optimization of energy consumption, and the gaming domain. However, it can also be used to build recommender systems as well. 
