---
kernelspec:
  name: python3
  display_name: Python 3
---

# Hydrogenlike Atoms

:::{note} **What you will learn**

- The **hydrogen atom** is the simplest atom for which the Schrödinger equation can be solved exactly. In contrast, helium, though it has only one additional electron, cannot be solved exactly due to the complexity introduced by electron-electron interactions.
- Solving the Schrödinger equation for the hydrogen atom leverages the fact that the **Coulomb potential from the nucleus is isotropic**: it is radially symmetric and depends solely on the distance from the nucleus. This **symmetry leads to degeneracies in the energy levels**.
- While the resulting energy eigenfunctions (atomic orbitals) are not necessarily isotropic, their dependence on angular coordinates arises fundamentally from the isotropy of the underlying potential.
- Because angular momentum is conserved, energy eigenvalues can be classified by two angular momentum quantum numbers, $l$ and $m$ (both integers), which quantize the magnitude and projection of angular momentum.
- **Atomic orbitals** derived for hydrogen are also foundational in describing the structure of multi-electron atoms and molecules.


``````{admonition} 中文翻译
:class: dropdown

- **氢原子** 是薛定谔方程可以精确求解的最简单原子。相比之下，氦原子虽然只多一个电子，但由于电子-电子相互作用引入的复杂性，无法精确求解。
- 求解氢原子的薛定谔方程利用了一个事实：来自原子核的**库仑势是各向同性的**：它径向对称且仅取决于相对于原子核的距离。这种**对称性导致能级的简并性**。
- 得到的能量本征函数（原子轨道）不一定是各向同性的，但它们在角坐标上的依赖性根本上源于底层势场的各向同性。
- 由于角动量守恒，能量本征值可以由两个角动量量子数 $l$ 和 $m$（均为整数）来分类，这量子化了角动量的大小和分量。
- 为氢原子推导出的**原子轨道**也是描述多电子原子和分子结构的基础。
``````
:::

### Schrödinger equation for hydrogenlike atoms

- Consider one electron and one nucleus with charge $Ze$, where $e$ is the magnitude of the electron charge ($1.6021773 \times 10^{-19}$ C) and $Z$ is the atomic number. Examples of such systems are H, $He^+$, and $Li^{2+}$.

- We can reduce the two-body problem to a one-body problem of an electron with reduced mass moving with respect to a fixed nucleus. Since the electron is much lighter compared to the nucleus, we can use the electron mass instead of the reduced mass, $\mu \approx m_e$.

- We have a problem of one particle moving in a symmetric potential field in 3D. We expect to get 3 quantum numbers and anticipate some degeneracies due to this radial symmetry.

- **Kinetic energy operator** in 3D is the same as for the particle in a box in 3D:


``````{admonition} 中文翻译
:class: dropdown

- 考虑一个电子和一个带电量为 $Ze$ 的核，其中 $e$ 是电子电荷的大小（$1.6021773 \times 10^{-19}$ C）且 $Z$ 是原子序数。此类系统的例子有 H、$He^+$ 和 $Li^{2+}$。
- 我们可以将两体问题简化为电子的单体问题，该电子具有归一化质量并相对于固定核运动。由于电子的质量远小于核，我们可以使用电子质量代替归一化质量，$\mu \approx m_e$。
- 我们有一个粒子在三维对称势场中运动。我们期望得到3个量子数，并由于这种径向对称性而预期出现某些简并。
- 三维中的**动能算符**与三维势箱中的粒子相同：
``````

$$\frac{\hbar^2}{2m_e}\nabla^2$$

- **Potential energy operator** consists of one Coulomb term encoding the electrostatic attraction between nucleus and electron:


``````{admonition} 中文翻译
:class: dropdown

- **势能算符**包含一个库仑项，描述原子核与电子间的静电吸引：
``````

$$V = - \frac{Ze^2}{4\pi\epsilon_0 r}$$

