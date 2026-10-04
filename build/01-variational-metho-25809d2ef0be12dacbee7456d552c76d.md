---
kernelspec:
  name: python3
  display_name: Python 3
---

# Variational Method

:::{note} **What you will learn**

- **Why we need approximations:** The Schrodinger equation can be solved analytically only for a handful of simple systems. The hydrogen atom is the most complex atomic case with a closed-form solution; helium and any multi-electron system are intractable.
- **The variational theorem:** For any trial wavefunction, the computed energy is always greater than or equal to the true ground-state energy. This gives a rigorous upper bound and a way to rank approximations.
- **Trial functions and parameters:** Start from an educated guess for the wavefunction, then tune its parameters to minimize the energy and approach the exact value.
- **Worked examples:** Particle in a box, the hydrogen atom with Gaussian trial functions, and the helium atom with an effective nuclear charge.
- **The linear variational method:** Expanding the trial function in a basis set turns a hard differential-equation problem into a tractable linear algebra problem, where we solve for eigenvalues and eigenvectors of a matrix. This idea underlies electronic-structure methods such as Hartree-Fock.


``````{admonition} 中文翻译
:class: dropdown

- **为什么我们需要近似：** 只有少数简单系统的薛定谔方程可以解析求解。氢原子是具有闭形式解的最复杂的原子情况；氦和任何多电子系统都是不可处理的。
- **变分定理：** 对于任何试函数，计算出的能量总是大于或等于真实的基态能量。这给出了严格的上界，并提供了一种对近似进行排序的方法。
- **试函数和参数**：从波函数的一个有根据的猜测开始，然后调整其参数以最小化能量并接近精确值。
- **例题：** 箱中粒子、采用高斯试探函数的氢原子、以及采用有效核电荷的氦原子。
- **线性变分法：** 将试函数展开为基函数集，将一个艰难的微分方程问题转化为一个可处理的线性代数问题，我们求解矩阵的特征值和特征向量。这是电子结构方法（如哈特里-福克方法）的基础。
``````
:::

## Why approximations are needed

- The Schrodinger equation can be solved analytically only for simple systems.
- For atomic systems, the hydrogen atom represents the most complex case with an analytical solution.
- For systems with multiple interacting electrons, such as the helium atom or other multi-electron systems, analytical solutions become intractable.
- Approximation methods are therefore essential for finding solutions to complex quantum systems. These methods let us estimate solutions and evaluate how close the approximate results are to the true values.


``````{admonition} 中文翻译
:class: dropdown

- 薛定谔方程仅能对简单体系求得解析解。
- 对于原子体系，氢原子代表了具有解析解的最复杂情况。
- 对于具有多个相互作用电子的体系，如氦原子或其他多电子体系，解析解变得难以求得。
- 因此，近似方法对于求解复杂的量子系统至关重要。这些方法让我们能够估计解并评估近似结果与真实值的接近程度。
``````

The variational method provides a systematic approach for making approximations and a quantitative way to assess the convergence of predictions toward exact values. Its core idea is simple:


``````{admonition} 中文翻译
:class: dropdown

变分法提供了一种系统的近似方法，并定量评估预测值向精确值收敛的过程。其核心思想很简单：
``````

- Begin with an educated guess by selecting a trial function to represent the wavefunction of the system.
- Adjust the parameters of the trial function to minimize the energy, bringing the solution closer to the exact value.


``````{admonition} 中文翻译
:class: dropdown

- 从一个合理的猜测开始，选择一个试函数来表示体系的波函数。
- 调整试函数的参数以使能量最小化，使解更接近精确值。
``````

## Variational theorem

- The variational method states that for any trial (approximate) function $|\phi\rangle$, the computed energy always comes out greater than or equal to the exact (true) ground-state energy.


``````{admonition} 中文翻译
:class: dropdown

- 变分法指出，对于任何试函数 $|\phi\rangle$，计算出的能量总是大于或等于精确（真）基态能量。
``````

:::{important} **Variational Theorem of Quantum Mechanics**

$$
E_{\phi}=\frac{\langle \phi \mid \hat{H}  \mid \phi\rangle}{\langle \phi \mid \phi\rangle} \geq E_0
$$

- $\hat{H}$ is the Hamiltonian of the problem we want to solve.
- $|\phi\rangle$ is a trial wavefunction with unknown parameters we want to determine.
- $E_0$ is the true ground-state energy, which is generally not known to us.


``````{admonition} 中文翻译
:class: dropdown

- $\hat{H}$ 是我们要求解问题的哈密顿量。
- $|\phi\rangle$ 是一个含有待定未知参数的试探波函数。
- $E_0$ 是真实的基态能量，通常我们并不知道它的值。
``````
:::

- When the trial wavefunction is not normalized, we divide by $\langle \phi \mid \phi\rangle$. The expression simplifies when the trial function is normalized beforehand, so that $\langle \phi \mid \phi\rangle=1$.
- If the true ground-state wavefunction $\psi_0$ is inserted in place of the trial function, the equality is reached. For all other (trial) wavefunctions the energy expectation value on the left side will always be larger. The ratio is also called the Rayleigh ratio.


