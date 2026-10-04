---
kernelspec:
  name: python3
  display_name: Python 3
---

# Multi-Electron Atoms

:::{note} **What you will learn**

- We approximate many-electron wavefunctions using **hydrogenic orbitals** as building blocks.
- Unlike the hydrogen atom, **multi-electron problems do not separate** and therefore do not admit exact analytical solutions.
- **Spin and antisymmetry** impose strict constraints on the allowed electronic wavefunctions, giving rise to the Pauli exclusion principle and the **Slater determinant**.
- Symmetric versus antisymmetric spatial functions split helium's excited states into **singlets and triplets**, and the energy difference between them is the origin of **exchange stabilization**.
- The **Aufbau principle**, **Pauli exclusion**, and **Hund's rule** together explain how electrons fill atomic orbitals.


``````{admonition} 中文翻译
:class: dropdown

- 我们用 **类氢轨道** 作为构建模块来近似多电子波函数。
- 与氢原子不同，**多电子问题不可分离**，因此不存在精确的解析解。
- **自旋和反对称** 对允许的电子波函数施加严格约束，从而产生保罗不相容原理和**Slater行列式**。
- 对称与反对称空间函数将氦激发态分裂为**单态和三态**，它们之间的能量差就是**交换稳定化**的由来。
- **构造原理**、**泡利不相容原理**和**洪特规则**共同解释了电子如何填充原子轨道。
``````
:::

## The Orbital Approximation

:::{figure} images/HvsHe.png
:alt: H vs He
:width: 500px

Fig. 1 Difference between the hydrogen and helium Hamiltonians that makes multi-electron atoms analytically unsolvable. The extra electron, electron repulsion term couples the coordinates and blocks separation of variables.


``````{admonition} 中文翻译
:class: dropdown

图 1 氢和氦哈密顿量之间的差异，使得多电子原子在分析上不可求解。额外的电子，电子排斥项耦合了坐标并阻断了变量的分离。
``````
:::

For multi-electron atoms, the Hamiltonian depends on the coordinates of all electrons. The coordinates **cannot be separated**, so the Schrodinger equation is not analytically solvable.


``````{admonition} 中文翻译
:class: dropdown

对于多电子原子，哈密顿量依赖于所有电子的坐标。电子坐标**不能分离**，所以薛定谔方程不可解析求解。
``````

A practical approximation is to represent the wavefunction as a product of **single-electron orbitals**, which are obtained computationally (for example, variationally):


``````{admonition} 中文翻译
:class: dropdown

一种实用的近似方法是将波函数表示为**单电子轨道**的乘积，这些轨道是通过计算获得的（例如，变分法）：
``````

:::{important} **Orbital Approximation**

$$
\Psi(r_1, r_2, \ldots, r_n) \approx \phi_1(r_1)\phi_2(r_2)\cdots\phi_n(r_n)
$$

- $\Psi$ is the multi-electron wavefunction.
- Each $\phi_i(r)$ is an **atomic orbital** occupied by one electron.


``````{admonition} 中文翻译
:class: dropdown

- $\Psi$ 是多电子波函数。
- 每个 $\phi_i(r)$ 是一个被一个电子占据的 **原子轨道**。
``````
:::

## The Helium Wavefunction

For helium, the simplest guess would be

$$
\Psi(r_1, r_2) \approx \phi_1(r_1)\phi_2(r_2).
$$

This form, however, suffers from three fundamental issues:


``````{admonition} 中文翻译
:class: dropdown

然而，这种形式存在三个根本问题：
``````

1. **Indistinguishability.** Electrons are identical; the wavefunction cannot assign "electron 1" to "orbital 1" and "electron 2" to "orbital 2".

2. **Missing spin information.** The spatial wavefunction must combine with a spin function so that the **total wavefunction is antisymmetric**.

3. **Neglect of electron, electron correlation.** The product form assumes electrons move independently, which leads to quantitative errors in energies.


``````{admonition} 中文翻译
:class: dropdown