- Here $m_e$ is the electron mass and $\epsilon_0$ is the [vacuum permittivity](http://en.wikipedia.org/wiki/Vacuum_permittivity).


``````{admonition} 中文翻译
:class: dropdown

- 这里 $m_e$ 是电子质量，而 $\epsilon_0$ 是[真空介电常数](http://en.wikipedia.org/wiki/Vacuum_permittivity)。
``````

### H-atom in the spherical coordinate system

- The Schrödinger equation for the H atom is a problem in full three dimensions with kinetic and potential energy terms. We also expect to get infinitely many eigenfunctions and eigenvalues since we have a bound electron.


``````{admonition} 中文翻译
:class: dropdown

- 氢原子的薛定谔方程是一个三维全问题，包含动能和势能项。我们也期望获得无限多个本征函数和本征值，因为我们有一个束缚电子。
``````

$${\left[ -\frac{\hbar^2}{2m_e}\nabla^2 - \frac{Ze^2}{4\pi\epsilon_0 r}\right]\psi(r,\theta,\phi) = E\psi(r,\theta,\phi)}$$

- Because of the spherical symmetry of the [Coulomb potential](http://en.wikipedia.org/wiki/Coulomb's_law), it is convenient to work in spherical coordinates:


``````{admonition} 中文翻译
:class: dropdown

- 由于[库仑势](http://en.wikipedia.org/wiki/Coulomb's_law)的球对称性，在球坐标系中工作是方便的：
``````

$$\nabla^2 = \nabla_r^2 + \frac{1}{r^2}\nabla_{\theta, \phi}^2$$

- Note that the Coulomb potential term above depends only on $r$ (and not on $\theta$ or $\phi$). The Laplacian can be written in terms of the angular momentum operator $\hat{L}$:


``````{admonition} 中文翻译
:class: dropdown

- 注意上述库仑势项仅依赖于 $r$（而非 $\theta$ 或 $\phi$）。拉普拉斯算子可以用角动量算符 $\hat{L}$ 表示：
``````

$$\nabla^2 = \nabla_r^2 - \frac{1}{r^2}\frac{\hat{L}^2}{\hbar^2}$$

- By substituting this in and multiplying both sides by $2m_e r^2$, we get:


``````{admonition} 中文翻译
:class: dropdown

- 将其代入并两边同乘 $2m_e r^2$，可得：
``````

$$\left[\frac{-\hbar^2}{2m_e}\nabla^2_r - \frac{Ze^2}{4\pi\epsilon_0 r} + \frac{\hat{L}^2}{2m_e r^2}\right]\psi_i(r,\theta,\phi) = E\psi_i(r,\theta,\phi)$$

- Since the operator can be split into $r$-dependent and angle-dependent parts, the solution can be written as a product of the radial and angular parts.


``````{admonition} 中文翻译
:class: dropdown

- 由于算符可以分离为 $r$ 相关部分和角度相关部分，解可以写成径向部分和角向部分的乘积。
``````

### Separation of variables

$${\psi_i(r,\theta,\phi) = R_{nl}(r)Y_l^m(\theta,\phi)}$$

- The $R_{nl}$ is called the **radial wavefunction**, which we need to obtain.
- The $Y_l^m$ are **spherical harmonics**, which are eigenfunctions of angular momentum $\hat{L}^2$ as discussed earlier. Hence this part is already solved.


``````{admonition} 中文翻译
:class: dropdown

- $R_{nl}$ 称为 **径向波函数**，这是我们需要求得的。
- $Y_l^m$ 是 **球谐函数**，它们是角动量算符 $\hat{L}^2$ 的本征函数，如前所述。因此这部分已经求解。
``````

$$\hat{L}^2 Y_{lm} = \hbar^2 l(l+1) Y_{lm}$$

- Plugging $R_{nl}(r)Y_l^m(\theta,\phi)$ into the Schrödinger equation, applying the angular momentum operator, and cancelling the spherical harmonics from both sides, we end up with the radial part:


``````{admonition} 中文翻译
:class: dropdown

- 将 $R_{nl}(r)Y_l^m(\theta,\phi)$ 代入薛定谔方程，应用角动量算子，并从两边消去球谐函数，我们得到径向部分：
``````

$${\left[ -\frac{\hbar^2}{2m_e}\left(\frac{\partial^2}{\partial r^2} + \frac{2}{r}\frac{\partial}{\partial r}\right) - \frac{Ze^2}{4\pi\epsilon_0 r} + \frac{l(l+1)\hbar^2}{2m_e r^2}\right] R_{nl}(r) = E_{nl}R_{nl}(r)}$$

- We find that the electron is moving in an effective potential generated by the attractive Coulomb interaction and the repulsive orbital kinetic energy.


``````{admonition} 中文翻译
:class: dropdown

- 我们发现电子在一个有效势中运动，该势由吸引性的库仑相互作用和排斥性的轨道动能产生。
``````

$$V_{eff} = - \frac{Ze^2}{4\pi\epsilon_0 r} + \frac{l(l+1)\hbar^2}{2m_e r^2}$$

- The first (repulsive) term grows more rapidly with $1/r$ than the Coulomb potential, so it dominates at small distances if $l \neq 0$. Both terms approach zero for large values of $r$. The resultant potential is repulsive at short distances for $l > 0$ and is more repulsive the greater the value of $l$. The net result of this repulsive centrifugal potential is to force electrons in orbitals with $l > 0$ on average farther from the nucleus than $l = 0$ electrons.


``````{admonition} 中文翻译
:class: dropdown

- 第一项（排斥项）随 $1/r$ 的增长速度比库仑势更快，因此在 $l \neq 0$ 时它在短距离处占主导地位。两项在 $r$ 很大时都趋近于零。对于 $l > 0$，合成势在短距离处呈排斥性，且 $l$ 值越大排斥越强。这种排斥性离心势的净效应是迫使 $l > 0$ 轨道中的电子平均比 $l = 0$ 电子离原子核更远。
``````

:::{figure} images/centrifug.png
:alt: Effective radial potential for the hydrogen atom
:width: 70%

Fig.1 Effective radial potential $V_{eff}(r)$ for the hydrogen atom. The attractive Coulomb term and the repulsive centrifugal term combine to push higher-$l$ electrons farther from the nucleus.


``````{admonition} 中文翻译
:class: dropdown

氢原子有效径向势 $V_{eff}(r)$ 的图1. 吸引的库仑项和排斥的角动量项共同作用，将更高-$l$ 的电子推得更远离原子核。
``````
:::

### Radial wavefunctions

- The radial eigenfunctions $R_{nl}$ can be written as (the derivations are lengthy but standard):


``````{admonition} 中文翻译
:class: dropdown

- 径向本征函数 $R_{nl}$ 可写为（推导过程冗长但标准）：
``````

$$R_{nl}(r) = \rho^l e^{-\rho/2}{L_{n-l-1}^{2l+1}(\rho)}$$

- **Bohr radius:** $a_0 = \frac{4\pi\epsilon_0\hbar^2}{m_e e^2}$

- **Dimensionless distance defined via the ratio to the Bohr radius:** $\rho = \frac{2Zr}{na_0}$

- **[Laguerre polynomials](http://en.wikipedia.org/wiki/Laguerre_polynomials):** $L_{n-l-1}^{2l+1}(\rho)$


``````{admonition} 中文翻译
:class: dropdown

- **玻尔半径:** $a_0 = \frac{4\pi\epsilon_0\hbar^2}{m_e e^2}$
- **通过与玻尔半径之比定义的无量纲距离：** $\rho = \frac{2Zr}{na_0}$
- **[拉格朗日多项式](http://en.wikipedia.org/wiki/Laguerre_polynomials):** $L_{n-l-1}^{2l+1}(\rho)$
``````

#### Examples of the radial wavefunctions for hydrogenlike atoms

| Orbital | $n$ | $l$ | $R_{nl}$                                                                             |
|---------|-----|-----|--------------------------------------------------------------------------------------|
| 1s      | 1   | 0   | $2\left(\frac{Z}{a_0}\right)^{3/2}e^{-\rho/2}$                                       |
| 2s      | 2   | 0   | $\frac{1}{2\sqrt{2}}\left(\frac{Z}{a_0}\right)^{3/2}(2 - \rho)e^{-\rho/2}$           |
| 2p      | 2   | 1   | $\frac{1}{2\sqrt{6}}\left(\frac{Z}{a_0}\right)^{3/2}\rho e^{-\rho/2}$                |
| 3s      | 3   | 0   | $\frac{1}{9\sqrt{3}}\left(\frac{Z}{a_0}\right)^{3/2}(6 - 6\rho - \rho^2)e^{-\rho/2}$ |
| 3p      | 3   | 1   | $\frac{1}{9\sqrt{6}}\left(\frac{Z}{a_0}\right)^{3/2}(4 - \rho)\rho e^{-\rho/2}$      |
| 3d      | 3   | 2   | $\frac{1}{9\sqrt{30}}\left(\frac{Z}{a_0}\right)^{3/2}\rho^2 e^{-\rho/2}$             |

### Full quantum solution of the H-atom

- The complete solution of the H-atom problem is provided by writing down all eigenfunctions and eigenvalues of the Hamiltonian:


``````{admonition} 中文翻译
:class: dropdown

- 氢原子问题的完整解通过写出哈密顿量的所有本征函数和本征值得到：
``````

$$
\hat{H} |n, l, m_l\rangle = E_n |n, l, m_l\rangle
$$

- We notice that while the wavefunction depends on three quantum numbers (coming from quantization of the radial and angular coordinates), the energy depends only on the principal quantum number $n$. This is another example of **energetic degeneracy** that is due to the **special spherical symmetry** of the H-atom.


``````{admonition} 中文翻译
:class: dropdown

- 我们注意到，虽然波函数依赖于三个量子数（来自径向和角度坐标的量子化），但能量仅依赖于主量子数 $n$。这是另一个 **energetic degeneracy** 的例子，其原因是 H-atom 的 **special spherical symmetry**。
``````

:::{important} **Eigenfunctions and eigenvalues of the H-atom**

$$
\hat{H} \psi_{n,l,m_l}(r,\theta,\phi) = E_n \psi_{n,l,m_l}(r,\theta,\phi)
$$

$$E_n = -\frac{m_e e^4}{8 \varepsilon_0^2 h^2} \cdot \frac{1}{n^2},
\quad n = 1, 2, 3, \ldots
$$

$${\psi_{n,l,m_l}(r,\theta,\phi) = N_{nl}\cdot R_{nl}(r)\cdot Y_{l, m_l}(\theta,\phi)}$$

- Where $N_{nl}$ is a normalization factor.
:::

:::{figure} images/Henergies.png
:alt: Energy level diagram of the hydrogen atom
:width: 70%

Fig.2 Energy levels of the hydrogen atom. All states with the same principal quantum number $n$ share the same energy, an accidental degeneracy of the Coulomb problem.


``````{admonition} 中文翻译
:class: dropdown

图2 氢原子的能量级。所有具有相同主量子数 $n$ 的态能量相同，这是库仑问题的偶然简并。
``````
:::

### Spectrum of the H atom

The equation for the hydrogen atom energy can be expressed in wavenumber units ($m^{-1}$; usually $cm^{-1}$ is used):


``````{admonition} 中文翻译
:class: dropdown

氢原子能量的方程可以用波数单位表示（$m^{-1}$；通常用 $cm^{-1}$）：
``````

$${\tilde{E}_n = \frac{E_n}{hc} = \frac{E_n}{2\pi\hbar c} = -\overbrace{\frac{m_e e^4}{4\pi c(4\pi\epsilon_0)^2\hbar^3}}^{\equiv R}
\times\frac{Z^2}{n^2}}$$

- where $R$ is the [Rydberg constant](http://en.wikipedia.org/wiki/Rydberg_constant) and we have assumed that the nucleus has infinite mass. To be exact, the Rydberg constant depends on the nuclear mass, but this difference is very small. For the H atom, $R_H = 1.096\,775\,856 \times 10^7$ $m^{-1}$.

- The H-atom energy expression can be used to calculate the differences between energy levels:


``````{admonition} 中文翻译
:class: dropdown

- 其中 $R$ 为 [瑞德伯常数](http://en.wikipedia.org/wiki/Rydberg_constant) 且已假设核质量无限大。为精确起见，瑞德伯常数依赖于核质量，但此差异极小。对于氢原子，$R_H = 1.096\,775\,856 \times 10^7$ $m^{-1}$.
- 氢原子能量表达式可用于计算能级差：
``````

$$\Delta\tilde{v}_{n_1,n_2} = \tilde{E}_{n_2} - \tilde{E}_{n_1} = -\frac{R_H Z^2}{n_2^2} + \frac{R_H Z^2}{n_1^2} = R_H Z^2\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)$$

- The [Lyman series](http://en.wikipedia.org/wiki/Lyman_series) is obtained with $n_1 = 1$, the [Balmer series](http://en.wikipedia.org/wiki/Balmer_series) with $n_1 = 2$, and the [Paschen series](http://en.wikipedia.org/wiki/Hydrogen_spectral_series) with $n_1 = 3$. The ionization energy is given by:


``````{admonition} 中文翻译
:class: dropdown

- [朗德系列](http://en.wikipedia.org/wiki/Lyman_series) 通过 $n_1 = 1$ 获得，[巴尔mer 系列](http://en.wikipedia.org/wiki/Balmer_series) 通过 $n_1 = 2$ 获得，[帕申 系列](http://en.wikipedia.org/wiki/Hydrogen_spectral_series) 通过 $n_1 = 3$ 获得。离子化能由：
``````

$${E_i = R_H Z^2\left(\frac{1}{1^2} - \frac{1}{\infty}\right)}$$

- For a ground-state hydrogen atom (i.e., $n = 1$), the above equation gives a value of $109678$ cm$^{-1}$ = $13.6057$ eV. Note that the larger the nuclear charge $Z$ is, the larger the binding energy is.


``````{admonition} 中文翻译
:class: dropdown

- 对于基态氢原子（即 $n = 1$），上式给出 $109678$ cm$^{-1}$ = $13.6057$ eV。注意核电荷 $Z$ 越大，结合能越大。
``````

:::{figure} images/Balmer.png
:alt: Balmer series of the hydrogen spectrum
:width: 70%

Fig.3 The Balmer series of the hydrogen atom: transitions ending on $n_1 = 2$ that give rise to the visible emission lines of hydrogen.


``````{admonition} 中文翻译
:class: dropdown

图3 氢原子的巴尔末系：跃迁终止于 $n_1 = 2$，产生氢原子可见发射谱线。
``````
:::

### Quantum numbers $n$, $l$, and $m$

The quantum numbers in hydrogenlike atoms take on the following values, dictated by the solution of the Schrödinger equation with boundary conditions imposed on the respective radial and angular parts.


``````{admonition} 中文翻译
:class: dropdown

氢原子类似原子的量子数由求解薛定谔方程并对各径向和角向部分施加边界条件而确定。
``````

:::{important} **Quantum numbers of the hydrogen atom**

$${n = 1, 2, 3, ...}$$
$${l = 0, 1, 2, ..., n-1}$$
$${m = 0, \pm 1, \pm 2, ..., \pm l}$$
$${m_s = \pm 1/2}$$
:::

- For historical reasons, the following letters are used to express the value of $l$:


``````{admonition} 中文翻译
:class: dropdown

- 由于历史原因，以下字母用于表示 $l$ 的值：
``````

$$l = 0, 1, 2, 3, ... \quad \Leftrightarrow \quad \text{symbol} = s, p, d, f, ...$$

- For $n = 1$ we have only one wavefunction: $R_{10}(r)Y_0^0(\theta,\phi)$. This state is usually labeled $1s$, where 1 indicates the [shell number](http://en.wikipedia.org/wiki/Electron_shell) ($n$) and $s$ corresponds to orbital angular momentum $l$ being zero.
- For $n = 2$, we have several possibilities: $l = 0$ or $l = 1$. The former is labeled $2s$. The latter is the $2p$ state and consists of three degenerate states (for example, $2p_x$, $2p_y$, $2p_z$ or $2p_{+1}$, $2p_0$, $2p_{-1}$). In the latter notation the values for $m$ are indicated as subscripts.

- There is one more quantum number that has not been discussed yet: the [spin quantum number](http://en.wikipedia.org/wiki/Spin_quantum_number), $m_s = \pm 1/2$.

- For one-electron systems this can take values $\pm\frac{1}{2}$ (discussed in more detail later). In the absence of magnetic fields the spin levels are degenerate, and therefore the total degeneracy of the levels is $2n^2$.


``````{admonition} 中文翻译
:class: dropdown

- 对于 $n = 1$，我们只有唯一的波函数：$R_{10}(r)Y_0^0(\theta,\phi)$。该态通常标记为 $1s$，其中 1 表示 [电子壳层](http://en.wikipedia.org/wiki/Electron_shell)（$n$），而 $s$ 对应于轨道角动量 $l$ 为零。
- 对于 $n = 2$，有几种可能性：$l = 0$ 或 $l = 1$。前者标记为 $2s$。后者是 $2p$ 态，由三个简并态组成（例如，$2p_x$、$2p_y$、$2p_z$ 或 $2p_{+1}$、$2p_0$、$2p_{-1}$）。在后一种标记法中，$m$ 的值作为下标表示。
- 还有一个量子数尚未讨论：[自旋量子数](http://en.wikipedia.org/wiki/Spin_quantum_number)，$m_s = \pm 1/2$。
- 对于一电子系统，此值可取 $\pm\frac{1}{2}$（稍后将详细讨论）。在没有磁场的情况下，自旋能级是退化的，因此能级的总退化度为 $2n^2$。
``````

### Table of wavefunctions in Cartesian coordinates

The full hydrogenlike wavefunctions, written in terms of $\sigma = \frac{Zr}{a_0}$:


``````{admonition} 中文翻译
:class: dropdown

完整的类氢波函数，用 $\sigma = \frac{Zr}{a_0}$ 表示为：
``````

| $n$ | $l$ | $m$     | Wavefunction expressed in $\sigma = \frac{Zr}{a_0}$                                                                                                                          |
|-----|-----|---------|------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | 0   | 0       | $\psi_{1s} = \frac{1}{\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}e^{-\sigma}$                                                            |
| 2   | 0   | 0       | $\psi_{2s} = \frac{1}{4\sqrt{2\pi}}\left(\frac{Z}{a_0}\right)^{3/2}(2 - \sigma)e^{-\sigma/2}$                                            |
| 2   | 1   | 0       | $\psi_{2p_z} = \frac{1}{4\sqrt{2\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\sigma e^{-\sigma/2}\cos(\theta)$                        |
| 2   | 1   | $\pm 1$ | $\psi_{2p_x} = \frac{1}{4\sqrt{2\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\sigma e^{-\sigma/2}\sin(\theta)\cos(\phi)$ |
|     |     |         | $\psi_{2p_y} = \frac{1}{4\sqrt{2\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\sigma e^{-\sigma/2}\sin(\theta)\sin(\phi)$ |
| 3   | 0   | 0       | $\psi_{3s} = \frac{1}{81\sqrt{3\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\left(27 - 18\sigma + 2\sigma^2\right)e^{-\sigma/3}$                                                      |
| 3   | 1   | 0       | $\psi_{3p_z} = \frac{\sqrt{2}}{81\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\left(6 - \sigma\right)\sigma e^{-\sigma/3}\cos(\theta)$                               |
| 3   | 1   | $\pm 1$ | $\psi_{3p_x} = \frac{\sqrt{2}}{81\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\left(6 - \sigma\right)\sigma e^{-\sigma/3}\sin(\theta)\cos(\phi)$       |
|     |     |         | $\psi_{3p_y} = \frac{\sqrt{2}}{81\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\left(6 - \sigma\right)\sigma e^{-\sigma/3}\sin(\theta)\sin(\phi)$                                                                 |
| 3   | 2   | 0       | $\psi_{3d_{z^2}} = \frac{1}{81\sqrt{6\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\sigma^2 e^{-\sigma/3}\left(3\cos^2(\theta) - 1\right)$                                  |
| 3   | 2   | $\pm 1$ | $\psi_{3d_{xz}} = \frac{\sqrt{2}}{81\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\sigma^2 e^{-\sigma/3}\sin(\theta)\cos(\theta)\cos(\phi)$ |
|     |     |         | $\psi_{3d_{yz}} = \frac{\sqrt{2}}{81\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\sigma^2 e^{-\sigma/3}\sin(\theta)\cos(\theta)\sin(\phi)$                                                                                     |
| 3   | 2   | $\pm 2$ | $\psi_{3d_{x^2-y^2}} = \frac{1}{81\sqrt{3\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\sigma^2 e^{-\sigma/3}\sin^2(\theta)\cos(2\phi)$                       |
|     |     |         | $\psi_{3d_{xy}} = \frac{1}{81\sqrt{3\pi}}\left(\frac{Z}{a_0}\right)^{3/2}\sigma^2 e^{-\sigma/3}\sin^2(\theta)\sin(2\phi)$                                                                                             |

### Computing with wavefunctions

- We can use the wavefunctions from the table above to calculate various averages by using the definition of an average in quantum mechanics, $\langle f(r) \rangle = \langle \psi |f(r)|\psi\rangle$:


``````{admonition} 中文翻译
:class: dropdown

- 我们可以使用上表中的波函数，通过量子力学中平均值的定义来计算各种平均值，$\langle f(r) \rangle = \langle \psi |f(r)|\psi\rangle$：
``````

$$
\langle r\rangle_{n,l,m} = \frac{a_0 n^2}{Z}\left( 1 + \frac{1}{2}\left[1 - \frac{l(l+1)}{n^2}\right]\right)
$$

$$
\langle r^2\rangle_{n,l,m} = \frac{a_0^2 n^4}{Z^2}\left( 1 + \frac{3}{2}\left[1 - \frac{l(l+1) - 1/3}{n^2}\right]\right)
$$

$$
\langle r^{-1}\rangle_{n,l,m} = \frac{Z}{a_0 n^2}
$$

$$
\langle r^{-2}\rangle_{n,l,m} = \frac{Z^2}{a_0^2 n^3 (l+1/2)}
$$

$$
\langle r^{-3}\rangle_{n,l,m} = \frac{Z^3}{a_0^3 n^3 (l+1/2)(l+1)}
$$

```{marimo-config}
---
pyproject: |
  requires-python = ">=3.10"
  dependencies = [
      "numpy",
      "scipy",
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
from scipy.special import genlaguerre, factorial
```

```{marimo} python
:hide-code: true

def radial_m(r, n=1, l=0):
    pre = np.sqrt(((2 / n) ** 3 * factorial(n - l - 1)) / (2 * n * factorial(n + l)))
    p = 2 * r / n
    return pre * np.exp(-p / 2) * p**l * genlaguerre(n - l - 1, 2 * l + 1)(p)
```

```{marimo} python
:hide-code: true

n_r = mo.ui.slider(1, 6, step=1, value=2, show_value=True, label="n")
n_r
```

```{marimo} python
:hide-code: true

l_r = mo.ui.dropdown(
    options={str(v): v for v in range(n_r.value)}, value="0", label="l"
)
l_r
```

```{marimo} python
:hide-code: true

l_eff = l_r.value
r_g = np.linspace(1e-6, 12 * n_r.value, 900)
R_g = radial_m(r_g, n_r.value, l_eff)

fig_r, (ax_R, ax_P) = plt.subplots(figsize=(9, 3.6), ncols=2)
ax_R.plot(r_g, R_g, lw=2)
ax_R.axhline(0, color="0.8", lw=0.8)
ax_R.set_xlabel("r (Bohr)")
ax_R.set_title(f"radial function R({n_r.value},{l_eff})", fontsize=11)
ax_P.plot(r_g, r_g**2 * R_g**2, lw=2, color="seagreen")
ax_P.set_xlabel("r (Bohr)")
ax_P.set_title("radial probability r^2 R^2", fontsize=11)
fig_r.tight_layout()
fig_r
```