``````{admonition} 中文翻译
:class: dropdown

- 当试函数未归一化时，我们除以 $\langle \phi \mid \phi\rangle$。当试函数先归一化时，表达式会简化，使得 $\langle \phi \mid \phi\rangle=1$。
- 如果真实的基态波函数 $\psi_0$ 代入试函数，则达到等式。对于所有其他（试）波函数，左侧能量期望值将始终更大。该比值也称为莱维比。
``````

### Consequences of the variational theorem

1. **Ground-state energy is the lowest possible energy for the system.**
2. **By minimizing the energy functional we obtain the most accurate prediction for a given trial function.**
3. **More parameters give us more handles to vary, and hence more accurate solutions.**


``````{admonition} 中文翻译
:class: dropdown

- **基态能量是系统可能的最低能量。**
- **通过最小化能量泛函，我们可以获得给定试探函数的最准确预测。**
- **参数越多给我们提供的调节手段越多，从而能得到更精确的解。**
``````

## Worked examples

:::{note} **Example: Particle in a box**

Consider the one-dimensional particle in a box (boundaries at $0$ and $a$). Use the variational theorem to obtain an upper bound for the ground-state energy using the following normalized trial wavefunction:


``````{admonition} 中文翻译
:class: dropdown

考虑一维盒子问题（边界在 $0$ 和 $a$ 处）。使用变分定理，利用以下归一化的试函数获得基态能量的上界：
``````

$$\psi_t(x) = \frac{\sqrt{30}}{a^{5/2}}x(a - x)$$
:::

:::{admonition} **Solution:**
:class: dropdown solution

Clearly this is not the correct ground-state wavefunction. First we check that it satisfies the boundary conditions: $\psi_t(0) = 0$ and $\psi_t(a) = 0$ (OK). The Hamiltonian for this problem is:


``````{admonition} 中文翻译
:class: dropdown

显然这不是正确的基态波函数。首先我们检查它是否满足边界条件：$\psi_t(0) = 0$ 和 $\psi_t(a) = 0$（OK）。此问题的哈密顿量是：
``````

$$\hat{H} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2}, \quad 0\le x\le a$$

Plugging both the Hamiltonian and $\psi_t$ into the energy expression gives:


``````{admonition} 中文翻译
:class: dropdown

将哈密顿量和 $\psi_t$ 代入能量表达式得到：
``````

$$\int_0^a\psi_t^*\hat{H}\psi_t \, d\tau = -\frac{30\hbar^2}{2a^5m}\int_0^a\left( ax - x^2\right)\frac{d^2}{dx^2}\left( ax - x^2\right)dx$$

$$= \frac{30\hbar^2}{a^5m}\int_0^a\left( ax-x^2\right) dx = \frac{5\hbar^2}{a^2m}\ge E_1$$

As indicated, this gives an upper limit for the ground-state energy $E_1$.


``````{admonition} 中文翻译
:class: dropdown

如图所示，这给出了基态能量 $E_1$ 的一个上限。
``````
:::

:::{note} **Example: Hydrogen atom with a Gaussian trial function**

- The exact solution for the ground state is $\psi(r)=\frac{1}{(\pi a^3_0)^{1/2}}e^{-r/a_0}$ with $E_1 = -0.5 \, h$ (in Hartree atomic units).
- Use a trial function $\phi=e^{-\alpha r^2}$ to predict the ground-state energy.


``````{admonition} 中文翻译
:class: dropdown

- 基态的精确解为 $\psi(r)=\frac{1}{(\pi a^3_0)^{1/2}}e^{-r/a_0}$，能量 $E_1 = -0.5 \, h$（哈特里原子单位制）。
- 使用试探函数 $\phi=e^{-\alpha r^2}$ 来预测基态能量。
``````
:::

:::{admonition} **Solution:**
:class: dropdown solution

Plug the trial function into the energy expression, computing the energy as a function of the parameter $\alpha$:


``````{admonition} 中文翻译
:class: dropdown

将试探函数代入能量表达式，计算作为参数 $\alpha$ 函数的能量：
``````

$$
E_{trial} = \frac{\langle \phi \mid \hat{H}  \mid \phi\rangle}{\langle \phi \mid \phi\rangle}
$$

$$
E_{trial}(\alpha) = \frac{4\pi \int^{\infty}_0  e^{-\alpha r^2}\left[-\frac{\hbar^2}{2\mu}\nabla_r^2 -\frac{e^2}{4\pi \epsilon_0 r}\right] e^{-\alpha r^2} \, r^2 dr }{4\pi \int^{\infty}_0 e^{-2\alpha r^2} r^2 dr}
$$

$$
E_{trial}(\alpha)=\frac{3\hbar^2 \alpha}{2m_e}-\frac{e^2 \alpha^{1/2}}{\sqrt{2}\epsilon_0 \pi^{3/2}}
$$

Minimization with respect to the parameter $\alpha$ gives the best value of the energy:


``````{admonition} 中文翻译
:class: dropdown

