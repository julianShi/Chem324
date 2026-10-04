# Eigenvalues and Expectation Values

:::{note} **What you need to know**


- Mastering the abstract mathematical formalism brings **simplicity, unity, and clarity** to the relationships in quantum mechanics.
- Key concepts like **basis sets, orthogonality, and linear superpositions** form the logical foundation of quantum mechanics.
- **Dirac notation** frees you from the limitations of explicit coordinate representations, which can obscure the underlying physics.
- **Eigenvalues** correspond to the only observable quantities measured in experiments.
- Quantum states, represented as linear superpositions of the eigenfunctions of an operator $\hat{A}$, yield different eigenvalues of $\hat{A}$, with probabilities given by the **square of the coefficients** in the superposition.
- The expectation value $\langle \psi |\hat{A}|\psi \rangle$, when expressed in terms of a linear superposition of eigenfunctions, simplifies to a **probability-weighted sum of eigenvalues**.
- Phenomena like **Schrödinger's cat** and the **double slit experiment** are explained through the concept of quantum superposition involving orthogonal states.


``````{admonition} 中文翻译
:class: dropdown

- 掌握这套抽象的数学形式体系，能为量子力学中的各种关系带来**简洁性、统一性与清晰性**。
- **基组 (basis set)、正交性与线性叠加**等关键概念构成了量子力学的逻辑基础。
- **狄拉克符号 (Dirac notation)**把你从显式坐标表示的局限中解放出来，因为后者往往掩盖了背后的物理图像。
- **特征值 (eigenvalue)**对应的是实验中所能测量的唯一可观测量。
- 量子态可以表示为某个算符 $\hat{A}$ 的本征函数的线性叠加，它会给出 $\hat{A}$ 的不同特征值，而相应的概率由叠加中**系数的平方**决定。
- 期望值 (expectation value) $\langle \psi |\hat{A}|\psi \rangle$ 若用本征函数的线性叠加来表达，可以化简为**特征值的概率加权和**。
- **薛定谔的猫**和**双缝实验**这类现象，都可以借助涉及正交态的量子叠加概念来解释。
``````

:::

### Reminder: Eigenfunction-eigenvalue problem


$${\hat{A}\psi_n = A_n\psi_n}$$

- This is an eigenvalue problem whose solution yields $n = 1,2,3,...$ eigenfunctions $\psi_n$ and the eigenvalues $E_i$. Depending on the boundary conditions there can be a finite or infinite number of solutions. 

``````{note}
**原文勘误 EN-01** ｜ 本行把算符 $\hat{A}$ 的本征值问题与 $E_i$ 混用。$\hat{A}$ 的特征值应记作 $A_n$；$E_n$ 是哈密顿算符 $\hat{H}$ 的特征值，此处应为 $A_i$。
``````




``````{admonition} 中文翻译
:class: dropdown

- 这是一个特征值问题，其解给出 $n = 1,2,3,...$ 的本征函数 $\psi_n$ 以及特征值 $E_i$。根据边界条件的不同，解的个数可以是有限的，也可以是无限的。
``````

:::{note} **Example: find eigenvalues and eigenfunctions of momentum operator**

What are the eigenfunctions and eigenvalues of the operator $\hat{p_x} = -i\hbar d/dx$?


``````{admonition} 中文翻译
:class: dropdown

算符 $\hat{p_x} = -i\hbar d/dx$ 的本征函数和特征值分别是什么？
``````
:::

:::{admonition} **Solution**
:class: dropdown solution

$$\hat{p} f = p f $$

$$-i\hbar \frac{df}{dx} = p$$

Let us use the only trick we know when solving ODEs, $f=e^{kx}$


``````{admonition} 中文翻译
:class: dropdown

让我们用解常微分方程时唯一会的那一招，$f=e^{kx}$
``````

$$-i\hbar k = p\rightarrow k=\frac{ip}{\hbar}$$

$$f = e^{ipx/\hbar}$$

- Periodic plane waves are the eigenfunctions of momentum!


``````{admonition} 中文翻译
:class: dropdown

- 周期平面波正是动量的本征函数！
``````

:::

**For operators written in matrix form**

- In applied numerical work, operators are converted into matrices and one solves the eigenvalue-eigenvector problem of finding eigenvectors $v$ and eigenvalues $\lambda$. 
- For a matrix with $N$ dimensions there can be at most $N$ eigenvalues!


``````{admonition} 中文翻译
:class: dropdown

