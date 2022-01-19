#!/usr/bin/env python
# coding: utf-8

# # Chapter Two: Introduction to the Python World
# **Fabio Nelli**
# 
# **Hernan Chavez 1/7/2021**
# 
# **Book Blurb<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).**
# 
# ## Python-The Programming Language
# Python-The Programming Language<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ## Python-The Interpreter
# Python-The Interpreter<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ### Cython
# Python-The Interpreter > Cython<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ### Jython
# Python-The Interpreter > Jython<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ### PyPy
# Python-The Interpreter > PyPy<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ## Python 2 and Python 3
# Python 2 and Python 3<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ### Installing Python
# Python 2 and Python 3 > Installing Python<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# In order to develop programs in Python you have to install it on your operating system. Linux distributions and MacOS X machines should already have preinstalled version of Python. If not, or if you would like to replace that version with another, you can easily install it. The installation of Python differs from operating system to operating system; however, it is a rather simple operation.
# 
# On Debian-Ubuntu Linux systems, run this command
# 
# *apt-aget install python*
# 
# On Red Hat Fedora Linux systems working with *rpm* packages, run this command
# 
# *yum install python*
# 
# If you are running Windows or MacOS X, you can go to the official Python site (https://www.python.org/) and download the version you prefer. The packages in this case are installed automatically.
# 
# However, today there are distributions that provide a number of tools that make the management and installation of Python, all libraries, and associated applications easier. I strongly recommend you choose one of the distributions available online.
# 
# ## Python Distributions
# Python Distributions<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ### Anaconda
# Python Distributions > Anaconda<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# Anaconda is a free distribution of Python packages distributed by Continuum Analytics (https://www.anaconda.com/). This distribution supports Linux, Windows, and MacOS X operating systems. Anaconda, in addition to providing the latest packages released in the Python world, comes bundled with most of the tools you need to set up a Python development environment.
# 
# Indeed, when you install the Anaconda distribution on your system, you can use many tools and applications described in this chapter, without worrying about having to install and manage each separately. The basic distribution includes Spyder as the IDe, IPython QtConsole, and Notebook.
# 
# The management of the entire Anaconda distribution is perfromed by an application called *conda* This is the package manager and the environment manager of the Anaconda distribution and it handles all of the packages and their versions.
# 
# *conda install <package_name\>*
# 
# One of the most interesting aspects of this distribution is the ability to manage multiple development environments, each with its own version of Python/ Indeed, when you install Anaconda, the Python version 2.7 is installed by default. All installed packages then will refer to that version. This is not a problem, because Anaconda offers the possibility to work simulatenously and independently with other Python versions by creating a new environment. You can create, for instance, an environment based on Python 3.6.
# 
# *conda create -n py36 python=3.6 anaconda*
# 
# This will generate a new Anaconda enviroment with all the packages related to the Python 3.6 version. This installation will not affect in any way the environment built with Python 2.7. Once it's installed, you can activate the new environment by entering the following command.
# 
# *source activate py36*
# 
# On Windows, use this instead:
# 
# *activate py36*
# 
# *C:\Users\Hernan>activate py36<br/>
# (py36) C:\Users\Hernan>*
# 
# You can create as many versions of Python as you want; you need only to change the parameter passed with the python option in the conda *create* command. When you want to return to work with the original Python version, you have to use the following command:
# 
# *source deactivate*
# 
# On Windows, use this:
# 
# *(py36) C:\Users\Hernan>deactivate<br/>
# Deactivating environment "py36"...<br/>
# C:\Users\Hernan>*
# 
# ### Enthought Canopy
# Python Distributions > Enthought Canopy<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ### Python(x,y)
# Python Distributions > Python(x,y)<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ## Using Python
# Using Python<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ### Python Shell
# Using Python > Python Shell<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# The asiest way to approach the Python world is to open a session in the Python shell, which is a terminal running a command line. In fact, you can enter one comma at a time and test its operation manually. This mode makes clear the nature of the interpreter that underlies Python. In fact, the interpreter can read one command at a time, keeping the status of the variables specificed in the previous lines, a behavior similar to that of MATLAB and other claculation software.
# 
# This approach is helpful when apporaching Python the first time. You can test commands one at a time without having to write, edit, and run an entire program, which could be composed of many lines of code.
# 
# This model is also good for testing and debugging Python code one line at a time, or simply to make calculations. To start a session on the terminal, simply type this con the command line:
# 
# <img src="Figures/2_1.jpg" alt="Python shell start" width="900" height="900">   
# 
# Now the Python shell is active and the interprete is ready to receive commands in Python. Start by entering the simplest of commands, but a classic for getting started with programming.
# 
# <img src="Figures/2_2.jpg" alt="Python shell print" width="900" height="900">  
# 
# ### Run an Entire Program
# Using Python > Run an Entire Program<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# The best way to become familiar with Python is to erite an entire program and then run it from the terminal. First write a program using a simple text editor. For example, you can use the code shown in Listing 2-1 and save it as *MyFirstProgram.py*.
# 
# *Listing 2-1. MyFirstProgram.py*
# 
# <img src="Figures/2_3.jpg" alt="MyFirstProgram.py" width="600" height="600">  
# 
# Now you've written your first program in Python, and you can runn it directly from the command line by calling the python command and then the name of the file containing the program code.
# 
# <img src="Figures/2_4.jpg" alt="MyFirstProgram.py run" width="800" height="800"> 
# 
# ### Implement the Code Using an IDE
# Using Python > Implement the Code Uisng an IDE<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ### Interact with Python
# Using Python > Interact with Python<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ## Writing Python Code
# Writing Python Code<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ### Make Calculation
# Writing Python Code > Make Calculations<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# You have already seen that the *print()* function is useful for printing almost anything. Python, in addition to being a printing tool, is also a great calculator. Start a session on Python shell and begin to perform these mathematical operations:

