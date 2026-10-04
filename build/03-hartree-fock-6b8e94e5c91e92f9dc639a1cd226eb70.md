---
kernelspec:
  name: python3
  display_name: Python 3
---

# The Hartree-Fock Method

:::{note} **What you will learn**

- The Schrodinger equation for multi-electron systems cannot be solved exactly because of the electron, electron interaction.
- The **Hartree-Fock** method provides an approximate approach by treating each electron as moving in the **average (mean-field) potential** created by all the others.
- Antisymmetry of the total wavefunction is enforced using a **Slater determinant**, which introduces the **exchange interaction**, a purely quantum effect with no classical analogue.
- The solution is obtained **self-consistently**: the orbitals define the mean field, and the mean field determines the orbitals. This is the **SCF** procedure.
- Hartree-Fock captures exchange exactly but misses **dynamic correlation**, motivating post-Hartree-Fock methods.


``````{admonition} 中文翻译
:class: dropdown

- 多电子系统的薛定谔方程因电子-电子相互作用而无法精确求解。
- **Hartree-Fock** 方法通过将每个电子视为在所有其他电子产生的**平均（平均场）势**中运动，提供了一种近似方法。
- 使用 **Slater 确定性** 来强制总波函数的反对称性，这引入了 **交换相互作用**，这是一种纯量子效应，没有经典类比。
- 解是**自洽**获得的：轨道定义平均场，而平均场决定轨道。这就是**SCF**过程。
- Hartree-Fock 精确处理了交换，但遗漏了**动态相关**，这促使了后 Hartree-Fock 方法的发展。
``````
:::

## The Wavefunction

The total wavefunction $\Psi(1, 2, \ldots, N)$ is approximated as a single Slater determinant so that it satisfies the Pauli exclusion principle automatically:


``````{admonition} 中文翻译
:class: dropdown

总波函数 $\Psi(1, 2, \ldots, N)$ 近似为单个斯莱特行列式，从而自动满足泡利不相容原理：
``````

:::{important} **Slater determinant ansatz**

$$
\Psi(1, 2, \ldots, N) = \frac{1}{\sqrt{N!}}
\begin{vmatrix}
\psi_1(1) & \psi_2(1) & \cdots & \psi_N(1) \\
\psi_1(2) & \psi_2(2) & \cdots & \psi_N(2) \\
\vdots & \vdots & \ddots & \vdots \\
\psi_1(N) & \psi_2(N) & \cdots & \psi_N(N)
\end{vmatrix}
$$

:::

## The Hartree-Fock Equations

Each molecular orbital (MO) $\psi_i$ satisfies the self-consistent field (SCF) equation:


``````{admonition} 中文翻译
:class: dropdown

每个分子轨道 (MO) $\psi_i$ 都满足自洽场 (SCF) 方程：
``````

:::{important} **Hartree-Fock equation**

$$
\hat{F} \psi_i = \varepsilon_i \psi_i
$$

where $\hat{F}$ is the **Fock operator** and $\varepsilon_i$ are the orbital energies.


``````{admonition} 中文翻译
:class: dropdown

其中 $\hat{F}$ 是 **Fock 算符**，$\varepsilon_i$ 是轨道能量。
``````
:::

### The Fock Operator

The Fock operator $\hat{F}$ is the sum of the one-electron Hamiltonian and a mean-field potential:


``````{admonition} 中文翻译
:class: dropdown

Fock 算符 $\hat{F}$ 是单电子哈密顿量与平均场势之和：
``````

$$
\hat{F} = \hat{h} + \sum_{j} \left( \hat{J}_j - \hat{K}_j \right)
$$

- $\hat{h}$ contains the kinetic energy and nuclear attraction operators.
- $\hat{J}_j$ is the Coulomb operator (electron, electron repulsion).
- $\hat{K}_j$ is the exchange operator, which arises from the antisymmetry requirement of the wavefunction and has no classical analogue.


``````{admonition} 中文翻译
:class: dropdown

- $\hat{h}$ 包含动能算符和核吸引算符。
- $\hat{J}_j$ 是库仑算符（电子-电子排斥）。
- $\hat{K}_j$ 是交换算符，它源于波函数的反对称性要求，且没有经典对应物。
``````

## The Self-Consistent Field (SCF) Procedure

The Fock operator depends on the orbitals it is meant to determine, so the equations must be solved iteratively:


``````{admonition} 中文翻译
:class: dropdown

Fock 算符依赖于它要确定的轨道，因此这些方程必须迭代求解：
``````

1. **Guess** an initial set of molecular orbitals $\psi_i$.
2. **Construct** the Fock operator $\hat{F}$ using the current $\psi_i$.
3. **Solve** the Hartree-Fock equation $\hat{F}\psi_i = \varepsilon_i\psi_i$ to obtain new orbitals $\psi_i$.
4. **Repeat** steps 2 and 3 until convergence, that is, until the orbitals no longer change significantly.


``````{admonition} 中文翻译
:class: dropdown

- **猜测** 一组初始分子轨道 $\psi_i$。
- **构建** 福克算符 $\hat{F}$，使用当前的 $\psi_i$。
- **求解**哈特里-福克方程 $\hat{F}\psi_i = \varepsilon_i\psi_i$ 以获得新轨道 $\psi_i$。
- **重复** 步骤 2 和 3 直到收敛，即轨道不再显著变化。
``````

