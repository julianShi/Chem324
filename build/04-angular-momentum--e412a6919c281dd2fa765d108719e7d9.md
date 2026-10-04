---
kernelspec:
  name: python3
  display_name: Python 3
---

# Angular Momentum and Term Symbols

:::{note} **What you will learn**

- Total orbital angular momentum $\hat{L} = \sum_{i=1}^N \hat{l}_i$ quantifies the combined angular momentum of all electrons, with quantized values of $L$ ranging from $|l_1 - l_2|$ to $l_1 + l_2$.
- Total spin angular momentum $\hat{S} = \sum_{i=1}^N \hat{s}_i$ follows a similar quantization rule, with possible $S$ values for two electrons being 1 (triplet) or 0 (singlet).
- The total angular momentum $\hat{J} = \hat{L} + \hat{S}$ combines orbital and spin contributions, with $J$ taking values from $|L - S|$ to $L + S$.
- Term symbols are written as $^{2S+1}L_J$, where $2S+1$ is the spin multiplicity, $L$ is the total orbital momentum (S, P, D, F, ...), and $J$ is the total angular momentum.
- Hund's rules state that (1) the highest spin multiplicity lies lowest in energy, (2) for the same $S$, the highest $L$ is lowest, and (3) for the same $S$ and $L$, the smallest $J$ is lowest for a less-than-half-filled subshell, while the largest $J$ is lowest for a more-than-half-filled subshell.
- Spin-orbit interaction couples $\vec{L}$ and $\vec{S}$ via $\hat{H}_{SO} = A\,\vec{\hat{L}} \cdot \vec{\hat{S}}$, causing fine-structure splitting, especially in heavier atoms.
- Selection rules for allowed transitions are $\Delta l = \pm 1$, $\Delta L = 0, \pm 1$ (except $L = 0 \to L = 0$), $\Delta J = 0, \pm 1$ (except $J = 0 \to J = 0$), and $\Delta S = 0$.
- In light atoms, Russell-Saunders ($LS$) coupling applies, so $L$, $S$, and $J$ are all good quantum numbers; in heavier atoms spin-orbit coupling dominates and $J$ becomes the only good quantum number.
- The ground-state term symbol of an atom is determined using Hund's rules; for example He ($1s^2$) has term symbol $^1$S$_0$, while C ($1s^2 2s^2 2p^2$) has term symbol $^3$P$_0$.


``````{admonition} 中文翻译
:class: dropdown

- 总轨道角动量 $\hat{L} = \sum_{i=1}^N \hat{l}_i$ 量化了所有电子的组合角动量，其量化值 $L$ 的范围从 $|l_1 - l_2|$ 到 $l_1 + l_2$。
- 总自旋角动量 $\hat{S} = \sum_{i=1}^N \hat{s}_i$ 遵循类似的量子化规则，两个电子的可能 $S$ 值为 1（三重态）或 0（单重态）。
- 总角动量 $\hat{J} = \hat{L} + \hat{S}$ 结合了轨道和自旋贡献，$J$ 取从 $|L - S|$ 到 $L + S$ 的值。
- 项符号写作 $^{2S+1}L_J$，其中 $2S+1$ 是自旋倍性，$L$ 是总轨道动量（S、P、D、F...），$J$ 是总角动量。
- 洪特规则规定：(1) 最高自旋多重态能量最低，(2) 对于相同的 $S$，最高的 $L$ 最低，(3) 对于相同的 $S$ 和 $L$，半补电亚层最少时最小的 $J$ 能量最低，而半补电亚层最多时最大的 $J$ 能量最低。
- 自旋-轨道相互作用通过 $\hat{H}_{SO} = A\,\vec{\hat{L}} \cdot \vec{\hat{S}}$ 耦合 $\vec{L}$ 和 $\vec{S}$，导致细结构分裂，特别是在重原子中。
- 允许跃迁的选取规则是 $\Delta l = \pm 1$，$\Delta L = 0, \pm 1$ (除 $L = 0 \to L = 0$ 外)，$\Delta J = 0, \pm 1$ (除 $J = 0 \to J = 0$ 外)，和 $\Delta S = 0$。
- 在轻原子中，适用拉塞尔-桑德斯 ($LS$) 耦合，因此 $L$、$S$ 和 $J$ 都是良量子数；在重原子中，自旋-轨道耦合占主导，$J$ 成为唯一的良量子数。
- 原子的基态项符号使用洪德规则确定；例如 He ($1s^2$) 的项符号为 $^1$S$_0$，而 C ($1s^2 2s^2 2p^2$) 的项符号为 $^3$P$_0$。
``````
:::

## The Vector Model for Adding Angular Momenta

:::{figure} images/vec_add_L.png
:alt: Vector addition of angular momenta
:width: 400px

Fig. 1 Vector addition model used to determine the quantization of total angular momentum from individual contributions.


``````{admonition} 中文翻译
:class: dropdown

图1 用于确定总角动量量子化的矢量加法模型，由各个贡献构成。
``````
:::

In many-electron atoms, each electron has both orbital and spin angular momenta. First, for simplicity, consider only the total orbital angular momentum operator:


``````{admonition} 中文翻译
:class: dropdown

在多电子原子中，每个电子都有轨道和自旋角动量。首先，为简化起见，只考虑总轨道角动量算符：
``````

$${\hat{L} = \sum\limits_{i=1}^{N} \hat{l}_i}$$

