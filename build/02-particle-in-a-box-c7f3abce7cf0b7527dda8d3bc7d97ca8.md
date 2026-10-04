---
kernelspec:
  name: python3
  display_name: Python 3
---

# Particle in a Box

 :::{note} **What you need to know**

 **Particle in a Box (PIB) as a Model System**  
   The Particle in a Box (PIB) is a simple model that helps illustrate the behavior of electrons confined within atoms and molecules. It serves as a useful tool to introduce key quantum concepts:


``````{admonition} 中文翻译
:class: dropdown

 **一维无限深势阱（PIB）作为模型系统**  
   一维无限深势阱（PIB）是一个简单模型，有助于说明被束缚在原子和分子内部的电子的行为。它是引入关键量子概念的有用工具：
``````

   - **Energetic Quantization**: Energy levels in quantum systems are discrete, not continuous, as seen in the PIB model.


``````{admonition} 中文翻译
:class: dropdown

- **能量的量子化**：量子系统中的能级是分立的，而非连续的，正如一维无限深势阱模型所示。
``````
   
   - **Probabilistic Nature of Quantum Particles**: The probability distribution for the particle's position is non-uniform, with nodal points where the probability is zero, emphasizing the inherent uncertainty in the particle's exact location.


``````{admonition} 中文翻译
:class: dropdown

- **量子粒子的概率性本质**：粒子位置的概率分布不均匀，存在概率为零的节点，这凸显了粒子确切位置内在的不确定性。
``````
   
   - **Uncertainty Principle**: There is an inverse relationship between the uncertainty in position and momentum, demonstrating the fundamental limit on how precisely both quantities can be known simultaneously.


``````{admonition} 中文翻译
:class: dropdown

- **不确定性原理**：位置的不确定性与动量的不确定性之间存在反比关系，这表明了两个量能被同时精确知道的根本限度。
``````
   
   - **Zero-Point Energy**: Quantum particles always possess a minimum kinetic energy, even at absolute zero. This zero-point energy highlights the impossibility of freezing all motion in quantum systems.


``````{admonition} 中文翻译
:class: dropdown

- **零点能**：量子粒子总是具有一个最小的动能，即使在绝对零度也是如此。这一零点能凸显了在量子系统中冻结所有运动是不可能的。
``````
   
   - **Quantum-Classical Correspondence**: As the system scales up, quantum behavior smoothly transitions to classical behavior, illustrating the correspondence principle.

   - **Degeneracy of Energy Levels**: In systems with symmetries, multiple wave functions can correspond to the same energy level, a phenomenon known as degeneracy.


``````{admonition} 中文翻译
:class: dropdown

- **量子—经典对应**：随着系统尺度增大，量子行为会平滑过渡到经典行为，体现了对应原理。
- **能级的简并**：在具有对称性的系统中，多个波函数可以对应同一个能级，这种现象称为简并。
``````
:::

### Classical vs Quantum particle in a box

- The particle in a box is a toy model of an electron (or atom, molecule, or small quantum object) trapped in some region of space $[0,L]$.
- The positional information of a quantum "particle" is described by a quantum wave function $\psi(x)$, which is obtained by solving the Schrödinger equation with boundary conditions.
- Wave functions are standing waves, just as in the vibrating guitar string problem, with one major difference: a quantum wave function has a probabilistic meaning and hence is completely different from the classical notion of a "wave".
- **According to classical mechanics**, in the absence of any attractive interactions the particle bounces back and forth between the walls with constant speed. We therefore expect to find it with equal probability at all locations $x$.
- **According to quantum mechanics**, the quantum particle in the box is found in some regions with high probability and in others with little or zero probability.


``````{admonition} 中文翻译
:class: dropdown

- 一维无限深势阱中的粒子是一个玩具模型，用来描述被束缚在某个空间区域 $[0,L]$ 内的电子（或原子、分子，或小量子物体）。
- 量子“粒子”的位置信息由量子波函数 $\psi(x)$ 描述，该波函数是通过求解带边界条件的薛定谔方程得到的。
- 波函数是驻波，正如振动的吉他弦问题中那样，但有一个主要区别：量子波函数具有概率意义，因此与经典意义上的“波”完全不同。
- **根据经典力学**，在没有任何吸引相互作用的情况下，粒子以恒定速率在两壁之间来回弹跳。因此我们预期在任何位置 $x$ 找到它的概率都相等。
- **根据量子力学**，势阱中的量子粒子在某些区域被发现概率高，在另一些区域概率低或为零。
``````

```{code-cell} python
:tags: [hide-input]
# synced: box_bounce
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
rng = np.random.default_rng(5)
xc = rng.random(4000)                                       # classical: snapshots at random times
cand = rng.random(16000)
xq = cand[rng.random(16000) < np.sin(3 * np.pi * cand) ** 2][:4000]   # quantum: samples of |psi_3|^2
yj = rng.random(4000)
counts = np.unique(np.round(np.geomspace(1, 4000, 44)).astype(int))
counts = np.concatenate([counts, np.full(8, counts[-1])])
edges = np.linspace(0, 1, 31); mid = 0.5 * (edges[1:] + edges[:-1]); dx = edges[1] - edges[0]
xs = np.linspace(0, 1, 300)
fig, axes = plt.subplots(2, 2, figsize=(8, 3.9), sharex=True,
                         gridspec_kw={"height_ratios": [1, 2.2], "hspace": 0.12, "wspace": 0.1})
(ta, tb), (ha, hb) = axes
for ax in (ta, tb):
    ax.axvline(0, color="k", lw=3); ax.axvline(1, color="k", lw=3)
    ax.set_ylim(0, 1); ax.set_yticks([]); ax.spines["left"].set_visible(False); ax.tick_params(bottom=False)
ta.set_title("classical: a ball bouncing at constant speed", loc="left", fontsize=10.5)
tb.set_title(r"quantum, $n = 3$: each dot is one detection", loc="left", fontsize=10.5)
(trail,) = ta.plot([], [], "o", color=ORANGE, ms=9, alpha=0.25)
(ball,) = ta.plot([], [], "o", color=ORANGE, ms=12)
scat = tb.scatter([], [], s=5, color=TEAL, alpha=0.6, lw=0)
bars_c = ha.bar(mid, 0 * mid, width=0.92 * dx, color=ORANGE, alpha=0.5)
bars_q = hb.bar(mid, 0 * mid, width=0.92 * dx, color=TEAL, alpha=0.5)
(pc,) = ha.plot([], [], color=GRAY, lw=2.4, ls="--", label=r"flat: $1/L$")
(pq,) = hb.plot([], [], color=CARDINAL, lw=2.4, label=r"$|\psi_3(x)|^2$")
for ax in (ha, hb):
    ax.set_xlim(-0.02, 1.02); ax.set_yticks([])
    ax.set_xticks([0, 0.5, 1]); ax.set_xticklabels(["0", "L/2", "L"]); ax.set_xlabel("position x")
    ax.legend(loc="upper right", frameon=False, fontsize=9.5)
ha.set_ylabel("times caught here")
fig.subplots_adjust(left=0.05, right=0.99, top=0.84, bottom=0.13)
sup = fig.suptitle("", fontsize=11.5)
tri = lambda s: 0.04 + 0.92 * (1 - np.abs(2 * (s % 1) - 1))  # bounce between the walls

def update(i):
    N = counts[i]
    pos = tri(np.arange(i - 3, i + 1) / 11.0)
    trail.set_data(pos[:-1], np.full(3, 0.5)); ball.set_data(pos[-1:], [0.5])
    scat.set_offsets(np.column_stack([xq[:N], yj[:N]]))
    hc = np.histogram(xc[:N], bins=edges)[0]; hq = np.histogram(xq[:N], bins=edges)[0]
    for b, c in zip(bars_c, hc):
        b.set_height(c)
    for b, c in zip(bars_q, hq):
        b.set_height(c)
    pc.set_data(xs, np.full_like(xs, N * dx)); pq.set_data(xs, N * dx * 2 * np.sin(3 * np.pi * xs) ** 2)
    top = 1.3 * max(1.0, hc.max(), hq.max(), 2 * N * dx)
    ha.set_ylim(0, top); hb.set_ylim(0, top)
    sup.set_text(f"N = {N} position measurement" + ("" if N == 1 else "s"))

ani = FuncAnimation(fig, update, frames=len(counts), interval=150, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. Catching the particle many times. Left: a classical ball bounces between the walls at constant speed, so its position measurements pile up evenly. Right: in the quantum state $n = 3$ the measurements pile up into three lobes, and the particle is never found at $x = L/3$ or $x = 2L/3$. Each dot is one measurement, as in the Born-rule figure of the [previous lecture](01-schrodinger-equation.md).


``````{admonition} 中文翻译
:class: dropdown

图。多次捕捉粒子。左图：经典小球以恒定速率在两壁之间弹跳，因此其位置测量结果均匀堆积。右图：在量子态 $n = 3$ 中，测量结果堆积成三个瓣，粒子在 $x = L/3$ 或 $x = 2L/3$ 处永远不会被发现。每个点代表一次测量，正如[上一讲](01-schrodinger-equation.md)的玻恩规则图所示。
``````

### Solving the Schrödinger Equation for the Particle in a Box (PIB)


:::{figure} images/ext_infinite_well.svg
:label: fig-particle-in-a-box-2
:alt: Particle in a box
:width: 300px

Particle in a box subject to infinitely high potential walls.


``````{admonition} 中文翻译
:class: dropdown

受到无限高势壁束缚的势阱中的粒子。
``````
:::

The Schrödinger equation for a particle in a box (PIB) is defined by a Hamiltonian operator that incorporates a potential energy which is infinitely large at the boundaries of the box and zero inside. This potential confines the particle within the box, where it can only possess kinetic energy.


``````{admonition} 中文翻译
:class: dropdown

一维无限深势阱（PIB）中粒子的薛定谔方程由一个哈密顿算符定义，该算符包含一个在势阱边界处为无限大、在内部为零的势能。这个势将粒子束缚在势阱内，粒子在阱内只能具有动能。
``````

- **The potential energy for PIB is defined:**

$$
V(x) =
\begin{cases} 
\infty & x \le 0 \text{ or } x \ge L \\ 
0 & 0 < x < L
\end{cases}
$$

- **The boundary conditions are:**

$$
\psi(0) = \psi(L) = 0
$$

- **The Hamiltonian operator** in this case accounts only for kinetic energy:


``````{admonition} 中文翻译
:class: dropdown

- **哈密顿算符**在这种情况下只计及动能：
``````

$$
\hat{H} = \hat{K} = -\frac{\hbar^2}{2m} \frac{d^2}{dx^2}
$$

- Now, we have all the necessary ingredients to solve the time-independent Schrödinger equation for the 1D PIB:


``````{admonition} 中文翻译
:class: dropdown

- 现在，我们已具备求解一维无限深势阱的不含时薛定谔方程所需的全部要素：
``````

$$
\hat{H} \psi(x) = E \psi(x)
$$

- Substituting the Hamiltonian, we get:

$$
-\frac{\hbar^2}{2m} \frac{d^2}{dx^2} \psi(x) = E \psi(x)
$$

$$
\psi''(x) = -k^2 \psi(x)
$$

- where $k^2$ is a positive real number that relates the particle's energy $E$ to its wavefunction.


``````{admonition} 中文翻译
:class: dropdown

- 其中 $k^2$ 是一个正实数，它将粒子的能量 $E$ 与其波函数联系起来。
``````

$$
k^2 = \frac{2mE}{\hbar^2}
$$

### Solution and Boundary Conditions

- Mathematically, the form of the 1D PIB problem is similar to the ordinary differential equation (ODE) used in the 1D vibrating guitar string problem. The key differences lie in the constant coefficients and the interpretation of the wavefunction.


``````{admonition} 中文翻译
:class: dropdown

- 从数学上看，一维无限深势阱问题的形式与一维吉他弦振动问题中使用的常微分方程（ODE）相似。关键区别在于常系数和波函数的解释。
``````

$$
\psi''(x) = -k^2 \psi(x)
$$

- The general solution to this differential equation is:


``````{admonition} 中文翻译
:class: dropdown

- 这个微分方程的通解为：
``````

$$
\psi(x) = c_1 e^{ikx} + c_2 e^{-ikx} = A \cos(kx) + B \sin(kx)
$$

- Applying the boundary condition $\psi(0) = 0$, we find that $A = 0$, leaving us with:


``````{admonition} 中文翻译
:class: dropdown

- 应用边界条件 $\psi(0) = 0$，我们发现 $A = 0$，于是得到：
``````

$$
\psi(x) = B \sin(kx)
$$

- Applying the boundary condition $\psi(L) = 0$, we get:


``````{admonition} 中文翻译
:class: dropdown

- 应用边界条件 $\psi(L) = 0$，我们得到：
``````

$$
B \sin(kL) = 0
$$

- This condition is satisfied when:

$$
kL = n\pi \quad \text{or} \quad k = \frac{n\pi}{L}
$$

- Thus, the wavefunction becomes:

$$
\psi(x) = B \sin\left(\frac{n\pi}{L}x\right)
$$

- Using the relationship $k^2 = \frac{n^2\pi^2}{L^2} = \frac{2mE}{\hbar^2}$, we can express the energy levels as:


``````{admonition} 中文翻译
:class: dropdown

- 利用关系 $k^2 = \frac{n^2\pi^2}{L^2} = \frac{2mE}{\hbar^2}$，我们可以把能级表示为：
``````

$$
E_n = \frac{n^2 h^2}{8mL^2}
$$

- The quantization of energy results from confining the wavefunction within a finite space. This is the reason bound states exhibit quantized energy levels. Atoms, molecules, and solids all possess discrete energy levels due to similar constraints.
- This is the trial-energy experiment of the [previous lecture](01-schrodinger-equation.md) in its simplest form. There the decaying tails admitted only special energies; here the walls do: $\sin kx$ reaches zero at $x = L$ only when a whole number of half-waves fits, $L = n\lambda/2$.


``````{admonition} 中文翻译
:class: dropdown

- 能量的量子化源于将波函数限制在有限空间内。这就是束缚态呈现分立能级的原因。原子、分子和固体都因类似的约束而具有分立的能级。
- 这是[上一讲](01-schrodinger-equation.md)中试探能量实验的最简单形式。在那里，衰减的尾巴只允许特殊的能量；在这里则是壁在起作用：$\sin kx$ 只有在整数个半波恰好放入时才在 $x = L$ 处达到零，即 $L = n\lambda/2$。
``````

### Wavefunctions Must Be Normalized

- Next, we determine the constant coefficient $B_n$ by enforcing the normalization condition:


``````{admonition} 中文翻译
:class: dropdown

- 接下来，我们通过施加归一化条件来确定常系数 $B_n$：
``````

$$
\int_0^L \psi_n(x)^2 \, dx = 1
$$

- To evaluate the integral, we use the trigonometric identity $\sin^2 x = \frac{1}{2}(1 - \cos 2x)$


``````{admonition} 中文翻译
:class: dropdown

- 为了计算这个积分，我们使用三角恒等式 $\sin^2 x = \frac{1}{2}(1 - \cos 2x)$
``````

$$
B_n^2 \int_0^L \sin^2\left(\frac{n\pi x}{L}\right) dx = \frac{B_n^2}{2} \int_0^L \left[ 1 - \cos\left(\frac{2n\pi x}{L}\right) \right] dx =1
$$

- Since the integral of $\cos\left(\frac{2n\pi x}{L}\right)$ over a full period from $0$ to $L$ is zero, we are left with:


``````{admonition} 中文翻译
:class: dropdown

- 由于 $\cos\left(\frac{2n\pi x}{L}\right)$ 在从 $0$ 到 $L$ 的整个周期上的积分为零，我们剩下：
``````

$$
\frac{B_n^2}{2} \cdot L = 1
$$

- Solving for $B_n$, we determine the **normalization constant**, which ensures that the square of the wavefunction integrates to 1.


``````{admonition} 中文翻译
:class: dropdown

- 解出 $B_n$，我们确定了**归一化常数**，它保证波函数的平方积分为 1。
``````

$$
B_n = \sqrt{\frac{2}{L}}
$$

### PIB Eigenfunctions and Eigenvalues

:::{important} **Eigenfunctions and eigenvalues of 1D particle in a box**

$${\psi_n(x) = \Big (\frac{2}{L}\Big)^{\frac{1}{2}} \sin\frac{n\pi x}{L}}$$

$${E_n=\frac{n^2 h^2}{8mL^2}}$$

:::

:::{important} **Full time dependent solution**

$${\psi_n(x, t) = \Big (\frac{2}{L}\Big)^{\frac{1}{2}} \sin\frac{n\pi x}{L}}\cdot e^{-i\frac{E_n t}{\hbar}}$$

$$\Psi(x,t) = \sum_n c_n \psi_n(x, t)$$

- where the coefficients $c_n$ depend on the initial condition. For example, all could be zero except one (a pure state), or a few could be non-zero (a mixed state).


``````{admonition} 中文翻译
:class: dropdown

- 其中系数 $c_n$ 取决于初始条件。例如，除了一个之外可以全为零（纯态），也可以有若干个不为零（混合态）。
``````

:::

```{code-cell} python
:tags: [hide-input]
# synced: pib_ladder
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
x = np.linspace(0, 1, 400)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4.4), sharey=True, gridspec_kw={"wspace": 0.08})
for ax in (ax1, ax2):
    ax.plot([0, 0, 1, 1], [18.3, 0, 0, 18.3], color="k", lw=2.6)
    ax.set_xlim(-0.04, 1.04); ax.set_ylim(-0.4, 18.3)
    ax.set_xticks([0, 0.5, 1]); ax.set_xticklabels(["0", "L/2", "L"]); ax.set_xlabel("x")
    ax.spines["left"].set_visible(False)
