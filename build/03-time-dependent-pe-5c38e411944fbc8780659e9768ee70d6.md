# Time-Dependent Perturbation Theory and Selection Rules

:::{note} **What you will learn**

- **Transitions between states:** When a system is exposed to a time-dependent perturbation, such as an oscillating electromagnetic field, it can make transitions between the stationary states of the unperturbed Hamiltonian.
- **First-order transition amplitude:** Expanding the time-dependent state in the unperturbed eigenbasis and keeping the leading term gives a simple integral for the amplitude of going from an initial state $|i\rangle$ to a final state $|f\rangle$.
- **Resonance and energy conservation:** For an oscillating field, the transition is large only when the photon energy matches the level spacing, $E_f - E_i = \pm\hbar\omega$.
- **Selection rules:** The transition probability is proportional to $|\mu_{fi}|^2$. When this dipole matrix element vanishes by symmetry, the transition is forbidden. For hydrogen-like atoms this yields $\Delta l = \pm 1$ and $\Delta m_l = 0, \pm 1$.


``````{admonition} 中文翻译
:class: dropdown

- 各态间的跃迁：**当系统受到时依扰动，如振荡电磁场时，可使无摄动哈密顿量的驻态之间发生跃迁。**
- **一阶跃迁幅度:** 将时依状态展开到无扰动本征基并保留首项，可得到从初态 $|i\rangle$ 到末态 $|f\rangle$ 跃迁幅度的简单积分。
- **共振与能量守恒**：对于摆动场，仅当光子能量与能级间距匹配时跃迁才显著，$E_f - E_i = \pm\hbar\omega$。
- **选取规则：** 过渡概率与 $|\mu_{fi}|^2$ 成正比。当此偶极矩阵元因对称性而消去时，该跃迁被禁止。对于氢样子原子，这产生了 $\Delta l = \pm 1$ 和 $\Delta m_l = 0, \pm 1$。
``````
:::

## Setup: stationary states and a time-dependent perturbation

We consider a Hamiltonian split into an exactly solvable part and a weak, time-dependent perturbation:


``````{admonition} 中文翻译
:class: dropdown

我们考虑一个哈密顿量，将其分为一个可精确求解的部分和一个微弱的、时变的微扰：
``````

$$
\hat{H}(t) = \hat{H}_0 + \hat{V}(t)
$$

The unperturbed Hamiltonian $\hat{H}_0$ has known eigenstates and eigenvalues:


``````{admonition} 中文翻译
:class: dropdown

未受微扰的哈密顿量 $\hat{H}_0$ 具有已知的本征态和本征值：
``````

$$
\hat{H}_0 |n\rangle = E_n |n\rangle
$$

We expand the full time-dependent state in the stationary basis:


``````{admonition} 中文翻译
:class: dropdown

我们将完整的时间依赖态在定态基底中展开：
``````

$$
|\Psi(t)\rangle = \sum_n c_n(t)\, e^{-iE_n t/\hbar} |n\rangle
$$

The time-dependent coefficients $c_n(t)$ encode the transitions between stationary states caused by $\hat{V}(t)$.


``````{admonition} 中文翻译
:class: dropdown

时变系数 $c_n(t)$ 编码了由 $\hat{V}(t)$ 引起的定态间跃迁。
``````

## Deriving the first-order transition amplitude

Insert the expansion into the time-dependent Schrodinger equation:


``````{admonition} 中文翻译
:class: dropdown

将展开式代入含时薛定谔方程：
``````

$$
i\hbar \frac{\partial}{\partial t}|\Psi(t)\rangle = \hat{H}(t)|\Psi(t)\rangle
$$

After some algebra, using orthonormality $\langle m|n\rangle = \delta_{mn}$, we obtain the equation of motion for the coefficients:


``````{admonition} 中文翻译
:class: dropdown

经过一些代数运算，利用正交归一性 $\langle m|n\rangle = \delta_{mn}$，我们得到系数的运动方程：
``````

$$
i\hbar\, \dot{c}_m(t) = \sum_n c_n(t)\, V_{mn}(t)\, e^{i\omega_{mn} t}
$$

where

$$
V_{mn}(t) = \langle m|\hat V(t)|n\rangle, \qquad \omega_{mn} = \frac{E_m - E_n}{\hbar}
$$

Assume the system starts in state $|i\rangle$ at $t=0$:


``````{admonition} 中文翻译
:class: dropdown

假设系统在 $t=0$ 时处于态 $|i\rangle$：
``````

$$
c_n(0) = \delta_{ni}, \quad c_i(0) = 1, \quad c_{f\neq i}(0) = 0
$$

