import numpy as np
import matplotlib.pyplot as plt

V0 = 5.0       # supply voltage (V)
R = 10e3       # resistance (10 kohm)
C = 22e-12     # capacitance (22 pF)

tau = R * C

V_tau = V0 * (1 - np.exp(-1))    # voltage at t = tau (~0.632 * V0)

t = np.linspace(0, 5 * tau, 500)
V = V0 * (1 - np.exp(-t / tau))

fig, ax = plt.subplots()

ax.plot(t, V, color="black")              # the only solid line
ax.axhline(V_tau, linestyle=":", color="0.4")  # dotted reference line

ax.grid(False)

ax.set_xlabel("Time (s)")
ax.set_ylabel("Voltage (V)")
ax.set_title(
    f"Capacitor charging (R = {R/1e3:.0f} k$\\Omega$, C = {C*1e12:.0f} pF)"
)

# Paths are relative to the repository root (run the script from there)
fig.savefig("../figures/generated/rc_charging.pdf")  # vector, publishable
