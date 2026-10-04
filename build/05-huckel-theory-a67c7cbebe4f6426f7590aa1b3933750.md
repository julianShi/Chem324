---
kernelspec:
  name: python3
  display_name: Python 3
---

# Huckel Molecular Orbital Theory

:::{note} **What you will learn**

- Conjugated and aromatic systems with delocalized $\pi$ electrons are poorly described by localized valence bond pictures and call for a dedicated approach.
- **Huckel theory** treats the $\pi$ electrons independently and reduces the secular problem to a matrix built from just two empirical parameters: the Coulomb integral $\alpha$ and the resonance integral $\beta$.
- Diagonalizing the Huckel matrix gives the $\pi$ orbital energies and coefficients, and the energy gap predicts the lowest electronic excitation.
- Worked examples for **ethylene, 1,3-butadiene, and benzene** show how delocalization lowers the total $\pi$ energy and produces the aromatic stabilization of benzene.


``````{admonition} 中文翻译
:class: dropdown

- 具有离域 $\pi$ 电子的共轭体系和芳香体系难以用定域价键图像描述，需要专门的方法。
- **Hückel理论**独立处理 $\pi$ 电子，并将世问题简化为仅由两个经验参数构成的矩阵：库仑积分 $\alpha$ 和共振积分 $\beta$。
- 对 Huckel 矩阵对角化得到 $\pi$ 电子轨道能量和系数，能隙预测最低电子激发。
- 针对**乙烯、1,3-丁二烯和苯**的例题展示了离域化如何降低总$\pi$能量并产生苯的芳香性稳定化。
``````
:::

### Conjugated systems

- Molecules with extensive $\pi$ bonding systems, such as benzene, are not described very well by valence bond theory because the $\pi$ electrons are delocalized over the whole molecule. The $\sigma$ and $\pi$ bonds are illustrated below for ethylene ($C_2H_4$, with $sp^2$ carbons):


``````{admonition} 中文翻译
:class: dropdown

- 具有广泛$\pi$键系统的分子，如苯，由于$\pi$电子在整个分子上成键，不能很好地用价键理论描述。下面展示了乙烯($C_2H_4$，含$sp^2$碳)的$\sigma$和$\pi$键：
``````

:::{figure} images/Huckel1.png
:alt: Sigma and pi bonding in ethylene
:width: 600px

Fig. 1 The $\sigma$ framework and the delocalized $\pi$ system of ethylene ($C_2H_4$).


``````{admonition} 中文翻译
:class: dropdown

图 1 乙烯 ($C_2H_4$) 的 $\sigma$ 框架和离域 $\pi$ 体系。
``````
:::

- We have chosen the $z$-axis along the internuclear axis. Because both $\sigma$ and $\pi$ bonding occur between the two carbon atoms, we say that this is a double bond. The hybrid orbitals here also explain the geometry. For triple bonds, one $\sigma$ and two $\pi$ bonds are formed.


``````{admonition} 中文翻译
:class: dropdown

- 我们将$z$轴治设于核间轴。由于$\sigma$和$\pi$键都在两个碳原子之间形成，我们称这是一个双键。这里的杂化轨道也解释了几何形状。对于三键，形成一个$\sigma$键和两个$\pi$键。
``````

### Huckel MO theory

- Huckel molecular orbital theory assumes that the $\pi$ electrons, which are responsible for the special properties of conjugated and aromatic hydrocarbons, do not interact with one another, and that the total wavefunction is just a product of the one-electron molecular orbitals. The $\pi$ molecular orbital of the two carbons in $C_2H_4$ can be written approximately as:


``````{admonition} 中文翻译
:class: dropdown

- 休克尔分子轨道理论假设，负责共轭和芳香烃特殊性质的 $\pi$ 电子之间不相互作用，总波函数仅为一电子分子轨道的乘积。$C_2H_4$ 中两个碳原子的 $\pi$ 分子轨道可以近似地写成：
``````

$${\psi = c_1\phi_1 + c_2\phi_2}$$

- where $\phi_1$ and $\phi_2$ are the $2p_y$ atomic orbitals for carbons 1 and 2, respectively. Using the variational principle gives the following secular determinant:


``````{admonition} 中文翻译
:class: dropdown

- 其中 $\phi_1$ 和 $\phi_2$ 分别为碳1和碳2的 $2p_y$ 原子轨道。使用变分原理给出以下 secular 行列式：
``````