where $N$ is the number of electrons and $\hat{l}_i$ is the angular momentum operator for electron $i$. The projection operator along the $z$-axis is then:


``````{admonition} 中文翻译
:class: dropdown

其中 $N$ 是电子数，$\hat{l}_i$ 是电子 $i$ 的角动量算符。沿 $z$ 轴的投影算符则为：
``````

$${\hat{L}_z = \sum\limits_{i=1}^{N} \hat{l}_{z,i}}$$

$${M_L = \sum\limits_{i=1}^{N}m_i}$$

- $\vec{L}$ is the total orbital angular momentum.
- $\vec{l}_1, \vec{l}_2, \vec{l}_3$ are the individual angular momenta.
- $\hat{L}, \hat{l}_i$ are operators; $L, l_i$ are the corresponding quantum numbers.
- We assume a light atom and thus neglect the spin-orbit coupling.


``````{admonition} 中文翻译
:class: dropdown

- $\vec{L}$ 是总轨道角动量。
- $\vec{l}_1, \vec{l}_2, \vec{l}_3$ 是各个角动量。
- $\hat{L}, \hat{l}_i$ 是算符；$L, l_i$ 是对应的量子数。
- 我们假设是轻原子，因此忽略自旋-轨道耦合。
``````

## Total Orbital Angular Momentum

Consider an atom with two electrons having orbital angular momenta $l_1$ and $l_2$. The maximum total angular momentum is obtained when the two vectors are parallel: $L = l_1 + l_2$. When they point in opposite directions, $L = |l_1 - l_2|$. Hence the total angular momentum quantum number $L$ can take values (the "Clebsch-Gordan series"):


``````{admonition} 中文翻译
:class: dropdown

考虑一个有两个电子的原子，其轨道角动量为 $l_1$ 和 $l_2$。当两个矢量平行时得到的最大总角动量为 $L = l_1 + l_2$。当它们指向相反方向时，$L = |l_1 - l_2|$。因此总角动量量子数 $L$ 可以取的值（即“高斯-高登列”）：
``````

:::{important} **Quantization of orbital angular momentum $L$**

$${L = l_1 + l_2,\, l_1 + l_2 - 1,\, \ldots,\, \left|l_1 - l_2\right|}$$

:::

For example, if we have two electrons in $p$-orbitals, this gives $L = 2, 1$, or $0$. Furthermore, for $L = 2$ we can have $M_L = +2, +1, 0, -1, -2$; for $L = 1$, $M_L = +1, 0, -1$; and for $L = 0$, $M_L = 0$.


``````{admonition} 中文翻译
:class: dropdown

例如，如果我们有两个电子在 $p$ 轨道中，这给出了 $L = 2, 1$, 或 $0$。此外，对于 $L = 2$，我们可以有 $M_L = +2, +1, 0, -1, -2$；对于 $L = 1$，$M_L = +1, 0, -1$；对于 $L = 0$，$M_L = 0$。
``````

It is instructive to check that we have the same number of states in both representations (the uncoupled versus the coupled representation). In the uncoupled representation there are $3^2 = 9$ states (3 $p$-orbitals and 2 electrons), and in the coupled representation $5 + 3 + 1 = 9$.


``````{admonition} 中文翻译
:class: dropdown

检查一下我们在两种表示法（非耦合与耦合表示）中状态的数量相同是很有启发性的。在非耦合表示中有$3^2 = 9$个状态（3个$p$轨道和2个电子），在耦合表示中有$5 + 3 + 1 = 9$。
``````

Usually the closed-shell inner-core electrons are not included in the consideration, as they do not contribute to the end result.


``````{admonition} 中文翻译
:class: dropdown

通常不考虑闭壳层内核电子，因为它们不影响最终结果。
``````

## Total Spin Angular Momentum

The total spin angular momentum operator for a many-electron atom is:


``````{admonition} 中文翻译
:class: dropdown

多电子原子的总自旋角动量算符为：
``````

$${\hat{S} = \sum\limits_{i=1}^{N}\hat{s}_i}$$

and the $z$-component of the total spin operator is:


``````{admonition} 中文翻译
:class: dropdown

总自旋算符的 $z$ 分量为：
``````

$${\hat{S}_z = \sum\limits_{i=1}^{N}\hat{s}_{z,i}}$$

Here $\hat{s}_i$ and $\hat{s}_{z,i}$ refer to the spin angular momenta of the individual electrons. The total quantum number $M_S$ is:


``````{admonition} 中文翻译
:class: dropdown

这里 $\hat{s}_i$ 和 $\hat{s}_{z,i}$ 指代各个电子的自旋角动量。总量子数 $M_S$ 为：
``````

$${M_S = \sum\limits_{i=1}^{N} m_{s,i}}$$

This value ranges from $-S$ to $S$, and the total quantum number $S$ is given by:


``````{admonition} 中文翻译
:class: dropdown

该值范围从 $-S$ 到 $S$，总量子数 $S$ 由下式给出：
``````

:::{important} **Quantization of spin angular momentum $S$**

$${S = s_1 + s_2,\, s_1 + s_2 - 1,\, \ldots,\, \left|s_1 - s_2\right|}$$

:::

For example, for two electrons, $S = 1$ (a "triplet state") or $S = 0$ (a "singlet state").


``````{admonition} 中文翻译
:class: dropdown

例如，对于两个电子，$S = 1$（"三重态"）或 $S = 0$（"单重态"）。
``````

## Total Angular Momentum (Combined Orbital and Spin)

