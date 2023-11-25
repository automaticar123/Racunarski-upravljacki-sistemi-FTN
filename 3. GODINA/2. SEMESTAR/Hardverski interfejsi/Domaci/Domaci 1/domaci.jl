using ControlSystems
using Plots
using LinearAlgebra
using LaTeXStrings


function v_in(t)
    1 .* (t .< 7) + 0 .* (t .>= 7)
end

R1 = 100;
R2 = 100;
C = 5e-3;

s = tf("s");
G = (1/(C*R1)) / (s + (1/C)*(1/R1 + 1/R2));

vrijeme = "Vrijeme " * L"[s]"
napon = "Napon " * L"[V]"

t = 0:0.01:10;
y, t, x = lsim(G, (v_in(t))', t);
plot(t, v_in(t), xlabel=vrijeme,
                 xguidefontsize=20,
                 ylabel=napon,
                 yguidefontsize=20,
                 label=L"v_{in}(t)",
                 xticks=0:1:10,
                 yticks=0:0.1:1,
                 lw=3)
plot!(t, y', label=L"v_{out}(t)", lw=3)

