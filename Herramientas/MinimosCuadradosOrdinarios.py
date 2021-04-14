#!/usr/bin/env python
# coding: utf-8

# # <font color = 'DodgerBlue'> Metodo para calcular minimos cuadrados ordinarios </font>

# ## <font color = #585858> Este programa contiene metodos que calculan el valor de los parametros optimos para reducir al minimo el error cuadratico en un ajuste lineal de 2 arrays </font>

# _________________

#  <font color ='gray'> se importa numpy para poder trabajar comodamente con matrices para soluciar el problema por el metodo vectorial </font>

# In[1]:


import numpy as np


# #  Formula para hallar $\beta $ que minimiza el error cuadratico medio (MCO)
# $ \beta = (X^{T}X)^{-1} X^{T} Y$

# In[2]:


#El metodo recibe 2 arrays y nos da los parametros para la regresion lineal que minimiza el error cuadratico
def MinCua(a,b):
    
    #Se convierten en arrays de numpy para poder usar los metodos de dicha libreria
    xt = np.array(a)
    Y = np.array(b)

    #se añade columna de unos(1) para representar el termino independiente
    C1 =  np.ones(len(xt))
    
    """" 
    Se transpone X debido a que la matriz de parametros beta resultante, tiene la forma de 1 fila y 2 coumnas
    por tanto no esta en la forma vectorial sino en la vectorial transpuesta 
    """
    
    X = np.array([C1, xt]).T

    # @ = Multiplicacion Matricial
    # X.T = np.transpose(x) = X transpuesta
    B = np.linalg.inv(X.T @ X) @ X.T @ Y

    #Esta operacion nos da como resultado una lista con 2 parametros, el primero representa la variable independiente
    # y el segundo la pendiente optima para minimizar el error cuadratico, esta formula se demostro en algebra lineal
    #b = B[0]
    #m = B[1]
    return [B[0],B[1]]


#  <font color ='gray'> Finalmente el metodo nos retorna un array con 5 parametros, el primero representa el intercepto de la recta solucion, el segundo la pendiente, el tercero es el array dado como parametro 'a' (representando la variable independiente) convertido a numpy, el cuarto es este mismo array pero en forma de matriz con una columna de 1's representando el parametro independiente, y el quinto representa el parametro 'b' (variable dependiente) convertido a numpy  </font>

# In[3]:


def MinCua2(y,x1, dim = 2, x2=[0], x3=[0], x4=[0], x5=[0]):
    
    #Se convierten en arrays de numpy para poder usar los metodos de dicha libreria
    Y = np.array(y)
    x1t = np.array(x1)
    x2t = np.array(x2)
    x3t = np.array(x3)
    x4t = np.array(x4)
    x5t = np.array(x5)

    #se añade columna de unos(1) para representar el termino independiente
    C1 =  np.ones(len(x1t))
    
    """" 
    Se transpone X debido a que la matriz de parametros beta resultante, tiene la forma de 1 fila y 2 coumnas
    por tanto no esta en la forma vectorial sino en la vectorial transpuesta 
    """
    if dim ==1:
        X = np.array([x1t]).T
    elif dim == 2:
        X = np.array([C1, x1t]).T
    elif dim == 3:
        X = np.array([C1, x1t,x2t]).T
    elif dim == 4:
        X = np.array([C1, x1t, x2t, x3t]).T
    elif dim == 5:
        X = np.array([C1, x1t, x2t, x3t, x4t, x5t]).T
    else:
        print("Error: Este metodo solo funciona hasta orden 5")
        return ("Este metodo solo funciona hasta orden 5")

    # @ = Multiplicacion Matricial
    # X.T = np.transpose(x) = X transpuesta
    B = np.linalg.inv(X.T @ X) @ X.T @ Y

    #Esta operacion nos da como resultado una lista con 2 parametros, el primero representa la variable independiente
    # y el segundo la pendiente optima para minimizar el error cuadratico, esta formula se demostro en algebra lineal
    #b = B[0]
    #m_x1 = B[1]
    #m_x2 = B[2] ...
    return [B]

