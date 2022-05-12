# importando os modulos
import numpy as npy
import matplotlib.pyplot as plt 
import leitura as ld


A = 1.0
rho_ref = 4.41727565e-07
u_ref = 10416.70117188
qref = 0.5*rho_ref*u_ref**2

# leitura 
x = ld.linhas('coordenada_x.dat',1)
y = ld.linhas('coordenada_y.dat',1)
p = ld.linhas('pressao.dat',1)


# ctrl + / comenta e descomenta
x = ld.periodic(x)
y = ld.periodic(y)
p = ld.periodic(p)


n =len(x)

ds = npy.zeros((n))
nx = npy.zeros((n))
ny = npy.zeros((n))

for i in range(n-1):
	ds[i] = npy.sqrt((x[i+1]-x[i])**2+(y[i+1]-y[i])**2)
	nx[i] = (y[i+1]-y[i])/ds[i]
	ny[i] = -(x[i+1]-x[i])/ds[i]

nx[n-1] = nx[0]
ny[n-1] = ny[0]
ds[n-1] = ds[0]


plt.plot(x,y)
plt.plot(x,y,'o')
plt.quiver(x,y,nx,ny)     # plot dos vetores normais
plt.show()

plt.plot(nx)
plt.plot(ny)
plt.plot(nx**2+ny**2)
plt.show()


Fx = 0.0
Fy = 0.0
for i in range(n-1):
	Fx = Fx - (p[i+1]+p[i])/2*nx[i]*ds[i] 
	Fy = Fy - (p[i+1]+p[i])/2*ny[i]*ds[i] 

Cd = Fx/(qref*A)
Cl = Fy/(qref*A)

print(Cd,Cl)
