#!/usr/bin/env python
# coding: utf-8

# # Beginning Apache Spark Using Azure Databricks: Unleashing Large Cluster Analytics in the Cloud. 
# 
# Please refer to: ***1. Robert Ilijason, 2020. "Beginning Apache Spark Using Azure Databricks," Springer Books, Springer, number 978-1-4842-5781-4, August.***
# 
# Elaborated by: Hernan Carlos Chavez Paura Garcia
# 
# Date: July 17, 2022

# ## Chapter One. Introduction to Large-Scale Data Analytics
# 
# ### Summary
# 
# While analytics has been around for a long time, increases in data volumes, easy access to cloud processing power, and great open source tools have enabled new opportunities in the anaytics field.
# 
# One of the most popular frameworks available, Apache Spark, has risen to the top on the tool side. Databricks has made using it in the cloud easy. With a few button clicks you can have it handle billions upon billions of rows of data without even breaking a sweat. Throw petabytes at it and it'll just shrug.
# 
# It's also a complete toolset with everything you need to load, scrub, and analyze data using a huge amount of resources that you can rent from pay-as-you-go cloud providers such as Microsoft or Amazon.
# 
# Databricks probably won't replace your data warehouse nor your desktop analytics tools even though it could take on those chores. It's the power tool you pick up when everything else fails - the beast to unleash when things get really hairy.
# 
# Still, the tool doesn't do all the work. Ultimately, you need to consider what to do, how it will help your business, what the result will look like, and who will take your findings and make sure they are implemented and maintained.
# 
# Next, let's look at what Spark is, how it works, and what makes Databricks special.

# ## Chapter Two. Spark and Databricks
# 
# ### Data Processing
# 
# On a high level, RDDs support two things: transformations and actions. Transformations are operations on RDDs that return one or more new RDDs. As you might recall, all RDDs are immutable which is why new RDDs have to be made.
# 
# If you build up a chain of transformations, maybe combining sorting and grouping, nothing will happen immediately. This is because Spark does lazy evaluation. It basically just builds a map of everything that you asked for in an optimized order. This is the Directed Acyclic Graph, or DAG, we talked about earlier. let's look at an example in Python:
# 
# ***df = spark.sql('select from sales')***<br/>
# ***df.select('country', 'sales').filter(df\['region'\] == 'EU').groupBy('country')***
# 
# Don't worry if the code looks confusing, you'll get familiar with it in Chapter Seven. It picks up data from sales table and then groups the data to sum sales per country. A filter makes sure that only use data from EU countries.
# 
# No matter if you have ten rows or billions of rows, running this will take a split second. The reason is that we only do transformations. Spark realizes this and decides not to bother the executors with it just yet. Let's look at another statement:
# 
# ***df2 = df.select('country', 'sales').filter(df\['region'\] == 'EU').groupBy('country')***
# 
# We now assign the result to a new DataFrame. In this case, you might think that the assignment will create an action, but it but it won't. It's not until you actually do something with the DataFrame that you will end up creating an action that triggers work. Let's show a couple of actions:
# 
# ***display(df2)***<br/>
# ***df.count()***<br/>
# ***df.write.parquet('/tmp/p.parquet')***
# 
# Actions are what get work going. They return non-RDD results, like data to the driver or to storage. In the preceding example, the first one runs a collect to pick up rows. The second one shows a count of rows. The third saves to a file system. It makes sense if you think about it. All of these actions require results to be available, which you only have once the processing is done.
# 
# These manipulations and actions are what the driver needs to consider when you pass on a job. The lazy evaluation makes it possible for it to optimize the whole job instead of just one step.
# 
# In a later chapter, we'll actually look at DAGs to see how they work more in detail. Looking at them can be helpful if you think that executions takes longer that expected. You can usually find hints of issues in the execution plan.
# 
# ### Summary
# 
# Over the pages of this chapter, we've gone through what both Apache Spark and Databricks are. You should now have an understanding of what it is that makes the tools stick out and where they fit into the data analytics ecosystem.
# 
# We have also talked about how data is being processed in the tool, with drivers handing tasks over the executors. You've seen how Apache Spark builds on top of cluster technology and how that makes it fast.
# 
# Then we went through data both from an internal and external perspectives. We read up to RDD's, DataFrames, and datasets and how lazy evaluations hold transformations back until there's an action.
# 
# To round everything off, we quickly went through the four packages that are being offered on top of Spark. One of them, Spark SQL, you'll be using soon. The others will come back in the latter part of the material.
# 
# Now that you have an understanding of how Apache Spark works in general, it's time to start digging into Databricks. To do that, you'll need to get up and running with the tool. That's exactly what we'll do in the next chapter.
# 
# So next up, working with Databricks.