- **不可辨别性。** 电子是相同的；波函数不能将“电子 1”指派给“轨道 1”，将“电子 2”指派给“轨道 2”。
- **缺少自旋信息。** 空间波函数必须与自旋函数结合，使 **总波函数是反对称的**。
- **忽略电子-电子相关。** 乘积形式假设电子独立运动，这会导致能量计算出现定量误差。
``````

## Issue 1: Indistinguishability and Antisymmetry

Particles such as electrons are indistinguishable. Therefore the probability density must remain unchanged upon interchange:


``````{admonition} 中文翻译
:class: dropdown

电子等粒子是不可区分的。因此，交换时概率密度必须保持不变：
``````

$$
|\Psi(r_1,r_2)|^2 = |\Psi(r_2,r_1)|^2,
$$

which implies

$$
\Psi(r_1,r_2) = \pm \Psi(r_2,r_1).
$$

Electrons are **fermions**, and Pauli's principle dictates that their total wavefunction must be **antisymmetric**:


``````{admonition} 中文翻译
:class: dropdown

电子是**费米子**，泡利原理要求它们的总波函数必须是**反对称**的：
``````

:::{important} **Antisymmetry Requirement**

$$
\Psi(\ldots, r_m, \ldots, r_n, \ldots)
= -\Psi(\ldots, r_n, \ldots, r_m, \ldots).
$$

:::

A simple way to generate symmetric or antisymmetric forms for a two-variable function $f(x,y)$:


``````{admonition} 中文翻译
:class: dropdown

为二元函数 $f(x,y)$ 生成对称或反对称形式的简单方法：
``````

- Symmetric:

  $$
  g_+(x,y) = f(x,y) + f(y,x)
  $$

- Antisymmetric:

  $$
  g_-(x,y) = f(x,y) - f(y,x)
  $$

For helium, the antisymmetrized spatial wavefunction is

$$
\Psi(r_1,r_2) \propto \phi_1(r_1)\phi_2(r_2) - \phi_1(r_2)\phi_2(r_1).
$$

## Issue 2: The Spin Requirement

Electrons have two spin states, $\alpha$ and $\beta$. The **total wavefunction** (spatial times spin) must be antisymmetric:


``````{admonition} 中文翻译
:class: dropdown

电子有两种自旋态，$\alpha$ 和 $\beta$。**总波函数**（空间部分乘以自旋部分）必须是反对称的：
``````

- If the spatial part is **symmetric**, the spin part must be **antisymmetric**.
- If the spatial part is **antisymmetric**, the spin part must be **symmetric**.


``````{admonition} 中文翻译
:class: dropdown

- 如果空间部分是 **对称** 的，自旋部分必须是 **反对称** 的。
- 如果空间部分是 **反对称** 的，自旋部分必须是 **对称** 的。
``````

The three **symmetric spin** functions are:

$$
\alpha(1)\alpha(2)
$$

$$
\beta(1)\beta(2)
$$

$$
\frac{1}{\sqrt{2}}\left[\alpha(1)\beta(2) + \alpha(2)\beta(1)\right]
$$

The single **antisymmetric spin** function is:

$$
\frac{1}{\sqrt{2}}\left[\alpha(1)\beta(2) - \alpha(2)\beta(1)\right]
$$

### The Pauli Exclusion Principle

A key result of antisymmetry is the **Pauli exclusion principle**:


``````{admonition} 中文翻译
:class: dropdown

反对称性的一个关键结果是 **泡利不相容原理**：
``````

> **No two electrons can possess identical sets of quantum numbers.**


``````{admonition} 中文翻译
:class: dropdown

> **没有两个电子可以拥有相同的量子数集合。**
``````

For helium's ground state ($1s^2$), the properly antisymmetrized total wavefunction is


``````{admonition} 中文翻译
:class: dropdown

对于氦的基态 ($1s^2$)，正确反对称化的总波函数是
``````

$$
\Psi = \frac{1}{\sqrt{2}}
\left[1s(1)1s(2) + 1s(2)1s(1)\right]
\left[\alpha(1)\beta(2) - \alpha(2)\beta(1)\right].
$$

### Slater Determinants