$${\begin{vmatrix} H_{11} - ES_{11} & H_{12} - ES_{12}\\
H_{21} - ES_{21} & H_{22} - ES_{22}\\ \end{vmatrix} = 0 \textnormal{ with }
H_{ij} = \int\phi_i^*H\phi_jd\tau \textnormal{ and } S_{ij} = \int\phi_i^*\phi_jd\tau}$$

:::{important} **The Huckel approximations**

In Huckel theory, the secular equation is simplified by assuming:


``````{admonition} 中文翻译
:class: dropdown

在 Hückel 理论中，通过假设简化了本征方程：
``````

1. All overlap integrals $S_{ij}$ are set to zero unless $i = j$, when $S_{ii} = 1$.
2. All diagonal matrix elements $H_{ii}$ are set to a constant denoted $\alpha$.
3. The resonance integrals $H_{ij}$ ($i \ne j$) are set to zero except for those on neighboring atoms, which are set equal to a constant $\beta$. The indices here also identify atoms, because the atomic orbitals are centered on atoms.


``````{admonition} 中文翻译
:class: dropdown

- 所有重叠积分 $S_{ij}$ 设为零，除非 $i = j$，此时 $S_{ii} = 1$。
- 所有对角矩阵元素 $H_{ii}$ 都设为一个用 $\alpha$ 表示的常数。
- 共振积分 $H_{ij}$ ($i \ne j$) 除邻近原子外均设为零，邻近原子的设为常数 $\beta$。此处的索引也标识原子，因为原子轨道以原子为中心。
``````
:::

With these rules, the secular determinant for ethylene becomes:


``````{admonition} 中文翻译
:class: dropdown

根据这些规则，乙烯的行列式变为：
``````

$${\begin{vmatrix}\alpha - E & \beta\\
\beta & \alpha - E\\ \end{vmatrix} = 0}$$

- In Huckel theory, the Coulomb integral $\alpha$ and the resonance integral $\beta$ are regarded as empirical parameters. They can be obtained, for example, from experimental data. Thus, in Huckel theory it is not necessary to specify the Hamiltonian operator. Expansion of the determinant leads to a quadratic equation for $E$, with solutions $E = \alpha \pm \beta$. In general, it can be shown that $\beta < 0$, which implies that the lowest orbital energy is $E_1 = \alpha + \beta$. There are two $\pi$ electrons, and therefore the total energy is $E_{tot} = 2E_1 = 2\alpha + 2\beta$. Do not confuse $\alpha$ and $\beta$ here with electron spin.


``````{admonition} 中文翻译
:class: dropdown

- 在胡克尔理论中，库仑积分 $\alpha$ 和共振积分 $\beta$ 被视为经验参数。它们可以例如从实验数据中获得。因此，在胡克尔理论中，不需要指定哈密顿算子。展开行列式得到 $E$ 的二次方程，其解为 $E = \alpha \pm \beta$。一般来说，可以证明 $\beta < 0$，这意味着最低轨道能量为 $E_1 = \alpha + \beta$。有两个 $\pi$ 电子，因此总能量为 $E_{tot} = 2E_1 = 2\alpha + 2\beta$。此处勿将 $\alpha$ 和 $\beta$ 与电子自旋混淆。
``````

### Solving for the Huckel MOs

The wavefunctions (the coefficients $c_1$ and $c_2$) can be obtained by substituting the two values of $E$ into the original linear equations:


``````{admonition} 中文翻译
:class: dropdown

将 $E$ 的两个值代入原来的线性方程组，即可得到波函数（系数 $c_1$ 和 $c_2$）：
``````

$${c_1(\alpha - E) + c_2\beta = 0}$$

$${c_1\beta + c_2(\alpha - E) = 0}$$

For the lowest energy orbital ($E_1 = \alpha + \beta$), we get (including normalization):


``````{admonition} 中文翻译
:class: dropdown

对于最低能量轨道 ($E_1 = \alpha + \beta$)，我们得到（含归一化）：
``````

$${\psi_1 = \frac{1}{\sqrt{2}}(\phi_1 + \phi_2) \hspace{0.5cm}(\textnormal{i.e. }c_1 = c_2 = \frac{1}{\sqrt{2}})}$$

and for the highest energy orbital ($E_2 = \alpha - \beta$) (including normalization):


``````{admonition} 中文翻译
:class: dropdown

对于最高能量轨道 ($E_2 = \alpha - \beta$)（含归一化）：
``````

$${\psi_2 = \frac{1}{\sqrt{2}}(\phi_1 - \phi_2) \hspace{0.5cm}(\textnormal{i.e. }c_1 = \frac{1}{\sqrt{2}}, c_2 = -\frac{1}{\sqrt{2}})}$$

