---
kernelspec:
  name: python3
  display_name: Python 3
---

# Perturbation Theory

:::{note} **What you will learn**

- **The big idea:** Perturbation theory attacks analytically intractable problems by splitting the Hamiltonian into an exactly solvable part $\hat{H}^0$ and a small perturbation $\hat{H}^1$. It is the quantum analog of a Taylor expansion: the key is finding the small parameter to expand in.
- **How it works:** Expand the energies and eigenfunctions as power series in a bookkeeping parameter $\lambda$, then collect terms order by order to get corrections of increasing order. In practice the first- and second-order corrections are usually enough for quantitatively accurate results.
- **The master formula:** Perturbation theory lets us write all corrections entirely in terms of the eigenfunctions and eigenvalues of the exactly solved problem, through matrix elements $H_{nk} = \langle n^0|\hat{H}^1|k^0\rangle$.
- **Where it shows up:** Hydrogen in a magnetic field, spin-orbit coupling, a shifted particle in a box, the anharmonic oscillator, and a perturbative picture of chemical bonding.


``````{admonition} 中文翻译
:class: dropdown

- **大体思路:** 微扰理论通过将哈密顿算符分解为可精确求解的部分 $\hat{H}^0$ 和小扰动 $\hat{H}^1$ 来处理解析上不可处理的问题。这量子力学上的泰勒展开类比：关键是找到可以展开的小参数。
- **它是如何工作的:** 用书签参数 $\lambda$ 展开能量和本征函数，然后逐项收集项以获得递增阶数的修正。实际上，通常只需要第一阶和第二阶的修正就能得到定量准确的结果。
- **主公式：** 微扰理论让我们完全用已解问题的本征函数和本征值，通过矩阵元 $H_{nk} = \langle n^0|\hat{H}^1|k^0\rangle$ 来表示所有修正项。
- **它出现的地方：** 氢原子在磁场中，自旋轨道耦合，位移的粒子在盒子里，非谐振子，以及化学键的扰动图。
``````
:::

## The idea behind perturbation theory

- Perturbation theory attempts to solve analytically intractable problems by identifying an exactly *solvable* part and a *small* perturbation to it.
- The method is similar in spirit to the Taylor expansion of continuous functions familiar from calculus. Just as in a Taylor expansion, the key is identifying the relatively small parameter in the problem to expand in.
- Application of perturbation theory proceeds in two steps. Step one: identify the solvable part and the perturbation. Step two: expand the energy and eigenfunctions as a series of corrections of increasing order. In practice the first- and second-order corrections to the energy are sufficient to get quantitatively accurate results.
- Perturbation theory allows us to write down expressions entirely in terms of the eigenfunctions and eigenvalues of the exactly solved problem.


``````{admonition} 中文翻译
:class: dropdown

- 微扰理论试图通过识别一个精确*可解*的部分和一个*微小*的微扰来解析地求解难以处理的问题。
- 该方法的精神与微积分中连续函数的泰勒展开相似。就像泰勒展开一样，关键是找到问题中相对较小的参数进行展开。
- 微扰理论的应用分两步进行。第一步：确定可解部分和微扰。第二步：将能量和本征函数展开为递增阶数的修正级数。实际中，能量的第一阶和第二阶修正通常足以得到定量准确的结果。
- 微扰理论允许我们完全用精确求解问题的本征函数和本征值来写出表达式。
``````

:::{figure} images/perturb1.png
:alt: perturbation of energy levels
:width: 300px

Fig.1 Perturbation theory quantifies how much the energy levels shift when a small deviation is added to an exactly solvable Hamiltonian. For many problems that are impossible to solve exactly, one can still identify part of the Hamiltonian as exactly solvable, $\hat{H}^0$, with the rest treated as a perturbation.


``````{admonition} 中文翻译
:class: dropdown

图 1 扰动理论量化了当精确可解哈密顿量加上一个小的偏差时，能级偏移了多少。对于许多无法精确求解的问题，仍然可以将哈密顿量的一部分视为可解的 $\hat{H}^0$，其余部分视为摄动。
``````
:::

