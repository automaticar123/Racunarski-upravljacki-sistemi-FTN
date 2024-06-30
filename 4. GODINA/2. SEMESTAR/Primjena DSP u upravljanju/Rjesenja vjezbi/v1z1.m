%% UVOD 
A = magic(3);
B = eye(3);
if size(A)==size(B)
    C=A+B;
else
    disp("Greska");
end
%% zadatak 1
n = 5;
faktorijel = 1;
for i = 1:n
    faktorijel = faktorijel*i;
end

faktorijel

%% zadatak 2
mat = zeros(5);
for i = 1:5
    for j=1:5        
        if i+j==6
            mat(i,j) = 6;
        end
        if i == j
            mat(i,j) = 2;
        end
    end
end
mat
%% zadatak 3 a
A = magic(5);
minimalni = inf;
for i = 1:5
    for j=1:5   
        if A(i,j) < minimalni
            minimalni = A(i,j);
            vrsta = i;
            kolona = j;
        end
    end
end
A
minimalni
vrsta
kolona

min(min(A))
% ili min(A(:))

%% zad3 b
I = eye(5);
maksimalni = -inf;
for i = 1:5
    for j=1:5        
        if i == j
            if A(i,j)>maksimalni
               maksimalni = A(i, j);
               kolona = j;
               vrsta = i;
            end
        end
    end
end

maksimalni
vrsta
kolona

%% zad3 c
zbir = 0;
for i = 1:5
    for j=1:5        
        if rem((i + j), 2) == 0
            zbir = zbir+ A(i,j);
        end
    end
end
zbir

%% zad 4
niz = rand(1, 25);
niz = niz*100;
max(niz)
min(niz)
mean(niz)

%% zad 5a
% isto uraditi za trapez, pravu..
t = 0:0.01:10;
x = 4*sin(2*pi*t);
plot(t, x)

%% b
x = 4*sin(2*pi*t+pi/2);
plot(t, x)

%% c
x = 4*sin(pi*t+pi/2);
plot(t, x)

%% sve zajedno
t = 0:0.01:10;
x = 4*sin(2*pi*t);
subplot(3, 1, 1), plot(t, x, 'b--');
xlabel('t(s)')
ylabel('y(s)')
title("Signal 4sin(2pi*t)")
x = 4*sin(2*pi*t+pi/2);
subplot(3, 1, 2), plot(t, x, 'r');
xlabel('t(s)')
ylabel('y(s)')
title("Signal 4*sin(2*pi*t+pi/2))")
x = 4*sin(pi*t+pi/2);
subplot(3, 1, 3), plot(t, x, 'g-.');
xlabel('t(s)')
ylabel('y(s)')
title("Signal 4*sin(pi*t+pi/2)")

%% d
t = 0:0.01:2;
x = 2*sin(6*pi*t + pi/4);
subplot(2, 2, 1), plot(t, x, 'r--');
x1 = 3*sin(t*(2*pi)/3);
subplot(2, 2, 2), plot(t, x1, 'black');
x2 = 3*sin(3*pi*t+pi);
subplot(2, 2, 3), plot(t, x2, 'g-.');
x3 = 2*sin(2*pi*t+pi/2); 
subplot(2, 2, 4), plot(t, x3, 'b');

%% c

t = -5:0.01:5;
u = heaviside(t);
u2= heaviside(t-3);
x = u-u2;
subplot(3, 1, 1), plot(t, x);
grid on
ylim([-1, 1.5])

x_inv = heaviside(-t)-heaviside(-t-3);
even = (x+x_inv) /2;
subplot(3, 1, 2), plot(t, even);
grid on
ylim([-1, 1.5])

odd = (x-x_inv) /2;
subplot(3, 1, 3), plot(t, odd);
grid on
ylim([-1, 1.5])

%% d.1
s = [-5, -2, -1, 0, 1, 2, 3, 7];
n = [0, 0, 1, 0, 1, 1, 0, 0];
plot(s, n)
%% d.2
t = -5:0.01:5;
x1=(t+2).*(heaviside(t+2)-heaviside(t+1));
x2=(-t).*(heaviside(t+1)-heaviside(t));
x3=t.*(heaviside(t)-heaviside(t-1));
x4=heaviside(t-1)-heaviside(t-2);
x5=(-t+3).*(heaviside(t-2)-heaviside(t-3));
x=x1+x2+x3+x4+x5;
plot(t, x)
ylim([-0.5, 1.5])












