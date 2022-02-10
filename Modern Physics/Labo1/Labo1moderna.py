#!/usr/bin/env python
# coding: utf-8

# # <font color='DodgerBlue'>Laboratorio 1 de fisica moderna</font> 
# ###  <font color ='gray'> Este programa busca cuantizar los resultados de los datos obtenidos en el laboratorio en relacion a las corrientes y los voltajes para analizar las relaciones fisicas existentes y estudiar si los resultados concuerdan con los predichos por la teoria </font>

# __________________________________________

# <font color ='gray'>Se importan las librerias de numpy para realizar operaciones matematicas avanzadas, scypy.optimize para realizar las aproximaciones cuadraticas, seaborn para graficar los residuales y matplotlib para realizar las graficas.</font>

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.optimize import curve_fit


#  <font color ='gray'> se importan las librerias con los metodos de regresion por minimos cuadrados ordinarios, ecuacion cuadratica, .... </font>

# In[2]:


import sys
sys.path.append('/home/ramsus/Programming/NicolasPersonal/University/Herramientas')

import MinimosCuadradosOrdinarios as mc
import MetodosBasicos as mb
import DatosLabo1 as dl1


# <font color ='gray'> Se importan las listas con los datos dados por las guias, los tomados en el experimento y las variables derivadas directamente de los mismos</font>

# In[3]:


#Se importan las Resistividades calculadas
R1, R2, R3, R4, R5 = dl1.R1, dl1.R2, dl1.R3, dl1.R4, dl1.R5

#Se importan las Corrientes obtenidas experimentalmente
I1, I2, I3, I4, I5 = dl1.I1, dl1.I2, dl1.I3, dl1.I4, dl1.I5

#Se importan los Voltajes obtenidos experimentalmente
V1, V2, V3, V4, V5 = dl1.V1, dl1.V2, dl1.V3, dl1.V4, dl1.V5

#Se importan los valores de temperatura y resistencia dados por la guia
t, r = dl1.t , dl1.r


# Metodos para graficar los datos y aproximarlos a una regresion lineal minimizando el error cuadratico, definir el residual y graficarlo junto con una aproximacion cuadratica

# In[4]:


#Recibe como parametros 2 arrays (a,b) que van a ser ajustados con el metodo de los minimos cuadrados, los 2
# valores de la posicion de la grafica en un subplot arbitrario (n1, n2), el tipo de subplot al que se va a 
# agregar (tipoSP) y finalmente el voltaje que reprenta la grafica (voltios)
def graf(c,d, n1, n2, tipoSP, voltios):
    B = mc.MinCua(c,d)
    b = B[0]
    m = B[1]
    i1 = B[2]
    T = B[3]
    v1 = B[4]

    if tipoSP == True:
        axs[n1,n2].scatter(i1,v1, alpha = 0.7)
        axs[n1,n2].plot([min(i1), max(i1)] , [m*min(i1) + b, m*max(i1) + b], c = "orange" )
        axs[n1,n2].set_xlabel("corriente(Amperios)")
        axs[n1,n2].set_ylabel("Voltaje (V)")
        axs[n1,n2].set_title('Corriente VS Voltaje'+ voltios)

    elif tipoSP == 2:
        axs[n1].scatter(i1,v1, alpha = 0.7)
        axs[n1].plot([min(i1), max(i1)] , [m*min(i1) + b, m*max(i1) + b], c = "orange" )
    elif tipoSP == 3:
        plt.scatter(i1,v1, alpha = 0.7)
        plt.plot([min(i1), max(i1)] , [m*min(i1) + b, m*max(i1) + b], c = "orange" )
        
    else:
        return B
    

    
# retorna la grafica del residual del ajuste de la grafica
def res(teo, var ,B, ax):
    ex = B[0] + B[1]*var
    sns.residplot(teo, ex, lowess=True, color="g", ax = ax )
    ax.set_title('Residual')
    
#Realiza un ajuste cuadratico de los datos y grafica el residual
def ajuCua(i, v, nom):
    # Ajuste de los datos
    # curve_fit devuelve dos variables, los parámetros del ajuste y la matriz de covarianza
    popt, bas = curve_fit(mb.Cuadratica, i, v)

    # Ahora creo una curva teórica a partir del modelo ajustado
    times = np.arange(i[0], i[-1], 0.0001)
    model = mb.Cuadratica(times, *popt)

    axs[0].scatter(i, v)
    axs[0].plot(times, model, '-r')

    
    ex = popt[2] + (popt[1]*i)+(popt[0]*(i**2))
    sns.residplot(v, ex, lowess=True, color="g", ax = axs[1] )
    axs[1].set_title('Residual')
    

    
    print('El R es: '+ str(popt[1]))
    


# In[5]:


fig, axs = plt.subplots(1,2, figsize =  (18,5))
graf(t,r,0,0, 2, "")

mb.Nombrar("corriente(Amperios)", "Voltaje (V)", 'Corriente VS Voltaje', 1, 0, 0, axs)

res(r,t, graf(t,r,0,0, -1, ''), axs[1] )


# In[20]:


popt, bas = curve_fit(mb.Cuadratica, t, r)