## Time-independent perturbations

- We start with a Hamiltonian $\hat{H}^0$ for some exactly solvable problem, such as a particle in a box, a harmonic oscillator, and so on:


``````{admonition} 中文翻译
:class: dropdown

- 我们从某个可精确求解问题的哈密顿量 $\hat{H}^0$ 开始，例如一维势箱中的粒子、谐振子等：
``````

$$
\hat{H}^0 \mid n^0\rangle=E^0_n \mid n^0\rangle
$$

- The $0$ superscript indicates the exactly solvable Hamiltonian, its eigenfunctions, and its eigenvalues. The state $\mid n^0\rangle$ is the eigenfunction corresponding to the $n$-th eigenvalue $E^0_n$.
- Consider a problem whose Hamiltonian is similar to an exactly solvable one, differing only by a small perturbation $\hat{H}^1$. "Small" means the eigenvalue shifts of the two systems are small relative to the level spacing.
- The parameter $\lambda$ turns the perturbation on ($\lambda=1$) and off ($\lambda=0$):


``````{admonition} 中文翻译
:class: dropdown

- 上标 $0$ 表示可精确求解的哈密顿量、其本征函数及其本征值。态 $\mid n^0\rangle$ 是对应于第 $n$ 个本征值 $E^0_n$ 的本征函数。
- 考虑一个其哈密顿类似于可精确求解的一个，仅仅由一个小的扰动 $\hat{H}^1$ 组成。"小" 是指这两个系统的能级位移相对于能级间距都很小。
- 参数 $\lambda$ 控制微扰的开启 ($\lambda=1$) 和关闭 ($\lambda=0$)：
``````

$$
\hat{H}=\hat{H}^0+\lambda {\hat{H}^1}
$$

- The objective of perturbation theory is to solve the new problem, expressing everything in terms of the eigenvalues and eigenfunctions of the exactly solvable problem:


``````{admonition} 中文翻译
:class: dropdown

- 微扰理论的目标是求解新问题，将一切表示为完全可解问题的特征值和特征函数：
``````

$$
\hat{H}\mid n\rangle =E_n \mid n\rangle
$$

### It is just like a Taylor expansion

- We assume that the eigenvalues and eigenfunctions can be expanded in a power series in the parameter $\lambda$, which is set to $1$ in the end:


``````{admonition} 中文翻译
:class: dropdown

- 我们假设本征值和本征函数可以按参数 $\lambda$ 的幂级数展开，最后令 $\lambda$ 等于 $1$：
``````

$$
E_n ={\color{green}E^0_n}+{\color{red}\lambda E^1_n}+{\color{blue}\lambda^2 E^2_n}+...
$$

$$
\mid n\rangle = {\color{green}\mid n^0\rangle}+{\color{red} \lambda\mid n^1\rangle}+{\color{blue} \lambda^2\mid n^2\rangle} ...
$$

- Plugging the expansions into $\hat{H}\mid n\rangle =E_n \mid n\rangle$ gives an expression with various powers of $\lambda$. The next step is to expand the brackets and group terms according to $\lambda^0$, $\lambda^1$, and $\lambda^2$:


``````{admonition} 中文翻译
:class: dropdown

- 将展开式代入 $\hat{H}\mid n\rangle =E_n \mid n\rangle$ 得到一个包含各种 $\lambda$ 次幂的表达式。下一步是展开括号并按 $\lambda^0$，$\lambda^1$，和 $\lambda^2$ 对项进行分组：
``````

$$
\Big({\color{green}\hat{H}^0}+{\color{red}\lambda \hat{H}^1} \Big)\Big({\color{green}\mid n^0\rangle}+{\color{red}\lambda\mid n^1\rangle} +{\color{blue}\lambda^2\mid n^2\rangle}\Big)  = \Big({\color{green}E^0_n}+{\color{red}\lambda E^1_n}+{\color{blue}\lambda^2 E^2_n}\Big) \Big({\color{green}\mid n^0\rangle}+{\color{red}\lambda\mid n^1\rangle}+{\color{blue}\lambda^2\mid n^2\rangle}\Big)
$$