对参数 $\alpha$ 求极小值可得能量的最佳值：
``````

$$
\frac{\partial E_{trial}(\alpha)}{\partial \alpha} = 0
$$

$$
\alpha_{min} = \frac{m_e e^4}{18 \pi^3 \epsilon^2_0 \hbar^4}
$$

Finally, we plug this parameter back into the energy function to obtain the energy minimized with respect to $\alpha$, that is $E(\alpha_{min})$:


``````{admonition} 中文翻译
:class: dropdown

最后，我们将这个参数代回能量函数，得到关于 $\alpha$ 极小化的能量，即 $E(\alpha_{min})$：
``````

$$
E_0 = -0.5 \, h, \qquad E_{trial}(\alpha_{min}) = -0.424
$$

This is about 15% error. Not too bad for a start. Adding more parameters and functions will reduce the error.


``````{admonition} 中文翻译
:class: dropdown

这大约有 15% 的误差。作为开端不算太坏。增加更多参数和函数将减小误差。
``````
:::

## The helium atom is tough

- The Schrodinger equation for the helium atom is already extremely complicated mathematically. No analytic solution to this equation has been found. However, with certain approximations, useful results can be obtained. The Hamiltonian for the He atom can be written as:


``````{admonition} 中文翻译
:class: dropdown

- 氦原子的薛定谔方程在数学上已经极其复杂。人们尚未找到该方程的解析解。然而，通过某些近似，可以得到有用的结果。氦原子的哈密顿量可以写成：
``````

$${\hat{H} = \underbrace{-\frac{\hbar^2}{2m_e}\left(\Delta_1 + \Delta_2\right)}_{\textnormal{Kinetic energy}}
\underbrace{- \frac{1}{4\pi\epsilon_0}\left(\frac{Ze^2}{r_1} + \frac{Ze^2}{r_2} \overbrace{- \frac{e^2}{r_{12}}}^{\textnormal{Tough!}}\right)}_{\textnormal{Potential energy}}}$$

- Here $\Delta_1$ is the Laplacian for the coordinates of electron 1 and $\Delta_2$ for electron 2; $r_1$ is the distance of electron 1 from the nucleus, $r_2$ the distance of electron 2 from the nucleus, and $r_{12}$ the distance between electrons 1 and 2. For the He atom $Z = 2$.


``````{admonition} 中文翻译
:class: dropdown

- 这里 $\Delta_1$ 是电子 1 坐标的拉普拉斯算子，$\Delta_2$ 是电子 2 的；$r_1$ 是电子 1 离原子的距离，$r_2$ 是电子 2 离原子的距离，$r_{12}$ 是电子 1 和电子 2 之间的距离。对于 He 原子 $Z = 2$。
``````

### Independent-electron approximation

- Ignore the tough term containing $r_{12}$. In this case the Hamiltonian becomes a sum of two hydrogen-like atoms:


``````{admonition} 中文翻译
:class: dropdown

- 忽略含 $r_{12}$ 的困难项。此时哈密顿量变为两个类氢原子之和：
``````

$${\hat{H} = \hat{H}_1 + \hat{H}_2}$$

$${\hat{H}_1 = -\frac{\hbar^2}{2m_e}\Delta_1 - \frac{Ze^2}{4\pi\epsilon_0r_1}}$$

$${\hat{H}_2 = -\frac{\hbar^2}{2m_e}\Delta_2 - \frac{Ze^2}{4\pi\epsilon_0r_2}}$$

- Because the Hamiltonian is a sum of two independent parts, the Schrodinger equation separates into two (each a hydrogen-like atom equation):


``````{admonition} 中文翻译
:class: dropdown

- 因为哈密顿量是两个独立部分的和，薛定谔方程可分离为两个方程（各为一个类氢原子方程）：
``````

$${\hat{H}_1\psi(r_1) = E_1\psi(r_1)}$$
$${\hat{H}_2\psi(r_2) = E_2\psi(r_2)}$$

The total energy is a sum of $E_1$ and $E_2$, and the total wavefunction is a product of $\psi(r_1)$ and $\psi(r_2)$. Based on our previous wavefunction table for hydrogen-like atoms:


``````{admonition} 中文翻译
:class: dropdown

总能量是 $E_1$ 和 $E_2$ 的和，总波函数是 $\psi(r_1)$ 和 $\psi(r_2)$ 的积。基于氢样本原子的先前波函数表:
``````

$${E = E_1 + E_2 = -RZ^2\left(\frac{1}{n_1^2} + \frac{1}{n_2^2}\right)}$$

$${\psi(r_1)\psi(r_2) = \frac{1}{\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}e^{-Zr_1/a_0}\frac{1}{\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}e^{-Zr_2/a_0}
=\frac{1}{\pi}\left(\frac{Z}{a_0}\right)^3e^{-Z(r_1 + r_2)/a_0}}$$

### Consequences of the independent-electron approximation

