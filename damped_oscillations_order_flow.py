import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 1. Define the system ODEs (State-Space Form)
def damped_oscillator(y, t, m, c, k):
    x, v = y
    dxdt = v
    dvdt = -(c / m) * v - (k / m) * x
    return [dxdt, dvdt]

# 2. Define physical parameters
m = 1.0       # Mass (kg)
k = 100.0     # Stiffness (N/m)
c_crit = 2.0 * np.sqrt(k * m)  # Critical damping coefficient = 20.0 Ns/m

# 3. Time domain
t = np.linspace(0, 3.0, 1000)
y0 = [1.0, 0.0]  # Initial conditions: x0 = 1.0 m, v0 = 0.0 m/s

# 4. Define damping regimes
regimes = {
    'Underdamped ($\zeta = 0.2, c = 4.0$ Ns/m)': 4.0,
    'Critically Damped ($\zeta = 1.0, c = 20.0$ Ns/m)': 20.0,
    'Overdamped ($\zeta = 2.5, c = 50.0$ Ns/m)': 50.0
}

# 5. Solve ODEs and plot responses
plt.figure(figsize=(10, 6))

for label, c in regimes.items():
    sol = odeint(damped_oscillator, y0, t, args=(m, c, k))
    plt.plot(t, sol[:, 0], label=label, linewidth=2)

plt.title('1-DOF Mass-Spring-Damper System Dynamic Response Across Damping Regimes', fontsize=12, fontweight='bold')
plt.xlabel('Time t (seconds)', fontsize=10)
plt.ylabel('Displacement x(t) (meters)', fontsize=10)
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right')
plt.tight_layout()

# Save plot image
plt.savefig('damped_oscillation_response.png', dpi=300)
plt.show()