### Perturbation equations of order 0, 1, and 2

- Opening the brackets and collecting different orders of $\lambda$, we get the zeroth-, first-, and second-order perturbation equations:


``````{admonition} 中文翻译
:class: dropdown

- 展开括号并合并不同阶的 $\lambda$，我们得到零阶、一阶和二阶微扰方程：
``````

$$
\color{green}{\hat{H}^0\mid n^0\rangle = E^0_n\mid n^0 \rangle}
$$

$$
\color{red}{\hat{H}^0\mid n^1\rangle +\hat{H}^1\mid n^0\rangle = E^0_n\mid n^1 \rangle+E^1_n\mid n^0 \rangle}
$$

$$
\color{blue}{\hat{H}^0\mid n^2\rangle+\hat{H}^1\mid n^1\rangle = E^0_n\mid n^2 \rangle + E^1_n\mid n^1 \rangle+E^2_n\mid n^0 \rangle}
$$

- Note how **the sum of the superscript indices determines** the order of the perturbation expansion.
- The **zeroth order is just the exact solution.**
- The **Hamiltonian only has a first-order term**, while the eigenfunctions and eigenvalues are expanded to infinitely many terms. Usually going to second order is enough for most problems.


``````{admonition} 中文翻译
:class: dropdown

- 注意**上标指数之和决定了**微扰展开的阶数。
- **零阶近似就是精确解。**
- 哈密顿量**仅包含一阶项**，而本征函数和本征值则展开为无限多项。通常二阶近似足以解决大多数问题。
``````

## Computing perturbation corrections to energy levels

:::{important} **Perturbation approximation to energies**

$$
{E_n = \color{green}{E^0_n} + \color{red}{H_{nn}} + \color{blue}{\sum_{k \neq n} \frac{\mid H_{nk}\mid^2}{E^0_n-E^0_k}}}
$$

- $n$ and $k$ are quantum numbers running from ground to excited states, $n=0,1,2,\dots$
- **Matrix elements of the perturbation:**


``````{admonition} 中文翻译
:class: dropdown

- $n$ 和 $k$ 是从基态到激发态的量子数，$n=0,1,2,\dots$
- **扰动的矩阵元:**
``````

$$\color{red} H_{nk}=\langle n^0\mid \hat{H}^1\mid k^0\rangle$$

$$\color{blue} H_{nn}=\langle n^0\mid \hat{H}^1\mid n^0\rangle$$
:::

:::{tip} **Example: first- and second-order corrections to the ground state**
:class: dropdown

- The **first-order correction to the ground state** requires computing the **diagonal** matrix element only:


``````{admonition} 中文翻译
:class: dropdown

- **基态的一阶修正** 仅需计算 **对角** 矩阵元：
``````

$$E_0^{(1)}  = \langle 0|\hat{H}^1|0\rangle$$

- The **second-order correction to the ground state** requires the **off-diagonal** elements $H_{0k}$, where $n=0$ and $k$ runs over all excited states:


``````{admonition} 中文翻译
:class: dropdown

- 基态的**二阶修正**需要**非对角**元素 $H_{0k}$，其中 $n=0$ 且 $k$ 遍历所有激发态：
``````

$$E_0^{(2)} = {\sum_{k \neq 0} \frac{\mid H_{0k}\mid^2}{E^0_0-E^0_k}}$$

- The denominator of the second-order term involves the difference between the energy of the given state $E_n$ and all other states $E_k$ (the summation index).
- **Key insight:** if the matrix elements are of comparable magnitude, neighboring energy levels make the larger contributions to the perturbation expression, because their small energy denominators amplify the term.


``````{admonition} 中文翻译
:class: dropdown