- For a ground-state He atom both electrons reside in the lowest-energy orbital, so the total wavefunction is $\psi(r_1,r_2) = \psi(r_1)\psi(r_2) = \psi(1)\psi(2) = 1s(1)1s(2)$. The energy from this approximation is not sufficiently accurate (it misses electron-electron repulsion), but the wavefunction is useful for qualitative analysis. The variational principle gives a systematic way to assess how good our approximation is.
- The exact ground-state energy has been found (by very extensive analytic and numerical calculations) to be $-79.0$ eV. Using the approximate wavefunction, we can calculate the expectation value of the energy. This yields $-74.8$ eV, so the error in energy for this wavefunction is $5.2$ eV. Note that the approximate value is, in accordance with the variational principle, higher than the true energy.


``````{admonition} 中文翻译
:class: dropdown

- 对于基态 He 电子，两个电子都居于最低能轨道，因此总波函数为 $\psi(r_1,r_2) = \psi(r_1)\psi(r_2) = \psi(1)\psi(2) = 1s(1)1s(2)$。此近似下的能量不够准确（漏掉了电-电排斥），但该波函数有利于定性分析。变分原理提供了一种系统的方法来评估我们近似的好坏。
- 精确的基态能量已通过大量的解析和数值计算找到，结果为 $-79.0$ eV。使用近似波函数，可以计算能量的期望值。这得到 $-74.8$ eV，所以该波函数能量的误差为 $5.2$ eV。注意，根据变分原理，近似值高于真实能量。
``````

### A better approximation

- We take the wavefunction from the previous step and use the nuclear charge $Z$ as a variational parameter. The variational principle states that minimizing the energy expectation value with respect to $Z$ should approach the true value from above (but will not reach it).
- The obtained value of $Z$ is less than the true $Z$ (= 2). This can be understood in terms of electrons shielding the nucleus from each other, giving a reduced effective nuclear charge.


``````{admonition} 中文翻译
:class: dropdown

- 我们从上一步的波函数开始，并将核电荷 $Z$ 作为变分参数。变分原理指出，关于 $Z$ 最小化能量期望值应该从上方逼近真实值（但不会达到它）。
- 得到的 $Z$ 值小于真实的 $Z$ (= 2)。这可以用电子相互屏蔽核的概念来理解，从而得到有效核电荷的降低。
``````

$${E = \langle\psi |\hat{H}|\psi\rangle = ... = \left[ Z^2 - \frac{27Z}{8}\right]\frac{e^2}{4\pi\epsilon_0a_0}}$$

- To minimize this expression we differentiate with respect to $Z$ and set it to zero (the extremum here is clearly a minimum):


``````{admonition} 中文翻译
:class: dropdown

- 为了使该表达式最小化，我们对 $Z$ 求导并令其为零（此处的极值显然是最小值）：
``````

$${\frac{dE}{dZ} = \left(2Z - \frac{27}{8}\right)\frac{e^2}{4\pi\epsilon_0a_0} = 0}$$

- This gives $Z = 27/16 \approx 1.7$ and $E \approx -77.5$ eV (compared with $-74.8$ eV before and $-79.0$ eV exact). This result could be improved by adding more terms and variables to the trial wavefunction. For example, higher hydrogen-like orbitals with appropriate variational coefficients would yield a much better result.


``````{admonition} 中文翻译
:class: dropdown

- 这给出了 $Z = 27/16 \approx 1.7$ 和 $E \approx -77.5$ eV（与 $-74.8$ eV 之前和 $-79.0$ eV 精确值相比）。此结果可通过向试验波函数中添加更多项和变量来改进。例如，带有适当变分系数的更高氢原子样态轨道将获得更好的结果。
``````

## The linear variational method

- How does the variational method scale to harder problems in practice? If we cannot solve for $\psi$ exactly, we can expand the wavefunction in a convenient **basis set** $f_n$ (a set of functions indexed by $n$, like a Fourier series) and tune the expansion to get as close as possible to the true energy and wavefunction.


``````{admonition} 中文翻译
:class: dropdown

- 如果无法精确求解 $\psi$，我们可以将波函数展开为一个方便的 **基组** $f_n$（按 $n$ 索引的一组函数，如傅里叶级数），并调整展开以尽可能逼近真实的能量和波函数。
``````

$$\phi(r) = \sum_n^N c_nf_n(r)$$

- With an infinite number of basis functions we could in principle approximate any function and obtain a nearly exact numerical solution. Computationally this is not feasible, so we truncate the expansion to a finite number $N$ of basis functions and minimize the energy with respect to the coefficients $c_n$.
- Using a linear combination of trial functions transforms a difficult quantum-mechanics problem into a more tractable linear algebra task: instead of solving differential equations for eigenfunctions and eigenvalues, we solve for the eigenvalues and eigenvectors of a matrix.


``````{admonition} 中文翻译
:class: dropdown

- 理论上，使用无限多的基函数可以近似任意函数并获得近似精确的数值解。然而，从计算角度来看这是不切实际的，因此我们将展开式截断为有限的 $N$ 个基函数，并将能量关于系数 $c_n$ 最小化。
- 使用试函数的线性组合将困难的量子力学问题转化为更易处理的线性代数任务：不再对欧拉函数和特征值求解微分方程，而是求解矩阵的特征值和特征向量。
``````

