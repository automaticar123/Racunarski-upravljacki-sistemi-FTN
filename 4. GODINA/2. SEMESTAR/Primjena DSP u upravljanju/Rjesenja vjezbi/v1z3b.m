T = 1;
interval = -T/4:0.01:T/4; 
A2 = 2;
N_values = [0, 1, 2, 5, 10, 50, 100, 500, 1000];

t=-2.5:0.01:2.5;
f_true=zeros(size(t));

for i=1:length(t)
    tp=t(i);
    period = floor((tp + T/4) / T);
    t_adjusted = tp - period * T;
    if t_adjusted >= -T/4 && t_adjusted <= T/4
        f_true(i) = A2 * (1-(4*abs(t_adjusted)/T));
    else
        f_true(i) = 0;
    end
end

subplot(2, 5, 1);
plot(t, f_true);

%h=A2 * (1-(4*abs(interval)/T));
%subplot(2, 5, 2);
%plot(interval, h);

for i=1:length(N_values)
    f = faprox3(A2, T, N_values(i), t);
    subplot(2, 5, i+1)
    plot(t, f)
    title(["N=", N_values(i)])
end







