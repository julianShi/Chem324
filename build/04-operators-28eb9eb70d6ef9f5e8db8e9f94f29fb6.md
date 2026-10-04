# Operators

:::{note} What you need to know
- For every experimental **observable** there is a **corresponding operator** in quantum mechanics.
- **Operators must be linear**, because they are derived from the Schrodinger equation, which itself is linear.
- **Operators must be Hermitian**, because only Hermitian operators produce real eigenvalues.
- **Operators must produce real eigenvalues**, because eigenvalues are the only possible values measured in experiments.
- Operator **commutators** show whether two experimental observables can be **measured simultaneously**. For example, can one simultaneously and precisely determine the position and momentum of an electron?
- Commuting operators share eigenfunctions; non-commuting operators have different eigenfunctions.


``````{admonition} 中文翻译
:class: dropdown

- 在量子力学中，每一个实验**可观测量**都有一个**对应的算符**。
- **算符必须是线性的**，因为它们源自薛定谔方程，而薛定谔方程本身是线性的。
- **算符必须是厄米的**，因为只有厄米算符才能产生实特征值。
- **算符必须产生实特征值**，因为特征值是实验中测量到的唯一可能取值。
- 算符的**对易子**表明两个实验可观测量能否被**同时测量**。例如，能否同时精确地确定一个电子的位置和动量？
- 对易的算符拥有共同的本征函数；不对易的算符具有不同的本征函数。
``````
:::


### Operators

- In quantum mechanics, **operators** represent physical observables and are denoted by a hat symbol ($\hat{}$), which indicates a mathematical operation on functions.

- For example, the momentum operator differentiates the function with respect to $x$, then multiplies the result by $-i\hbar$.


``````{admonition} 中文翻译
:class: dropdown

- 在量子力学中，**算符**代表物理可观测量，并用帽形符号（$\hat{}$）表示，它指示对函数进行的数学运算。
- 例如，动量算符先对函数关于 $x$ 求导，再将结果乘以 $-i\hbar$。
``````

  $$
  \hat{p}_x = -i\hbar\frac{d}{dx}
  $$

- The position operator simply multiplies the function by $x$.


``````{admonition} 中文翻译
:class: dropdown

- 位置算符则只是把函数乘以 $x$。
``````

  $$
  \hat{x} = x
  $$

- In quantum mechanics we use **a simple recipe to find operators**: take expressions from classical mechanics and replace position and momentum by their respective operator expressions.


``````{admonition} 中文翻译
:class: dropdown

- 在量子力学中，我们使用**一个寻找算符的简单方法**：取经典力学的表达式，并将位置和动量替换为它们各自的算符表达式。
``````


:::{admonition} **Example of operators**
:class: dropdown

- Let us take the function $e^{2x}$ as an example and see how operator notation works:


``````{admonition} 中文翻译
:class: dropdown

- 我们以函数 $e^{2x}$ 为例，看看算符记号是如何运作的：
``````

$$\frac{d^2}{dx^2} e^{2x} = 4e^{2x}$$

$$\hat{A} f =4f$$

-  Here we say that the operator $\hat{A}$ acts on the function $e^{2x}$ to produce another function, which in this case is the same function multiplied by 4.

- In general, operators can be anything placed in front of a function $f(x)$. Here are a few more examples of operators:

  - $\hat{A} = x$ multiplies the function by $x$, e.g. $\hat{A}e^{2x} = xe^{2x}$
  - $\hat{A} = -i$ multiplies the function by $-i$, e.g. $\hat{A}e^{2x} = -ie^{2x}$
  - $\hat{A} = \sqrt{\phantom{x}}$ takes the square root, e.g. $\hat{A}e^{2x} = e^{x}$
  - $\hat{A} = d/dx + x^2$ differentiates, then adds $x^2$ times the function: $\hat{A}e^{2x} = 2e^{2x}+x^2e^{2x} = (2+x^2)e^{2x}$


``````{admonition} 中文翻译
:class: dropdown

- 这里我们说算符 $\hat{A}$ 作用在函数 $e^{2x}$ 上，产生另一个函数，在本例中这个结果是原函数乘以 4。
- 一般来说，算符可以是放在函数 $f(x)$ 前面的任何东西。以下是算符的更多几个例子：
- $\hat{A} = x$ 将函数乘以 $x$，例如 $\hat{A}e^{2x} = xe^{2x}$
- $\hat{A} = -i$ 将函数乘以 $-i$，例如 $\hat{A}e^{2x} = -ie^{2x}$
- $\hat{A} = \sqrt{\phantom{x}}$ 取平方根，例如 $\hat{A}e^{2x} = e^{x}$
- $\hat{A} = d/dx + x^2$ 先求导，再加上 $x^2$ 乘以函数：$\hat{A}e^{2x} = 2e^{2x}+x^2e^{2x} = (2+x^2)e^{2x}$
``````

:::


### Linearity of Operators

- Operators in quantum mechanics are **linear**, meaning they satisfy:


``````{admonition} 中文翻译
:class: dropdown

- 量子力学中的算符是**线性的**，这意味着它们满足：
``````

$$
\hat{A}(\psi_1 + \psi_2) = \hat{A}\psi_1 + \hat{A}\psi_2
$$

$$
\hat{A}(c\psi) = c\hat{A}\psi
$$

- Here $c$ is a constant, and $\psi_1$, $\psi_2$, and $\psi$ are wavefunctions.
- $\hat{x}$, $\hat{p_x}$, and $\hat{H}$ all satisfy this property.


``````{admonition} 中文翻译
:class: dropdown

- 这里 $c$ 是常数，$\psi_1$、$\psi_2$ 和 $\psi$ 是波函数。
- $\hat{x}$、$\hat{p_x}$ 和 $\hat{H}$ 都满足这一性质。
``````



:::{admonition} **Example of linear operators**
:class: dropdown

- Which of the following would be linear operator? $\hat{A}=\frac{d}{dx}$,      $\hat{B}=\int dx$       $\hat{C}=\sqrt{}$.


- Using the rules of calculus, we know that the derivative and integral act on each term in the sum:


``````{admonition} 中文翻译
:class: dropdown

- 下列哪个是线性算符？$\hat{A}=\frac{d}{dx}$，$\hat{B}=\int dx$，$\hat{C}=\sqrt{}$。
- 利用微积分的规则，我们知道导数和积分分别作用于和式中的每一项：
``````

$$\frac{d}{dx}(c_1f_1+c_2f_2) = c_1\frac{df_1}{dx}+c_2\frac{df_2}{dx}$$

$$\int(c_1f_1+c_2f_2)dx = c_1\int f_1dx+c_2\int f_2dx$$

- For the square root, the linearity property does not hold!


``````{admonition} 中文翻译
:class: dropdown

- 对于平方根，线性性质不成立！
``````

$$\sqrt{(c_1f_1+c_2f_2)} \neq c_1\sqrt{f_1} +c_2\sqrt{f_2}$$

