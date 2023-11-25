Rl = 1;
Rc = 1;
L = 100e-2;
C = 1e-5;
Rp = 100;

b1 = Rc*C;
b0 = 1;

a2 = L*(Rc*C/Rp + C);
a1 = (Rc*C + Rc*C/Rp + L/Rp);
a0 = Rl/Rp + 1;

G = tf([b1 b0], [a2 a1 a0]);
t = 0:0.01:1000;

bode(G)

%%
u = abs(sin(314*t));
y = lsim(G1, u, t);
hold on
plot(t, y)
plot(t, u)
