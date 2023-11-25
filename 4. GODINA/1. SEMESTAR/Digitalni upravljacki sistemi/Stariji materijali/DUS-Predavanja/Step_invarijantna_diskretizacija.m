clc
close all
clear all
%% Kontinualni sistem
s = tf('s');
G_c = 1/(s+3);
t = 0:0.01:10;
y_c = step(G_c,t);
plot(t,y_c)
hold on
%% Diskretni sistem
T = 0.3;
trenuci_odabiranja = 0:T:10;
br_odbiraka = length(trenuci_odabiranja);

G_d1 = c2d(G_c,T,'zoh');
y_d1 = step(G_d1,trenuci_odabiranja);
plot(trenuci_odabiranja,y_d1,'o')

%% Implementacija koda bez ugradjenih matlab funkcija
ulazni_signal = ones(1,br_odbiraka);
izlazni_signal = zeros(1,br_odbiraka);
yp = 0;
up = 0;
for i=1:br_odbiraka
    u = ulazni_signal(i);
    y = yp*exp(-3*T) + 1/3*(1-exp(-3*T))*up;
    izlazni_signal(i) = y;
    yp = y;
    up = u;
end

plot(trenuci_odabiranja,izlazni_signal,'*')