- 二阶项的分母涉及给定态能量 $E_n$ 与所有其他态能量 $E_k$（求和指标）的差值。
- **关键洞察：** 如果矩阵元幅值相当，相邻能级对扰动表达式的贡献更大，因为它们的小能量分母放大了该项。
``````
:::

## Derivations of the first- and second-order corrections

:::{admonition} **Deriving the first-order energy correction $E^1_n$**
:class: dropdown

**Fixing the normalization.** If the zeroth-order eigenfunctions are normalized, the unperturbed eigenfunction is orthogonal to all higher-order corrections:


``````{admonition} 中文翻译
:class: dropdown

**确定归一化。** 若零阶本征函数已归一化，则未受扰动的本征函数与所有高阶修正项正交：
``````

$$
\langle n^0 \mid n^0 \rangle=1
$$

$$
\langle n^0\mid n\rangle = \langle n^0\mid n^0\rangle + \lambda\langle n^0\mid n^1\rangle=1+0+...
$$

$$
\langle n^0 \mid n^{k} \rangle=0, \quad k=1,2,\dots
$$

**Using the orthogonality.** Start from the first-order perturbation equation:


``````{admonition} 中文翻译
:class: dropdown

**利用正交性。** 从一阶微扰方程出发：
``````

$$
{\hat{H}^0\mid n^1\rangle +\hat{H}^1\mid n^0\rangle = E^0_n\mid n^1 \rangle+E^1_n\mid n^0 \rangle}
$$

Multiply by $\langle n^0 \mid$ and use the Hermitian property of the Hamiltonian:


``````{admonition} 中文翻译
:class: dropdown

乘以 $\langle n^0 \mid$ 并利用哈密顿量的厄米性质：
``````

$$
{{\langle n^0} \mid \hat{H}^0\mid n^1\rangle +{\langle n^0} \mid  \hat{H}^1\mid n^0\rangle = E^0_n{\langle n^0} \mid n^1 \rangle+E^1_n {\langle n^0} \mid n^0 \rangle}
$$

The first terms on each side cancel by orthogonality, since $\langle n^0 \mid \hat{H}^0\mid n^1\rangle = E^0_n \langle n^0 \mid n^1\rangle = 0$.


``````{admonition} 中文翻译
:class: dropdown

由于正交性，等式两边的第一项相互抵消，因为 $\langle n^0 \mid \hat{H}^0\mid n^1\rangle = E^0_n \langle n^0 \mid n^1\rangle = 0$。
``````

**First-order correction.** We obtain the central result of perturbation theory, the first-order correction to the energy:


``````{admonition} 中文翻译
:class: dropdown

**一阶修正。** 我们得到了微扰理论的核心结果，即能量的一阶修正：
``````

$$
\color{red}{E_n^1 = \langle n^0 \mid \hat{H}^1\mid n^0 \rangle}
$$

$$
\boxed{E_n=\color{green}{E^0_n}+\color{red}{E^1_n}=\color{green}{E^0_n}+\color{red}{\langle n^0 \mid \hat{H}^1\mid n^0 \rangle}}
$$

- This expression looks like an expectation value but is different: the eigenfunctions of $\hat{H}^0$ sandwich the perturbation $\hat{H}^1$. The two Hamiltonians in general do not share eigenfunctions.


``````{admonition} 中文翻译
:class: dropdown

- 此表达式看起来像期望值但不同：$\hat{H}^0$ 的本征函数夹持扰动 $\hat{H}^1$。两个哈密顿算子一般不共享本征函数。
``````
:::

:::{admonition} **Deriving the first-order correction to the eigenfunction $\mid n^1 \rangle$**
:class: dropdown

We express the unknown first-order eigenfunction $\mid n^1 \rangle$ in terms of the known eigenfunctions $\mid k^0 \rangle$, which form a complete basis set because $\hat{H}^0$ is Hermitian:


``````{admonition} 中文翻译
:class: dropdown

