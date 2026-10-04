---
kernelspec:
  name: python3
  display_name: Python 3
---

# Electronic Structure of Polyatomic Molecules

:::{note} **What you will learn**

- The MO picture extends across the homonuclear diatomic series, where filling alternating bonding and antibonding orbitals predicts **bond order, bond length, and dissociation energy**.
- The **non-crossing rule:** molecular orbital states of the same symmetry never cross as a function of internuclear distance.
- The **valence bond approach** builds bonds from overlapping atomic orbitals, and it naturally gives rise to **hybrid orbitals** ($sp$, $sp^2$, $sp^3$) that explain molecular geometries.
- Worked examples for $BeH_2$, $BH_3$, $CH_4$, and $H_2O$ connect hybridization to the observed shapes of small molecules.
- Practical numerical quantum chemistry replaces atomic orbitals with **Gaussian basis sets** that allow analytic evaluation of the required integrals.


``````{admonition} 中文翻译
:class: dropdown

- MO 图像延伸至同原子二原子系列，填充交替的键合和反键轨道预测 **bond order, bond length, and dissociation energy**（键序、键长和解离能）。
- **不相交规则：** 同一对称性的分子轨道态作为核间距离的函数永不相交。
- **价键法** 从重叠的原子轨道构建键，并自然产生**杂化轨道** ($sp$, $sp^2$, $sp^3$) 来解释分子几何结构。
- $BeH_2$、$BH_3$、$CH_4$ 和 $H_2O$ 的例题将杂化与小分子观测到的形状联系起来。
- 实际的数值量子化学用**高斯基组**取代原子轨道，从而能解析地计算所需积分。
``````
:::

### Orbitals of homonuclear diatomic molecules

Which atomic orbitals mix to form molecular orbitals, and what are their relative energies? The interactive viewer below can be used to obtain the energy order of molecular orbitals and indicates the atomic orbital limits.


``````{admonition} 中文翻译
:class: dropdown

哪些原子轨道混合形成分子轨道？它们的相对能量是多少？下面的交互式查看器可用于获取分子轨道的能量顺序，并指示原子轨道的极限。
``````

<iframe src="https://al2me6.github.io/evanescence/"
        width="800"
        height="500"
        allowfullscreen>
</iframe>

### The non-crossing rule

States with the same symmetry never cross.

| Bonding orbitals:     | $1\sigma_g$, $2\sigma_g$, $1\pi_u$, etc.       |
|-----------------------|------------------------------------------------|
| Antibonding orbitals: | $1\sigma_u^*$, $2\sigma_u^*$, $1\pi_g^*$, etc. |

:::{figure} images/non-crossing-rule.png
:alt: Non-crossing rule for molecular orbital correlation diagram
:width: 600px

Fig. 1 Correlation diagram illustrating the non-crossing rule: orbitals of the same symmetry avoid each other as the internuclear distance changes.


``````{admonition} 中文翻译
:class: dropdown

图 1 说明不相交规则的相关图：当核间距离变化时，相同对称性的轨道相互避让。
``````
:::

### Table of molecular orbitals

The orbitals are filled with electrons in order of increasing energy. Note that $\pi$, $\delta$, etc. orbitals can hold a total of 4 electrons. If only one bond is formed, we say that the bond order (BO) is 1. If two bonds form (for example, one $\sigma$ and one $\pi$), the bond order is 2 (a double bond). Molecular orbitals always come in pairs: bonding and antibonding.


``````{admonition} 中文翻译
:class: dropdown

电子按能量递增的顺序填充轨道。注意，$\pi$、$\delta$ 等轨道总共可以容纳4个电子。如果只形成一个键，我们称键级（BO）为1。如果形成两个键（例如一个$\sigma$和一个$\pi$），键级为2（双键）。分子轨道总是成对出现：键合轨道和反键合轨道。
``````

