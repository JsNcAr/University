import numpy as np


# #  Formula para hallar $\beta $ que minimiza el error cuadratico medio (MCO)
# $ \beta = (X^{T}X)^{-1} X^{T} Y$

"""" 
Recibe un array Y correspondiente al resultado que queremos modelar, y una lista con
     los arrays representando las variables con las que queremos realizar el ajuste lineal 
"""


def MinCua(y, xn):

    # transforma el parametro y en un array Y en dado caso de que fuera una lista
    Y = np.array(y)
    # Crea una columna de unos para representar el termino independiente y corrimiento del ajuste
    X_0 = np.ones(len(xn[0]))

    # Crea la matriz vacia de parametros XT y le asigna sus valores correspondientes
    # Esta representaria la transpuesta de la matriz X por motivos de optimizacion
    XT = np.empty(shape=(len(xn)+1, len(X_0)))

    XT[0] = X_0
    XT[1:] = xn

    # Aplica formula para encontrar el vector de parametros que minimiza error cuadratico
    B = np.linalg.inv(XT @ XT.T) @ XT @ Y

    return B