for n in range(1, 5):
    E, s = n * n, np.sin(n * np.pi * x)
    for ax in (ax1, ax2):
        ax.hlines(E, 0, 1, color=GRAY, lw=0.8, ls="--")
    ax1.plot(x, E + 1.25 * s, color=TEAL, lw=2.4)
    ax2.fill_between(x, E, E + 1.6 * s**2, color=CARDINAL, alpha=0.18, lw=0)
    ax2.plot(x, E + 1.6 * s**2, color=CARDINAL, lw=2.2)
    ax2.plot(np.arange(1, n) / n, np.full(n - 1, E), "o", color="k", ms=5, zorder=5)
    ax2.text(1.06, E, rf"$n = {n}$,  " + (r"$E_1$" if n == 1 else rf"${E}E_1$"), va="center", fontsize=11.5)
ax1.set_yticks([]); ax1.set_ylabel("energy")
ax1.set_title(r"$\psi_n(x)$, drawn on its level $E_n$", loc="left", fontsize=11)
ax2.set_title(r"$|\psi_n(x)|^2$: dots mark the $n-1$ nodes", loc="left", fontsize=11)
fig.subplots_adjust(left=0.05, right=0.83, top=0.92, bottom=0.12)
plt.show()
```

Fig. The four lowest states of the particle in a box, each drawn on its energy level $E_n = n^2E_1$. Left: the wavefunctions $\psi_n(x)$. Right: the probability densities $|\psi_n(x)|^2$; the dots mark the $n-1$ nodes, where the particle is never found.


``````{admonition} 中文翻译
:class: dropdown

图。一维无限深势阱中粒子的四个最低态，每个都画在其能级 $E_n = n^2E_1$ 上。左图：波函数 $\psi_n(x)$。右图：概率密度 $|\psi_n(x)|^2$；圆点标出了 $n-1$ 个节点，在这些节点处粒子永远不会被发现。
``````

### Discrete energy levels and zero point energy

**Quantum particles are never at rest**

- The lowest energy an electron in a box can have is at $n=1$, and it is not zero!


``````{admonition} 中文翻译
:class: dropdown

- 势阱中电子所能具有的最低能量在 $n=1$ 处，而且它不为零！
``````

$$E_1 = h^2/8mL^2$$

- Keeping in mind that the energy is purely kinetic, this means a quantum particle never ceases its motion.

- This is the **uncertainty principle** at work. Confining the particle to a length $L$ leaves a position spread $\sigma_x \approx 0.18L$ in the ground state (Problem 2), and the momentum cannot be pinned down either: $\langle p \rangle = 0$ but $\langle p^2 \rangle = (h/2L)^2$, so $\sigma_p = h/2L$. The product $\sigma_x\sigma_p \approx 0.57\hbar$ sits just above the Heisenberg limit $\hbar/2$. A smaller box means a larger $\sigma_p$ and a larger kinetic energy.

- The spacing of energy levels is finite and depends on the size of the box:


``````{admonition} 中文翻译
:class: dropdown

- 请记住这里的能量纯粹是动能，这意味着量子粒子永远不会停止运动。
- 这就是**不确定性原理**在起作用。把粒子限制在长度 $L$ 内，会使基态（问题 2）留下位置展宽 $\sigma_x \approx 0.18L$，而且动量也无法确定：$\langle p \rangle = 0$ 但 $\langle p^2 \rangle = (h/2L)^2$，因此 $\sigma_p = h/2L$。乘积 $\sigma_x\sigma_p \approx 0.57\hbar$ 恰好略高于海森堡极限 $\hbar/2$。盒子越小，$\sigma_p$ 越大，动能也越大。
- 能级间距是有限的，且取决于势阱的尺寸：
``````

$$E_{n+1} - E_n = (2n+1)\frac{h^2}{8mL^2}$$

**Increasing Box size leads to more classical behavior**


``````{admonition} 中文翻译
:class: dropdown

**增大势阱尺寸会导致更经典的行为**
``````

- As the box size is increased, the energy spacing gets smaller.
- Thus quantum effects are more pronounced when an electron is bound in smaller regions of space.


``````{admonition} 中文翻译
:class: dropdown

- 随着势阱尺寸增大，能级间距变小。
- 因此，当电子被束缚在更小的空间区域时，量子效应更加显著。
``````

```{marimo-config}
---
pyproject: |
  requires-python = ">=3.10"
  dependencies = [
      "numpy",
      "matplotlib",
      "plotly",
  ]
---
```

```{marimo} python
:hide-code: true

import marimo as mo
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.dpi"] = 150
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
import plotly.graph_objects as go
TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
```

```{marimo} python
:hide-code: true

box_L = mo.ui.slider(0.5, 1.0, step=0.05, value=1.0, show_value=True, label="box length L (units of L₀)")
box_L
```

```{marimo} python
:hide-code: true

_L = box_L.value
_x = np.linspace(0, _L, 300)
_fig, (_ax, _axl) = plt.subplots(1, 2, figsize=(7.5, 3.4), gridspec_kw={"width_ratios": [1.4, 1]})
_ax.plot([0, 0, _L, _L], [38, 0, 0, 38], color="k", lw=2.6)
for _n, _c in zip((1, 2, 3), (TEAL, ORANGE, PURPLE)):
    _E = _n**2 / _L**2
    _ax.hlines(_E, 0, _L, color=_c, lw=0.9, ls="--")
    _ax.plot(_x, _E + 1.2 * np.sin(_n * np.pi * _x / _L), color=_c, lw=2.4)
    _ax.text(_L + 0.05, _E, rf"$E_{_n} = {_E:.1f}$", color=_c, va="center", fontsize=11)
