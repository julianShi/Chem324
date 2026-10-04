---
kernelspec:
  name: python3
  display_name: Python 3
---

# The Hydrogen Molecule Ion

:::{note} **What you will learn**

- We can construct an approximate trial wavefunction for a molecule using atomic orbitals to gain intuition about chemical bonding.
- Applying the variational method leads to two molecular orbitals (MOs) with distinct spatial character: one increases the electron probability density between the nuclei **(bonding)**, while the other decreases it **(antibonding)**.
- These **bonding and antibonding MOs** respectively lower and raise the energy of the molecule relative to two separated atoms.
- More accurate quantum chemical methods do not rely directly on atomic orbitals, but instead use abstract linear combinations of **Gaussian basis sets** to represent molecular orbitals.


``````{admonition} 中文翻译
:class: dropdown

- 我们可以利用原子轨道构建分子的近似试验波函数，以获得对化学键合的直观理解。
- 应用变分法得到两个分子轨道（MOs），它们具有不同的空间特征：一个增加核之间电子概率密度（**结合**），而另一个减少它（**反结合**）。
- 这些 **成键和反成键分子轨道** 分别降低和升高了分子相对于两个分离原子的能量。
- 更准确的量子化学方法不直接依赖原子轨道，而是使用 **Gaussian basis sets**（高斯基组）的抽象线性组合来表示分子轨道。
``````
:::

### Constructing MOs from AOs

:::{figure} ./images/Starting_aos.png
:alt: 1s atomic orbitals centered on each hydrogen atom
:width: 400px

Fig. 1 The 1s atomic orbitals centered on each H atom in the $H_2^+$ molecule.


``````{admonition} 中文翻译
:class: dropdown

图 1 $H_2^+$ 分子中以每个 H 原子为中心的 1s 原子轨道。
``````
:::

The electronic Schrodinger equation for $H_2^+$ can be solved exactly because the system contains only a single electron. However, the analytical solution involves quite challenging mathematics. Instead, we adopt a simpler approximate approach that still captures the essential physics of chemical bonding.


``````{admonition} 中文翻译
:class: dropdown

单电子系统 $H_2^+$ 的电子薛定谔方程可以精确求解，因为系统中只有一个电子。然而，解析解涉及相当棘手的数学。相反，我们采用一个更简单的近似方法，该方法仍然捕捉化学键合的本质物理。
``````

We construct a trial (approximate) molecular wavefunction as a real linear combination of hydrogen 1s atomic orbitals:


``````{admonition} 中文翻译
:class: dropdown

我们将试探（近似）分子波函数构造为氢原子 1s 原子轨道的实线性组合：
``````

$$
\psi_{\pm}(\vec{r}_1) = c_1\,1s_A(\vec{r}_1) \; \pm \; c_2\,1s_B(\vec{r}_1)
$$

- Here, $1s_A$ and $1s_B$ are hydrogen 1s orbitals centered on nuclei A and B, respectively, and $c_1$ and $c_2$ are coefficients (constants).
- This form is known as the **Linear Combination of Atomic Orbitals (LCAO)** approximation for constructing molecular orbitals.
- Because the two nuclei are identical, symmetry requires $c_1 = c_2 \equiv c$ (and we choose $c > 0$).

- The $\pm$ sign indicates that two distinct molecular orbitals can be formed:
    - the **bonding** combination ($+$), which enhances electron density between the nuclei
    - the **antibonding** combination ($-$), which decreases electron density between the nuclei

- Normalization of the molecular wavefunction requires:


``````{admonition} 中文翻译
:class: dropdown

- 此处，$1s_A$ 和 $1s_B$ 分别是以核 A 和核 B 为中心的氢原子 1s 轨道，$c_1$ 和 $c_2$ 为系数（常数）。
- 这种形式被称为用于构建分子轨道的**原子轨道线性组合（LCAO）**近似。
- 因为两个原子核相同，对称性要求 $c_1 = c_2 \equiv c$（且我们取 $c > 0$）。
- $\pm$ 号表示可以形成两个不同的分子轨道：
- **成键** 组合（$+$），它增强了原子核之间的电子密度
- **反键** 组合（$-$），它降低了两核间的电子密度
- 归一化分子波函数要求：
``````

