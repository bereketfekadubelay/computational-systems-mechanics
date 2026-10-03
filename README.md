# Computational Systems Mechanics: Numerical Modeling of Damped Mechanical Oscillations and Quantitative Analysis of Dynamic Market Order/Options Flow

**Author:** Bereket Fekadu Belay  
**Date:** October 2026  
**Target Major:** Computational Engineering / Mechanical Systems  
**Repository:** https://github.com/bereketfekadubelay/computational-systems-mechanics  

---

## 1. Abstract & Objectives
This research establishes a unified computational framework bridging physical mechanical dynamics with financial market microstructure. By reformulating a 1-DOF mass-spring-damper Ordinary Differential Equation (ODE) into state-space representation, we numerically solve for displacement responses across three distinct damping regimes using Python (`SciPy`/`NumPy`). We then map these physical damping behaviors directly to market liquidity absorption and option dealer Gamma Exposure (GEX) dynamic hedging flows. The primary objective is to prove that complex price stabilization (pinning) and volatility expansion (resonance) in financial markets can be mathematically modeled using classical systems mechanics principles.

---

## 2. Governing Equations & Mathematical Methodology

### Physical Mechanical Model
The system is governed by the second-order linear homogeneous ordinary differential equation:
$$m \cdot \frac{d^2 x}{dt^2} + c \cdot \frac{dx}{dt} + k \cdot x = 0$$

Transforming into state-space representation yields two coupled first-order ODEs:
$$\frac{dx}{dt} = v(t)$$
$$\frac{dv}{dt} = -\left(\frac{c}{m}\right) v(t) - \left(\frac{k}{m}\right) x(t)$$

Where damping ratio $\zeta = \frac{c}{c_{crit}}$ and critical damping coefficient $c_{crit} = 2 \sqrt{k \cdot m}$:
1. **Underdamped ($\zeta < 1.0$):** Oscillatory decay, $x(t) = A \cdot e^{-\zeta \omega_n t} \cos(\omega_d t - \phi)$
2. **Critically Damped ($\zeta = 1.0$):** Non-oscillatory fastest decay to equilibrium, $x(t) = (C_1 + C_2 t) e^{-\omega_n t}$
3. **Overdamped ($\zeta > 1.0$):** Sluggish non-oscillatory decay, $x(t) = C_1 e^{r_1 t} + C_2 e^{r_2 t}$

### Quantitative Microstructure & Options Flow Model
Order book delta imbalances and option dealer hedging dynamics dictate the price state variable $P(t)$:
$$\text{CVD}(t) = \int_0^t (V_{\text{Ask}}(\tau) - V_{\text{Bid}}(\tau)) \, d\tau$$
$$\text{GEX}_{\text{total}} = \sum (\text{OI}_i \cdot \Gamma_i \cdot 100 \cdot S^2 \cdot \Phi_i)$$

In positive gamma regimes ($\text{GEX} > 0$), dealer hedging behaves as positive damping ($c > 0$) with a restoring stiffness force ($k$), stabilizing market price near equilibrium strike prices. In negative gamma regimes ($\text{GEX} < 0$), dealer hedging induces negative damping ($c < 0$), destabilizing price and generating exponential velocity expansion (volatility).

---

## 3. Computational Simulation & Code Architecture
The computational model was executed in Python 3 using `scipy.integrate.odeint` over a discretization domain of $t \in [0, 3.0]$ seconds ($N = 1000$). System parameters were defined as $m = 1.0\text{ kg}$ and $k = 100.0\text{ N/m}$ ($\omega_n = 10.0\text{ rad/s}$, $c_{crit} = 20.0\text{ Ns/m}$).

The simulation verified:
* **Underdamped regime ($c = 4.0\text{ Ns/m}, \zeta = 0.2$):** Exhibited periodic overshoot and damped harmonic oscillations.
* **Critically Damped regime ($c = 20.0\text{ Ns/m}, \zeta = 1.0$):** Returned to equilibrium in $t \approx 0.6$ seconds without overshoot.
* **Overdamped regime ($c = 50.0\text{ Ns/m}, \zeta = 2.5$):** Exhibited heavy viscous drag, requiring $t > 2.2$ seconds to reach baseline.

---

## 4. Quantitative Order & Options Flow Case Study
A comparative empirical analysis was conducted evaluating market price behavior across distinct liquidity states:

* **Case A (Positive GEX Regime / High DOM Depth):** High resting limit order density ($m$) paired with positive dealer gamma exposure ($\text{GEX} > 0$) mimics a critically damped physical system ($\zeta \ge 1.0$). Aggressive buy market sweeps (CVD injection) are instantly absorbed by passive ask liquidity. Price displacement is bounded, exhibiting rapid mean-reversion.
* **Case B (Negative GEX Regime / Low DOM Depth):** Exhaustion of resting limit orders ($c \to 0$) combined with net short dealer gamma ($\text{GEX} < 0$) introduces negative damping. As price moves down, dealers are forced to sell underlying futures, injecting kinetic energy into price velocity. This results in runaway price movement analogous to mechanical parametric resonance.

---

## 5. Engineering Conclusions & System Synthesis
This research demonstrates that financial order books and options hedging environments behave as dynamic mechanical systems governed by differential conservation laws. Damping parameters ($c$) directly equate to limit order book absorption depth, while spring stiffness ($k$) maps directly to options market maker gamma exposure. Applying numerical ODE solvers to quantitative market microstructure offers a robust, physics-informed framework for engineering automated risk management algorithms and predicting liquidity-driven volatility regimes.
