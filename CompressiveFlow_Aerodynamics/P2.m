close all
clear variables
clc

tic
%% Ex 01.

fprintf('\n')
fprintf('---------------')
fprintf('\nEx 01\n')

%%%%%%%%%%% (a) %%%%%%%%%%%%
fprintf('\n########## (a) ##########\n')

%--- Dados de Entrada ---%
c = 0.1;
b = 0.3;
Eps = 5.;
alpha = 5.;
gamma = 1.4;



%--- Região 1 ---%
fprintf('\n--> Região 1\n')
%P0, T0:
P0_1 = 1020.e+03
T0_1 = 630


%Mach, T, p:
Mach_1 = 2.
T_1 = 350.
p_1 = 130.e3

%nu:
nu_1 = sqrt((gamma+1)/(gamma-1))*atan(sqrt(((gamma-1)/...
            (gamma+1))*((Mach_1^2)-1)))-atan(sqrt((Mach_1^2)-1));
   
nu_1 = rad2deg(nu_1)



%--- Região 2 ---%
fprintf('\n--> Região 2\n')
%P0, T0:
P0_2 = P0_1
T0_2 = T0_1

%theta, nu:
theta_2 = alpha - Eps
nu_2 = nu_1 + theta_2

%Mach, T, p:
Mach_2 = Mach_1
T_2 = T_1
p_2 = p_1



%--- Região 3 ---%
fprintf('\n--> Região 3\n')
%P0, T0:
P0_3 = P0_2
T0_3 = T0_2

%theta, nu:
theta_3 = 2*Eps
nu_3 = theta_3 + nu_2

%Mach, T, p:
Mach_3 = 2.385

p2_p3 = ( (1+(((gamma-1)/2))*(Mach_3^2))/...
          (1+(((gamma-1)/2))*(Mach_2^2)) ) ^ (gamma/(gamma-1)); %relação p3/p2
p_3 = (1/p2_p3)*p_2

T2_T3 = (1+(((gamma-1)/2))*(Mach_3^2))/(1+(((gamma-1)/2))*(Mach_2^2));
T_3 = (1/T2_T3)*T_2



%--- Região 4 ---%
fprintf('\n--> Região 4\n')
%P0, T0:
P0_4 = 733.
T0_4 = T0_3

%Mach, T, p:
Mach_4 = sqrt( (1+ ((gamma-1)/2) * (Mach_1^2) ) / ...
               ((gamma*(Mach_1^2)) - ((gamma-1)/(2))) );

p4_p3 = 1 + ( ((2*gamma)/(gamma+1)) * ((Mach_1^2)-1) );
p_4 = p4_p3*p_3;
p_4 = 585.e+03;

rho4_rho3 = ( (gamma+1)*(Mach_1^2) )/...
            ( ((gamma-1)*(Mach_1^2)) + 2);

T4_T3 = (p_4/p_3)*(1/rho4_rho3);
T_4 = (T4_T3)*T_3;
T_4 = 590.625;



%--- Região 5 ---%

%P0, T0:
P0_5 = P0_4
T0_5 = T0_4

%Mach, T, p:
Mach_5 = Mach_4
p_5 = p_4
T_5 = T_4



%--- Coeficientes de Sustentação e Arrasto ---%

l = c/(2*cosd(Eps));


D_5dg = -(p_2*b*l*sind(alpha-Eps)) - ...
         (p_3*b*l*sind(alpha+(2*Eps))) + ...
         (p_4*b*l*sind(alpha+(2*Eps))) + ...
         (p_5*b*l*sind(alpha-Eps))
Cd_5dg = D_5dg/((gamma/2)*p_1*(Mach_1^2)*b*c)


L_5dg = -(p_2*b*l*cosd(alpha-Eps)) - ...
         (p_3*b*l*cosd(alpha+(2*Eps))) + ...
         (p_4*b*l*cosd(alpha+(2*Eps))) + ...
         (p_5*b*l*cosd(alpha-Eps))
Cl_5dg = L_5dg/((gamma/2)*p_1*(Mach_1^2)*b*c)



%%%%%%%%%%% (b) %%%%%%%%%%%%
fprintf('\n########## (b) ##########\n')

