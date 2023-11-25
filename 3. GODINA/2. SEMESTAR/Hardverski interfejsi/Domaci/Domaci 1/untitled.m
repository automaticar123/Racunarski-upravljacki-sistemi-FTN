syms t s
R1 = 100;
R2 = 100;
C = 5e-3;

G = (1/(R1*C))/(s + (1/C)*(1/R1 + 1/R2));

v_in = heaviside(t) - heaviside(t-7);
V_in = laplace(v_in);

V_out = G*V_in;
v_out = matlabFunction(ilaplace(V_out));
t1 = 0:0.01:10;

hold on
grid on
v_in1 = heaviside(t1) - heaviside(t1-7);
plot(t1, v_in1, 'LineWidth', 3)
plot(t1, v_out(t1), 'LineWidth', 3)
xlabel({'Vrijeme [{\it s} ]'}, 'FontSize', 18, 'FontName', 'Times New Roman')
ylabel({'Napon [{\it V} ]'}, 'FontSize', 18, 'FontName', 'Times New Roman')

legend({'\it v_{in}(t)', '\it v_{out}(t)'}, 'FontSize', 18, 'FontName', 'Times New Roman')

%%

R1 = 100;
R2 = 100;
C = 5e-3;
G = tf([1/(R1*C)], [1, (1/C)*(1/R1 + 1/R2)]);
bode(G);
bandwidth(G)