import numpy as np
import math

def multiple_roots_function(funct, first_derivate, second_derivate, x0, tol=1e-7, max_count=100):
    # Inicializar las variables de resultados
    results = {
        'iterations': [],
        'conclusion': None
    }

    if max_count < 0:
        raise ValueError(f"Max iterations is < 0: iterations = {max_count}")
    
    if tol < 0:
        raise ValueError(f"tol is an incorrect value: tol = {tol}")
    
    err = tol + 1
    cont = 0

    # Funciones que evaluan la función, derivada y segunda derivada en cada punto
    x=x0
    f_x0 = eval(funct)
    f_xp = eval(first_derivate)
    f_xs = eval(second_derivate)

    # Almacenar la primera iteración
    results['iterations'].append([cont, round(x0, 10), "{:.2e}".format(f_x0), ""])
    
    while err > tol and cont < max_count:
        # Calcular d para verificar la división por cero
        f_xp2 = f_xp**2
        d = f_xp2 - f_x0 * f_xs
        
        if d == 0:
            results['conclusion'] = "The method exploded due to division by zero"
            return results
        
        # Calcular el nuevo x usando el método de la raíz múltiple
        try:
            x_ev = x0 - (f_x0 * f_xp) / d
        except ZeroDivisionError:
            raise ValueError(f"Infinity value in step {cont}")
        
        # Evaluar nuevas funciones
        x=x_ev
        f_x0 = eval(funct)
        f_xp = eval(first_derivate)
        f_xs = eval(second_derivate)
        
        # Calcular error
        err = abs(x_ev - x0)
        cont += 1
        
        # Actualizar x0 para la siguiente iteración
        x0 = x_ev
        
        # Almacenar resultados de iteraciones
        results['iterations'].append([cont, round(x0, 10), "{:.2e}".format(f_x0), "{:.2e}".format(err)])
    
    # Conclusión final
    if f_x0 == 0:
        results['conclusion'] = f"The root was found for x = {x0:.15f}"
    elif err <= tol:
        results['conclusion'] = f"An approximation of the root was found for x = {x0:.15f}"
    else:
        results['conclusion'] = "Given the number of iterations and the tolerance, it was impossible to find a satisfying root"
    
    return results

# Ejemplo de uso:
funct = 'np.exp(x)-x-1'
first_derivate = 'math.exp(x)-1'
second_derivate = 'math.exp(x)'
x0 = 1
tol = 1e-7
max_count = 100

results = multiple_roots_function(funct, first_derivate, second_derivate, x0, tol, max_count)

# Imprimir resultados
for iteration in results['iterations']:
    print(f"Iteration: {iteration[0]}, x: {iteration[1]}, f(x): {iteration[2]}, Error: {iteration[3]}")

print(results['conclusion'])