These orbitals resemble the $H_2^+$ LCAO MOs discussed previously. This also gives us an estimate for one of the excited states, where one electron is promoted from the bonding to the antibonding orbital. The excitation energy is found to be $2|\beta|$, which allows, for example, the estimation of $\beta$ from UV/VIS absorption spectroscopy.


``````{admonition} 中文翻译
:class: dropdown

这些轨道与先前讨论的 $H_2^+$ LCAO MO 相似。这也让我们对其中一个激发态进行了估计，其中一个电子从结合轨道被激发到反结合轨道。激发能量被发现为 $2|\beta|$，这允许例如通过 UV/VIS 吸收光谱估计 $\beta$。
``````

| HOMO orbital | The highest occupied molecular orbital. |
|--------------|-------------------------------------------|
| LUMO orbital | The lowest unoccupied molecular orbital. |

### Example: 1,3-butadiene

- Let us calculate the $\pi$ electronic energy for 1,3-butadiene ($CH_2=CHCH=CH_2$) using Huckel theory. First we write the secular determinant using the rules given earlier. To do this, it is convenient to number the carbon atoms in the molecule:


``````{admonition} 中文翻译
:class: dropdown

- 让我们使用 Huckel 理论计算 1,3-丁二烯 ($CH_2=CHCH=CH_2$) 的 $\pi$ 电子能量。首先，我们根据 earlier（此处指 earlier given rules，保留 earlier 或译为“前文”）给出的规则写出 secular determinant（此处保留 secular determinant 或译为“ secular 行列式”。为保持一致，此处译为“ secular 行列式”。）。为方便操作，我们给分子中的碳原子编号：
``````

$$\overset{1}{\textnormal{CH}_2} = \overset{2}{\textnormal{CH}} 
- \overset{3}{\textnormal{CH}} = \overset{4}{\textnormal{CH}_2}$$

In this case there are two scenarios to consider:


``````{admonition} 中文翻译
:class: dropdown

在这种情况下有两种情形需要考虑：
``````

1. A localized solution where the $\pi$ electrons are shared either between atoms 1 and 2 or between atoms 3 and 4. This implies that the $\beta$ parameter should not be written between nuclei 2 and 3.
2. A delocalized solution where the $\pi$ electrons are delocalized over all four carbons. This implies that the $\beta$ parameter should be written between nuclei 2 and 3.


``````{admonition} 中文翻译
:class: dropdown

- 一个局域化解，其中 $\pi$ 电子在原子 1 和 2 之间或原子 3 和 4 之间共享。这意味着 $\beta$ 参数不应在原子 2 和 3 之间的核之间书写。
- 一种离域解，其中 $\pi$ 电子在所有四个碳原子上离域。这意味着 $\beta$ 参数应写在核 2 和 3 之间。
``````

Here it turns out that scenario 2 gives a lower energy solution, and we study that in more detail. In general, however, both cases should be considered. The energy difference between scenarios 1 and 2 is called the resonance stabilization energy. The secular determinant is:


``````{admonition} 中文翻译
:class: dropdown

在这种情况下，情况 2 得到的能量解更低，我们将在更细节地研究该情况。然而，一般来说，两种情况都应该考虑。情况 1 和情况 2 之间的能量差称为共振稳定化能。 secular determinant（ secular 行列式）为：
``````

$${\begin{matrix} 1\\2\\3\\4\\
\end{matrix}\begin{vmatrix}
\alpha - E & \beta & 0 & 0\\
\beta & \alpha - E & \beta & 0\\
0 & \beta & \alpha - E & \beta\\
0 & 0 & \beta & \alpha - E\\
\end{vmatrix}
= 0}$$

To simplify the notation, we divide each row by $\beta$ and denote $x = (\alpha - E) / \beta$:


``````{admonition} 中文翻译
:class: dropdown

为简化符号，我们将每行除以 $\beta$ 并令 $x = (\alpha - E) / \beta$：
``````

$${\begin{vmatrix}
x & 1 & 0 & 0\\
1 & x & 1 & 0\\
0 & 1 & x & 1\\
0 & 0 & 1 & x\\
\end{vmatrix} = 0}$$

Expansion of this determinant gives $x^4 - 3x^2 + 1 = 0$. There are four solutions, $x = \pm 0.618$ and $x = \pm 1.618$. Thus there are four possible orbital energy levels:


``````{admonition} 中文翻译
:class: dropdown

展开该行列式得 $x^4 - 3x^2 + 1 = 0$。有四个解，$x = \pm 0.618$ 且 $x = \pm 1.618$。因此有四个可能的轨道能级：
``````