In **first-order perturbation theory** we approximate $c_n(t) \approx \delta_{ni}$ on the right-hand side (the perturbation is weak, so the population stays mostly in the initial state). The equation for $c_f(t)$ becomes


``````{admonition} 中文翻译
:class: dropdown

在**一阶摄动理论**中，我们近似 $c_n(t) \approx \delta_{ni}$ 在右边（摄动弱，所以电子主要留在初态）。 $c_f(t)$ 的方程变成
``````

$$
\dot{c}_f^{(1)}(t) = -\frac{i}{\hbar} V_{fi}(t)\, e^{i\omega_{fi} t}
$$

Integrating from $0$ to $t$:

$$
c_f^{(1)}(t) = -\frac{i}{\hbar} \int_0^t V_{fi}(t')\, e^{i\omega_{fi} t'} dt'
$$

This is the **first-order transition amplitude** from state $|i\rangle$ to $|f\rangle$.


``````{admonition} 中文翻译
:class: dropdown

这是从态 $|i\rangle$ 到 $|f\rangle$ 的**一阶跃迁振幅**。
``````

## Coupling to light: the dipole approximation

For an atom or molecule in a classical electromagnetic field, the **electric dipole approximation** gives the perturbation


``````{admonition} 中文翻译
:class: dropdown

对于处于经典电磁场中的原子或分子，**电偶极近似**给出了微扰
``````

$$
\hat{V}(t) = -\hat{\boldsymbol{\mu}}\cdot \mathbf{E}(t)
$$

For a monochromatic, linearly polarized field

$$
\mathbf{E}(t) = \mathbf{E}_0 \cos(\omega t)
$$

the matrix element is

$$
V_{fi}(t) = \langle f|\hat{V}(t)|i\rangle = -\langle f|\hat{\boldsymbol{\mu}}\cdot \mathbf{E}_0|i\rangle \cos(\omega t)
$$

Define the (possibly complex) dipole matrix element

$$
\mu_{fi} = \langle f|\hat{\boldsymbol{\mu}}\cdot \hat{\mathbf{e}}|i\rangle
$$

where $\hat{\mathbf{e}}$ is the polarization direction of the field, and let $E_0 = |\mathbf{E}_0|$. Then


``````{admonition} 中文翻译
:class: dropdown

其中 $\hat{\mathbf{e}}$ 是场的偏振方向，令 $E_0 = |\mathbf{E}_0|$。然后
``````

$$
V_{fi}(t) = -\mu_{fi} E_0 \cos(\omega t)
$$

Plugging into the transition amplitude:

$$
c_f^{(1)}(t) = \frac{i E_0}{\hbar} \mu_{fi} \int_0^t \cos(\omega t')\, e^{i\omega_{fi} t'} dt'
$$

## Resonance condition and energy conservation

Use the exponential form of the cosine:

