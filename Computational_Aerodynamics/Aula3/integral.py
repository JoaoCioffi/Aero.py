import matplotlib.pyplot as plt
import numpy as npy
import funcao as fn

n = 100
L = 8.0

x = npy.linspace(0,L,n)

print(x)

f = x**2/4 + npy.cos(2*npy.pi*x)
intf = L**3/12 - npy.sin(2*npy.pi*L)/2*npy.pi+ npy.sin(0)


soma = fn.trapezio(f,x)

plt.plot(x,f)
plt.show()

print(soma,intf)