我们用已知的本征函数 $\mid k^0 \rangle$ 来表示未知的一阶本征函数 $\mid n^1 \rangle$，它们形成一个完整的基集，因为 $\hat{H}^0$ 是埃尔米特算子：
``````

$$
\mid n^1 \rangle = \sum_{k \neq n} c_{k} \mid k^0 \rangle
$$

The coefficients are $c_k =\langle k^0 \mid n^1 \rangle$. By orthogonality, the $k=n$ term drops out, since $c_n=\langle n^0 \mid n^1 \rangle=0$; hence the $k\neq n$ condition in the sum.


``````{admonition} 中文翻译
:class: dropdown

系数为 $c_k =\langle k^0 \mid n^1 \rangle$。由正交性可知，$k=n$ 项消去，因为 $c_n=\langle n^0 \mid n^1 \rangle=0$；因此求和中的条件为 $k\neq n$。
``````

Insert the expansion into the first-order equation and take the dot product with $\langle k^0 \mid$:


``````{admonition} 中文翻译
:class: dropdown

将展开式代入一阶方程并与 $\langle k^0 \mid$ 做点积：
``````

$$
{\hat{H}^0\mid n^1\rangle +\hat{H}^1\mid n^0\rangle = E^0_n\mid n^1 \rangle+E^1_n\mid n^0 \rangle}
$$

$$
c_k E^0_k + \langle k^0 \mid \hat{H}^1 \mid n^0\rangle  = c_k E^0_n
$$

$$
c_k = \frac{ \langle k^0 \mid \hat{H}^1 \mid n^0\rangle}{E^0_n-E^0_k}=\frac{H_{nk}}{E^0_n-E^0_k}
$$

$$
\boxed{\mid n^1 \rangle = \sum_{k \neq n} c_{k} \mid k^0 \rangle = \sum_{k \neq n} \frac{H_{nk}}{E^0_n-E^0_k} \mid k^0 \rangle}
$$

**Matrix element notation.** We have introduced the convenient notation $H_{nk} = \langle k^0 \mid \hat{H}^1 \mid n^0\rangle$. Note that the Hamiltonian inside the matrix element is always the perturbation part.


``````{admonition} 中文翻译
:class: dropdown

**矩阵元记号。** 我们引入了方便的记号 $H_{nk} = \langle k^0 \mid \hat{H}^1 \mid n^0\rangle$。请注意，矩阵元中的哈密顿算符总是微扰部分。
``````
:::

:::{admonition} **Deriving the second-order correction $E^2_n$**
:class: dropdown

$$
{\hat{H}^0\mid n^2\rangle+\hat{H}^1\mid n^1\rangle = E_n^0\mid n^2\rangle+ E^1_n\mid n^1 \rangle+E^2_n\mid n^0 \rangle}
$$

Take the dot product with $\langle n^0 \mid$:


``````{admonition} 中文翻译
:class: dropdown

与 $\langle n^0 \mid$ 做点积：
``````

$$
{{\langle n^0 \mid }\hat{H}^0 \mid n^2\rangle+{\langle n^0 \mid }\hat{H}^1\mid n^1\rangle = E^0{\langle n^0}\mid n^2\rangle+ E^1_n{\langle n^0 \mid } n^1 \rangle+E^2_n {\langle n^0}\mid n^0 \rangle}
$$

The first term on the left vanishes (Hermitian plus orthogonality), and the first two terms on the right vanish by orthogonality, leaving:


``````{admonition} 中文翻译
:class: dropdown

左边的第一项消失（厄米性加正交性），右边的前两项因正交性而消失，剩下：
``````

$$
\color{blue}{E^2_n = \langle n^0 \mid \hat{H}^1 \mid n^1 \rangle}
$$

We are not done: the expression still contains $\mid n^1 \rangle$, which we express in terms of the known solutions:


``````{admonition} 中文翻译
:class: dropdown

还没完：表达式仍包含 $\mid n^1 \rangle$，我们用已知解来表示它：
``````

