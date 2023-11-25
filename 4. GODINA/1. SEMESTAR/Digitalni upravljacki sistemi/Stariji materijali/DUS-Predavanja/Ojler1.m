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
T = 1/3;
trenuci_odabiranja = 0:T:10;
br_odbiraka = length(trenuci_odabiranja);

%% Implementacija koda bez ugradjenih matlab funkcija
ulazni_signal = ones(1,br_odbiraka);
izlazni_signal = zeros(1,br_odbiraka);
yp = 0;
up = 0;
for i = 1:br_odbiraka
    u = ulazni_signal(i);
    y = (1-3*T)*yp+T*up;
    yp = y;
    up = u;
    izlazni_signal(i) = y;
end
plot(trenuci_odabiranja,izlazni_signal,'go')