$${\int{\psi_\pm^*\psi_\pm d\tau} = 1}$$

### The overlap integral

- We now consider the **bonding** molecular orbital (the "+" combination) and evaluate the normalization condition.

- Here, $S$ is the **overlap integral**, which depends on the internuclear distance $R$:


``````{admonition} 中文翻译
:class: dropdown

- 我们现在考虑**成键**分子轨道（“+”组合）并计算归一化条件。
- 这里，$S$ 是 **重叠积分**，取决于核间距离 $R$：
``````

$$
1 = \int |\psi_+|^2 \, d\tau
= c^2 \int (1s_A + 1s_B)(1s_A + 1s_B) \, d\tau
$$

- Expanding the integrand:

$$
\begin{aligned}
1 &= c^2 \int \left(1s_A^2 + 1s_B^2 + 2\,1s_A\,1s_B \right) d\tau \\
  &= c^2 \left( \int 1s_A^2 d\tau + \int 1s_B^2 d\tau + 2\int 1s_A\,1s_B\, d\tau \right)
\end{aligned}
$$

- Normalized atomic orbitals satisfy:

$$
\int 1s_A^2 d\tau = \int 1s_B^2 d\tau = 1
$$

- Defining the overlap integral:

$$
S = \int 1s_A(\vec{r})\,1s_B(\vec{r})\, d\tau
$$

- we obtain:

$$
1 = c^2(2 + 2S)
\quad \Rightarrow \quad 
c = \frac{1}{\sqrt{2(1 + S)}}
$$

:::{important} **Bonding and antibonding molecular orbitals**

$$
\psi_{+} \equiv \psi_g
= \frac{1}{\sqrt{2(1+S)}}
\left( 1s_A + 1s_B \right)
$$

$$
\psi_{-} \equiv \psi_u
= \frac{1}{\sqrt{2(1-S)}}
\left( 1s_A - 1s_B \right)
$$

The antibonding orbital has a **node between the nuclei**, resulting in **zero electron density** in that region.


``````{admonition} 中文翻译
:class: dropdown

反成键轨道在**核间有一个节点**，导致该区域**电子密度为零**。
``````
:::

### Bonding versus antibonding orbitals

:::{figure} ./images/b_vs_u.png
:alt: Bonding versus antibonding wavefunctions and densities
:width: 800px

Fig. 2 Bonding versus antibonding wavefunctions (molecular orbitals). Shown are the wavefunctions and the probability densities (squares of the wavefunctions).


``````{admonition} 中文翻译
:class: dropdown

图 2 成键与反成键波函数（分子轨道）。展示了波函数及其概率密度（波函数的平方）。
``````
:::

- The main feature of a chemical bond is the increased electron density between the nuclei. This identifies the $+$ wavefunction as a **bonding orbital** and the $-$ wavefunction as an **antibonding orbital**.

- When a molecule has a center of symmetry (here halfway between the nuclei), the wavefunction may or may not change sign when it is inverted through the center of symmetry. If the origin is placed at the center of symmetry, then we can assign symmetry labels $g$ and $u$ to the wavefunctions.

- If $\psi(x, y, z) = \psi(-x, -y, -z)$ then the symmetry label is $g$ (even parity), and for $\psi(x, y, z) = -\psi(-x, -y, -z)$ we have the $u$ label (odd parity).
- According to this notation, the $g$ symmetry orbital is the bonding orbital and the $u$ symmetry corresponds to the antibonding orbital. Later we will see that this is reversed for $\pi$-orbitals.

- The overlap integral $S(R)$ can be evaluated analytically (derivation not shown):


``````{admonition} 中文翻译
:class: dropdown

