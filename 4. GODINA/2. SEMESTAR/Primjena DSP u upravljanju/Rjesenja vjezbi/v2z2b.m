t=-2.5:0.01:2.5;
A=1;
alfa=1;
T=1;
N_values=[0,1,2,5,10,50,100,500,1000];
rows=2;
cols=5;

t1=-T/2:0.01:T/2;
figure;
%f_true = A*exp(alfa*t);
%subplot(rows, cols, 1);
%plot(t, f_true);
f_true = zeros(size(t));

for i = 1:length(t)
    t2 = t(i);
    period = floor((t2 + T/2) / T);
    t_adjusted = t2 - period * T;
    if t_adjusted >= -T/2 && t_adjusted <= T/2
        f_true(i) = A * exp(alfa * t_adjusted);
    else
        f_true(i) = 0;
    end
end

subplot(rows, cols, 1);
plot(t, f_true);

for i = 1:length(N_values)
    f = faprox1(A, alfa, T, N_values(i), t);
    subplot(rows,cols,i+1);
    plot(t, f, t, f_true);
    title(["N=", num2str(N_values(i))]);
end