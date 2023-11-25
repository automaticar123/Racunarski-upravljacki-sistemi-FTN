s=tf('s');

G=10000/((s+100)^2)

bode(G)
grid on;
%%
syms z
f = (;
ztrans(f)
%% zadatak 4.
syms s 
F = s^2/((s+100)^2)
Fl = ilaplace(F)
syms z T
F2 = ztrans(Fl, T, z)

%%
s=tf('s');
  
%%
syms s
F = 1/((s+100)^2)
Fl = ilaplace(F)

%% zadatak 4.
syms s 
F = 1/((s+100)^2)
Fl = ilaplace(F)
syms z T
F2 = ztrans(Fl)

%% kons
s=tf('s');

G=10000/((s+100)^2)
Gd = c2d(G,0.01,'zoh')
Gi = c2d(G,0.01,'impulse')
Gt = c2d(G,0.01,'tustin')


step(G,'-',Gd,'--')
%impulse(G,'-',Gi,'--')
%step(G,'-',Gt,'--')

%% Z4 IMPULSNI   FINAAAAAL

s=tf('s');

G=10000/((s+100)^2)

T=0.01;
A=10000*T*T*exp(-100*T);
H = tf([A, 0],[1,-2*exp(-100*T), exp(-200*T)],T);
impulse(G,'-',H,'--')

%% Z4 STEP
T = 0.01;
A = (1-exp(-100*T)-exp(-100*T)*T)
B = exp(-200*T)-exp(-100*T)+100*exp(-100*T)*T
C = 100;
D = -200*exp(-100*T)
E = 100*exp(-200*T) + 200*exp(-100*T)
F = -100*exp(-200*T)

Gd = c2d(G,0.01,'zoh')

H = tf([A, B, 0],[D, E, F],T);

step(G,'-')

%% Z4 STEP SA SYMBOLABA
T = 0.005;

A = 1- 100*T*T*exp(-100*T) - exp(-100*T)
B = exp(-200*T) + 100*T*T*exp(-100*T) - exp(-100*T)

C = 1
D = -2*exp(-100*T)
E = exp(-200*T)

Gd = c2d(G,T,'zoh')

H = tf([A, B],[C, D, E],T);

step(G,'-',H,'--')

%% Z4 STEP SA SYMBOLABA BEZ T NA KVADRAT FINAAAAAAAAAL
T = 0.01;

A = 1- 100*T*exp(-100*T) - exp(-100*T)
B = exp(-200*T) + 100*T*exp(-100*T) - exp(-100*T)

C = 1
D = -2*exp(-100*T)
E = exp(-200*T)

Gd = c2d(G,T,'zoh')

H = tf([A, B],[C, D, E],T);

step(G,'-',H,'--')

%% Z4 STEP DOMACE
T = 0.01;

A = 100*(T*T-exp(-100*T))
B = (101*exp(-100*T)-T*T+1)
M = exp(-100*T)

C = 1
D = -2*exp(-100*T)
E = exp(-200*T)

Gd = c2d(G,0.01,'zoh')

H = tf([A, B, M],[C, D, E],T);

step(G,'-',H,'--')

%% Z4 TUST   FINAAAAAL

s=tf('s');

A=10000*T*T
B = 20000*T*T
C = A

D = 4+400*T+10000*T*T
E = 20000*T*T - 8
F = 4+10000*T*T-400*T

G=10000/((s+100)^2)

T=0.01;
H = tf([A,B,C],[D, E, F],T);
step(G,'-',H,'--')
