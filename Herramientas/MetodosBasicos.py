#!/usr/bin/env python
# coding: utf-8

# # <font color = 'DodgerBlue'> Metodos basicos para el trabajo en fisica computacional </font>

# ## <font color = #585858> Este programa contiene los siguiente metodos basicos para el analisis fisico:
# 
# -   Cuadratica (x,a,b,c): dados los parametros retorna una funcion cuadratica
# -   Nombrar (x_label, y_label, title, dimension, p1, p2, axs): da nombres dados por parametro a una grafica
# -   
# 
# </font>

# In[1]:


def Cuadratica(x, a, b, c):
   return (a*(x**2))+ b*x + c


# In[2]:


def Nombrar (x_label, y_label, title, dimension, p1, p2, axs):
    if dimension == 1:
        
        axs[p1].set_xlabel(x_label)
        axs[p1].set_ylabel(y_label)
        axs[p1].set_title(title)
    else:
        axs[p1,p2].set_xlabel(x_label)
        axs[p1,p2].set_ylabel(y_label)
        axs[p1,p2].set_title(title)    

