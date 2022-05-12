import numpy as np


#>> Input data:
T1 = 288.    #-> temperatura (K)
gamma = 1.4  #-> gamma do ar
rho1 = 1.225 #-> dens. (kg/m³)
V = np.arange(150.,1005.,5.) #-> variação de velocidade no intervalo [150;1000]km/h
V = V/3.6 #-> fator de conversão: km/h to m/s


#>> Expressão para rho2 e verificação lógica para 5.00% e 10.00%:
rho2 = rho1 * ((( T1 - ( (69*(V**2))/(200800) ) )/T1)**(2.5))
var = 100-((rho2/rho1)*100) #-> variação percentual entre rho1 e rho2


#>> Percentuais desejados:
perc_1 = 5.
perc_2 = 10. 

#>> Iteração:
delta = 0.05 #-> fator de incerteza
pos = []     #-> posição dos elementos a serem validados
for i in range(0, len(var)):
  if (perc_1-delta) <= var[i] <= (perc_1+delta):
    pos.append(i)
  elif (perc_2-delta) <= var[i] <= (perc_2+delta):
    pos.append(i)


#>> Para 5.00%:
print(f"\n>> Dados: ρ1 = 1.225; V1 = {V[pos[0]]}m/s, teremos:")
print(f"\nρ2 = {rho2[pos[0]]}kg/m³ e uma variação de {var[pos[0]]}%\n")

print('_'*70)

#>> Para 10.00%:
print(f"\n>> Dados: ρ1 = 1.225; V1 = {V[pos[1]]}m/s, teremos:")
print(f"\nρ2 = {rho2[pos[1]]}kg/m³ e uma variação de {var[pos[1]]}%\n")