- 在实际数值工作中，算符会被转换成矩阵，然后求解求本征向量 $v$ 与特征值 $\lambda$ 的本征值—本征向量问题。
- 对于一个 $N$ 维矩阵，特征值最多只能有 $N$ 个！
``````

$$Av = \lambda v$$

:::{note} **Example: finding eigenvalues of a matrix**

$$\begin{pmatrix}
1 & 2 \\
2 & 4
\end{pmatrix}\begin{pmatrix}
v_1 \\
v_2
\end{pmatrix} = \lambda \begin{pmatrix}
v_1 \\
v_2
\end{pmatrix}$$
::: 

````{admonition} **Solving eigenfunction-eigenvalue problems numerically**
:class: note, dropdown

```python
import numpy as np

# Define the matrix
matrix = np.array([ [1, 2], 
                    [2, 4]   ] )

# Compute the eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(matrix)

# Display the eigenvalues and eigenvectors
eigenvalues, eigenvectors
```

````



### Eigenfunctions of Hermitian operators form complete basis set


::::{grid}
:gutter: 2

:::{grid-item-card} Integral Notation

$\int \phi^* \hat{H}\psi dx = \int \psi (\hat{H}\phi)^*dx$


``````{admonition} 中文翻译
:class: dropdown

$\int \phi^* \hat{H}\psi dx = \int \psi (\hat{H}\phi)^*dx$
``````

:::

:::{grid-item-card} Dirac Notation

$\langle \phi \mid \hat{H} \mid \psi \rangle = \langle \psi \mid \hat{H}\mid \phi \rangle^*$


``````{admonition} 中文翻译
:class: dropdown

$\langle \phi \mid \hat{H} \mid \psi \rangle = \langle \psi \mid \hat{H}\mid \phi \rangle^*$
``````

:::

::::

The three crucial consequences of the Hermitian property of operators:


``````{admonition} 中文翻译
:class: dropdown

厄米性带来的三个关键推论：
``````

- **Eigenvalues are real**: 

$$\hat{H} \mid \psi_n \rangle=E_n \mid \psi_n \rangle$$

$$E_n=E^*_n$$

- **Eigenfunctions are orthogonal** 

$$\langle \psi_n \mid  \psi_m\rangle=\delta_{nm}$$

- **Eigenfunctions form a complete basis set!**

$$\mid f\rangle = \sum_i c_i \mid \psi_i \rangle$$

- The last two properties imply that eigenfunctions of Hermitian operators play the same role for functions as unit vectors do for vectors.  
- Thus a wavefunction can be expressed in terms of the eigenfunctions of an operator that can act on the function.


``````{admonition} 中文翻译
:class: dropdown

- 后两条性质意味着：厄米算符的本征函数对函数所起的作用，正如单位向量对向量的作用。
- 因此，波函数可以用某个能够作用于该函数的算符的本征函数来展开。
``````

### Wave function as a linear superposition of eigenfunctions

- We can express a wavefunction $\mid \psi \rangle$ describing the state of a quantum object as a superposition of **the eigenfunctions of any Hermitian operator**, be it energy, momentum, position, or another operator. 


``````{admonition} 中文翻译
:class: dropdown

- 我们可以把描述量子对象状态的波函数 $\mid \psi \rangle$ 表示为**任意厄米算符的本征函数**的叠加，无论该算符是能量、动量、位置还是别的算符。
``````

$$\hat{A}\mid \phi_n \rangle = A_n \mid \phi_n \rangle$$

$$\mid \psi \rangle = \sum_n c_n \mid \phi_n \rangle $$

- Here is an example of expressing the wavefunction for a particle in a box in terms of energy eigenfunctions. 


``````{admonition} 中文翻译
:class: dropdown

- 下面举例说明如何用能量本征函数来表达盒中粒子的波函数。
``````

::::{grid}
:gutter: 2

:::{grid-item-card} Integral Notation

``````{note}
**原文勘误 EN-02（重要）** ｜ 下方两个卡片标题被写反了。标为 *Integral Notation* 的卡片内含 $\psi=\sum_n c_n \mid n\rangle$ 与 $c_n = \braket{n \mid \psi}$，这是狄拉克记号；标为 *Dirac Notation* 的卡片内含位置空间的正弦展开。以下译文已按正确对应关系排列，但**未改动任何公式**，卡片标题的原始错误保持原样。
``````



$$\psi=\sum_n c_n \mid n\rangle$$

$$c_n = \braket{n \mid \psi}$$



