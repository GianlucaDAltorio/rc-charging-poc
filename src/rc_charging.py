import numpy as np
import matplotlib.pyplot as plt

V0 = 5.0
VIH = 0.7 * V0

# 10 kOhm metal-film resistor: +-5%
# 1 uF ceramic capacitor: +-10%
R_nominal = 10e3
C_nominal = 1e-6
R_tolerance = 0.05
C_tolerance = 0.10

# Fastest case: both R and C at minimum
R_fast = R_nominal * (1 - R_tolerance)
C_fast = C_nominal * (1 - C_tolerance)

# Slowest case: both R and C at maximum
R_slow = R_nominal * (1 + R_tolerance)
C_slow = C_nominal * (1 + C_tolerance)

def t_release(R, C):
    return -R * C * np.log(1 - VIH / V0)

t_nominal = t_release(R_nominal, C_nominal)
t_fast = t_release(R_fast, C_fast)
t_slow = t_release(R_slow, C_slow)

print(f"Nominal t_release = {t_nominal*1e3:.2f} ms")
print(f"Fastest (R_min, C_min) t_release = {t_fast*1e3:.2f} ms")
print(f"Slowest (R_max, C_max) t_release = {t_slow*1e3:.2f} ms")

# Plot all three charging curves
t = np.linspace(0, 5 * t_slow / (-np.log(1 - VIH / V0)), 500)
tau_max = R_slow * C_slow
t = np.linspace(0, 5 * tau_max, 500)

def charging(t, R, C):
    tau = R * C
    return V0 * (1 - np.exp(-t / tau))

fig, ax = plt.subplots()
ax.plot(t, charging(t, R_nominal, C_nominal), color="black", linewidth=2.5,
        label=f"Nominal (R={R_nominal/1e3:.0f}k$\\Omega$, C={C_nominal*1e6:.0f}$\\mu$F)")
ax.plot(t, charging(t, R_fast, C_fast), color="black", linestyle="--", linewidth=1.3,
        label=f"Fastest case ({t_fast*1e3:.1f} ms)")
ax.plot(t, charging(t, R_slow, C_slow), color="black", linestyle="-.", linewidth=1.3,
        label=f"Slowest case ({t_slow*1e3:.1f} ms)")

ax.axhline(VIH, linestyle=":", color="0.4", label="$V_{IH}$")
ax.grid(False)
ax.set_xlabel("Time (s)")
ax.set_ylabel("Voltage (V)")
ax.set_title("POR charging curve with component tolerance")
ax.legend()

fig.savefig("figures/generated/rc_tolerance.pdf")