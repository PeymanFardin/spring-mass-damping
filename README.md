# Spring-Mass System with Three Damping Models

## Overview
This project simulates a mass attached to a spring under three different conditions:
1. No damping
2. Linear damping
3. Quadratic damping

The position, velocity, total energy, and phase portrait are calculated and compared for each case.
All three cases are solved numerically with the same method (semi-implicit Euler), using Python, NumPy, and Matplotlib.

## Physical Parameters
The mass is $m = 1 \space \mathrm{kg}$ and the spring constant is $k = 10 \space \mathrm{N/m}$. The mass is released from rest at $x_0 = 1 \space \mathrm{m}$ ($v_0 = 0$).

The damping coefficients used in the simulation are:

Linear damping coefficient: $c_{lin} = 1 \space \mathrm{kg/s}$

Quadratic damping coefficient: $c_{quad} = 1 \space \mathrm{kg/m}$

The time step is $\Delta t = 0.001 \space \mathrm{s}$ and the total simulated time is $10 \space \mathrm{s}$.

## Model
The equation of motion for all three cases is:

$$m\ddot{x} = -kx - c_{lin} \ v - c_{quad} \ |v| \ v$$

Each case is obtained by turning the coefficients on or off:

| Case              | $c_{lin}$ | $c_{quad}$ |
|-------------------|-----------|------------|
| No damping        | 0         | 0          |
| Linear damping    | 1         | 0          |
| Quadratic damping | 0         | 1          |

The term $|v|\,v$ has magnitude $v^2$ but keeps the sign of $v$, so the quadratic damping force always acts against the direction of motion.

## Method
The equation is solved with the semi-implicit Euler method. In each time step:

$$v_{i+1} = v_i + a_i\,\Delta t$$

$$x_{i+1} = x_i + v_{i+1}\,\Delta t$$

The position is updated using the new velocity $v_{i+1}$. This small change compared to the standard Euler method keeps the energy of an undamped oscillator from growing artificially, which is why it is used here.

A single function, `simulate(c_lin, c_quad)`, is used for all three cases. The cases are stored in a dictionary and the function is called once for each of them.

## Energy
The total energy is calculated as:

$$E = \frac{1}{2}mv^2 + \frac{1}{2}kx^2$$

## Results
The program produces four plots: position vs time, velocity vs time, total energy vs time, and the phase portrait ($v$ vs $x$).

Observations from the simulation:
- **No damping:** the energy stays close to its initial value of $5 \space \mathrm{J}$ (it varies between about $4.992 \space \mathrm{J}$ and $5.008 \space \mathrm{J}$), and the phase portrait is a closed ellipse. The small variation comes from the numerical method.
- **Linear damping:** the energy decays smoothly and the phase portrait spirals inward. The energy drops to half of its initial value at $t \approx 0.63 \space \mathrm{s}$ and is almost zero ($\approx 0.0002 \space \mathrm{J}$) at $t = 10 \space \mathrm{s}$.
- **Quadratic damping:** at the beginning, when the speed is high, the damping is stronger than in the linear case and the energy drops to half at $t \approx 0.47 \space \mathrm{s}$. As the speed decreases, the damping force ($\propto v^2$) becomes weak and the energy decays more slowly. At $t = 10 \space \mathrm{s}$ the energy is about $0.024 \space \mathrm{J}$, which is higher than in the linear case.

So the two damping models cross over: quadratic damping removes energy faster at high speeds, and linear damping removes it faster at low speeds.

## Limitations
- The values of $c_{lin}$ and $c_{quad}$ are chosen arbitrarily, and they have different units. Therefore the comparison between the linear and quadratic cases is only valid for these specific values. With other coefficients, the crossover point would move.
- Semi-implicit Euler is a first-order method. The results were not compared with an analytical solution or a higher-order method in this project.

## How to Run
```
pip install -r requirements.txt
python spring_mass_damping.py
```

## Note
This project was created as a physics programming project to explore damped oscillations and numerical methods.
