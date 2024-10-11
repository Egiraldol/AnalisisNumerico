import pandas as pd
import numpy as np
import math

# Entrada de datos
Xi = float(input("xi (a): "))
Xs = float(input("xs (b): "))
Tol = float(input("tol: "))
Niter = int(input("niter: "))
Fun = input("function: ")

# Listas para almacenar los valores de la función y los errores
iteraciones = []
xi_list = []
f_xi_list = []
error_list = []
error_relativo_list=[]

# Evaluación inicial
x = Xi
fi = eval(Fun)
x = Xs
fs = eval(Fun)

# Tolerancia mínima para evitar división por cero
epsilon = 1e-10

# Comprobación inicial de raíces en los extremos
if fi == 0:
    print(Xi, "es raíz de f(x)")
elif fs == 0:
    print(Xs, "es raíz de f(x)")
else:
    c = 0
    # Primera aproximación por método de la secante
    Xm = Xi - (fi * (Xs - Xi)) / (fs - fi)
    
    x = Xm
    fe = eval(Fun)

    # Almacenamos la primera iteración
    iteraciones.append(c)
    xi_list.append(Xm)
    f_xi_list.append(fe)
    error_list.append(100)  # Primer error inicial grande

    # Iteración hasta que el error sea menor que la tolerancia o se alcance la raíz exacta
    while error_list[c] > Tol and fe != 0 and c < Niter:
        Xi_old = Xi  # Guardar el valor anterior
        Xi = Xs  # Actualizamos Xi a Xs
        Xs = Xm  # Actualizamos Xs al nuevo Xm
        fi = fs
        fs = fe

        # Verificación de división por cero
        Xm = Xi - (fi * (Xs - Xi)) / (fs - fi)
        
        x = Xm
        fe = eval(Fun)

        # Cálculo del error
        Error = abs(Xm - Xs)/Xm

        # Almacenamos los resultados de cada iteración
        c += 1
        iteraciones.append(c)
        xi_list.append(Xm)
        f_xi_list.append(fe)
        error_list.append(Error)

    # Verificación de la raíz o aproximación
    if fe == 0:
        print(Xm, "es raíz de f(x)")
    elif Error < Tol:
        print(Xm, "es una aproximación de una raíz de f(x) con una tolerancia", Tol)
    else:
        print("Fracaso en", Niter, "iteraciones")

    # Crear la tabla de resultados
    resultados = pd.DataFrame({
        'Iteración': iteraciones,
        'xi': xi_list,
        'f(xi)': f_xi_list,
        'E (relativo)': error_list
    })

    # Mostrar la tabla
    print(resultados)