%--- Dados de Entrada ---%
c = 0.1;
b = 0.3;
Eps = 5.;
alpha = 10.;
gamma = 1.4;



%--- Região 1 ---%
fprintf('\n--> Região 1\n')
%P0, T0:
P0_1 = 1020.e+03
T0_1 = 630

%Mach, T, p:
Mach_1 = 2.
T_1 = 350.
p_1 = 130.e3

%nu:
nu_1 = sqrt((gamma+1)/(gamma-1))*atan(sqrt(((gamma-1)/...
            (gamma+1))*((Mach_1^2)-1)))-atan(sqrt((Mach_1^2)-1));
   
nu_1 = rad2deg(nu_1)



%--- Região 2 ---%
fprintf('\n--> Região 2\n')
%P0, T0:
P0_2 = P0_1
T0_2 = T0_1

%theta, nu:
theta_2 = alpha - Eps
nu_2 = nu_1 + theta_2

%Mach, T, p:
Mach_2 = 2.186

T1_T2 = ( 1 + ( ((gamma-1)/2)*(Mach_2^2)) )/...
        ( 1 + ( ((gamma-1)/2)*(Mach_1^2)) )
T_2 = (1/T1_T2)*T_1

p1_p2 = ( ( 1 + ( ((gamma-1)/2)*(Mach_2^2)) )/...
          ( 1 + ( ((gamma-1)/2)*(Mach_1^2)) ) ) ^ (gamma/(gamma-1));
p_2 = (1/p1_p2)*p_1



%--- Região 3 ---%
fprintf('\n--> Região 3\n')
%P0, T0:
P0_3 = P0_2
T0_3 = T0_2

%theta, nu:
theta_3 = 2*Eps
nu_3 = theta_3 + nu_2

%Mach, T, p:
Mach_3 = 2.599

T2_T3 = ( 1 + ( ((gamma-1)/2)*(Mach_3^2)) )/...
        ( 1 + ( ((gamma-1)/2)*(Mach_2^2)) )
T_3 = (1/T2_T3)*T_2

p2_p3 = ( ( 1 + ( ((gamma-1)/2)*(Mach_3^2)) )/...
          ( 1 + ( ((gamma-1)/2)*(Mach_2^2)) ) ) ^ (gamma/(gamma-1))
p_3 = (1/p2_p3)*p_2



%--- Região 4 ---%
fprintf('\n--> Região 4\n')
%P0, T0:
P0_4 = 733.
T0_4 = T0_3

%Mach, T, p:
Mach_4 = sqrt( (1+ ((gamma-1)/2) * (Mach_1^2) ) / ...
               ((gamma*(Mach_1^2)) - ((gamma-1)/(2))) )

p4_p3 = 1 + ( ((2*gamma)/(gamma+1)) * ((Mach_1^2)-1) )
p_4 = p4_p3*p_3
p_4 = 585.e+03

rho4_rho3 = ( (gamma+1)*(Mach_1^2) )/...
            ( ((gamma-1)*(Mach_1^2)) + 2)

T4_T3 = (p_4/p_3)*(1/rho4_rho3)
T_4 = (T4_T3)*T_3
T_4 = 590.625



%--- Região 5 ---%
fprintf('\n--> Região 5\n')
%P0, T0:
P0_5 = P0_4
T0_5 = T0_4

%Mach, T, p:
Mach_5 = Mach_4
p_5 = p_4
T_5 = T_4



%--- Coeficientes de Sustentação e Arrasto ---%

l = c/(2*cosd(Eps));


D_10dg = -(p_2*b*l*sind(alpha-Eps)) - ...
          (p_3*b*l*sind(alpha+(2*Eps))) + ...
          (p_4*b*l*sind(alpha+(2*Eps))) + ...
          (p_5*b*l*sind(alpha-Eps))
Cd_10dg = D_10dg/((gamma/2)*p_1*(Mach_1^2)*b*c)


L_10dg = -(p_2*b*l*cosd(alpha-Eps)) - ...
          (p_3*b*l*cosd(alpha+(2*Eps))) + ...
          (p_4*b*l*cosd(alpha+(2*Eps))) + ...
          (p_5*b*l*cosd(alpha-Eps))
Cl_10dg = L_10dg/((gamma/2)*p_1*(Mach_1^2)*b*c)

%%
toc