Slater introduced a compact and universally applicable way to construct **antisymmetric** many-electron wavefunctions:


``````{admonition} 中文翻译
:class: dropdown

Slater 提出了一种紧凑且普遍适用的方法来构造 **反对称** 多电子波函数：
``````

- A determinant expands into an antisymmetric sum of products of one-electron spin-orbitals.
- Any exchange of two electrons flips the sign of the wavefunction.
- This guarantees that the Pauli exclusion principle is satisfied automatically.


``````{admonition} 中文翻译
:class: dropdown

- 行列式展开为单电子自旋轨道乘积的反对称和。
- 任意两个电子的交换都会翻转波函数的符号。
- 这保证了泡利不相容原理自动得到满足。
``````

:::{important} **Slater Determinant**

$$
\Psi(r_1,\ldots, r_n)
= \frac{1}{\sqrt{n!}}
\begin{vmatrix}
\chi_1(1) & \chi_2(1) & \cdots & \chi_n(1) \\
\chi_1(2) & \chi_2(2) & \cdots & \chi_n(2) \\
\vdots    & \vdots    & \ddots & \vdots    \\
\chi_1(n) & \chi_2(n) & \cdots & \chi_n(n)
\end{vmatrix}
$$

- $\chi_j(i)$ is a **spin-orbital**, that is, an orbital times a spin function, describing electron $i$ in spin-orbital $j$.
- The factor $1/\sqrt{n!}$ ensures proper normalization of the determinant.


``````{admonition} 中文翻译
:class: dropdown

- $\chi_j(i)$ 是一个 **自旋轨道**，即轨道与自旋函数的乘积，描述处于自旋轨道 $j$ 中的电子 $i$。
- 因子 $1/\sqrt{n!}$ 确保行列式的正确归一化。
``````
:::

For example, the helium ground-state Slater determinant looks like this:


``````{admonition} 中文翻译
:class: dropdown

例如，氦原子基态的斯莱特行列式如下所示：
``````

$$
\Psi_{He} = \frac{1}{\sqrt{2}}
\begin{vmatrix}
1s(1)\alpha(1) & 1s(1)\beta(1) \\
1s(2)\alpha(2) & 1s(2)\beta(2)
\end{vmatrix}
$$

For lithium the ground-state Slater determinant looks like this:


``````{admonition} 中文翻译
:class: dropdown

对于锂，基态斯莱特行列式如下所示：
``````

$$
\Psi_{\text{Li}} = \frac{1}{\sqrt{3!}}
\begin{vmatrix}
1s(1)\alpha(1) & 1s(1)\beta(1) & 2s(1)\alpha(1) \\
1s(2)\alpha(2) & 1s(2)\beta(2) & 2s(2)\alpha(2) \\
1s(3)\alpha(3) & 1s(3)\beta(3) & 2s(3)\alpha(3)
\end{vmatrix}
$$

## Singlet and Triplet Excited States of Helium

When one electron occupies $1s$ and the other $2s$, their spatial wavefunctions can be combined as:


``````{admonition} 中文翻译
:class: dropdown

当一个电子占据 $1s$ 而另一个占据 $2s$ 时，它们的空间波函数可以组合为：
``````

$$
\Psi_{\text{S}}(1,2)
= \frac{1}{\sqrt{2}}\left[1s(1)2s(2) + 1s(2)2s(1)\right]
\qquad\text{(symmetric)},
$$

$$
\Psi_{\text{A}}(1,2)
= \frac{1}{\sqrt{2}}\left[1s(1)2s(2) - 1s(2)2s(1)\right]
\qquad\text{(antisymmetric)}.
$$

Because electrons are fermions, the **total** wavefunction must be antisymmetric:


``````{admonition} 中文翻译
:class: dropdown

因为电子是费米子，**总**波函数必须是反对称的：
``````

$$
\underbrace{\text{(spatial symmetry)}}_{\Psi_{S/A}}
\times
\underbrace{\text{(spin symmetry)}}_{\chi_{S/A}}
= \text{antisymmetric}
$$

so that