$$
{E_1 = \alpha + 1.618\beta \hspace{0.5cm}\textnormal{(lowest energy)}} \\
{E_2 = \alpha + 0.618\beta} \\
{E_3 = \alpha - 0.618\beta} \\
{E_4 = \alpha - 1.618\beta \hspace{0.5cm}\textnormal{(highest energy)}}$$

:::{figure} images/c4MOs.png
:alt: Huckel molecular orbitals of butadiene
:width: 600px

Fig. 2 The four Huckel $\pi$ molecular orbitals of 1,3-butadiene, ordered by energy.


``````{admonition} 中文翻译
:class: dropdown

图 2 1,3-丁二烯的四个 Hückel $\pi$ 分子轨道，按能量排序。
``````
:::

There are four $\pi$ electrons, which occupy the two lowest energy orbitals. This gives the total $\pi$ electronic energy of the molecule:


``````{admonition} 中文翻译
:class: dropdown

有四个 $\pi$ 电子，它们占据两个最低能量轨道。这给出了分子的总 $\pi$ 电子能量：
``````

$${E_\pi = 2(\alpha + 1.618\beta) + 2(\alpha + 0.618\beta)
= 4\alpha + 4.472\beta}$$

and the lowest excitation energy is $1.236|\beta|$.

The four Huckel MO wavefunctions are (calculations not shown):


``````{admonition} 中文翻译
:class: dropdown

四个 Hückel 分子轨道波函数为（计算过程略）：
``````

$${\psi_1 = 0.372\phi_1 + 0.602\phi_2 + 0.602\phi_3 + 0.372\phi_4}$$
$${\psi_2 = 0.602\phi_1 + 0.372\phi_2 - 0.372\phi_3 - 0.602\phi_4}$$
$${\psi_3 = 0.602\phi_1 - 0.372\phi_2 - 0.372\phi_3 + 0.602\phi_4}$$
$${\psi_4 = 0.372\phi_1 - 0.602\phi_2 + 0.602\phi_3 - 0.372\phi_4}$$

### Example: the benzene molecule

- Let us now apply the Huckel method to the benzene molecule. The secular determinant for benzene is (electrons delocalized):


``````{admonition} 中文翻译
:class: dropdown

- 现在让我们将 Hückel 方法应用于苯分子。苯的本征值行列式为（电子离域）：
``````

$${
\begin{vmatrix}
\alpha - E & \beta      &     0      & 0          & 0          & \beta\\
\beta      & \alpha - E & \beta      & 0          & 0          & 0\\
0          & \beta      & \alpha - E & \beta      & 0          & 0\\
0          & 0          & \beta      & \alpha - E & \beta      & 0\\
0          & 0          & 0          & \beta      & \alpha - E & \beta\\
\beta      & 0          & 0          & 0          & \beta      & \alpha - E\\
\end{vmatrix}
= 0
}$$

The solutions are (showing where the six $\pi$ electrons should be placed):


``````{admonition} 中文翻译
:class: dropdown

解如下（显示六个 $\pi$ 电子应放置的位置）：
``````

$$
{E_1 = \alpha + 2\beta~~\textnormal{(lowest energy)}} \\
{E_2 = E_3 = \alpha + \beta} \\
{E_4 = E_5 = \alpha - \beta} \\
{E_6 = \alpha - 2\beta~~\textnormal{(highest energy)}}$$

:::{figure} images/benzeneMos.png
:alt: Huckel molecular orbitals of benzene
:width: 600px

Fig. 3 The six Huckel $\pi$ molecular orbitals of benzene. The doubly degenerate pairs reflect the high symmetry of the ring.


``````{admonition} 中文翻译
:class: dropdown

图 3 苯的六个 Hückel $\pi$ 分子轨道。成对的二重简并反映了环的高对称性。
``````
:::

The six $\pi$ electrons fill the lowest three levels ($E_1$ and the degenerate pair $E_2 = E_3$), giving a total $\pi$ energy of $6\alpha + 8\beta$. Compared with three isolated ethylene double bonds ($6\alpha + 6\beta$), benzene is stabilized by an extra $2\beta$, which is the origin of its aromatic stability.

``````{admonition} 中文翻译
:class: dropdown

六个 $\pi$ 电子填入最低的三个能级 ($E_1$ 以及退配对 $E_2 = E_3$)，给出总 $\pi$ 能量 $6\alpha + 8\beta$。与三个孤立的乙烯双键 ($6\alpha + 6\beta$) 相比，苯因额外的 $2\beta$ 而稳定，这是其芳香稳定性的由来。
``````