``````{note}
**原文勘误 EN-02 续** ｜ 本卡片标题原作 *Integral Notation*，但内容为狄拉克记号。
``````

:::

:::{grid-item-card} Dirac Notation

$$\psi(x) = \sum_n c_n \Big(\frac{2}{L}\Big )^{1/2} sin \Big (\frac{n\pi x}{L} \Big )$$

$$c_k = \Big(\frac{2}{L}\Big )^{1/2} \int sin \Big (\frac{k\pi x}{L} \Big )\psi(x) dx$$


``````{note}
**原文勘误 EN-02 续** ｜ 本卡片标题原作 *Dirac Notation*，但内容为位置空间展开式。
``````

:::

::::


### Probabilistic meaning of linear superposition

- A wavefunction can be written as a linear superposition of the eigenfunctions of any QM operator $\hat{A}$.


``````{admonition} 中文翻译
:class: dropdown

- 波函数可以写成任意量子力学算符 $\hat{A}$ 的本征函数的线性叠加。
``````

$$|\psi\rangle  = \sum_n c_n |\phi_n\rangle $$

- The squared absolute values of the coefficients $\mid c_n \mid^2$ are equal to the probabilities $p_n$ of finding the system in a state $n$ described by eigenvalue $A_n$ and eigenfunction $\mid \phi_n \rangle$ of the operator $\hat{A}$.


``````{admonition} 中文翻译
:class: dropdown

- 系数 $\mid c_n \mid^2$ 的模平方，等于在算符 $\hat{A}$ 下找到系统处于状态 $n$（该状态由特征值 $A_n$ 和本征函数 $\mid \phi_n \rangle$ 描述）的概率 $p_n$。
``````

$$p_n=\mid c_n \mid^2$$

$$\sum_n \mid c_n \mid^2 =\sum_n p_n=1$$


### Averages are probability weighted sums of eigenvalues.

- Quantum objects can exist in any superposition of states. For instance, an atom can be in a superposition of its ground and first excited states with 50% probabilities each. 

- From the normalization condition imposed on the wavefunction we see the true meaning of the coefficients in a linear superposition.


``````{admonition} 中文翻译
:class: dropdown

- 量子对象可以存在于状态的任意叠加之中。例如，一个原子可以处于基态与第一激发态的叠加，两者的概率各为 50%。
- 从对波函数施加的归一化条件可以看出，线性叠加中各系数的真正含义。
``````

$$\mid \psi \rangle=c_1 \mid 1 \rangle+c_2 \mid 2\rangle$$ 



``````{note}
**原文勘误 EN-03** ｜ 由归一化条件应得 $|c_1|^2 + |c_2|^2 = 1$，原文写作 $c_1^2 + c_2^2 = 1$，漏掉了模长竖线。概率必须非负，故此处应为模平方。
``````

$$\langle \psi \mid \psi \rangle = \Big[c^*_1\langle 1\mid +c^*_2 \langle 2\mid \Big]\Big[c_1\mid 1\rangle + c_2 \mid 2\rangle\Big] =\\ = \mid c_1 \mid^2 \langle 1 \mid 1 \rangle+(c^*_1 c_2\langle 1 \mid 2 \rangle+c_1 c^*_2\langle 2 \mid 1 \rangle)+\mid c_2\mid^2   = c_1^2+c^2_2=p_1+p_2=1$$

- The meaning of the expectation value becomes more transparent as an average over all eigenvalues obtained in the experiment. 


``````{admonition} 中文翻译
:class: dropdown

- 把期望值理解为对实验中所有可能测得特征值的平均，其含义就更加清楚了。
``````



``````{note}
**原文勘误 EN-03 续** ｜ 同上，本行的期望值推导中 $c_1^2 E_1 + c_2^2 E_2$ 应为 $|c_1|^2 E_1 + |c_2|^2 E_2$。
``````

 $$\langle E\rangle= \langle \psi \mid \hat{H}\mid \psi \rangle = \Big[c^*_1\langle 1\mid +c^*_2 \langle 2\mid \Big]\Big[c_1\hat{H}\mid 1\rangle + c_2 \hat{H}\mid 2\rangle\Big] =\Big[c^*_1\langle 1\mid +c^*_2 \langle 2\mid \Big]\Big[c_1E_1\mid 1\rangle + c_2 E_2\mid 2\rangle\Big] = \\ = c_1^2E_1+c^2_2 E_2=p_1E_1+p_2 E_2$$


:::{note} **Example**

A particle in a box is described as a superposition of the 1st and 5th states. 