$$
\Psi_{\text{total}}(1,2) = \Psi_{\text{spatial}}(1,2)\,\chi_{\text{spin}}(1,2).
$$

### Triplet states ($S=1$, symmetric spin)

These must pair with the **antisymmetric** spatial part $\Psi_A(1,2)$.


``````{admonition} 中文翻译
:class: dropdown

这些必须与**反对称**空间部分 $\Psi_A(1,2)$ 配对。
``````

**Spin functions:**

$$
\begin{aligned}
\chi_{+1} &= \alpha(1)\alpha(2) \\
\chi_{0} &= \frac{1}{\sqrt{2}}\!\left[\alpha(1)\beta(2)+\beta(1)\alpha(2)\right] \\
\chi_{-1} &= \beta(1)\beta(2)
\end{aligned}
$$

**Total wavefunctions:**

$$
|\psi_{+1}\rangle = \Psi_A(1,2)\,\chi_{+1}
$$

$$
|\psi_{0}\rangle = \Psi_A(1,2)\,\chi_{0}
$$

$$
|\psi_{-1}\rangle = \Psi_A(1,2)\,\chi_{-1}
$$

### Singlet state ($S=0$, antisymmetric spin)

This must pair with the **symmetric** spatial part $\Psi_S(1,2)$.


``````{admonition} 中文翻译
:class: dropdown

这必须与**对称**空间部分 $\Psi_S(1,2)$ 配对。
``````

**Spin function:**

$$
\chi_{\text{singlet}} = \frac{1}{\sqrt{2}}\!\left[\alpha(1)\beta(2) - \beta(1)\alpha(2)\right]
$$

**Total wavefunction:**

$$
|\psi_{\text{singlet}}\rangle = \Psi_S(1,2)\,\chi_{\text{singlet}}
$$

### Action of the Spin Operators

Triplets:

$$
\hat{S}_z|\psi_{+1}\rangle = +\hbar|\psi_{+1}\rangle,\quad
\hat{S}_z|\psi_{0}\rangle = 0,\quad
\hat{S}_z|\psi_{-1}\rangle = -\hbar|\psi_{-1}\rangle
$$

$$
\hat{S}^2|\psi_{+1,0,-1}\rangle = 2\hbar^2|\psi_{+1,0,-1}\rangle
$$

Singlet:

$$
\hat{S}_z|\psi_{\text{singlet}}\rangle = 0,\qquad
\hat{S}^2|\psi_{\text{singlet}}\rangle = 0
$$

### Which is lower in energy?

- The **triplet** has electrons that are **spatially antisymmetric**, so they avoid each other, feel **less Coulomb repulsion**, and lie **lower in energy**.
- The **singlet** is spatially symmetric, so electrons overlap more and lie **higher in energy**.


``````{admonition} 中文翻译
:class: dropdown

- **三重态** 的电子在空间上是 **反对称** 的，因此它们相互避开，感受到 **较小的库仑排斥**，能量 **更低**。
- **单重态**在空间上是对称的，因此电子重叠更多且处于**较高能量**。
``````

This is the origin of **exchange stabilization**.

:::{figure} images/He_exc1.png
:alt: Helium excited singlet and triplet
:width: 500px

Fig. 2 Singlet and triplet excited configurations of helium. The spatially antisymmetric triplet keeps the electrons apart and lies below the spatially symmetric singlet.


``````{admonition} 中文翻译
:class: dropdown

图2 氦原子的单态和 triplet 激发构型。空间反对称的 triplet 使电子保持分离，能量低于空间对称的 singlet。
``````
:::

## Energies of Multi-Electron States

The Hamiltonian is

$$
\hat{H} = \hat{H}_1 + \hat{H}_2 + \hat{H}_{12},
$$

with $\hat{H}_{12}$ corresponding to electron, electron repulsion. The energies are built from three kinds of integral.


``````{admonition} 中文翻译
:class: dropdown

其中 $\hat{H}_{12}$ 对应电子-电子排斥。能量由三种积分构建而成。
``````

:::{important} **Single-electron energy**

