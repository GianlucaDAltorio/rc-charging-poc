import numpy as np
import matplotlib.pyplot as plt

V0 = 5.0 # supply voltage (V)
R = 10e3 # resistance (10 kohm)
C = 22e-12 # capacitance (22 pF)

tau = R * C # time constant (s)
t = np.linspace(0, 5 * tau, 500)
V = V0 * (1 - np.exp(-t / tau))

plt.plot(t, V, color="black")
plt.xlabel("Time (s)")
plt.ylabel("Voltage (V)")
plt.title("Capacitor charging")
plt.show() # default interactive view; nothing saved yet

print("tau =", tau, "s ; V(tau) =", V0 * (1 - np.exp(-1)), "V")