``````{admonition} 中文翻译
:class: dropdown

一个盒中粒子被描述为第 1 态与第 5 态的叠加。
``````
- Write down the wavefunction in terms of the eigenfunctions of the Hamiltonian operator.
- Compute the average energy


``````{admonition} 中文翻译
:class: dropdown

- 用哈密顿算符的本征函数写出该波函数。
- 计算平均能量
``````
:::

:::{admonition} **Solution**
:class: dropdown solution

$$\psi(x)=\frac{1}{\sqrt{2}}\cdot \Big(\frac{2}{L} \Big )^{1/2}sin\frac{\pi x}{L}+\frac{1}{\sqrt{2}}\cdot \Big(\frac{2}{L} \Big )^{1/2}sin\frac{5\pi x}{L}$$ 

- This means that when we measure the energy we will obtain only two values, $E_1$ and $E_5$, with equal probabilities $p_1=p_2=(1/\sqrt{2})^2$. The average energy is given by

``````{note}
**原文勘误 EN-04（重要）** ｜ 本题说波函数是第 1 态与第 5 态的叠加，但随后的公式误写为 $p_1=p_2$ 与 $\langle E\rangle = p_1E_1+p_2E_2$，下标应为 5：即 $p_5=p_1$，$\langle E\rangle = p_1E_1+p_5E_5$。后续算式中 $5^2h^2/8mL^2$ 的数值是对的，只有下标标签写错。以下译文按原文照译，不改动公式。
``````




``````{admonition} 中文翻译
:class: dropdown

- 这意味着当我们测量能量时，只会得到两个取值：$E_1$ 和 $E_5$，且二者概率相同，$p_1=p_2=(1/\sqrt{2})^2$。平均能量为
``````

$$\langle E \rangle =p_1 E_1+p_2 E_2 = \frac{1}{2}\frac{1^2 h^2}{8mL^2}+\frac{1}{2}\frac{5^2 h^2}{8mL^2}$$
:::



:::{note} **Example**

Consider a particle in a quantum state $\psi$ that is a superposition of two eigenfunctions $\phi_1$ and $\phi_2$, with energy eigenvalues $E_1$ and $E_2$ of operator $\hat{H}$  ($E_1 \ne E_2$):


``````{admonition} 中文翻译
:class: dropdown

考虑一个处于量子态 $\psi$ 的粒子，它是两个本征函数 $\phi_1$ 与 $\phi_2$ 的线性叠加，二者对应算符 $\hat{H}$ 的能量特征值 $E_1$ 与 $E_2$（$E_1 \ne E_2$）：
``````

$$\psi = c_1\phi_1 + c_2\phi_2$$

- If one attempts to measure the energy of such a state, what will be the outcome? 
- What will be the average energy and the standard deviation in energy?


``````{admonition} 中文翻译
:class: dropdown

- 若尝试测量这样一个状态的能量，结果会是什么？
- 平均能量和能量的标准差分别是多少？
``````
:::

:::{admonition} **Solution**
:class: dropdown solution

Since $\psi$ is normalized and $\phi_1$ and $\phi_2$ are orthogonal, we have $\left|c_1\right|^2 + \left|c_2\right|^2 = 1$. The probability of measuring $E_1$ is $\left|c_1\right|^2$ and $E_2$ is $\left|c_2\right|^2$. The average energy is given by:


``````{admonition} 中文翻译
:class: dropdown

由于 $\psi$ 已归一化，且 $\phi_1$ 与 $\phi_2$ 相互正交，我们有 $\left|c_1\right|^2 + \left|c_2\right|^2 = 1$。测得 $E_1$ 的概率是 $\left|c_1\right|^2$，测得 $E_2$ 的概率是 $\left|c_2\right|^2$。平均能量为：
``````


$$\left<\hat{H}\right> = \left<\psi\left|\hat{H}\right|\psi\right> = \left|c_1\right|^2\left<\phi_1\left|\hat{H}\right|\phi_1\right> + c_1^*c_2\left<\phi_1\left|\hat{H}\right|\phi_2\right> + c_2^*c_1\left<\phi_2\left|\hat{H}\right|\phi_1\right>$$
$$ + \left|c_2\right|^2\left<\phi_2\left|\hat{H}\right|\phi_2\right> = \left|c_1\right|^2E_1 + c_1^*c_2E_2\underbrace{\left<\phi_1\left|\phi_2\right.\right>}_{= 0} + c_2^*c_1E_1\underbrace{\left<\phi_2\left|\phi_1\right.\right>}_{= 0} + \left|c_2\right|^2E_2$$
$$= \left|c_1\right|^2E_1 + \left|c_2\right|^2E_2$$


 The standard deviation is given by : $\sigma_{\hat{H}} = \sqrt{\left<\hat{H}^2\right> - \left<\hat{H}\right>^2}$. We have already calculated $\left<\hat{H}\right>$ above and need to calculate $\left<\hat{H}^2\right>$ (use the eigenvalue equation and orthogonality):


