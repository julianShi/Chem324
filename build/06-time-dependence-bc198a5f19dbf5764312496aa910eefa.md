# Time Dependence

:::{admonition} **What you need to know**

- The **time-dependent Schrödinger equation** governs the evolution of the quantum wavefunction over time, $\psi(x,t)$. 
- **Stationary states** are eigenfunctions of the Hamiltonian $\hat{H}$ containing a spatial part and a time-dependent phase factor:  $\psi(x,t) = \psi(x) e^{-i E t / \hbar}$  
- The stationary states have definite energy and their probability distributions are **time-independent**.
- In more general situations, the wavefunction can be expressed as a **linear superposition of energy eigenstates**, with time evolution given by the phase factors of the eigenstates:  $\psi(x,t) = \sum_n c_n \psi_n(x) e^{-i E_n t / \hbar}$ 

- This superposition leads to **time-dependent probabilities** as different eigenstates interfere.
- The time-dependence of quantum states is key to understanding **quantum dynamics**, such as oscillations between states in **two-level systems** or time evolution of **quantum superpositions**.


``````{admonition} 中文翻译
:class: dropdown

- **含时薛定谔方程**支配着量子波函数 $\psi(x,t)$ 随时间的演化。
- **定态**是哈密顿算符 $\hat{H}$ 的本征函数，包含空间部分和一个含时相位因子：$\psi(x,t) = \psi(x) e^{-i E t / \hbar}$
- 定态具有确定的能量，其概率分布是**不含时**的。
- 在更一般的情形下，波函数可以表示为**能量本征态的线性叠加**，其时间演化由各本征态的相位因子给出：$\psi(x,t) = \sum_n c_n \psi_n(x) e^{-i E_n t / \hbar}$
- 由于不同本征态之间相互干涉，这种叠加会导致**含时概率**。
- 量子态的含时性是理解**量子动力学**的关键，例如**两能级系统**中态之间的振荡，或**量子叠加**的时间演化。
``````

:::



### Time Dependence of a Pure Eigenfunction

- Until now, we have largely ignored the time dependence of quantum systems. This is because we have primarily focused on pure eigenfunction states, $\psi_n(x,t)$, which exhibit no time-dependent behavior for observable quantities. The reason for this is straightforward.


``````{admonition} 中文翻译
:class: dropdown

- 迄今为止，我们基本上忽略了量子系统的含时性。这是因为我们主要关注纯本征函数态 $\psi_n(x,t)$，其可观测量并不表现出含时行为。原因很简单。
``````

$$\psi_n(x,t) = \psi_n(x) e^{-\frac{i}{\hbar}E_n t}$$

- In any probabilistic calculation, the time dependence vanishes because the expressions involve the square of the wavefunction. The absolute value of the complex time-dependent phase factor equals unity:


``````{admonition} 中文翻译
:class: dropdown

- 在任何概率计算中，含时性都会消失，因为这些表达式涉及波函数的平方。复含时相位因子的绝对值等于 1：
``````

$$\mid \psi_n(x,t) \mid^2 = \psi_n^*(x)\psi_n(x) e^{-\frac{i}{\hbar}E_n t} e^{+\frac{i}{\hbar}E_n t} = \mid \psi_n(x) \mid^2$$

- Similarly, for the expectation value of an operator $\hat{A}$, the time-dependent phases cancel out, leaving only the spatial part:


``````{admonition} 中文翻译
:class: dropdown

- 类似地，对于算符 $\hat{A}$ 的期望值，含时相位相互抵消，只留下空间部分：
``````

$$\langle A \rangle = \int \psi_n^*(x) e^{+\frac{i}{\hbar}E_n t} \hat{A} \psi_n(x) e^{-\frac{i}{\hbar}E_n t} dx = \int \psi_n^*(x) \hat{A} \psi_n(x) dx$$

- Will we always have this fortunate cancellation of time dependence? The answer is no. When the system is described as a **linear superposition** of eigenstates, time dependence reappears in a significant way.


``````{admonition} 中文翻译
:class: dropdown