$$
\color{black}{E^2_n = \langle n^0 \mid \hat{H}^1 \mid n^1 \rangle}= \sum_{k \neq n} c_k \langle n^0 \mid \hat{H}^1 \mid k^0 \rangle = \sum_{k \neq n} c_k H_{nk}
$$

$$
\color{blue}{E^2_n = \sum_{k \neq n} \frac{\mid H_{nk}\mid^2}{E^0_n-E^0_k}}
$$

$$
\boxed{E_n = \color{green}{E^0_n} + \color{red}{\langle n^0\mid \hat{H}^1\mid n^0\rangle} + \color{blue}{\sum_{k \neq n} \frac{\mid H_{nk}\mid^2}{E^0_n-E^0_k}}}
$$
:::

## Applications

:::{note} **Example 1: Second-order correction to the ground state**

Write the second-order correction explicitly for the ground state of some exactly solvable Hamiltonian $\hat{H}^0$ perturbed by $\hat{H}^1$:


``````{admonition} 中文翻译
:class: dropdown

为某个可精确求解的哈密顿量 $\hat{H}^0$ 在微扰 $\hat{H}^1$ 下的基态显式写出二阶修正：
``````

$$
E_n = E^0_n+ H_{nn} + \sum_{k \neq n} \frac{\mid H_{nk}\mid^2}{E^0_n-E^0_k}
$$

$$
E_0 =E^0_0+ H_{00} + \frac{\mid H_{01}\mid^2}{E^0_0-E^0_1}+\frac{\mid H_{02}\mid^2}{E^0_0-E^0_2}+ \frac{\mid H_{03}\mid^2}{E^0_0-E^0_3}+ ...
$$

Notice that for the ground state the second-order correction is always negative, because $\Delta E_{0k}=E_0-E_k<0$ for every excited state.


``````{admonition} 中文翻译
:class: dropdown

注意，对于基态，二阶修正总是负的，因为 $\Delta E_{0k}=E_0-E_k<0$ 对每一个激发态都成立。
``````
:::

:::{note} **Example 2: Magnetic field and spin-orbit coupling**

A hydrogen atom in a magnetic field can be viewed as the H-atom Hamiltonian plus a small perturbation from the interaction with the field:


``````{admonition} 中文翻译
:class: dropdown

磁场中的氢原子可以看作是氢原子哈密顿量加上来自与磁场相互作用的微小微扰：
``````

$$
\hat{H}=\hat{H}_0 + \frac{e}{2m_e} B \hat{L}_z =  \hat{H}_0 + \hat{H}^1
$$

Using the first-order expression, the ground-state energy shift is (with $R_H$ the Rydberg constant and $\beta_B$ the Bohr magneton):


``````{admonition} 中文翻译
:class: dropdown

使用一阶表达式，基态能量位移为（其中 $R_H$ 为里德伯常数，$\beta_B$ 为玻尔磁子）：
``````

$$
E_0=E^0_0 + \langle 0\mid \hat{H}^1 \mid 0\rangle = -\frac{R_H}{n^2}+m_l \beta_B B
$$

In a similar way, the effect of spin-orbit coupling ($LS$) is:


``````{admonition} 中文翻译
:class: dropdown

类似地，自旋-轨道耦合 ($LS$) 的效应为：
``````

$$
\hat{H} = \hat{H}_0 + A_{SO}\hat{L}\hat{S}, \qquad E=E_0+ A_{SO} \langle 0 \mid \hat{L} \hat{S}\mid 0 \rangle
$$
:::

:::{note} **Example 3: Perturbing the particle in a box**

Estimate the ground-state and first-excited-state energies, within first-order perturbation theory, of a particle in a box with an added constant potential:


``````{admonition} 中文翻译
:class: dropdown

在一阶微扰理论下，估算附加恒定势能的势箱中粒子的基态和第一激发态能量：
``````

$$
V(x) = V_0, \quad 0 \leq x \leq L
$$

This is a particle in a box perturbed by the constant potential $V_0$. The first-order correction is:


``````{admonition} 中文翻译
:class: dropdown

