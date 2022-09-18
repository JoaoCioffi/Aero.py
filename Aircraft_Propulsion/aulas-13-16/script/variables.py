import numpy as npy

# Variáveis principais
mu = 1.783e-5    # viscosidade dinâmica [Kg/m/s]
Te = 288.15      # temperatura [k]
rho = 1.225      # densidade [kg/m3]
V = 44.4         # velocidade da aeronave [m/s]
N = 2000         # rotação do motor [rpm]
d = 96*0.0254    # diâmetro da hélice [m]
np = 2           # n de pás
q = 0.5*rho*V**2 # pressão dinâmica [Pa]

# Definição da geometria da pá
# r = npy.array([1e-6,10.,12.,18.,24.,30.,36.,42.,48.]) * 0.0254 # raio [m]
# c = npy.array([0.,4.82,5.48,6.86,7.29,7.06,6.35,5.06,0.]) * 0.0254 # corda [m]
# beta = npy.array([0.,46.3,43.25,38.1,31.65,26.3,22.4,19.5]) # ângulo geométrico [graus]

r = npy.linspace(1e-6,48,31) * 0.0254 # raio [m]
c = npy.array([0.,4.82,4.83,4.84,4.85,4.97,5.03,5.17,5.35,5.48,
               6.86,6.89,6.93,6.98,7.14,7.21,7.29,7.25,7.15,7.06,
               6.35,6.21,6.05,5.75,5.32,5.27,5.13,5.09,5.07,5.06,0.]) * 0.0254 # corda [m]
beta = npy.array([0.,46.3,46.3,46.3,46.3,46.3,46.3,46.3,46.3,43.25,
                   38.1,38.1,38.1,38.1,38.1,38.1,38.1,38.1,38.1,31.65,
                   26.3,26.3,26.3,26.3,22.4,22.4,22.4,19.5,19.5,19.5,19.5]) # ângulo geométrico [graus]