- 化学键的主要特征是原子间电子密度的增大。这将 $+$ 波函数识别为**键轨道**，将 $-$ 波函数识别为**反键轨道**。
- 当一个分子具有中心对称性（这里位于两个核之间）时，波函数在通过中心对称性反演时可能改变符号也可能不改变。如果原点置于中心对称点，我们可以给波函数赋予 $g$ 和 $u$ 的对称标签。
- 如果 $\psi(x, y, z) = \psi(-x, -y, -z)$ 则对称标记为 $g$（偶偶对称），且对于 $\psi(x, y, z) = -\psi(-x, -y, -z)$ 我们有 $u$ 标记（奇偶对称）。
- 按照此符号，$g$ 对称轨道是结合轨道，$u$ 对称对应反结合轨道。后来我们会看到，对于 $\pi$ 轨道这种情况是反过来的。
- 重叠积分 $S(R)$ 可以解析求得（推导略）：
``````

$${S(R) = e^{-R}\left( 1 + R + \frac{R^3}{3}\right)}$$

- Note that when $R = 0$ (the nuclei overlap), $S(0) = 1$, which is a useful check that the expression is reasonable.


``````{admonition} 中文翻译
:class: dropdown

- 注意当 $R = 0$（核重叠）时，$S(0) = 1$，这是一个检验表达式是否合理的有用方法。
``````

### Energy of the hydrogen molecule ion

- Using a linear combination of atomic orbitals, it is possible to calculate the best values, in terms of energy, of the coefficients $c_1$ and $c_2$. Remember that this linear combination can only provide an approximate solution to the $H_2^+$ Schrodinger equation. The variational principle provides a systematic way to calculate the energy when $R$ (the distance between the nuclei) is fixed:


``````{admonition} 中文翻译
:class: dropdown

- 使用原子轨道的线性组合，可以以能量为最优的方式计算系数 $c_1$ 和 $c_2$ 的值。记住，这种线性组合只能提供 $H_2^+$  Schrödinger 方程的近似解。变分原理提供了一种系统的方法来计算当 $R$（核间距离）固定时的能量：
``````

$${E = \frac{\int\psi_g^*\hat{H}_e\psi_gd\tau}{\int\psi_g^*\psi_gd\tau} = 
\frac{\int (c_11s_A + c_21s_B)\hat{H}_e(c_11s_A + c_21s_B)d\tau}
{\int (c_11s_A + c_21s_B)^2d\tau}}$$

$${= \frac{c_1^2H_{AA} + 2c_1c_2H_{AB} + c_2^2H_{BB}}
{c_1^2 S_{AA} + 2c_1c_2 S_{AB} + c_2^2 S_{BB}}}$$

where $S_{AA} = S_{BB} = 1$ and $S_{AB} = S$.


``````{admonition} 中文翻译
:class: dropdown

其中 $S_{AA} = S_{BB} = 1$ 且 $S_{AB} = S$。
``````

- Here $H_{AA}$, $H_{AB}$, $H_{BB}$, $S_{AA}$, $S_{AB}$, and $S_{BB}$ denote the integrals occurring in the variational treatment of the problem. The integrals $H_{AA}$ and $H_{BB}$ are called the Coulomb integrals (sometimes more generally termed matrix elements).

- This interaction is attractive, and therefore its numerical value must be negative. Note that by symmetry $H_{AA} = H_{BB}$. The integral $H_{AB}$ is called the resonance integral, and also by symmetry $H_{AB} = H_{BA}$.


``````{admonition} 中文翻译
:class: dropdown

- 这里 $H_{AA}$、$H_{AB}$、$H_{BB}$、$S_{AA}$、$S_{AB}$ 和 $S_{BB}$ 表示变分处理问题时出现的积分。积分 $H_{AA}$ 和 $H_{BB}$ 被称为库仑积分（有时更普遍地称为矩阵元）。
- 这种相互作用是有吸引力的，因此其数值必须为负。注意，由于对称性，$H_{AA} = H_{BB}$。积分 $H_{AB}$ 被称为共振积分，同样由于对称性，$H_{AB} = H_{BA}$。
``````