The total angular momentum operator $\hat{J}$ is the vector sum of $\hat{L}$ and $\hat{S}$:


``````{admonition} 中文翻译
:class: dropdown

总角动量算符 $\hat{J}$ 是 $\hat{L}$ 和 $\hat{S}$ 的矢量和：
``````

$${\vec{\hat{J}} = \vec{\hat{L}} + \vec{\hat{S}}}$$

$${\hat{J}_z = \hat{L}_z + \hat{S}_z}$$

The total quantum number $J$, with its corresponding magnetic quantum number $M_J$, is given by:


``````{admonition} 中文翻译
:class: dropdown

总量子数 $J$ 及其对应的磁量子数 $M_J$ 由下式给出：
``````

:::{important} **Quantization of total angular momentum $J$**

$${J = L + S,\, L + S - 1,\, \ldots,\, \left|L - S\right|}$$

$${M_J = M_L + M_S}$$
:::

The coupling scheme above is called the $LS$ coupling or **Russell-Saunders coupling**.


``````{admonition} 中文翻译
:class: dropdown

上述耦合方案称为 $LS$ 耦合或**罗素-桑德斯耦合**。
``````

This approach is only approximate when spin-orbit coupling is included in the Hamiltonian. Spin-orbit interaction arises from relativistic effects; here we simply think of it as coupling the orbital and spin angular momenta with some given magnitude (the "spin-orbit coupling constant").


``````{admonition} 中文翻译
:class: dropdown

当哈密顿算符中包含自旋-轨道耦合时，此方法仅近似有效。自旋-轨道相互作用源于相对论效应；此处我们仅将其视为以某种幅度（即“自旋-轨道耦合常数”）将轨道角动量和自旋角动量耦合在一起。
``````

The spin-orbit effect is larger for heavier atoms. For these atoms the $LS$ coupling scheme begins to break down and only $J$ remains a good quantum number. This means, for example, that one can no longer speak about singlet and triplet electronic states. The $LS$ coupling scheme works reasonably well for the first two rows of the periodic table.


``````{admonition} 中文翻译
:class: dropdown

自旋-轨道效应对于重原子更大。对于这些原子，$LS$ 耦合方案开始失效，仅剩 $J$ 为良量子数。这意味着，例如，不再能谈论单态和 triplet 电子态。$LS$ 耦合方案对于周期表的前两行 reasonably well 起作用。
``````

## Atomic Terms and Selection Rules

:::{figure} images/possible_term.png
:alt: Possible atomic terms
:width: 400px

Fig. 2 Possible atomic terms for given electronic configurations.


``````{admonition} 中文翻译
:class: dropdown

图 2 给定电子构型可能的原子项。
``````
:::

The table above shows the various term symbols that can correspond to given electronic configurations. A term symbol contains information about the total orbital and spin angular momenta as well as the total angular momentum ($J = L + S$):


``````{admonition} 中文翻译
:class: dropdown

上表列出了给定电子构型所对应的各种项符号。项符号包含关于总轨道角动量和总自旋角动量以及总角动量 ($J = L + S$) 的信息：
``````

:::{important} **Term Symbols**

$${^{2S+1}L_J}$$

- $S$ is the total spin.
- $L$ is the total orbital angular momentum.
- $J$ is the total angular momentum.


``````{admonition} 中文翻译
:class: dropdown

- $S$ 是总自旋。
- $L$ 是总轨道角动量。
- $J$ 是总角动量。
``````
:::

Both $2S+1$ and $J$ are written as numbers, while $L$ is written as a letter: S for $L = 0$, P for $L = 1$, D for $L = 2$, and so on. The quantity $2S+1$ is the spin multiplicity (1 = singlet, 2 = doublet, 3 = triplet, ...).


``````{admonition} 中文翻译
:class: dropdown

Both $2S+1$ and $J$ are written as numbers, while $L$ is written as a letter: S for $L = 0$, P for $L = 1$, D for $L = 2$, and so on. The quantity $2S+1$ is the spin multiplicity (1 = singlet, 2 = doublet, 3 = triplet, ...).
``````

The term symbol specifies the ground-state electronic configuration exactly. Note that only the valence electrons contribute to the term symbol.


``````{admonition} 中文翻译
:class: dropdown

项符号精确指定了基态电子构型。注意只有价电子对项符号有贡献。
``````

Because of electron, electron interactions and spin-orbit coupling, we expect a splitting of energy levels that can be described by various term symbols.


``````{admonition} 中文翻译
:class: dropdown

由于电子-电子相互作用和自旋-轨道耦合，我们预期能级会发生分裂，这可以用各种项符号来描述。
``````

:::{figure} images/Overview.png
:alt: Configurations, terms, levels, states
:width: 500px

Fig. 3 Relationship of configurations, terms, levels, and states. The top row indicates the degree of approximation and type of interaction; the second row shows the group of states that are degenerate in energy; and the bottom row indicates the good quantum numbers at each level of approximation.


``````{admonition} 中文翻译
:class: dropdown

图3 配置、项、能级与态的关系。顶行表示近似程度和相互作用类型；第二行显示能量相同的态的组；底行表示每个近似水平的良好量子数。
``````
:::

:::{figure} images/Carbon_splitting.png
:alt: Term and level splitting of carbon
:width: 400px