### A two-function example

- We illustrate the idea and the general matrix construction with a simple example of two basis functions ($N=2$):


``````{admonition} 中文翻译
:class: dropdown

- 我们用一个包含两个基函数（$N=2$）的简单例子来说明这一思路和一般的矩阵构造：
``````

$$\phi = c_1f_1 + c_2f_2$$

- There is no need to define these functions explicitly yet, so we leave them as generic functions $f_1$ and $f_2$. The energy is:


``````{admonition} 中文翻译
:class: dropdown

- 目前无需显式定义这些函数，因此我们将它们保留为通用函数 $f_1$ 和 $f_2$。能量为：
``````

$$E_\phi = \frac{\langle\phi|\hat{H}|\phi\rangle}{\langle\phi|\phi\rangle} = \frac{\langle c_1f_1 + c_2f_2|\hat{H}|c_1f_1 + c_2f_2 \rangle}{\langle c_1f_1 + c_2f_2|c_1f_1 + c_2f_2 \rangle}$$

- Expanding the brackets, the numerator and denominator are built from two kinds of matrix elements, the **Hamiltonian matrix** elements $H_{ij}$ and the **overlap matrix** elements $S_{ij}$:


``````{admonition} 中文翻译
:class: dropdown

- 展开括号后，分子式由两类矩阵元组成：**哈密顿矩阵**元素 $H_{ij}$ 和**重叠矩阵**元素 $S_{ij}$：
``````

$$H_{ij} = \langle f_i|\hat{H}|f_j\rangle, \qquad S_{ij} = \langle f_i|f_j\rangle$$

so that

$$E_\phi = \frac{c_1^2 H_{11} + 2 c_1 c_2 H_{12} + c_2^2 H_{22}}{c_1^2 S_{11} + 2 c_1 c_2 S_{12} + c_2^2 S_{22}}$$

### Minimization leads to a generalized eigenvalue problem

- Since $E_\phi \geq E_0$ for any trial function $\phi$, we minimize $E_\phi$ by varying the parameters $c_1$ and $c_2$.
- Minimizing with respect to $c_1$ means differentiating $E_\phi$ with respect to $c_1$ and setting the derivative to zero:


``````{admonition} 中文翻译
:class: dropdown

- 由于对于任何试探函数 $\phi$ 都有 $E_\phi \geq E_0$，我们通过改变参数 $c_1$ 和 $c_2$ 来使 $E_\phi$ 最小化。
- 关于 $c_1$ 求极小值意味着对 $E_\phi$ 关于 $c_1$ 求导并令导数为零：
``````

$$\frac{\partial E_\phi}{\partial c_1} = 0 = c_1(H_{11} - ES_{11}) + c_2(H_{12} - ES_{12})$$

- Minimizing with respect to $c_2$ gives:

$$\frac{\partial E_\phi}{\partial c_2} = 0 = c_1(H_{12} - ES_{12}) + c_2(H_{22} - ES_{22})$$

- These two coupled linear equations can be written compactly as a matrix equation:


``````{admonition} 中文翻译
:class: dropdown

- 这两个耦合线性方程可以紧凑地写成矩阵方程：
``````

:::{important} **Linear variational (generalized eigenvalue) problem**

$$
\mathbf{H}\mathbf{c} = E\,\mathbf{S}\mathbf{c}
$$

$$
\begin{bmatrix} H_{11} & H_{12} \\ H_{12} & H_{22} \end{bmatrix}
\begin{bmatrix} c_1 \\ c_2 \end{bmatrix}
= E
\begin{bmatrix} S_{11} & S_{12} \\ S_{12} & S_{22} \end{bmatrix}
\begin{bmatrix} c_1 \\ c_2 \end{bmatrix}
$$

- $\mathbf{H}$ is the Hamiltonian matrix with elements $H_{ij} = \langle f_i|\hat{H}|f_j\rangle$.
- $\mathbf{S}$ is the overlap matrix with elements $S_{ij} = \langle f_i|f_j\rangle$.
- The lowest eigenvalue $E$ is the variational estimate of the ground-state energy; the corresponding eigenvector $\mathbf{c}$ gives the best coefficients.


``````{admonition} 中文翻译
:class: dropdown

- $\mathbf{H}$ 是哈密顿矩阵，其元素为 $H_{ij} = \langle f_i|\hat{H}|f_j\rangle$。
- $\mathbf{S}$ 是重叠矩阵，其元素为 $S_{ij} = \langle f_i|f_j\rangle$。
- 最低本征值 $E$ 是基态能量的变分估计；对应的本征向量 $\mathbf{c}$ 给出最佳系数。
``````
:::

- A nontrivial solution exists only when the secular determinant vanishes, $\det(\mathbf{H} - E\,\mathbf{S}) = 0$. Solving this determinant gives the variational energies. For an orthonormal basis ($\mathbf{S} = \mathbf{I}$) this reduces to the ordinary eigenvalue problem $\mathbf{H}\mathbf{c} = E\mathbf{c}$.