### Variational solution

- To minimize the energy expectation value with respect to $c_1$ and $c_2$, we calculate the partial derivatives of the energy with respect to these parameters:


``````{admonition} 中文翻译
:class: dropdown

- 为了使关于 $c_1$ 和 $c_2$ 的能量期望值最小化，我们计算能量对这些参数的偏导数：
``````

$${E\times (c_1^2 + 2c_1c_2S + c_2^2) = c_1^2H_{AA} + 2c_1c_2H_{AB} + c_2^2H_{BB}}$$

- Both sides can be differentiated with respect to $c_1$ to give:


``````{admonition} 中文翻译
:class: dropdown

- 对 $c_1$ 求导，两边可得：
``````

$${E\times (2c_1 + 2c_2S) + \frac{\partial E}{\partial c_1}\times (c_1^2 + 2c_1c_2S + c_2^2) = 2c_1H_{AA} + 2c_2H_{AB}}$$

- In a similar way, differentiation with respect to $c_2$ gives:


``````{admonition} 中文翻译
:class: dropdown

- 同样地，对 $c_2$ 求导得到：
``````

$${E\times (2c_2 + 2c_1S) + \frac{\partial E}{\partial c_2}\times (c_1^2 + 2c_1c_2S + c_2^2) = 2c_2H_{BB} + 2c_1H_{AB}}$$

- At the minimum energy (with respect to $c_1$ and $c_2$), the partial derivatives must be zero:


``````{admonition} 中文翻译
:class: dropdown

- 在最低能量处（关于 $c_1$ 和 $c_2$），偏导数必须为零：
``````

$${c_1(H_{AA} - E) + c_2(H_{AB} - SE) = 0}$$
$${c_2(H_{BB} - E) + c_1(H_{AB} - SE) = 0}$$

- In matrix notation this is a generalized matrix eigenvalue problem:


``````{admonition} 中文翻译
:class: dropdown

- 用矩阵表示法，这是一个广义矩阵特征值问题：
``````

$${\begin{pmatrix}H_{AA} - E & H_{AB} - SE\\
H_{AB} - SE & H_{BB} - E\\
\end{pmatrix}\begin{pmatrix} c_1\\ c_2\\\end{pmatrix} = 0}$$

- From linear algebra, we know that a non-trivial solution exists only if the secular determinant vanishes:


``````{admonition} 中文翻译
:class: dropdown

- 根据线性代数知识，只有当行列式为零时，才存在非平凡解：
``````

$${\begin{vmatrix}H_{AA} - E & H_{AB} - SE\\
H_{AB} - SE & H_{BB} - E\\
\end{vmatrix} = 0}$$

### Energies of the bonding and antibonding orbitals

- It can be shown that $H_{AA} = H_{BB} = E_{1s} + J(R)$, where $E_{1s}$ is the energy of a single hydrogen atom and $J(R)$ is a function of the internuclear distance $R$:


``````{admonition} 中文翻译
:class: dropdown

- 可以证明 $H_{AA} = H_{BB} = E_{1s} + J(R)$，其中 $E_{1s}$ 是单氢原子的能量，$J(R)$ 是核间距离 $R$ 的函数：
``````

$${J(R) = e^{-2R}\left( 1 + \frac{1}{R}\right)}$$

- Furthermore, $H_{AB} = H_{BA} = E_{1s}S(R) + K(R)$, where $K(R)$ is also a function of $R$:


``````{admonition} 中文翻译
:class: dropdown

- 此外，$H_{AB} = H_{BA} = E_{1s}S(R) + K(R)$，其中 $K(R)$ 也是 $R$ 的函数：
``````

$${K(R) = \frac{S(R)}{R} - e^{-R}\left( 1 + R\right)}$$

- If these expressions are substituted into the previous secular determinant, we get:


``````{admonition} 中文翻译
:class: dropdown

