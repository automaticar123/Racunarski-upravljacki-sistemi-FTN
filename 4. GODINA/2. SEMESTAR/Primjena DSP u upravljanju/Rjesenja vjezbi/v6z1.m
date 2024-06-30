%% FURIJEOVA TRANSFORMACIJA DISKRETNIH SIGNALA

% Amplitudski spektar je uvek parna funkcija

% 1. Periodicni signali 
% Razvojem periodicnog signala u furijeov red, dobijamo diskreni spektar.
% Vrednosti frekvencija na ampplitudskom spektru su celobrojni umnosci
% omega0. omega0 = 2*pi/T

% 2. Aperiodicni signali
% a) kontinualni aperiodican signal: t->inf
%    Za racunanje spektra se koristi Furijeova trnasformacija. Spektar
%    aperiodicnog kontinualnog signala je kontinualan.
% b) diskretni aperiodicni signali
%    neki kontinualni signal se diskretizuje u vremenu, sa periodom 
%    odabiranja Ts da bi se dobio diskretan (konti pomnozimo sa povorkom 
%    delta impulsa).
%    Nad diskrenim signalom se radi furijeova transformacija diskretnog
%    signala pri cemu se dobija periodican, kontinualan spektar. Spektri se
%    ponavljaju sa periodom celobrojnog omega0. omega0 = 2*pi/T.
%    T jako malo -> omega0 jako veliko,  sigurno ispostivan Nikvist
%    T jako veliko -> omega0 jako malo,  dolazi do preklapanja spektra 
%    (alijasing) i ne moze da se rekonstruise originalni spektar

% Nikvistova teorema omega0 > 2*omegaMax

% veliko_omega = 2*pi*F ili omega*T tj omega/f

% "kontinualne frekvencije" -> f, omega (mali)

%% 1 Zasto t=10s n=100?
clc
clear

t = 0:0.01:10;
x = exp(-t);

figure, subplot(211), plot(t, x);
xlabel("t[s]");
title("Kontinualni signal");

n = 0:100;
T = 0.15;      % probati i T=20 i T=0.15
xn = exp(-n*T);
subplot(212), stem(n, xn);
xlabel("n");
title("Diskreni signal");

f = -5:0.01:5;
omega = 2*pi*f;
X_jW = 1 ./ (1+1j*omega); % spektar kontinualnog signala
figure, subplot(511)
plot(f, abs(X_jW));
title("X(jW) - Amplitudski spektar kontinualnog signala");
xlabel("f(Hz)");

vW = -4*pi:0.01:4*pi; % diskretna kruzna ucestanost
X_exp_jvW = T./(1-exp(-T)*cos(vW) + 1j*exp(-T) * sin(vW));
subplot(512), plot(vW, abs(X_exp_jvW));
title("X(e^j*vW) Amplitudski spektar diskretnog signala")
xlabel("\Omega (rad)");  % perioda je 2pi

F = vW/(2*pi);
subplot(513), plot(F, abs(X_exp_jvW));
title("X(e^j*vW)")
xlabel("F (/)");  % perioda je 1

omega = vW/T;
subplot(514), plot(omega, abs(X_exp_jvW));
title("X(e^j*vW)")
xlabel("\omega (rad/s)");

f = omega/(2*pi);
subplot(515), plot(f, abs(X_exp_jvW))
title("X(e^j*vW)")
xlabel("f (Hz)");

%% 2
% na ulaz antialijasing filtra dovodi se x(t)

clc
clear
% k = linspace(-10,10,512);
omega = linspace(-10,10,512);
X_jw = 1./(1j*omega-log(0.5));

figure, subplot(311)
plot(omega, abs(X_jw))
title("Amplitudski signala na ulazu filtra")
xlabel("\omega (rad/s)")

H_jw = (omega>-5) & (omega<5);
subplot(312), plot(omega, H_jw);  % u opstem slucaju treba abs
title("Amplitudska karakteristika filtra")
xlabel("\omega (rad/s)")
ylim([-0.5, 1.5])

Y_jw = X_jw .* H_jw;
subplot(313), plot(omega, abs(Y_jw));
title("Amplitudski spektar signala nakon filtracije")
xlabel("\omega (rad/s)")


%% 3 

clc
clear

t = 0:0.01:10;
xt = 0.1.^t;
n = 0:100;
T = 0.4;
xn = 0.1.^(T*n);
subplot(411), plot(t, xt)
title("Kontinualni signal")

subplot(413), stem(n, xn)
title("Diskreni signal")

w = -20:0.01:20;
X_jw = 1./(1j*w-log(0.1));
subplot(412), plot(w, abs(X_jw));
title("Amplitudski spektar kontinualnog signala")

W = w*T;
X_exp_jvW = 1./(1-0.1^T*exp(1j*W));
subplot(414), plot(W, abs(X_exp_jvW))
title("Amplituski spektar diskretnog signala")


































