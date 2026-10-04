---
kernelspec:
  name: python3
  display_name: Python 3
---

# Molecular Orbital Description of the Hydrogen Molecule

:::{note} **What you will learn**

- The neutral $H_2$ molecule has two electrons, which introduces an electron-electron repulsion term $1/r_{12}$ that makes the electronic Schrodinger equation analytically unsolvable.
- We build the ground state of $H_2$ by placing two electrons of opposite spin in the bonding $1\sigma_g$ orbital, writing the total wavefunction as an antisymmetric **Slater determinant**.
- The simple LCAO-MO wavefunction already predicts a bound molecule, though it overestimates the bond length and underestimates the binding energy.
- Accuracy is systematically improved by separating **ionic and covalent contributions** and ultimately by configuration interaction, which reaches essentially exact agreement with experiment.


``````{admonition} 中文翻译
:class: dropdown

- 中性 $H_2$ 分子有两个电子，这引入了电子-电子排斥项 $1/r_{12}$，使得电子薛定谔方程无法解析地求解。
- 通过将两个自旋相反的电子放入结合的 $1\sigma_g$ 轨道来构建 $H_2$ 的基态，写出总波函数为反对称 **Slater 确定式**。
- 简单的 LCAO-MO 波函数已经预测出了束缚分子，尽管它高估了键长并低估了结合能。
- 精度通过分离**离子和共价贡献**，最终通过构型相互作用得到，后者与实验结果基本精确一致。
``````
:::

### Setting up the Hamiltonian

:::{figure} images/H2mol-fig1.png
:alt: Coordinates of the hydrogen molecule
:width: 400px

Fig. 1 Coordinates used to describe the two electrons and two nuclei of the $H_2$ molecule.


``````{admonition} 中文翻译
:class: dropdown

图 1 描述 $H_2$ 分子两个电子和两个核的坐标。
``````
:::

$${H = -\frac{\hbar^2}{2m_e}\left( \Delta_1 + \Delta_2\right)
+ \frac{e^2}{4\pi\epsilon_0}\left(\frac{1}{R} + \frac{1}{r_{12}} - \frac{1}{r_{A1}} 
- \frac{1}{r_{A2}} - \frac{1}{r_{B1}} - \frac{1}{r_{B2}}\right)}$$

- The main difficulty in the molecular Hamiltonian is the $1/r_{12}$ term, which couples the two electrons to each other. This means that a simple product wavefunction is not sufficient. No analytic solution has been found for the electronic Schrodinger equation of $H_2$.
- For this reason, we solve the problem approximately by using the LCAO-MO approach used previously. For example, the ground state for $H_2$ is obtained by placing two electrons with opposite spins in the $1\sigma_g$ orbital. This assumes that the wavefunction is expressed as an antisymmetrized product (a Slater determinant).


``````{admonition} 中文翻译
:class: dropdown

- 分子哈密顿量的主要难点是 $1/r_{12}$ 项，该项耦合了两个电子。这意味着简单的乘积波函数是不够的。$H_2$ 的电子薛定谔方程尚未找到解析解。
- 因此，我们通过先前使用的 LCAO-MO 方法近似求解此问题。例如，$H_2$ 的基态是通过将两个自旋相反的电子置于 $1\sigma_g$ 轨道获得的。这假设波函数表示为反对称乘积（一个 Slater 确定子）。
``````

### Constructing MOs for the hydrogen molecule

- According to the Pauli principle, two electrons with opposite spins can be assigned to a given spatial orbital. As a first approximation, we assume that the molecular orbitals in $H_2$ remain the same as in $H_2^+$. Hence both electrons occupy the $1\sigma_g$ orbital (the ground state) and the electronic configuration is denoted ($1\sigma_g)^2$. This is similar to the notation used previously for atoms (for example, the He atom is ($1s)^2$).

- The molecular orbital for electron 1 in the $1\sigma_g$ molecular orbital is:


