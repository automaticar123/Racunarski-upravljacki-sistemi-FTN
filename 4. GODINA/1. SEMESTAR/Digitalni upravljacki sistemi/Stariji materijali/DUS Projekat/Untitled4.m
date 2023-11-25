clear variables
close all

% Signal ucitan iz fajla je vec odbirkovan frekvencijom 48000 Hz. Sada
% zelimo da pokazemo sta bi se dogodilo da je signal odbirkovan manjom
% frekvencijom, na primer 3000 Hz. Ovo postizemo uzimanjem svakog osmog
% odbirka iz originalno odbirkovanog signala. Striktno govoreci, ovaj
% proces se ne zove odbirkovanje (jer je signal vec odbirkovan), vec
% decimacija.

% Ucitavamo uz datoteke signal i njegovu frekvenciju odbirkovanja u Hercima
%T1 = 1 / sampling_frequency1;
signal1 = signal1(:, 1);

% Zeljena frekcencija i perioda odabiranja
target_frequency = 3000;
T2 = 1 / target_frequency;

% Koliko puta manje odbiraka treba da uzimamo. Pretpostavljamo da je ovo
% ceo broj :)
ratio = sampling_frequency1 / target_frequency;

% 'Odbirkujemo' signal manjom frekvencijom (odnosno vrsimo decimaciju)
signal2 = signal1(1:ratio:end);
n2 = length(signal2);

% Racunamo Furijeovu transformaciju odbirkovanog signala
spektar2_kompleksni = fft(signal2);

% Amplitudski spektar signala dobijamo uzimanjem modua kompleksnog spektra
spektar2_amplitudski = abs(spektar2_kompleksni);

% Da bismo mogli da pravilno obelezimo odgovarajuce frekvencije na x-osi
% grafika, moramo da napravimo odgovarajuci niz vrednosti frekvencija. 
frequency_array2 = linspace(0, target_frequency, n2);

% Zelimo da dobijeni spektar uporedimo sa donjim delom originalnog spektra,
% i uverimo se da su alijasi nepovratno unistili nase informacije. Zbog
% toga cemo paralelno iscrtati i donji deo originalnog spektra.
spektar1_amplitudski = abs(fft(signal1));
donji_deo_spektra = spektar1_amplitudski(1:n2);

% Crtamo amplitudske spektre
subplot(2, 1, 1);
plot(frequency_array2, donji_deo_spektra);
title('Dodnji deo aplitudskog spektra originalnog zasumljenog signala');
xlabel('Frekvencija');
ylabel('Amplituda');

subplot(2, 1, 2);
plot(frequency_array2, spektar2_amplitudski);
title('Amplitudski spektar decimiranog zasumljenog signala');
xlabel('Frekvencija');
ylabel('Amplituda');