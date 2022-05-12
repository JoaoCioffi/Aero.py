import numpy as np
from math import (pi as pi,
                  sqrt as sqrt,
                  cos as cos,
                  sin as sin)

#------------------------------------------------------------------------------

class VLM:
    def __init__(self, vertices_painel_data, vertices_anel_data, pontos_controle_data):
        self.__vp = vertices_painel_data    #-> coord. vértices de cada painel
        self.__va = vertices_anel_data      #-> coord. vértices de cada anel
        self.__pc = pontos_controle_data    #-> coord. pontos de controle
    

    #///////////////////////////////////////////////////////////
    #||             Influência de um Vórtice Anel             ||          
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    def ring_vortex(self):
        """
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
            Fator de influência do vórtice anel de um painel 'k'
                sobre o ponto de controle de um painel 'n'
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        """
        print('>> Seja um fator de influência definido por Cnk:')
        n = int(input('Insira o ponto de controle de um painel (n) -> '))
        k = int(input('Insira o vórtice anel de um painel (k) -> '))
        
        
        #>> Slicing do Array Definido Pelo Usuário:
        pc = self.__pc[n-1]
        va = self.__va[k-1]
        
        
        #>> Termos Gerais da Equação do Cnk:
        r1 = np.array(([pc[1] - va[1]],                         #-> em x
                       [pc[2] - va[2]],                         #-> em y
                       [pc[3] - va[3]],))                       #-> em z 
        
        r2 = np.array(([pc[1] - va[4]],                         #-> em x
                       [pc[2] - va[5]],                         #-> em y
                       [pc[3] - va[6]],))                       #-> em z
        
        r3 = np.array(([pc[1] - va[7]],                         #-> em x
                       [pc[2] - va[8]],                         #-> em y
                       [pc[3] - va[9]],))                       #-> em z
        
        r4 = np.array(([pc[1] - va[10]],                        #-> em x
                       [pc[2] - va[11]],                        #-> em y
                       [pc[3] - va[12]],))                      #-> em z
        
        r12 = np.array(([r2[0] - r1[0]],
                        [r2[1] - r1[1]],
                        [r2[2] - r1[2]]),) * (-1)               #-> array: -(r2-r1)
        
        r23 = np.array(([r3[0] - r2[0]],
                        [r3[1] - r2[1]],
                        [r3[2] - r2[2]]),) * (-1)               #-> array: -(r3-r2)
        
        r34 = np.array(([r4[0] - r3[0]],
                        [r4[1] - r3[1]],
                        [r4[2] - r3[2]]),) * (-1)               #-> array: -(r4-r3)
        
        r41 = np.array(([r4[0] - r1[0]],
                        [r4[1] - r1[1]],
                        [r4[2] - r1[2]]),) * (-1)               #-> array: -(r4-r1)
        
        
        #>> Produto Vetorial:
        pv12 = np.array(([(r1[1]*r2[2]) - (r1[2]*r2[1])],
                         [(r1[2]*r2[0]) - (r1[0]*r2[2])],
                         [(r1[0]*r2[1]) - (r1[1]*r2[0])],))     #-> r1 x r2
            
        pv23 = np.array(([(r2[1]*r3[2]) - (r2[2]*r3[1])],
                         [(r2[2]*r3[0]) - (r2[0]*r3[2])],
                         [(r2[0]*r3[1]) - (r2[1]*r3[0])],))     #-> r2 x r3
            
        pv34 = np.array(([(r3[1]*r4[2]) - (r3[2]*r4[1])],
                         [(r3[2]*r4[0]) - (r3[0]*r4[2])],
                         [(r3[0]*r4[1]) - (r3[1]*r4[0])],))     #-> r3 x r4
            
        pv41 = np.array(([(r4[1]*r1[2]) - (r4[2]*r1[1])],
                         [(r4[2]*r1[0]) - (r4[0]*r1[2])],
                         [(r4[0]*r1[1]) - (r4[1]*r1[0])],))     #-> r4 x r1
         
        
        #>> Módulo do Produto Vetorial:
        mod_pv12 = sqrt(((pv12[0])**2) + ((pv12[1])**2) + ((pv12[2])**2))   #-> |r1 x r2|
        mod_pv23 = sqrt(((pv23[0])**2) + ((pv23[1])**2) + ((pv23[2])**2))   #-> |r2 x r3|
        mod_pv34 = sqrt(((pv34[0])**2) + ((pv34[1])**2) + ((pv34[2])**2))   #-> |r3 x r4|
        mod_pv41 = sqrt(((pv41[0])**2) + ((pv41[1])**2) + ((pv41[2])**2))   #-> |r4 x r1|
        
        
        #>> Produto Escalar:
        pe121 = (r12[0]*r1[0]) + (r12[1]*r1[1]) + (r12[2]*r1[2])            #-> r12 * r1
        pe122 = (r12[0]*r2[0]) + (r12[1]*r2[1]) + (r12[2]*r2[2])            #-> r12 * r2
        pe232 = (r23[0]*r2[0]) + (r23[1]*r2[1]) + (r23[2]*r2[2])            #-> r23 * r2
        pe233 = (r23[0]*r3[0]) + (r23[1]*r3[1]) + (r23[2]*r3[2])            #-> r23 * r3
        pe343 = (r34[0]*r3[0]) + (r34[1]*r3[1]) + (r34[2]*r3[2])            #-> r34 * r3
        pe344 = (r34[0]*r4[0]) + (r34[1]*r4[1]) + (r34[2]*r4[2])            #-> r34 * r4
        pe414 = (r41[0]*r4[0]) + (r41[1]*r4[1]) + (r41[2]*r4[2])            #-> r41 * r4
        pe411 = (r41[0]*r1[0]) + (r41[1]*r1[1]) + (r41[2]*r1[2])            #-> r41 * r1
        
        
        #>> Módulo do Vetor:
        mod_r1 = sqrt(((r1[0])**2) + ((r1[1])**2) + ((r1[2])**2))           #-> |r1|
        mod_r2 = sqrt(((r2[0])**2) + ((r2[1])**2) + ((r2[2])**2))           #-> |r2|
        mod_r3 = sqrt(((r3[0])**2) + ((r3[1])**2) + ((r3[2])**2))           #-> |r3|
        mod_r4 = sqrt(((r4[0])**2) + ((r4[1])**2) + ((r4[2])**2))           #-> |r4|
         
        
        #>> Equação do Cnk:
        zeta = (1/(4*pi)) * ( ((1/(mod_pv12**2)) * ((pe121/mod_r1) - (pe122/mod_r2))) \
                          +   ((1/(mod_pv23**2)) * ((pe232/mod_r2) - (pe233/mod_r3))) \
                          +   ((1/(mod_pv34**2)) * ((pe343/mod_r3) - (pe344/mod_r4))) \
                          +   ((1/(mod_pv41**2)) * ((pe414/mod_r4) - (pe411/mod_r1))) )
        
        global_array_user = np.array(([pv12[0] + pv23[0] + pv34[0] + pv41[0]],\
                                       [pv12[1] + pv23[1] + pv34[1] + pv41[1]],\
                                       [pv12[2] + pv23[2] + pv34[2] + pv41[2]],))
        
        Cnk = zeta*global_array_user
        
        
        Cnk = {'x: ':float(Cnk[0]), 'y: ':float(Cnk[1]), 'z: ':float(Cnk[2])}
        print(f'\n\n>> Fator de influência do vórtice anel do painel {k} sobre o ponto de controle do painel {n}:')
        print(f'\n\t\t(C{n}{k})')
        print('-------------------------')
        for key, value in Cnk.items():
            print(f'{key}{value}')
        
        del (n, k, pc, va,
            r1, r2, r12,
            pv12, mod_pv12,
            pe121, pe122,
            mod_r1, mod_r2,
            zeta, global_array_user)
            
        return Cnk
        
    
    #///////////////////////////////////////////////////////////
    #||          Influência de um Vórtice Ferradura           ||          
    #\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 
    def horseshoe_vortex(self):
        """
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
         Fator de influência do vórtice ferradura de um painel 'k'
                 sobre o ponto de controle de um painel 'n'
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        """
        print('>> Seja um fator de influência definido por Cnk*:')
        n = int(input('Insira o ponto de controle de um painel (n) -> '))
        k = int(input('Insira o vórtice anel de um painel (k) -> '))
        
        
        #>> Slicing do Array Definido Pelo Usuário:
        pc = self.__pc[n-1]
        va = self.__va[k-1]
        
        
        print('\n')
        
        
        print('>> Seja o ângulo de ataque do escoamento livre (desconsiderando vento lateral):')
        alpha = float(input('Insira ângulo de ataque, alpha(°) -> '))
        def deg2rad(alpha):
            c = pi/180     #-> fator de conversão
            return alpha*c
        alpha = deg2rad(alpha)
        e_infty = (cos(alpha), 0., sin(alpha))
        
        
        #>> Termos Gerais da Equação do Cnk*:
        r1 = np.array(([pc[1] - va[10]],                        #-> em x
                       [pc[2] - va[11]],                        #-> em y
                       [pc[3] - va[12]],))                      #-> em z
        
        r2 = np.array(([pc[1] - va[7]],                         #-> em x
                       [pc[2] - va[8]],                         #-> em y
                       [pc[3] - va[9]],))                       #-> em z
        
        r3 = np.array(([pc[1] - va[7]],                         #-> em x
                       [pc[2] - va[8]],                         #-> em y
                       [pc[3] - va[9]],))                       #-> em z
        
        r4 = np.array(([pc[1] - va[10]],                        #-> em x
                       [pc[2] - va[11]],                        #-> em y
                       [pc[3] - va[12]],))                      #-> em z
        
        r34 = np.array(([r4[0] - r3[0]],
                        [r4[1] - r3[1]],
                        [r4[2] - r3[2]]),) * (-1)               #-> array: -(r4-r3)
        
        
        r12 = r34 * (-1)                                        #-> r12(atual) = -r34(anterior)
        
        
        #>> Produto Vetorial:
        pve1 = np.array(([(e_infty[1]*r1[2]) - (e_infty[2]*r1[1])],
                          [(e_infty[2]*r1[0]) - (e_infty[0]*r1[2])],
                          [(e_infty[0]*r1[1]) - (e_infty[1]*r1[0])],))          #-> e_infty x r1
        
        pve2 = np.array(([(e_infty[1]*r2[2]) - (e_infty[2]*r2[1])],
                          [(e_infty[2]*r2[0]) - (e_infty[0]*r2[2])],
                          [(e_infty[0]*r2[1]) - (e_infty[1]*r2[0])],))          #-> e_infty x r2
        
        pv12 = np.array(([(r1[1]*r1[2]) - (r1[2]*r1[1])],
                         [(r1[2]*r2[0]) - (r1[0]*r1[2])],
                         [(r1[0]*r2[1]) - (r1[1]*r1[0])],))                     #-> r1 x r2
        
        
        #>> Módulo do Produto Vetorial:
        mod_pve1 = sqrt(((pve1[0])**2) + ((pve1[1])**2) + ((pve1[2])**2))       #-> |e_infty x r1|
        mod_pve2 = sqrt(((pve2[0])**2) + ((pve2[1])**2) + ((pve2[2])**2))       #-> |e_infty x r2|
        mod_pv12 = sqrt(((pv12[0])**2) + ((pv12[1])**2) + ((pv12[2])**2))       #-> |e_infty x r1|
        
        
        #>> Produto Escalar:
        pe1e = (r1[0]*e_infty[0]) + (r1[1]*e_infty[1]) + (r1[2]*e_infty[2])     #-> r1 * e_infty
        pe2e = (r2[0]*e_infty[0]) + (r2[1]*e_infty[1]) + (r2[2]*e_infty[2])     #-> r2 * e_infty
        pe121 = (r12[0]*r1[0]) + (r12[1]*r1[1]) + (r12[2]*r1[2])                #-> r12 * r1
        pe122 = (r12[0]*r2[0]) + (r12[1]*r2[1]) + (r12[2]*r2[2])                #-> r12 * r2
        
        
        #>> Módulo do Vetor:
        mod_r1 = sqrt(((r1[0])**2) + ((r1[1])**2) + ((r1[2])**2))               #-> |r1|
        mod_r2 = sqrt(((r2[0])**2) + ((r2[1])**2) + ((r2[2])**2))               #-> |r2|
        
        
        #>> Equação do Cnk*:
        zeta = float( (((pe2e/mod_r2)+1)/(4*pi*(mod_pve2**2))) )
        xi =   float( (((pe1e/mod_r1)+1)/(4*pi*(mod_pve1**2))) )
        eta =  float( ((pe121/mod_r1)-(pe122/mod_r2))*(1/(4*pi*(mod_pv12**2))) )
        
        
        global_array_user = np.array(([pve2[0] + pve1[0] + pv12[0]],\
                                      [pve2[1] + pve1[1] + pv12[1]],\
                                      [pve2[2] + pve1[2] + pv12[2]]))
        
        Cnk = ((zeta*global_array_user[0]) - (xi*global_array_user[0]) + eta*global_array_user[0],\
               (zeta*global_array_user[1]) - (xi*global_array_user[1]) + eta*global_array_user[1],\
               (zeta*global_array_user[2]) - (xi*global_array_user[2]) + eta*global_array_user[2])
        
        Cnk = {'x: ':float(Cnk[0]), 'y: ':float(Cnk[1]), 'z: ':float(Cnk[2])}
        print(f'\n\n>> Fator de influência do vórtice ferradura do painel {k} sobre o ponto de controle do painel {n} para alpha = {alpha*180/pi}°:')
        print(f'\n\t\t(C{n}{k}*)')
        print('-------------------------')
        for key, value in Cnk.items():
            print(f'{key}{value}')
            
        return Cnk

