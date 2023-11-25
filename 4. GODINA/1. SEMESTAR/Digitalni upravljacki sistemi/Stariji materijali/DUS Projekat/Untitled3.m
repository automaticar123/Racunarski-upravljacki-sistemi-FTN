Tmax= 50;

W=1;
f=W/(2*pi);
t=0:0.001:Tmax;
y=sin(W*t);

Ws=2;
fs=Ws/(2*pi);
ts=0:1/fs:Tmax;
ys=sin(W*ts);

subplot(2,1,1);
plot(t,y);
hold on;
plot(ts,ys);
xlabel('Time[s]');
ylabel('Amplitude');
title('Original');
grid on;

subplot(2,1,2);
stem(ts,ys);
xlabel('Time[s]');
ylabel('Amplitude');
title('Sample');
grid on;