Fig. 4 Relationship of terms and levels for carbon. Assuming a spherically symmetric electron distribution, a single energy state is allowed. Including the dependence of electron repulsion on the directions of $L$ and $S$ splits this into terms of different energy, here $^3$P, $^1$D, and $^1$S. Coupling of $L$ and $S$ further splits the terms into levels according to $J$, here $^1$S$_0$, $^1$D$_2$, $^3$P$_2$, $^3$P$_1$, and $^3$P$_0$. The separation of the levels for the $^3$P term has been multiplied by a factor of 25 to make it visible.


``````{admonition} 中文翻译
:class: dropdown

图 4 碳的能级与项的关系。假设电子分布具有球对称性，则只允许一个能级。考虑到电子排斥随 $L$ 和 $S$ 方向的依赖性，将其分裂为不同能级的项，此处为 $^3$P、$^1$D 和 $^1$S。$L$ 与 $S$ 的耦合进一步将项分裂为根据 $J$ 的各能级，此处为 $^1$S$_0$、$^1$D$_2$、$^3$P$_2$、$^3$P$_1$ 和 $^3$P$_0$。$^3$P 项的能级分离已乘以 25 倍以使其可见。
``````
:::

::::{admonition} **Example: term symbol for ground-state He**
:class: note

What is the atomic term symbol for the He atom in its ground state?


``````{admonition} 中文翻译
:class: dropdown

He 原子基态的原子项符号是什么？
``````

:::{admonition} **Solution**
:class: dropdown solution

The electron configuration of He is $1s^2$ (two electrons in the $1s$ orbital with opposite spins). First we obtain $S$. There are two possibilities: $S = 1$ (triplet) or $S = 0$ (singlet). Since we are interested in the ground state, both electrons are in the $1s$ orbital and must have opposite spins, giving a singlet state. Thus $S = 0$ and $2S + 1 = 1$. Since both electrons reside in an $s$-orbital, $l_1 = l_2 = 0$ and $L = 0$. The total momentum is $J = L + S = 0 + 0 = 0$. The term symbol is therefore $^1$S$_0$.


``````{admonition} 中文翻译
:class: dropdown

He的电子构型是 $1s^2$（两个电子在 $1s$ 轨道中，自旋相反）。首先我们得到 $S$。有两种可能性：$S = 1$（三重态）或 $S = 0$（单重态）。由于我们感兴趣的是基态，两个电子都在 $1s$ 轨道中，必须有相反的自旋，从而得到单重态。因此 $S = 0$ 且 $2S + 1 = 1$。由于两个电子都居住在 $s$ 轨道中，$l_1 = l_2 = 0$，所以 $L = 0$。总动量 $J = L + S = 0 + 0 = 0$。因此项符号为 $^1$S$_0$。
``````
:::
::::

::::{admonition} **Example: lowest-lying terms of carbon**
:class: note

What are the lowest-lying term symbols for a carbon atom?


``````{admonition} 中文翻译
:class: dropdown

碳原子最低的项符号是什么？
``````

:::{admonition} **Solution**
:class: dropdown solution

The electronic configuration for ground-state C is $1s^2 2s^2 2p^2$. To get the possible lowest-lying states, we consider only the two $p$-electrons. From the spin rule we get $S = \tfrac{1}{2} + \tfrac{1}{2} = 1$ or $S = 0$. The first case corresponds to a triplet, the second to a singlet. The total orbital angular momentum quantum numbers are $L = 2, 1, 0$, which correspond to D, P, and S terms, respectively. Because the electrons must have opposite spins when they share the same orbital, some $S$ and $L$ combinations are not allowed:


``````{admonition} 中文翻译
:class: dropdown

ground-state C 的电子构型是 $1s^2 2s^2 2p^2$。要得到可能的最低能激发态，我们只考虑两个 $p$ 电子。从自旋规则得到 $S = \tfrac{1}{2} + \tfrac{1}{2} = 1$ 或 $S = 0$。前一种情况对应三重态，后一种对应单重态。总轨道角动量量子数为 $L = 2, 1, 0$，对应 D、P 和 S 项， respectively. 由于电子在同一轨道时必须有相反的自旋，某些 $S$ 和 $L$ 组合是不允许的：
``````

1. **$L = 2$ (D term):** One state ($M_L = -2$) must have both electrons in the $p$-orbital with $m_l = -1$. These electrons must have opposite spins, so the triplet (parallel spins) is not allowed. Hence for $L = 2$ only the singlet $^1$D is possible.

2. **$L = 1$ (P term):** In principle these configurations could also be written for the singlet, but a more careful analysis shows that this is *not allowed*.

3. **$L = 0$ (S term):** Here only $M_L = 0$ is possible. Again the triplet is not possible because the spins would have to be parallel in the same orbital, so only $^1$S exists.


``````{admonition} 中文翻译
:class: dropdown

- **$L = 2$ (D 项):** 一个态 ($M_L = -2$) 必须有两个电子都在 $m_l = -1$ 的 $p$ 态中。这些电子必须有相反的自旋，因此不允许 triplet（平行自旋）。因此对于 $L = 2$ 只有单态 $^1$D 是可能的。
- **$L = 1$ (P 项)：** 原则上这些构型也可以写成单重态，但更仔细的分析表明这是*不允许的*。
- **$L = 0$ (S 项):** 此处仅可能出现 $M_L = 0$。同样，因为自旋不能平行于同一轨道，所以三重态不可能存在，仅存在 $^1$S。
``````