_ax.text(0, -1.5, "0", ha="center", va="top", fontsize=11)
_ax.text(_L, -1.5, "L", ha="center", va="top", fontsize=11)
_ax.set_xlim(-0.05, 1.42); _ax.set_ylim(-4.5, 38); _ax.set_xticks([]); _ax.set_yticks([])
_ax.spines["left"].set_visible(False); _ax.spines["bottom"].set_visible(False)
_ax.set_title(rf"$L = {_L:.2f}\,L_0$", loc="left", fontsize=11)
_Lg = np.linspace(0.45, 3, 300)
_axl.plot(_Lg, 1 / _Lg**2, color=TEAL, lw=2.2)
_axl.plot([_L], [1 / _L**2], "o", color=TEAL, ms=9)
_axl.set_xlim(0.4, 3); _axl.set_ylim(0, 5)
_axl.set_xlabel(r"$L / L_0$"); _axl.set_ylabel(r"$E_1$")
_axl.set_title(r"$E_1 \propto 1/L^2$: never zero", loc="left", fontsize=11)
_fig.subplots_adjust(left=0.02, right=0.98, top=0.88, bottom=0.17, wspace=0.22)
_fig
```

Fig. Left: the three lowest levels of a particle in a box of length $L$, each wavefunction drawn on its level. Right: the ground-state energy against box length. Shrinking the box raises every level as $1/L^2$; enlarging it lowers $E_1$ toward zero without ever reaching it. Energies in units of $h^2/8mL_0^2$.


``````{admonition} 中文翻译
:class: dropdown

图。左图：长度为 $L$ 的势阱中粒子的三个最低能级，每个波函数都画在其能级上。右图：基态能量随势阱长度的变化。缩小势阱会使每个能级以 $1/L^2$ 上升；增大势阱则使 $E_1$ 向零降低，但永远不会达到零。能量以 $h^2/8mL_0^2$ 为单位。
``````

### Non-uniform probabilities and nodes

1. **Nodes imply zero probability to find an electron in the box**. 
    - $|\psi_n|^2=0$ at nodal points, which means zero probability.
    - This sharply contradicts classical mechanics, which bases its prediction on purely particle-like motion of the electron.
    - The existence of nodes implies a wave-like character of the electron.

2. **There are $n-1$ nodes for quantum state $n$**

- Recall that the sine function hits zero at integer multiples of $\pi$: $\sin(n\pi)=0$ when $n=1,2,3,4,...$
- The wavefunction $\psi_n(x) = \sin \frac{n\pi x}{L}$ then has $n-1$ nodes at the points $x=L/n$, $2L/n$, $3L/n$, ..., $(n-1)L/n$.
- Note that we do not count the $x=0$ and $x=L$ points as nodes, because they are part of the boundary conditions that apply to all wavefunctions.
    - For instance, the $n=3$ nodes are at $x=L/3$ and $x=2L/3$.
    - For instance, the $n=4$ nodes are at $L/4$, $2L/4$, and $3L/4$.

- The dots in the right panel of the figure of the four lowest states mark these nodes.


``````{admonition} 中文翻译
:class: dropdown

- **节点意味着在势阱中找到电子的概率为零**。
- 在节点处 $|\psi_n|^2=0$，这意味着概率为零。
- 这与经典力学形成鲜明对比，经典力学基于电子的纯粒子性运动作出预测。
- 节点的存在意味着电子具有波动性特征。
- **量子态 $n$ 有 $n-1$ 个节点**
- 回想一下，正弦函数在 $\pi$ 的整数倍处为零：当 $n=1,2,3,4,...$ 时，$\sin(n\pi)=0$。
- 于是波函数 $\psi_n(x) = \sin \frac{n\pi x}{L}$ 在点 $x=L/n$、$2L/n$、$3L/n$、……、$(n-1)L/n$ 处有 $n-1$ 个节点。
- 注意，我们不把 $x=0$ 和 $x=L$ 这两点算作节点，因为它们是适用于所有波函数的边界条件的一部分。
- 例如，$n=3$ 的节点在 $x=L/3$ 和 $x=2L/3$ 处。
- 例如，$n=4$ 的节点在 $L/4$、$2L/4$ 和 $3L/4$ 处。
- 四个最低态图中右面板的圆点标出了这些节点。
``````

### Large quantum numbers: the classical box returns

- As $n$ grows, the lobes of $|\psi_n|^2$ crowd together. A real detector has a finite resolution and averages over many lobes, and $\sin^2$ averages to $\frac{1}{2}$ over whole half-waves, so the measured density approaches the flat classical value $1/L$.
- Problem 1 gives the probability of catching the particle in the middle third of the box:


``````{admonition} 中文翻译
:class: dropdown

- 随着 $n$ 增大，$|\psi_n|^2$ 的瓣会挤在一起。真实探测器具有有限的分辨率，会对许多瓣取平均，而 $\sin^2$ 在完整的半波上平均为 $\frac{1}{2}$，因此测得的密度趋近于平坦的经典值 $1/L$。
- 问题 1 给出了在势阱中间三分之一处捕捉到粒子的概率：
``````

$$
P_n = \frac{1}{3} + \frac{\sin(2n\pi/3) - \sin(4n\pi/3)}{2n\pi}
$$

- The correction to the classical $\frac{1}{3}$ dies off as $1/n$. This is the **correspondence principle**: quantum predictions go over to classical ones at large quantum numbers. A 1 g marble crawling at 1 cm/s across a 30 cm box has $n \approx 10^{28}$, far beyond any lobe we could resolve.


``````{admonition} 中文翻译
:class: dropdown

- 对经典值 $\frac{1}{3}$ 的修正以 $1/n$ 衰减。这就是**对应原理**：在大量子数下，量子预言过渡到经典预言。一个以 1 cm/s 的速度在 30 cm 长的盒子里爬行的 1 g 弹珠具有 $n \approx 10^{28}$，远远超出我们能分辨的任何瓣。
``````

```{marimo} python
:hide-code: true

n_c = mo.ui.slider(1, 40, step=1, value=1, show_value=True, label="quantum number n")
n_c
```

```{marimo} python
:hide-code: true

_n = n_c.value
_x = np.linspace(0, 1, 3000)
_p = 2 * np.sin(_n * np.pi * _x) ** 2
_P = 1 / 3 + (np.sin(2 * _n * np.pi / 3) - np.sin(4 * _n * np.pi / 3)) / (2 * _n * np.pi)
_fig, _ax = plt.subplots(figsize=(7, 3.0))
_ax.axvspan(1 / 3, 2 / 3, color=PURPLE, alpha=0.09, lw=0)
_ax.fill_between(_x, _p, color=CARDINAL, alpha=0.2, lw=0)
_ax.plot(_x, _p, color=CARDINAL, lw=1.4 if _n < 12 else 0.8, label=r"$|\psi_n|^2$")
_ax.axhline(1, color="k", lw=2, ls="--", label=r"classical: $1/L$")
_ax.plot([0, 0, 1, 1], [2.6, 0, 0, 2.6], color="k", lw=2.6)
_ax.set_xlim(-0.02, 1.02); _ax.set_ylim(0, 2.6)
_ax.set_yticks([0, 1, 2]); _ax.set_yticklabels(["0", "1/L", "2/L"])
_ax.set_xticks([0, 1 / 3, 2 / 3, 1]); _ax.set_xticklabels(["0", "L/3", "2L/3", "L"])
_ax.legend(loc="upper right", frameon=False, fontsize=10, ncol=2, bbox_to_anchor=(1.0, 1.18))
_ax.set_title(f"n = {_n}:  P(middle third) = {_P:.3f}", loc="left", fontsize=11, color=PURPLE)
_fig.tight_layout()
_fig
```

Fig. The probability density of state $n$ against the flat classical density $1/L$. The shaded band is the middle third of the box; its probability tends to the classical $\frac{1}{3}$ as $n$ grows.


``````{admonition} 中文翻译
:class: dropdown

图。态 $n$ 的概率密度与平坦经典密度 $1/L$ 的对比。阴影带是势阱的中间三分之一；随着 $n$ 增大，其概率趋于经典值 $\frac{1}{3}$。
``````

### Superposition: the particle sloshes

- A single state $\psi_n(x)\,e^{-iE_nt/\hbar}$ is stationary. Its phase turns, but the time factor has absolute value one, so $|\psi_n(x,t)|^2 = |\psi_n(x)|^2$ never changes (see the phase clocks in the [previous lecture](01-schrodinger-equation.md)).
- A superposition of two states does move. Take equal amounts of the two lowest states:


``````{admonition} 中文翻译
:class: dropdown

- 单个态 $\psi_n(x)\,e^{-iE_nt/\hbar}$ 是定态的。它的相位在转动，但时间因子的绝对值为 1，因此 $|\psi_n(x,t)|^2 = |\psi_n(x)|^2$ 永不改变（参见[上一讲](01-schrodinger-equation.md)的相位钟）。
- 两个态的叠加确实会运动。取两个最低态的等量叠加：
``````

$$
\Psi(x,t) = \frac{1}{\sqrt{2}}\left[\psi_1(x)\,e^{-iE_1t/\hbar} + \psi_2(x)\,e^{-iE_2t/\hbar}\right]
$$

- Multiplying by the complex conjugate (Problem 2 of the previous lecture) leaves a fixed part and a **cross term** that oscillates at the difference of the two phase rates, $\omega = (E_2 - E_1)/\hbar$:


``````{admonition} 中文翻译
:class: dropdown

- 乘以其复共轭（上一讲问题 2）后，剩下一个固定部分和一个以两个相位速率之差 $\omega = (E_2 - E_1)/\hbar$ 振荡的**交叉项**：
``````

$$
|\Psi(x,t)|^2 = \frac{1}{2}\left[\psi_1^2(x) + \psi_2^2(x)\right] + \psi_1(x)\,\psi_2(x)\cos\omega t
$$

```{code-cell} python
:tags: [hide-input]
# synced: box_slosh
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE, ORANGE = "#107895", "#C8102E", "#6c757d", "#6a3d9a", "#e07b00"
plt.rcParams.update({"axes.spines.top": False, "axes.spines.right": False})
x = np.linspace(0, 1, 400)
p1, p2 = np.sqrt(2) * np.sin(np.pi * x), np.sqrt(2) * np.sin(2 * np.pi * x)
fixed, cross = 0.5 * (p1**2 + p2**2), p1 * p2               # |Psi|^2 = fixed + cross cos(wt): even + odd about L/2
nf = 60
ts = np.linspace(0, 2 * np.pi, nf, endpoint=False)          # E1 = 1, E2 = 4, hbar = 1: w = 3, three sloshes
xbar = lambda t: 0.5 - 16 / (9 * np.pi**2) * np.cos(3 * t)  # <x>(t) = L/2 + x12 cos(wt), x12 = -16L/9pi^2
th = np.linspace(0, 2 * np.pi, 200)
fig = plt.figure(figsize=(7.2, 3.4))
gs = fig.add_gridspec(2, 2, width_ratios=[2.3, 1], height_ratios=[2, 1], hspace=0.42, wspace=0.08)
ax, axx = fig.add_subplot(gs[0, 0]), fig.add_subplot(gs[1, 0])
axc, axl = fig.add_subplot(gs[0, 1]), fig.add_subplot(gs[1, 1])
ax.plot(x, fixed, color=GRAY, lw=1.8, ls="--", label=r"$\frac{1}{2}(\psi_1^2 + \psi_2^2)$")
(dens,) = ax.plot([], [], color=CARDINAL, lw=2.8, label=r"$|\Psi|^2$")
band = [ax.fill_between(x, 0 * x, color=CARDINAL, alpha=0.18, lw=0)]
(mark,) = ax.plot([], [], marker="^", color=PURPLE, ms=14, zorder=6, ls="none", label=r"$\langle x\rangle$")
ax.plot([0, 0, 1, 1], [3.35, 0, 0, 3.35], color="k", lw=2.6)          # peak of |Psi|^2 is 3.10
ax.set_xlim(-0.02, 1.02); ax.set_ylim(0, 3.35); ax.set_xticks([]); ax.set_yticks([])
ax.spines["left"].set_visible(False); ax.spines["bottom"].set_visible(False)
ax.legend(loc="lower left", bbox_to_anchor=(0, 0.97), ncol=3, frameon=False, fontsize=13,
          handlelength=1.6, columnspacing=1.4)
axx.axhline(0, color=GRAY, lw=0.8)
(crs,) = axx.plot([], [], color=PURPLE, lw=2.6)
cband = [axx.fill_between(x, 0 * x, color=PURPLE, alpha=0.18, lw=0)]
axx.set_xlim(-0.02, 1.02); axx.set_ylim(-1.7, 1.7); axx.set_yticks([])
axx.set_xticks([0, 0.5, 1]); axx.set_xticklabels(["0", "L/2", "L"], fontsize=13)
axx.spines["left"].set_visible(False)
axx.set_title(r"cross term $\psi_1\psi_2\cos\omega t$", loc="left", fontsize=13, color=PURPLE)
for a in (ax, axx):
    a.axvline(0.5, color=GRAY, lw=0.8, ls=":")
axc.plot(np.cos(th), np.sin(th), color=GRAY, lw=1, ls="--")
(arc,) = axc.plot([], [], color=PURPLE, lw=3.2, label=r"$\omega t$")
(h1,) = axc.plot([], [], color=TEAL, lw=3.2, label=r"$E_1$")
(h2,) = axc.plot([], [], color=ORANGE, lw=3.2, label=r"$E_2 = 4E_1$")
axc.set_aspect("equal"); axc.set_xlim(-1.15, 1.15); axc.set_ylim(-1.15, 1.15); axc.set_axis_off()
axc.set_title("phase clocks", fontsize=13)
axl.set_axis_off()
axl.legend(handles=[h1, h2, arc], loc="center", frameon=False, fontsize=13, handlelength=1.2)
fig.subplots_adjust(left=0.02, right=0.99, top=0.87, bottom=0.1)

def update(i):
    t = ts[i]
    c = cross * np.cos(3 * t)
    dens.set_data(x, fixed + c)
    band[0].remove(); band[0] = ax.fill_between(x, fixed + c, color=CARDINAL, alpha=0.18, lw=0)
    mark.set_data([xbar(t)], [0.14])
    crs.set_data(x, c)
    cband[0].remove(); cband[0] = axx.fill_between(x, c, color=PURPLE, alpha=0.18, lw=0)
    a1, a2 = -t, -4 * t                                     # clock hands: e^{-iE1 t}, e^{-iE2 t}
    d = (a1 - a2) % (2 * np.pi)                             # angle between the hands, w t
    s = np.linspace(a2, a2 + d, 40) if d <= np.pi else np.linspace(a1, a1 + 2 * np.pi - d, 40)
    arc.set_data(0.42 * np.cos(s), 0.42 * np.sin(s))
    h1.set_data([0, np.cos(a1)], [0, np.sin(a1)]); h2.set_data([0, np.cos(a2)], [0, np.sin(a2)])

