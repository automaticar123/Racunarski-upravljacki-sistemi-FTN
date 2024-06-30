% DISKRETNA FURIJEOVA TRANSFORMACIJA - DFT
% X = fft(x, N)
% x je diskretan signal
% N je bruj tacaka u kojima se radi diskretizacija spektra, default je
% duzina x.

% - kod realnih signala spektar nije ogranicen
% - kod beskonacnih signala spektar jeste ogranicen

% f0/fs treba da je ceo broj

%% 
M = 8;
N = 16;
n = 0:N-1;  % Ts je 1 
x = (n>=0)-((n-M)>=0);
figure, subplot(311);
stem(n, x)
xlabel('n');
title('x(n)');

X_k = fft(x, N);
k = 0:N-1;

% kad je data frekvencija odabiranja, onda ima smisla plotovati na frekv
% osi
subplot(312), stem(k, abs(X_k))
xlabel('k')
title(['X(k) Amplitudski spektar, za N = ', num2str(N)]);

N = 64;
X_k2 = fft(x, N);
k = 0:N-1;

subplot(313), stem(k, abs(X_k2))
xlabel('k')
title(['X(k) Amplitudski spektar, za N = ', num2str(N)]);

%% DFT jedinicnog impulsa u 16 tacaka
clc
clear

N = 16;
n = 0:N-1;
x = (n==0);
figure, subplot(211), stem(n, x);
title('\delta (n)')

X_k = fft(x, N);
k = 0:N-1;
subplot(212)
stem(k, abs(X_k));
title('amplitudski spektar \delta(n)')

%% DFT Hevisajd signala u 16 tacaka
clc
clear

N = 16;
n = 0:N-1;
x = (n>=0);
figure, subplot(211), stem(n, x);
title('h(n)')

X_k = fft(x, N);
k = 0:N-1;
subplot(212)
stem(k, abs(X_k));
title('amplitudski spektar h(n)')

%% 6
clc
clear

N = 16;
n = 0:N-1;
x = (n==0) + 1.5*((n-1)==0) + ((n-2)==0) + 0.75*((n-3)==0);
figure, subplot(311), stem(n, x);
title('x(n)')

X_k = fft(x, N);
k = 0:N-1;
subplot(312)
stem(k, abs(X_k));
title(['amplitudski spektar u N = ', num2str(N)])

N=64;
X_k = fft(x, N);
k = 0:N-1;
subplot(313)
stem(k, abs(X_k));
title(['amplitudski spektar u N = ', num2str(N)])

fs = 1;
frekv = linspace(0, fs, N);
figure, stem(frekv, abs(X_k));

%% 7

f = 20;
tn = 10;
fs = 100;
N = 1000;

t = 0:0.0001:tn;
x = sin(2*pi*f*t);
figure, subplot(411), plot(t, x);
title('f(t)')
xlabel('t[s]s')

n = 0:1/fs:tn;
x = sin(2*pi*f*n);
subplot(412), stem(n, x);
title('f(n)')
xlabel('n')

X_k = fft(x, N);
frekv = linspace(0, fs, N);    % f = W/(T*2*pi) [Hz] ; 2*pi odgovara fs
subplot(413), stem(frekv, abs(X_k));
title('Amplitudski spektar sin(2\pift)')
xlabel('f[Hz]')

% crtamo spektar od -fs/2 do fs/2 - centiramo oko nule
x_centrirano = fftshift(fft(x, N));
f_centrirano = linspace(-fs/2, fs/2, N);
subplot(414), stem(f_centrirano, abs(x_centrirano));
title('Centriran spektar oko nule')

% odraditi racunanje spektra od 0 do fs/2, od pocetka

%% opet 7 
f = 20;
tn = 10;
fs = 100;
N = 1000;

% Continuous-time signal
t = 0:0.0001:tn;
x = sin(2*pi*f*t);
figure, subplot(511), plot(t, x);
title('f(t)')
xlabel('t[s]')

% Discrete-time signal
n = 0:1/fs:tn;
x = sin(2*pi*f*n);
subplot(512), stem(n, x);
title('f(n)')
xlabel('n')

% Full FFT spectrum
X_k = fft(x, N);
frekv = linspace(0, fs, N);
subplot(513), stem(frekv, abs(X_k));
title('Amplitudski spektar sin(2\pift)')
xlabel('f[Hz]')

% Centered FFT spectrum
x_centrirano = fftshift(fft(x, N));
f_centrirano = linspace(-fs/2, fs/2, N);
subplot(514), stem(f_centrirano, abs(x_centrirano));
title('Centriran spektar oko nule')

% Spectrum from 0 to fs/2
half_N = N/2; 
X_k_half = X_k(1:half_N);
frekv_half = linspace(0, fs/2, half_N);
subplot(515), stem(frekv_half, abs(X_k_half));
title('Spektar od 0 do fs/2')
xlabel('f[Hz]')

%% 9

tn = 10;
fs = 120;  % mora da bude bar 60 po Nikvistu i da ispunjava uslov 
N = 12;

n=0:1/fs:tn;
x = sin(2*pi*10*n) + sin(2*pi*20*n) + sin(2*pi*30*n);

figure, subplot(211);
stem(n, x)
xlabel('n')
title('sinusi frekvencija 10,20,30 Hz')

X = fftshift(fft(x, N));
f = linspace(-fs/2, fs/2, N);
subplot(212);
stem(f, abs(X));
xlabel('f[Hz]')
title('Amplitudski spektar sinusa na 10, 20, 30 Hz')

%% 10
fs = 2100;
N = [21, 42, 120];
figure
n = 0:1/fs:1;
x = cos(2*pi*100*n) + cos(2*pi*105*n);
subplot(3, 2, 1), stem(n, abs(x))
subplot(3, 2, 3), stem(n, abs(x))
subplot(3, 2, 5), stem(n, abs(x))

X = fftshift(fft(x, N(1)));
f = linspace(-fs/2, fs/2, N(1));
subplot(3, 2, 2), stem(f, abs(X));
xlabel('f[Hz]')
title(['N = ', num2str(N(1))])

X = fftshift(fft(x, N(2)));
f = linspace(-fs/2, fs/2, N(2));
subplot(3, 2, 4), stem(f, abs(X));
title(['N = ', num2str(N(2))])

X = fftshift(fft(x, N(3)));
f = linspace(-fs/2, fs/2, N(3));
subplot(3, 2, 6), stem(f, abs(X));
title(['N = ', num2str(N(3))])