# Ahora creo una curva teórica a partir del modelo ajustado 295,79 g = 76.95
times = np.arange(t[0], t[-1], 0.01)
model = mb.Cuadratica(times, *popt)

#fig, axs = plt.subplots(1,, figsize =  (18,5))


plt.scatter(t, r)
plt.plot(times, model, '-r')
plt.xlabel("Temperatura(K)")
plt.ylabel("Resistividad ($\mu \Omega$)")
plt.title('Resistividad VS Temperatura')
# Guardo la grafica
plt.savefig("RvsT.png")
    
print('El R en 295,79 K es: '+ str(popt[2] + (popt[1]*295.79)+(popt[0]*(295.79**2))))
# Para mostrar la gráfica por pantalla

graf(t,r,0,0, 3, "")
plt.show()

#mb.Nombrar("Temperatura(K)", "Resistividad ($\mu \Omega$)", 'Resistividad VS Temperatura', 1, 0, 0, )


# In[7]:


popt, bas = curve_fit(mb.Cuadratica, r, t)

# Ahora creo una curva teórica a partir del modelo ajustado 295,79 g = 76.95
times = np.arange(r[0], r[-1], 0.001)
model = mb.Cuadratica(times, *popt)
plt.scatter(r, t)
plt.plot(times, model, '-r')
plt.ylabel("Temperatura(K)")
plt.xlabel("Resistividad ($\mu \Omega$")
plt.title(' Temperatura VS Resistividad')
# Guardo la grafica
plt.savefig("TvsR.png")


a = R5
print(str(popt[2] + (popt[1]*a)+(popt[0]*(a**2)))+ "\\")

# Para mostrar la gráfica por pantalla


# In[8]:


fig, axs = plt.subplots(2,5, figsize =  (18,10))
graf(I1,V1, 0, 0, True, '(Fuente 3V)')
graf(I2,V2, 0, 1, True, '(Fuente 9V)')
graf(I3,V3,0,2, True, '(Fuente 24V)')
graf(I4,V4,0,3, True, '(Fuente 54V)')
graf(I5,V5,0,4, True, '(Fuente 115V)')

res(V1,I1, graf(V1,I1,0,0, -1, ''), axs[1,0] )
res(V2,I2, graf(V2,I2,0,1, -1, ''), axs[1,1] )
res(V3,I3, graf(V3,I3,0,2, -1, ''), axs[1,2] )
res(V4,I4, graf(V4,I4,0,3, -1, ''), axs[1,3] )
res(V5,I5, graf(V5,I5,0,4, -1, ''), axs[1,4] )


# In[9]:


fig, axs = plt.subplots(1,2, figsize =  (18,5))
ajuCua(I1*(1/1000), V1, '003V')

axs[0].set_xlabel("corriente(Amperios)")
axs[0].set_ylabel("Voltaje (V)")
axs[0].set_title('Corriente VS Voltaje '+ '003V')
     # Se guarda la grafica
plt.savefig("ajuste"+'003V'+".png")
plt.show()


fig, axs = plt.subplots(1,2, figsize =  (18,5))
ajuCua(I2*(1/1000), V2, '009V')

axs[0].set_xlabel("corriente(Amperios)")
axs[0].set_ylabel("Voltaje (V)")
axs[0].set_title('Corriente VS Voltaje '+ '009V')
     # Se guarda la grafica
plt.savefig("ajuste"+'009V'+".png")
plt.show()


fig, axs = plt.subplots(1,2, figsize =  (18,5))
ajuCua(I3*(1/1000), V3, '024V')
axs[0].set_xlabel("corriente(Amperios)")
axs[0].set_ylabel("Voltaje (V)")
axs[0].set_title('Corriente VS Voltaje '+ '009V')
     # Se guarda la grafica
plt.savefig("ajuste"+'009V'+".png")
plt.show()


fig, axs = plt.subplots(1,2, figsize =  (18,5))
ajuCua(I4*(1/1000), V4, '054')
axs[0].set_xlabel("corriente(Amperios)")
axs[0].set_ylabel("Voltaje (V)")
axs[0].set_title('Corriente VS Voltaje '+ '054')
     # Se guarda la grafica
plt.savefig("ajuste"+'054'+".png")
plt.show()


fig, axs = plt.subplots(1,2, figsize =  (18,5))
ajuCua(I5*(1/1000), V5, '115')
axs[0].set_xlabel("corriente(Amperios)")
axs[0].set_ylabel("Voltaje (V)")
axs[0].set_title('Corriente VS Voltaje '+ '115')
     # Se guarda la grafica
plt.savefig("ajuste"+'115'+".png")
plt.show()


# .

# In[10]:


def gra3 (I, V, vol):
    i = np.array(I*1/1000)
    #print(len(i1), V1.size())
    plt.scatter(i,V , alpha = 0.4, label =vol)
    plt.xlabel("Corriente (A)")
    plt.ylabel("Voltaje (V)")


# In[11]:


gra3(I1, V1, '003V')
gra3(I2, V2, '009V')
gra3(I3, V3, '024V')
gra3(I4, V4, '054V')
gra3(I5, V5, '115V')
plt.legend()
plt.savefig('er4.png')

