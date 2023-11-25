clear variables;

% Konstante
g = 9.81;
A0 = 0.01;
A1 = 2;
qu_max = 0.099;

% Odabir mirne radne tacke
h0 = 5;
q0 = A0 * sqrt(2*g*h0);

% Racunanje matrica linearnog modela u prostoru stanja
A = -A0/A1 * (g / sqrt(2*g*h0));
B = 1/A1;
C = 1;
D = 0;