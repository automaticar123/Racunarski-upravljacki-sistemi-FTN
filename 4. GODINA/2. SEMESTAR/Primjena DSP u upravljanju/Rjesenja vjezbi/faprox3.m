function f=faprox3(A, T, N, t)
    An= fseries3(A, T, N);
    f=ones(size(t))*An(1);
    omega0=2*pi/T;
    for i=1:N
        f=f+An(i+1)*cos(i*omega0*t);
    end
end