:::


### Commutations of operators

:::{important} **Commutator $\hat{A}$ and $\hat{B}$**

$${\left[\hat{A},\hat{B}\right]f = \left(\hat{A}\hat{B} - \hat{B}\hat{A}\right)f}$$
:::

- From linear algebra we know that the order of matrix multiplication matters and that $AB\neq BA$ for two matrices $A$ and $B$.
- Thus we also generally expect $\hat{A}\hat{B} \neq \hat{B}\hat{A}$ for any two operators.

- We can quantify the relationship between two operators by computing the **commutator**.
    - If the commutator is zero, the order of multiplication of operators or matrices can be changed.
    - If the commutator is non-zero, the order matters and cannot be changed.


``````{admonition} 中文翻译
:class: dropdown

- 从线性代数我们知道，矩阵乘法的次序很重要，对于两个矩阵 $A$ 和 $B$ 有 $AB\neq BA$。
- 因此，对于任意两个算符，我们通常也预期 $\hat{A}\hat{B} \neq \hat{B}\hat{A}$。
- 我们可以通过计算**对易子**来定量描述两个算符之间的关系。
- 如果对易子为零，则算符或矩阵相乘的次序可以交换。
- 如果对易子非零，则次序很重要，不能交换。
``````


:::{note} **Example**

Prove that operators $\hat{A} = x$ and $\hat{B} = d/dx$ do not commute (i.e., $\left[\hat{A}, \hat{B}\right] \ne 0$).


``````{admonition} 中文翻译
:class: dropdown

证明算符 $\hat{A} = x$ 和 $\hat{B} = d/dx$ 不对易（即 $\left[\hat{A}, \hat{B}\right] \ne 0$）。
``````
:::

:::{admonition} **Solution**
:class: dropdown solution

Let $f$ be an arbitrary well-behaved function. We need to calculate both $\hat{A}\hat{B}f$ and $\hat{B}\hat{A}f$:


``````{admonition} 中文翻译
:class: dropdown

设 $f$ 为任意良态函数。我们需要分别计算 $\hat{A}\hat{B}f$ 和 $\hat{B}\hat{A}f$：
``````

$$
\hat{A}\hat{B}f = xf'(x)\textnormal{ and } \hat{B}\hat{A}f = \frac{d}{dx}\left(xf(x)\right) = f(x) + xf'(x)$$
$$\left[\hat{A},\hat{B}\right]f = \hat{A}\hat{B}f - \hat{B}\hat{A}f = -f$$
$$\Rightarrow \left[\hat{A},\hat{B}\right] = -1\textnormal{ (this is non-zero and the operators do not commute)}
$$
:::

#### Simple rules for commutators

$${\left[A,A\right] = \left[A,A^n\right] = \left[A^n,A\right] = 0}$$

- This shows that an operator always commutes with itself and its powers. Now let's apply this. Would the kinetic energy operator commute with the momentum operator?


``````{admonition} 中文翻译
:class: dropdown

- 这表明一个算符总是与其自身及其幂对易。现在让我们应用这一点。动能算符与动量算符对易吗？
``````

$${\left[A,B\right] = -\left[B,A\right]}$$

- This shows that order is important in a commutator. When you swap the operators, the sign changes.


``````{admonition} 中文翻译
:class: dropdown

- 这表明在对易子中次序很重要。当你交换算符时，符号会改变。
``````


### Commutators and experimental measurements

We have seen previously that operators may not always commute (i.e., $[A, B] \ne 0$). An example of such an operator pair is position $\hat{x}$ and momentum $\hat{p}_x$:


``````{admonition} 中文翻译
:class: dropdown

我们之前已经看到，算符并不总是对易的（即 $[A, B] \ne 0$）。这样的一对算符的一个例子是位置 $\hat{x}$ 和动量 $\hat{p}_x$：
``````

$${\hat{p}_x\hat{x}\psi(x) = \hat{p}_x\left(x\psi(x)\right) = \left(\frac{\hbar}{i}\frac{d}{dx}\right)\left(x\psi(x)\right) = \frac{\hbar x}{i}\frac{d\psi(x)}{dx} + \frac{\hbar}{i}\psi(x)}$$

$${\hat{x}\hat{p}_x\psi(x) = x\left(\frac{\hbar}{i}\frac{d\psi(x)}{dx}\right)}$$

$${\Rightarrow \left[\hat{p}_x,\hat{x}\right]\psi(x) = \left(\hat{p}_x\hat{x} - \hat{x}\hat{p}_x\right)\psi(x) = \frac{\hbar}{i}\psi(x)}$$

$${\Rightarrow \left[\hat{p}_x,\hat{x}\right] = \frac{\hbar}{i}}$$

In contrast, the kinetic energy operator and the momentum operator commute:


``````{admonition} 中文翻译
:class: dropdown

相比之下，动能算符与动量算符对易：
``````

$$
{\left[\hat{T},\hat{p}_x\right] = \left[\frac{\hat{p}_x^2}{2m},\hat{p}_x\right] = \frac{p_x^3}{2m} - \frac{p_x^3}{2m} = 0}
$$

We had the uncertainty principle for the position and momentum operators:


``````{admonition} 中文翻译
:class: dropdown

我们曾有位置和动量算符的不确定性原理：
``````

$$
\Delta x\Delta p_x \ge \frac{\hbar}{2}
$$


