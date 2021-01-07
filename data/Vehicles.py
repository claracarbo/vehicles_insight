#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


vehicles = pd.read_csv("~/Desktop/Data/Pandas/vehicles.csv")


# In[4]:


def shape(x):
    print(x.shape)


# In[5]:


shape(vehicles)


# In[ ]:




