A2_v=[1,2];
T_v=[1,2];
N=30;
frekv=0:1/T:N/T;
i=1;
for A2=A2_v
    for T=T_v
        An=fseries3(A2, T, N);
        subplot(2, 2, i);
        i=i+1;
        stem(frekv, An);
        title("An");
    end
end
