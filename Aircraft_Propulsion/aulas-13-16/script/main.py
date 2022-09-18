# Main Libraries
from load_dependencies import loadData
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import variables as var
import numpy as npy
import time

startMain = time.time()

#--------------------------------------------------------------#
# Parte 1: leitura dos dados do Xfoil e funções de interpolação
data = loadData()
print(data)

def aerodinamic_coeff(data=data, plot=True):

    # iterpolação das curvas de coeficientes aerodinâmicos
    Cl = interp1d(data['alpha'],data['CL'],kind='cubic')
    CdCl = interp1d(data['alpha'],data['CD']/data['CL'],kind='cubic')

    # plot dos coeficientes
    if plot==True:
        
        plt.subplot(1,2,1)
        plt.plot(data['alpha'],data['CL'])
        plt.xlabel(r'$\alpha$',fontsize=15)
        plt.ylabel(r'$C_L$',fontsize=15)
        plt.grid(True)

        plt.subplot(1,2,2)
        plt.plot(data['alpha'],data['CD'])
        plt.xlabel(r'$\alpha$',fontsize=15)
        plt.ylabel(r'$C_D$',fontsize=15)
        plt.grid(True)
        
        plt.show()
    
    return Cl,CdCl

Cl,CdCl = aerodinamic_coeff()

#-------------------------------#
# Parte 2: Ângulos e velocidades:
"""
obtenção dos ângulos pertinentes
e velocidades ao longo da pá
(a,β,Φ,V_t,V_r)
"""
def blade_analysis(data=data):

    Vt = 2*npy.pi*var.r*var.N/60
    V0 = ((Vt*Vt)+var.V**2)**0.5

    alpha = data['alpha']
    phi = npy.arctan(V0/Vt)
    beta = alpha + phi

    plt.figure()
    plt.plot(var.r,phi)
    plt.xlabel('r/R')
    plt.ylabel('Phi')
    plt.show()

    return alpha,beta,Vt
alpha,beta,Vt = blade_analysis()

#-------------------------------#
# Parte 3: Cálculo de tração e torque:
def thrustTorqueCalculator(alpha=alpha,beta=beta,Vt=Vt):
    alpha_min,alpha_max = min(alpha),max(alpha)
    beta = beta * npy.pi/180

    # velocidade tangencial
    Vt = 2*npy.pi * var.N / 60 * var.r
    
    # velocidade resultante
    Vr = npy.sqrt(Vt**2 + var.V**2)

    Mach = Vr/npy.sqrt(1.4*287*var.Te)

    # angulo de deslizamento
    phi = npy.arctan2(var.V,Vt)
    
    dT = alpha * 0.0
    dQ = alpha * 0.0
    
    for i in range(1,len(alpha) - 1):
     if (alpha[i] < alpha_min or alpha[i] > alpha_max):
       dT[i] = 0.0
       dQ[i] = 0.0
     else:
       gamma = npy.arctan(CdCl(alpha[i]))

       # diferencial de tração
       coef = npy.cos(phi[i] + gamma) / (npy.cos(gamma) * npy.sin(phi[i]) ** 2)
       dT[i] = var.q * Cl(alpha[i]) * var.c[i] * coef

       # diferencial de torque
       coef = npy.sin(phi[i] + gamma) / (npy.cos(gamma) * npy.sin(phi[i]) ** 2)
       dQ[i] = var.q * Cl(alpha[i]) * var.c[i] * var.r[i] * coef
    
    plt.figure()
    plt.plot(var.r,dT,'-x')
    plt.xlabel('r')
    plt.ylabel('dT/dr')
    plt.show()

    T = npy.trapz(dT,var.r) * var.np
    Q = npy.trapz(dQ,var.r) * var.np
    eta = T * var.V / (Q * var.N * 2 * npy.pi/60)

    print(f'Tracao: T={round(T,3)}N')
    print(f'Torque resistivo: Q={round(Q,3)}N.m')
    print(f'Eficiencia na helice: {round(eta,3)}')
    print(f'Mach na ponta da pa: {round(Mach[-1],3)}')

    dTn = interp1d(var.r, dT, kind='cubic')
    dQn = interp1d(var.r, dQ, kind='cubic')
    R= npy.linspace(var.r[0],var.r[-1],40)

    plt.subplot(1,2,1)
    plt.plot(R/var.r.max(), dTn(R))
    plt.plot(var.r/var.r.max(), dT, 'x')
    plt.xlabel(r'$r/R$',fontsize=15)
    plt.ylabel(r'$dT/dr [N/m]$',fontsize=15)
    plt.grid(True)
    
    plt.subplot(1,2,2)
    plt.plot(R/var.r.max(), dQn(R))
    plt.plot(var.r/var.r.max(), dQ, 'x')
    plt.xlabel(r'$r/R$',fontsize=15)
    plt.ylabel(r'$dQ/dr$',fontsize=15)
    plt.grid(True)

    plt.show()

    plt.subplot(1,2,1)
    plt.plot(var.r/var.r.max(), Vr)
    plt.xlabel(r'$r/R$',fontsize=15)
    plt.ylabel(r'$V_r [m/s]$',fontsize=15)
    plt.grid(True)

    plt.subplot(1,2,2)
    plt.plot(var.r/var.r.max(), Mach)
    plt.xlabel(r'$r/R$',fontsize=15)
    plt.ylabel(r'$Mach$',fontsize=15)
    plt.grid(True)

    plt.plot(var.r/var.r.max(), phi*180/npy.pi)
    plt.xlabel(r'$r/R$',fontsize=15)
    plt.ylabel(r'$\phi$',fontsize=15)
    plt.grid(True)
    
    plt.show()

    return T,Q,eta

T,Q,eta = thrustTorqueCalculator()

endMain = time.time()
print(f'\n>> Time elapsed is {round((endMain-startMain),3)} seconds.\n   End of execution.\n')