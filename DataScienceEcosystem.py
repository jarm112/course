#!/usr/bin/env python
# coding: utf-8

# # Data Science Tools and Ecosystem

# In this notebook, Data science and Ecosystems are summarized

# **Objectives:** 
# 
# - Learn the most popular languages for data science 
# - Learn about the different libraries 
# - Learn about databases

# ## Author
# 
# John Rincon

# In[1]:


# Some of the popular languages that Data Scientist use are
data_science_languages = ["Python", "R", "SQL", "Java"]

# Printing each language with a number
for index, language in enumerate(data_science_languages, start=1):
    print(f"{index}. {language}")


# Some of the commonly used libraries used by Data Scientist include:

# In[5]:


data_science_library = ["Panda", "Numpy", "ggplot"]

# Printing each library with a number
for index, library in enumerate(data_science_libraries, start=1):
    print(f"{index}. {library}")


# | Data Science Tools |
# |--------------------|
# | Jupyter Notebook   |
# | RStudio            |
# | Apache Zeppelin    |
# 

# ### Below are a few examples of evaluating arithmetic expressions in Python

# In[7]:


# This is a simple arithmetic expression to multiply then add integers

A=(3*4)+5
print(A)


# In[8]:


# This will convert 200 minutes to hours by dividind by 60

B=200/60
print(B)