# ## Chapter Three. Getting Started with Databricks
# 
# ### Summary
# 
# In this chapter, we went through the different versions of Databricks. We also got both the community edition and the commercial editions up and running on both of the available cloud platforms.
# 
# Now that we have our Databricks system ready to go in your preferred cloud, it's time to get familiar with the environment. Fortunately, this is exactly what we'll discuss in the next chapter.

# ## Chapter Four. Workspaces, Clusters, and Notebooks
# 
# When you start Databricks, you are met by a general start screen (Fig. 1). To the left, you have a small toolbar with a few buttons connected to features in the tool. On the top bar, you have links connected to your cloud account. Just beneath that and to the right, you have a quick link to the documentation and another one to your user account. Finally, you have a starty page with a bunch of quick links to different functions in the middle.
# 
# As Databricks is a cloud service, expect the UI to change from month to month. This immager is from summer 2022. 
# 
# *Fig. 1*
# 
# <p align="center">
#     <img src="Images/4_1a.png" alt="Fig. 1" width="1500"/>
#     <img src="Images/4_1b.png" alt="Fig. 1" width="200"/>
# </p>
# 
# Let's start with a few on the middle section, even tough it's just a bunch of shortcuts. On the top, you have links to the quickstart guide, the import feature, and notebook creation. We'll come back to that later. You also have common tasks in the first column, recent files in the second, and links to the documentation - all pretty self-explanatory.
# 
# While you can do all the things available here at different places, I frequently come back to the start page to create a blank notebook. It's also a good place to pick up where you left off, considering that you can see your recent files here as well.
# 
# Mostly though, you'll be using the left bar to actually access features and documents. It's available at all times, and most buttons will not transport you to another page, but rather just open a box on top of the existing page. Unfortunately, there's no indicator of which button opens a box and which replaces the workspace, but you'll quickly learn which one does what.
# 
# The top button, Databricks, will just take you to the start page where you already are. Both Home and Workspace will open the folder structure where you keep your files. The difference between them is that the Home button will take you to your personal folder, while Workspace will return you to the place you were when you last closed the bar.
# 
# We'll talk more about this folder structure later, but there are a couple of interesting things here worth mentioning already now. First, at the root you have folders containing documentation and training material. Second, at the same level, you have a Shared folder. While you don't need to use it for shared material, it's a good place for actually doing so as it's there by default.
# 
# Recents are, as you might imagine, a list of files and views you recently visited. Infortunately, it's just a list oflinks. You don't get any metadata in this view, so you for instance don't know if you used the ducment last week or last year.
# 
# Next up is Data. THis one you will probably use a lot. It lists all databases (or schemas), if you prefer that nomenclature) snd tables in that database. You only see what you've stored in the metastore, so text files on you data lake won't appear here. We'll talk more about this in the next chapter.
# 
# The following two buttons are different in that they actually open new pages in the main view. So if you're in a notebook and click Clusters of Jobs, you'll replace what you were working with in the main owrk window. If you do it by mistake, the browser back button will help you come back to where you were.
# 
# Clusters is where you define and handle the underlying engines of Databricks. This is where you tell the system how many processing cores and memory you need. You can switch between clusters and pools at the top of the main view. We'll play around with this in a bit.
# 
# Jobs, which we will investigate in depth in Chapter 11, is where you schedule your finished products to run either again and again or at a given time. You define what needs to be done, which cluster should do it, and on what schedule. Then Databricks will make sure that your jobs are executed on time. You can also track what happened here.
# 
# Finally, Search will let you search in the folder structure for a document, folder, or user. It's pretty nifty if you use the same porefix for files connected to a project as you can then use subfolder and still get everything in one list.
# 
# Note that if you want to find stuff in the documentation or the Databricks forum, you can instread click the question mark up and go to the right. The result will open up in a different tab in your web browser.
# 
# About navigation, It's
# 
# 
# 
# ### Summary
