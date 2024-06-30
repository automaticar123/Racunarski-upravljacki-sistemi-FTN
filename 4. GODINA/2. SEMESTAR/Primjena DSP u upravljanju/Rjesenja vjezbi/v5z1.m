% KONVOLUCIJA
% a[n]*b[n] = sum(a[k]b[n-k])  k=(-inf, inf)
% ili u MATLAB-u conv(a, b)
% ako prvi signal ima duzinu Na, a drugi Nb, 
% duzina signala konvolucije bice duzine Na+Nb-1

% IMPULSNI ODZIV
% Odziv sistema na delta impuls na ulazu
% IMPULSNI_ODZIV[n] = delta[n]*sistem
% Y[n] = conv(X[n], IMPULSNI_ODZIV[n])

% ** conv se koristi i za mnozenje polinoma

%% 1
x1 = [4, 3, -6, 8, -4];
x2 = [1, 1, -1, 2, -4];
y = conv(x1, x2);
Ny = length(x1) + length(x2) - 1;
n = 0:Ny-1;
figure, stem(n, y);
xlabel('n');
ylabel("y[n] = x1[n]*x2[n]")

%% 2  
% impulsni odziv
n = 0:10;
h = (n>=0) - ((n-3)>=0);
x = h;
figure, subplot(311);
stem(n, x);
xlabel("n")
ylabel("x[n]")

subplot(312);
stem(n, h);
xlabel("n")
ylabel("h[n]")

y = conv(x, h);
ny = 0:length(y)-1;
subplot(313);
stem(ny, y);
xlabel("n")
ylabel("h[n]*x[n]")

%% 3
% redna veza --> h1 --> h2 --> postaje conv(h1, h2)
% paralelne veza 
% --> h1 --> + -->   postaje h1+h2
%  |--> h2 --^
h1 = [0.5, 0.25, 0.125, -4];
h2 = [1, 0.5, 0.25, 0.0625];
n = 0:3;
figure, subplot(221);
stem(n, h1);
ylabel("h1")
subplot(222);
stem(n, h2);
ylabel("h2")

% redna veza
h3 = conv(h1, h2);
nh3 = 0:length(h3)-1;
subplot(223)
stem(nh3, h3)
ylabel('h1*h2')
title('redna veza')

% paralelna veza
h4 = h1+h2;
subplot(224)
stem(n, h4)
ylabel('h1+h2')
title('paralelna veza')


%% 6 (4 i 5 preskociti)
% Izracunati izlaz sistema sa slike
n = 0:3;
h1 = (n>=0)-((n-2)>=0);
h2 = [1, 2, 0, 0]; % dodate de nule kako bi duzine h1 i h2 bile iste
h3 = [2, 2, 1, 2];
x = [2, 1, 8];
%y = conv(x, conv((h1+h2), h3));
y = conv(h3, conv(x, (h1+h2)));

stem(0:length(y)-1, y)

%% postepeno
n = 0:3;
h1 = (n>=0)-((n-2)>=0);
h2 = [1, 2, 0, 0];
h3 = [2, 2, 1, 2];
x = [2, 1, 8];
x1 = conv(x, h1);
x2 = conv(x, h2);
x3 = x1+x2;
y = conv(x3, h3);
ny = 0:length(y)-1;
figure, stem(ny, y);

%% 7 
n = 0:3;
x = (n==0) - 0.1*((n-1)==0) + 4*((n-2)==0);
r1 = (n==0) - 5*((n-1)==0) + 9*((n-2)==0)+ 3 *((n-4)==0);
r2 = -(n==0);
r3 = (n==0) - 2*((n-1)==0) + 5*((n-2)==0) -((n-3)==0);

x1 = conv(x, conv(r1, (r2+r3)));
% x i x1 moraju biti iste velicine za oduzimanje
% dodamo onoliko nula koliko fali 

x_pov = (n==0);
x_pov = conv(x, x_pov);
x_pov = [x_pov zeros(1, length(x1)-length(x_pov))];
y = conv((x1 - x_pov), r1);
zm=y;
figure, stem(0:length(y)-1, y)

%% 8
n = 0:3;
x = (n==0) - 2*((n-1)==0) + 4*((n-2)==0);
r1 = (n==0) - 5*((n-1)==0) + 9*((n-2)==0)+ 3 *((n-3)==0);
r2 = -1*(n==0);
r3 = (n==0) - 2*((n-1)==0) + 5*((n-2)==0) -((n-3)==0);

x3 = conv(x, r3);
x2 = conv(x, r2);
x1 = conv(x2, r1);
x4 = -[x3 zeros(1, length(x1)- length(x3))] + x1 + [x zeros(1, length(x1)-length(x))];
y = conv(x4, r1);
ny = 0:length(y)-1;
stem(ny, y);





















