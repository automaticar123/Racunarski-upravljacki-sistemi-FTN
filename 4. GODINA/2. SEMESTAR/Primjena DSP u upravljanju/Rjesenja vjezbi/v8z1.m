% Analiza LVN sistema pomocu Z transformacije
% kasnjenje
% f(k-k0) = z^-k0 * F(z)

%% 1

% y*(1-5/2*z^-1+z^-2) = x*(3-7*z^-1+5^-2);
% brojilac 3-7*z^-1+5*z^-2
% imenilac 1-5/2*z^-1+z^-2
a = [3, -7, 5];    % imenilac
b = [1, -5/2, 1];  % brojilac

nule = roots(b)
polovi = roots(a)


%% 2 a)
b = [1, -6, 4];
a = [1, -1, 0.33, -0.044, 0.002];

nule = roots(b);
polovi = roots(a);

zplane(nule, polovi);

H = tf(b, a, 0.01, 'variable', 'z') ;
% vreme odabiranja je razlika konti i disc
% kao promenljivu moze da se prosledi i 'z^-1'

[z, K] = zero(H)

% K=1,  z= 5.2361, 0.7639

%% 3 a)
% impulsni odziv filtra u 50 tacaka
b = 0.06769*[1 2 1];
a = [1 -1.142 0.4142];

n = 0:49;  % 50 tacaka
delta = (n == 0);
y = filter(b, a, delta); % vraca signal iste duzine kao pocetni

figure, stem(0:length(y)-1, y);
title("Impulsni odziv sistema")


%% b)
% 128 odbiraka signala y. nacrtati spektre signala na ulazu i izlazu
% filtra i obradzloziti dobijene grafike. O kakvom tipu filtra je rec?
clc
clear
fs = 3.55*3000; % nikvistova teorema
N = 128;
n = 0:1/fs:(N-1)/fs;
y = cos(2*pi*500*n)+cos(2*pi*750*n)+cos(2*pi*3000*n);
X = fftshift(fft(y, N));
f_osa = linspace(-fs/2, fs/2, N);

figure
stem((-length(X)/2):(length(X)/2-1), abs(X));
xlabel('n')

figure, subplot(311)
stem(f_osa, abs(X));
xlabel('f[Hz]')
title('amplitudski spektar signala na ulazu')

b = 0.06769*[1 2 1];
a = [1 -1.142 0.4142];

% racuna frekvencijsku karakteristiku filtra
% moduo h je amplitudska karakteristika
% faza h je fazna karakteristika
% W odgovarajuca osa diskretnih kruzniih frekvencija
[h, W] = freqz(b, a, N); 

w = W*fs;
frekv = w/(2*pi);
% subplot(312), plot(W, abs(h));
% xlabel('\Omega[rad]')
subplot(312), plot(frekv, abs(h));
xlabel('f[Hz]')
title('amplitudska karakteristika filtra');

y = filter(b, a, y);
Y = fftshift(fft(y));
subplot(313)
stem(f_osa, abs(Y));
xlabel('f[Hz]')
title('amplitudski spektar filtriranog signala');

%% 4
clc
clear

N = 256;
b = [0.0647, -0.0106, 0.0997, -0.0106, 0.0647];
a = [1, -2.28, 2.6543, -1.5624, 0.4215];
nule = roots(b);
polovi = roots(a);
zplane(nule, polovi)

[h, W] = freqz(b, a, N);
figure, subplot(311), plot(W, abs(h));
xlabel("\Omega[rad]")
title("Amplitudska karakteristika")

subplot(312), plot(W, angle(h));
xlabel("\Omega[rad]")
title("Fazna karakteriska")

% prikazati 50 vrednosti odbiraka impulsnog odziva sistema
n = 0:49;
delta = (n==0);
y = filter(b, a, delta);
subplot(313), stem(n, y)
xlabel("n")
title("impulsni odziv sistema")

%% 5 dz

b = [0.0186, -0.0294, 0.0731, -0.0396, 0.3045, 0.4528, 0.3045, 0.0396,...
    -0.0731, -0.0294, 0.0186];
a = 1;
H = tf(b, a, 0.01, 'variable', 'z^-1');
nule = roots(b);
polovi = roots(a);
zplane(nule, polovi);

[z, K]=zero(H);

n = 0:49;
delta = (n==0);
y = filter(b, a, delta);
figure, stem(0:(length(y)-1), y)

[h,W] = freqz(b, a, N);
figure, subplot(211), plot(W, abs(h));
title("Amplitudski spektar")
xlabel("\Omega[rad]")

subplot(212), plot(W, angle(h));
title("Fazni spektar")
xlabel("\Omega[rad]")

