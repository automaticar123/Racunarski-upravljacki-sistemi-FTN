import skfuzzy as fuzz
import numpy as np
from skfuzzy.control import ControlSystem, Rule, ControlSystemSimulation, Antecedent, Consequent
import matplotlib.pyplot as plt

temperature_universe = np.arange(10, 41, 1)
humidity_universe = np.arange(20, 100, 1)
fan_speed_universe = np.arange(0, 101, 1)

temperature = Antecedent(temperature_universe, 'temperature')
humidity = Antecedent(humidity_universe, 'humidity')
fan_speed = Consequent(fan_speed_universe, 'fan_speed')

temperature['low'] = fuzz.trapmf(temperature_universe, [10, 10, 16.5, 21])
temperature['medium'] = fuzz.trimf(temperature_universe, [15, 25, 33])
temperature['high'] = fuzz.trapmf(temperature_universe, [27, 30, 40, 40])

humidity['low'] = fuzz.trapmf(humidity_universe, [20, 20, 40, 60])
humidity['medium'] = fuzz.trimf(humidity_universe, [30, 44, 70])
humidity['high'] = fuzz.trapmf(humidity_universe, [65, 80, 100, 100])

fan_speed['low'] = fuzz.trapmf(fan_speed_universe, [0, 0, 10, 22])
fan_speed['medium'] = fuzz.trimf(fan_speed_universe, [16, 53, 70])
fan_speed['high'] = fuzz.trapmf(fan_speed_universe, [80, 90, 100, 100])

rule1 = Rule(temperature['low'] & humidity['low'], fan_speed['low'])
rule2 = Rule(temperature['low'] & humidity['medium'], fan_speed['low'])
rule3 = Rule(temperature['low'] & humidity['high'], fan_speed['medium'])
rule4 = Rule(temperature['medium'] & humidity['low'], fan_speed['low'])
rule5 = Rule(temperature['medium'] & humidity['medium'], fan_speed['medium'])
rule6 = Rule(temperature['medium'] & humidity['high'], fan_speed['high'])
rule7 = Rule(temperature['high'] & humidity['low'], fan_speed['medium'])
rule8 = Rule(temperature['high'] & humidity['medium'], fan_speed['high'])
rule9 = Rule(temperature['high'] & humidity['high'], fan_speed['high'])

sys = ControlSystem([rule1, rule2, rule3,
                     rule4, rule5, rule6,
                     rule7, rule8, rule9])

sys_sim = ControlSystemSimulation(sys)

temp_input = [14, 33, 16, 11, 28]
hum_input = [54, 61, 49, 85, 36]

for i in range(len(temp_input)):
    sys_sim.input['temperature'] = temp_input[i]
    sys_sim.input['humidity'] = hum_input[i]
    sys_sim.compute()
    print(sys_sim.output['fan_speed']) 

x, y = np.meshgrid(temperature_universe, humidity_universe)
z = np.zeros_like(x)

for i in range(80):
    for j in range(30):
        sys_sim.input['temperature'] = x[i, j]
        sys_sim.input['humidity'] = y[i, j]
        sys_sim.compute()
        z[i, j] = sys_sim.output['fan_speed']

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