- 我们是否总能如此幸运地消去含时性？答案是否定的。当系统被描述为本征态的**线性叠加**时，含时性会以显著的方式重新出现。
``````


### Time Dependence of a Superposition of Eigenfunctions

- Let us start with a superposition state of two energy eigenfunctions at time $t=0$:


``````{admonition} 中文翻译
:class: dropdown

- 让我们从 $t=0$ 时刻两个能量本征函数的叠加态开始：
``````

$$\mid \psi(0) \rangle =c_1\mid 1 \rangle + c_2 \mid 2 \rangle$$

- What would the state be after some time $t$? By virtue of separation of variables, we add the time dependence as a multiplicative factor for each eigenfunction:


``````{admonition} 中文翻译
:class: dropdown

- 经过一段时间 $t$ 后，态会变成什么样？借助分离变量法，我们为每个本征函数乘上一个含时因子：
``````

$$\mid \psi(t) \rangle =c_1 e^{-\frac{i}{\hbar}E_1 t}\mid 1 \rangle + c_2 e^{-\frac{i}{\hbar}E_2 t}\mid 2 \rangle= c_1(t)\mid 1\rangle+c_2(t) \mid 2 \rangle$$

- Thus we see that the coefficients change over time. This means our state vector moves in the functional space spanned by the fixed orthogonal eigenfunctions! We can verify that this expression satisfies the time-dependent Schrödinger equation by plugging it in.


``````{admonition} 中文翻译
:class: dropdown

- 由此我们看到系数随时间变化。这意味着我们的态矢量在由固定正交本征函数张成的函数空间中运动！我们可以通过代入来验证该表达式满足含时薛定谔方程。
``````

:::{admonition} **Proof that the superposition obeys the time-dependent Schrödinger equation**
:class: dropdown

$$  i\hbar\frac{\partial}{\partial t}\mid \psi \rangle =\hat{H}\psi(t)\rangle $$

*Left hand side :*

$$i\hbar \Big( -\frac{i}{\hbar}E_1 c_1 e^{-\frac{i}{\hbar}E_1 t}\mid 1\rangle-\frac{i}{\hbar}E_2 c_2 e^{-\frac{i}{\hbar}E_2 t}\mid 2\rangle \Big) = E_1 c_1(t)\mid 1 \rangle +E_2 c_2(t)\mid 2 \rangle$$

*Right hand side:*

$$c_1 e^{-\frac{i}{\hbar}E_1 t}\hat{H}\mid 1 \rangle + c_2 e^{-\frac{i}{\hbar}E_2 t}\hat{H} \mid 2 \rangle = E_1 c_1(t)\mid 1 \rangle +E_2 c_2(t)\mid 2 \rangle $$

:::



```{marimo-config}
---
pyproject: |
  requires-python = ">=3.10"
  dependencies = [
      "numpy",
      "matplotlib",
  ]
---
```

```{marimo} python
:hide-code: true

import marimo as mo
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.dpi"] = 150
```

```{marimo} python
def psi_n(x, n):
    """Time-independent wavefunction for a particle in a box."""
    L = 1 # set box length

    return np.sqrt(2/L) * np.sin(n * np.pi * x / L)

def T_n(t, n):
    """Time dependence factor for the wavefunction."""
    L = 1 # set box length
    m, hbar = 1, 1 # set atomic units
    En = n**2 * np.pi**2 * hbar**2 / (2 * m * L**2)

    return np.exp(-1j * En * t / hbar)

def psi_combined(x, t, c1=1, c2=1, n1=1, n2=2):
    """Time-dependent wavefunction for a normalized superposition of two PIB states."""

    norm = np.sqrt(c1**2 + c2**2)

    return (c1 * psi_n(x, n1) * T_n(t, n1) + c2 * psi_n(x, n2) * T_n(t, n2)) / norm
```

