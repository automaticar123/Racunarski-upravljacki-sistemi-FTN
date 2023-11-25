import numpy as np
import skfuzzy as fuzz
from skfuzzy import control
import matplotlib.pyplot as plt

temperature_universe = np.arange(10, 41, 1)
humidity_universe = np.arange(20, 101, 1)
fan_speed_universe = np.arange(0, 101, 1)

temperature_low = fuzz.trimf(temperature_universe, [10, 10, 20])
temperature_medium = fuzz.trimf(temperature_universe, [15, 25, 32])
temperature_high = fuzz.trimf(temperature_universe, [23, 40, 40])

humidity_low = fuzz.trimf(humidity_universe, [20, 20, 50])
humidity_medium = fuzz.trimf(humidity_universe, [30, 50, 80])
humidity_high = fuzz.trimf(humidity_universe, [60, 100, 100])

fan_speed_low = fuzz.trimf(fan_speed_universe, [0, 0, 30])
fan_speed_medium = fuzz.trimf(fan_speed_universe, [15, 50, 70])
fan_speed_high = fuzz.trimf(fan_speed_universe, [60, 100, 100])

x, y = np.meshgrid(temperature_universe, humidity_universe)
z = np.zeros_like(x)

for i in humidity_universe:
    for j in temperature_universe:
        temperature_low_val = fuzz.interp_membership(temperature_universe, temperature_low, j)
        temperature_medium_val = fuzz.interp_membership(temperature_universe, temperature_medium, j)
        temperature_high_val = fuzz.interp_membership(temperature_universe, temperature_high, j)

        humidity_low_val = fuzz.interp_membership(humidity_universe, humidity_low, i)
        humidity_medium_val = fuzz.interp_membership(humidity_universe, humidity_medium, i)
        humidity_high_val = fuzz.interp_membership(humidity_universe, humidity_high, i)

        rules_act = []
        # 1st rule
        tlhl = np.fmin(temperature_low_val, humidity_low_val)
        rules_act.append(np.fmin(tlhl, fan_speed_low))

        # 2nd rule
        tlhm = np.fmin(temperature_low_val, humidity_medium_val)
        rules_act.append(np.fmin(tlhm, fan_speed_medium))

        # 3rd rule
        tlhh = np.fmin(temperature_low_val, humidity_high_val)
        rules_act.append(np.fmin(tlhh, fan_speed_medium))

        # 4th rule
        tmhl = np.fmin(temperature_medium_val, humidity_low_val)
        rules_act.append(np.fmin(tmhl, fan_speed_medium))

        # 5th rule
        tmhm = np.fmin(temperature_medium_val, humidity_medium_val)
        rules_act.append(np.fmin(tmhm, fan_speed_medium))

        # 6th rule
        tmhh = np.fmin(temperature_medium_val, humidity_high_val)
        rules_act.append(np.fmin(tmhh, fan_speed_high))

        # 7th rule
        thhl = np.fmin(temperature_high_val, humidity_low_val)
        rules_act.append(np.fmin(thhl, fan_speed_high))

        # 8th rule
        thhm = np.fmin(temperature_high_val, humidity_medium_val)
        rules_act.append(np.fmin(thhm, fan_speed_high))

        # 9th rule
        thhh = np.fmin(temperature_high_val, humidity_high_val)
        rules_act.append(np.fmin(thhh, fan_speed_high))

        mf_action = np.fmax(rules_act[0], 
                            np.fmax(rules_act[1], 
                                    np.fmax(rules_act[2], 
                                            np.fmax(rules_act[3], 
                                                    np.fmax(rules_act[4],
                                                            np.fmax(rules_act[5], 
                                                                    np.fmax(rules_act[6],
                                                                            np.fmax(rules_act[7],
                                                                                    rules_act[8]))))))))
        
        action_fuzz = fuzz.defuzz(fan_speed_universe, mf_action, 'centroid')
        z[i-20, j-10] = action_fuzz

ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z)
plt.show()
