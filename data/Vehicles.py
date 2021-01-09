#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


vehicles = pd.read_csv("../data/vehicles.csv")


# In[6]:


def shape(x):
    print("The shape of the dataframe is", x.shape)


# In[7]:


shape(vehicles)


# In[8]:


def rows(x):
    print("It has a total of", len(x), "rows")


# In[9]:


rows(vehicles)


# In[10]:


def columns(x):
    print("It has a total of", len(x.columns), "columns")


# In[11]:


columns(vehicles)


# In[54]:


def column_names(x):
    print("Columns are:",list(x.columns))


# In[52]:


column_names(vehicles)


# In[91]:


def min_value(x):
    print(x.min(axis=None, skipna=None, level=None, numeric_only=True))


# In[92]:


min_value(vehicles)


# In[90]:


def max_value(x):
    print(x.max(axis=None, skipna=None, level=None, numeric_only=True))


# In[93]:


max_value(vehicles)


# In[ ]:




