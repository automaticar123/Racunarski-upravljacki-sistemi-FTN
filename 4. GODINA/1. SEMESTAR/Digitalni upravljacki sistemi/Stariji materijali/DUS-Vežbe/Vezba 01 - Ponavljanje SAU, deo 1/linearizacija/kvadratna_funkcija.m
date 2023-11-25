start_point = -2;
end_point = 2;
step_size = 0.01;
x_vector = start_point:step_size:end_point;
x0 = 1;
y0 = x0^2;


% Izvod u tacki x0
y_diff = 2 * x0;

% Prava funkcija
y_vector = x_vector.^2;

% Linearizovana funkcija
y_linearized = y0 + y_diff*(x_vector - x0);

plot(x_vector, y_vector);
hold('on');
plot(x_vector, y_linearized);
grid('on');
legend('Prava funkcija', 'Linearizovana funkcija');