这是一个受常数势 $V_0$ 扰动的势箱中的粒子。一阶修正为：
``````

$$
E_n^1 = \langle n \mid V_0 \mid n \rangle = V_0 \cdot \frac{2}{L} \int^L_0 \sin^2 \frac{n\pi x}{L}dx=V_0
$$

Every level is shifted up by the same constant amount:


``````{admonition} 中文翻译
:class: dropdown

每个能级都向上移动了相同的常数量：
``````

$$
E_n = E^0_n+E^1_n \approx \frac{n^2 h^2}{8mL^2}+V_0
$$
:::

:::{note} **Example 4: Anharmonic oscillator**

The anharmonic oscillator is a harmonic oscillator plus a cubic perturbation:


``````{admonition} 中文翻译
:class: dropdown

非谐振子是谐振子加上一个三次微扰：
``````

$$
\hat{H} = \hat{K}+ \frac{kx^2}{2} +\gamma x^3 = \hat{H}_0+\gamma x^3
$$

The first-order correction vanishes by symmetry, since $x^3$ is odd and $|\psi_n|^2$ is even:


``````{admonition} 中文翻译
:class: dropdown

由于 $x^3$ 是奇函数而 $|\psi_n|^2$ 是偶函数，一阶修正因对称性而消失：
``````

$$
E_n^1 = \langle n\mid \gamma x^3 \mid n\rangle = \langle \text{even/odd} \mid \text{odd} \mid \text{even/odd}\rangle = 0
$$

The energy levels must still change, so we turn to second order. For the ground state:


``````{admonition} 中文翻译
:class: dropdown

能级仍然必须改变，因此我们转向二阶。对于基态：
``````

$$
E^2_0 =  \sum_{k \neq 0} \frac{\mid  \langle 0\mid \gamma x^3 \mid k\rangle \mid^2}{E^0_0-E^0_k} = \frac{\mid  \langle 0\mid \gamma x^3 \mid 1\rangle \mid^2}{E^0_0-E^0_1}+\frac{\mid  \langle 0\mid \gamma x^3 \mid 3\rangle \mid^2}{E^0_0-E^0_3}+ ...
$$

$$
E_0 = \frac{\hbar \omega}{2} + 0 + \frac{H^2_{01}}{\hbar \omega}+\frac{H^2_{03}}{2\hbar \omega}+ ...
$$

Only odd terms in the sum contribute. The matrix elements must be evaluated explicitly using Hermite polynomials.


``````{admonition} 中文翻译
:class: dropdown

求和中只有奇数项有贡献。矩阵元必须利用埃尔米特多项式显式计算。
``````
:::

## Problems

#### Problem 1

::::{admonition} **Problem 1: Linear perturbation of a box**
:class: note

A particle in a box of length $L$ is perturbed by the linear potential $\hat{H}^1 = \varepsilon x$. Compute the first-order energy correction $E_n^{(1)}$ for an arbitrary level $n$.


``````{admonition} 中文翻译
:class: dropdown

盒长为 $L$ 的粒子受到线性势 $\hat{H}^1 = \varepsilon x$ 的扰动。计算任意能级 $n$ 的一阶能修正 $E_n^{(1)}$。
``````

:::{admonition} **Solution:**
:class: dropdown solution

$$E_n^{(1)} = \langle n|\varepsilon x|n\rangle = \frac{2\varepsilon}{L}\int_0^L x\sin^2\frac{n\pi x}{L}\,dx = \frac{2\varepsilon}{L}\cdot\frac{L^2}{4} = \frac{\varepsilon L}{2}.$$

Every level is shifted by the same amount $\varepsilon L/2$, since the average position $\langle x\rangle = L/2$ is the same for all $n$. The level spacing is unchanged to first order.


``````{admonition} 中文翻译
:class: dropdown

每个能级都被相同的量 $\varepsilon L/2$ 移动，因为平均位置 $\langle x\rangle = L/2$ 对所有 $n$ 都相同。能级间隔在第一阶近似下保持不变。
``````
:::
::::