```{marimo} python
def plot_wavefunction(t=0, c1=1, c2=1, n1=1, n2=2):

    L = 1.0
    x = np.linspace(0, L, 1000)

    psi_squared_x = np.abs(psi_combined(x, t, c1=c1, c2=c2, n1=n1, n2=n2))**2

    plt.plot(x, psi_squared_x, color="#3d81f6", lw=2)
    plt.fill_between(x, psi_squared_x, alpha=0.2, color="#3d81f6")

    plt.title(f"$|\\Psi(x,t)|^2$ for states n={n1} and n={n2} at t={t:.2f}")
    plt.xlabel('x')
    plt.ylabel(r'$|\Psi(x, t)|^2$')
    plt.grid(True, alpha=0.4)
    plt.ylim([0, 4.5])
    plt.gcf()
```

```{marimo} python
:hide-code: true

t_qw = mo.ui.slider(0, 10.0, step=0.1, value=0.0, show_value=True, label="time t")
n2_qw = mo.ui.slider(2, 6, step=1, value=2, show_value=True, label="second state n2")
mo.hstack([t_qw, n2_qw], justify="start", gap=2)
```

```{marimo} python
:hide-code: true

plot_wavefunction(t=t_qw.value, c1=1, c2=1, n1=1, n2=n2_qw.value)
plt.gcf()
```

- Drag the **time slider** and watch the probability sloshing between the two walls: the interference term beats at the frequency $(E_{n_2} - E_1)/\hbar$. Raising $n_2$ makes the pattern richer and the beat faster. A single eigenstate would sit perfectly still; motion in quantum mechanics lives in superpositions.


``````{admonition} 中文翻译
:class: dropdown

- 拖动**时间滑块**，观察概率在两个壁之间来回晃动：干涉项以频率 $(E_{n_2} - E_1)/\hbar$ 振荡。增大 $n_2$ 会使图样更丰富、振荡更快。单个本征态会完全静止不动；量子力学中的运动存在于叠加之中。
``````
### Normalization is time independent!

- Certain quantities remain invariant under time evolution. For instance, it is natural to expect that normalization does not change over time: the particle must always be located somewhere within the box at any given moment.


``````{admonition} 中文翻译
:class: dropdown

- 某些量在时间演化中保持不变。例如，很自然地可以预期归一化不随时间改变：粒子在任何给定时刻都必须位于盒子内的某个位置。
``````

$$\mid \psi(t)\rangle = \sum_n c_n e^{-\frac{i}{\hbar}E_n t} \mid n\rangle$$

- The normalization condition is expressed as:

$$\langle \psi(t) \mid \psi(t)\rangle = \sum_n \sum_k \langle n \mid c^*_n e^{\frac{i}{\hbar}E_n t} \cdot c_k e^{-\frac{i}{\hbar}E_k t} \mid k\rangle = \sum_n \sum_k c^*_n c_k e^{-\frac{i}{\hbar}(E_k - E_n)t} \delta_{kn} = \sum_n \mid c_n \mid^2 = 1$$

- In the final step, we use the fact that the eigenfunctions are orthogonal, meaning $\langle n \mid k \rangle = 0$ for $n \neq k$, so the cross terms vanish and only the diagonal terms, where $n = k$, survive.


``````{admonition} 中文翻译
:class: dropdown

- 在最后一步中，我们利用了本征函数相互正交这一事实，即当 $n \neq k$ 时 $\langle n \mid k \rangle = 0$，因此交叉项消失，只有 $n = k$ 的对角项保留下来。
``````


### Constants of Motion

- Quantities that remain conserved over time are called **constants of motion**. In quantum mechanics, we typically deal with expectations or averages rather than sharply defined values.

- However, the principle of energy conservation dictates that the **average total energy** must be a conserved quantity. To determine whether a particular quantity depends on time, we take the time derivative of the expectation value:


``````{admonition} 中文翻译
:class: dropdown

- 随时间保持守恒的量称为**运动常数**。在量子力学中，我们通常处理的是期望值或平均值，而非精确定义的值。
- 然而，能量守恒原理要求**平均总能量**必须是一个守恒量。为了确定某个量是否含时，我们对期望值求时间导数：
``````

  $$\langle A \rangle = \langle \psi \mid \hat{A} \mid \psi \rangle$$

  The time derivative of this expectation value is:


``````{admonition} 中文翻译
:class: dropdown