$$
\cos(\omega t') = \frac{1}{2}\left(e^{i\omega t'} + e^{-i\omega t'}\right)
$$

Then the integral in $c_f^{(1)}(t)$ contains terms of the form


``````{admonition} 中文翻译
:class: dropdown

那么 $c_f^{(1)}(t)$ 中的积分包含如下形式的项
``````

$$
\int_0^t e^{i(\omega_{fi} \pm \omega)t'} dt'
$$

If $\omega_{fi} \pm \omega$ is large, the exponential oscillates rapidly and the integral averages out to a small value. A **large transition amplitude** occurs when the exponent is nearly stationary:


``````{admonition} 中文翻译
:class: dropdown

如果 $\omega_{fi} \pm \omega$ 很大，指数会快速振荡，积分平均会得到一个较小的值。当指数几乎不变时会发生**大跃迁幅度**：
``````

$$
\omega_{fi} - \omega \approx 0 \quad \Rightarrow \quad \omega_{fi} \approx \omega
$$

This gives the familiar **energy-conservation condition** for absorption:


``````{admonition} 中文翻译
:class: dropdown

这给出了吸收的熟悉 **能量守恒条件**：
``````

$$
E_f - E_i = \hbar\omega
$$

Similarly, for stimulated emission one finds $E_f - E_i = -\hbar\omega$.


``````{admonition} 中文翻译
:class: dropdown

同样地，对于受激辐射可得 $E_f - E_i = -\hbar\omega$。
``````

## From transition amplitudes to selection rules

:::{important} **Selection Rules**

The **transition probability** (to first order) is

$$
P_{i\to f}(t) \approx |c_f^{(1)}(t)|^2 \propto |\mu_{fi}|^2
$$

- A transition $|i\rangle \to |f\rangle$ is electric-dipole allowed only if the dipole matrix element is nonzero:


``````{admonition} 中文翻译
:class: dropdown

- 只有当偶极矩阵元非零时，跃迁 $|i\rangle \to |f\rangle$ 才是电偶极允许的：
``````

$$
\mu_{fi} = \langle f|\hat{\boldsymbol{\mu}}\cdot \hat{\mathbf{e}}|i\rangle \neq 0
$$
:::

If the matrix element is **exactly zero** due to symmetry, the transition is **dipole-forbidden** (in first order).


``````{admonition} 中文翻译
:class: dropdown

如果矩阵元因对称性而**恰好为零**，则该跃迁是**偶极子禁戒**的（一级近似下）。
``````

Selection rules therefore come from:

- the symmetry properties (angular, parity, and so on) of the **wavefunctions** $|i\rangle$ and $|f\rangle$
- the transformation properties of the **operator** $\hat{\boldsymbol{\mu}} \sim \mathbf{r}$ (a vector operator)


``````{admonition} 中文翻译
:class: dropdown

- **波函数** $|i\rangle$ 和 $|f\rangle$ 的对称性质（角、宇称等）
- **算符** $\hat{\boldsymbol{\mu}} \sim \mathbf{r}$ 的变换性质（矢量算符）
``````

## Electric dipole selection rules for hydrogen-like orbitals

For an electron in a central potential (for example, a hydrogenic atom), the stationary states are labeled by $|n, l, m_l\rangle$.


``````{admonition} 中文翻译
:class: dropdown

对于中心势场中的电子（例如，类氢原子），定态用 $|n, l, m_l\rangle$ 标记。
``````

The position operator $\mathbf{r}$ transforms like an angular-momentum-1 object (similar to the spherical harmonics $Y_{1m}$). From angular-momentum coupling rules one obtains:


``````{admonition} 中文翻译
:class: dropdown

位置算符 $\mathbf{r}$ 像角动量-1 物体一样转换（类似球谐函数 $Y_{1m}$）。从角动量耦合规则得出：
``````

**Orbital angular momentum selection rule**

$$
\Delta l = l_f - l_i = \pm 1
$$

**Magnetic quantum number selection rule**

$$
\Delta m_l = m_{l,f} - m_{l,i} = 0, \pm 1
$$

:::{tip} **Summary**

- Start from the time-dependent Schrodinger equation with $\hat{H}(t) = \hat{H}_0 + \hat{V}(t)$.
- Expand the state in the eigenbasis of $\hat{H}_0$ to obtain equations for $c_n(t)$.
- First-order perturbation theory gives a transition amplitude


``````{admonition} 中文翻译
:class: dropdown

- 从含时薛定谔方程出发，其中 $\hat{H}(t) = \hat{H}_0 + \hat{V}(t)$。
- 将态在 $\hat{H}_0$ 的本征基下展开，以得到 $c_n(t)$ 的方程。
- 一阶摄动理论给出一个跃迁幅度
``````
  $$
  c_f^{(1)}(t) = -\frac{i}{\hbar} \int_0^t \langle f|\hat{V}(t')|i\rangle\, e^{i\omega_{fi} t'} dt'
  $$
- For an oscillating field, the integral is large only when $E_f - E_i = \pm \hbar\omega$ (energy conservation).
- The transition probability is proportional to $|\langle f|\hat{\boldsymbol{\mu}}|i\rangle|^2$.
- If the dipole matrix element is zero by symmetry, the transition is forbidden.
- For electric-dipole transitions in atoms: $\Delta l = \pm 1$, $\Delta m_l = 0, \pm 1$, and the parity changes.


``````{admonition} 中文翻译
:class: dropdown

- 对于振荡场，仅当 $E_f - E_i = \pm \hbar\omega$（能量守恒）时积分才较大。
- 跃迁概率与 $|\langle f|\hat{\boldsymbol{\mu}}|i\rangle|^2$ 成正比。
- 如果偶极矩阵元因对称性而为零，则该跃迁是禁戒的。
- 对于原子中的电偶极跃迁：$\Delta l = \pm 1$，$\Delta m_l = 0, \pm 1$，且宇称发生改变。
``````
:::

:::{seealso} Chapter demos
Computational labs for this chapter: [Linear variational method](../demos/08-demo-linear-variational.md) · [Variational method](../demos/09-demo-variational-method.md) · [Perturbation theory](../demos/10-demo-perturbation-theory.md)


``````{admonition} 中文翻译
:class: dropdown

本章计算实验：[线性变分法](../demos/08-demo-linear-variational.md) · [变分法](../demos/09-demo-variational-method.md) · [摄动理论](../demos/10-demo-perturbation-theory.md)
``````
:::