#------------------------------------------------------------------------------

#///////////////////////////////////////////////////////////
#||                     Inputs                            ||          
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

    
#>> Vértices dos Painéis:
vertices_painel_data = np.loadtxt( 'vertices_painel.txt' )
"""
COORDENADAS DOS VERTICES DOS PAINEIS 
Ordem de numeracao dos vertices em cada painel: 
                1        2 
                 x------x  
                 |      |  
                 |      |  
                 x------x  
                4        3 
          Vertice 1               Vertice 2               Vertice 3               Vertice 4 
N     x       y       z       x       y       z       x       y       z       x       y       z 
1  1.8821 -3.0000 -0.0617  0.9410 -1.5000 -0.0372  1.7910 -1.5000  0.0372  2.5821 -3.0000  0.0617 
2  0.9410 -1.5000 -0.0372  0.0000  0.0000 -0.0000  1.0000  0.0000  0.0000  1.7910 -1.5000  0.0372 
3  0.0000  0.0000 -0.0000  0.9410  1.5000 -0.0372  1.7910  1.5000  0.0372  1.0000  0.0000  0.0000 
4  0.9410  1.5000 -0.0372  1.8821  3.0000 -0.0617  2.5821  3.0000  0.0617  1.7910  1.5000  0.0372 
5  2.5821 -3.0000  0.0617  1.7910 -1.5000  0.0372  2.6410 -1.5000  0.1115  3.2821 -3.0000  0.1851 
6  1.7910 -1.5000  0.0372  1.0000  0.0000  0.0000  2.0000  0.0000  0.0000  2.6410 -1.5000  0.1115 
7  1.0000  0.0000  0.0000  1.7910  1.5000  0.0372  2.6410  1.5000  0.1115  2.0000  0.0000  0.0000 
8  1.7910  1.5000  0.0372  2.5821  3.0000  0.0617  3.2821  3.0000  0.1851  2.6410  1.5000  0.1115
"""