# In[1]:


1 + 2


# In[2]:


(1.045 * 3)/4


# In[3]:


4 ** 2


# In[4]:


((4 + 5j) * (2 + 3j))


# In[5]:


4 < (2 * 3)


# Python can calculate many types of data including complex numbers and conditions with Boolean values. As you can see from these calculations, Python interpreter directly returns the result if the calculations without the need to use the *print()* function. The same thing applies to values contained in variables. it's enough to call the variable to see its contents.

# In[6]:


a = 12 * 3.4
a


# ### Import New Libraries and Functions
# Writing Python Code > Import New Libraries and Functions<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# You saw that Python is characterized by the ability to extend its functionality by importing numerous packages and modules. To import a module in its entirety, you have to use the *import* command.  

# In[7]:


import math


# In this way all the functions contained in the *math* package are available in your Python session so you can call them directly. Thus you have extended the standard set of functions available when you start a Python session. These functions are called with the following expression.
# 
# *library_name.function_name()*
# 
# For example, you can now calculate the sine of the value contained in the variable *a*.

# In[8]:


math.sin(a)


# As you can see, the function is called along with the name of the library. Sometimes you might find the following expression for declaring an import.

# In[9]:


from math import *


# Even if this works properly, it is to be avoided for good practice. In fact, writing an import in this way involves the importation of all functions without necessarily defining the libreary to which they belong.

# In[10]:


sin(a)


# This form of import can lead to very large errors, especially if the imported libraries are numerous. In fact, it is not unlikely that different libraries have functions with the same name, and importing all of these would result in an override of all functions with the same name previously imported. Therefore the behavior of the program could generate numerous errors or worse, abnormal behavior.
# 
# Actually, this way to import is generally used for only a limited number of functions, that is, functions that are strictly necessary for the functioning of the program, thus avoiding the importation of an entire library when it is completely unecessary.

# In[11]:


from math import sin


# ### Data Structure
# Writing Python Code > Data Structure<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# You saw in the previous examples how to use simple variables containing a single value. Python provides a number of extremely useful data structure. These data structure are able to contain lots of data simulatenously and sometimes even data of different types.
# 
# The various data structures provided are defined differently depending on how their data are structured internally.
# 
# * List
# * Set
# * Strings
# * Tuples
# * Dictionary
# * Deque
# * Heap
# 
# This is only a small part of all the data structures that can be made with Python. Among all these structures, the most commonly used are *dictionaries* and *lists*.
# 
# The type *dictionary*, defined also as *dicts*, is a data structure in which each particular value is associated with a particular label, called a *key*. The data collected in a dictionary have no internal order but are only definitions of key/value pairs. 

# In[12]:


dict = {'name':'William', 'age':25, 'city':'London'}


