%% pod a)
fs = 6000;
t = 0:1/fs:0.2;
y = cos(2*pi*50*t) + cos(2*pi*1500*t) + cos(2*pi*2500*t);

Y = fftshift(fft(y));
frekv = linspace(-fs/2, fs/2, length(Y));



% NF, eliminise f3 od 2500hz
r = 0.5;
fp = 1500; % granicna frekvencija koju zelimo da zadrzimo
teta = 2*pi*fp/fs;
b = [1, 2, 1];                     % z^2 + 2*z + 1
a = [1, -2*r*cos(teta), r^2];      % z^2 - 2*r*cos(teta)*z + r^2
zplane(roots(b), roots(a));

[h, W] = freqz(b, a, 500);
f_osa = W*fs/2/pi;

figure, subplot(411), stem(t, y)
title("Pocetni signal")
subplot(412), stem(frekv, abs(Y));
title("Amplitudski spektar pocetnog signala")
subplot(413), plot(f_osa, abs(h))
title("Amplitudski spektar filtra")
xlabel('f[Hz]')

y_filtr = filter(b, a, y);
Y_filtr = fftshift(fft(y_filtr));
subplot(414), stem(frekv, abs(Y_filtr))
title("Amplitudski spektar filtriranog signala")

%% pod b)
% takodje NF, ali elimise f2 i f3, od 1500Hz
fs = 6000;
t = 0:1/fs:0.2;
y = cos(2*pi*50*t) + cos(2*pi*1500*t) + cos(2*pi*2500*t);

Y = fftshift(fft(y));
frekv = linspace(-fs/2, fs/2, length(Y));

r = 0.5;
fp = 50; % granicna frekvencija koju zelimo da zadrzimo
teta = 2*pi*fp/fs;
b = [1, 2, 1];                     % z^2 + 2*z + 1
a = [1, -2*r*cos(teta), r^2];      % z^2 - 2*r*cos(teta)*z + r^2
zplane(roots(b), roots(a));

[h, W] = freqz(b, a, 500);
f_osa = W*fs/2/pi;

figure, subplot(411), stem(t, y)
title("Pocetni signal")
subplot(412), stem(frekv, abs(Y));
title("Amplitudski spektar pocetnog signala")
subplot(413), plot(f_osa, abs(h))
title("Amplitudski spektar filtra")
xlabel('f[Hz]')

y_filtr = filter(b, a, y);
Y_filtr = fftshift(fft(y_filtr));
subplot(414), stem(frekv, abs(Y_filtr))
title("Amplitudski spektar filtriranog signala")

%% pod c)
% PO, propusta f2 
fs = 6000;
t = 0:1/fs:0.2;
y = cos(2*pi*50*t) + cos(2*pi*1500*t) + cos(2*pi*2500*t);

Y = fftshift(fft(y));
frekv = linspace(-fs/2, fs/2, length(Y));

r = 0.9;
fp = 1500;               % granicna frekvencija koju zelimo da zadrzimo
teta = 2*pi*fp/fs;
b = [1, 0, -1];                     % z^2 - 1
a = [1, -2*r*cos(teta), r^2];      % z^2 - 2*r*cos(teta)*z + r^2
zplane(roots(b), roots(a));

[h, W] = freqz(b, a, 500);
f_osa = W*fs/2/pi;

figure, subplot(411), stem(t, y)
title("Pocetni signal")
subplot(412), stem(frekv, abs(Y));
title("Amplitudski spektar pocetnog signala")
subplot(413), plot(f_osa, abs(h))
title("Amplitudski spektar filtra")
xlabel('f[Hz]')

y_filtr = filter(b, a, y);
Y_filtr = fftshift(fft(y_filtr));
subplot(414), stem(frekv, abs(Y_filtr))
title("Amplitudski spektar filtriranog signala")

%% pod d)
fs = 6000;
t = 0:1/fs:0.2;
y = cos(2*pi*50*t) + cos(2*pi*1500*t) + cos(2*pi*2500*t);

Y = fftshift(fft(y));
frekv = linspace(-fs/2, fs/2, length(Y));

r = 0.5;
fp = 1500; % granicna frekvencija koju zelimo da zadrzimo
teta = 2*pi*fp/fs;
b = [1, 2, 1];                     % z^2 + 2*z + 1
a = [1, -2*r*cos(teta), r^2];      % z^2 - 2*r*cos(teta)*z + r^2
zplane(roots(b), roots(a));

[h, W] = freqz(b, a, 500);
f_osa = W*fs/2/pi;

figure, subplot(411), stem(t, y)
title("Pocetni signal")
subplot(412), stem(frekv, abs(Y));
title("Amplitudski spektar pocetnog signala")
subplot(413), plot(f_osa, abs(h))
title("Amplitudski spektar filtra")
xlabel('f[Hz]')

y_filtr = filter(b, a, y);
Y_filtr = fftshift(fft(y_filtr));
subplot(414), stem(frekv, abs(Y_filtr))
title("Amplitudski spektar filtriranog signala")

%% NPO
clc;clear;
fs = 6000;
t = 0:1/fs:0.2;
y = cos(2*pi*50*t) + cos(2*pi*1500*t) + cos(2*pi*2500*t);

Y = fftshift(fft(y));
frekv = linspace(-fs/2, fs/2, length(Y));

% PNO eliminise f2
r1 = 0.5;
r2 = 0.9;
fp = 1500; % granicna frekvencija koju zelimo da zadrzimo
teta = 2*pi*fp/fs;
b = [1, -2*r2*cos(teta), r2^2];                    
%a = [1, -2*r1*cos(teta2), r1^2];      % z^2 - 2*r*cos(teta)*z + r^2
a = [1, 0, -r1^2];
zplane(roots(b), roots(a));

[h, W] = freqz(b, a, 500);
f_osa = W*fs/2/pi;

figure, subplot(411), stem(t, y)
title("Pocetni signal")
subplot(412), stem(frekv, abs(Y));
title("Amplitudski spektar pocetnog signala")
subplot(413), plot(f_osa, abs(h))
title("Amplitudski spektar filtra")
xlabel('f[Hz]')

y_filtr = filter(b, a, y);
Y_filtr = fftshift(fft(y_filtr));
subplot(414), stem(frekv, abs(Y_filtr))
title("Amplitudski spektar filtriranog signala")