ani = FuncAnimation(fig, update, frames=nf, interval=90, blit=False)
plt.close(fig)
HTML(ani.to_jshtml())
```

Fig. An equal superposition of $\psi_1$ and $\psi_2$. Top: the density $|\Psi|^2$ is the fixed part $\frac{1}{2}(\psi_1^2 + \psi_2^2)$ (dashed) plus the cross term; the triangle marks $\langle x \rangle$. Bottom: the cross term $\psi_1\psi_2\cos\omega t$. Right: the phase clocks of the two states; the angle between their hands is $\omega t$.


``````{admonition} 中文翻译
:class: dropdown

图。$\psi_1$ 与 $\psi_2$ 的等量叠加。上图：密度 $|\Psi|^2$ 由固定部分 $\frac{1}{2}(\psi_1^2 + \psi_2^2)$（虚线）加上交叉项构成；三角形标记 $\langle x \rangle$。下图：交叉项 $\psi_1\psi_2\cos\omega t$。右图：两个态的相位钟；它们的指针之间的夹角为 $\omega t$。
``````

- The fixed part is symmetric about the center of the box, so on its own it balances at $L/2$. The cross term is odd about the center: it adds probability on one side, removes the same amount on the other, and flips sign every half period. The mean position swings with it:


``````{admonition} 中文翻译
:class: dropdown

- 固定部分关于势阱中心对称，因此仅凭它自身会在 $L/2$ 处平衡。交叉项关于中心是奇函数：它在一侧增加概率，在另一侧减去相同的量，并且每隔半个周期翻转一次符号。平均位置随之摆动：
``````

$$
\langle x \rangle(t) = \frac{L}{2} + \cos\omega t \int_0^L x\,\psi_1\psi_2\,dx = \frac{L}{2} - \frac{16L}{9\pi^2}\cos\omega t
$$

- For an electron, an oscillating $\langle x \rangle$ is an oscillating electric dipole: a tiny antenna that emits or absorbs light of angular frequency $\omega$, that is photons with $h\nu = E_2 - E_1$. This is the link to the colors of conjugated molecules in the applications below. The general theory is in [Time Dependence](06-time-dependence.md).


``````{admonition} 中文翻译
:class: dropdown

- 对于电子，振荡的 $\langle x \rangle$ 就是一个振荡的电偶极：一个微小的天线，以角频率 $\omega$ 发射或吸收光，即能量为 $h\nu = E_2 - E_1$ 的光子。这就是下面应用中与共轭分子颜色之间的联系。一般理论见[含时演化](06-time-dependence.md)。
``````

### Quantum PIB in 3D

:::{figure} ./images/pib3d.png
:label: fig-particle-in-a-box-3
:alt: pib1
:width: 300px

Particle in a 3D box subject to infinitely high potential walls.


``````{admonition} 中文翻译
:class: dropdown

受到无限高势壁束缚的三维势阱中的粒子。
``````
:::

$$\hat{H}\psi(x,y,z) = E\psi(x,y,z)$$


$${-\frac{\hbar^2}{2m}\left(\frac{\partial^2\psi}{\partial x^2} + \frac{\partial^2\psi}{\partial y^2} + \frac{\partial^2\psi}{\partial z^2}\right) = E\psi}$$

- Where we set $V=0$ for particle inside the box and enforce the solutions $\psi$ to be normalized within the confines of the box (electron must be somewhere in the box!)


``````{admonition} 中文翻译
:class: dropdown

- 其中我们对势阱内部的粒子设 $V=0$，并要求解 $\psi$ 在势阱范围内归一化（电子一定在势阱内的某处！）
``````

$${\int\limits_{-\infty}^{\infty}\int\limits_{-\infty}^{\infty}\int\limits_{-\infty}^{\infty}\left|\psi(x,y,z)\right|^2dxdydz = 1}$$

- Consider a particle in a box with side lengths $a$ in $x$, $b$ in $y$, and $c$ in $z$. The potential is zero inside the box and infinite outside it. Again, the potential term can be handled by boundary conditions (i.e., infinite potential implies that the wavefunction must be zero there). The above equation can now be written as:


``````{admonition} 中文翻译
:class: dropdown

- 考虑一个边长分别为 $x$ 方向 $a$、$y$ 方向 $b$、$z$ 方向 $c$ 的势阱中的粒子。势在势阱内部为零，外部为无限大。同样，势能项可以通过边界条件来处理（即无限大势意味着波函数在那里必须为零）。上述方程现在可以写为：
``````

$${-\frac{\hbar^2}{2m}\Delta\psi = E\psi} \\
{\textnormal{with }\psi(a,y,z) = \psi(x,b,z) = \psi(x,y,c) = 0} \\
{\textnormal{and }\psi(0,y,z) = \psi(x,0,z) = \psi(x,y,0) = 0}$$

- **Note the Laplacian symbol $\Delta$**, which concisely denotes the sum of the three second-order derivatives with respect to the spatial variables. We will see this operator in all 3D problems.
- In general, when the potential term can be expressed as a sum of terms that depend separately on $x$, $y$, and $z$, the solutions can be written as a product:


``````{admonition} 中文翻译
:class: dropdown

- **注意拉普拉斯算符符号 $\Delta$**，它简洁地表示对空间变量的三个二阶导数之和。我们将在所有三维问题中见到这个算符。
- 一般来说，当势能项可以表示为分别依赖于 $x$、$y$ 和 $z$ 的项之和时，解可以写成乘积形式：
``````

$${\psi(x,y,z) = X(x)Y(y)Z(z)}$$

- By substituting and dividing by $X(x)Y(y)Z(z)$, we obtain:


``````{admonition} 中文翻译
:class: dropdown

- 通过代入并除以 $X(x)Y(y)Z(z)$，我们得到：
``````

$${-\frac{\hbar^2}{2m}\left[\frac{1}{X(x)}\frac{d^2X(x)}{dx^2} + \frac{1}{Y(y)}\frac{d^2Y(y)}{dy^2} + \frac{1}{Z(z)}\frac{d^2Z(z)}{dz^2}\right] = E}$$

- The total energy $E$ consists of a sum of three terms, each depending separately on $x$, $y$, and $z$. Thus we can write $E = E_x + E_y + E_z$ and separate the equation into three one-dimensional problems:


``````{admonition} 中文翻译
:class: dropdown

- 总能量 $E$ 由三项之和组成，每一项分别依赖于 $x$、$y$ 和 $z$。因此我们可以写 $E = E_x + E_y + E_z$，并把方程分离成三个一维问题：
``````

$${-\frac{\hbar^2}{2m}\left[\frac{1}{X(x)}\frac{d^2X(x)}{dx^2}\right] = E_x\textnormal{ with }X(0) = X(a) = 0}\\
{-\frac{\hbar^2}{2m}\left[\frac{1}{Y(y)}\frac{d^2Y(y)}{dy^2}\right] = E_y\textnormal{ with }Y(0) = Y(b) = 0}\\
{-\frac{\hbar^2}{2m}\left[\frac{1}{Z(z)}\frac{d^2Z(z)}{dz^2}\right] = E_z\textnormal{ with }Z(0) = Z(c) = 0}$$

- Thus we find energy quantization due to spatial confinement of the quantum wave function in the $x$, $y$, and $z$ dimensions:


``````{admonition} 中文翻译
:class: dropdown

- 因此，我们发现能量的量子化源于量子波函数在 $x$、$y$ 和 $z$ 维度上的空间束缚：
``````

$${X(x) = \sqrt{\frac{2}{a}}\sin\left(\frac{n_x\pi x}{a}\right)}\\
{Y(y) = \sqrt{\frac{2}{b}}\sin\left(\frac{n_y\pi y}{b}\right)}\\
{Z(z) = \sqrt{\frac{2}{c}}\sin\left(\frac{n_z\pi z}{c}\right)}$$

:::{important} **Eigenfunctions and eigenvalues of particle in 3D Box**

**Rectangular Box**

$${\psi(x,y,z) = X(x)Y(y)Z(z) = \sqrt{\frac{8}{abc}}\sin\left(\frac{n_x\pi x}{a}\right)\sin\left(\frac{n_y\pi y}{b}\right)\sin\left(\frac{n_z\pi z}{c}\right)}$$

$${E_{n_x,n_y,n_z} = \frac{h^2}{8m}\left(\frac{n_x^2}{a^2} + \frac{n_y^2}{b^2} + \frac{n_z^2}{c^2}\right)}$$

**Cubic Box**

$$
\psi_{n_x, n_y, n_z}(x, y, z) = \frac{2}{L^{3/2}} \sin\left( \frac{n_x \pi x}{L} \right) \sin\left( \frac{n_y \pi y}{L} \right) \sin\left( \frac{n_z \pi z}{L} \right)
$$


$$
E_{n_x, n_y, n_z} = \frac{\hbar^2 \pi^2}{2mL^2} \left( n_x^2 + n_y^2 + n_z^2 \right)
$$


:::


- Energy is quantized and when $a = b = c$, we find that the energy levels can also be **degenerate** (i.e., the same energy with different values of $n_x, n_y$ and $n_z$).

- In most cases, **degeneracy in quantum mechanics arises from symmetry**. When $a = b = c$, the first excited level is triply degenerate: $(2,1,1)$, $(1,2,1)$ and $(1,1,2)$ are one shape turned to face different axes. When only $a = b \neq c$, that level splits into a pair and a single state; the pair lies lower when $c$ is shorter than $a$.


``````{admonition} 中文翻译
:class: dropdown

- 能量是量子化的，当 $a = b = c$ 时，我们发现能级也可以是**简并**的（即相同的能量对应不同的 $n_x, n_y$ 和 $n_z$ 值）。
- 在大多数情况下，**量子力学中的简并源于对称性**。当 $a = b = c$ 时，第一激发态是三重简并的：$(2,1,1)$、$(1,2,1)$ 和 $(1,1,2)$ 是同一个形状转向不同的轴。当只有 $a = b \neq c$ 时，该能级分裂成一对和一个单态；当 $c$ 比 $a$ 短时，这一对位于更低处。
``````


:::{admonition} **Table of energy levels for a cubic box**
:class: dropdown

Energies in units of $E_0 = \dfrac{h^2}{8mL^2}$, so $E = (n_x^2 + n_y^2 + n_z^2)\,E_0$. The degeneracy $g$ counts the states on each level.


``````{admonition} 中文翻译
:class: dropdown

能量以 $E_0 = \dfrac{h^2}{8mL^2}$ 为单位，因此 $E = (n_x^2 + n_y^2 + n_z^2)\,E_0$。简并度 $g$ 统计每个能级上的态数。
``````

| $n_x^2 + n_y^2 + n_z^2$ | states $(n_x, n_y, n_z)$ | degeneracy $g$ |
| :-- | :-- | :-- |
| 3 | (1,1,1) | 1 |
| 6 | (2,1,1), (1,2,1), (1,1,2) | 3 |
| 9 | (2,2,1), (2,1,2), (1,2,2) | 3 |
| 11 | (3,1,1), (1,3,1), (1,1,3) | 3 |
| 12 | (2,2,2) | 1 |
| 14 | all six orderings of (3,2,1) | 6 |
| 17 | (3,2,2), (2,3,2), (2,2,3) | 3 |
| 18 | (4,1,1), (1,4,1), (1,1,4) | 3 |
| 19 | (3,3,1), (3,1,3), (1,3,3) | 3 |
| 21 | all six orderings of (4,2,1) | 6 |
| 22 | (3,3,2), (3,2,3), (2,3,3) | 3 |
| 24 | (4,2,2), (2,4,2), (2,2,4) | 3 |
| 26 | all six orderings of (4,3,1) | 6 |
| 27 | (3,3,3) and the three orderings of (5,1,1) | 4 |

The last row is an **accidental** degeneracy: $3^2 + 3^2 + 3^2 = 5^2 + 1^2 + 1^2$, and no rotation of the cube turns $(3,3,3)$ into $(5,1,1)$.


``````{admonition} 中文翻译
:class: dropdown

最后一行是一个**偶然**简并：$3^2 + 3^2 + 3^2 = 5^2 + 1^2 + 1^2$，且立方体的任何旋转都不能把 $(3,3,3)$ 变成 $(5,1,1)$。
``````
:::


```{marimo} python
:hide-code: true

