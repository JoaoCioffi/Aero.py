import numpy as npy

def trapezio(f,x):
    n = len(f)
    soma = 0.0
    for i in range(n-1):
        soma = soma + (f[i+1]+f[i])/2*(x[i+1]-x[i])
        print(i,soma)
    return soma
