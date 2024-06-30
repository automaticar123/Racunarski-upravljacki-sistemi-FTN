function [f] = faprox1(A, alfa, T, N, t)
[An, Fn] = fseries1(A, alfa, T, N);
f = ones(size(t))*An(1,1);
omega = 2*pi/T;
for i=1:N
    f=f+An(1, i + 1)*cos(i*omega*t+Fn(1, i + 1));
end
end