# If you want to access a specific value within the dictionary, you have to indicate the name of the associated key.

# In[13]:


dict['name']


# If you want to iterate the pairs of values in a dictionary, you have to use the *for-in* construct. This is possible through the use of the *items()* function.

# In[14]:


for key, value in dict.items():
    print(key,value)


# The type *list* is a data structure that contains a number of objects in a precise order to form a sequence to which elements can be added and removed. Each item is marked with a number corresponding to the order of the sequence, called *index*.

# In[15]:


list = [1, 2, 3, 4]
list


# If you want to access the individual elements, it is sufficient to specify the index in square brackets (the first item in the list has 0 as its index), while if you take out a portion of the list (or a sequence), it is sufficient to specify the range with the indices i and j corresponding to the extremes of the portion.

# In[16]:


list[2]


# In[17]:


list[1:3]


# If you are using a negative indices instead, this means you are considering the last in the list and gradually moving to the first.

# In[18]:


list[-1]


# In order to do a scan of the elements of a list, you can use the *for-in* construct.

# In[19]:


items = [1, 2, 3, 4, 5]
for item in items:
    print(item + 1)


# ### Functional Programming
# Writing Python Code > Functional Programming<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# The *for-in* shown in the previous example is very similar to loops found in other programming languages. But actually, if you want to be a "Python" developer, you have to avoind using explicit loops. Python ofers alternative apporaches, specifying programming technqiues such as *functional programming* (expression-oriented programming).
# 
# The tools that Python provides to develop functional programming comprise a series of functions:
# 
# * map(function, list)
# * filter(function, list)
# * reduce(function, list)
# * lambda
# * list comprehension
# 
# The *for* loop that you have just seen has a specific purpose, which is to apply an operation on each item and then somehow gather the result. This can be done by the *map()* function.

# In[20]:


items = [1, 2, 3, 4]
def inc(x): 
    return x + 1


# In[21]:


[*map(inc, items)]


# In the previous example, it first defined the function that performs the operation on every single element, and then it passes it as the first argument to *map()*. Python allows you to define the function directly within the first argument uisng *lambda* as a function. This greatly reduces the code and compacts the previous construct into a single line of code.

# In[22]:


[*map((lambda x: x + 1), items)]


# Two other functions working in a similar way are *filter()* and *reduce()*. The *filter()* function extracts the elements of the list for which the function returns *True*. The *reduce()* function instead considers all the elements of the list to produce a single result. To use *reduce()*, you must import the module *functools*.

# In[23]:


[*filter((lambda x: x < 4), items)]


# In[24]:


from functools import reduce
reduce((lambda x,y: x/y), items)


# Both of these functions implement other types by using the *for* loop. They replace those cycles and their functionaly, which can be alternatively extressed with simple functions. That is what constitutes *functional programming*.
# 
# The final concept of *functional programming* is *list comprehension*. This concept is used to build lists in a very natural and simple way, referring to them in a manner similar to how mathematicians describe datasets. The values in a sequence are defined through a particular function or operation.

# In[25]:


S = [x**2 for x in range(5)]
S


# ### Indentation
# Writing Python Code > Indentation<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# A peculiarity for those coming from other programming languages is the role that *indentation* plays. Whereas you used to manage indentation for purely aesthetic reasons, making the code somewhat more readable, in Python identation assumes an integral role in the implementation of the code, by dividing it into logical blocks. In fact, while in Java, C, and C++, each line of code is separated from the next by a semicolon (;) , in Python you should not specify any symbol that separates them, included the braces to indicate a logical block.
# 
# These roles in Python are handled through indentation; that is, depending on the starting point of the code line, the interpreter determines whether it belongs to a logical block or not.

# In[26]:


a = 4
if a > 3:
    if a < 5:
        print("I'm four")
else:
    print("I'm a little number")


# In[27]:


if a > 3:
    if a < 5:
        print("I'm four")
    else:
        print("I'm a big number")


