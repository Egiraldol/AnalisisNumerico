import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def gauss_seidel(A, b, x0, tol, niter):
    """
    Método de Gauss-Seidel para resolver sistemas de ecuaciones lineales A * x = b.
    
    :param A: Matriz de coeficientes (numpy array de tamaño n x n).
    :param b: Vector de términos independientes (numpy array de tamaño n).
    :param x0: Vector inicial de valores de las incógnitas (numpy array de tamaño n).
    :param tol: Tolerancia para el criterio de convergencia.
    :param niter: Número máximo de iteraciones.
    :return: Un DataFrame con la tabla de iteraciones, errores, radio espectral, convergencia.
    """
    # Dimensiones de la matriz A
    n = A.shape[0]
    x = np.copy(x0)
    errors = []
    iter_data = []  # Para almacenar cada iteración

    # Calcular el radio espectral (valor absoluto del mayor autovalor de la matriz iterativa)
    D = np.diag(np.diag(A))
    L = np.tril(A, -1)
    U = np.triu(A, 1)
    T = np.linalg.inv(D - L) @ U  # Matriz iterativa para Gauss-Seidel
    spectral_radius = max(abs(np.linalg.eigvals(T)))

    # Determinar si el método puede converger basado en el radio espectral
    converge = spectral_radius < 1

    for k in range(niter):
        x_old = np.copy(x)

        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i + 1:], x_old[i + 1:])
            x[i] = (b[i] - sum1 - sum2) / A[i, i]
        
        # Calcular error relativo
        error = np.linalg.norm(x - x_old, ord=np.inf) / np.linalg.norm(x, ord=np.inf)
        errors.append(error)

        # Agregar datos de la iteración a la tabla
        iter_data.append([k + 1] + list(x) + [error])

        # Verificar convergencia
        if error < tol:
            break

    # Convertir la tabla de iteraciones a un DataFrame
    column_names = ['Iteración'] + [f'x{i+1}' for i in range(n)] + ['Error']
    df_iter = pd.DataFrame(iter_data, columns=column_names)

    return df_iter, spectral_radius, converge, x, errors
