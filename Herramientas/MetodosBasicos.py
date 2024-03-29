# -   Cuadratica (x,a,b,c): dados los parametros retorna una funcion cuadratica
# -   Nombrar (x_label, y_label, title, dimension, p1, p2, axs): da nombres dados por parametro a una grafica
# -   ajuCua(x, y): grafica ajuste cuadratico a una grafica
# -   puntosCriticos(r1, r2, lis): Devuelve una lista con los puntos criticos de un Dataframe

from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def Cuadratica(x, a, b, c):
    return (a*(x**2)) + b*x + c


def Nombrar(x_label, y_label, title, dimension, p1, p2, axs):

    if dimension == 0:
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
    elif dimension == 1:

        axs[p1].set_xlabel(x_label)
        axs[p1].set_ylabel(y_label)
        axs[p1].set_title(title)
    else:
        axs[p1, p2].set_xlabel(x_label)
        axs[p1, p2].set_ylabel(y_label)
        axs[p1, p2].set_title(title)


def ajuCua(x, y, c, lab):
    # Ajuste de los datos
    # curve_fit devuelve dos variables, los parámetros del ajuste y la matriz de covarianza
    popt, bas = curve_fit(Cuadratica, x, y)

    # Ahora creo una curva teórica a partir del modelo ajustado
    times = np.arange(x[0], x[-1], 0.0001)
    model = Cuadratica(times, *popt)

    plt.scatter(x, y)
    plt.plot(times, model, '-r', color=c, label=lab)


def ajuCuaEcu(x, y):
    # Ajuste de los datos
    # curve_fit devuelve dos variables, los parámetros del ajuste y la matriz de covarianza
    popt, bas = curve_fit(Cuadratica, x, y)

    return popt


def puntosCriticos(r1, r2, lis):
    criticos = []
    for var in range(r1, r2):
        if float(lis.iloc[var-1]) < float(lis.iloc[var]) and (float(lis.iloc[var+1]) <
                                                              float(lis.iloc[var])):
            criticos.append(var)

    return(criticos)
