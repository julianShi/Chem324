---
kernelspec:
  name: python3
  display_name: Python 3
---

# The Helium Atom

:::{note} **What you will learn**

- **Why helium is hard:** The two-electron Schrodinger equation contains an electron, electron repulsion term $1/r_{12}$ that prevents an exact analytic solution.
- **The independent-electron approximation:** Dropping the repulsion term turns helium into two hydrogenlike atoms, giving a separable problem and a first estimate of the energy.
- **The variational principle in action:** Treating the nuclear charge $Z$ as an adjustable parameter improves the energy from above and introduces the idea of nuclear shielding.
- **How good is good enough:** We compare approximate ground-state energies against the essentially exact value of $-79.0$ eV and learn to read the error.


``````{admonition} 中文翻译
:class: dropdown

- **氦原子难以处理的原因：** 两电子薛定谔方程包含一个电子-电子排斥项 $1/r_{12}$，这阻碍了精确解析解的获得。
- **独立电子近似:** 丢弃排斥项将氦原子转化为两个氢原子样的原子，得到可分离的问题和能量的第一估计。
- **变分原理的应用:** 将核电荷 $Z$ 视为可调参数可从上方改进能量，并引入核屏蔽的概念。
- **多好才算好**：我们将近似基态能量与基本精确值 $-79.0$ eV 进行比较，并学会如何读取误差。
``````
:::

## The Helium Hamiltonian

The Schrodinger equation for the helium atom is already extremely complicated from a mathematical point of view. No analytic solution to this equation has been found. However, with certain approximations, useful results can be obtained. The Hamiltonian for the He atom can be written as:


``````{admonition} 中文翻译
:class: dropdown

从数学角度来看，氦原子的薛定谔方程已经极其复杂。人们尚未找到该方程的解析解。然而，在某些近似下，可以得到有用的结果。氦原子的哈密顿算符可以写成：
``````

$${\hat{H} = \underbrace{-\frac{\hbar^2}{2m_e}\left(\Delta_1 + \Delta_2\right)}_{\textnormal{Kinetic energy}}
\underbrace{- \frac{1}{4\pi\epsilon_0}\left(\frac{Ze^2}{r_1} + \frac{Ze^2}{r_2} \overbrace{- \frac{e^2}{r_{12}}}^{\textnormal{Tough!!}}\right)}_{\textnormal{Potential energy}}}$$

where $\Delta_1$ is the Laplacian for the coordinates of electron 1, $\Delta_2$ for electron 2, $r_1$ is the distance of electron 1 from the nucleus, $r_2$ is the distance of electron 2 from the nucleus, and $r_{12}$ is the distance between electrons 1 and 2. For the He atom $Z = 2$.


``````{admonition} 中文翻译
:class: dropdown

其中$\Delta_1$是电子1坐标的拉普拉斯算子，$\Delta_2$是电子2的，$r_1$是电子1距离核的距离，$r_2$是电子2距离核的距离，$r_{12}$是电子1和电子2之间的距离。对于He原子，$Z = 2$。
``````

The term that makes this problem unsolvable is the electron, electron repulsion $e^2/r_{12}$. It couples the two electron coordinates so that the Hamiltonian no longer separates into independent one-electron pieces.


``````{admonition} 中文翻译
:class: dropdown

使此问题无法求解的项是电-电排斥 $e^2/r_{12}$。它将两个电子坐标耦合，以至于哈密顿不再分解为独立的单电子项。
``````

## The Independent-Electron Approximation

A first approximation is to ignore the "tough" term containing $r_{12}$. In this case the Hamiltonian becomes a sum of two hydrogenlike atoms:


``````{admonition} 中文翻译
:class: dropdown

一种初步近似是忽略包含 $r_{12}$ 的“困难”项。在这种情况下，哈密顿量变为两个类氢原子之和：
``````

$${\hat{H} = \hat{H}_1 + \hat{H}_2}$$

$${\hat{H}_1 = -\frac{\hbar^2}{2m_e}\Delta_1 - \frac{Ze^2}{4\pi\epsilon_0r_1}}$$

$${\hat{H}_2 = -\frac{\hbar^2}{2m_e}\Delta_2 - \frac{Ze^2}{4\pi\epsilon_0r_2}}$$

Because the Hamiltonian is a sum of two independent parts, the Schrodinger equation separates into two equations, each a hydrogenlike atom problem:


``````{admonition} 中文翻译
:class: dropdown

因为哈密顿量是两个独立部分的和，薛定谔方程分离为两个方程，每个都是一个类氢原子问题：
``````

$${\hat{H}_1\psi(r_1) = E_1\psi(r_1)}$$

$${\hat{H}_2\psi(r_2) = E_2\psi(r_2)}$$

The total energy is the sum of $E_1$ and $E_2$, and the total wavefunction is a product of $\psi(r_1)$ and $\psi(r_2)$. Based on our previous wavefunction table for hydrogenlike atoms, we have:


``````{admonition} 中文翻译
:class: dropdown

总能量是 $E_1$ 和 $E_2$ 的和，总波函数是 $\psi(r_1)$ 和 $\psi(r_2)$ 的乘积。基于氢样本波函数表，我们有：
``````

:::{important} **Separable two-electron solution**

$${E = E_1 + E_2 = -RZ^2\left(\frac{1}{n_1^2} + \frac{1}{n_2^2}\right)}$$

$${\psi(r_1)\psi(r_2) = \frac{1}{\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}e^{-Zr_1/a_0}\frac{1}{\sqrt{\pi}}\left(\frac{Z}{a_0}\right)^{3/2}e^{-Zr_2/a_0}
= \frac{1}{\pi}\left(\frac{Z}{a_0}\right)^3e^{-Z(r_1 + r_2)/a_0}}$$

