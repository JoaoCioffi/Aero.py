import time
import numpy as np
import matplotlib.pyplot as plt 

#>> Dados de entrada gerais:
pi = np.pi
sin = np.sin
cos = np.cos

tic = time.perf_counter()
#%% Funções:
    
#>> Função derivada:
def derivative(f,a,method,h):
    
    #>> métodos possíveis:
    central = (f(a + h) - f(a - h))/(2*h)
    forward = (f(a + h) - f(a))/h
    backward = (f(a) - f(a - h))/h
    
    if method == 'central':
        return central
    
    elif method == 'forward':
        return forward
    
    elif method == 'backward':
        return backward
    
    else:
        raise Exception


#>> Esquema 01:
def dif1(u0,u1,dx):
    dfdx1 = (u1-u0)/dx
    return dfdx1

#>> Esquema 02:
def dif2(u0,u2,dx):
    dfdx2 = (u2-u0)/(2*dx)
    return dfdx2


#>> Esquema 03:
def dif3(u0,u1,u2,u3,dx):
    dfdx3 = (u0-6*u1+3*u2+2*u3)/(6*dx)
    return dfdx3

#%% Ex 1.

#>> Dados de entrada:
n = int(1e+02)
x = np.linspace(0,2*pi,n)
dx = x[1]-x[0]
f = sin(x)
f_1 = derivative(sin, x, method='central', h=1e-02)


esquema1, esquema2, esquema3 = [], [], []

for g in range(n-1):
    a = dif1(f[g],f[g+1],dx)
    esquema1 = np.append(esquema1,a)

for h in range(n-2):
    b = dif2(f[h],f[h+2],dx)
    esquema2 = np.append(esquema2,b)

for i in range(n-3):
    c = dif3(f[i],f[i+1],f[i+2],f[i+3],dx)
    esquema3 = np.append(esquema3,c)

plt.figure(1)
plt.plot(x,f,'-',label='f(x)',color='blue', linewidth=1)
plt.plot(x,f_1,'-',label='f´(x)',color='red', linewidth=1)
plt.plot(x[0:n-1],esquema1,'--',label='esquema1',color='orange',linewidth=1)
plt.plot(x[0:n-2],esquema2,'--',label='esquema2',color='lime',linewidth=1)
plt.plot(x[0:n-3],esquema3,'--',label='esquema3',color='purple',linewidth=1)
plt.xlabel('x', weight='bold', size=10)
plt.legend()
plt.show()

#%% Ex 2.

A = np.array(([-1.,   -1.,    -1.,    -1. ],
              [0.,    1.,     2.,     3. ],
              [0., -(1/2),  -2.,   -(9/2)],
              [0.,  (1/6), (4/3),   (9/2)]))

B = np.array(([0.],
              [-1.],
              [0.],
              [0.]))

R = np.linalg.solve(A,B)

print(f'\n>> Resposta do Sistema:\na={R[0,0]}\nb={R[1,0]}\
        \nc={R[2,0]}\nd={R[3,0]}')

#%% Ex 3.

Coef = [1,0.5,1/6,1/12]
nn = 10**4
dx = np.linspace(0,1,nn)

Erro1, Erro2, Erro3 = [], [], []

for Coef[0] in dx:
    Erro1.append(Coef[1]*Coef[0])
    Erro2.append(Coef[2]*Coef[0]**2)
    Erro3.append(Coef[3]*Coef[0]**3)

plt.figure(2)
plt.loglog(dx,Erro1,'-',label='Erro 1',color='indigo', linewidth=2)
plt.loglog(dx,Erro2,'--',label='Erro 2',color='slategray', linewidth=2)
plt.loglog(dx,Erro3,'-.',label='Erro 3',color='darkkhaki', linewidth=2)
plt.xlabel('Discretização (Δx)', weight='bold', size=10)
plt.ylabel('Erro (Δy)', weight='bold', size=10)
plt.legend()
plt.show()

#%%
toc = time.perf_counter()
print('\n')
print('-'*30)
print(f'\nElapsed time: {toc-tic}s\n')
del tic,toc

#--------------------------------------------------------------------------End.