- 如果将这些表达式代入前面的行列式方程，我们得到：
``````

$${\begin{vmatrix}E_{1s} + J - E & E_{1s}S + K - SE\\
E_{1s}S + K - SE & E_{1s} + J - E\\
\end{vmatrix} = (E_{1s} + J - E)^2 - (E_{1s}S + K - SE)^2 = 0}$$

- This equation has two roots:

:::{important} **Energies of the two MOs**

$${E_g(R) = E_{1s} + \frac{J(R) + K(R)}{1 + S(R)}}$$

$${E_u(R) = E_{1s} + \frac{J(R) - K(R)}{1 - S(R)}}$$
:::

:::{figure} ./images/Energies.png
:alt: Energies of bonding and antibonding orbitals
:width: 600px

Fig. 3 Energies of the bonding and antibonding orbitals as a function of internuclear distance.


``````{admonition} 中文翻译
:class: dropdown

图 3 成键轨道和反键轨道的能量随核间距离的变化。
``````
:::

- Since energy is a relative quantity, it can be expressed relative to the separated nuclei:


``````{admonition} 中文翻译
:class: dropdown

- 由于能量是相对量，可以相对于分离的核来表示：
``````

$${\Delta E_g(R) = E_g(R) - E_{1s} = \frac{J(R) + K(R)}{1 + S(R)}}$$

$${\Delta E_u(R) = E_u(R) - E_{1s} = \frac{J(R) - K(R)}{1 - S(R)}}$$

### Comparison of MO energies with experiment

- These values can be compared with experimental results. The calculated ground state equilibrium bond length is 132 pm, whereas the experimental value is 106 pm. The binding energy is 170 kJ mol$^{-1}$, whereas the experimental value is 258 kJ mol$^{-1}$.
- The excited state (labeled with $u$) leads to repulsive behavior at all bond lengths $R$ (it is antibonding). Because the $u$ state lies higher in energy than the $g$ state, the $u$ state is an excited state of $H_2^+$.
- This calculation can be made more accurate by adding more than two terms to the linear combination. This procedure would also yield more excited state solutions. These would correspond to $u$/$g$ combinations of $2s$, $2p_x$, $2p_y$, $2p_z$, and so on.


``````{admonition} 中文翻译
:class: dropdown

- 这些值可以与实验结果进行比较。计算得到的基态平衡键长为 132 pm，而实验值为 106 pm。结合能为 170 kJ mol$^{-1}$，而实验值为 258 kJ mol$^{-1}$。
- 带有 $u$ 标签的激发态在所有键长 $R$ 处导致排斥行为（它是反键合态）。因为 $u$ 态的能量高于 $g$ 态，$u$ 态是 $H_2^+$ 的激发态。
- 通过在线性组合中加入两项以上，可以使此计算更准确。此过程也会产生更多激发态解。这些将对应于 $u$/$g$ 组合 $2s$, $2p_x$, $2p_y$, $2p_z$, 以及其他轨道。
``````

### MO diagrams

- It is common practice to represent the molecular orbitals using molecular orbital (MO) diagrams. The formation of bonding and antibonding orbitals can be visualized as follows:


``````{admonition} 中文翻译
:class: dropdown

- 常用分子轨道 (MO) 图表示分子轨道。键合和反键合轨道的形成可以如下可视化：
``````

:::{figure} ./images/h2plus_diag.png
:alt: Molecular orbital diagram for the hydrogen molecule ion
:width: 400px

Fig. 4 Molecular orbital diagram for $H_2^+$.
:::

- **$\sigma$ orbitals.** When two $s$ or $p_z$ orbitals interact, a $\sigma$ molecular orbital is formed. The notation $\sigma$ specifies the amount of angular momentum about the molecular axis (for $\sigma$, $\lambda = 0$ with $L_z = \pm\lambda\hbar$). In many-electron systems, both bonding and antibonding $\sigma$ orbitals can each hold a maximum of two electrons. Antibonding orbitals are often denoted by an asterisk.