#>> Vértices dos Anéis:
vertices_anel_data = np.loadtxt( 'vertices_anel.txt' )
"""
COORDENADAS DOS VERTICES DOS ANEIS 
Ordem de numeracao dos vertices: 
                1        2 
                 x------x  
                 |      |  
                 |      |  
                 x------x  
                4        3 
          Vertice 1               Vertice 2               Vertice 3               Vertice 4 
N     x       y       z       x       y       z       x       y       z       x       y       z 
1  2.0571 -3.0000 -0.0309  1.1535 -1.5000 -0.0186  2.0035 -1.5000  0.0558  2.7571 -3.0000  0.0926 
2  1.1535 -1.5000 -0.0186  0.2500  0.0000 -0.0000  1.2500  0.0000  0.0000  2.0035 -1.5000  0.0558 
3  0.2500  0.0000 -0.0000  1.1535  1.5000 -0.0186  2.0035  1.5000  0.0558  1.2500  0.0000  0.0000 
4  1.1535  1.5000 -0.0186  2.0571  3.0000 -0.0309  2.7571  3.0000  0.0926  2.0035  1.5000  0.0558 
5  2.7571 -3.0000  0.0926  2.0035 -1.5000  0.0558  2.8535 -1.5000  0.1301  3.4571 -3.0000  0.2160 
6  2.0035 -1.5000  0.0558  1.2500  0.0000  0.0000  2.2500  0.0000  0.0000  2.8535 -1.5000  0.1301 
7  1.2500  0.0000  0.0000  2.0035  1.5000  0.0558  2.8535  1.5000  0.1301  2.2500  0.0000  0.0000 
8  2.0035  1.5000  0.0558  2.7571  3.0000  0.0926  3.4571  3.0000  0.2160  2.8535  1.5000  0.1301
"""


