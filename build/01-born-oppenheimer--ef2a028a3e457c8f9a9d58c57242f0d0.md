---
kernelspec:
  name: python3
  display_name: Python 3
---

# The Born-Oppenheimer Approximation

:::{note} **What you will learn**

- **The Born-Oppenheimer (BO) approximation.** Because nuclei are much heavier than electrons, the Schrodinger equation can be approximately separated into a nuclear part and an electronic part. The electronic Schrodinger equation for a molecule can then be solved at each fixed nuclear configuration.
- **From atoms to molecules.** The BO approximation lets us extend the multi-electron treatment of atoms to molecules.
- **Molecular orbitals (MOs).** Single-electron wavefunctions of molecules are called molecular orbitals.
- **Nuclear geometry as a parameter.** The geometry of a molecule, for example the bond length $R$ of $H_2$, is held fixed when determining the molecular orbitals. For different values of $R$ one obtains different energies and different MOs.


``````{admonition} 中文翻译
:class: dropdown

- **Born-Oppenheimer (BO) 近似.** 因为原子核比电子重得多，Schrödinger 方程可以近似分离为核部分和电子部分。然后可以在每个固定的核构型下求解分子的电子 Schrödinger 方程。
- **从原子到分子。** 玻恩-奥本海默近似让我们能将原子的多电子处理扩展到分子。
- **分子轨道 (MOs)。** 分子的单电子波函数称为分子轨道。
- **核几何作为参数。** 分子的几何结构，例如 $H_2$ 的键长 $R$，在确定分子轨道时保持固定。对于不同的 $R$ 值，得到不同的能量和不同的轨道。
``````
:::

### The simplest molecule

:::{figure} ./images/h2plus_mol.png
:alt: Coordinates of the hydrogen molecule ion
:width: 300px

Fig. 1 Coordinates used to describe the $H_2^+$ molecule.


``````{admonition} 中文翻译
:class: dropdown

图 1 描述 $H_2^+$ 分子所用的坐标。
``````
:::

In the following, we will consider the simplest molecule $H_2^+$, which contains only one electron. This simple system demonstrates the basic concepts of chemical bonding. The Schrodinger equation for $H_2^+$ is:


``````{admonition} 中文翻译
:class: dropdown

在下面，我们将考虑最简单的分子 $H_2^+$，它只包含一个电子。这个简单的系统展示了化学键合的基本概念。$H_2^+$ 的薛定谔方程为：
``````

$${H\psi(\vec{r}_1,\vec{R}_A,\vec{R}_B) = E\psi(\vec{r}_1,\vec{R}_A,\vec{R}_B)}$$

where $\vec{r}_1$ is the vector locating the (only) electron and $\vec{R}_A$ and $\vec{R}_B$ are the positions of the two protons. The Hamiltonian for $H_2^+$ is:


``````{admonition} 中文翻译
:class: dropdown

其中 $\vec{r}_1$ 是（唯一）电子的位置矢量，而 $\vec{R}_A$ 和 $\vec{R}_B$ 是两个质子的位置。$H_2^+$ 的哈密顿量为：
``````

$${\hat{H} = -\frac{\hbar^2}{2M}(\Delta_A + \Delta_B) - \frac{\hbar^2}{2m_e}\Delta_e+ \frac{e^2}{4\pi\epsilon_0}\left(\frac{1}{R} - \frac{1}{r_{1A}} - \frac{1}{r_{1B}}\right)}$$

where $M$ is the proton mass, $m_e$ is the electron mass, $r_{1A}$ is the distance between the electron and nucleus A, $r_{1B}$ is the distance between the electron and nucleus B, and $R$ is the A to B distance.


``````{admonition} 中文翻译
:class: dropdown

其中 $M$ 是质子质量，$m_e$ 是电子质量，$r_{1A}$ 是电子与A核之间的距离，$r_{1B}$ 是电子与B核之间的距离，$R$ 是A到B的距离。
``````

Note that the Hamiltonian also includes the quantum mechanical kinetic energy of the protons. As such, the wavefunction depends on $\vec{r}_1$, $\vec{R}_A$, and $\vec{R}_B$.


``````{admonition} 中文翻译
:class: dropdown

请注意，哈密顿量也包括质子的量子动能。因此，波函数依赖于 $\vec{r}_1$，$\vec{R}_A$，和 $\vec{R}_B$。
``````

### The Born-Oppenheimer approximation

:::{figure} ./images/Born.jpg
:alt: Max Born
:width: 200px

Fig. 2 Max Born.
:::

:::{figure} ./images/BO.jpeg
:alt: Robert J. Oppenheimer
:width: 200px

Fig. 3 Robert J. Oppenheimer.
:::

Because the nuclear mass $M$ is much larger than the electron mass $m_e$, the wavefunction can be separated (the Born-Oppenheimer approximation):


``````{admonition} 中文翻译
:class: dropdown

因为核质量 $M$ 远大于电子质量 $m_e$，波函数可以分离（玻恩-奥本海默近似）：
``````

$${\psi(\vec{r}_1,\vec{R}_A,\vec{R}_B) = \psi_e(\vec{r}_1, R)\psi_n(\vec{R}_A, \vec{R}_B)}$$

where $\psi_e$ is the electronic wavefunction that depends on the distance $R$ between the nuclei and $\psi_n$ is the nuclear wavefunction depending on $\vec{R}_A$ and $\vec{R}_B$. It can be shown that the nuclear part can often be further separated into vibrational, rotational, and translational parts. The electronic Schrodinger equation can now be written as:


``````{admonition} 中文翻译
:class: dropdown

其中 $\psi_e$ 是依赖于核间距离 $R$ 的电子波函数，$\psi_n$ 是依赖于 $\vec{R}_A$ 和 $\vec{R}_B$ 的核波函数。可以证明，核部分通常可以进一步分解为振动、旋转和平动部分。电子薛定谔方程现在可以写成：
``````

:::{important} **The electronic Schrodinger equation**

$${\hat{H}_e\psi_e = E_e\psi_e}$$

$${\hat{H}_e = -\frac{\hbar^2}{2m_e}\Delta_e + \frac{e^2}{4\pi\epsilon_0}
\left(\frac{1}{R} - \frac{1}{|r_1 - R_A|} - \frac{1}{|r_1 - R_B|}\right)}$$

This equation depends parametrically on $R$: there is one equation for each value of $R$.


``````{admonition} 中文翻译
:class: dropdown

该方程在参数上依赖于 $R$：每个 $R$ 值对应一个方程。
``````
:::

Because $R$ is a parameter, both $E_e$ and $\psi_e$ are functions of $R$. Solving the electronic problem at a sequence of fixed nuclear geometries traces out the potential energy surface on which the nuclei move, which is the central idea that makes molecular electronic structure tractable.

``````{admonition} 中文翻译
:class: dropdown

因为 $R$ 是一个参数，所以 $E_e$ 和 $\psi_e$ 都依赖于 $R$。在一系列固定核几何构型下求解电子问题，勾勒出核运动的势能面，这是使分子电子结构可处理的核心思想。
``````