| Molecule | Electrons | Configuration                    | Term sym.    | BO  | $R_e$ (Å) | $D_e$ (eV)   |
|----------|------------|----------------------------------|--------------|-----|-------------|--------------|
| $H_2^+$  | 1          | $(1\sigma_g)$                    | $^2\Sigma_g$ | 0.5 | 1.060       | 2.793        |
| $H_2$    | 2          | $(1\sigma_g)^2$                  | $^1\Sigma_g$ | 1.0 | 0.741       | 4.783        |
| $He_2^+$ | 3          | $(1\sigma_g)^2(1\sigma_u)$       | $^2\Sigma_u$ | 0.5 | 1.080       | 2.5          |
| $He_2$   | 4          | $(1\sigma_g)^2(1\sigma_u)^2$     | $^1\Sigma_g$ | 0.0 |             |              |
| $Li_2$   | 6          | $He_2(2\sigma_g)^2$              | $^1\Sigma_g$ | 1.0 | 2.673       | 1.14         |
| $Be_2$   | 8          | $He_2(2\sigma_g)^2(2\sigma_u)^2$ | $^1\Sigma_g$ | 0.0 |             |              |
| $B_2$    | 10         | $Be_2(1\pi_u)^2$                 | $^3\Sigma_g$ | 1.0 | 1.589       | $\approx 3.0$ |
| $C_2$    | 12         | $Be_2(1\pi_u)^4$                 | $^1\Sigma_g$ | 2.0 | 1.242       | 6.36         |
| $N_2^+$  | 13         | $Be_2(1\pi_u)^4(3\sigma_g)$      | $^2\Sigma_g$ | 2.5 | 1.116       | 8.86         |
| $N_2$    | 14         | $Be_2(1\pi_u)^4(3\sigma_g)^2$    | $^1\Sigma_g$ | 3.0 | 1.094       | 9.902        |
| $O_2^+$  | 15         | $N_2(1\pi_g)$                    | $^2\Pi_g$    | 2.5 | 1.123       | 6.77         |
| $O_2$    | 16         | $N_2(1\pi_g)^2$                  | $^3\Sigma_g$ | 2.0 | 1.207       | 5.213        |
| $F_2$    | 18         | $N_2(1\pi_g)^4$                  | $^1\Sigma_g$ | 1.0 | 1.435       | 1.34         |
| $Ne_2$   | 20         | $N_2(1\pi_g)^4(3\sigma_u)^2$     | $^1\Sigma_g$ | 0.0 |             |              |

:::{note} **Reading the table**

- A missing value of $R_e$ means that the molecule is not stable.
- Hund's rules predict that the electron configuration with the largest multiplicity lies lowest in energy when the highest occupied MOs are degenerate.


``````{admonition} 中文翻译
:class: dropdown

- $R_e$ 缺失意味着分子不稳定。
- 洪特规则预测，当最高占据分子轨道简并时，多重度最大的电子构型能量最低。
``````
:::

### The valence bond approach

- The valence bond method is an approximate approach that is useful for understanding the formation of chemical bonds. In particular, concepts like hybrid orbitals follow directly from it.

- The valence bond method is based on the idea that a chemical bond forms when there is non-zero overlap between the atomic orbitals of the participating atoms. The atomic orbitals must therefore have the same symmetry in order to gain overlap.

- Hybrid orbitals are essentially linear combinations of atomic orbitals that belong to a single atom. Note that hybrid orbitals are not meaningful for free atoms, as they only begin to form when other atoms approach. The idea is best illustrated through the following examples.


``````{admonition} 中文翻译
:class: dropdown

- 价键法是一种近似方法，对于理解化学键的形成很有用。特别是，杂化轨道的概念直接源于此。
- 价键法基于这样的理念：当参与原子的原子轨道之间存在非零重叠时，化学键才会形成。因此，原子轨道必须具有相同的对称性才能获得重叠。
- 杂化轨道本质上是属于单一原子的原子轨道的线性组合。注意，对于自由原子，杂化轨道没有意义，它们仅在其他原子接近时才开始形成。其思想最好通过以下示例来说明。
``````

### Example 1: The $BeH_2$ molecule

- The Be atom has the atomic electron configuration He$2s^2$. The two approaching hydrogens perturb the atomic orbitals, and the two outer-shell electrons reside on the two hybrid orbitals formed (the $z$-axis is along the molecular axis):


``````{admonition} 中文翻译
:class: dropdown

- Be 原子的原子电子排布为 He$2s^2$。两个靠近的氢原子扰动了原子轨道，两个最外层电子占据形成的两个杂化轨道上（$z$ 轴沿分子轴）：
``````

:::{figure} images/BeH1.png
:alt: sp hybrid orbital formation in BeH2
:width: 500px

Fig. 2 Formation of $sp$ hybrid orbitals on the Be atom in $BeH_2$.


``````{admonition} 中文翻译
:class: dropdown

图 2 $BeH_2$ 中 Be 原子上 $sp$ 杂化轨道的形成。
``````
:::

$${\psi_{sp}^1 = \frac{1}{\sqrt{2}}(2s + 2p_z)}$$

$${\psi_{sp}^2 = \frac{1}{\sqrt{2}}(2s - 2p_z)}$$

The hybrid orbitals further form two molecular $\sigma$ orbitals:


``````{admonition} 中文翻译
:class: dropdown

杂化轨道进一步形成两个分子 $\sigma$ 轨道：
``````

:::{figure} images/BeH2.png
:alt: sigma bonds formed by sp hybrids in BeH2
:width: 500px