该期望值的时间导数为：
``````

  $$
  \frac{\partial}{\partial t}\langle A \rangle = \langle \frac{\partial \psi}{\partial t} \mid \hat{A} \mid \psi \rangle + \langle \psi \mid \hat{A} \mid \frac{\partial \psi}{\partial t} \rangle + \langle \psi \mid \frac{\partial \hat{A}}{\partial t} \mid \psi \rangle
  $$

- Now, using the time-dependent Schrödinger equation,  

  $$
  i\hbar \frac{\partial}{\partial t} \mid \psi \rangle = \hat{H} \mid \psi \rangle
  $$  

  we can express the time derivatives of the bras and kets as:


``````{admonition} 中文翻译
:class: dropdown

我们可以把左矢和右矢的时间导数表示为：
``````

  $$\langle \frac{\partial \psi}{\partial t} \mid = -\frac{1}{i\hbar} \langle \psi \mid \hat{H},$$
  $$\mid \frac{\partial \psi}{\partial t} \rangle = \frac{1}{i\hbar} \hat{H} \mid \psi \rangle.$$

- Substituting these into the time derivative of the expectation value, we obtain:


``````{admonition} 中文翻译
:class: dropdown

- 将这些代入期望值的时间导数，我们得到：
``````

  $$\frac{\partial}{\partial t}\langle A \rangle = \frac{1}{i\hbar} \langle \psi \mid \hat{A}\hat{H} \mid \psi \rangle - \frac{1}{i\hbar} \langle \psi \mid \hat{H}\hat{A} \mid \psi \rangle + \langle \psi \mid \frac{\partial \hat{A}}{\partial t} \mid \psi \rangle$$
  
:::{important} **Time dependence of expectation**

  $$
  \frac{\partial}{\partial t}\langle A \rangle = \frac{1}{i\hbar} \langle \psi \mid [\hat{A}, \hat{H}] \mid \psi \rangle + \langle \psi \mid \frac{\partial \hat{A}}{\partial t} \mid \psi \rangle.
  $$

:::

- This important relationship shows that if the operator $\hat{A}$ does not explicitly depend on time, i.e., $\frac{\partial \hat{A}}{\partial t} = 0$, then quantities that **commute with the Hamiltonian** $[\hat{A}, \hat{H}] = 0$ will be constants of motion. Those that do not commute, $[\hat{A}, \hat{H}] \neq 0$, will evolve over time.

- Since the Hamiltonian commutes with itself and does not depend on time, the **energy** is conserved.


``````{admonition} 中文翻译
:class: dropdown

- 这一重要关系表明：如果算符 $\hat{A}$ 不显含时间，即 $\frac{\partial \hat{A}}{\partial t} = 0$，那么**与哈密顿算符对易** $[\hat{A}, \hat{H}] = 0$ 的量就是运动常数；而不对易的量 $[\hat{A}, \hat{H}] \neq 0$ 将随时间演化。
- 由于哈密顿算符与自身对易且不显含时间，**能量**是守恒的。
``````

  $$
  \frac{\partial}{\partial t}\langle E \rangle = 0
  $$  
 

### Quantum Dynamics

:::{figure} ./images/gaussian_potential.gif
:label: fig-time-dependence-1
:alt: pib1
:width: 300px

Wavefunction dynamics in a Gaussian potential, showing the probability density along with the real and imaginary parts.


``````{admonition} 中文翻译
:class: dropdown

高斯势中的波函数动力学，展示了概率密度以及实部和虚部。
``````
:::

:::{figure} ./images/barrier_potential.gif
:label: fig-time-dependence-2
:alt: pib1
:width: 300px

Wavefunction dynamics in a barrier potential, showing the probability density along with the real and imaginary parts.


``````{admonition} 中文翻译
:class: dropdown

势垒中的波函数动力学，展示了概率密度以及实部和虚部。
``````
:::

:::{seealso} Chapter demos
Computational lab for this chapter: [Numerical Schrödinger solver](../demos/07-demo-numerical-schrodinger.md)


``````{admonition} 中文翻译
:class: dropdown

本章计算实验：[数值薛定谔求解器](../demos/07-demo-numerical-schrodinger.md)
``````
:::