#>> Pontos de Controle:
pontos_controle_data = np.loadtxt( 'pontos_de_controle.txt' )
"""
COORDENADAS DOS PONTOS DE CONTROLE 
N     x       y       z 
1  1.9928 -2.2500  0.0255 
2  1.1643 -0.7500  0.0101 
3  1.1643  0.7500  0.0101 
4  1.9928  2.2500  0.0255 
5  2.7678 -2.2500  0.1275 
6  2.0893 -0.7500  0.0505 
7  2.0893  0.7500  0.0505 
8  2.7678  2.2500  0.1275 
"""

#------------------------------------------------------------------------------
print('\n\n')
print('<_________________>')
print('|   Ring Vortex   |')
print('<_________________>')
print(VLM.ring_vortex.__doc__)
ans_ringvortex = VLM(vertices_painel_data,\
                     vertices_anel_data,\
                     pontos_controle_data).ring_vortex()

    
print('\n\n')
print('<______________________>')
print('|   Horseshoe Vortex   |')
print('<______________________>')
print(VLM.horseshoe_vortex.__doc__)
ans_horseshoevortex = VLM(vertices_painel_data,\
                          vertices_anel_data,\
                          pontos_controle_data).horseshoe_vortex()
    
#--------------------------------------------------------------------------End.