:::

For a ground-state He atom both electrons reside in the lowest-energy orbital, so the total wavefunction is


``````{admonition} 中文翻译
:class: dropdown

对于基态氦原子，两个电子都处于最低能量轨道中，因此总波函数为
``````

$$\psi(r_1,r_2) = \psi(r_1)\psi(r_2) = \psi(1)\psi(2) = 1s(1)1s(2).$$

The energy obtained from this approximation is not sufficiently accurate (it misses electron, electron repulsion) but the wavefunction can be used for qualitative analysis. The variational principle gives a systematic way to assess how good our approximation is.


``````{admonition} 中文翻译
:class: dropdown

该近似得到的能量不够精确（它漏掉了电子-电子排斥）但波函数可用于定性分析。变分原理提供了一种系统的方法来评估我们的近似有多好。
``````

:::{tip} **Comparing with the exact answer**

The exact ground-state energy has been found, after very extensive analytic and numerical calculations, to be $-79.0$ eV. Using the approximate wavefunction above to calculate the expectation value for energy yields $-74.8$ eV, so the error in energy for this wavefunction is about $5.2$ eV. Note that the approximate value is, in accordance with the variational principle, higher than the true energy.


``````{admonition} 中文翻译
:class: dropdown

精确的基态能量已通过大量的解析和数值计算找到，结果为 $-79.0$ eV。使用上述近似波函数计算能量的期望值得到 $-74.8$ eV，所以该波函数能量的误差约为 $5.2$ eV。注意，根据变分原理，近似值高于真实能量。
``````
:::

## A Better Approximation: Variational Nuclear Charge

We can take the wavefunction from the previous step and use the nuclear charge $Z$ as a variational parameter. The variational principle states that minimization of the energy expectation value with respect to $Z$ should approach the true value from above (but obviously will not reach it).


``````{admonition} 中文翻译
:class: dropdown

我们可以取上一步的波函数，并把核电荷 $Z$ 作为变分参数。变分原理指出，关于 $Z$ 最小化能量期望值应该从上方逼近真实值（但显然不会达到它）。
``````

By judging the energy, we can say that this new wavefunction is better than the previous one. The obtained value of $Z$ is less than the true $Z$ ($=2$). This can be understood in terms of electrons shielding the nucleus from each other and hence giving a reduced effective nuclear charge.


``````{admonition} 中文翻译
:class: dropdown

通过判断能量，我们可以说这个新的波函数比之前的更好。得到的 $Z$ 值小于真实的 $Z$ ($=2$)。这可以用电子相互屏蔽核的角度来理解，从而给出了一个减小的有效核电荷。
``````

If this trial wavefunction is used in calculating the energy expectation value, we get:


``````{admonition} 中文翻译
:class: dropdown

若用此试探波函数计算能量期望值，可得：
``````

$${E = \langle\psi |\hat{H}|\psi\rangle = \cdots = \left[ Z^2 - \frac{27Z}{8}\right]\frac{e^2}{4\pi\epsilon_0a_0}}$$

In order to minimize the energy we differentiate it with respect to $Z$ and set the result to zero (an extremum point; here it is clear that this point is a minimum):


``````{admonition} 中文翻译
:class: dropdown

为最小化能量，我们对 $Z$ 求导并将结果设为零（极值点；此处显然该点为最小值）：
``````

$${\frac{dE}{dZ} = \left(2Z - \frac{27}{8}\right)\frac{e^2}{4\pi\epsilon_0a_0} = 0}$$

:::{important} **Optimal effective charge for helium**

$${Z = \frac{27}{16} \approx 1.7, \qquad E \approx -77.5 \textnormal{ eV}}$$

(compared with $-74.8$ eV for $Z = 2$ and the exact $-79.0$ eV).


``````{admonition} 中文翻译
:class: dropdown

(与 $Z = 2$ 时的 $-74.8$ eV 和精确值 $-79.0$ eV 相比)。
``````
:::

This result could be improved by adding more terms and variables to the trial wavefunction. For example, higher hydrogenlike orbitals with appropriate variational coefficients would yield a much better result.


``````{admonition} 中文翻译
:class: dropdown

通过向试波函数中添加更多项和变量，可以改进此结果。例如，带有适当变分系数的更高氢原子轨道将得到更好的结果。
``````

Another type of approximate method is based on **perturbation theory**, which would typically treat the electron, electron repulsion as an additional (small) perturbation to the independent-electron case above.


``````{admonition} 中文翻译
:class: dropdown

另一种近似方法基于**微扰论**，它通常将电-电排斥作为在上述独立电子情形之外的一个（较小）微扰来处理。
``````

:::{tip} **The lesson of helium**

Even the simplest two-electron atom has no closed-form solution. Two themes that recur throughout multi-electron quantum chemistry already appear here: (1) we build approximate wavefunctions from hydrogenlike orbitals, and (2) we use the variational principle to systematically improve them. The reduced effective charge $Z \approx 1.7$ is our first quantitative encounter with **shielding**, which the next pages develop into a full picture of multi-electron atoms.


``````{admonition} 中文翻译
:class: dropdown

即使是最简单的两电子原子也没有解析解。多电子量子化学中反复出现的两个主题已在此出现：(1) 我们从氢原子轨道构建近似波函数，(2) 我们使用变分原理系统地改进它们。有效电荷 $Z \approx 1.7$ 是我们首次定量接触**屏蔽**，后续章节将其发展为多电子原子的完整图景。
``````
:::