``````{admonition} 中文翻译
:class: dropdown

- 只有当 secular determinant（ secular 行列式）消去时，才存在非平凡解，即 $\det(\mathbf{H} - E\,\mathbf{S}) = 0$。求解此行列式得到变分能量。对于正交基组（$\mathbf{S} = \mathbf{I}$），这简化为普通的特征值问题 $\mathbf{H}\mathbf{c} = E\mathbf{c}$。
``````

:::{tip} **Worked example: particle in a box by linear variation**
:class: dropdown

Consider a free particle in 1D bound to $0\leq x\leq a$, with Hamiltonian $\hat{H} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2}$. Although we can solve this analytically, it is instructive to see the variational solution. We approximate $\psi(x)$ as an expansion in two basis functions $f_1=x(a-x)$ and $f_2=x^2(a-x)^2$:


``````{admonition} 中文翻译
:class: dropdown

考虑一个自由粒子在 1D 中受限于 $0\leq x\leq a$，哈密顿量 $\hat{H} = -\frac{\hbar^2}{2m}\frac{d^2}{dx^2}$。虽然我们可以解析解，但看到变分解也很有 instructive。我们将 $\psi(x)$ 近似为两个基函数 $f_1=x(a-x)$ 和 $f_2=x^2(a-x)^2$ 的展开：
``````

$$\psi(x) \approx c_1x(a-x) + c_2x^2(a-x)^2$$

Computing the matrix elements (by integrating each $\langle f_i|\hat{H}|f_j\rangle$ and $\langle f_i|f_j\rangle$ over $0\le x\le a$) gives:


``````{admonition} 中文翻译
:class: dropdown

计算矩阵元素（通过在 $0\le x\le a$ 上积分每个 $\langle f_i|\hat{H}|f_j\rangle$ 和 $\langle f_i|f_j\rangle$）得到：
``````

$$\mathbf{H} = \frac{\hbar^2a^3}{m} \begin{bmatrix} \frac{1}{6} & \frac{a^2}{30}\\ \frac{a^2}{30} & \frac{a^4}{105} \end{bmatrix}, \qquad
\mathbf{S} = \frac{a^5}{10} \begin{bmatrix} \frac{1}{3} & \frac{a^2}{14}\\ \frac{a^2}{14} & \frac{a^4}{63} \end{bmatrix}$$

Solving the generalized eigenvalue problem (with $a = \hbar = m = 1$) gives a lowest energy of


``````{admonition} 中文翻译
:class: dropdown

求解广义本征值问题（令 $a = \hbar = m = 1$）可得最低能量为
``````

$$E_\phi = 4.9349 \, \frac{\hbar^2}{m}$$

which is essentially the exact analytic value $E_1 = \frac{\pi^2\hbar^2}{2} \approx 4.9348 \, \frac{\hbar^2}{m}$. The variational solution captures both the energy and the shape of the ground-state wavefunction. See the demo notebooks at the end of this chapter for the full calculation and plots.


``````{admonition} 中文翻译
:class: dropdown

这本质上是精确的解析值 $E_1 = \frac{\pi^2\hbar^2}{2} \approx 4.9348 \, \frac{\hbar^2}{m}$。变分解既捕获了能量也捕获了基态波函数的形状。参见本章末尾的演示笔记本，获取完整的计算和图形绘制。
``````
:::

## Problems

#### Problem 1

::::{admonition} **Problem 1: Hydrogen atom by variation**
:class: note

Use the variational principle to obtain the lowest-energy solution to the hydrogen atom Schrodinger equation in spherical coordinates using the following trial wavefunctions:


``````{admonition} 中文翻译
:class: dropdown

使用变分原理，利用以下试函数，获得氢原子薛定谔方程在球坐标中的最低能量解：
``````

- (a) $\psi_{trial} = e^{-kr}$ with $k$ as a variational parameter.
- (b) $\psi_{trial} = e^{-kr^2}$ with $k$ as a variational parameter.
- (c) Which trial function gives the better (lower) energy?


``````{admonition} 中文翻译
:class: dropdown

- (a) $\psi_{trial} = e^{-kr}$，其中 $k$ 为变分参数。
- (b) $\psi_{trial} = e^{-kr^2}$，其中 $k$ 为变分参数。
- (c) 哪个试探函数给出的能量更好（更低）？
``````

Both trial functions depend only on $r$, so the angular terms drop out of the Laplacian. You may find the following integrals useful:


``````{admonition} 中文翻译
:class: dropdown

两个试探函数都只依赖于 $r$，因此拉普拉斯算子中的角度项消失。你可能会用到以下积分：
``````

$$\int_0^\infty x^ne^{-ax}dx = \frac{n!}{a^{n+1}}, \qquad \int_0^\infty x^me^{-ax^2}dx = \frac{\Gamma[(m + 1)/2]}{2a^{(m + 1) / 2}}$$

