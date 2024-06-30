%% 1
% Reailzovati Batervortov NF filtar. Filtar treba da zadovolji sledeće specifikacije:
% granična učestanost propusnog opsega 
fp = 500;
% granična učestanost nepropusnog opsega
fa = 600;
% maksimalno slabljenje u propusnom opsegu
alphap = 1; %dB
% minimalno slabljenje u nepropusnom opsegu
alphaa = 25; %dB

fs = 6000;
% Nacrtati amplitudsko-frekvencijsku karakteristiku filtra na osi učestanosti u Hz.
% Filtrirati signal x
% Nacrtati signal na vremenskoj osi na ulazu i izlazu filtra kao i amplitudski spektar
% signala na ulazu i na izlazu filtra i obrazložiti dobijene grafike

Wp = fp1/fs*2; 
Ws = fa2/fs*2;
Rp = alphap;
Rs = alphaa - alphap;

[n, W] = buttord(Wp, Ws, Rp, Rs);
[b, a] = butter(n, W, 'low');      % low, high, stop, bandpass
[h, Wd] = freqz(b, a, 1000);
w = fs*Wd;
frekv = w/(2*pi);
figure
plot(frekv, abs(h));
xlabel("f[Hz]")
title("Amplitudska karakteristika filtra")

t = 0:1/fs:10;
x = 5 + 7*cos(2*pi*800*t);
figure, subplot(221)
plot(t, x)
xlabel('t[s]')
title("Signal pre filtriranja")
xlim([0, 0.05])

X = fftshift(fft(x));
f_osa = linspace(-fs/2, fs/2, length(X));
subplot(222), stem(f_osa, abs(X));
title("Amplitudski spektar signala")
xlabel('f[Hz]')

y = filter(b,a, x);
subplot(223)
plot(t, y);
xlabel('t[s]')
title("Signal posle filtriranja")
xlim([0, 0.05]);

Y = fftshift(fft(y));
subplot(224), stem(f_osa, abs(Y));
title("Amplitudski spektar filtriranog signala")
xlabel('f[Hz]')


%% 2 
% Realizovati inverzni Čebiševljev filtar propusnik opsega (PO) učestanosti. 
% Filtar treba da zadovolji sledeće specifikacije:
fp1 = 340;
fp2 = 500;
fa1 = 240;
fa2 = 600;
alphap = 1;
alphaa = 25;
% fs = 3000;
fs = 8000;

% Nacrtati amplitudsko-frekvencijsku karakteristiku filtra na osi učestanosti u Hz.
% Filtrirati signal x
% Nacrtati signal na vremenskoj osi na ulazu i izlazu filtra kao i amplitudski
% spektar signala na ulazu i na izlazu filtra i obrazložiti dobijene grafike.

Wp1 = fp1/fs*2; 
Wp2 = fp2/fs*2; 
Ws1 = fa1/fs*2;
Ws2 = fa2/fs*2;
Rp = alphap;
Rs = alphaa - alphap;
[n, Wn] = cheb2ord([Wp1, Wp2], [Ws1, Ws2], Rp, Rs);
[b, a] = cheby2(n, Rs, Wn, 'bandpass');

[h, Wd] = freqz(b, a, 200);
w = fs*Wd;
frekv = w/(2*pi);
figure
plot(frekv, abs(h));
xlabel("f[Hz]")
title("Amplitudska karakteristika filtra")

t = 0:1/fs:10;
x = sin(2*pi*400*t) + sin(2*pi*800*t);
figure, subplot(221)
plot(t, x)
xlabel('t[s]')
title("Signal pre filtriranja")
xlim([0, 0.05])

X = fftshift(fft(x));
f_osa = linspace(-fs/2, fs/2, length(X));
subplot(222), stem(f_osa, abs(X));
title("Amplitudski spektar signala")
xlabel('f[Hz]')

y = filter(b,a, x);
subplot(223)
plot(t, y);
xlabel('t[s]')
title("Signal posle filtriranja")
xlim([0, 0.05]);

Y = fftshift(fft(y));
subplot(224), stem(f_osa, abs(Y));
title("Amplitudski spektar filtriranog signala")
xlabel('f[Hz]')