``````{admonition} 中文翻译
:class: dropdown

- **$\sigma$ 轨道.** 当两个 $s$ 或 $p_z$ 轨道相互作用时，会形成一个 $\sigma$ 分子轨道。记号 $\sigma$ 指定了关于分子轴的角动量量（对于 $\sigma$，$\lambda = 0$ 且 $L_z = \pm\lambda\hbar$）。在多电子系统中，每个结合和反结合 $\sigma$ 轨道都最多可容纳两个电子。反结合轨道通常用星号表示。
``````

:::{figure} ./images/MO_variety.png
:alt: Molecular orbitals for homonuclear molecules
:width: 800px

Fig. 5 MOs for homonuclear molecules have distinct symmetry.


``````{admonition} 中文翻译
:class: dropdown

图 5 同核分子的分子轨道具有不同的对称性。
``````
:::

- **$\pi$ orbitals.** When two $p_{x,y}$ orbitals interact, a $\pi$ molecular orbital forms. $\pi$-orbitals are doubly degenerate: $\pi_{+1}$ and $\pi_{-1}$ (or alternatively $\pi_x$ and $\pi_y$), where the $+1/-1$ refer to the eigenvalue of the $L_z$ operator ($\lambda = \pm1$). In many-electron systems a bonding $\pi$-orbital can therefore hold a maximum of 4 electrons (both $\pi_{+1}$ and $\pi_{-1}$ each hold two electrons). The same holds for the antibonding $\pi$ orbitals. Note that only atomic orbitals of the same symmetry mix to form molecular orbitals (for example, $p_z - p_z$, $p_x - p_x$, and $p_y - p_y$). When atomic $d$ orbitals mix to form molecular orbitals, $\sigma$ ($\lambda = 0$), $\pi$ ($\lambda = \pm 1$), and $\delta$ ($\lambda = \pm 2$) MOs form.


``````{admonition} 中文翻译
:class: dropdown

- **$\pi$ 轨道.** 当两个 $p_{x,y}$ 轨道相互作用时，会形成一个 $\pi$ 分子轨道。$\pi$ 轨道是双重简并的：$\pi_{+1}$ 和 $\pi_{-1}$（或替代地 $\pi_x$ 和 $\pi_y$），其中 $+1/-1$ 对应 $L_z$ 算符的本征值（$\lambda = \pm1$）。在多电子系统中，因此键合 $\pi$ 轨道最多可容纳 4 个电子（每个 $\pi_{+1}$ 和 $\pi_{-1}$ 各容纳两个电子）。抗键合 $\pi$ 轨道也是如此。请注意，只有对称性相同的原子轨道才会混合形成分子轨道（例如，$p_z - p_z$，$p_x - p_x$，和 $p_y - p_y$）。当原子 $d$ 轨道混合形成分子轨道时，会形成 $\sigma$（$\lambda = 0$），$\pi$（$\lambda = \pm 1$），和 $\delta$（$\lambda = \pm 2$）分子轨道。
``````

:::{figure} ./images/MO_summary.png
:alt: MO diagram of homonuclear molecules
:width: 500px

Fig. 6 The MO diagram of homonuclear molecules follows a similar pattern with alternating bonding and antibonding MOs.


``````{admonition} 中文翻译
:class: dropdown

图 6 同核分子的 MO 图遵循类似的模式，成键和反键 MO 交替出现。
``````
:::

- Excited state energies of $H_2^+$ resulting from a calculation employing an extended basis set (more terms in the LCAO) are shown on the left below. The MO energy diagram, which includes the higher energy molecular orbitals, is shown on the right. Note that the energy order of the MOs depends on the molecule.

``````{admonition} 中文翻译
:class: dropdown

- 使用扩展基组（LCAO 中基函数项更多）计算得到的 $H_2^+$  excited state energies（激发态能量）如左图所示。右图所示的分子轨道能级图包含了更高能量的分子轨道。请注意，MOs（分子轨道）的能级顺序取决于分子。
``````

