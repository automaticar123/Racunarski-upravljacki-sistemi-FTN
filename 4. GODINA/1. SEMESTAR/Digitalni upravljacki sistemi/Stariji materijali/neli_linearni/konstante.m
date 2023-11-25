%% Definisanje konstanti modela

clc
clear all
Ao=0.01;  % Površina izlaznog  preseka rezervoara
Ai=2;    % Površina gornjeg preseka rezervoara
g=9.81;  % Gravitaciono ubrzanje





%%
k=1;     % Konstanta gubitaka

%%
% 
% $$k \in [0,1]$$
% 




%% Radna taèka
% Odreðeno je da radna taèka bude na visini od 5m
H0=5;   
Q0=Ao*sqrt(2*k*g*H0);
%% Formiranje modela u prostoru stanja 
A=-Ao/Ai*k*g/sqrt(2*k*g*H0);
B=1/Ai;
C=[1];
D=[0];
sys=ss(A,B,C,D) %% Formiranje modela u prostoru stanja
%% Funkcija prenosa linearnog modela
G=tf(sys) %Formiranje funkcije prenosa od modela u prostoru stanja

%%


inflow=10;
outflow=50;
lolim=0;
hilim=10;
area=100