In general, it turns out that for operators $\hat{A}$ and $\hat{B}$ that do not commute, the [uncertainty principle](http://en.wikipedia.org/wiki/Uncertainty_principle) applies in the following form:


``````{admonition} 中文翻译
:class: dropdown

一般来说，对于不对易的算符 $\hat{A}$ 和 $\hat{B}$，[不确定性原理](http://en.wikipedia.org/wiki/Uncertainty_principle)以如下形式成立：
``````

$${\Delta A\Delta B \ge \frac{1}{2}\left|\left<\left[\hat{A},\hat{B}\right]\right>\right|}$$


- Let's check this relation on the example of momentum and position operators

- Denote $\hat{A} = \hat{x}$ and $\hat{B} = \hat{p}_x$. 


``````{admonition} 中文翻译
:class: dropdown

- 让我们用动量和位置算符的例子来检验这一关系。
- 令 $\hat{A} = \hat{x}$，$\hat{B} = \hat{p}_x$。
``````

$$\frac{1}{2}\left|\left<\left[\hat{A},\hat{B}\right]\right>\right| = \frac{1}{2}\left|\left<\left[\hat{x},\hat{p}_x\right]\right>\right| = \frac{1}{2}\left|\left<\frac{\hbar}{i}\right>\right|
= \frac{1}{2}\left|\left<\psi\left|\frac{\hbar}{i}\right|\psi\right>\right| = \frac{1}{2}\left|\frac{\hbar}{i}\underbrace{\left<\psi\left|\psi\right.\right>}_{=1}\right| = \frac{\hbar}{2}$$

$$\Rightarrow \Delta x\Delta p_x \ge \frac{\hbar}{2}$$

- We find that we cannot measure precise values of position and momentum simultaneously.


``````{admonition} 中文翻译
:class: dropdown

- 我们发现无法同时精确测量位置和动量的值。
``````


### Commuting operators and simultaneous measurements

:::{important} **Commuting operators share eigenfunction**

$$[\hat{A},\hat{B}]=0$$

$$\hat{A}\phi_k = a_k \phi_k$$

$$\hat{B}\phi_k = b_k \phi_k$$

:::

:::{admonition} **Proof that commutation implies shared eigenfunctions**
:class: dropdown

- We will show that if all eigenfunctions of operators $\hat{A}$ and $\hat{B}$ are identical, then $\hat{A}$ and $\hat{B}$ commute with each other.


``````{admonition} 中文翻译
:class: dropdown

- 我们将证明，如果算符 $\hat{A}$ 和 $\hat{B}$ 的所有本征函数都相同，那么 $\hat{A}$ 和 $\hat{B}$ 彼此对易。
``````

Denote the eigenvalues of $\hat{A}$ and $\hat{B}$ by $a_i$ and $b_i$ and the common eigenfunctions by $\psi_i$. For both operators we have then:


``````{admonition} 中文翻译
:class: dropdown

用 $a_i$ 和 $b_i$ 分别表示 $\hat{A}$ 和 $\hat{B}$ 的特征值，用 $\psi_i$ 表示它们的共同本征函数。于是对这两个算符我们有：
``````

$$\hat{A}\psi_i = a_i\psi_i\textnormal{ and }\hat{B}\psi_i = b_i\psi_i$$

By using these two equations and expressing the general wavefunction $\psi$ as a linear combination of the eigenfunctions, the commutator can be evaluated as:


``````{admonition} 中文翻译
:class: dropdown

利用这两个方程，并将一般波函数 $\psi$ 表示为本征函数的线性组合，对易子可以计算如下：
``````

$$\hat{A}\hat{B}\psi = \hat{A}\left(\hat{B}\psi\right) = \hat{A}\overbrace{\left(\hat{B}\sum\limits_{i=1}^{\infty}c_i\psi_i\right)}^{\textnormal{complete basis}}
= \hat{A}\overbrace{\left(\sum\limits_{i=1}^{\infty}c_i\hat{B}\psi_i\right)}^{\hat{B}\textnormal{ linear}} = \hat{A}\overbrace{\left(\sum\limits_{i=1}^{\infty}c_ib_i\psi_i\right)}^{\textnormal{eigenfunction of }\hat{B}}$$
$$= \overbrace{\sum\limits_{i=1}^{\infty}c_ib_i\hat{A}\psi_i}^{\hat{A}\textnormal{ linear}} = \overbrace{\sum\limits_{i=1}^{\infty}c_ib_ia_i\psi_i}^{\textnormal{eigenfunction of }\hat{A}} = \overbrace{\sum\limits_{i=1}^{\infty}c_ia_ib_i\psi_i}^{a_i\textnormal{ and }b_i\textnormal{ are constants}} = \sum\limits_{i=1}^{\infty}c_ia_i\hat{B}\psi_i$$
$$= \hat{B}\sum\limits_{i=1}^{\infty}c_ia_i\psi_i = \hat{B}\sum\limits_{i=1}^{\infty}c_i\hat{A}\psi_i = \hat{B}\hat{A}\sum\limits_{i=1}^{\infty}c_i\psi_i = \hat{B}\hat{A}\psi$$
$$\Rightarrow \left[\hat{A},\hat{B}\right] = 0$$

Note that the commutation relation must apply to all well-behaved functions and not just for some given subset of functions!


``````{admonition} 中文翻译
:class: dropdown

注意，对易关系必须对所有良态函数成立，而不仅仅对某个给定的函数子集成立！
``````
:::

- If operators commute, that means we can **simultaneously measure the corresponding observables in a single experiment**.

- For instance, the kinetic energy and momentum operators commute, so we can measure momentum and kinetic energy together. But we cannot do the same for momentum and position.

- If we measure observables $A$ and $B$ described by a common eigenfunction $\phi_k$, we find the observables to be the corresponding eigenvalues $a_k$ and $b_k$.


``````{admonition} 中文翻译
:class: dropdown

- 如果算符对易，那意味着我们可以**在单个实验中同时测量相应的可观测量**。
- 例如，动能算符和动量算符对易，所以我们可以同时测量动量和动能。但对于动量和位置，我们却做不到这一点。
- 如果我们测量由共同本征函数 $\phi_k$ 描述的可观测量 $A$ 和 $B$，我们会发现这些可观测量为相应的特征值 $a_k$ 和 $b_k$。
``````



### Expectation expression

- The **expectation value** of an observable $\hat{A}$, which gives the average outcome of measurements, is computed as:


``````{admonition} 中文翻译
:class: dropdown

- 可观测量 $\hat{A}$ 的**期望值**给出测量的平均结果，其计算方式为：
``````

  $$
  \langle A \rangle = \int \psi^* \hat{A} \psi \, d\tau
  $$

- **Special Case**: If the wavefunction $\psi$ is an eigenfunction of the operator $\hat{A}$, with eigenvalue $a$:


``````{admonition} 中文翻译
:class: dropdown

- **特殊情况**：如果波函数 $\psi$ 是算符 $\hat{A}$ 的本征函数，其特征值为 $a$：
``````

  $$
  \hat{A}\psi = a\psi
  $$

  Then the expectation value simplifies to:

  $$
  \langle A \rangle = \int \psi^* a \psi \, d\tau = a \int \psi^*\psi \, d\tau = a
  $$

  Since $\int \psi^*\psi \, d\tau = 1$ (normalization), the expectation value is simply the eigenvalue $a$.


``````{admonition} 中文翻译
:class: dropdown

由于 $\int \psi^*\psi \, d\tau = 1$（归一化），期望值就是特征值 $a$。
``````



### Dirac Notation

To express quantum states and operators more compactly, we use **Dirac (bra–ket) notation**.


``````{admonition} 中文翻译
:class: dropdown

为了更简洁地表达量子态和算符，我们使用**狄拉克（左矢–右矢）记号**。
``````

* A **state** is written as a *ket*, $|\psi\rangle$, and its complex conjugate (dual) is the *bra*, $\langle\psi|$.
* The **inner product** between two states corresponds to the integral over space:


``````{admonition} 中文翻译
:class: dropdown

- 一个**态**写成一个*右矢* $|\psi\rangle$，它的复共轭（对偶）是*左矢* $\langle\psi|$。
- 两个态之间的**内积**对应于对空间的积分：
``````
  
$$
  \langle \phi | \psi \rangle = \int \phi^*(r), \psi(r), d\tau
$$

* In this notation, the **expectation value** of an operator $\hat{A}$ becomes simply:


``````{admonition} 中文翻译
:class: dropdown

- 在这种记号下，算符 $\hat{A}$ 的**期望值**就简单地变成：
``````
  
$$
  \langle A \rangle = \langle \psi | \hat{A} | \psi \rangle
$$
  
* This form is elegant and general: it applies to all quantum systems, independent of the particular representation (position, momentum, etc.).


``````{admonition} 中文翻译
:class: dropdown

- 这种形式既优雅又普遍：它适用于所有量子系统，与具体的表象（位置、动量等）无关。
``````


### Hermitian Property of Operators


- In quantum mechanics, operators often act on **complex-valued functions**, so we need a notion of “complex conjugate” that applies not just to numbers but to operators.
This leads to the concept of the **adjoint operator**.


``````{admonition} 中文翻译
:class: dropdown

- 在量子力学中，算符常常作用在**复值函数**上，因此我们需要一个不仅适用于数、也适用于算符的“复共轭”概念。
这就引出了**伴随算符**的概念。
``````

#### The Adjoint (Conjugate Transpose)

- For complex numbers we take the **complex conjugate**:
$(3 + 2i)^* = 3 - 2i$.

- For matrices or linear operators, the corresponding operation is the **adjoint**, denoted by the dagger symbol $(\dagger)$.


``````{admonition} 中文翻译
:class: dropdown

- 对于复数，我们取**复共轭**：
$(3 + 2i)^* = 3 - 2i$。
- 对于矩阵或线性算符，相应的运算是**伴随**，用匕首符号 $(\dagger)$ 表示。
``````

:::{important} **Definition of Adjoint**

* For an **operator**, the adjoint is defined through the **inner product**:


``````{admonition} 中文翻译
:class: dropdown

- 对于一个**算符**，其伴随通过**内积**来定义：
``````

$$
\langle \phi | \hat{A}\psi \rangle = \langle \hat{A}^\dagger \phi | \psi \rangle.
$$

- This means that moving an operator from one side of an inner product to the other requires taking its adjoint (and thus a complex conjugate).

* For a **matrix**, the adjoint is its **conjugate transpose**:


``````{admonition} 中文翻译
:class: dropdown

- 这意味着把一个算符从内积的一边移到另一边，需要取它的伴随（也就是取复共轭）。
- 对于一个**矩阵**，其伴随就是它的**共轭转置**：
``````

$$
A^\dagger = (A^T)^*
$$

That is, swap rows and columns, then take the complex conjugate of every entry:


``````{admonition} 中文翻译
:class: dropdown

也就是说，先交换行与列，再对每一个元素取复共轭：
``````

$$
(A^\dagger)_{jk} = A_{kj}^*.
$$


:::

In matrix element form, taking the adjoint generates different elements:


``````{admonition} 中文翻译
:class: dropdown

用矩阵元的形式表示，取伴随会产生不同的元素：
``````

$$
a_{jk} = \langle \psi_j | \hat{A} | \psi_k \rangle
\quad \Rightarrow \quad
a^*_{kj} = \langle \psi_k | \hat{A}^\dagger | \psi_j \rangle.
$$



#### Hermitian (Self-Adjoint) Operators

An operator is **Hermitian** if it equals its own adjoint:


``````{admonition} 中文翻译
:class: dropdown

如果一个算符等于它自身的伴随，则称其为**厄米**算符：
``````

$$
\hat{A} = \hat{A}^\dagger.
$$

This means the operator behaves the same way when acting on either side of the inner product.


``````{admonition} 中文翻译
:class: dropdown

这意味着该算符作用于内积的任何一边时，其行为是相同的。
``````

:::{important} **Hermitian Matrix**

$$
A = A^\dagger, \quad a_{jk} = a_{kj}^*.
$$
:::

:::{important} **Hermitian Operator**

$$
\langle \phi | \hat{A}\psi \rangle = \langle \hat{A}\phi | \psi \rangle,
\qquad \text{or equivalently,} \qquad
\langle j| \hat{A}|k\rangle = \langle k| \hat{A}|j\rangle^*.
$$

In integral form:

$$
\int \psi_j^*(x), [\hat{A}\psi_k(x)],dx
= \int \psi_k(x), [\hat{A}\psi_j(x)]^*,dx.
$$
:::



#### Why Hermitian Operators Matter


1. **Eigenvalues are real**: Observables in quantum mechanics (energy, momentum, position, etc.) are represented by **Hermitian operators**, ensuring all measurement outcomes are real numbers.


``````{admonition} 中文翻译
:class: dropdown

- **特征值是实数**：量子力学中的可观测量（能量、动量、位置等）都由**厄米算符**表示，从而保证所有测量结果都是实数。
``````

  $$
  \hat{A}|\psi\rangle = a|\psi\rangle \implies a \in \mathbb{R}.
  $$

:::{tip} **Proof of real eigenvalues**
:class: dropdown

- Let $\psi$ be an eigenfunction of $\hat{A}$ with eigenvalue $a$. Choose $\psi_j = \psi_k = \psi$. Then we can write the left-hand and right-hand sides of the Hermitian condition:


``````{admonition} 中文翻译
:class: dropdown

- 设 $\psi$ 是 $\hat{A}$ 的、特征值为 $a$ 的本征函数。取 $\psi_j = \psi_k = \psi$。那么我们可以写出厄米条件的左端和右端：
``````

$$
\int \psi^* \hat{A} \psi \, d\tau = a
$$

$$
\int \psi \left(\hat{A} \psi\right)^* \, d\tau = a^*
$$

- Since the operator is Hermitian, this leads to an equality ensuring the eigenvalues are real.


``````{admonition} 中文翻译
:class: dropdown

- 由于该算符是厄米的，由此得到一个等式，从而保证特征值是实数。
``````

$$
a = a^*
$$

:::

2. **Eigenfunctions are orthogonal**:

  $$
  \langle \psi_m | \psi_n \rangle = 0 \quad (m \ne n).
  $$

:::{tip} **Proof of orthogonal eigenfunctions**
:class: dropdown

The Hermitian property can also be used to show that eigenfunctions $\psi_j$ and $\psi_k$, corresponding to different eigenvalues $a_j$ and $a_k$ (with $a_j \neq a_k$, i.e., "non-degenerate"), are orthogonal to each other:


``````{admonition} 中文翻译
:class: dropdown

厄米性质也可以用来证明，对应于不同特征值 $a_j$ 和 $a_k$（其中 $a_j \neq a_k$，即“非简并”）的本征函数 $\psi_j$ 和 $\psi_k$ 彼此正交：
``````

$$
\textnormal{LHS: } \int \psi_j^* \hat{A} \psi_k \, d\tau = \int \psi_j^* a_k \psi_k \, d\tau = a_k \int \psi_j^* \psi_k \, d\tau
$$

$$
\textnormal{RHS: } \int \psi_k \left(\hat{A} \psi_j \right)^* \, d\tau = \int \psi_k \left(a_j \psi_j \right)^* \, d\tau = a_j \int \psi_j^* \psi_k \, d\tau
$$

- Since the operator is Hermitian, we require that LHS = RHS. This results in:


``````{admonition} 中文翻译
:class: dropdown

- 由于算符是厄米的，我们要求左端等于右端（LHS = RHS）。于是得到：
``````

$$
\left(a_k - a_j \right) \int \psi_j^* \psi_k \, d\tau = 0
$$

- If $a_j \neq a_k$, then we have:

$$
\int \psi_j^* \psi_k \, d\tau = 0
$$

- This shows that $\psi_j$ and $\psi_k$ are orthogonal.

- **Note**: If $a_j = a_k$, meaning the eigenvalues are degenerate, this result does not hold.


``````{admonition} 中文翻译
:class: dropdown

- 这表明 $\psi_j$ 和 $\psi_k$ 是正交的。
- **注意**：如果 $a_j = a_k$，即特征值是简并的，这个结论不成立。
``````

:::

:::{note} **Example of Hermitian Matrix**

Which of these matrices is Hermitian?

$\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}$, $\begin{pmatrix}
i & 0 \\
0 & 1
\end{pmatrix}$, $\begin{pmatrix}
-1 & -3i \\
3i & 8
\end{pmatrix}$, $\begin{pmatrix}
1 & 2i \\
2i & 3
\end{pmatrix}$


``````{admonition} 中文翻译
:class: dropdown

$\begin{pmatrix}
1 & 2 \\
3 & 4
\end{pmatrix}$, $\begin{pmatrix}
i & 0 \\
0 & 1
\end{pmatrix}$, $\begin{pmatrix}
-1 & -3i \\
3i & 8
\end{pmatrix}$, $\begin{pmatrix}
1 & 2i \\
2i & 3
\end{pmatrix}$
``````
:::

:::{admonition} **Solution**
:class: dropdown solution

- For the first matrix we have $a_{12}=2\neq a^{*}_{21}=3$, **non-Hermitian**
- For the second matrix $a_{11}\neq a^{*}_{11}=0$, **non-Hermitian**
- For the third matrix  $a_{12}=-3i =a^{*}_{21} = (3i)^{*}=-3i$, **Hermitian**
- For the fourth matrix  $a_{12}=2i \neq a^{*}_{21} = (2i)^{*} = -2i$, **non-Hermitian**


``````{admonition} 中文翻译
:class: dropdown

- 对于第一个矩阵，我们有 $a_{12}=2\neq a^{*}_{21}=3$，**非厄米**
- 对于第二个矩阵，$a_{11}\neq a^{*}_{11}=0$，**非厄米**
- 对于第三个矩阵，$a_{12}=-3i =a^{*}_{21} = (3i)^{*}=-3i$，**厄米**
- 对于第四个矩阵，$a_{12}=2i \neq a^{*}_{21} = (2i)^{*} = -2i$，**非厄米**
``````

:::

- Seeing that differentiation operators are Hermitian requires a little more work.

- A trick that helps is integration by parts, where the boundary term is zero because the wavefunction decays to zero at the boundaries (postulate 1, keeping probability finite).


``````{admonition} 中文翻译
:class: dropdown

- 要看出微分算符是厄米的，需要多做一些工作。
- 一个有用的技巧是分部积分，其中边界项为零，因为波函数在边界处衰减到零（公设 1，保持概率有限）。
``````

$$\int \psi_1 d\psi_2 =- \int \psi_2d\psi_1 + \psi_1\psi_2\Big|_{x_{min}}^{x_{max}} =- \int \psi_2d\psi_1$$

:::{note} **Example of Hermitian Operator**

Prove that the momentum operator (in one dimension) is Hermitian.


``````{admonition} 中文翻译
:class: dropdown

证明（一维）动量算符是厄米的。
``````
:::

:::{admonition} **Solution**
:class: dropdown solution

${\int\limits_{-\infty}^{\infty}\psi_j^*(x)\left(-i\hbar\frac{d\psi_k(x)}{dx}\right)dx} = -i\hbar\int\limits_{-\infty}^{\infty}\psi_j^*(x)\frac{d\psi_k(x)}{dx}dx = \\ \overbrace{\int\limits_{-\infty}^{\infty}\psi_k(x)\left(i\hbar\frac{d\psi_j^*(x)}{dx}\right)dx}^{{integration\, by\, parts}}$
$ = {\int\limits_{-\infty}^{\infty}\psi_k(x)\left(-i\hbar\frac{d\psi_j(x)}{dx}\right)^*dx} \Rightarrow \hat{p}_x\textnormal{ is Hermitian}$.


``````{admonition} 中文翻译
:class: dropdown

${\int\limits_{-\infty}^{\infty}\psi_j^*(x)\left(-i\hbar\frac{d\psi_k(x)}{dx}\right)dx} = -i\hbar\int\limits_{-\infty}^{\infty}\psi_j^*(x)\frac{d\psi_k(x)}{dx}dx = \\ \overbrace{\int\limits_{-\infty}^{\infty}\psi_k(x)\left(i\hbar\frac{d\psi_j^*(x)}{dx}\right)dx}^{{integration\, by\, parts}}$
$ = {\int\limits_{-\infty}^{\infty}\psi_k(x)\left(-i\hbar\frac{d\psi_j(x)}{dx}\right)^*dx} \Rightarrow \hat{p}_x\textnormal{ is Hermitian}$.
``````
:::

**Geometric Intuition** Hermitian operators are the analog of **symmetric matrices** in real vector spaces. They represent linear transformations that **do not rotate vectors into complex directions**: they only stretch or compress them along real axes.


``````{admonition} 中文翻译
:class: dropdown

**几何直觉**：厄米算符是实向量空间中**对称矩阵**的类比。它们表示的线性变换**不会把向量旋转到复方向上**：它们只沿实轴拉伸或压缩向量。
``````


### Problems

#### Problem-1: Is the $xd/dx$ operator Hermitian?

Check whether the operator $\hat{A} = xd/dx$ is Hermitian.


``````{admonition} 中文翻译
:class: dropdown

检验算符 $\hat{A} = xd/dx$ 是否为厄米算符。
``````

- You can test whether the following condition holds:


``````{admonition} 中文翻译
:class: dropdown

- 你可以检验以下条件是否成立：
``````

$$
\int_{a}^{b} \psi_1^*(x) \left( x \frac{d}{dx} \psi_2(x) \right) \, dx = \int_{a}^{b} \left( x \frac{d}{dx} \psi_1(x) \right)^* \psi_2(x) \, dx
$$

- Note how complex conjugation applies to an expression with an operator inside.
- But since our operator contains no imaginary numbers, complex conjugation only applies to the wavefunction.


``````{admonition} 中文翻译
:class: dropdown

- 注意复共轭如何作用于内部含有算符的表达式。
- 但由于我们的算符不包含虚数，复共轭只作用于波函数。
``````


:::{note} **Solution**
:class: dropdown


**Step 1: Left-hand side**

The left-hand side is:

$$
\int_{a}^{b} \psi_1^*(x) \left( x \frac{d}{dx} \psi_2(x) \right) \, dx
$$

**Step 2: Integration by parts**

We apply integration by parts to simplify this expression. Using the product rule for differentiation, we get:


``````{admonition} 中文翻译
:class: dropdown

我们应用分部积分来简化这个表达式。利用微分的乘积法则，我们得到：
``````

$$
\int_{a}^{b} \psi_1^*(x) \left( x \frac{d}{dx} \psi_2(x) \right) \, dx = \left[ x \psi_1^*(x) \psi_2(x) \right]_{a}^{b} - \int_{a}^{b} \frac{d}{dx} \left( x \psi_1^*(x) \right) \psi_2(x) \, dx
$$

The boundary term $\left[ x \psi_1^*(x) \psi_2(x) \right]_{a}^{b}$ can be discarded if the wavefunctions vanish at the boundaries (such as in the case of bound states in a box).


``````{admonition} 中文翻译
:class: dropdown

如果波函数在边界处为零（例如盒子中的束缚态情况），边界项 $\left[ x \psi_1^*(x) \psi_2(x) \right]_{a}^{b}$ 可以舍去。
``````

Now, for the remaining integral, we apply the derivative to the product $x \psi_1^*(x)$:


``````{admonition} 中文翻译
:class: dropdown

现在，对于剩下的积分，我们把导数作用到乘积 $x \psi_1^*(x)$ 上：
``````

$$
\int_{a}^{b} \frac{d}{dx} \left( x \psi_1^*(x) \right) \psi_2(x) \, dx = \int_{a}^{b} \left( \psi_1^*(x) + x \frac{d}{dx} \psi_1^*(x) \right) \psi_2(x) \, dx
$$

Thus, the left-hand side becomes:

$$
\int_{a}^{b} \psi_1^*(x) \psi_2(x) \, dx + \int_{a}^{b} x \frac{d}{dx} \psi_1^*(x) \psi_2(x) \, dx
$$

**Step 3: Right-hand side**

The right-hand side is:

$$
\int_{a}^{b} \left( x \frac{d}{dx} \psi_1^*(x) \right) \psi_2(x) \, dx
$$

**Step 4: Comparison**

Now, we compare the two expressions. The left-hand side contains the extra term:


``````{admonition} 中文翻译
:class: dropdown

现在，我们比较这两个表达式。左端含有一个额外的项：
``````

$$
\int_{a}^{b} \psi_1^*(x) \psi_2(x) \, dx
$$

which is not present in the right-hand side. This means:


``````{admonition} 中文翻译
:class: dropdown

这一项在右端中并不存在。这意味着：
``````

$$
\int_{a}^{b} \psi_1^*(x) \left( x \frac{d}{dx} \psi_2(x) \right) \, dx \neq \int_{a}^{b} \left( x \frac{d}{dx} \psi_1^*(x) \right) \psi_2(x) \, dx
$$

- Since the two sides are not equal, we conclude that the operator $x \frac{d}{dx}$ **is non-Hermitian.**


``````{admonition} 中文翻译
:class: dropdown

- 由于两端不相等，我们得出结论：算符 $x \frac{d}{dx}$ **是非厄米的**。
``````
:::

#### Problem-2: Is the $d^2/dx^2$ operator Hermitian?

- You can test whether the following condition holds:


``````{admonition} 中文翻译
:class: dropdown

- 你可以检验以下条件是否成立：
``````

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \psi_2(x)\left( \frac{d^2}{dx^2} \psi_1(x) \right)^*  \, dx
$$

- Note how complex conjugation applies to an expression with an operator inside. But since our operator contains no imaginary numbers, it will only apply to the wavefunction.


``````{admonition} 中文翻译
:class: dropdown

- 注意复共轭如何作用于内部含有算符的表达式。但由于我们的算符不包含虚数，它只会作用于波函数。
``````


:::{note} **Solution**
:class: dropdown

To show that the operator $\hat{A} = \frac{d^2}{dx^2}$ is Hermitian, we need to check whether the following condition holds:


``````{admonition} 中文翻译
:class: dropdown

为了证明算符 $\hat{A} = \frac{d^2}{dx^2}$ 是厄米的，我们需要检验以下条件是否成立：
``````

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \left( \frac{d^2}{dx^2} \psi_1(x) \right)^* \psi_2(x) \, dx
$$

### Step 1: Left-hand side

The left-hand side is:

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx
$$

### Step 2: Integration by parts

We apply integration by parts twice. First, applying integration by parts to the term $\psi_1^*(x) \frac{d^2}{dx^2} \psi_2(x)$, we get:


``````{admonition} 中文翻译
:class: dropdown

我们应用两次分部积分。首先，对项 $\psi_1^*(x) \frac{d^2}{dx^2} \psi_2(x)$ 应用分部积分，我们得到：
``````

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \left[ \psi_1^*(x) \frac{d}{dx} \psi_2(x) \right]_{a}^{b} - \int_{a}^{b} \frac{d}{dx} \psi_1^*(x) \frac{d}{dx} \psi_2(x) \, dx
$$

The boundary term $\left[ \psi_1^*(x) \frac{d}{dx} \psi_2(x) \right]_{a}^{b}$ can be discarded if the wavefunctions vanish at the boundaries (as for bound states in a box).


``````{admonition} 中文翻译
:class: dropdown

如果波函数在边界处为零（如盒子中的束缚态），边界项 $\left[ \psi_1^*(x) \frac{d}{dx} \psi_2(x) \right]_{a}^{b}$ 可以舍去。
``````

We now apply integration by parts again to the remaining term:


``````{admonition} 中文翻译
:class: dropdown

我们现在对剩余的项再次应用分部积分：
``````

$$
-\int_{a}^{b} \frac{d}{dx} \psi_1^*(x) \frac{d}{dx} \psi_2(x) \, dx = \left[ \frac{d}{dx} \psi_1^*(x) \psi_2(x) \right]_{a}^{b} - \int_{a}^{b} \frac{d^2}{dx^2} \psi_1^*(x) \psi_2(x) \, dx
$$

Again, the boundary term $\left[ \frac{d}{dx} \psi_1^*(x) \psi_2(x) \right]_{a}^{b} $ vanishes if the wavefunctions vanish at the boundaries. This leaves us with:


``````{admonition} 中文翻译
:class: dropdown

同样，如果波函数在边界处为零，边界项 $\left[ \frac{d}{dx} \psi_1^*(x) \psi_2(x) \right]_{a}^{b} $ 会消失。这样我们得到：
``````

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \left( \frac{d^2}{dx^2} \psi_1^*(x) \right) \psi_2(x) \, dx
$$

**Step 3: Conclusion**

Since the two sides are equal, we conclude that the operator $\frac{d^2}{dx^2}$ is Hermitian:


``````{admonition} 中文翻译
:class: dropdown

由于两端相等，我们得出结论：算符 $\frac{d^2}{dx^2}$ 是厄米的：
``````

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \left( \frac{d^2}{dx^2} \psi_1(x) \right)^* \psi_2(x) \, dx
$$

:::


#### Problem-3: Is the $id^2/dx^2$ operator Hermitian?

- You can test whether the following condition holds:


``````{admonition} 中文翻译
:class: dropdown

- 你可以检验以下条件是否成立：
``````

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \psi_2(x)\left( \frac{d^2}{dx^2} \psi_1(x) \right)^*  \, dx
$$

:::{note} **Solution**
:class: dropdown

From the last problem we learned that the following condition holds, which makes the second derivative operator $d^2/dx^2$ Hermitian:


``````{admonition} 中文翻译
:class: dropdown

从上一题我们得知以下条件成立，它使得二阶导数算符 $d^2/dx^2$ 成为厄米算符：
``````

$$
\int_{a}^{b} \psi_1^*(x) \left( \frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \psi_2(x)\left( \frac{d^2}{dx^2} \psi_1^*(x) \right)  \, dx
$$

- Now if we have $id^2/dx^2$, the complex conjugate part will produce a minus sign, which breaks the Hermitian equality:


``````{admonition} 中文翻译
:class: dropdown

- 现在如果我们有 $id^2/dx^2$，复共轭部分会产生一个负号，从而破坏了厄米等式：
``````

$$
\int_{a}^{b} \psi_1^*(x) \left( i\frac{d^2}{dx^2} \psi_2(x) \right) \, dx = \int_{a}^{b} \psi_2(x)\left( i\frac{d^2}{dx^2} \psi_1(x) \right)^*  \, dx = -\int_{a}^{b} \psi_2(x)\left( i\frac{d^2}{dx^2} \psi_1(x)^* \right)
$$

:::

#### Problem-4: Identify Hermitian Matrices

$$
A = \begin{pmatrix}
1 & 2 \\
2 & 3
\end{pmatrix}
$$

$$
B = \begin{pmatrix}
i & 1 \\
-1 & -i
\end{pmatrix}
$$

$$
C = \begin{pmatrix}
2 & i \\
-i & 2
\end{pmatrix}
$$

:::{note} **Solution**
:class: dropdown

**A Matrix**

To check if a matrix is Hermitian, it must satisfy the condition $A = A^\dagger$, where $A^\dagger$ is the conjugate transpose of $A$. Since this matrix has real entries, the conjugate transpose is just the transpose.


``````{admonition} 中文翻译
:class: dropdown

要检验一个矩阵是否为厄米矩阵，它必须满足条件 $A = A^\dagger$，其中 $A^\dagger$ 是 $A$ 的共轭转置。由于这个矩阵的元素都是实数，其共轭转置就是转置。
``````

The transpose of $A$ is:

$
A^\dagger = \begin{pmatrix}
1 & 2 \\
2 & 3
\end{pmatrix}
$


``````{admonition} 中文翻译
:class: dropdown

$
A^\dagger = \begin{pmatrix}
1 & 2 \\
2 & 3
\end{pmatrix}
$
``````

Since $A = A^\dagger$, matrix $A$ is **Hermitian**.


``````{admonition} 中文翻译
:class: dropdown

由于 $A = A^\dagger$，矩阵 $A$ 是**厄米矩阵**。
``````

**B Matrix**
Now, let's compute the conjugate transpose of $B$. We first take the transpose and then take the complex conjugate of each entry:


``````{admonition} 中文翻译
:class: dropdown

**矩阵 B**
现在，让我们计算 $B$ 的共轭转置。我们先取转置，再对每个元素取复共轭：
``````

$$
B^\dagger = \begin{pmatrix}
-i & -1 \\
1 & i
\end{pmatrix}
$$

Clearly, $B \neq B^\dagger$, so matrix $B$ is **not Hermitian**.


``````{admonition} 中文翻译
:class: dropdown

显然，$B \neq B^\dagger$，所以矩阵 $B$ **不是厄米矩阵**。
``````

**C Matrix**

The conjugate transpose of $C$ is:

$$
C^\dagger = \begin{pmatrix}
2 & -i \\
i & 2
\end{pmatrix}
$$

Since $C = C^\dagger$, matrix $C$ is **Hermitian**.


``````{admonition} 中文翻译
:class: dropdown

由于 $C = C^\dagger$，矩阵 $C$ 是**厄米矩阵**。
``````

:::

#### Problem-5 Momentum Matrix

Show how the momentum operator looks in matrix form using a finite-dimensional example where you evaluate the wavefunction on 4 points, which will correspond to a $4 \times 4$ matrix.


``````{admonition} 中文翻译
:class: dropdown

用一个有限维的例子展示动量算符的矩阵形式，即在 4 个点上计算波函数的值，这将对应一个 $4 \times 4$ 的矩阵。
``````

:::{note} **Solution**
:class: dropdown

- We can represent the momentum operator $\hat{p} = -i \hbar \frac{d}{dx}$ in a discrete basis, such as using a position basis. In this case, the matrix elements of the momentum operator can be approximated using finite differences.

- For simplicity, let's assume we are working in a discrete system, where we approximate the derivative $\frac{d}{dx}$ with finite differences. The finite difference approximation for the derivative at point $x_n$ is:


``````{admonition} 中文翻译
:class: dropdown

- 我们可以在离散基（例如位置基）中表示动量算符 $\hat{p} = -i \hbar \frac{d}{dx}$。在这种情况下，动量算符的矩阵元可以用有限差分来近似。
- 为简单起见，假设我们在一个离散系统中工作，用有限差分来近似导数 $\frac{d}{dx}$。在点 $x_n$ 处导数的有限差分近似为：
``````

$$
\frac{d \psi(x)}{dx} \approx \frac{\psi(x_{n+1}) - \psi(x_{n-1})}{2 \Delta x}
$$

- where $\Delta x$ is the spacing between the discrete points.

- The corresponding momentum operator matrix in this finite-dimensional space can be written as a skew-symmetric matrix that captures this finite difference behavior.

- Here is an example of a $4 \times 4$ momentum operator matrix $P$, assuming $\hbar = 1$ for simplicity:


``````{admonition} 中文翻译
:class: dropdown

- 其中 $\Delta x$ 是离散点之间的间距。
- 在这个有限维空间中，相应的动量算符矩阵可以写成一个反对称矩阵，它体现了这种有限差分行为。
- 这里是一个 $4 \times 4$ 动量算符矩阵 $P$ 的例子，为简单起见假设 $\hbar = 1$：
``````

$$
P = \frac{i}{2 \Delta x} \begin{pmatrix}
0 & -1 & 0 & 1 \\
1 & 0 & -1 & 0 \\
0 & 1 & 0 & -1 \\
-1 & 0 & 1 & 0
\end{pmatrix}
$$

**Explanation:**
- The non-diagonal entries correspond to the finite difference approximation of the derivative.
- The factor of $\frac{i}{2 \Delta x}$ ensures that the momentum operator reflects the correct dimensionality.
- The matrix is anti-Hermitian (i.e., $P^\dagger = -P$), as expected for the momentum operator.

- This $4 \times 4$ matrix represents the momentum operator in a discrete system with 4 grid points. The matrix elements link neighboring points, reflecting the nature of the derivative approximation.


``````{admonition} 中文翻译
:class: dropdown

- 非对角元对应于导数的有限差分近似。
- 因子 $\frac{i}{2 \Delta x}$ 确保动量算符体现出正确的量纲。
- 该矩阵是反厄米的（即 $P^\dagger = -P$），这符合动量算符的预期。
- 这个 $4 \times 4$ 矩阵表示具有 4 个格点的离散系统中的动量算符。这些矩阵元连接相邻的点，反映了导数近似的性质。
``````
:::

#### Problem-6: Taking the square of an operator

Consider the operator $ \hat{A} = x \frac{d}{dx} $. Find $ \hat{A}^2 $, i.e., $ \hat{A}(\hat{A}f(x)) $, and apply it to an arbitrary function $ f(x) $.


``````{admonition} 中文翻译
:class: dropdown

考虑算符 $ \hat{A} = x \frac{d}{dx} $。求 $ \hat{A}^2 $，即 $ \hat{A}(\hat{A}f(x)) $，并将其作用于任意函数 $ f(x) $。
``````

:::{admonition} **Solution**
:class: dropdown solution

First, apply $ \hat{A} f(x) = x \frac{d}{dx} f(x) $:


``````{admonition} 中文翻译
:class: dropdown

首先，应用 $ \hat{A} f(x) = x \frac{d}{dx} f(x) $：
``````

$$
\hat{A} f(x) = x \frac{df}{dx}
$$

Now, apply $ \hat{A} $ again to the result:


``````{admonition} 中文翻译
:class: dropdown

现在，把 $ \hat{A} $ 再次作用于这个结果：
``````

$$
\hat{A}(\hat{A} f(x)) = \hat{A} \left( x \frac{df}{dx} \right) = x \frac{d}{dx} \left( x \frac{df}{dx} \right)
$$

Using the product rule:

$$
\frac{d}{dx} \left( x \frac{df}{dx} \right) = \frac{df}{dx} + x \frac{d^2 f}{dx^2}
$$

Thus:

$$
\hat{A}^2 f(x) = x \left( \frac{df}{dx} + x \frac{d^2 f}{dx^2} \right) = x \frac{df}{dx} + x^2 \frac{d^2 f}{dx^2}
$$

:::

#### Problem-7: Verifying an eigenfunction and its eigenvalue

Consider the operator $ \hat{B} = -i\hbar \frac{d}{dx} $ (momentum operator). Verify that $ f(x) = e^{ikx} $ is an eigenfunction of $ \hat{B} $, and find the corresponding eigenvalue.


``````{admonition} 中文翻译
:class: dropdown

考虑算符 $ \hat{B} = -i\hbar \frac{d}{dx} $（动量算符）。验证 $ f(x) = e^{ikx} $ 是 $ \hat{B} $ 的本征函数，并求出相应的特征值。
``````

:::{admonition} **Solution**
:class: dropdown solution

Apply $ \hat{B} $ to $ f(x) = e^{ikx} $:


``````{admonition} 中文翻译
:class: dropdown

把 $ \hat{B} $ 作用于 $ f(x) = e^{ikx} $：
``````

$$
\hat{B} f(x) = -i\hbar \frac{d}{dx} e^{ikx}
$$

The derivative of $ e^{ikx} $ is:

$$
\frac{d}{dx} e^{ikx} = ik e^{ikx}
$$

Thus:

$$
\hat{B} f(x) = -i\hbar \cdot ik e^{ikx} = \hbar k e^{ikx}
$$

Since $ \hat{B} f(x) = \hbar k f(x) $, $ f(x) = e^{ikx} $ is an eigenfunction of $ \hat{B} $ with eigenvalue $ \hbar k $.


``````{admonition} 中文翻译
:class: dropdown

由于 $ \hat{B} f(x) = \hbar k f(x) $，$ f(x) = e^{ikx} $ 是 $ \hat{B} $ 的本征函数，特征值为 $ \hbar k $。
``````

:::

#### Problem-8: Linearity and eigenfunction testing

Consider the operator $ \hat{D} = x \frac{d}{dx} $. Show whether this operator is linear and check if $ f(x) = x^n $ is an eigenfunction of $ \hat{D} $.


``````{admonition} 中文翻译
:class: dropdown

考虑算符 $ \hat{D} = x \frac{d}{dx} $。说明这个算符是否为线性算符，并检验 $ f(x) = x^n $ 是否为 $ \hat{D} $ 的本征函数。
``````

:::{admonition} **Solution**
:class: dropdown solution

First, test linearity by applying $ \hat{D} $ to $ \alpha f(x) + \beta g(x) $:


``````{admonition} 中文翻译
:class: dropdown

首先，通过把 $ \hat{D} $ 作用于 $ \alpha f(x) + \beta g(x) $ 来检验线性：
``````

$$
\hat{D}(\alpha f(x) + \beta g(x)) = x \frac{d}{dx} (\alpha f(x) + \beta g(x)) = \alpha x \frac{df}{dx} + \beta x \frac{dg}{dx}
$$

This is $ \alpha \hat{D} f(x) + \beta \hat{D} g(x) $, so $ \hat{D} $ is linear.


``````{admonition} 中文翻译
:class: dropdown

这正是 $ \alpha \hat{D} f(x) + \beta \hat{D} g(x) $，所以 $ \hat{D} $ 是线性的。
``````

Now, apply $ \hat{D} $ to $ f(x) = x^n $:


``````{admonition} 中文翻译
:class: dropdown

现在，把 $ \hat{D} $ 作用于 $ f(x) = x^n $：
``````

$$
\hat{D} f(x) = x \frac{d}{dx} x^n = x \cdot n x^{n-1} = n x^n
$$

Since the result is proportional to $ f(x) = x^n $, $ f(x) = x^n $ is an eigenfunction of $ \hat{D} $ with eigenvalue $ n $.


``````{admonition} 中文翻译
:class: dropdown

由于结果与 $ f(x) = x^n $ 成正比，$ f(x) = x^n $ 是 $ \hat{D} $ 的本征函数，特征值为 $ n $。
``````

:::