$$\Gamma[n + 1] = n!, \qquad \Gamma[n + 1] = n\Gamma[n], \qquad \Gamma\left[\frac{1}{2}\right] = \sqrt{\pi}$$

:::{admonition} **Solution:**
:class: dropdown solution

Use the variational principle and employ spherical coordinates in the integrations:


``````{admonition} 中文翻译
:class: dropdown

使用变分原理，并在积分中采用球坐标：
``````

$$E = \frac{\int\psi^*_{trial}H\psi_{trial}d\tau}{\int\psi^*_{trial}\psi_{trial}d\tau}$$

**(a)** Normalization integral:

$$\int\psi^*_{trial}\psi_{trial}d\tau = \int_0^\infty e^{-2kr}
\underbrace{4\pi r^2dr}_{d\tau} = 4\pi\int_0^\infty r^2e^{-2kr}dr
= \frac{\pi}{k^3}$$

Energy numerator:

$$\int\psi_{trial}^*H\psi_{trial}d\tau = \int\left( e^{-kr}\right)
\left( -\frac{\hbar^2}{2m_e}\Delta - \frac{e^2}{4\pi\epsilon_0r}\right)
\left( e^{-kr}\right)d\tau$$

$$= -\frac{4\pi\hbar^2}{2m_e}\int_0^\infty e^{-2kr}(r^2k^2 - 2kr)dr
- \frac{e^2}{\epsilon_0}\int_0^\infty re^{-2kr}dr$$

$$= -\frac{\pi\hbar^2}{2m_ek} + \frac{\pi\hbar^2}{m_ek}
- \frac{e^2}{4k^2\epsilon_0}$$

Dividing numerator by denominator:

$$E = \frac{\hbar^2k^2}{2m_e} - \frac{e^2k}{4\pi\epsilon_0}$$

Minimize with respect to $k$:

$$\frac{dE}{dk} = \frac{\hbar^2k}{m_e} - \frac{e^2}{4\pi\epsilon_0} = 0
\Rightarrow k = \frac{m_ee^2}{4\pi\epsilon_0\hbar^2} \Rightarrow
E = -\frac{1}{2}\frac{m_ee^4}{(4\epsilon_0)^2\hbar^2} = -hcR$$

where $R$ is the Rydberg constant. This trial function recovers the exact ground-state energy because it has the correct functional form.


``````{admonition} 中文翻译
:class: dropdown

其中 $R$ 是里德伯常数。该试探函数因具有正确的函数形式，能恢复精确的基态能量。
``````

**(b)** The logic is identical. The normalization integral is


``````{admonition} 中文翻译
:class: dropdown

**(b)** 逻辑相同。归一化积分为
``````

$$\int\psi^*_{trial}\psi_{trial}d\tau = \frac{4\pi\Gamma[3/2]}{2(2k)^{3/2}}
= \frac{\pi^{3/2}}{(2k)^{3/2}}$$

The Laplacian of the Gaussian is

$$\Delta\psi_{trial} = \left( 4k^2r^2 - 6k\right) e^{-kr^2}$$

Carrying out the integrals gives the energy

$$E = \frac{3\hbar^2k}{2m_e} - \frac{e^2\sqrt{k}}{\sqrt{2}\pi^{3/2}\epsilon_0}$$

Minimizing,

$$\frac{\partial E}{\partial k} = \frac{3\hbar^2}{2m_e} - \frac{e^2}{2\sqrt{2}\pi^{3/2}\epsilon_0\sqrt{k}} = 0
\Rightarrow k = \frac{m_e^2e^4}{18\pi^3\epsilon_0^2\hbar^4}$$

and the total energy at this point is


``````{admonition} 中文翻译
:class: dropdown

这一点的总能量为
``````

$$E = -\frac{m_ee^4}{12\pi^3\epsilon_0^2\hbar^2} = -\frac{8}{3\pi}hcR \approx -0.85\,hcR$$

**(c)** The function in (a) gives the lower energy ($-1.0\,hcR$ versus $-0.85\,hcR$) and is therefore the better trial function. The exponential has the correct cusp at the origin, while the Gaussian does not.


``````{admonition} 中文翻译
:class: dropdown

**(c)** 函数 (a) 给出的能量较低（$-1.0\,hcR$ 对比 $-0.85\,hcR$），因此是更好的试函数。指数函数在原点处有正确的cusp，而高斯函数没有。
``````
:::
::::

#### Problem 2

::::{admonition} **Problem 2: Why is the bound always from above?**
:class: note

Expand an arbitrary normalized trial function in the exact eigenbasis of $\hat{H}$, $|\phi\rangle = \sum_n a_n |\psi_n\rangle$ with $\hat{H}|\psi_n\rangle = E_n|\psi_n\rangle$ and $E_0 \le E_1 \le E_2 \le \dots$. Show that $\langle \phi|\hat{H}|\phi\rangle = \sum_n |a_n|^2 E_n \ge E_0$, and state the condition under which equality holds.


``````{admonition} 中文翻译
:class: dropdown

