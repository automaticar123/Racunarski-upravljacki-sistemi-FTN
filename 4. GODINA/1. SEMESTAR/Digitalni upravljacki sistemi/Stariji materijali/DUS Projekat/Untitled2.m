%%
clear variables
close all

f1 = 1;
f2 = 1001;%kad stavimo 1000 poklapaju se spektri pa ne videimo
Fod=4.5;
T=1/Fod;
t=0:T:100;

x= sin(2*pi*f1*t);


spektar1 = abs(fft(x));

frequency_array = linspace(0,Fod, length(x));

figure(1);
subplot(2, 1, 1);
plot(frequency_array,spektar1);
subplot(2,1,2);
plot(t,x);
title('Spektar');
xlabel('frekvencija');
ylabel('Amplituda');

%%
%Zadatak 2.
clear variables
close all


Fod=4000;
T2=1/Fod;
f1 = 1;
f2 = 1000;

t=0:T2:2;
x= sin(2*pi*f1*t)+sin(2*pi*f2*t);

t_max = length(x) * T2;


s = tf('s');
wg =20;%tacka prelamanja ampl dijagrama
%w=100/(s/wg+10)^2    Filter koji 100% radi kako treba ali zbog jed resavanja dalje w2 smo izabrali
w2 = 1/(s/wg+1);

t_array = linspace(0,t_max, length(x));
x2 = lsim(w2,x, t_array);

frequency_array = linspace(0,Fod, length(x));

figure(2);
subplot(2, 1, 1);
plot(t, x)
title('Nefiltriran');
xlabel('Vreme');
ylabel('Amplituda');
subplot(2,1,2);
plot(t,x2)
title('Filtriran signal');
xlabel('Vreme');
ylabel('Amplituda');

%%
%Zadatak 3.
s=tf('s');
w=1/(s+1);
figure(3);
bode(w);
T=0.25;
b=-0.79;
a=0,21;