$$
I(a) = \int \phi_a^*(r)
\left[
-\frac{\hbar^2}{2m}\nabla^2
- \frac{Ze^2}{4\pi\epsilon_0 r}
\right]
\phi_a(r)\, d\tau
$$

:::

:::{important} **Coulomb Integral**

$$
J_{ij} =
\int |\phi_i(r_1)|^2
\frac{e^2}{4\pi\epsilon_0 r_{12}}
|\phi_j(r_2)|^2 \, d^3r_1 \, d^3r_2,
$$

always **positive**.
:::

:::{important} **Exchange Integral**

$$
K_{ij} =
\int \phi_i^*(r_1)\phi_j^*(r_2)
\frac{e^2}{4\pi\epsilon_0 r_{12}}
\phi_j(r_1)\phi_i(r_2) \, d^3r_1 \, d^3r_2.
$$

Positive, but it leads to **energy lowering** for triplet states.


``````{admonition} 中文翻译
:class: dropdown

为正，但它会导致三重态的**能量降低**。
``````
:::

### Energies of the $1s2s$ Singlet and Triplet

Triplet (antisymmetric spatial):

$$
E_{\text{triplet}} = I(1s) + I(2s) + J(1s,2s) - K(1s,2s)
$$

Singlet (symmetric spatial):

$$
E_{\text{singlet}} = I(1s) + I(2s) + J(1s,2s) + K(1s,2s)
$$

Thus the triplet state is **lower in energy** by $2K(1s,2s)$, due to exchange stabilization.


``````{admonition} 中文翻译
:class: dropdown

因此三重态因交换稳定化而 **能量更低** $2K(1s,2s)$。
``````

:::{figure} images/He_exc2.png
:alt: Exchange splitting of helium states
:width: 500px

Fig. 3 The Coulomb integral $J$ shifts both states up, while the exchange integral $K$ splits them: the triplet drops by $K$ and the singlet rises by $K$.


``````{admonition} 中文翻译
:class: dropdown

图 3 库仑积分 $J$ 使两个态都上移，而交换积分 $K$ 使它们分裂：三重态下降 $K$，单重态上升 $K$。
``````
:::

## Hund's Rule and the Aufbau Principle

Three simple rules govern how electrons fill orbitals in a multi-electron atom.


``````{admonition} 中文翻译
:class: dropdown

三条简单规则决定了电子如何在多电子原子中填充轨道。
``````

:::{figure} images/aufbau.png
:alt: Aufbau filling order
:width: 400px

Fig. 4 Aufbau filling pattern for atomic orbitals: electrons enter orbitals in order of increasing energy.


``````{admonition} 中文翻译
:class: dropdown

图4 原子轨道的构造填充模式：电子按能量递增的顺序进入轨道。
``````
:::

**Aufbau principle.** Electrons fill orbitals in order of increasing energy.


``````{admonition} 中文翻译
:class: dropdown

**构造原理。** 电子按能量递增顺序填充轨道。
``````

**Pauli exclusion principle.** Each orbital holds at most two electrons, and they must have opposite spins.


``````{admonition} 中文翻译
:class: dropdown

**泡利不相容原理。** 每个轨道最多容纳两个电子，且它们必须具有相反的自旋。
``````

**Hund's rule.** Electrons occupy **degenerate orbitals singly with parallel spins** before pairing. This reflects exchange stabilization, exactly the effect we saw splitting helium's triplet below its singlet.


``````{admonition} 中文翻译
:class: dropdown

**Hund规则。** 电子在**退化轨道**中单占并平行自旋之前不成对。这反映了交换稳定化，正是我们在氦原子三重态低于单重态的分裂中看到的效应。
``````

:::{figure} images/Hund1.png
:alt: Hund exchange stabilization
:width: 400px

Fig. 5 Exchange stabilization of the parallel-spin (triplet) arrangement underlies Hund's rule: parallel spins in separate degenerate orbitals minimize repulsion.


``````{admonition} 中文翻译
:class: dropdown

图 5 平行自旋（三重态）排列的交换稳定化是洪特规则的基础：简并轨道中的平行自旋使排斥能最小化。
``````
:::