We conclude that the possible terms are $^1$D, $^3$P, and $^1$S. Hund's rules (below) predict that the $^3$P term is the ground state. The total angular momentum quantum number $J$ for this state may be $J = L + S = 2, 1$, or $0$. Due to spin-orbit coupling these states have different energies, and Hund's rules predict that the $J = 0$ state lies lowest. Therefore the $^3$P$_0$ state is the ground state of the carbon atom.


``````{admonition} 中文翻译
:class: dropdown

我们得出可能的项为 $^1$D、$^3$P 和 $^1$S。洪德规则（下文）预测 $^3$P 项是基态。该态的总角动量量子数 $J$ 可为 $J = L + S = 2, 1$ 或 $0$。由于自旋-轨道耦合，这些态具有不同的能量，洪德规则预测 $J = 0$ 态能量最低。因此，$^3$P$_0$ 态是碳原子的基态。
``````
:::
::::

The "$L, S$" method above is fast and convenient but does not always work and cannot show, for instance, that $^1$P does not exist. A more complete approach lists every possible electron configuration (microstate), labels each by its $M_L$ and $M_S$ values, counts how many times each $(M_L, M_S)$ combination appears, and decomposes the result into term symbols. The total number of microstates $N$ is:


``````{admonition} 中文翻译
:class: dropdown

上述的 "$L, S$" 方法很快便捷，但并不总是适用，且无法展示例如 $^1$P 不存在。一种更完整的方法是列出每一种可能的电子构型（微观状态），用 $M_L$ 和 $M_S$ 值标记每一种，统计每一种 $(M_L, M_S)$ 组合出现的次数，并将结果分解为符号。微观状态的总数 $N$ 是：
``````

$${N = \frac{(2(2l+1))!}{n!\,(2(2l+1) - n)!}}$$

where $n$ is the number of electrons and $l$ is the orbital angular momentum quantum number (1 for $p$-orbitals, 2 for $d$, and so on). Counting the $(M_L, M_S)$ combinations and decomposing them into term symbols confirms the carbon result and shows explicitly that $^1$P does not exist.


``````{admonition} 中文翻译
:class: dropdown

其中 $n$ 为电子数，$l$ 为轨道角动量量子数（$p$ 轨道为 1，$d$ 为 2，以此类推）。计算 $(M_L, M_S)$ 组合并分解为项符号，可确认碳的结果，并明确说明 $^1$P 态不存在。
``````

::::{admonition} **Exercise: term symbols of oxygen**
:class: note

Carry out the microstate-counting procedure for the oxygen atom (4 electrons distributed over the $2p$ orbitals). What are the resulting atomic term symbols?


``````{admonition} 中文翻译
:class: dropdown

对氧原子（4 个电子分布在 $2p$ 轨道上）进行微观态计数。得到的原子项符号是什么？
``````
::::

## Hund's Rules

Hund's (partly empirical) rules are:

- The term arising from the ground configuration with the **maximum multiplicity** $2S+1$ lies lowest in energy.
- For levels with the same multiplicity, the one with the **maximum value of $L$** lies lowest in energy.
- For levels with the same $S$ and $L$ but different $J$, the lowest-energy state depends on how much the subshell is filled:
  - If the subshell is **less than half-filled**, the state with the **smallest** $J$ is lowest in energy.
  - If the subshell is **more than half-filled**, the state with the **largest** $J$ is lowest in energy.


``````{admonition} 中文翻译
:class: dropdown

- 基态构型中**最大多重度** $2S+1$ 所对应的项能量最低。
- 对于多重度相同的能级，**$L$ 值最大** 的那个能量最低。
- 对于具有相同 $S$ 和 $L$ 但不同 $J$ 的能级，最低能态取决于亚层的填充程度：
- 如果亚壳层**不到半充满**，具有**最小** $J$ 的态能量最低。
- 如果亚壳层**超过半充满**，则具有**最大** $J$ 的态能量最低。
``````

:::{figure} images/term_periodic.png
:alt: Ground-state terms across the periodic table
:width: 500px

Fig. 5 Term symbols for the ground states of the elements across the periodic table.


``````{admonition} 中文翻译
:class: dropdown

图 5 元素周期表中各元素基态的项符号。
``````
:::

## Spin-Orbit Interaction

This relativistic effect can be incorporated into non-relativistic quantum mechanics by adding the following term to the Hamiltonian:


``````{admonition} 中文翻译
:class: dropdown

这种相对论效应可以通过向哈密顿量添加以下项，纳入非相对论量子力学中：
``````

$${\hat{H}_{SO} = A\,\vec{\hat{L}}\cdot \vec{\hat{S}}}$$

where $A$ is the spin-orbit coupling constant and $\hat{L}$ and $\hat{S}$ are the orbital and spin angular momentum operators.


``````{admonition} 中文翻译
:class: dropdown

其中 $A$ 是自旋-轨道耦合常数，$\hat{L}$ 和 $\hat{S}$ 分别是轨道和自旋角动量算符。
``````

The total angular momentum $J$ commutes with both $\hat{H}$ and $\hat{H}_{SO}$, so it can be specified simultaneously with the energy. We say that the quantum number $J$ remains good even when spin-orbit interaction is included, whereas $L$ and $S$ do not. The operator dot product $\hat{L}\cdot\hat{S}$ can be evaluated in terms of the quantum numbers:


``````{admonition} 中文翻译
:class: dropdown

