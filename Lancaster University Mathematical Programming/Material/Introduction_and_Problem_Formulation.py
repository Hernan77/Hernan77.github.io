#!/usr/bin/env python
# coding: utf-8

# # Lancaster University - Mathematical Programming
# 
# **Hernan Chavez 1/7/2021**
# 
# **Lancaster University 2003 - 2004**
# 
# ## Introduction
# 
# Mathematcial programming (MP) means optimizing a given function under certain constraints. The simplest form is Linear Programming (LP), although there are other more complex variations. In this course, you will discover the versatility of LP techniques, their limiations, and the information which can be obtained from a Linear Programming 'solution'. Another MP variant known as Integer Programming (IP) will also be discussed.
# 
# The techniques of mathematical programming are varied. The essence of mathematical programming is the creation of a mathematical model and rigorous manipulation of the model to secure an optimum solution to a real world problem. Since mathematical programming is designed to deal with complex problems having many variables, the models are often complex, albeit less complex than in the real world. Since the modeling process involves the extraction of the important from the complex, there is always some sort of simplification. In some problems there may be too much simplification, and the solution may not be optimal in the real world. But if the appropriate technique - linear programming, stochastic or goal programming - is chosen, then the process and solution should at least shed some light and provide some information.
# 
# The development of linear programming has been ranked among the most important scientific advances of the mid-20<sup>th</sup> century, and we must agree with this assessment. Its impact since just 1950 has been extraordinary. Today it is a standard tool that has saved many thousands or millions of dollars to many companies or businesses of even moderate size in the various industrialized countries of the world; and its use in other sectors of society has been spreading rapidly. A major proportion of all scientific computation on computers is devoted to the use of linear programming. Dozens of textbooks have been written about linear programming, and published articles describing important applications now number in the thousands.
# 
# Many type of applications involve the general problem of allocating limited resources among competing activities in the best possible (i.e., optimal) way. More precisely, this problem involves selecting the level of certain activities for scarce resources that are necessary to perform those activities. The choice of activity levels then indicate how much of each resources will be consumed by each activitiy. The variety of situations to which this description applies is diverse, indeed, ranging from the allocation of production facilities to products to the allocation of national resource to domestic needs, from protfolio selection to the selection of shipping patterns, from agricultural planning to the design of radiation theory, and so on. However, the one common ingredient in each of these situatiosn is the necessity for allocating resources to activities by choosing the levels of those activities.
# 
# ## LP Example
# 
# A firm manufactures two products P<sub>1</sub> and P<sub>2</sub> on three machines M<sub>1</sub>, M<sub>2</sub>, and M<sub>3</sub>. P<sub>1</sub> must be processed on M<sub>1</sub> and M<sub>2</sub>, P<sub>2</sub> is processed on all three machines. The manufacturing times for the products are given in the following table.
# 
# *<u>Manufacturing times in hours/unit product.</u>*
#     
# |             | M<sub>1</sub> | M<sub>2</sub> | M<sub>3</sub> |
# |:-----------:|:-------------:|:-------------:|:-------------:|
# |P<sub>1</sub>|     0.25      |       0.4     |      0.0      |
# |P<sub>2</sub>|     0.5       |       0.2     |      0.8      |
# 
# Each machine can be used for a total of 40 hours/week. If the firm obtains a profit of &#36;2/per unit for product P<sub>1</sub> and \\$3/unit for product P<sub>2</sub> then how much of each product should be made each week to maximize profit?
# 
# This problem can be formulated in the following way:
# 
# Let x<sub>1</sub> be the no. of units of P<sub>1</sub> produced/week.
# Let x<sub>2</sub> be the no. of units of P<sub>2</sub> produced/week.
# 
# Then we wish to maximize profit function  f = 2x<sub>1</sub> + 3x<sub>2</sub>
# 
# Subject to the machine capacity constraints
# 
# 0.25x<sub>1</sub> + 0.5x<sub>2</sub> <= 40 (Machine 1)<br/>
# 0.4x<sub>1</sub> + 0.2x<sub>2</sub> <= 40 (Machine 2)<br/>
# 0.8x<sub>2</sub> <= 40 (Machine 3)<br/>
# 
# and also to the conditions
# 
# x<sub>1</sub> >= 0<br/>
# x<sub>2</sub> >= 0<br/>
# 
# This formulation is an example of a Linear Program (LP).
# 
# ## Formal Defintions
# 
# A Linear Program is a problem of *maximizing (or minimizing) a linear function of a set of variables when these variables are required to satisfy a set of linear constraints.*
# 
# Note that the word *Programming* used in the context of MP, LP, etc. simply means 'planning'. This is not to be confused with the 'programming' of computers. Linear Programming (and MP in general) involves optimizing a certain function, whereas Computer Programming is instructing a computer to perfrom a certain task. Of course, one might use a computer program to solve an LP problem.
# 
# By a *linear function fo a set of variables* meant an expression which can be written in the form 
# 
# c<sub>0</sub> +  c<sub>1</sub>x<sub>1</sub> + c<sub>2</sub>x<sub>1</sub> + ... + c<sub>n</sub>x<sub>n</sub>
# 
# where c<sub>0</sub>, c<sub>1</sub>, c<sub>2</sub>, ..., c<sub>n</sub> are constants.
# 
# In the previous example the linear function was
# 
# f = 2x<sub>1</sub> + 3x<sub>2</sub>
# 
# The constant which multiplies a variable is called *coefficient* of the variable. Thus the coefficient of x<sub>1</sub> in our example is 2.
# 
# This function which is to be maximized (or minimized) is called the *objective function* or *cost function*.
# 
# A *linear constraint* is one which can be written as:
# 
# a linear function = constant,<br/>
# a linear function <= constant, or<br/>
# a linear function >= constant<br/>
# 
# In our example there are 3 linear constraints all involving "<=".
# 
# A complete general linear programming problem could thus be written in the following way:
# 
# Max c<sub>1</sub>x<sub>1</sub> + c<sub>2</sub>x<sub>1</sub> + ... + c<sub>n</sub>x<sub>n</sub><br/>
# 
# Subject to:
# 
# a<sub>11</sub>x<sub>1</sub> + a<sub>12</sub>x<sub>1</sub> + ... + a<sub>1n</sub>x<sub>n</sub> (R<sub>1</sub>) b<sub>1</sub><br/>
# a<sub>21</sub>x<sub>1</sub> + a<sub>22</sub>x<sub>1</sub> + ... + a<sub>2n</sub>x<sub>n</sub> (R<sub>2</sub>) b<sub>2</sub><br/>
# ... + ... + ... + ... ... ...<br/>
# a<sub>m1</sub>x<sub>1</sub> + a<sub>m2</sub>x<sub>1</sub> + ... + a<sub>mn</sub>x<sub>n</sub> (R<sub>m</sub>) b<sub>m</sub><br/>
# 
# where the relationships (R<sub>1</sub>)...(R<sub>m</sub>) are either "=", ">=", or "<=".
# 
# Remember that when we divide or multiply an inequality by a negative number we must change the symbol (<= for >=, and inverse).
# 
# ## Standard LP Model and Basic Solutions
# 
# The characteristics of a standard LP model are:
# 
# 1. All the constraints (except the non-negative constraints) are equations with a poitive or zero right hand sides.
# 2. All the variables are zero or positive.
# 3. The objective function can maximize or minimize an efficiency measure.
# 
# ## Formulation
# 
# It is impossible to give a detailed procedure for formulating linear programs which will work in every case. However, the following simple steps can be helpfully borne in mind.
# 
# <u>Step 1</u>: Identify the variables. These are sometimes known as 'activities' and represent things under our control. In our example we used x<sub>1</sub> and x<sub>2</sub> to represent the amounts of the two products to be produced each week. It is important to have defined the units of each variable carefully, so you understand precisely what x<sub>1</sub> = 1 means.
# 
# <u>Step 2</u>: Identify things which are to be constrained. These are often called "items". In our example these were the times available on the machines.
# 
# <u>Step 3</u>: Write down the objective function in terms of variables. We had
# f = 2x<sub>1</sub> + 3x<sub>2</sub>
# 
# <u>Step 4</u>: Add in any additional constraints, such as those involving the ratios of activities.
# 
# <u>Step 5</u>: Don't forget any non-negativity constraints! Our's were 
# 
# x<sub>1</sub>> = 0<br/>
# x<sub>2</sub>> = 0<br/>
# 
# 
# ## Examples
# 
# Formulate the following problems.
# 
# **Problem 1**. A manufacturing company company produces two models of grills, A and B. Manufacturing a grill of model A requires 3 ounces of steel and 6 labor hours. Model B requires 4 ounces of steel and 3 labor hours. The profit of model A is \\$2/unit and of model B is $1.5/unit. There are 100 ounces of steel available in inventory and 20 labor hours available per day. How many units of each model the company should produce so as to maximize the profit?
# 
# **Formulation Problem 1**.
# 
# Let x<sub>1</sub> be the number of model A grills<br/>
# Let x<sub>2</sub> be the number of model B grills<br/>
# 
# Objective function<br/>
# Max f = 2x<sub>1</sub> + 1.5x<sub>2</sub><br/>
# 
# Subject to<br/>
# 3x<sub>1</sub> + 4x<sub>2</sub> <= 100<br/>
# 6x<sub>1</sub> + 3x<sub>2</sub> <= 20<br/>
# x<sub>i</sub> >= 0<br/>
# x<sub>i</sub> INTEGERS<br/>
# i = 1, 2<br/>
# 
# **Problem 2**. A manufacturing company produces two models of lamps, L<sub>1</sub> and L<sub>2</sub>. Manufacturing a L<sub>1</sub> lamp requires 20 man-labor minutes. Model L<sub>2</sub> requires 30 man-labor minutes. Then, both models must go into a machine where it takes 10 minutes to process a single unit. There are 100 man-labor hours available and 80 machine hours available each month. The profit per unit for each model is 15 and 10 dollars, respectively. Elaborate a production plan so as to maximize the profit.
# 
# **Formulation Problem 2**.
# 
# Let x<sub>1</sub> be the number of L<sub>1</sub> lamps to be manufactured<br/>
# Let x<sub>2</sub> be the number of L<sub>2</sub> lamps to be manufactured<br/>
# 
# Objective function<br/>
# Max f = 15x<sub>1</sub> + 10x<sub>2</sub><br/>
# 
# Subject to<br/>
# 20x<sub>1</sub> + 30x<sub>2</sub> <= (100 \* 60)<br/>
# 10x<sub>1</sub> + 10x<sub>2</sub> <= (80 \* 60)<br/>
# x<sub>i</sub> >= 0<br/>
# x<sub>i</sub> INTEGERS<br/>
# i = 1, 2<br/>
# 
# **Problem 3**. Soon, kids will go back to school. An office supplies store knows this, and they are planning to have some special discounts on some products. Currently this store has 600 notebooks, 500 file keepers, and 400 pens in stock. The manager of the store is planning to pack these items as follows: Option 1) 2 notebooks, 1 file keeper, and 2 pens; Option 2) 3 notebooks, 1 file keeper, and 1 pen. The selling price of each pack is \\$6.5 and $7, repectively. How many units of each pack they should sell so as to maximize income?
# 
# **Formulation Problem 3**.
# 
# Let x<sub>1</sub> be the number of pack 1 units to be sold<br/>
# Let x<sub>2</sub> be the number of pack 2 units to be sold<br/>
# 
# Objective function<br/>
# Max f = 6.5x<sub>1</sub> + 7x<sub>2</sub><br/>
# 
# Subject to<br/>
# 2x<sub>1</sub> + 3x<sub>2</sub> <= 600<br/>
# x<sub>1</sub> + x<sub>2</sub> <= 500<br/>
# 2x<sub>1</sub> + x<sub>2</sub> <=400<br/>
# x<sub>i</sub> >= 0<br/>
# x<sub>i</sub> INTEGERS<br/>
# i = 1, 2<br/>
# 
# **Problem 4**. Another classic linear programming problem is the feed mix problem. This problem could also arise in determining the optimal ingredients in grass seed manufacturing, cereal making, or sausage formulation.
# 
# Suppose the Super Chicken Production Company requires an special formula to feed their chicken. The mixture must include a minimum of 15 units of substance A and minimum of 15 units of substance B. There are two components available on the market to produce the feed mix. X component has 1 unit of substance A and 5 units of substance B. Y component has 5 units of substance A and 1 unit of substance B. The cost of X component is \\$10. The cost of Y component is $30. The manager of Super Chicken Production Company must decide how to combine these components to meet the minimum requirements at the minimum cost.
# 
# **Formulation Problem 4**.
# 
# Let x<sub>1</sub> be the number of X component units to include in the mix<br/>
# Let x<sub>2</sub> be the number of Y component units to include in the mix<br/>
# 
# Objective function<br/>
# Min f = 10x<sub>1</sub> + 30x<sub>2</sub><br/>
# 
# Subject to<br/>
# x<sub>1</sub> + 5x<sub>2</sub> >= 15<br/>
# 5x<sub>1</sub> + x<sub>2</sub> >= 15<br/>
# x<sub>i</sub> >= 0<br/>
# i = 1, 2<br/>
# 
# **Problem 5**. A pharmaceutical company produces large and small pills of certain drug. Currently, they have 600g of the chemical substance from which the pills are produced. The large pills weights 40g and the small pills, 30g. They have some policies to follow:<br/>
# a) They must produce at least 3 large pills.<br/>
# b) The number of small pills must be at least as twice the number of large pills.<br/>
# 
# The profit they obtain from the large pills is \\$2/pill. And the profit they obtain from the small pills is $1/pill. Determine how many of each type they should produce.
# 
# **Formulation Problem 5**.
# 
# Let x<sub>1</sub> be the number of small pills to produce<br/>
# Let x<sub>2</sub> be the number of large pills to produce<br/>
# 
# Objective function<br/>
# Max f = x<sub>1</sub> + 2x<sub>2</sub><br/>
# 
# Subject to<br/>
# 30x<sub>1</sub> + 40x<sub>2</sub> <= 600<br/>
# x<sub>2</sub> >= 3<br/>
# x<sub>1</sub> >= 2x<sub>2</sub> or x<sub>1</sub> - 2x<sub>2</sub> >= 0<br/>
# x<sub>i</sub> >= 0<br/>
# x<sub>i</sub> INTEGERS<br/>
# i = 1, 2<br/>
# 
# **Problem 6**. An important store wants to put on sale 200 shirts and 100 pairs of jeans. They thought of two discount campaigns. The first discount consists of one shirt and one pair of jeans for \\$30. The second discount consists of 3 shirts and a  pair of jeans for $50. The current policy is to offer at least 20 packs under the fist discount plan and 10 under the second. How many packs under each discount plan they should sell if they want to maximize their income?
# 
# **Formulation Problem 6**.
# 
# Let x<sub>1</sub> be the number of packs (discount 1) on sale<br/>
# Let x<sub>2</sub> be the number of packs (discount 2) on sale<br/>
# 
# Objective function<br/>
# Max f = 30x<sub>1</sub> + 50x<sub>2</sub><br/>
# 
# Subject to<br/>
# x<sub>1</sub> + 3x<sub>2</sub> <= 200<br/>
# x<sub>1</sub> + x<sub>2</sub> <= 100<br/>
# x<sub>1</sub> >= 20<br/>
# x<sub>2</sub> >= 10<br/>
# x<sub>i</sub> >= 0<br/>
# x<sub>i</sub> INTEGERS<br/>
# i = 1, 2<br/>
# 
# **Problem 7**. Suppose the Super Chicken Production Company can purchase and mix one or more of three different grains, each containing different amounts of four nutritional ingredients. The production manager specifies that any feed mix for the chicken must meet certain minimal nutritional requirements and at the same time be as low in cost as possible. Grains can be bought and mixed on a weekly basis at known prices to meet known total nutritional requirements during that week.
# 
# The following table lists the requirements of each nutritional ingredient, the contribution fo each grain to the requirement, and the cost of each grain. The manager must decide how to combine these grains to meet the minimum requirements at the minimum cost.
# 
# *Grain Contribution per Unit Weight*
# 
# |Nutritional Ingredient|     Grain 1       |       Grain 2        |       Grain 3         | Minimum Total Requirement |
# |:--------------------:|:-----------------:|:--------------------:|:---------------------:|:-------------------------:|
# |        A             |         1         |           0          |           1           |         1,200             |
# |        B             |         3         |           2          |           0.5         |         4,000             |
# |        C             |         5         |           7          |           9           |         5,500             |
# |        D             |         0         |           3          |           4           |           750             |
# |----------------------|-------------------|----------------------|-----------------------|---------------------------|
# |  Cost / Unit Weight  |    &#36;30        |       &#36;37        |       &#36;45         |                           |
# 
# **Formulation Problem 7**.
# 
# Let x<sub>1</sub> be the amount of Grain 1 to include in the mix<br>
# Let x<sub>2</sub> be the amount of Grain 2 to include in the mix<br>
# Let x<sub>3</sub> be the amount of Grain 3 to include in the mix<br>
# 
# Objective function<br>
# Min f = 30x<sub>1</sub> + 37x<sub>2</sub></br> + 45x<sub>2</sub><br/>
# 
# Subject to<br/>
# x<sub>1</sub> + x<sub>3</sub> >= 1,200<br/>
# 3x<sub>1</sub> + 2x<sub>2</sub> + 0.5x<sub>3</sub> >= 4,000<br/>
# 5x<sub>1</sub> + 6x<sub>2</sub> + 9x<sub>3</sub> >= 5,500<br/>
# 3x<sub>2</sub> + 4x<sub>3</sub> >= 750<br/>
# x<sub>i</sub> >= 0<br/>
# i = 1, 2, 3<br/>
# 
# Note: The solution to this problem is to use 1,180.64 units of Grain 1, 1,224.19 of grain 2, and 19.36 units of Grain 3 at a total cost \\$44,385.48 for the entire mix. (ref. Production and Inventory Management, Fogarty, Blackstone, Hoffman, pg. 756-757, 1991).  
# 
# **Problem 8**. An airline company is considering the purchase of a new long-range, medium-range and short-range passenger jets. The purchase price would be \\$3M for each long-range plane, \$2M for each medium-range plane and \$1.5M for each short-range plane, and the company has authorized a maximum commitment of \$60M for these purchases. It is estimated that the net annual profit (after subtracting capital recovery costs) would be \$200,000, \$150,000 and \$100,000 for the long-, medium-, and short-range planes respectively.
# 
# It is predicted that enough trained pilots will be available to the company to man 30 new planes.
# 
# If only short-range planes were purchased, the maintenance facilities would be able to handle 40 new planes. However, each medium-range plane is equivalent to 1 1/3 short-range planes, and each long-range plane is equivalent to 1 2/3 short-range planes in terms of the use of maintenance facilities.
# 
# How many planes of each type should be purchased in order to maximize profit? (Ignore the fact that numbers of planes must be integer).
# 
# **Formulation Problem 8**.
# 
# Let x<sub>1</sub> be the number of long-range airplanes<br/>
# Let x<sub>2</sub> be the number of medium-range airplanes<br/>
# Let x<sub>3</sub> be the number of short-range airplanes<br/>
# 
# Constraints:
# 1. Investment
# 2. Number of pilots
# 3. Maintenance
# 
# Objective function<br/>
# Max f = 200,000x<sub>1</sub> + 150,000x<sub>2</sub> + 100,000x<sub>3</sub><br/>
# 
# Subject to<br/>
# 3x<sub>1</sub> + 2x<sub>2</sub> + 1.5x<sub>3</sub> <= 60<br/>
# x<sub>1</sub> + x<sub>2</sub> + x<sub>3</sub> <= 30<br/>
# 1 2/3x<sub>1</sub> + 1 1/3x<sub>2</sub> + x<sub>3</sub> <= 40<br/>
# x<sub>i</sub> >= 0<br/>
# x<sub>i</sub> INTEGERS<br/>
# 
# **Problem 9**. A metal products company produces waste cans, filing cabinets, correspondence boxes and lunch boxes. The manufacture of these products requires sheet Metal of two different thicknesses called A and B, and of course labor (measured in man hours). One waste can requires 0.6m<sup>2</sup> of A, 4 man hours and generates &#36;1.98 profit. One filing cabinet requires 1.0m<sup>2</sup> of B, 3 man hours, and generates &#36;44.95 profit. One correspondence box requires 0.2m<sup>2</sup> of A, 2 man hours, and generates &#36;9.95 profit. One lunch box requires 0.3m<sup>2</sup> of A, 3 man hours, and generates &#36;2.98 profit. This week there will be 22.5m<sup>2</sup> of A, 30.0m<sup>2</sup> of B and 190 man hours available.
# 
# The company also has a rolling machine which will convert 1m<sup>2</sup> of B to 2.5m<sup>2</sup> of A in one man hour at a cost of &#36;1.
# 
# How should the company maximize profit for the week?
# 
# **Formulation Problem 9**.
# 
# Let W be the number of waste cans/week<br/>
# Let F be the number of filing cabinets/weeks<br/>
# Let C be the number of correspondence boxes/week<br/>
# Let L be the number of lunch boxes/week<br/>
# Let X be the number of m<sup>2</sup> of B converted to A<br/>
# 
# Objective function<br/>
# Max f = 1.98W + 44.95F + 9.95C + 2.98L - X<br/>
# 
# S.T.(Subject to)<br/>
# 0.6W + 0.2C + 0.3L - 2.5X <= 22.5<br/>
# F + X <= 30<br/>
# 4W + 3F + 2C + 3L + X <= 190<br/>
# W, F, C, L, X >= 0<br/>
# W, F, C, L INTEGERS<br/>
# 
# **Problem 10**. An amateur dramatic society is putting on a show in a local hall. They must decide how many rows of hard chairs and how many rows of easy chairs to set out. 12 hard chairs can be arranged in one row or 10 easy chairs. They allow 3ft for each row of hard chairs and 3.5ft for each row of easy chairs and the hall is 84ft long. There are 280 hard chairs and 210 easy chairs available. They decide to provide at least twice as many rows of hard chairs as rows of easy chairs, but the hard chairs should not be more than 90% of the total no. of chairs. If they charge 50 cents for a hard chair and 65 cents for an easy chair, how many rows of each type should be set out?
# 
# **Formulation Problem 10**.
# 
# Let H be the number of rows of hard chairs<br/>
# Let E be the number of rows of easy chairs<br/>
# 
# O.F.(Objective function)<br/>
# Max f = (0.5 \* 12)H + (0.65 \* 10)E<br/>
# 
# S.T.<br/>
# 12H <= 280<br/>
# 10E <= 210<br/>
# H >= 2E or H-2E >= 0<br/>
# 12H <= 0.9(10E + 12H) or 1.2H - 9E <= 0<br/>
# 3H + 3.5E <= 84<br/>
# H, E >= 0<br/>
# H, E INTEGERS<br/>
# 
# **Problem 11**. Three types of crude petroleum are avilable as follows:
# 
# |               |   Octane Rating   |    Vapour Pressure   |   Gallons Available   |  Cost per Gallon   |
# |:-------------:|:-----------------:|:--------------------:|:---------------------:|:------------------:|
# |   Crude 1     |      108          |            4         |       32,000          |      40 cents      |
# |   Crude 2     |       90          |           10         |       20,000          |      24 cents      |
# |   Crude 3     |       73          |            5         |       38,000          |      24 cents      |
# 
# These may be blended to form premium or regular petrol. Premium has an octane rating of at least 100, a vapour pressure of no more than 6, and can be sold at a profit (ignoring the crudes) of 36 cents per gallon. Regular petrol has an octane rating of at least 80, a vapour pressure of 9 or less, and can be sold at a profit of 28 cents per gallon.
# 
# How should the petrol be blended to maximize profit?
# 
# **Formulation Problem 11**.
# 
# Let x<sub>1P</sub> be the gallons of crude 1 used to produce permium petrol<br/>
# Let x<sub>2P</sub> be the gallons of crude 2 used to produce permium petrol<br/>
# Let x<sub>3P</sub> be the gallons of crude 3 used to produce permium petrol<br/>
# Let x<sub>1R</sub> be the gallons of crude 1 used to produce regular petrol<br/>
# Let x<sub>2R</sub> be the gallons of crude 2 used to produce regular petrol<br/>
# Let x<sub>3R</sub> be the gallons of crude 3 used to produce regular petrol<br/>
# 
# O.F.<br/>
# Max f = 36(x<sub>1P</sub> + x<sub>2P</sub> + x<sub>3P</sub>) + 28(x<sub>1R</sub> + x<sub>2R</sub> + x<sub>3R</sub>)<br/>
# 
# S.T.<br/>
# 108x<sub>1P</sub> + 90x<sub>2P</sub> + 73x<sub>3P</sub> >= 100<br/>
# 4x<sub>1P</sub> + 10x<sub>2P</sub> + 5x<sub>3P</sub> <= 6<br/>
# 108x<sub>1R</sub> + 90x<sub>2R</sub> + 73x<sub>3R</sub> >= 80<br/>
# 4x<sub>1R</sub> + 10x<sub>2R</sub> + 5x<sub>3R</sub> <= 9<br/>
# x<sub>1P</sub> + x<sub>1R</sub> <= 32,000<br/>
# x<sub>2P</sub> + x<sub>2R</sub> <= 20,000<br/>
# x<sub>3P</sub> + x<sub>3R</sub> <= 38,000<br/>
# x<sub>ij</sub> >= 0<br/>
# i = 1, 2, 3<br/>
# j = P, R<br/>
# 
# **Problem 12**. A manufacturer wishes to produce 1 ton of an alloy where the percentages of lead and zinc are equal and the percentage of tin lies between 35% and 45%. There are on the market alloys with the following compositions and prices.
# 
# |     Alloy     |        A          |           B          |          C            |          D         |
# |:-------------:|:-----------------:|:--------------------:|:---------------------:|:------------------:|
# |   % Lead      |       10          |           10         |           40          |         35         |
# |   % Zinc      |       10          |           30         |           50          |         15         |
# |   % Tin       |       30          |           60         |           10          |         50         |
# |---------------|-------------------|----------------------|-----------------------|--------------------|
# |Price per Ton  |       41          |           43         |           58          |           50       |
# 
# How much of each type of allow should be purchased to minimize cost?
# 
# **Formulation Problem 12**.
# 
# Let x<sub>A</sub> be the tons of alloy A used to produce the ton of alloy<br/>
# Let x<sub>B</sub> be the tons of alloy B used to produce the ton of alloy<br/>
# Let x<sub>C</sub> be the tons of alloy C used to produce the ton of alloy<br/>
# Let x<sub>D</sub> be the tons of alloy D used to produce the ton of alloy<br/>
# 
# O.F.<br/>
# Min f = 41x<sub>A</sub> + 43x<sub>B</sub> + 58x<sub>C</sub> + 50x<sub>D</sub><br/>
# 
# S.T.<br>
# 0.10x<sub>A</sub> + 0.10x<sub>B</sub> + 0.40x<sub>C</sub> + 0.35x<sub>D</sub> = 0.10x<sub>A</sub> + 0.30x<sub>B</sub> + 0.50x<sub>C</sub> + 0.15x<sub>D</sub>   or<br/>
# -0.2x<sub>B</sub> - 0.1x<sub>C</sub> + 0.2x<sub>D</sub> = 0<br/>
# 0.3x<sub>A</sub> + 0.6x<sub>B</sub> + 0.1x<sub>C</sub> + 0.5x<sub>D</sub> >= 0.35(x<sub>A</sub> + x<sub>B</sub> + x<sub>C</sub> + x<sub>D</sub>)<br/>
# 
# Note: x<sub>A</sub> + x<sub>B</sub> + x<sub>C</sub> + x<sub>D</sub> = 1;<br/> 
# Therefore...<br/>
# 0.3x<sub>A</sub> + 0.6x<sub>B</sub> + 0.1x<sub>C</sub> + 0.5x<sub>D</sub> >= 0.35<br/>
# 0.3x<sub>A</sub> + 0.6x<sub>B</sub> + 0.1x<sub>C</sub> + 0.5x<sub>D</sub> <= 0.45<br/>
# x<sub>A</sub> + x<sub>B</sub> + x<sub>C</sub> + x<sub>D</sub> = 1<br/>
# x<sub>A</sub>, x<sub>B</sub>, x<sub>C</sub>, x<sub>D</sub> >= 0<br/>
# 
# **Problem 13**. The Soft Suds Brewing Company, because of faulty planning, was not prepared for a long weekend coming up. There was to be a big disco at University of lancaster and Charles Guzzler, the manager, knew that Soft Suds would be called upon to supply the refreshments. However, the raw materials required had not been ordered and could be obtained before the weekend. Charles took inventory of the available supplies and found the following:
# 
# Malt: 500 units<br/>
# Hops: 250 units<br/>
# Yeast: 250 units<br/>
# 
# Soft Suds has 3 products: lager, bitter, and brown ale, with the following specifications:
# 
# *Requirements per barrel*
# 
# |             |    Malt    |    Hops    |    Yeast    |
# |:-----------:|:----------:|:----------:|:-----------:|
# |    Lager    |     2      |      1     |      2      |
# |   Bitter    |     4      |      3     |      2      |
# |  Brown Ale  |     7      |      2     |      2      |
# 
# The 3 products bring profits of \\$5/barrel, \$10/barrel, and \$15/barrel, respectively. Charles knows that the students will boy whatever is available! Formulate the problem of maximizing profit as a linear program.
# 
# (For interest: The optimum is to make about 47 barrels for A and B, and 31 of C, giving a profit of \\$1,170)
# 
# Note: This problem is adapted from W. Spivey & R, Thrall (1970) *Linear Optimization*.
# 
# **Formulation Problem 13**.
# 
# Let L be the number of barrels of lager<br/>
# Let B be the number of barrels of bitter<br/>
# Let A be the number of barrels of brown ale<br/>
# 
# O.F.<br/>
# Max f = 5L + 10B + 15C<br/>
# 
# S.T.<br/>
# 2L + 4B + 7A <= 500 (Malt limit)<br/>
# L + 3B + 2A <= 250 (Hops limit)<br/>
# 2L + 2B + 2A <= 250 (Yeast limit)<br/>
# L, B, A >= 0 (Non-negativity)<br/>
# 
# **Problem 14**. A charter flying company in Florida contracts to deliver ammunition, guns and drugs to a client. The client will accept whatever he can get.
# 
# |               |   Density: (Pounds/Cubic Ft.)   | Profit: &#36;/pound |
# |:-------------:|:-------------------------------:|:-------------------:|
# |   Ammunition  |               30                |        3.00         |
# |      Guns     |               40                |        4.50         |
# |      Drugs    |               20                |        1.50         |
# 
# The company has two planes. Plane A can carry no more than 15,000 pounds and no more than 100 cubic feet of cargo. Plane B can carry up to 25,000 pounds of cargo and no more than 200 cubic feet. One restriction is imposed: no more than 100 pounds of drugs may be delivered with each delivery (one flight each by both A and B is defined as a delivery). Formulate the problem of maximizing the profit of one delivery as a linear program.
# 
# Six variables are needed for this problem.
# 
# (For interest: The optimum is to fill up both planes with guns, giving a profit of \\$54,000)
# 
# Note: This problem is adapted from W. Spivey & R, Thrall (1970) *Linear Optimization*.
# 
# **Formulation Problem 14**.
# 
# Let AA be the number of cubic feet of ammunition in plane A
# Let AB be the number of cubic feet of ammunition in plane B
# Let GA be the number of cubic feet of guns in plane A
# Let GB be the number of cubic feet of guns in plane B
# Let DA be the number of cubic feet of drugs in plane A
# Let DB be the number of cubic feet of drugs in plane B
# 
# O.F.<br/>
# Max f = (3 \* 30)(AA + AB) + (4.5 \* 40)(GA + GB) + (1.5 \* 20)(DA + DB) = 90AA + 90AB + 180GA + 180GB + 30DA + 30DB<br/>
# 
# S.T.<br/>
# 30AA + 40GA + 20DA <= 15,000 (Weight limit on Plane A)<br/>
# 30AB + 40GB + 20DB <= 25,000 (Weight limit on Plane B)<br/>
# AA + GA + DA <= 100 (Volume limit on Plane A)<br/>
# AB + GB + DB <= 200 (Volume limit on Plane B)<br/>
# 20DA + 20DB <= 100 (Drugs limit)<br/>
# AA, AB, GA, GB, DA, DB >= 0 (Non-negativity)<br/>
# 
# **Problem 15**. A manufacturing firm has discontinued production of a certain unprofitable product line. This created considerable excess production capacity on three machines. Management is considering devoting this excess capacity to one or more of three products, which we will call products 1, 2, and 3. The following table gives some relevant data.
# 
# *Productivity (units processed / hour)*
# 
# |      Machine     | Available Time (hours per week) | Product 1 | Product 2 | Product 3 |
# |:----------------:|:-------------------------------:|:---------:|:---------:|:---------:|
# |  Milling Machine |             200                 |    75     |    30     |    20     |
# |     Lathe        |             100                 |    15     |    20     |    --     |
# |    Grinder       |              50                 |    30     |    --     |    60     |
# 
# Sales potential for products 1 and 2 is unlimited; sales potential for product 3 is 20 units/week. Products 1, 2, and 3 give \\$10, \$3, and \$4 unit profit respectively. Formulate the problem of maximizing profit as a linear program.
# 
# (For interest; the optimum is to make about 1,490 of product 1, but only 13 of product 2 and 20 of product 3. This gives a profit of \\$15,019.)
# 
# **Formulation Problem 15**.
# 
# Let x<sub>i</sub> be the number of units of product *i* processed per week, for *i* = 1, 2, 3.<br/>
# 
# O.F.<br/>
# Min f = 10x<sub>1</sub> + 3x<sub>2</sub> + 4x<sub>3</sub><br/>
# 
# S.T.<br/>
# (x<sub>1</sub>/75) + (x<sub>2</sub>/30) + (x<sub>3</sub>/20) <= 200 (Milling hours)<br/>
# (x<sub>1</sub>/15) + (x<sub>2</sub>/20) <= 100 (Lathe hours)<br/>
# (x<sub>1</sub>/30) + (x<sub>3</sub>/60) <= 50 (Grinder hours)<br/>
# x<sub>3</sub> <= 20 (Sales of product 3)<br/>
# x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub> >= 0<br/>
# 
# Note that productivity is units per hour, not hours per unit. Thus we divide by 75, 30, etc. instead of multiplying.
# 
# **Problem 16**. Solid rock fuels A, B, and C are to be blended to provide a satisfactory fuel at a minimum cost. Three factors are measured for each fuel type as follows:
# 
# |           | Thrust per cubic inch |  Corrosion factor per cubic inch | Density in pounds per cubic inch |
# |:---------:|:---------------------:|:--------------------------------:|:--------------------------------:|
# |   Fuel A  |           10          |               10                 |               0.6                |
# |   Fuel B  |            5          |                4                 |                 1                |
# |   Fuel C  |            2          |                6                 |               0.8                |
# 
# The fuels must be blended so that the average thrusts per cubic inch is at least 4.2. The average corrosion factor for the mixture cannot exceed 6.4 per cubic inch and the average density must be less than or equal to 0.85 pounds per cubic inch. Fuel A costs \\$50 per cubic inch, Fuel B costs \$25, and Fuel C costs \$40. It takes 1,000 lbs of fuel to put a rocket into orbit. Formulate the problem of minizing cost as a linear program.
# 
# (For interest: the optimum is to use about 441 cu in A, 735 cu in B and no C. This gives a cost of about \\$40,441.)
# 
# Note: Thrust: A propulsive force produced by the fluid pressure or the change of momentum of the fluid in a jet engine, rocket engine, etc.
# 
# **Formulation Problem 16**.
# 
# Let A be the volume of fuel A used (in cubic inches).<br/>
# Let B be the volume of fuel B used (in cubic inches).<br/>
# Let C be the volume of fuel C used (in cubic inches).<br/>
# 
# At first sight it looks like the formulation should be:
# 
# O.F.<br/>
# Min f = 50A + 25B + 40C<br/>
# 
# S.T.<br>
# (10A + 5B + 2C) / (A + B + C) >= 4.2 (Minimum thrust)<br/>
# (10A + 4B + 6C) / (A + B + C) <= 6.4 (Maximum corrosion)<br/>
# (0.6A + 1B + 0.8C) / (A + B + C) <= 0.85 (Maximum density)<br/>
# 0.6A + 1B + 0.8C = 1,000 (Fuel requirement)<br/>
# A, B, C >= 0 (Non-negativcity)<br/>
# 
# However, the first three constraint contain *division* and are therefore *non-linear*. To make this into a linear program, we have to *linearize* these constraints (i.e., make them linear). To do this, multiply sides of each inequality by A + B + C to give:
# 
# (10A + 5B + 2C) >= 4.2(A + B + C) (Minimum thrust)<br/>
# (10A + 4B + 6C) <= 6.4(A + B + C) (Maximum corrosion)<br/>
# (0.6A + 1B + 0.8C) <= 0.85(A + B + C) (Maximum density)<br/>
# 
# These can then be simplified to give:
# 
# 5.8A + 0.8B - 2.2C >= 0 (Minimum thrust)<br/>
# 3.6A - 2.4B - 0.4C >= 0 (Maximum corrosion)<br/>
# -0.25A + 0.15B - 0.05C <= 0 (Maximum density)<br/>
# 
# **Problem 17**. A firm requires coal with <= 0.03% phosphorous and <= 3.25% ash impurity. Three grades of coal (A, B, and C) are available at prices shown:
# 
# |  Grade | % Phosphorous | % Ash | Cost &#36;/ton |
# |:------:|:-------------:|:-----:|:--------------:|
# |    A   |      0.06     |  2.0  |       50       |
# |    B   |      0.04     |  4.0  |       50       |
# |    C   |      0.02     |  3.0  |       75       |
# 
# The goal is to blend these three grades together in order to meet impurity restrictions at minimum cost. Show how this can be formulated as a linear program.
# 
# For this question we are not told how much coad need to be made. So we work with *proportions*. (Equivalently, we assume that we are making only one ton of coal.)
# 
# (For interest: the optimum is blend the three grades in a ratio of 1:4:7. This gives a cost of \\$64.58 per ton.)
# 
# **Formulation Problem 17**.
# 
# Let x<sub>i</sub> proportion of coal of grade *i* in blend, for *i* = 1, 2, 3.<br/>
# 
# O.F.<br/>
# Min f = 50x<sub>1</sub> + 50x<sub>2</sub> + 75x<sub>3</sub><br/>
# 
# S.T.<br/>
# 0.06x<sub>1</sub> + 0.04x<sub>2</sub> + 0.02x<sub>3</sub> <= 0.03 (Phosphorous limit)<br/>
# 2x<sub>1</sub> + 4x<sub>2</sub> + 3x<sub>3</sub> <= 3.25 (Ash limit)<br/>
# x<sub>1</sub> + x<sub>2</sub> + x<sub>3</sub> = 1 (Proportions sum to one)<br/>
# x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub> >= 0 (Non-negativity)<br/>
# 
# **Problem 18**. A paper mill manufactures its papers in standard reels 20ft. wide and custs there reels into a number of smaller, and possibly different, widths to meet its customers' requirements. This process usually results in some portion of each reel being left over which is unfortunately wasted. The mill has received the following orders for paper and naturally wishes to cut up its standard reels in such a way as to minimize the total waste.
# 
# |  Width (ft)  |   Length (no. reels)   |
# |:------------:|:----------------------:|
# |      9       |           30           |
# |      7       |          150           |
# |    5 1/2     |           65           |
# 
# Formulate the problem as a linear program.
# 
# Hint: You will need to define some integer variables.
# 
# **Formulation Problem 18**.
# 
# We enumerate all possible ways in which a reel can be cut:
# 
# |  Combination  |      Widths Produced     |   Waste  |
# |:-------------:|:------------------------:|:--------:|
# |       1       |    9,   9                |     2    |
# |       2       |    9,   7                |     4    |
# |       3       |    9,   5 1/2,  5 1/2    |     0    |
# |       4       |    7,   7,  5 1/2        |   1/2    |
# |       5       |    7,   5 1/2,  5 1/2    |     3    |
# |       6       |    5 1/2,  5 1/2,  5 1/2 |  3  1/2  |
# 
# There are other possibilities, such as cutting only one piece of width 9 and wasting 11 ft, but all of these other combinations produce unnecessary waste.
# 
# Now we define an integer variable x<sub>i</sub> for *i* = 1, 2, 3, 4, 5, 6, representing the number of reels of paper which are cut according to each combination *i*.
# 
# Now, since the amount of paper to be sold to customers is a constant, minimizing the total number of reels used will automatically minimize total waste.
# Total waste = total area from the reals used - area required
# 
# Area required by customers is constant so total waste is minimized by minimizing the number of reels used.
# 
# O.F.<br/>
# Min f = x<sub>1</sub> + x<sub>2</sub> + x<sub>3</sub> + x<sub>4</sub> + x<sub>5</sub> + x<sub>6</sub><br/>
# 
# S.T.<br>
# 2x<sub>1</sub> + x<sub>2</sub> + x<sub>3</sub> >= 30 (width 9 requirement)<br/>
# x<sub>2</sub> + 2x<sub>4</sub> + x<sub>5</sub> >= 150 (width 7 requirement)<br/>
# 2x<sub>3</sub> + x<sub>4</sub> + 2x<sub>5</sub> + 3x<sub>6</sub> >= 65 (width 5 1/2 requirement)<br/>
# x<sub>1</sub>, x<sub>2</sub>, x<sub>3</sub>, x<sub>4</sub>, x<sub>5</sub>, x<sub>6</sub> >= 0 (Non-negativity)<br/>
# 
# (The optimal solution uses 90 reels; cut 5 reels according to combination 1, 20 according to combination 2, and 65 according to combination 4. Totla waste 122.5 ft, or the equivalent of 6.125 reels.)
