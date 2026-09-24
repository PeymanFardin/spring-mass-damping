#Spring-mass system with three damping models (none, linear, quadratic), solved with semi-implicit Euler.

import numpy as np
import matplotlib.pyplot as plt


#Simulation Parameters
m = 1          #Mass (kg)
k = 10         #Spring constant (N/m)
x0 = 1         #Initial position (m)
v0 = 0         #Initial velocity (m/s)
dt = 0.001     #Time step (s)
t_max = 10     #Total time (s)

#Damping coefficients
c_lin = 1      #Linear damping coefficient (kg/s)
c_quad = 1     #Quadratic damping coefficient (kg/m)

CASES = {
    "No damping": (0, 0, "blue"),
    "Linear damping": (c_lin, 0, "red"),
    "Quadratic damping": (0, c_quad, "purple"), }


#Semi-Implicit Euler method
def simulate(c_lin, c_quad):
    n = int(round(t_max / dt)) + 1
    t = np.arange(n) * dt
    x = np.empty(n)
    v = np.empty(n)
    x[0], v[0] = x0, v0

    for i in range(n-1):
        a = (-k * x[i] - c_lin * v[i] - c_quad * abs(v[i]) * v[i]) / m
        v[i + 1] = v[i] + a * dt              #Update Velocity
        x[i + 1] = x[i] + v[i + 1] * dt       #Update Position

    E = 0.5 * m * v**2 + 0.5 * k * x**2
    return t, x, v, E


#Plot
fig, axs = plt.subplots(2, 2, figsize=(12, 8))
for name, (cl, cq, color) in CASES.items():
    t, x, v, E = simulate(cl, cq)
    axs[0, 0].plot(t, x, color=color, label=name)
    axs[0, 1].plot(t, v, color=color, label=name)
    axs[1, 0].plot(t, E, color=color, label=name)
    axs[1, 1].plot(x, v, color=color, label=name)


axs[0, 0].set(xlabel="Time (s)", ylabel="Position (m)", title="Position")
axs[0, 1].set(xlabel="Time (s)", ylabel="Velocity (m/s)", title="Velocity")
axs[1, 0].set(xlabel="Time (s)", ylabel="Energy (J)", title="Total energy")
axs[1, 1].set(xlabel="Position (m)", ylabel="Velocity (m/s)", title="Phase portrait")
for ax in axs.flat:
    ax.legend()
    ax.grid(True)

fig.suptitle("Spring-Mass System: No Damping vs Linear vs Quadratic Damping")
plt.tight_layout()
plt.savefig("spring_mass.png", dpi=150)
plt.show()
