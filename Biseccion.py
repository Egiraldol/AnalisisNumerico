import pandas as pd
import numpy as np
import math
#import wdb
#wdb.set_trace()

print("Xi:")
Xi = float(input())
print("Xs:")
Xs = float(input())
print("Tol:")
Tol = float(input())
print("Niter:")
Niter = float(input())
print("Function:")
Fun = input()

fm = []
E = []
x = Xi
fi = eval(Fun)
x = Xs
fs = eval(Fun)

if fi == 0:
    s = Xi
    E = 0
    print(Xi, "es raíz de f(x)")
elif fs == 0:
    s = Xs
    E = 0
    print(Xs, "es raíz de f(x)")
elif fs * fi < 0:
    c = 0
    Xm = (Xi + Xs) / 2
    x = Xm                 
    fe = eval(Fun)
    fm.append(fe)
    E.append(100)
    
    while E[c] > Tol and fe != 0 and c < Niter:
        if fi * fe < 0:
            Xs = Xm
            x = Xs                 
            fs = eval(Fun)
        else:
            Xi = Xm
            x = Xi
            fi = eval(Fun)
        
        Xa = Xm
        Xm = (Xi + Xs) / 2
        x = Xm 
        fe = eval(Fun)
        fm.append(fe)
        Error = abs(Xm - Xa)
        E.append(Error)
        c = c + 1

    if fe == 0:
        s = x
        print(s, "es raíz de f(x)")
    elif Error < Tol:
        s = x
        print(s, "es una aproximación de una raíz de f(x) con una tolerancia", Tol)
        print("Fm", fm)
        print("Error", E)
    else:
        s = x
        print("Fracaso en", Niter, "iteraciones")

else:
    print("El intervalo es inadecuado")
    