#### Problem 2

::::{admonition} **Problem 2: Sign of the ground-state second-order shift**
:class: note

Argue, without evaluating any integrals, that the second-order energy correction to the ground state of any system is always negative or zero.


``````{admonition} 中文翻译
:class: dropdown

不计算任何积分，论证任何体系基态的二阶能量修正总是负或零。
``````

:::{admonition} **Solution:**
:class: dropdown solution

The second-order correction is $E_0^{(2)} = \sum_{k\neq 0}\frac{|H_{0k}|^2}{E_0^0 - E_k^0}$. The numerator $|H_{0k}|^2 \ge 0$ for every term. Since the ground state is the lowest level, $E_0^0 - E_k^0 < 0$ for all $k \neq 0$. Each term is therefore negative or zero, so the sum is negative or zero. Physically, mixing in excited states always pushes the ground state down.


``````{admonition} 中文翻译
:class: dropdown

二阶修正为 $E_0^{(2)} = \sum_{k\neq 0}\frac{|H_{0k}|^2}{E_0^0 - E_k^0}$。分子符号 $|H_{0k}|^2 \ge 0$ 对于每一项。由于基态是最低能级，所以 $E_0^0 - E_k^0 < 0$ 对于所有 $k \neq 0$。因此每一项都是负数或零，所以和也是负数或零。物理上，混入激发态总是将基态推低。
``````
:::
::::

#### Problem 3

::::{admonition} **Problem 3: First-order correction vanishes for the cubic anharmonic term**
:class: note

Show that the first-order energy correction from a perturbation $\hat{H}^1 = \gamma x^3$ vanishes for every harmonic-oscillator eigenstate $|n\rangle$, and explain why the second-order correction does not.


``````{admonition} 中文翻译
:class: dropdown

证明一阶能量修正来自于扰动 $\hat{H}^1 = \gamma x^3$ 对于每一个谐振子本征态 $|n\rangle$ 都为零，并解释为什么二阶修正不为零。
``````
::::

#### Problem 4

::::{admonition} **Problem 4: Two-level perturbation**
:class: note

A two-level system has unperturbed energies $E_1^0$ and $E_2^0$ and a perturbation with the single off-diagonal element $H_{12} = H_{21} = v$ (and zero diagonal elements). Use second-order perturbation theory to write the corrected energies, then compare to the exact eigenvalues of the $2\times 2$ matrix. Under what condition does perturbation theory work well?


``````{admonition} 中文翻译
:class: dropdown

一个两级系统有未扰动能量 $E_1^0$ 和 $E_2^0$ 以及一个单一的非对角元 $H_{12} = H_{21} = v$（对角元为零）。使用二阶微扰理论写出修正后的能量，然后与 $2\times 2$ 矩阵的精确特征值进行比较。在什么条件下微扰理论效果良好？
``````
::::

#### Problem 5

::::{admonition} **Problem 5: Charged oscillator in a field**
:class: note

A charged harmonic oscillator $\hat{H}_0 = \frac{p^2}{2m} + \frac{1}{2}m\omega^2 x^2$ is placed in a uniform electric field, adding $\hat{H}^1 = -qEx$. Show that the first-order correction vanishes by symmetry, and that the exact energy shift (found by completing the square) is $-\frac{q^2E^2}{2m\omega^2}$, independent of $n$. This is one of the rare cases where perturbation theory can be checked against an exact result.


``````{admonition} 中文翻译
:class: dropdown

一个带电谐振子 $\hat{H}_0 = \frac{p^2}{2m} + \frac{1}{2}m\omega^2 x^2$ 置于均匀电场中，加上 $\hat{H}^1 = -qEx$。通过对称性论证一阶修正为零，且通过完成平方求得的精确能量位移为 $-\frac{q^2E^2}{2m\omega^2}$，与 $n$ 无关。这是微扰理论能与精确结果相比较的少见情况之一。
``````
::::
