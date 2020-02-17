#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


distancia = 93.6
centro = 50.5
H = np.array([74.4, 81.9, 86.3]) -centro
Hg = np.array([71.5, 74.7, 79.3, 81.7 ]) -centro
Ne = np.array([82.4, 83.4, 85.4]) -centro
Kr = np.array([73.5, 80.4, 82.2]) - centro


# Longitudes de onda

# In[3]:


Hl = np.array([486.3, 574, 656.5])
Hgl = np.array([ 435.8, 502.5, 546.1, 578 ])
Nel = np.array([  587.2, 607.4, 630 ])
Krl = np.array([ 400, 560, 590 ])