总角动量 $J$ 与 $\hat{H}$ 和 $\hat{H}_{SO}$ 都交换，因此可以与能量同时指定。我们说量子数 $J$ 即使在自旋-轨道相互作用包含时仍然良好，而 $L$ 和 $S$ 则不然。算子点积 $\hat{L}\cdot\hat{S}$ 可以用量子数表示为：
``````

:::{important} **Spin-orbit eigenvalue**

$${\vec{\hat{L}}\cdot\vec{\hat{S}}\left|\psi_{L,S,J}\right\rangle = \frac{1}{2}\left[J(J+1)-L(L+1)-S(S+1)\right]\left|\psi_{L,S,J}\right\rangle}$$
:::

For example, in alkali atoms ($S = 1/2$, $L = 1$) the spin-orbit interaction breaks the degeneracy of the excited $^2$P state into $^2$P$_{3/2}$ and $^2$P$_{1/2}$ (with $^2$S$_{1/2}$ as the ground state).


``````{admonition} 中文翻译
:class: dropdown

例如，在碱金属原子中 ($S = 1/2$, $L = 1$) 自旋-轨道相互作用打破了激发 $^2$P 态的简并性，将其分裂为 $^2$P$_{3/2}$ 和 $^2$P$_{1/2}$（其中 $^2$S$_{1/2}$ 为基态）。
``````

## Atomic Spectra and Selection Rules

The following selection rules for photon absorption or emission in **one-electron atoms** can be derived by considering the symmetries of the initial and final state wavefunctions:


``````{admonition} 中文翻译
:class: dropdown

通过考虑初态和末态波函数的对称性，可以推导出**单电子原子**中光子吸收或发射的以下选择定则：
``````

$${\Delta n = \textnormal{unrestricted},\quad \Delta l = \pm 1,\quad \Delta m_l = +1, 0, -1}$$

where $\Delta n$ is the change in the principal quantum number, $\Delta l$ the change in orbital angular momentum, and $\Delta m_l$ the change in its projection.


``````{admonition} 中文翻译
:class: dropdown

其中 $\Delta n$ 是主量子数的变化，$\Delta l$ 是角动量的变化，$\Delta m_l$ 是其投影的变化。
``````

Qualitatively, the selection rules follow from **conservation of angular momentum**:


``````{admonition} 中文翻译
:class: dropdown

定性地讲，选择规则源于**角动量守恒**：
``````

- Photons are spin-1 particles with $m_l = +1$ (left-circularly polarized light) or $m_l = -1$ (right-circularly polarized light).
- When a photon interacts with an atom, the angular momentum may change only by $+1$ or $-1$, exactly as in the selection rules above.


``````{admonition} 中文翻译
:class: dropdown

- 光子是自旋为 1 的粒子，具有 $m_l = +1$（左旋圆偏振光）或 $m_l = -1$（右旋圆偏振光）。
- 当光子与原子相互作用时，角动量只能改变 $+1$ 或 $-1$，这与上述选择规则完全一致。
``````

### Selection Rules for Multi-Electron Atoms

:::{figure} images/term_spectra.png
:alt: Allowed transitions of helium
:width: 400px

Fig. 6 Allowed electronic transitions of the He atom, organized by term symbol.


``````{admonition} 中文翻译
:class: dropdown

图 6 氦原子允许的电子跃迁，按项符号分类。
``````
:::

1. $\Delta L = 0, \pm 1$, except that a transition from $L = 0$ to $L = 0$ does not occur.
2. $\Delta l = \pm 1$ for the electron that is being excited (or is responsible for fluorescence).
3. $\Delta J = 0, \pm 1$, except that a transition from $J = 0$ to $J = 0$ does not occur.
4. $\Delta S = 0$: the electron spin does not change in an optical transition. The opposite holds for magnetic resonance spectroscopy, which deals with changes in spin states.


``````{admonition} 中文翻译
:class: dropdown

- $\Delta L = 0, \pm 1$，但 $L = 0$ 到 $L = 0$ 的跃迁不发生。
- $\Delta l = \pm 1$ 对于被激发的电子（或负责荧光的电子）。
- $\Delta J = 0, \pm 1$，但 $J = 0$ 到 $J = 0$ 的跃迁不发生。
- $\Delta S = 0$：光谱过程中电子自旋不变。磁共振光谱相反，涉及自旋态的变化。
``````

In some exceptional cases these rules may be violated, but the resulting transitions are extremely weak ("forbidden transitions"). Because of the last rule, some excited triplet states can have very long lifetimes, since the transition to the ground singlet state is forbidden (metastable states).


``````{admonition} 中文翻译
:class: dropdown

在某些特殊情况下，这些规则可能会被违反，但产生的跃迁极弱（"禁入跃迁"）。由于最后一条规则，一些激发的三重态可以具有非常长的寿命，因为从激发三重态到基态单重态的跃迁是被禁止的（亚稳态）。
``````

## The Nature of Light, Matter Interaction

Light is electromagnetic radiation, so it has both electric and magnetic components. The oscillating electric field drives transitions in optical spectroscopy (UV/Vis, fluorescence, IR), whereas the magnetic component drives transitions in magnetic resonance spectroscopy (NMR, EPR/ESR).


``````{admonition} 中文翻译
:class: dropdown

光是电磁辐射，因此具有电场和磁场两个分量。振荡的电场驱动光谱学（UV/Vis、荧光、IR）中的跃迁，而磁场分量驱动磁共振光谱学（NMR、EPR/ESR）中的跃迁。
``````