nx3 = mo.ui.slider(1, 4, step=1, value=2, show_value=True, label="nx")
ny3 = mo.ui.slider(1, 4, step=1, value=1, show_value=True, label="ny")
nz3 = mo.ui.slider(1, 4, step=1, value=1, show_value=True, label="nz")
mo.hstack([nx3, ny3, nz3], justify="start", gap=2)
```

```{marimo} python
:hide-code: true

side3 = 10.0
g3 = np.linspace(0, side3, 48)
X3, Y3, Z3 = np.meshgrid(g3, g3, g3, indexing="ij")

def psi1d_m(q, n_q):
    return np.sqrt(2 / side3) * np.sin(n_q * np.pi * q / side3)

psi_3d = psi1d_m(X3, nx3.value) * psi1d_m(Y3, ny3.value) * psi1d_m(Z3, nz3.value)
amp3 = 0.5 * np.abs(psi_3d).max()

fig3d = go.Figure(data=go.Isosurface(
    x=X3.flatten(), y=Y3.flatten(), z=Z3.flatten(), value=psi_3d.flatten(),
    colorscale="RdBu", isomin=-amp3, isomax=amp3, surface_count=2,
    showscale=False, caps=dict(x_show=False, y_show=False, z_show=False),
))
fig3d.update_layout(
    scene=dict(xaxis_title="x", yaxis_title="y", zaxis_title="z", aspectmode="data"),
    width=680, height=460,
    title_text=f"wavefunction isosurfaces, state ({nx3.value}, {ny3.value}, {nz3.value})",
)
fig3d
```

Fig. Surfaces of constant $\psi_{n_x n_y n_z}$ in a cubic box, red and blue for the two signs. Set $(2,1,1)$ and then $(1,2,1)$: the same shape turned by $90°$, so the two states share an energy.


``````{admonition} 中文翻译
:class: dropdown

图。立方体势阱中 $\psi_{n_x n_y n_z}$ 的等值面，红色和蓝色表示两种符号。先设 $(2,1,1)$，再设 $(1,2,1)$：同一个形状旋转 $90°$，因此这两个态具有相同的能量。
``````

- The level diagram below does the counting. Each short bar is one state. With all three sides equal, states related by a rotation of the box share a level; stretch or squeeze one side and those levels split.


``````{admonition} 中文翻译
:class: dropdown

- 下面的能级图完成了统计。每个短横条代表一个态。当三个边长相等时，由势阱旋转相关联的态共享一个能级；拉伸或挤压其中一个边长，这些能级就会分裂。
``````

```{marimo} python
:hide-code: true

side_a = mo.ui.slider(0.5, 2.0, step=0.05, value=1.0, show_value=True, label="side a (units of L)")
side_b = mo.ui.slider(0.5, 2.0, step=0.05, value=1.0, show_value=True, label="side b")
side_c = mo.ui.slider(0.5, 2.0, step=0.05, value=1.0, show_value=True, label="side c")
mo.hstack([side_a, side_b, side_c], justify="start", gap=2)
```

```{marimo} python
:hide-code: true

_s = (side_a.value, side_b.value, side_c.value)
_E = {}
for _i in range(1, 9):
    for _j in range(1, 9):
        for _k in range(1, 9):
            _E[(_i, _j, _k)] = _i**2 / _s[0]**2 + _j**2 / _s[1]**2 + _k**2 / _s[2]**2
_levels = []
for _st in sorted(_E, key=_E.get):
    if _levels and abs(_E[_st] - _levels[-1][0]) < 1e-6:
        _levels[-1][1].append(_st)
    else:
        _levels.append([_E[_st], [_st]])
_levels = _levels[:7]
_top = _levels[-1][0] * 1.08
_fig, _ax = plt.subplots(figsize=(7, 4.2))
_ylab = -1.0
for _Eg, _ss in _levels:
    _g = len(_ss)
    _col = PURPLE if _g > 1 else TEAL
    for _q in range(_g):
        _ax.hlines(_Eg, 0.1 + 0.34 * _q, 0.38 + 0.34 * _q, color=_col, lw=3.2)
    _ylab = max(_Eg, _ylab + 0.055 * _top)                  # keep labels of close levels apart
    _lab = f"g = {_g}:  " + ", ".join(f"({_a},{_b},{_c})" for _a, _b, _c in _ss) if _g <= 3 else f"g = {_g}"
    _ax.text(2.2, _ylab, _lab, va="center", fontsize=10, color=_col)
_ax.set_xlim(0, 5.4); _ax.set_ylim(0, _top)
_ax.set_xticks([]); _ax.set_yticks([]); _ax.spines["bottom"].set_visible(False)
_ax.set_ylabel(r"energy (units of $h^2/8mL^2$)")
_ax.set_title(f"sides a, b, c = {_s[0]:.2f}, {_s[1]:.2f}, {_s[2]:.2f}: the seven lowest levels", loc="left", fontsize=11)
_fig.tight_layout()
_fig
```

Fig. The seven lowest levels of a particle in a rectangular box. Each bar is one state and $g$ counts the states on a level. A cube has levels with $g = 1, 3, 3, 3, 1, 6, 3$; changing one side breaks the symmetry and splits them.


``````{admonition} 中文翻译
:class: dropdown

图。长方体势阱中粒子的七个最低能级。每个横条代表一个态，$g$ 统计一个能级上的态数。立方体具有 $g = 1, 3, 3, 3, 1, 6, 3$ 的能级；改变一个边长会破坏对称性并使它们分裂。
``````

### Note on Computing Average Properties from a Wave Function

Because of the probabilistic interpretation of the wave function, average properties can be computed from the wave function.  The general formula is


``````{admonition} 中文翻译
:class: dropdown

由于波函数的概率解释，平均性质可以从波函数计算出来。一般公式为
``````

$$
\langle A \rangle = \int \psi^*(x)\hat{A}\psi(x)dx
$$

where $\hat{A}$ is any operator. This could be momentum, kinetic energy, and so on. Below are a few problems illustrating how to do such calculations.


``````{admonition} 中文翻译
:class: dropdown

其中 $\hat{A}$ 是任意算符。它可以是动量、动能等等。下面是几个说明如何进行这类计算的例题。
``````

To calculate the average position (or **expectation value** of position) for a particle in a 1D box, follow the steps shown in the example below.


``````{admonition} 中文翻译
:class: dropdown

要计算一维势阱中粒子的平均位置（或位置的**期望值**），请按照下面例题中所示的步骤进行。
``````

:::{note} **Example: Calculate average (expectation) of position, $\langle x\rangle$**
:class: dropdown

**1. Wavefunction of the Particle in a 1D Box**


``````{admonition} 中文翻译
:class: dropdown

**1. 一维势阱中粒子的波函数**
``````

The wavefunction for a particle in a 1D box of length $L$ with infinite potential walls at $x = 0$ and $x = L$ is given by:


``````{admonition} 中文翻译
:class: dropdown

长度为 $L$、在 $x = 0$ 和 $x = L$ 处有无限高势壁的一维势阱中粒子的波函数为：
``````

$$
\psi_n(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{n\pi x}{L}\right)
$$

where:
- $n$ is the quantum number (1, 2, 3, ...),
- $L$ is the length of the box,
- $\psi_n(x)$ is the wavefunction.


``````{admonition} 中文翻译
:class: dropdown

- $n$ 是量子数（1, 2, 3, ...），
- $L$ 是势阱的长度，
- $\psi_n(x)$ 是波函数。
``````

**2. Expectation Value of Position $\langle x \rangle$**


``````{admonition} 中文翻译
:class: dropdown

**2. 位置的期望值 $\langle x \rangle$**
``````

The expectation value of the position $x$ for a particle is given by:


``````{admonition} 中文翻译
:class: dropdown

粒子位置 $x$ 的期望值为：
``````

$$
\langle x \rangle = \int_0^L x |\psi_n(x)|^2 \, dx
$$

This integral gives the average position of the particle based on the probability density $|\psi_n(x)|^2$. For the wavefunction $\psi_n(x)$, the probability density is:


``````{admonition} 中文翻译
:class: dropdown

该积分根据概率密度 $|\psi_n(x)|^2$ 给出粒子的平均位置。对于波函数 $\psi_n(x)$，概率密度为：
``````

$$
|\psi_n(x)|^2 = \left( \sqrt{\frac{2}{L}} \sin\left(\frac{n\pi x}{L}\right) \right)^2 = \frac{2}{L} \sin^2\left(\frac{n\pi x}{L}\right)
$$

**3. Set Up the Integral**

Substitute $|\psi_n(x)|^2$ into the expression for $\langle x \rangle$:


``````{admonition} 中文翻译
:class: dropdown

将 $|\psi_n(x)|^2$ 代入 $\langle x \rangle$ 的表达式：
``````

$$
\langle x \rangle = \int_0^L x \frac{2}{L} \sin^2\left(\frac{n\pi x}{L}\right) \, dx
$$

This is the integral you need to solve to find the average position.


``````{admonition} 中文翻译
:class: dropdown

这就是你需要求解以得到平均位置的积分。
``````

**4. Solve the Integral**

The integral can be simplified using known trigonometric identities. First, use the identity:


``````{admonition} 中文翻译
:class: dropdown

该积分可以利用已知的三角恒等式化简。首先使用恒等式：
``````

$$
\sin^2 \theta = \frac{1}{2} \left(1 - \cos(2\theta)\right)
$$

So, the integral becomes:

$$
\langle x \rangle = \frac{2}{L} \int_0^L x \left( \frac{1}{2} \left( 1 - \cos\left( \frac{2n\pi x}{L} \right) \right) \right) dx
$$

Simplifying:

$$
\langle x \rangle = \frac{1}{L} \int_0^L x \left( 1 - \cos\left( \frac{2n\pi x}{L} \right) \right) dx
$$

Now split this into two integrals:

$$
\langle x \rangle = \frac{1}{L} \left( \int_0^L x \, dx - \int_0^L x \cos\left( \frac{2n\pi x}{L} \right) dx \right)
$$

**5. Evaluate the Integrals**

- The first integral is straightforward:

$$
\int_0^L x \, dx = \frac{L^2}{2}
$$

- The second integral can be solved using integration by parts or by referring to standard integral tables. It turns out that this integral evaluates to 0 for any integer $n$. Thus:


``````{admonition} 中文翻译
:class: dropdown

- 第二个积分可以用分部积分法求解，或查阅标准积分表。结果是，对于任意整数 $n$，这个积分的值为 0。因此：
``````

$$
\int_0^L x \cos\left( \frac{2n\pi x}{L} \right) dx = 0
$$

**6. Final Result**

Thus, the expectation value of position simplifies to:


``````{admonition} 中文翻译
:class: dropdown

于是，位置的期望值化简为：
``````

$$
\langle x \rangle = \frac{1}{L} \times \frac{L^2}{2} = \frac{L}{2}
$$

**7. Interpretation**

For any quantum state $n$, the average position $\langle x \rangle$ of a particle in a 1D box is always:


``````{admonition} 中文翻译
:class: dropdown

对于任意量子态 $n$，一维势阱中粒子的平均位置 $\langle x \rangle$ 总是：
``````

$$
\langle x \rangle = \frac{L}{2}
$$

This result makes sense intuitively because, due to the symmetry of the problem, the particle is equally likely to be found on either side of the box, so its average position is right in the middle of the box at $x = \frac{L}{2}$.


``````{admonition} 中文翻译
:class: dropdown

这个结果在直观上是有道理的，因为由于问题的对称性，粒子在势阱两侧被找到的可能性相等，所以其平均位置恰好在势阱正中间 $x = \frac{L}{2}$ 处。
``````

**Summary**

To find the average position of a particle in a 1D box for a general wavefunction:


``````{admonition} 中文翻译
:class: dropdown

对于一般波函数，求一维势阱中粒子的平均位置：
``````
- Use the wavefunction $\psi_n(x)$,
- Set up the expectation value integral $\langle x \rangle = \int_0^L x\,|\psi_n(x)|^2 \, dx$,
- Solve the integral, which results in $\langle x \rangle = \frac{L}{2}$ for all $n$.


``````{admonition} 中文翻译
:class: dropdown

- 使用波函数 $\psi_n(x)$，
- 建立期望值积分 $\langle x \rangle = \int_0^L x\,|\psi_n(x)|^2 \, dx$，
- 求解积分，对于所有 $n$ 结果都是 $\langle x \rangle = \frac{L}{2}$。
``````

Thus, the particle's average position is always at the midpoint of the box, independent of the quantum number $n$.


``````{admonition} 中文翻译
:class: dropdown

因此，粒子的平均位置总是在势阱的中点，与量子数 $n$ 无关。
``````
:::


### Applications: electronic transitions in conjugated molecules

One of the most useful applications of the particle in a box is estimating the color of light absorbed by **π-conjugated molecules**. In molecules with alternating single and double bonds, the π-electrons are **delocalized** over the conjugated region and behave, to a first approximation, like particles confined to a box whose length is the length of the conjugated chain.


``````{admonition} 中文翻译
:class: dropdown

一维无限深势阱最有用的应用之一是估算**π 共轭分子**吸收的光的颜色。在单键和双键交替的分子中，π 电子在整个共轭区域内**离域**，作为一级近似，它们的行为就像被限制在长度等于共轭链长的势阱中的粒子。
``````

:::{figure} images/pib1d-1.jpeg
:width: 70%

A linear conjugated system (a polyene) modeled as a 1D particle in a box: the delocalized π-electrons are confined to the length of the conjugated chain.


``````{admonition} 中文翻译
:class: dropdown

一个线形共轭体系（多烯）被建模为一维无限深势阱：离域的 π 电子被限制在共轭链的长度范围内。
``````
:::

- **1D box** models linear conjugated systems such as butadiene and longer polyenes. The box length is the length of the conjugated chain, and the level spacing sets the wavelength of light absorbed.
- **2D box** models π-electrons delocalized over a two-dimensional region, such as aromatic rings or graphene fragments.


``````{admonition} 中文翻译
:class: dropdown

- **一维势阱**用于建模线形共轭体系，如丁二烯和更长的多烯。势阱长度就是共轭链的长度，能级间距决定了所吸收光的波长。
- **二维势阱**用于建模在二维区域内离域的 π 电子，如芳香环或石墨烯碎片。
``````

:::{figure} images/pib-applic2.jpeg
:width: 70%

Aromatic and extended π-systems modeled as a 2D particle in a box.


``````{admonition} 中文翻译
:class: dropdown

芳香族和扩展的 π 体系被建模为二维势阱中的粒子。
``````
:::

#### Worked example: butadiene

Consider butadiene (C₄H₆), whose four π-electrons are delocalized over the conjugated chain. We estimate the wavelength that excites one π-electron across the gap.


``````{admonition} 中文翻译
:class: dropdown

考虑丁二烯（C₄H₆），它的四个 π 电子在共轭链上离域。我们估算把一个 π 电子激发越过能隙所需的波长。
``````

**Step 1: length of the box.** Butadiene, CH₂=CH-CH=CH₂, has two C=C bonds and one C-C bond between its end carbons (C=C ≈ 1.35 Å, C-C ≈ 1.54 Å):


``````{admonition} 中文翻译
:class: dropdown

**第 1 步：势阱的长度。** 丁二烯 CH₂=CH-CH=CH₂ 在其末端碳原子之间有两个 C=C 键和一个 C-C 键（C=C ≈ 1.35 Å，C-C ≈ 1.54 Å）：
``````

$$
L = 1.35\,\text{Å} + 1.54\,\text{Å} + 1.35\,\text{Å} = 4.24\,\text{Å}.
$$

**Step 2: fill the levels.** Each level holds two electrons (Pauli), so the four π-electrons fill $n=1$ and $n=2$. The highest occupied level is $n=2$ and the lowest empty one is $n=3$, so the absorption is the $n=2 \to n=3$ transition.


``````{admonition} 中文翻译
:class: dropdown

**第 2 步：填充能级。** 每个能级容纳两个电子（泡利原理），因此四个 π 电子填满 $n=1$ 和 $n=2$。最高占据能级是 $n=2$，最低空能级是 $n=3$，因此吸收对应 $n=2 \to n=3$ 的跃迁。
``````

**Step 3: transition energy and wavelength.** With $E_n = \dfrac{n^2 h^2}{8mL^2}$, the absorbed photon satisfies


``````{admonition} 中文翻译
:class: dropdown

**第 3 步：跃迁能量和波长。** 由 $E_n = \dfrac{n^2 h^2}{8mL^2}$，被吸收的光子满足
``````

$$
\Delta E = E_3 - E_2 = \frac{(3^2 - 2^2)h^2}{8mL^2} = \frac{hc}{\lambda}.
$$

```{code-cell} python
:tags: [hide-input]
import numpy as np