``````{admonition} 中文翻译
:class: dropdown

- 根据Pauli原理，具有相反自旋的两个电子可以被分配到同一个空间轨道。作为第一近似，我们假设 $H_2$ 中的分子轨道保持 $H_2^+$ 不变。因此两个电子都占据 $1\sigma_g$ 轨道（基态），电子构型记为 ($1\sigma_g)^2$。这类似于此前用于原子的记法（例如，He 原子记为 ($1s)^2$）。
- 电子 1 在 $1\sigma_g$ 分子轨道中的分子轨道为：
``````

$${1\sigma_g(1) = \frac{1}{\sqrt{2(1 + S)}}(1s_A(1) + 1s_B(1))}$$

- Previously we found that the total wavefunction must be antisymmetric with respect to exchange of electron indices. This can be achieved by using the Slater determinant:


``````{admonition} 中文翻译
:class: dropdown

- 此前我们发现，总波函数必须在电子索引交换下反对称。可以通过使用斯莱特行列式来实现：
``````

:::{important} **Slater determinant for the $H_2$ ground state**

$${\psi_{MO}^{(1\sigma_g)^2} = \frac{1}{\sqrt{2}}\begin{vmatrix}
1\sigma_g(1)\alpha (1) & 1\sigma_g(1)\beta (1)\\
1\sigma_g(2)\alpha (2) & 1\sigma_g(2)\beta (2)\\
\end{vmatrix}}$$
:::

- where $\alpha$ and $\beta$ denote the electron spin. The Slater determinant can be expanded as follows:


``````{admonition} 中文翻译
:class: dropdown

- 其中 $\alpha$ 和 $\beta$ 表示电子自旋。Slater 行列式可以展开如下：
``````

$${\psi_{MO}^{(1\sigma_g)^2} = \frac{1}{\sqrt{2}} 
 (1\sigma_g(1)1\sigma_g(2)\alpha (1)\beta (2) 
- 1\sigma_g(1)1\sigma_g(2)\beta (1)\alpha (2))}$$

$${= \frac{1}{2\sqrt{2}(1 + S_{AB})}(1s_A(1) + 1s_B(1))(1s_A(2) + 1s_B(2))
(\alpha (1)\beta (2) - \alpha (2)\beta (1))}$$

- Note that this wavefunction is only approximate and is definitely not an eigenfunction of the $H_2$ electronic Hamiltonian. Thus we must calculate the electronic energy by taking the expectation value of this wavefunction with the Hamiltonian (the actual calculation is not shown):


``````{admonition} 中文翻译
:class: dropdown

- 注意，此波函数仅近似，绝对不是 $H_2$ 电子哈密顿量的本征函数。因此，必须通过取此波函数关于哈密顿量的期望值来计算电子能量（具体计算不展示）：
``````

$${E(R) = 2E_{1s} + \frac{e^2}{4\pi\epsilon_0 R} 
- \textnormal{integrals}}$$

- where $E_{1s}$ is the electronic energy of one hydrogen atom. The second term represents the Coulomb repulsion between the two positively charged nuclei, and the last term ("integrals") contains a series of integrals describing the interactions of various charge distributions with one another (see P. W. Atkins, Molecular Quantum Mechanics, Oxford University Press). With this approach, the minimum energy is reached at $R$ = 84 pm (experimental 74.1 pm) with a dissociation energy $D_e$ = 255 kJ mol$^{-1}$ (experimental 458 kJ mol$^{-1}$).


``````{admonition} 中文翻译
:class: dropdown

- 其中 $E_{1s}$ 为氢原子的电子能。第二项表示两个带正电核之间的库仑排斥，最后一项（“积分”）包含一系列描述各种电荷分布相互作用的积分（参见 P. W. Atkins, Molecular Quantum Mechanics, Oxford University Press）。使用此方法，最小能量在 $R$ = 84 pm 处达到（实验值 74.1 pm），解离能 $D_e$ = 255 kJ mol$^{-1}$（实验值 458 kJ mol$^{-1}$）。
``````