展开一个任意归一化的试函数，在 $\hat{H}$ 的精确本征基下：$|\phi\rangle = \sum_n a_n |\psi_n\rangle$，其中 $\hat{H}|\psi_n\rangle = E_n|\psi_n\rangle$ 且 $E_0 \le E_1 \le E_2 \le \dots$。证明 $\langle \phi|\hat{H}|\phi\rangle = \sum_n |a_n|^2 E_n \ge E_0$，并说明等号成立的条件。
``````

:::{admonition} **Solution:**
:class: dropdown solution

Because the $|\psi_n\rangle$ are orthonormal,

$$\langle \phi|\hat{H}|\phi\rangle = \sum_{n,m} a_m^* a_n \langle \psi_m|\hat{H}|\psi_n\rangle = \sum_{n,m} a_m^* a_n E_n \delta_{mn} = \sum_n |a_n|^2 E_n.$$

Normalization gives $\sum_n |a_n|^2 = 1$. Since every $E_n \ge E_0$,


``````{admonition} 中文翻译
:class: dropdown

归一化给出 $\sum_n |a_n|^2 = 1$。因为每个 $E_n \ge E_0$，
``````

$$\sum_n |a_n|^2 E_n \ge \sum_n |a_n|^2 E_0 = E_0.$$

Equality holds only when all the weight is on the ground state, $|a_0|^2 = 1$ and $a_{n\neq 0} = 0$, that is when the trial function equals the exact ground-state wavefunction.


``````{admonition} 中文翻译
:class: dropdown

当且仅当所有权重都在基态时成立，即 $|a_0|^2 = 1$ 且 $a_{n\neq 0} = 0$，即试函数等于精确基态波函数。
``````
:::
::::

#### Problem 3

::::{admonition} **Problem 3: Effective nuclear charge of helium**
:class: note

Using the helium trial energy $E(Z) = \left[ Z^2 - \frac{27Z}{8}\right]\frac{e^2}{4\pi\epsilon_0a_0}$, confirm that the optimal effective nuclear charge is $Z = 27/16$ and explain physically why $Z < 2$.


``````{admonition} 中文翻译
:class: dropdown

使用氦原子试能量 $E(Z) = \left[ Z^2 - \frac{27Z}{8}\right]\frac{e^2}{4\pi\epsilon_0a_0}$，确认最优有效核电荷为 $Z = 27/16$，并解释为什么 $Z < 2$的物理意义。
``````

:::{admonition} **Solution:**
:class: dropdown solution

Set the derivative to zero:

$$\frac{dE}{dZ} = \left(2Z - \frac{27}{8}\right)\frac{e^2}{4\pi\epsilon_0a_0} = 0 \Rightarrow Z = \frac{27}{16} \approx 1.69.$$

The effective charge is less than the true $Z = 2$ because each electron partially screens the nucleus from the other. From the viewpoint of one electron, the nuclear charge appears reduced by the average presence of the second electron, so the optimal variational charge is smaller than the bare value.


``````{admonition} 中文翻译
:class: dropdown

有效电荷小于真实的 $Z = 2$，因为每个电子部分屏蔽核对另一个电子的作用。从一个电子的角度看，由于第二个电子的平均存在，核电荷看起来被减小了，所以最优变分电荷小于裸值。
``````
:::
::::

#### Problem 4

::::{admonition} **Problem 4: Linear variation with an orthonormal basis**
:class: note

In the linear variational method, the trial energy satisfies $\mathbf{H}\mathbf{c} = E\,\mathbf{S}\mathbf{c}$. Show that if the basis functions are orthonormal ($\mathbf{S} = \mathbf{I}$), this reduces to an ordinary eigenvalue problem, and explain what the eigenvalues and eigenvectors represent.


``````{admonition} 中文翻译
:class: dropdown

在线性变分法中，试函数能量满足 $\mathbf{H}\mathbf{c} = E\,\mathbf{S}\mathbf{c}$。若基函数正交归一 ($\mathbf{S} = \mathbf{I}$)，则简化为普通特征值问题。说明特征值和特征向量的物理意义。
``````
::::

#### Problem 5

::::{admonition} **Problem 5: Secular determinant for two states**
:class: note

For a two-function basis with $H_{11} = \alpha$, $H_{22} = \alpha$, $H_{12} = \beta$, and an orthonormal basis ($S_{11} = S_{22} = 1$, $S_{12} = 0$), solve the secular determinant $\det(\mathbf{H} - E\mathbf{I}) = 0$ and show that the two variational energies are $E_\pm = \alpha \pm \beta$. (This is the bonding and antibonding splitting of two identical atomic orbitals.)


``````{admonition} 中文翻译
:class: dropdown

对于具有两个基函数的情况，$H_{11} = \alpha$，$H_{22} = \alpha$，$H_{12} = \beta$，以及正交标准基 ($S_{11} = S_{22} = 1$，$S_{12} = 0$)，解出 secular determinant $\det(\mathbf{H} - E\mathbf{I}) = 0$ 并表明两个变分能量为 $E_\pm = \alpha \pm \beta$。(这是两个相同原子轨道的键合和反键合分裂。)
``````
::::