Fig. 3 The $sp$ hybrids on Be each form a $\sigma$ bond with a hydrogen 1s orbital.


``````{admonition} 中文翻译
:class: dropdown

图 3 Be 上的 $sp$ 杂化轨道各自与一个氢 1s 轨道形成一条 $\sigma$ 键。
``````
:::

$${\psi = c_11s_A + c_2\psi_{sp}^1}$$

$${\psi' = c_1'1s_B + c_2'\psi_{sp}^2}$$

:::{figure} images/BeH2-orbs.png
:alt: BeH2 molecular orbitals
:width: 500px

Fig. 4 The resulting linear $\sigma$ framework of $BeH_2$.


``````{admonition} 中文翻译
:class: dropdown

图 4 $BeH_2$ 所得的线性 $\sigma$ 框架。
``````
:::

- **This form of hybridization is called $sp$.** It means that one $s$ and one $p$ orbital participate in forming the hybrid orbitals. For $sp$ hybrids, linear geometries are favored, and here H-Be-H is indeed linear. Each MO between Be and H contains two shared electrons. Note that the number of initial atomic orbitals and the number of hybrid orbitals formed must be identical: here $s$ and $p$ atomic orbitals give two $sp$ hybrid orbitals. Hybrid orbitals should be orthonormalized.


``````{admonition} 中文翻译
:class: dropdown

- **这种杂化称为 $sp$。** 这意味着一个 $s$ 轨道和一个 $p$ 轨道参与形成杂化轨道。对于 $sp$ 杂化轨道，倾向于线性几何结构，而这里的 H-Be-H 确实是线性的。每个 Be 与 H 之间的 MO 包含两个共享电子。值得注意的是：初始原子轨道的数量与形成的杂化轨道数量必须相同：这里 $s$ 和 $p$ 原子轨道形成两个 $sp$ 杂化轨道。杂化轨道应正交归一化。
``````

### Example 2: The $BH_3$ molecule

- All the atoms lie in a plane (a planar structure), and the angles between the H atoms are $120^\circ$. The boron atom has electron configuration $1s^22s^22p$. Three atomic orbitals ($2s$, $2p_z$, $2p_x$) participate in forming three hybrid orbitals:


``````{admonition} 中文翻译
:class: dropdown

- 所有原子都在一个平面内（平面结构），且 H 原子之间的角度为 $120^\circ$。硼原子的电子构型为 $1s^22s^22p$。三个原子轨道 ($2s$, $2p_z$, $2p_x$) 参与形成三个杂化轨道：
``````

$${\psi^1_{sp^2} = \frac{1}{\sqrt{3}}2s + \sqrt{\frac{2}{3}}2p_z}$$

$${\psi^2_{sp^2} = \frac{1}{\sqrt{3}}2s - \frac{1}{\sqrt{6}}2p_z 
+ \frac{1}{\sqrt{2}}2p_x}$$

$${\psi^3_{sp^2} = \frac{1}{\sqrt{3}}2s - \frac{1}{\sqrt{6}}2p_z 
- \frac{1}{\sqrt{2}}2p_x}$$

The three orbitals can have the following spatial orientations:


``````{admonition} 中文翻译
:class: dropdown

这三个轨道可以有以下空间取向：
``````

:::{figure} images/BeH3.png
:alt: sp2 hybrid orbitals of BH3
:width: 500px

Fig. 5 The three $sp^2$ hybrid orbitals of $BH_3$ point to the corners of an equilateral triangle.


``````{admonition} 中文翻译
:class: dropdown

图 5 $BH_3$ 的三个 $sp^2$ 杂化轨道指向正三角形的三个顶点。
``````
:::

- Each of these hybrid orbitals forms a $\sigma$ bond with an H atom. This is called $sp^2$ hybridization, because two $p$ orbitals and one $s$ orbital participate in the hybrid.


``````{admonition} 中文翻译
:class: dropdown

- 这些杂化轨道每个与一个 H 原子形成一个 $\sigma$ 键。这称为 $sp^2$ 杂化，因为两个 $p$ 轨道和一个 $s$ 轨道参与了杂化。
``````

### Example 3: The $CH_4$ molecule

- The electron configuration of the carbon atom is $1s^22s^22p^2$. The four outer valence electrons should be placed in four $sp^3$ hybrid orbitals:


``````{admonition} 中文翻译
:class: dropdown

- 碳原子的电子排布为 $1s^22s^22p^2$。四个外层价电子应放置在四个 $sp^3$ 杂化轨道中：
``````

$${\psi^1_{sp^3} = \frac{1}{2}(2s + 2p_x + 2p_y + 2p_z)}$$

$${\psi^2_{sp^3} = \frac{1}{2}(2s - 2p_x - 2p_y + 2p_z)}$$

$${\psi^3_{sp^3} = \frac{1}{2}(2s + 2p_x - 2p_y - 2p_z)}$$

$${\psi^4_{sp^3} = \frac{1}{2}(2s - 2p_x + 2p_y - 2p_z)}$$

These four hybrid orbitals form $\sigma$ bonds with the four hydrogen atoms.


``````{admonition} 中文翻译
:class: dropdown

这四个杂化轨道与四个氢原子形成 $\sigma$ 键。
``````

:::{figure} images/CH4.png
:alt: sp3 hybrid orbitals of methane
:width: 500px

Fig. 6 The four $sp^3$ hybrids of $CH_4$ point to the corners of a tetrahedron.


``````{admonition} 中文翻译
:class: dropdown

图 6 $CH_4$ 的四个 $sp^3$ 杂化轨道指向四面体的角点。
``````
:::

The $sp^3$ hybridization is directly responsible for the tetrahedral geometry of the $CH_4$ molecule. Note that for other elements with $d$-orbitals, one can also obtain bipyramidal (coordination 5) and octahedral (coordination 6) structures.


``````{admonition} 中文翻译
:class: dropdown

$sp^3$ 混合直接负责 $CH_4$ 分子的四面体几何结构。请注意，对于其他拥有 $d$ 轨道的元素，也可以得到配位数为5的双锥形以及配位数为6的八面体结构。
``````

### Example 4: The $H_2O$ molecule

- The oxygen is $sp^3$ hybridized, with O atom electron configuration $1s^22s^22p^4$. Two of the four hybrid orbitals are doubly occupied with electrons from the oxygen atom, and the remaining two hybrid orbitals participate in $\sigma$ bonding with the two H atoms. This predicts the bond angle H-O-H to be $109^\circ$ (experimental value $104^\circ$). Thus $H_2O$ has two lone pairs of electrons.


``````{admonition} 中文翻译
:class: dropdown

- 氧原子是 $sp^3$ 杂化，氧原子电子构型 $1s^22s^22p^4$。四个杂化轨道中有两个被氧原子上的电子双重占据，剩余的两个杂化轨道与两个 H 原子参与 $\sigma$ 键合。这预测 H-O-H 键角为 $109^\circ$（实验值 $104^\circ$）。因此 $H_2O$ 有两对电子孤对。
``````

:::{figure} images/watMO1.png
:alt: Water hybrid orbitals
:width: 500px

Fig. 7 The $sp^3$ hybrid framework of the water molecule.


``````{admonition} 中文翻译
:class: dropdown

图 7 水分子的 $sp^3$ 杂化骨架。
``````
:::

:::{figure} images/watMO2.png
:alt: Water bonding orbitals
:width: 500px

Fig. 8 Bonding and lone-pair orbitals of water.


``````{admonition} 中文翻译
:class: dropdown

图 8 水的成键轨道和孤对轨道。
``````
:::

:::{figure} images/watMO3.png
:alt: Water molecular orbitals
:width: 500px

Fig. 9 The occupied molecular orbitals of water.


``````{admonition} 中文翻译
:class: dropdown

图 9 水的占据分子轨道。
``````
:::

:::{figure} images/watMO-diag.png
:alt: Water molecular orbital diagram
:width: 500px

Fig. 10 Molecular orbital diagram for the water molecule.


``````{admonition} 中文翻译
:class: dropdown

图 10 水分子的分子轨道图。
``````
:::

### Other molecules

<iframe src="https://al2me6.github.io/evanescence/"
        width="800"
        height="500"
        allowfullscreen>
</iframe>

### Numerical calculations

In numerical quantum chemical calculations, basis sets that resemble linear combinations of atomic orbitals are typically used (LCAO-MO-SCF). The atomic orbitals are approximated by a group of Gaussian functions, which allow analytic evaluation of the integrals appearing, for example, in the Hartree-Fock (SCF; HF) method. Note that hydrogenlike atomic orbitals differ from Gaussian functions by the power of $r$ in the exponent. A useful rule for Gaussians: the product of two Gaussian functions is another Gaussian function.

``````{admonition} 中文翻译
:class: dropdown

在数值量子化学计算中，通常使用 resemble linear combinations of atomic orbitals 的基组（LCAO-MO-SCF）。原子轨道由一组高斯函数近似，这允许在例如哈特里-福克（SCF; HF）方法中出现的积分进行解析求解。请注意，氢原子轨道与高斯函数的不同之处在于指数中的 $r$ 的幂次。高斯函数的一个有用规则：两个高斯函数的乘积是另一个高斯函数。
``````

