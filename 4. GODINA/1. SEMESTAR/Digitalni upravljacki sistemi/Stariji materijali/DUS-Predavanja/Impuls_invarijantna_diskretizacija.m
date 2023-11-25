clc
close all
clear all
%% Kontinualni sistem
s = tf('s');
G_c = 1/(s+3);
t = 0:0.01:10;
y_c = impulse(G_c,t);
plot(t,y_c)
hold on

%% Diskretni sistem
T = 0.3;
trenuci_odabiranja = 0:T:10;
br_odbiraka = length(trenuci_odabiranja);

G_d1 = c2d(G_c,T,'impulse');
y_d1 = impulse(G_d1,trenuci_odabiranja);
plot(trenuci_odabiranja,y_d1,'o')

%% Implementacija koda bez ugradjenih matlab funkcija
ulazni_signal = [1/T,zeros(1,br_odbiraka-1)];
izlazni_signal = zeros(1,br_odbiraka);
yp = 0;
for i=1:br_odbiraka
    u = ulazni_signal(i);
    y = yp*exp(-3*T) + T*u;
    izlazni_signal(i) = y;
    yp = y;
end

plot(trenuci_odabiranja,izlazni_signal,'*')