Photon emission from an atom (for example, fluorescence) is difficult to understand with the quantum mechanical machinery developed so far. The plain Schrodinger equation predicts that excited states in atoms would have infinite lifetime in vacuum. This is not observed in practice: atoms and molecules return to the ground state by emitting a photon. This transition is caused by fluctuations of the electromagnetic field in the vacuum.


``````{admonition} 中文翻译
:class: dropdown

原子发光（例如荧光）难以用目前发展起来的量子力学机制来理解。纯粹的Schrodinger方程预测，原子激发态在真空中寿命无限。但实际上并非如此：原子和分子通过发射光子返回基态。此跃迁由真空中电磁场的波动引起。
``````

## Problems

::::{admonition} **Problem 1: Spin multiplicity of two electrons**
:class: note

Two electrons each have spin $s = \tfrac{1}{2}$. Use the spin-coupling rule to enumerate the allowed values of the total spin quantum number $S$, the corresponding spin multiplicities $2S+1$, and the allowed values of $M_S$ for each. Show that the total number of spin states is 4.


``````{admonition} 中文翻译
:class: dropdown

两个电子每个自旋 $s = \tfrac{1}{2}$。使用自旋耦合规则，列出总自旋量子数 $S$ 的允许值、对应的自旋倍性 $2S+1$，以及每种情况下 $M_S$ 的允许值。证明自旋状态总数为 4。
``````

:::{admonition} **Solution**
:class: dropdown solution

The coupling rule gives $S = s_1 + s_2, \ldots, |s_1 - s_2| = 1, 0$.


``````{admonition} 中文翻译
:class: dropdown

耦合规则给出 $S = s_1 + s_2, \ldots, |s_1 - s_2| = 1, 0$。
``````

- $S = 1$ (triplet, $2S+1 = 3$): $M_S = +1, 0, -1$, giving 3 states.
- $S = 0$ (singlet, $2S+1 = 1$): $M_S = 0$, giving 1 state.


``````{admonition} 中文翻译
:class: dropdown

- $S = 1$ (三重态, $2S+1 = 3$): $M_S = +1, 0, -1$, 共 3 个状态。
- $S = 0$ (单重态, $2S+1 = 1$): $M_S = 0$, 给出 1 个态。
``````

The total is $3 + 1 = 4$, which matches the $2^2 = 4$ states of the uncoupled representation ($\alpha\alpha$, $\alpha\beta$, $\beta\alpha$, $\beta\beta$).


``````{admonition} 中文翻译
:class: dropdown

总数为 $3 + 1 = 4$，与非耦合表示的 $2^2 = 4$ 个态（$\alpha\alpha$、$\alpha\beta$、$\beta\alpha$、$\beta\beta$）相符。
``````
:::
::::

::::{admonition} **Problem 2: Ground-state term symbol of nitrogen**
:class: note

Determine the ground-state term symbol of the nitrogen atom, whose valence configuration is $2p^3$. Apply Hund's rules in order.


``````{admonition} 中文翻译
:class: dropdown

确定氮原子的基态项符号，其价电子构型为 $2p^3$。按顺序应用洪特规则。
``````

:::{admonition} **Solution**
:class: dropdown solution

