import numpy as np
import skfuzzy as fuzz
from skfuzzy import control
import matplotlib.pyplot as plt

temperature_universe = np.arange(10, 41, 1)
humidity_universe = np.arange(20, 101, 1)
fan_speed_universe = np.arange(0, 101, 1)

temperature = control.Antecedent(temperature_universe, 'temperature')
humidity = control.Antecedent(humidity_universe, 'humidity')
fan_speed = control.Consequent(fan_speed_universe, 'fan_speed')

temperature['low'] = fuzz.trimf(temperature_universe, [10, 10, 20])
temperature['medium'] = fuzz.trimf(temperature_universe, [15, 25, 32])
temperature['high'] = fuzz.trimf(temperature_universe, [23, 40, 40])

humidity['low'] = fuzz.trimf(humidity_universe, [20, 20, 50])
humidity['medium'] = fuzz.trimf(humidity_universe, [30, 50, 80])
humidity['high'] = fuzz.trimf(humidity_universe, [60, 100, 100])

fan_speed['low'] = fuzz.trimf(fan_speed_universe, [0, 0, 30])
fan_speed['medium'] = fuzz.trimf(fan_speed_universe, [15, 50, 70])
fan_speed['high'] = fuzz.trimf(fan_speed_universe, [60, 100, 100])

rule1 = control.Rule(temperature['low'] & humidity['low'], fan_speed['low'])
rule2 = control.Rule(temperature['low'] & humidity['medium'], fan_speed['medium'])
rule3 = control.Rule(temperature['low'] & humidity['high'], fan_speed['medium'])
rule4 = control.Rule(temperature['medium'] & humidity['low'], fan_speed['medium'])
rule5 = control.Rule(temperature['medium'] & humidity['medium'], fan_speed['medium'])
rule6 = control.Rule(temperature['medium'] & humidity['high'], fan_speed['high'])
rule7 = control.Rule(temperature['high'] & humidity['low'], fan_speed['high'])
rule8 = control.Rule(temperature['high'] & humidity['medium'], fan_speed['high'])
rule9 = control.Rule(temperature['high'] & humidity['high'], fan_speed['high'])

system = control.ControlSystem([rule1, rule2, rule3, 
                                rule4, rule5, rule6,
                                rule7, rule8, rule9])

system_sim = control.ControlSystemSimulation(system)

system_sim.input['temperature'] = 15
system_sim.input['humidity'] = 20
system_sim.compute()

print(system_sim.output['fan_speed'])

x, y = np.meshgrid(temperature_universe, humidity_universe)
z = np.zeros_like(x)

for i in range(80):
    for j in range(30):
        system_sim.input['temperature'] = x[i, j]
        system_sim.input['humidity'] = y[i, j]
        system_sim.compute()
        z[i, j] = system_sim.output['fan_speed']

from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis',
                       linewidth=0.4, antialiased=True)

cset = ax.contourf(x, y, z, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
cset = ax.contourf(x, y, z, zdir='x', offset=3, cmap='viridis', alpha=0.5)
cset = ax.contourf(x, y, z, zdir='y', offset=3, cmap='viridis', alpha=0.5)

ax.view_init(30, 200)

plt.show()