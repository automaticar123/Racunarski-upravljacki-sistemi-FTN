function [An] = fseries3(A2, T, N)
A0=0.25*A2;
An=ones(1, N+1);
An(1)=A0;
for i=2:N+1
    An(i)=8*A2*(sin((i-1)*pi/4))^2/pi^2/(i-1)^2;
end