### Improving upon the simple MO approximation

:::{figure} images/H2mol-fig2.png
:alt: Improving the hydrogen molecule wavefunction
:width: 600px

Fig. 2 Improving the $H_2$ wavefunction by treating ionic and covalent contributions separately lowers the energy and shortens the predicted bond length toward experiment.


``````{admonition} 中文翻译
:class: dropdown

图2 通过分别处理离子和共价贡献来改进 $H_2$ 波函数，可以降低能量并将预测的键长收敛到实验值。
``````
:::

- This simple approach is not very accurate, but it demonstrates that the method works. To improve the accuracy, ionic and covalent terms should be considered separately:


``````{admonition} 中文翻译
:class: dropdown

- 这种简单的方法不够精确，但它证明了该方法是有效的。为了提高精度，应分别考虑离子项和共价项：
``````

$${\underbrace{1s_A(1)1s_A(2)}_{\textnormal{Ionic (H}^- \textnormal{ + H}^+)}
+ \underbrace{[1s_A(1)1s_B(2) + 1s_A(2)1s_B(1)]}_{\textnormal{Covalent (H + H)}}
+ \underbrace{1s_B(1)1s_B(2)}_{\textnormal{Ionic (H}^+ \textnormal{ + H}^-)}}$$

Both covalent and ionic terms can be introduced into the wavefunction with their own variational parameters $c_1$ and $c_2$:


``````{admonition} 中文翻译
:class: dropdown

共价项和离子项都可以引入波函数，并带有各自的变分参数 $c_1$ 和 $c_2$：
``````

$${\psi = c_1\psi_{\textnormal{covalent}} + c_2\psi_{\textnormal{ionic}}}$$

$${\psi_{\textnormal{covalent}} = 1s_A(1)1s_B(2) + 1s_A(2)1s_B(1)}$$

$${\psi_{\textnormal{ionic}} = 1s_A(1)1s_A(2) + 1s_B(1)1s_B(2)}$$

- Note that the variational constants $c_1$ and $c_2$ depend on the internuclear distance $R$. Minimization of the energy expectation value with respect to these constants gives $R_e$ = 74.9 pm (experiment 74.1 pm) and $D_e$ = 386 kJ mol$^{-1}$ (experiment 458 kJ mol$^{-1}$).

- Further improvement can be achieved by adding higher atomic orbitals to the wavefunction. The previously discussed Hartree-Fock method provides an efficient way of solving the problem. Recall that this method is only approximate, as it ignores electron-electron correlation effects completely. The full treatment requires configuration interaction methods, which can yield essentially exact results: $D_e$ = 36117.8 cm$^{-1}$ (CI) versus $36117.3\pm1.0$ cm$^{-1}$ (experiment), and $R_e$ = 74.140 pm versus 74.139 pm (experiment).

``````{admonition} 中文翻译
:class: dropdown

- 注意变分常数 $c_1$ 和 $c_2$ 取决于核间距离 $R$。对这些常数对能量期望值进行最小化得到 $R_e$ = 74.9 pm（实验 74.1 pm）和 $D_e$ = 386 kJ mol$^{-1}$（实验 458 kJ mol$^{-1}$）。
- 通过向波函数中添加更高的原子轨道可以进一步改进结果。前面讨论的 Hartree-Fock 方法提供了一种高效的求解途径。回顾一下，该方法只是近似的，因为它完全忽略了电子-电子相关效应。完整的处理需要组态相互作用方法，它能给出基本精确的结果：$D_e$ = 36117.8 cm$^{-1}$ (CI) 对比 $36117.3\pm1.0$ cm$^{-1}$ (实验)，以及 $R_e$ = 74.140 pm 对比 74.139 pm (实验)。
``````