# In this example you can see that depending on how the *else* command is indented, the conditions assume two different meanings (specified by me in the strings themselves).
# 
# ## IPython
# IPython<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# IPython is a further development of Python that includes a number of tools:
# 
# * The IPython shell, which is a powerful interactive shell resulting in a greatly enhanced Python terminal.
# * A QtConsole, which is a hybrid between a shell and a GUI, allowing you to display graphics inside the console instead of in a separate window.
# * The IPython Notebook, which is a web interface that allows you to mix text, executable code, graphics, and formulas in a single representation.
# 
# ## IPython Shell
# IPython > IPython Shell<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# This shell apparently resembles a Python session run from a command line , but actually, it provides many other features that make this shell much more powerful and versatile than the classic one. To launch this shell, just type *ipython* on the command line.
# 
# <img src="Figures/2_5.jpg" alt="IPython" width="900" height="900"> 
# 
# As you can see, a particular prompt appears with the value *In\[1\]*. This means that it is the first line of input. Indeed, IPython offers a system of numbered prompts (indexed) with input and output caching.
# 
# <img src="Figures/2_6.jpg" alt="IPython Run" width="900" height="900">
# 
# The same thing applies to values in output that are indicated with the values *Out\[1\]*, *Out\[2\]*, and so on. IPython saves all inputs that you enter by storing them as variables. In fact, all the inuts entered were included as fields in a list called *In*.
# 
# <img src="Figures/2_7.jpg" alt="In List" width="900" height="900">
# 
# The indices of the list elements are the values that appear in each prompt. Thus, to access a single line of input, you can simply specify the value.
# 
# <img src="Figures/2_8.jpg" alt="In Element" width="900" height="900">
# 
# For output, you can apply the same concept.
# 
# <img src="Figures/2_9.jpg" alt="Out List" width="900" height="900">
# 
# ## The Jupyter Project
# The Jupyter Project<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ### Jupyter QtConsole
# The Jupyter Project > Jupyter QtConsole<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ### Jupyter Notebook
# The Jupyter Project > Jupyter Notebook<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ## PyPI-The Python Package Index
# PyPI-The Python Package Index<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# The Python Package Index (PyPI) is a software repository that contains all the software needed for programming in Python, for example, all Python packages belonging to other Python libraries. The content repository is managed directly by the developers of individual packages that deal with updating the respository with the latest versions of their released libraries. For a list of the packages contained in the repository, go to the official page of PyPI at https://pypi.python.org/pypi
# 
# As far as the administration of these packages, you can use the pip application, which is the package manager of PyPI.
# 
# By launching it from the command line, you can manage all the packages and individually decide if a package should be installed, upgraded, or removed. Pip will check if the package is already installed, or if it needs to be updated, to control dependencies, and to assess whether other packages are necessary. Furthemore, it manages the downloading and installation processes.
# 
# *\$pip install <<package\_name>>*   
# 
# *\$pip search <<package\_name>>*   
# 
# *\$pip show <<package\_name>>*   
# 
# *\$pip uninstall <<package\_name>>*   
# 
# Regarding the installation, if you have Python 3.4+ (released March 2014) and Python 2.7.9+ (released December 2014) already installed on your system, the pip software is already included in these releases of Python. However, if you are still using an older version of Python, you need to install pip on your system. The installation of pip on your system depends on the operating system on which you are working.
# 
# On Linux Debian-Ubuntu, use this command
# 
# *\$sudo apt-get install python-pip*
# 
# On Linux Fedora, use this command:
# 
# *\$sudo yum install python-pip*
# 
# On Windows, visit https://pip.pypa.io/en/latest/installation/ and download *get-pip.py* onto your PC. Once the file is downloaded, runthis command
# 
# *python get-pip.py*
# 
# This way, you will install the package manager. Remember to add *C:\Python3.X\Scripts* to the **PATH environment variable**. 
# 
# ## The IDEs for Python
# The IDEs for Python<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ### Spyder
# The IDEs for Python > Spyder<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ### Eclipse (pyDev)
# The IDEs for Python > Eclipse (PyDev)<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ### Sublime
# The IDEs for Python > Sublime<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ### Liclipse
# The IDEs for Python > Liclipse<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ### NinjaIDE
# The IDEs for Python > NinjaIDE<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ### Komodo IDE
# The IDEs for Python > Komodo IDE<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ## SciPy
# SciPy<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ### NumPy
# SciPy > NumPy<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ### Pandas
# SciPy > Pandas<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ### Matplotlib
# SciPy > Matplotlib<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
# 
# ## Conclusions
# Conclusions<br/>
# Nelli, F. "Python Data Analytics: With Pandas." NumPy, and Matplotlib, Rome, Italy: Apress Media LLC (2018).
