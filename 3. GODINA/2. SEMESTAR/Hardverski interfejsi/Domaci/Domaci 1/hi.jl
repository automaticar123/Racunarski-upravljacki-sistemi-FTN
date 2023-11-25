using ControlSystems, Plots, LinearAlgebra

function v_in(t)
    return abs.(sin.(314 .* t))
end

Rt = 10;
Rd = 2;
Rl = 1;
Rc = 1;
Rp = 100;
R = Rt + Rd + Rl;
L = 1e-3;
C = 60e-3;

a = (Rc*C*L)/(Rp);
b = Rc*C + (R*Rc*C)/(Rp) + L/Rp + L*C;
c = R*C + R/Rp + 1;

G  = tf([Rc*C, 1], [a, b, c]);
t = 0:0.01:100
#bodeplot(G)

w = L/Rp + L*C
println(1/w)
#Gsimple = tf([1], [L/Rp + L*C, 1])
#bodeplot(Gsimple)

y, t, x = lsim(G, (v_in(t))', t);
plot(t, y')

