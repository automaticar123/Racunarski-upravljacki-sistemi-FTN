function [An,Fi] = fseries1(A, alfa, T, N)

A0 = A*(exp(alfa*T/2)-exp(-alfa*T/2))/T/alfa;

An = zeros(1, N);
Fi = zeros(1, N);

An(1) = A0;
Fi(1) = 0;
omega0 = 2*pi/T;
for i = 2:N+1
  An(i) = 2*A*(exp(alfa*T/2)-exp(-alfa*T/2))/T/sqrt(alfa^2+(i-1)^2*omega0^2);
  Fi(i) = (i-1)*pi+atan((i-1)*omega0/alfa) ;
end

end