With three $p$-electrons and three $p$-orbitals, the maximum-multiplicity arrangement (Hund's first rule) puts one electron in each orbital with parallel spins:


``````{admonition} 中文翻译
:class: dropdown

对于三个 $p$-电子和三个 $p$-轨道，最大多重度排列（洪特第一规则）将每个电子放入一个轨道，自旋平行：
``````

$$M_S^{\max} = \tfrac{1}{2}+\tfrac{1}{2}+\tfrac{1}{2} = \tfrac{3}{2} \;\Rightarrow\; S = \tfrac{3}{2},\quad 2S+1 = 4.$$

With one electron in each of $m_l = +1, 0, -1$, the total $M_L = +1+0-1 = 0$, so $L = 0$ (an S term). The subshell is exactly half-filled, so the only value of $J$ is $J = L + S = \tfrac{3}{2}$. The ground-state term symbol is $^4$S$_{3/2}$.


``````{admonition} 中文翻译
:class: dropdown

每个 $m_l = +1, 0, -1$ 中各有一个电子，总 $M_L = +1+0-1 = 0$，所以 $L = 0$（一个 S 项）。亚层正好半填满，所以 $J$ 只有一个值 $J = L + S = \tfrac{3}{2}$。基态项符号是 $^4$S$_{3/2}$。
``````
:::
::::

::::{admonition} **Problem 3: Spin-orbit splitting of a $^2$P term**
:class: note

Using the eigenvalue of $\vec{\hat{L}}\cdot\vec{\hat{S}}$, compute the spin-orbit energy $A\langle\vec{\hat{L}}\cdot\vec{\hat{S}}\rangle$ for the two levels $^2$P$_{3/2}$ and $^2$P$_{1/2}$ of an alkali atom ($L=1$, $S=\tfrac{1}{2}$). Which level lies lower for a less-than-half-filled subshell?


``````{admonition} 中文翻译
:class: dropdown

利用 $\vec{\hat{L}}\cdot\vec{\hat{S}}$ 的特征值，计算碱金属 ($L=1$, $S=\tfrac{1}{2}$) $^2$P$_{3/2}$ 和 $^2$P$_{1/2}$ 两个能级的自旋轨道能量 $A\langle\vec{\hat{L}}\cdot\vec{\hat{S}}\rangle$。对于少于半满的亚层，哪一能级更低？
``````

:::{admonition} **Solution**
:class: dropdown solution

The eigenvalue is $\tfrac{1}{2}[J(J+1) - L(L+1) - S(S+1)]$ with $L(L+1) = 2$ and $S(S+1) = \tfrac{3}{4}$.


``````{admonition} 中文翻译
:class: dropdown

本征值为 $\tfrac{1}{2}[J(J+1) - L(L+1) - S(S+1)]$，其中 $L(L+1) = 2$ 且 $S(S+1) = \tfrac{3}{4}$。
``````

- $J = \tfrac{3}{2}$: $\tfrac{1}{2}\left[\tfrac{15}{4} - 2 - \tfrac{3}{4}\right] = \tfrac{1}{2}(1) = +\tfrac{1}{2}$, so $E_{SO} = +\tfrac{1}{2}A$.
- $J = \tfrac{1}{2}$: $\tfrac{1}{2}\left[\tfrac{3}{4} - 2 - \tfrac{3}{4}\right] = \tfrac{1}{2}(-2) = -1$, so $E_{SO} = -A$.


``````{admonition} 中文翻译
:class: dropdown

- $J = \tfrac{3}{2}$: $\tfrac{1}{2}\left[\tfrac{15}{4} - 2 - \tfrac{3}{4}\right] = \tfrac{1}{2}(1) = +\tfrac{1}{2}$, 因此 $E_{SO} = +\tfrac{1}{2}A$。
- $J = \tfrac{1}{2}$: $\tfrac{1}{2}\left[\tfrac{3}{4} - 2 - \tfrac{3}{4}\right] = \tfrac{1}{2}(-2) = -1$，所以 $E_{SO} = -A$。
``````

For a less-than-half-filled subshell $A > 0$, so the $J = \tfrac{1}{2}$ level lies lower, consistent with Hund's third rule (smallest $J$ lowest).


``````{admonition} 中文翻译
:class: dropdown

对于不到半充满的亚层 $A > 0$，因此 $J = \tfrac{1}{2}$ 能级位置较低，符合洪特第三规则（最小 $J$ 最低）。
``````
:::
::::

::::{admonition} **Problem 4: Coupled-uncoupled state counting for $2p^2$**
:class: note

For two equivalent $p$-electrons ($l = 1$), use the microstate formula to compute the total number of allowed microstates $N$. The allowed terms are $^1$S, $^1$D, and $^3$P. Verify that the number of states in these terms adds up to $N$.


``````{admonition} 中文翻译
:class: dropdown

对于两个等价的 $p$ 电子 ($l = 1$)，使用微态公式计算允许微态的总数 $N$。允许的项为 $^1$S，$^1$D 和 $^3$P。验证这些项中状态的数量之和是否等于 $N$。
``````
::::

::::{admonition} **Problem 5: Allowed and forbidden transitions in helium**
:class: note

Apply the multi-electron selection rules to decide which of the following helium transitions are allowed: (a) $^1$S$_0 \to {}^1$P$_1$, (b) $^1$S$_0 \to {}^3$P$_1$, (c) $^3$P$_1 \to {}^3$S$_1$, (d) $^1$S$_0 \to {}^1$S$_0$.


``````{admonition} 中文翻译
:class: dropdown

将多电子选择规则应用于决定以下氦原子跃迁是否允许：(a) $^1$S$_0 \to {}^1$P$_1$，(b) $^1$S$_0 \to {}^3$P$_1$，(c) $^3$P$_1 \to {}^3$S$_1$，(d) $^1$S$_0 \to {}^1$S$_0$。
``````
::::

::::{admonition} **Problem 6: Ground-state term symbol of oxygen**
:class: note

Determine the ground-state term symbol of the oxygen atom, valence configuration $2p^4$. Note that the subshell is more than half-filled, so Hund's third rule selects the **largest** $J$.


``````{admonition} 中文翻译
:class: dropdown

确定氧原子基态项符号，价态配置 $2p^4$。注意由于亚层多于半满，胡德第三条则选择 **最大** $J$。
``````

:::{admonition} **Solution**
:class: dropdown solution

A $2p^4$ configuration has the same terms as $2p^2$ (a "hole" picture), namely $^1$S, $^1$D, and $^3$P, so the ground term is $^3$P with $S = 1$, $L = 1$. The possible $J$ values are $J = L+S, \ldots, |L-S| = 2, 1, 0$. Because the $2p$ subshell is more than half-filled (4 of 6 electrons), Hund's third rule selects the **largest** $J$, so $J = 2$. The ground-state term symbol is $^3$P$_2$.


``````{admonition} 中文翻译
:class: dropdown

$2p^4$ 电子构型与 $2p^2$ 具有相同的项（“空穴”图像），即 $^1$S、$^1$D 和 $^3$P，因此基态项为 $^3$P，其中 $S = 1$，$L = 1$。可能的 $J$ 值为 $J = L+S, \ldots, |L-S| = 2, 1, 0$。因为 $2p$ 亚层超过半充满（6 个电子中有 4 个），洪特第三规则选择**最大**的 $J$，所以 $J = 2$。基态项符号为 $^3$P$_2$。
``````
:::
::::

:::{seealso} Chapter demos
Computational lab for this chapter: [Hartree-Fock with PySCF](../demos/11-demo-hartree-fock.md)


``````{admonition} 中文翻译
:class: dropdown

本章计算实验室：[使用 PySCF 进行 Hartree-Fock 计算](../demos/11-demo-hartree-fock.md)
``````
:::