``````{admonition} 中文翻译
:class: dropdown

 标准差由下式给出：$\sigma_{\hat{H}} = \sqrt{\left<\hat{H}^2\right> - \left<\hat{H}\right>^2}$。上面我们已经算出 $\left<\hat{H}\right>$，接下来需要计算 $\left<\hat{H}^2\right>$（利用本征值方程和正交性）：
``````

$$\left<\hat{H}^2\right> = \left<\psi\left|\hat{H}^2\right|\psi\right> = \left<\psi\left|\hat{H}\right|E_1c_1\phi_1 + E_2c_2\phi_2\right> = \left<c_1\phi_1 + c_2\phi_2\left|E_1^2c_1\phi_1 + E_2^2c_2\phi_2\right.\right>$$
$$ = \left|c_1\right|^2E_1^2 + \left|c_2\right|^2E_2^2 \Rightarrow \sigma_{\hat{H}} = \sqrt{\left|c_1\right|^2E_1^2 + \left|c_2\right|^2E_2^2 - \left(\left|c_1\right|^2E_1 + \left|c_2\right|^2E_2\right)^2}$$

:::



```{marimo-config}
---
pyproject: |
  requires-python = ">=3.10"
  dependencies = [
      "sympy",
  ]
---
```

```{marimo} python
:hide-code: true

import marimo as mo
import sympy as sp
```

The computer can carry the whole calculation symbolically. Watch $\langle \hat{p}^2 \rangle$ come out of three live cells (each is editable):


``````{admonition} 中文翻译
:class: dropdown

计算机可以把整个计算过程用符号方式完成。观察 $\langle \hat{p}^2 \rangle$ 如何从三个可交互的单元格中依次算出（每个单元格都可编辑）：
``````

```{marimo} python
x, L, n, hbar = sp.symbols("x L n hbar", positive=True)
psi_n = sp.sqrt(2 / L) * sp.sin(n * sp.pi * x / L)
psi_n
```

```{marimo} python
p2_psi = -hbar**2 * sp.diff(psi_n, x, 2)
p2_psi
```

```{marimo} python
p2_avg = sp.simplify(sp.integrate(psi_n * p2_psi, (x, 0, L)))
p2_avg
```

The result $\langle p^2 \rangle = n^2 \pi^2 \hbar^2 / L^2$ is exactly $2m E_n$: all of the particle in a box energy is kinetic.


``````{admonition} 中文翻译
:class: dropdown

结果 $\langle p^2 \rangle = n^2 \pi^2 \hbar^2 / L^2$ 恰好等于 $2m E_n$：盒中粒子的全部能量都是动能。
``````

### Quantum states as linear superpositions of mutually exclusive states

$$\mid \psi \rangle = \sum_n c_n \mid \phi_n \rangle $$

- In an experiment one always obtains one of the eigenvalues (see Postulates), corresponding to $\phi_n$.

- In other words, the system described by a **superposition wavefunction "collapses" to one of the eigenfunctions** when the experiment is carried out. 


``````{admonition} 中文翻译
:class: dropdown

- 在一次实验中，人们总是得到某一个特征值（见公设），并对应于 $\phi_n$。
- 换句话说，当实验进行时，由**叠加波函数所描述的系统会“坍缩”到某一个本征函数**上。
``````

  $$\mid \psi \rangle \rightarrow \mid \phi_n \rangle$$

- In experiments one only observes different eigenvalues, with probability given by the squared coefficients $\mid c_n \mid^2$.

- The idea of a quantum system randomly collapsing into distinct and mutually exclusive states troubled many of the physicists who were at the frontiers of the development of quantum mechanics. 

- **Orthogonality of eigenfunctions** means **mutually exclusive** states. For example, the system can only be in either state 1 or state 2, but not both.


``````{admonition} 中文翻译
:class: dropdown

