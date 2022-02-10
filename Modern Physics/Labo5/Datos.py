#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


deu = pd.read_csv('deuprueba.csv', index_col= 'px')
h = pd.read_csv('hidro.csv', index_col= 'px')
ne = pd.read_csv('ne.csv', index_col = 'px')
na = pd.read_csv('na.csv', index_col = 'px')
hg = pd.read_csv('hg.csv', index_col = 'px')
cd = 1167 
ch = 1227 
