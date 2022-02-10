#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


E11 = np.array( [0.5, 1, 1.4, 1.74] )
E12 = np.array([0.5, 0.9, 1.3, 1.6])
E13 = np.array([0.5, 0.8, 1.08, 1.33])
E14 = np.array([0.3, 0.4, 0.53, 0.66])
E15 = np.array([0.2, 0.32, 0.47, 0.67, 0.87])

I4 = np.linspace( 1, 4, num = 4 )
I5 = np.linspace( 1, 5, num = 5 )
I3 = np.linspace(1,3, num =3)
T = np.linspace(-1,2, num = 3)
D = np.linspace(-1,1, num = 2)


# In[3]:


E21 = np.array([0.498, 0.618, 0.718])
E22 = np.array([0.45, 0.55, 0.65])
E23 = np.array([0.5, 0.7, 0.9])
E24 = np.array([0.63, 0.83, 1.04])
E25 = np.array([0.87, 1.18, 1.48])
E26 = np.array([1.13, 1.45, 1.74])
E27 = np.array([0.6, 0.4, 0.4])
E28 = np.array([1.25, 1.7, 2.19])
E29 = np.array([1.2, 1.65, 2.05])
E2d = np.array([2.2, 3.15, 4.05])


# In[4]:


E31= np.array([-22, 20, 56])
E32= np.array([-26,24])
E33= np.array([-32, 29])
E34= np.array([-40, 37])
E35= np.array([-45,42])
E36= np.array([-51, 55])
E37= np.array([-63, 61])
E38= np.array([-75, 70])
E39= np.array([-88, 84])
E3d= np.array([-101, 107])

D2 = np.array([0.274, 0.337, 0.377, 0.457, 0.524, 0.581, 0.639, 0.703, 0.80, 2.533])
D3 = np.array([0.52, 0.63, 0.72, 0.8, 1.03, 1.21, 1.35, 1.58, 1.91, 2.25])

