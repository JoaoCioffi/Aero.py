import numpy as np
from colorama import Fore, Back, Style

#------------------------------------------------------------------------------

class Ex1:
    def __init__(self, g, cma, leading_edge_cma):
            self.__g = g                        #-> ac. gravidade (m/s²)
            self.__cma = cma                    #-> corda média aerodinâmica (m)
            self.__lecma = leading_edge_cma     #-> pos. do bordo de ataque da cma (m)


    def CG(self):
        """
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                           Código adaptado para:
                   "Introdução às Cargas nas Aeronaves"
                
            Iscold, P. H.; Centro de Estudos Aeronáuticos - UFMG
_______________________________________________________________________________
Ex 1. - Seção 2.3.2
Determine o peso vazio (empty weight), o peso vazio operacional (operating em-
pty weight), o peso vazio operacional mínimo (minimum operating empty weight),
o peso máximo zero combustível (minimum zero fuel weight) e o peso máximo da
aeronave CEA307 CB10 Triathlon.
Determine a posição do centro de gravidade da aeronave para as diversas condi-
ções citadas acima.
_______________________________________________________________________________
OBS: 
   
(i) Equação do X_cg da aeronave: X_cg = sum(wi*xi) , com i = (1,2,3,...,n)
                                         _________
                                          sum(wi)
(ii) Equação do X_cg da aeronave em termos de (%) da corda média aerodinâmica, 
tomada com relação ao bordo de ataque: X_cg,cma = (X_cg - X_cma) * 100 , 
                                                  ______________
                                                       cma
     Sendo:                                                  
     * X_cma: posição do bordo de ataque da cma em relação ao sistema de ref.
       adotado; 
     
     * cma: valor da corda média aerodinâmica;
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
        """
        
        
        #----------------------------------------
        #>> Tabela 1 - Componentes da Fuselagem: [Massa(kg), Braço(m)]
        t1 = np.array(([14., 1.53],     #-> F1 
                       [18., 2.28],     #-> F2
                       [14., 3.15],     #-> F3
                       [8., 3.88],      #-> F4
                       [6., 4.63],      #-> F5
                       [4., 5.35],))    #-> F6
        
        st1 = np.shape(t1)
        for j in range (0, st1[0]):
            t1[j][0] *= self.__g        #-> kg to kgf
        
        
        #>> Tabela 2 - Componentes da Aeronave: [Massa(kg), Braço(m)]
        t2 = np.array(([.92, .29],      #-> spinner
                       [5., .29],       #-> hélice
                       [4.5, .67],      #-> silencioso e tubos de escapamento
                       [5.7, .85],      #-> cobertura do motor
                       [12.96, .92],    #-> trem de pouso - bequilha
                       [2., .93],       #-> berço do motor
                       [.5, 1.22],      #-> bomba auxiliar de combustível
                       [2.34, 1.24],    #-> parede de fogo
                       [.5, 1.33],      #-> cilindros de freio
                       [1.5, 1.48],     #-> controle do motor
                       [3., 1.64],      #-> rádio
                       [4.25, 1.67],    #-> instrumentos
                       [.46, 1.74],     #-> linha de combustível
                       [2.5, 1.78],     #-> para-brisas
                       [9., 1.81],      #-> tanque de combustível
                       [55., 2.],       #-> asa
                       [1., 2.1],       #-> isolamento acústico
                       [15., 2.15],     #-> controles
                       [30.24, 2.28],   #-> trem de pouso principal
                       [1., 2.49],      #-> assentos
                       [1., 2.49],      #-> almofadas
                       [1., 2.49],      #-> cintos de segurança
                       [6., 2.36],      #-> conopy
                       [7.28, 5.31],    #-> empenagem horizontal
                       [4.6, 5.59],     #-> empenagem vertical
                       [.5, 1.2],       #-> fiação elétrica 
                       [104.5, .72],    #-> motor Lycoming
                       [12., 1.18],))   #-> bateria e suporte
        
        st2 = np.shape(t2)
        for j in range (0, st2[0]):
            t2[j][0] *= self.__g        #-> kg to kgf
        
        #>> Tabela 3 - Equipamentos de Vôo: [Peso(kgf), Braço(m)]
        t3 = np.array(([60., 2.36],     #-> piloto
                       [60., 2.36],     #-> passageiro
                       [22., 3.01],))   #-> bagagem
        
        st3 = np.shape(t3)    
        
        
        #----------------------------------------
        #>> Somatório parcial (peso_i * braço_i):
        m1, m2, m3 = [], [], []
        
        for i in range(0, st1[0]):
            m1.append(t1[i][0]*t1[i][1])
            wi_xi_1 = sum(m1)                                    
        
        for j in range(0, st2[0]):
            m2.append(t2[j][0]*t2[j][1])
            wi_xi_2 = sum(m2)                                    
            
        for k in range(0, st3[0]):
            m3.append(t3[k][0]*t3[k][1])
            wi_xi_3 = sum(m3)                                    
        
        #>> Somatório total (peso_i * braço_i)
        sum_wi_xi_total = wi_xi_1 + wi_xi_2  + wi_xi_3
        
        
        #----------------------------------------
        #>> Somatório dos pesos:
        sum_weight_per_table = np.array(([t1.sum(axis=0)],
                                         [t2.sum(axis=0)],
                                         [t3.sum(axis=0)],))
        
        sum_values = sum_weight_per_table.sum(axis=0)
            #sum_values[0][0] : soma pesos
            #sum_values[0][1] : soma braços
        sum_wi_total = sum_values[0][0]
        
        
        #----------------------------------------          
        
        #>> Pesos:
        ew = t1.sum(axis=0)[0]                            #-> empty weight
        oew = t1.sum(axis=0)[0] + t2.sum(axis=0)[0]       #-> operating empty weight
        moew = sum_wi_total - t2[10][0]\
             - t2[11][0] - t2[16][0] - t3.sum(axis=0)[0]  #-> minimum operating empty weight
        mzfw = moew - t2[14][0]                           #-> minimum zero fuel weight
        amw = sum_wi_total                                #-> aircraft maximum weight
        
        #>> Cálculo da posição do CG (em x):
        #1. Para AMW:    
        X_cg = sum_wi_xi_total/sum_wi_total
        X_cg_cma = ((X_cg - self.__lecma)/(self.__cma)) * 100
        
        return f'\n>> Aircraft Maximum Weight: {amw}kg\
                 \n>> Xcg: {X_cg}m\
                 \n>> Xcg,cma: {X_cg_cma}%\
                 \n-------------------------\
                 \n>> EW: {ew}kg\
                 \n>> OEW: {oew}kg\
                 \n>> MOEW: {moew}kg\
                 \n>> MZFW: {mzfw}kg'


res = Ex1(9.81, 1.205, 1.593).CG()


print(Ex1.CG.__doc__)
print('\n\n', Fore.RED + Back.GREEN + Style.BRIGHT,\
      '.::. Valores Obtidos .::.', Style.RESET_ALL, f'\n{res}')