- 实验中只能观测到不同的特征值，其概率由系数 $\mid c_n \mid^2$ 给出。
- 量子系统会随机坍缩到彼此互斥的不同状态这一想法，让许多身处量子力学发展前沿的物理学家深感不安。
- **本征函数的正交性**意味着**互斥**的状态。例如，系统只能处于状态 1 或状态 2 之一，而不能同时处于两者。
``````

  $$\langle \phi_1 \mid \phi_2 \rangle=0$$


### Copenhagen Interpretation

- The [Copenhagen interpretation](https://en.wikipedia.org/wiki/Copenhagen_interpretation#cite_note-Siddiqui2017-1) is an expression of the meaning of [quantum mechanics](https://en.wikipedia.org/wiki/Quantum_mechanics) that was largely devised from 1925 to 1927 by [Niels Bohr](https://en.wikipedia.org/wiki/Niels_Bohr) and [Werner Heisenberg](https://en.wikipedia.org/wiki/Werner_Heisenberg). It is one of the oldest of numerous proposed [interpretations of quantum mechanics](https://en.wikipedia.org/wiki/Interpretations_of_quantum_mechanics), and remains one of the most commonly taught.

``````{note}
**原文勘误 EN-05** ｜ 哥本哈根诠释由玻尔与海森堡于 1925—1927 年间发展成型，但玻尔的贡献主要来自 1927 年的哥本哈根会议（同年他也因哥本哈根诠释获诺贝尔物理学奖）；**马克斯·玻恩**在 1926 年即引入“坍缩”一词，其贡献常被略去。本条仅为补充说明，译文未改动原句结构。
``````



- According to the Copenhagen interpretation, physical systems generally do not have definite properties prior to being measured, and quantum mechanics can only predict the probability distribution of a given measurement's possible results. 
- The act of measurement affects the system, causing the set of probabilities to reduce to only one of the possible values immediately after the measurement. This feature is known as [wave function collapse](https://en.wikipedia.org/wiki/Wave_function_collapse).


``````{admonition} 中文翻译
:class: dropdown

- [哥本哈根诠释](https://en.wikipedia.org/wiki/Copenhagen_interpretation#cite_note-Siddiqui2017-1)是对[量子力学](https://en.wikipedia.org/wiki/Quantum_mechanics)含义的一种表述，主要由[尼尔斯·玻尔](https://en.wikipedia.org/wiki/Niels_Bohr)和[维尔纳·海森堡](https://en.wikipedia.org/wiki/Werner_Heisenberg)在 1925 至 1927 年间逐步提出。它是众多[量子力学诠释](https://en.wikipedia.org/wiki/Interpretations_of_quantum_mechanics)中最早的一种，也是目前最常被讲授的诠释之一。
- 按照哥本哈根诠释，物理系统在测量之前一般并不具有确定的性质，量子力学只能预测某次测量可能结果的概率分布。
- 测量行为本身会影响系统，使得测量后这一组概率立刻坍缩到所有可能取值中的唯一一个。这一特征被称为[波函数坍缩](https://en.wikipedia.org/wiki/Wave_function_collapse)。
``````



### Quantum superposition of an atom

<html>

<iframe width="560" height="315" src="https://www.youtube.com/embed/7B1llCxVdkE" frameborder="0" allowfullscreen>
</iframe>
</html>


### Schrödinger's cat

- Schrödinger created a thought experiment to illustrate the bizarre nature of quantum superpositions, in which a quantum system such as an atom or photon can exist as a combination of multiple states corresponding to different possible outcomes. 

- The thought experiment puts a cat in a box with a single radioactive atom whose state dictates whether it decays, breaking a poison chamber in the box that kills the cat, or does not decay, leaving the cat alive. Schrödinger argued that the cat must then be thought of as simultaneously dead and alive until the experiment is done and the cat is found in one of the two states. 


``````{admonition} 中文翻译
:class: dropdown

- 薛定谔设计了一个思想实验，用以说明量子叠加的奇特本质：像原子或光子这样的量子系统，可以处于多个状态的组合之中，而每个状态对应一种可能的测量结果。
- 这个思想实验把一只猫放进盒子里，盒中有一个放射性原子，它是否衰变决定了毒药装置是否被触发：若衰变，装置释放毒气，猫被毒死；若不衰变，猫则存活。薛定谔据此认为，在实验完成、人们发现猫处于两种状态之一以前，这只猫必须被视为同时既死又活。
``````

<html>

<iframe width="560" height="315" src="https://www.youtube.com/embed/UjaAxUO6-Uw" frameborder="0" allowfullscreen>
</iframe>
</html>




