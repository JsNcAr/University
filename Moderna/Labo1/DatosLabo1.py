#!/usr/bin/env python
# coding: utf-8

# # <font color='DodgerBlue'>Datos laboratorio 1 de fisica moderna</font> 

# __________________

# In[1]:


import numpy as np


# ###  <font color ='gray'> Aqui se almacenan las listas con con los datos de dados por las guias, los tomados en el experimento y las variables derivadas directamente de los mismos </font>

# In[2]:


R1 =np.array([7.157629234,7.027521578,7.233319545,7.271859649,7.359659091,7.415839695,7.559600683,7.733134328,
7.879421365,7.811351145,7.896648193,8.081038288,8.217494624,8.287934866,8.367003766,8.44049278,
8.591939698,8.941874622,9.33248711,10.07118501,10.78731323])

R2 = np.array([7.756287425,8.088554585,8.361451493,8.756389408,9.280571229,10.20778441,11.35640755,12.12115596,
12.35851103,12.76701943,13.37016586,14.43009649,15.5806567,15.83700129,16.89187908,17.48836415,17.84697524,
18.96713392,19.57255522,20.91493578,22.49161088])

R3= np.array([9.922954856,11.49973659,12.89925311,16.38388228,17.74185969,19.52521182,20.48381395,21.53225974,
22.58876829,24.02104851,25.31927875,27.55606369,27.47258702,28.66775075,28.82134758,28.98830028,29.87263686,
31.00062468,31.61780482,33.34143508,35.85500638])

R4 = np.array([14.59629104,21.80975214,23.37611719,26.54303279,28.33959394,29.34549718,31.97670426,33.65386836,
               35.62075,37.99216444,39.0450395,40.49723777,40.6833662,44.05910949,45.78655716,46.37071334,
                48.43434194,48.85648428,50.21687571,51.8677718,54.3273974])

R5 = np.array([20.06802817,23.90553668,27.39902492,29.40583565,30.58253766,33.63133184,35.09135456,38.16721915,
38.99704263,40.85341887,41.53184127,43.11307806,43.90538678,46.8512766,46.71030691,48.37677616,49.79608595,
50.46242356,51.812,53.34364934,54.79119])

t = np.linspace( 300, 3600, num = 34 )
r = np.array([5.65, 8.06, 10.56,13.23,16.09,19.00,21.94,24.93,27.94,30.98,34.08,37.19,
    40.36,43.55,46.78,50.05,53.35,56.67,60.06,63.48,66.91,70.39,73.91,77.49,
    81.04,84.70,88.33,92.04,95.76,99.54,103.3,107.2,111.1,115.0])

I1 = np.array([0.561,0.811,0.967,1.14,1.672,1.834,2.93,3.35,3.37,3.93,
    4.15,4.44,4.65,5.22,5.31,5.54,5.97,6.62,7.37,8.54,9.45])
V1 = np.array([0.031,0.044,0.054,0.064,0.095,0.105,0.171,0.2,0.205,0.237,0.253
     ,0.277,0.295,0.334,0.343,0.361,0.396,0.457,0.531,0.664,0.787])

I2 = np.array([3.34,4.58,5.36,6.42,7.16,8.21,10.06,10.9,11.33,11.84,12.42,13.68,
      15.38,15.54,16.87,17.85,18.58,19.19,19.92,21.8,23.9])
V2 = np.array([0.2,0.286,0.346,0.434,0.513,0.647,0.882,1.02,1.081,1.167,1.282,
      1.524,1.85,1.9,2.2,2.41,2.56,2.81,3.01,3.52,4.15])

I3 = np.array([0.56,0.91,1.2,2.02,2.46,3.06,3.4,3.84,4.29,4.97,5.61,6.68,7.19,
               7.37,7.81,7.9,8.51,9.31,10.13,11.3,13.01])
V3 = np.array([ 7.31, 10.25, 12.05, 15.97, 17.96, 20.3 , 21.5 , 23.1 , 24.6 ,26.8 , 28.7 
      , 31.4 , 33.9 , 33.3 , 35.1 , 35.3 , 36.9 , 38.9 ,41.5 , 43.9 , 47.0 ])


I4 = np.array([13.4,23.4,25.6,30.5,33,35.4,39.9,43.3,48.8,52.3,55.7,59.3,63.9,
      68.5,76.1,75.7,81.3,85.9,87.7,92.9,99.9])
V4 = np.array([1.51,3.94,4.62,6.25,7.22,8.02,9.85,11.25,13.42,15.34,16.79,18.54,
      20.07,23.3,26.9,27.1,30.4,32.4,34,37.2,41.9])

I5 = np.array([21.3,25.9,32.1,35.9,38.5,44.6,47.1,54.3,56.3,60.4,63,67.9,
      71.1,75.2,78.2,82.2,86.1,88.3,93.5,98.4,100.1])
V5 = np.array([3.3,4.78,6.79,8.15,9.09,11.58,12.76,16,16.95,19.05,20.2,22.6,24.1,27.2,28.2,
      30.7,33.1,34.4,37.4,40.4,42.3])

