import numpy as np
import skfuzzy as fuzz
import skfuzzy.control as ctrl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

temperature_universe = np.linspace(10, 40, 10)
humidity_universe = np.linspace(20, 100, 10)
fan_speed_universe = np.linspace(0, 100, 10)

temperature = ctrl.Antecedent(temperature_universe, 'temperature')
humidity = ctrl.Antecedent(humidity_universe, 'humidity')
fan_speed = ctrl.Consequent(fan_speed_universe, 'fan_speed')

temperature_names = ['cold', 'medium', 'hot']
humidity_names = ['less humid', 'mildly humid', 'very humid']
fan_speed_names = ['slow', 'medium', 'fast']

temperature['cold'] = fuzz.trapmf(temperature.universe, [10, 10, 15, 25])
temperature['medium'] = fuzz.trimf(temperature.universe, [20, 25, 30])
temperature['hot'] = fuzz.trapmf(temperature.universe, [24, 35, 40, 40])

humidity['less humid'] = fuzz.trapmf(humidity.universe, [20, 20, 30, 55])
humidity['mildly humid'] = fuzz.trimf(humidity.universe, [40, 60, 80])
humidity['very humid'] = fuzz.trapmf(humidity.universe, [65, 85, 100, 100])

fan_speed['slow'] = fuzz.trapmf(fan_speed.universe, [0, 0, 20, 30])
fan_speed['medium'] = fuzz.trapmf(fan_speed.universe, [30, 35, 65, 70])
fan_speed['fast'] = fuzz.trapmf(fan_speed.universe, [70, 80, 100, 100])

# Rules

rule0 = ctrl.Rule(temperature['cold'] & humidity['less humid'], fan_speed['slow'])
rule1 = ctrl.Rule(temperature['medium'] & humidity['less humid'], fan_speed['fast'])
rule2 = ctrl.Rule(temperature['hot'] & humidity['less humid'], fan_speed['fast'])

rule3 = ctrl.Rule(temperature['cold'] & humidity['mildly humid'], fan_speed['medium'])
rule4 = ctrl.Rule(temperature['medium'] & humidity['mildly humid'], fan_speed['fast'])
rule5 = ctrl.Rule(temperature['hot'] & humidity['mildly humid'], fan_speed['fast'])

rule6 = ctrl.Rule(temperature['cold'] & humidity['very humid'], fan_speed['fast'])
rule7 = ctrl.Rule(temperature['medium'] & humidity['very humid'], fan_speed['fast'])
rule8 = ctrl.Rule(temperature['hot'] & humidity['very humid'], fan_speed['fast'])

# System

system = ctrl.ControlSystem(rules = [rule0,
                                     rule1,
                                     rule2,
                                     rule3,
                                     rule4,
                                     rule5,
                                     rule6,
                                     rule7,
                                     rule8])

sim = ctrl.ControlSystemSimulation(system)

sim.input['temperature'] = 25
sim.input['humidity'] = 40

upsampled_temperature = np.linspace(10, 40, 21)
upsampled_humidity = np.linspace(20, 100, 21)
x, y = np.meshgrid(upsampled_temperature, upsampled_humidity)
z = np.zeros_like(x)

for i in range(0, 21):
    for j in range(0, 21):
        sim.input['temperature'] = x[i, j]
        sim.input['humidity'] = y[i, j]
        sim.compute()
        z[i, j] = sim.output['fan_speed']

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')

surf = ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis',
                       linewidth=0.4, antialiased=True)

cset = ax.contourf(x, y, z, zdir='z', offset=-2.5, cmap='viridis', alpha=0.5)
cset = ax.contourf(x, y, z, zdir='x', offset=3, cmap='viridis', alpha=0.5)
cset = ax.contourf(x, y, z, zdir='y', offset=3, cmap='viridis', alpha=0.5)

ax.view_init(30, 200)
plt.show()