:::{figure} images/HF_iter.png
:alt: SCF iteration loop
:width: 500px

Fig. 1 The self-consistent field cycle. The orbitals define the mean field through the Fock operator, and solving the Fock equation produces updated orbitals; the loop repeats until self-consistency.


``````{admonition} 中文翻译
:class: dropdown

自洽场循环。轨道通过费克算子定义平均场，求解费克方程得到更新的轨道；循环反复进行，直到自洽。
``````
:::

## Total Energy of the System

The total electronic energy $E_{HF}$ in the Hartree-Fock approximation is:


``````{admonition} 中文翻译
:class: dropdown

哈特里-福克近似中的总电子能量 $E_{HF}$ 为：
``````

:::{important} **Hartree-Fock energy**

$$
E_{HF} = \sum_{i} \langle \psi_i | \hat{h} | \psi_i \rangle + \frac{1}{2} \sum_{i,j} \left( J_{ij} - K_{ij} \right)
$$

- $J_{ij}$ is the Coulomb integral.
- $K_{ij}$ is the exchange integral.
- The factor $\tfrac{1}{2}$ corrects for double counting of the electron, electron interaction.


``````{admonition} 中文翻译
:class: dropdown

- $J_{ij}$ is the Coulomb integral.
- $K_{ij}$ 是交换积分。
- 因子 $\tfrac{1}{2}$ 用于修正电子-电子相互作用的重复计数。
``````
:::

## Hartree-Fock for the Helium Atom

Helium is the simplest closed-shell atom on which to see the method work. Each $1s$ electron moves in an effective potential, the bare nuclear attraction plus the mean field of the other electron.


``````{admonition} 中文翻译
:class: dropdown

氦是最简单的闭壳层原子，可用于观察该方法的运作。每个 $1s$ 电子在有效势中运动，该势包括裸核吸引和其他电子的平均场。
``````

:::{figure} images/HF_He.png
:alt: Hartree-Fock applied to helium
:width: 500px

Fig. 2 Hartree-Fock applied to the helium atom: each electron is treated as moving in the average field of the other.


``````{admonition} 中文翻译
:class: dropdown

图 2 应用于氦原子的 Hartree-Fock 方法：每个电子被视为在另一个电子的平均场中运动。
``````
:::

:::{figure} images/V_eff.png
:alt: Effective potential seen by an electron
:width: 500px

Fig. 3 The effective (mean-field) potential felt by one electron is the nuclear attraction screened by the averaged charge cloud of the other electron.


``````{admonition} 中文翻译
:class: dropdown

图 3 一个电子感受到的有效（平均场）势是被另一个电子的平均电荷云屏蔽后的核吸引势。
``````
:::

:::{figure} images/HF_slater.png
:alt: Slater determinant for helium
:width: 500px

Fig. 4 The antisymmetrized helium wavefunction written as a Slater determinant of spin-orbitals.


``````{admonition} 中文翻译
:class: dropdown

图 4 以斯莱特行列式形式写出的反对称化氦波函数（自旋轨道）。
``````
:::

:::{figure} images/HF_orb_e.png
:alt: Hartree-Fock orbital energies
:width: 500px

Fig. 5 Orbital energies obtained from the converged Hartree-Fock calculation.


``````{admonition} 中文翻译
:class: dropdown

图 5 收敛 Hartree-Fock 计算得到的轨道能量。
``````
:::

## Strengths and Limitations

**Strengths**

- **Efficient.** It reduces the intractable multi-electron Schrodinger equation to a set of coupled one-electron equations.
- **Exchange interactions.** It includes the effects of exchange exactly through the Slater determinant.


``````{admonition} 中文翻译
:class: dropdown

- **高效。** 它将难以处理的多电子薛定谔方程简化为一组耦合的一电子方程。
- **交换相互作用。** 它通过斯莱特行列式精确地包含了交换效应。
``````

**Limitations**

- **No dynamic correlation.** Electron, electron correlation is only partially captured, because each electron sees only the *average* field of the others, not their instantaneous positions.
- **Post-Hartree-Fock methods.** More accurate energies require methods such as MP2 or CCSD that add correlation on top of the Hartree-Fock reference.


``````{admonition} 中文翻译
:class: dropdown

- **无动态相关。** 电子间的相关作用仅部分捕获，因为每个电子只感知到其他电子的*平均*场，而非它们的瞬时位置。
- **后哈特里-福克方法。** 更精确的能量需要诸如 MP2 或 CCSD 等方法，它们在哈特里-福克参考态的基础上加入了相关性。
``````

:::{tip} **Hartree-Fock in one sentence**

Hartree-Fock replaces the impossible many-body problem with a self-consistent set of one-electron problems in which each electron moves in the averaged field of all the others, capturing exchange exactly but correlation only on average. The companion demo notebook runs an actual Hartree-Fock calculation with PySCF.


``````{admonition} 中文翻译
:class: dropdown

哈密顿-福克将不可能的许多体问题替换为一组自洽的单电子问题，其中每个电子都在其他所有电子的平均场中运动，精确捕捉交换但仅在平均水平上捕捉相关性。同伴演示笔记本使用 PySCF 运行实际的哈密顿-福克计算。
``````
:::