h = 6.626e-34    # Planck constant (J s)
m = 9.109e-31    # electron mass (kg)
c = 3.0e8        # speed of light (m/s)
# box ending at the end carbons, then one carbon radius (0.77 A) past each end
for label, L in [("L = 4.24 A", 4.24e-10), ("L = 5.78 A", 5.78e-10)]:
    E = lambda n: n**2 * h**2 / (8 * m * L**2)
    dE = E(3) - E(2)             # HOMO (n=2) -> LUMO (n=3)
    lam = h * c / dE
    print(f"{label}:  Delta E (2 -> 3) = {dE:.3e} J,  absorption wavelength = {lam * 1e9:.0f} nm")
```

With the box ending at the end carbons, the estimate (about 119 nm) lands deep in the ultraviolet, well short of the measured 217 nm. The π-electrons do not stop at the end carbons, though: extending the box by one carbon radius (0.77 Å) past each end gives $L = 5.78$ Å and about 220 nm, close to experiment. The simple model captures the key trend: **longer conjugation means a longer box, smaller level spacing, and absorption shifted toward the red**, which is why extended π-systems like carotenes are colored.


``````{admonition} 中文翻译
:class: dropdown

如果把势阱的端点设在末端碳原子处，估算值（约 119 nm）落在远紫外区，远短于实测的 217 nm。不过，π 电子并不会在末端碳原子处停下：把势阱向每端各延伸一个碳原子半径（0.77 Å），得到 $L = 5.78$ Å 和约 220 nm，与实验接近。这个简单模型抓住了关键趋势：**共轭越长，势阱越长，能级间距越小，吸收向红光方向移动**，这就是为什么类胡萝卜素等扩展 π 体系呈现颜色。
``````

### Problems

#### Problem 1: Compute probability of finding particle somewhere

Compute the probability of observing the particle in a box in the domain $\frac{a}{3} \leq x \leq \frac{2a}{3}$.


``````{admonition} 中文翻译
:class: dropdown

计算在区域 $\frac{a}{3} \leq x \leq \frac{2a}{3}$ 内观测到势阱中粒子的概率。
``````

:::{admonition} **Solution**
:class: dropdown solution

Since the square of the wave function is a probability density, we can determine the probability of observing the particle in a particular domain using the relationship


``````{admonition} 中文翻译
:class: dropdown

由于波函数的平方是概率密度，我们可以利用如下关系确定在特定区域内观测到粒子的概率
``````

$$\begin{equation}
\text{Prob}(x_1 \leq x \leq x_2) = \int_{x_1}^{x_2}P(x)dx = \int_{x_1}^{x_2} \psi^*(x)\psi(x)dx
\end{equation}$$

We simply use the above equation together with the normalized particle-in-a-box wave function:


``````{admonition} 中文翻译
:class: dropdown

我们只需把上面的方程与归一化的一维无限深势阱波函数一起使用：
``````

$$\begin{align}
\text{Prob}(\frac{a}{3} \leq x \leq \frac{2a}{3}) = \frac{2}{a}\int_{\frac{a}{3}}^{\frac{2a}{3}} \sin^2\frac{n\pi x}{a}dx
\end{align}$$

We will use the definite integral of $\sin^2ax$ from a table:


``````{admonition} 中文翻译
:class: dropdown

我们将使用积分表中 $\sin^2ax$ 的定积分：
``````

$$\begin{equation}
\int\sin^2axdx = \frac{x}{2} - \frac{\sin2ax}{4a}
\end{equation}$$

Perform a $u$-substitution on the integral above to put it into the table form:


``````{admonition} 中文翻译
:class: dropdown

对上面的积分进行 $u$ 代换，使其化为积分表中的形式：
``````

$$\begin{align}
\text{Prob}(\frac{a}{3} \leq x \leq \frac{2a}{3}) &= \frac{2}{a}\left[ \frac{x}{2} - \frac{\sin\frac{2n\pi x}{a}}{\frac{4n\pi}{a}}\right]_{\frac{a}{3}}^{\frac{2a}{3}} \\
&= \frac{2}{a}\left[ \frac{x}{2} - \frac{a\sin\frac{2n\pi x}{a}}{4n\pi}\right]_{\frac{a}{3}}^{\frac{2a}{3}} \\
&= \frac{2}{a}\left[ \frac{a}{3} - \frac{a\sin\frac{4n\pi}{3}}{4n\pi} - \frac{a}{6} + \frac{a\sin\frac{2n\pi }{3}}{4n\pi}\right] \\
&= 2\left[ \frac{1}{6}  + \frac{\sin\frac{2n\pi }{3} - \sin\frac{4n\pi}{3}}{4n\pi}\right]
\end{align}$$
:::

#### Problem 2: Compute an expectation of $x^2$

Compute the average of $x^2$ for a particle in a box.


``````{admonition} 中文翻译
:class: dropdown

计算一维无限深势阱中粒子的 $x^2$ 的平均值。
``````

:::{admonition} **Solution**
:class: dropdown solution

To compute the average value of $x^2$, we start by writing the integral expression:


``````{admonition} 中文翻译
:class: dropdown

为了计算 $x^2$ 的平均值，我们先写出积分表达式：
``````

$$\begin{equation}
\langle x^2 \rangle = \int \psi^*(x) x^2 \psi(x)dx
\end{equation}$$

For the particle in a box, we can limit the domain, and thus the bounds of integration, to $0\leq x \leq a$. We can also set $\psi_n(x) = \sqrt{\frac{2}{a}}\sin\frac{n\pi x}{a}$.


``````{admonition} 中文翻译
:class: dropdown

对于一维无限深势阱，我们可以把区域以及积分上下限限制在 $0\leq x \leq a$。我们还可以设 $\psi_n(x) = \sqrt{\frac{2}{a}}\sin\frac{n\pi x}{a}$。
``````

Thus, for a particle in a 1D box of size $a$, we get


``````{admonition} 中文翻译
:class: dropdown

因此，对于尺寸为 $a$ 的一维势阱中的粒子，我们得到
``````

$$\begin{align}
\langle x^2 \rangle &= \int_0^a \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi x}{a}\right) x^2 \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi x}{a}\right)dx \\
&= \frac{2}{a} \int_0^a x^2 \sin^2\frac{n\pi x}{a}dx
\end{align}$$

From an integral table we find that

$$\begin{equation}
\int x^2\sin^2\alpha xdx = \frac{x^3}{6} - \left(\frac{x^2}{4\alpha} - \frac{1}{8\alpha^3}\right)\sin2\alpha x - \frac{x\cos 2\alpha x}{4\alpha^2} + C
\end{equation}$$

We use this equation with $\alpha = \frac{n\pi}{a}$ and get:


``````{admonition} 中文翻译
:class: dropdown

我们把此方程与 $\alpha = \frac{n\pi}{a}$ 一起使用，得到：
``````

$$\begin{align}
\langle x^2 \rangle &= \int_0^a \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi x}{a}\right) x^2 \sqrt{\frac{2}{a}}\sin\left(\frac{n\pi x}{a}\right)dx \\
&= \frac{2}{a} \int_0^a x^2 \sin^2\frac{n\pi x}{a}dx \\
&= \frac{2}{a}\left[ \frac{x^3}{6} - \left(\frac{x^2}{4\alpha} - \frac{1}{8\alpha^3}\right)\sin2\alpha x - \frac{x\cos 2\alpha x}{4\alpha^2}\right]_0^a \\
&= \frac{2}{a}\left[ \frac{a^3}{6} - \left(\frac{a^2}{4\alpha} - \frac{1}{8\alpha^3}\right)\sin2\alpha a - \frac{a\cos 2\alpha a}{4\alpha^2} \right] \\
&= \frac{2}{a}\left[ \frac{a^3}{6} - \left(\frac{a^2}{4\frac{n\pi}{a}} - \frac{1}{8\left(\frac{n\pi}{a}\right)^3}\right)\sin2\frac{n\pi}{a} a - \frac{a\cos 2\frac{n\pi}{a} a}{4\left(\frac{n\pi}{a}\right)^2} \right] \\
&= \frac{2}{a}\left[ \frac{a^3}{6} - \frac{a^3}{\left(2n\pi\right)^2} \right] \\
&=  \frac{a^2}{3} - \frac{a^2}{2\left(n\pi\right)^2} 
\end{align}$$

This result, combined with the result for $\langle x \rangle$, can be used to determine $\sigma_x$, the standard deviation of the particle's position:


``````{admonition} 中文翻译
:class: dropdown

这个结果与 $\langle x \rangle$ 的结果结合，可以用来确定 $\sigma_x$，即粒子位置的标准差：
``````

$$\begin{equation}
\sigma_x = \sqrt{\langle x^2 \rangle - \langle x \rangle^2} = \frac{a}{2\pi n}\sqrt{\frac{\pi^2n^2}{3} -2}
\end{equation}$$
:::

#### Problem 3: Compute expectation of energy

Compute the average energy of a particle in a box.


``````{admonition} 中文翻译
:class: dropdown

计算一维无限深势阱中粒子的平均能量。
``````

:::{admonition} **Solution**
:class: dropdown solution

The average energy of the particle in a box is a special case of computing an average quantity. We start by writing out the standard definition of an average computed from a wavefunction:


``````{admonition} 中文翻译
:class: dropdown

一维无限深势阱中粒子的平均能量是计算平均量的一个特例。我们先写出由波函数计算平均值的标准定义：
``````

$$\begin{equation}
\langle E \rangle = \int_0^a \psi_n^*(x)\hat{E}\psi_n(x)dx
\end{equation}$$

where $\hat{E}$ is the total energy operator. We know the total energy operator by another symbol, namely $\hat{E} = \hat{H}$. We plug this into the above equation to get:


``````{admonition} 中文翻译
:class: dropdown

其中 $\hat{E}$ 是总能量算符。我们知道总能量算符有另一个符号，即 $\hat{E} = \hat{H}$。把它代入上面的方程得到：
``````

$$\begin{equation}
\langle E \rangle = \int_0^a \psi_n^*(x)\hat{H}\psi_n(x)dx.
\end{equation}$$

We now recognize that the particle-in-a-box wavefunctions we are discussing were derived from the Schrödinger equation:


``````{admonition} 中文翻译
:class: dropdown

现在我们认识到，我们讨论的一维无限深势阱波函数是从薛定谔方程导出的：
``````

$$\begin{equation}
\hat{H}\psi_n(x)  = E_n\psi_n(x)
\end{equation}$$

where $E_n$ is a scalar. Thus, for the average energy we get:


``````{admonition} 中文翻译
:class: dropdown

其中 $E_n$ 是标量。因此，对于平均能量我们得到：
``````

$$\begin{align}
\langle E \rangle &= \int_0^a \psi_n^*(x)\hat{H}\psi_n(x)dx \\
&=\int_0^a \psi_n^*(x)E_n\psi_n(x)dx \\
&=E_n\int_0^a \psi_n^*(x)\psi_n(x)dx \\
&= E_n
\end{align}$$

The last equality holds because the wave functions are normalized.


``````{admonition} 中文翻译
:class: dropdown

最后一个等号成立是因为波函数是归一化的。
``````
:::

#### Problem 4: Compute expectation of momentum

Compute the average momentum for a particle in a box.


``````{admonition} 中文翻译
:class: dropdown

计算一维无限深势阱中粒子的平均动量。
``````

:::{admonition} **Solution**
:class: dropdown solution

To compute the average momentum of a particle in a 1D box, we start in the usual way:


``````{admonition} 中文翻译
:class: dropdown

为了计算一维势阱中粒子的平均动量，我们照常开始：
``````

$$\begin{equation}
\langle p \rangle = \int_0^a \psi_n^*(x)\hat{p}\psi_n(x)dx
\end{equation}$$

Recall that the momentum operator in one dimension is given by


``````{admonition} 中文翻译
:class: dropdown

回想一维中的动量算符为
``````

$$\begin{equation}
\hat{p}_x = -i\hbar\frac{d}{dx}
\end{equation}$$

We now substitute this into the above equation and solve:


``````{admonition} 中文翻译
:class: dropdown

现在把它代入上面的方程并求解：
``````

$$\begin{align}
\langle p \rangle &= \int_0^a \psi_n^*(x)\left(-i\hbar\frac{d}{dx}\right)\psi_n(x)dx \\
&= -\frac{2i\hbar}{a}\int_0^a \sin\left(\frac{n\pi x}{a}\right)\frac{d}{dx}\left(\sin\left(\frac{n\pi x}{a}\right)\right)dx \\
&= -\frac{2i\hbar}{a}\int_0^a \sin\left(\frac{n\pi x}{a}\right)\frac{n\pi}{a}\cos\left(\frac{n\pi x}{a}\right)dx \\
&= -\frac{2in\pi\hbar}{a^2}\int_0^a \sin\left(\frac{n\pi x}{a}\right)\cos\left(\frac{n\pi x}{a}\right)dx \\
&= 0
\end{align}$$

where the last equality can be found in an integral table.


``````{admonition} 中文翻译
:class: dropdown

其中最后一个等号可以在积分表中找到。
``````

So the average momentum of a particle in a box is zero. This is because it is equally probable for the particle to be moving forward and backward.


``````{admonition} 中文翻译
:class: dropdown

因此，一维无限深势阱中粒子的平均动量为零。这是因为粒子向前和向后运动的可能性相等。
``````
:::

#### Problem 5

 Consider an electron in superfluid helium ($^4$He) where it forms a solvation cavity with a radius of $18 \text{Å}$. Calculate the zero-point energy and the energy difference between the ground and first excited states by approximating the electron by a particle in a 3-dimensional box.


``````{admonition} 中文翻译
:class: dropdown

考虑超流氦（$^4$He）中的一个电子，它形成一个半径为 $18 \text{Å}$ 的溶剂化空腔。通过把电子近似为三维势阱中的粒子，计算零点能和基态与第一激发态之间的能量差。
``````


:::{admonition} **Solution**
:class: dropdown solution

The zero-point energy can be obtained from the lowest-state energy ($n = 1$) with $a = b = c = 36 \text{Å}$. The first excited state is triply degenerate ($E_{112}$, $E_{121}$, and $E_{211}$).


``````{admonition} 中文翻译
:class: dropdown

零点能可以从最低态能量（$n = 1$）以及 $a = b = c = 36 \text{Å}$ 得到。第一激发态是三重简并的（$E_{112}$、$E_{121}$ 和 $E_{211}$）。
``````

$$E_{111} = \frac{h^2}{8m_e}\left(\frac{n_x^2}{a^2} + \frac{n_y^2}{b^2} + \frac{n_z^2}{c^2}\right)$$
$$= \frac{(6.626076\times 10^{-34}\textnormal{ Js})^2}{8(9.109390\times 10^{-31}\textnormal{ kg})}\left(\frac{1}{(36\times 10^{-10}\textnormal{ m})^2} + \frac{1}{(36\times 10^{-10}\textnormal{ m})^2} + \frac{1}{(36\times 10^{-10}\textnormal{ m})^2}\right)$$
$$= 1.39\times10^{-20}\textnormal{ J} = 87.0\textnormal{ meV}$$


$$E_{211} = E_{121} = E_{112} = \frac{(6.626076\times 10^{-34}\textnormal{ Js})^2}{8(9.109390\times 10^{-31}\textnormal{ kg})}$$
$$\times\left(\frac{2^2}{(36\times 10^{-10}\textnormal{ m})^2} + \frac{1^2}{(36\times 10^{-10}\textnormal{ m})^2} + \frac{1^2}{(36\times 10^{-10}\textnormal{ m})^2}\right)$$
$$= 2.79\times 10^{-20}\textnormal{ J} = 174\textnormal{ meV} \Rightarrow \Delta E = 87\textnormal{ meV}$$
(Experimental value: 105 meV; Phys. Rev. B 41, 6366 (1990))


``````{admonition} 中文翻译
:class: dropdown

（实验值：105 meV；Phys. Rev. B 41, 6366 (1990)）
``````

:::

#### Problem 6: Energy Levels in a 3D Box

A particle is confined in a 3D box with side lengths $L_x = L_y = L_z = L$. The energy levels for a particle in this box are given by the formula:


``````{admonition} 中文翻译
:class: dropdown

一个粒子被束缚在边长 $L_x = L_y = L_z = L$ 的三维势阱中。该势阱中粒子的能级由以下公式给出：
``````

$$E_{n_x, n_y, n_z} = \frac{\hbar^2 \pi^2}{2mL^2} \left( n_x^2 + n_y^2 + n_z^2 \right)$$

where $n_x$, $n_y$, $n_z$ are the quantum numbers associated with the particle's motion in the $x$-, $y$-, and $z$-directions.


``````{admonition} 中文翻译
:class: dropdown

其中 $n_x$、$n_y$、$n_z$ 是与粒子在 $x$、$y$ 和 $z$ 方向运动相关的量子数。
``````

Calculate the energy levels for the quantum states with $n_x = 1$, $n_y = 1$, $n_z = 2$ and $n_x = 2$, $n_y = 2$, $n_z = 1$. Are these energy levels degenerate?


``````{admonition} 中文翻译
:class: dropdown

计算量子态 $n_x = 1$、$n_y = 1$、$n_z = 2$ 和 $n_x = 2$、$n_y = 2$、$n_z = 1$ 的能级。这些能级简并吗？
``````

:::{admonition} **Solution**
:class: dropdown solution

The energy for the state $(n_x, n_y, n_z) = (1, 1, 2)$ is:


``````{admonition} 中文翻译
:class: dropdown

态 $(n_x, n_y, n_z) = (1, 1, 2)$ 的能量为：
``````

$$E_{1,1,2} = \frac{\hbar^2 \pi^2}{2mL^2} \left( 1^2 + 1^2 + 2^2 \right) = \frac{\hbar^2 \pi^2}{2mL^2} (1 + 1 + 4) = \frac{\hbar^2 \pi^2}{2mL^2} \times 6$$

The energy for the state $(n_x, n_y, n_z) = (2, 2, 1)$ is:


``````{admonition} 中文翻译
:class: dropdown

态 $(n_x, n_y, n_z) = (2, 2, 1)$ 的能量为：
``````

$$E_{2,2,1} = \frac{\hbar^2 \pi^2}{2mL^2} \left( 2^2 + 2^2 + 1^2 \right) = \frac{\hbar^2 \pi^2}{2mL^2} (4 + 4 + 1) = \frac{\hbar^2 \pi^2}{2mL^2} \times 9$$

Since $E_{1,1,2} \neq E_{2,2,1}$, these energy levels are **not degenerate**.


``````{admonition} 中文翻译
:class: dropdown

由于 $E_{1,1,2} \neq E_{2,2,1}$，这些能级**不简并**。
``````

:::

#### Problem 7: Degeneracy of Energy Levels

Consider a particle confined in a cubic box with side lengths $L_x = L_y = L_z = L$. The energy levels are given by the same formula as in Problem 6.


``````{admonition} 中文翻译
:class: dropdown

考虑一个束缚在边长 $L_x = L_y = L_z = L$ 的立方体势阱中的粒子。能级由与问题 6 相同的公式给出。
``````

- **Part 1:** Find the degeneracy of the energy level corresponding to the quantum number sum $n_x^2 + n_y^2 + n_z^2 = 14$.
- **Part 2:** Write down all the quantum number triplets $(n_x, n_y, n_z)$ that correspond to this energy level.


``````{admonition} 中文翻译
:class: dropdown

- **第 1 部分：** 求对应于量子数平方和 $n_x^2 + n_y^2 + n_z^2 = 14$ 的能级的简并度。
- **第 2 部分：** 写出对应于此能级的所有量子数三元组 $(n_x, n_y, n_z)$。
``````

:::{admonition} **Solution**
:class: dropdown solution

**Part 1:**
We want to find the quantum numbers that satisfy:


``````{admonition} 中文翻译
:class: dropdown

**第 1 部分：**
我们希望找到满足以下条件的量子数：
``````

$n_x^2 + n_y^2 + n_z^2 = 14$

We can check different combinations of $n_x$, $n_y$, and $n_z$:


``````{admonition} 中文翻译
:class: dropdown

我们可以检查 $n_x$、$n_y$ 和 $n_z$ 的不同组合：
``````

- For $n_x = 3$, $n_y = 2$, and $n_z = 1$:


``````{admonition} 中文翻译
:class: dropdown

- 对于 $n_x = 3$、$n_y = 2$ 和 $n_z = 1$：
``````

$$3^2 + 2^2 + 1^2 = 9 + 4 + 1 = 14$$

- Other permutations of these quantum numbers will give the same energy:


``````{admonition} 中文翻译
:class: dropdown

- 这些量子数的其他排列会给出相同的能量：
``````
  
  - $(3, 2, 1)$
  - $(3, 1, 2)$
  - $(2, 3, 1)$
  - $(2, 1, 3)$
  - $(1, 3, 2)$
  - $(1, 2, 3)$


``````{admonition} 中文翻译
:class: dropdown

- $(3, 2, 1)$
- $(3, 1, 2)$
- $(2, 3, 1)$
- $(2, 1, 3)$
- $(1, 3, 2)$
- $(1, 2, 3)$
``````

**Part 2:**
The energy level corresponding to $n_x^2 + n_y^2 + n_z^2 = 14$ has **6 degenerate states**, since the quantum number triplets are $(3, 2, 1)$, $(3, 1, 2)$, $(2, 3, 1)$, $(2, 1, 3)$, $(1, 3, 2)$, and $(1, 2, 3)$.


``````{admonition} 中文翻译
:class: dropdown

**第 2 部分：**
对应于 $n_x^2 + n_y^2 + n_z^2 = 14$ 的能级有 **6 个简并态**，因为量子数三元组是 $(3, 2, 1)$、$(3, 1, 2)$、$(2, 3, 1)$、$(2, 1, 3)$、$(1, 3, 2)$ 和 $(1, 2, 3)$。
``````

:::

#### Problem 8: Degeneracy of the Ground State

- **Part 1:** What is the degeneracy of the ground state (the lowest energy state) for a particle in a cubic box?
- **Part 2:** Explain why the ground state does not have degeneracy.


``````{admonition} 中文翻译
:class: dropdown

- **第 1 部分：** 立方体势阱中粒子的基态（最低能量态）的简并度是多少？
- **第 2 部分：** 解释为什么基态没有简并。
``````

:::{admonition} **Solution**
:class: dropdown solution

**Part 1:**
The ground state corresponds to the quantum numbers $n_x = n_y = n_z = 1$. The energy for this state is:


``````{admonition} 中文翻译
:class: dropdown

**第 1 部分：**
基态对应量子数 $n_x = n_y = n_z = 1$。这个态的能量为：
``````

$$E_{1,1,1} = \frac{\hbar^2 \pi^2}{2mL^2} \left( 1^2 + 1^2 + 1^2 \right) = \frac{\hbar^2 \pi^2}{2mL^2} \times 3$$

There is only **one** combination of quantum numbers that gives this energy, so the degeneracy of the ground state is **1**.


``````{admonition} 中文翻译
:class: dropdown

只有**一种**量子数组合给出这个能量，因此基态的简并度为 **1**。
``````

**Part 2:**
The ground state is non-degenerate because there is only one way to assign the quantum numbers $n_x = n_y = n_z = 1$. Degeneracy arises when multiple different sets of quantum numbers give the same energy, which is not the case for the ground state.


``````{admonition} 中文翻译
:class: dropdown

**第 2 部分：**
基态是非简并的，因为只有一种方式赋予量子数 $n_x = n_y = n_z = 1$。当多组不同的量子数给出相同能量时才会产生简并，而基态并非如此。
``````

:::

#### Problem 9: Higher Energy Degeneracy

Consider a particle in a cubic box. The energy levels are quantized as:


``````{admonition} 中文翻译
:class: dropdown

考虑立方体势阱中的一个粒子。能级量子化为：
``````

$$E_{n_x, n_y, n_z} = \frac{\hbar^2 \pi^2}{2mL^2} \left( n_x^2 + n_y^2 + n_z^2 \right)$$

- **Part 1:** Find the quantum numbers that give the same energy for the quantum number sum $n_x^2 + n_y^2 + n_z^2 = 9$. How many degenerate states correspond to this energy?
- **Part 2:** What is the degeneracy of this energy level?


``````{admonition} 中文翻译
:class: dropdown

- **第 1 部分：** 求对于量子数平方和 $n_x^2 + n_y^2 + n_z^2 = 9$ 给出相同能量的量子数。有多少个简并态对应这个能量？
- **第 2 部分：** 这个能级的简并度是多少？
``````

:::{admonition} **Solution**
:class: dropdown solution

**Part 1:**
We want to solve:

$n_x^2 + n_y^2 + n_z^2 = 9$

Possible combinations of $n_x$, $n_y$, and $n_z$:

- $n_x = 2$, $n_y = 2$, $n_z = 1$ gives $2^2 + 2^2 + 1^2 = 4 + 4 + 1 = 9$.
- Permutations of $(2, 2, 1)$ are:
  - $(2, 2, 1)$
  - $(2, 1, 2)$
  - $(1, 2, 2)$
- $(3, 0, 0)$ also gives 9, but it is not allowed: each quantum number is at least 1, since $n = 0$ makes $\psi = 0$.


``````{admonition} 中文翻译
:class: dropdown

- $n_x = 2$、$n_y = 2$、$n_z = 1$ 给出 $2^2 + 2^2 + 1^2 = 4 + 4 + 1 = 9$。
- $(2, 2, 1)$ 的排列为：
- $(2, 2, 1)$
- $(2, 1, 2)$
- $(1, 2, 2)$
- $(3, 0, 0)$ 也给出 9，但不被允许：每个量子数至少为 1，因为 $n = 0$ 会使 $\psi = 0$。
``````

**Part 2:**
The degeneracy for the energy level corresponding to $n_x^2 + n_y^2 + n_z^2 = 9$ is **3**: the three permutations of $(2,2,1)$.


``````{admonition} 中文翻译
:class: dropdown

**第 2 部分：**
对应于 $n_x^2 + n_y^2 + n_z^2 = 9$ 的能级的简并度为 **3**：即 $(2,2,1)$ 的三种排列。
``````

:::

#### Problem 10: Absorption of a conjugated diene

A conjugated diene has a conjugation length of 5 Å. Using the 1D particle in a box, calculate the wavelength absorbed when a π-electron is excited from $n = 1$ to $n = 2$. Use $m = 9.109 \times 10^{-31}\,\text{kg}$ and $h = 6.626 \times 10^{-34}\,\text{J s}$.


``````{admonition} 中文翻译
:class: dropdown

一个共轭二烯的共轭长度为 5 Å。利用一维无限深势阱，计算 π 电子从 $n = 1$ 激发到 $n = 2$ 时吸收的波长。使用 $m = 9.109 \times 10^{-31}\,\text{kg}$ 和 $h = 6.626 \times 10^{-34}\,\text{J s}$。
``````

:::{admonition} **Solution**
:class: dropdown solution

The gap between $n = 1$ and $n = 2$ is


``````{admonition} 中文翻译
:class: dropdown

$n = 1$ 与 $n = 2$ 之间的能隙为
``````

$$
\Delta E = \frac{(2^2 - 1^2)h^2}{8mL^2} = \frac{3h^2}{8mL^2},
$$

with $L = 5 \times 10^{-10}\,\text{m}$. Compute $\Delta E$, then use $\Delta E = \dfrac{hc}{\lambda}$ to find $\lambda$.


``````{admonition} 中文翻译
:class: dropdown

其中 $L = 5 \times 10^{-10}\,\text{m}$。计算 $\Delta E$，然后用 $\Delta E = \dfrac{hc}{\lambda}$ 求 $\lambda$。
``````
:::

#### Problem 11: Total conjugation length of a polyene

A polyene has 6 alternating bonds with $C=C \approx 1.35$ Å and $C\text{-}C \approx 1.45$ Å. Find the total conjugation length and the wavelength needed to excite a π-electron from $n = 1$ to $n = 2$.


``````{admonition} 中文翻译
:class: dropdown

一个多烯有 6 个交替键，其中 $C=C \approx 1.35$ Å、$C\text{-}C \approx 1.45$ Å。求总共轭长度以及把一个 π 电子从 $n = 1$ 激发到 $n = 2$ 所需的波长。
``````

:::{admonition} **Solution**
:class: dropdown solution

$$
L = 4 \times 1.35\,\text{Å} + 3 \times 1.45\,\text{Å} = 10.55\,\text{Å} = 10.55 \times 10^{-10}\,\text{m}.
$$

Then $\Delta E = \dfrac{3h^2}{8mL^2}$ and $\lambda = \dfrac{hc}{\Delta E}$.


``````{admonition} 中文翻译
:class: dropdown

于是 $\Delta E = \dfrac{3h^2}{8mL^2}$ 且 $\lambda = \dfrac{hc}{\Delta E}$。
``````
:::

#### Problem 12: A higher transition

A linear conjugated molecule has 8 alternating C-C bonds (1.40 Å single, 1.35 Å double). Calculate the wavelength absorbed for the $n = 1 \to n = 3$ transition.


``````{admonition} 中文翻译
:class: dropdown

一个线形共轭分子有 8 个交替的 C-C 键（单键 1.40 Å，双键 1.35 Å）。计算 $n = 1 \to n = 3$ 跃迁吸收的波长。
``````

:::{admonition} **Solution**
:class: dropdown solution

For 8 bonds, take 4 double and 4 single:


``````{admonition} 中文翻译
:class: dropdown

对于 8 个键，取 4 个双键和 4 个单键：
``````

$$
L = 4 \times 1.35\,\text{Å} + 4 \times 1.40\,\text{Å} = 11.0\,\text{Å}.
$$

The energy gap is

$$
\Delta E = E_3 - E_1 = \frac{(3^2 - 1^2)h^2}{8mL^2} = \frac{8h^2}{8mL^2} = \frac{h^2}{mL^2},
$$

and $\lambda = \dfrac{hc}{\Delta E}$.
:::

#### Problem 13: Triene transition

A conjugated triene has a conjugation length of 7.5 Å. Find the wavelength absorbed for the $n = 1 \to n = 3$ transition.


``````{admonition} 中文翻译
:class: dropdown

一个共轭三烯的共轭长度为 7.5 Å。求 $n = 1 \to n = 3$ 跃迁吸收的波长。
``````

:::{admonition} **Solution**
:class: dropdown solution

With $L = 7.5 \times 10^{-10}\,\text{m}$,

$$
\Delta E = E_3 - E_1 = \frac{8h^2}{8mL^2} = \frac{h^2}{mL^2},
$$

then $\lambda = \dfrac{hc}{\Delta E}$.
:::

#### Problem 14: A transition between excited states

A polyene of 10 carbons has $C=C \approx 1.34$ Å and $C\text{-}C \approx 1.54$ Å. Find the total conjugation length and the wavelength for the $n = 2 \to n = 3$ transition.


``````{admonition} 中文翻译
:class: dropdown

一个含 10 个碳原子的多烯有 $C=C \approx 1.34$ Å 和 $C\text{-}C \approx 1.54$ Å。求总共轭长度以及 $n = 2 \to n = 3$ 跃迁的波长。
``````

:::{admonition} **Solution**
:class: dropdown solution

$$
L = 5 \times 1.34\,\text{Å} + 4 \times 1.54\,\text{Å} = 12.86\,\text{Å}.
$$

The gap is

$$
\Delta E = E_3 - E_2 = \frac{(3^2 - 2^2)h^2}{8mL^2} = \frac{5h^2}{8mL^2},
$$

then $\lambda = \dfrac{hc}{\Delta E}$.
:::

#### Problem 15: A 2D box for a graphene fragment

Model the π-electrons of a graphene-like fragment as a 2D particle in a box with $L_x = 2\,\text{nm}$ and $L_y = 1\,\text{nm}$. Calculate the energy of the state $n_x = 1$, $n_y = 2$.


``````{admonition} 中文翻译
:class: dropdown

把类石墨烯碎片的 π 电子建模为二维势阱中的粒子，其中 $L_x = 2\,\text{nm}$、$L_y = 1\,\text{nm}$。计算态 $n_x = 1$、$n_y = 2$ 的能量。
``````

:::{admonition} **Solution**
:class: dropdown solution

The 2D energy is

$$
E_{n_x, n_y} = \frac{h^2}{8m}\left(\frac{n_x^2}{L_x^2} + \frac{n_y^2}{L_y^2}\right).
$$

With $L_x = 2 \times 10^{-9}\,\text{m}$ and $L_y = 1 \times 10^{-9}\,\text{m}$,


``````{admonition} 中文翻译
:class: dropdown

由 $L_x = 2 \times 10^{-9}\,\text{m}$ 和 $L_y = 1 \times 10^{-9}\,\text{m}$，
``````

$$
\frac{1^2}{L_x^2} + \frac{2^2}{L_y^2} = 2.5 \times 10^{17} + 4.0 \times 10^{18} = 4.25 \times 10^{18}\,\text{m}^{-2},
$$

and $\dfrac{h^2}{8m} \approx 6.02 \times 10^{-38}\,\text{J m}^2$, giving


``````{admonition} 中文翻译
:class: dropdown

且 $\dfrac{h^2}{8m} \approx 6.02 \times 10^{-38}\,\text{J m}^2$，给出
``````

$$
E_{1,2} \approx 2.56 \times 10^{-19}\,\text{J} \approx 1.60\,\text{eV}.
$$
:::
