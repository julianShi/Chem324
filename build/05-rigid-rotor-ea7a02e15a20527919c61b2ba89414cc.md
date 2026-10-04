# The Rigid Rotor


:::{note} What You Need to Know

- The **rigid rotor model** serves as a prototype for understanding the quantization of rotational degrees of freedom in molecules. We use a spherical coordinate system to exploit the spherical symmetry of the problem, effectively reducing the system's dimensionality.

- Solving the Schrödinger equation in spherical coordinates yields eigenfunctions in the form of **spherical harmonics**. The resulting energy eigenvalues exhibit degeneracy with respect to one of the quantum numbers.

- To compute **rotational spectra**, the **moment of inertia** of the molecule must be known. For diatomic molecules, this is simply $I = \mu r^2 $, where $\mu $ is the reduced mass and $r $ is the bond distance. For polyatomic molecules, the calculation is more complex, as it must account for the spatial distribution of mass.

- **Microwave spectroscopy** is directly connected to this model, with spectral lines predicted to occur at equal intervals of $2\tilde{B} $.

- The **selection rule** is established through the recursion relation of spherical harmonics and requires $\Delta J = \pm 1 $ and $\Delta M_J = 0, \pm 1 $.

- **Coupling with vibrational modes** leads to rovibronic transitions, necessitating the inclusion of vibrational quantum numbers for a comprehensive description of transition frequencies.

- Rotational motion can cause slight changes in bond length, known as the **centrifugal distortion effect**. This effect can be accounted for by adding a centrifugal correction term to the rigid rotor model.


``````{admonition} 中文翻译
:class: dropdown

- **刚体转动模型**作为理解分子转动自由度量子化的原型。我们使用球坐标系来利用问题的球对称性，有效地降低系统的维度。
- 在球坐标系中求解薛定谔方程得到的本征函数形式为**球谐函数**。得到的能值本征值相对于其中一个量子数具有简并性。
- 计算**转动光谱**，分子的**转动惯量**必须已知。对于二原子分子，这仅仅是 $I = \mu r^2 $，其中 $\mu $ 是减质量，$r $ 是键长。对于多原子分子，计算更为复杂，必须考虑质量的空间分布。
- **微波光谱** 直接与该模型相关，谱线预测以 $2\tilde{B} $ 的等间隔出现。
- **选择定则** 通过球谐函数的递推关系建立，要求 $\Delta J = \pm 1 $ 和 $\Delta M_J = 0, \pm 1 $。
- **耦合于振动模式** 导致转动-振动跃迁，需要包含振动量子数才能全面描述跃迁频率。
- 旋转运动会导致键长的轻微变化，称为**离心畸变效应**。可以通过将离心修正项加到刚性转子模型中来考虑这一效应。
``````

:::





### Quantum rigid rotor and angular momentum operator 

- The Hamiltonian for the rigid rotor model is the kinetic energy operator of an effective mass $\mu$ which rotates around a sphere of radius $r=const$. 

- To incorporate the constraint $r=const$ it is more convenient to adopt spherical coordinates $(x,y,z)\rightarrow (r,\theta,\phi)$. The full Laplacian in spherical coordinates is:

- In spherical coordinates the Hamiltonian is more conveniently expressed in terms of the angular momentum operator as opposed to the linear momentum operator:


``````{admonition} 中文翻译
:class: dropdown

- 刚性转子模型的哈密顿量是绕半径 $r=const$ 的球体旋转的有效质量 $\mu$ 的动能算符。
- 为了约束 $r=const$，采用球坐标 $(x,y,z)\rightarrow (r,\theta,\phi)$ 更方便。球坐标下的完整拉普拉斯算子是：
- 在球坐标系中，哈密顿量用角动量算符表示比用线动量算符表示更方便：
``````


$$
\hat{H}=-\frac{\hbar^2}{2\mu}\nabla_{x,y,z}^2 = -\frac{\hbar^2}{2\mu r^2}\nabla_{\theta,\phi}^2=\frac{\hat{L}^2}{2I}
$$


- Where $I=\mu r^2$ is the moment of inertia and we have identified the angular momentum operator as:


``````{admonition} 中文翻译
:class: dropdown

- 其中 $I=\mu r^2$ 是转动惯量，我们已经将角动量算符确定为：
``````

$$
\hat{L}= -i\hbar \nabla_{\theta,\phi}
$$



### Quantum numbers $(J,M_J)$ for quantizing $(\theta,\phi)$ coordinate pair. 

- Having written down the Hamiltonian we now solve it, anticipating two quantum numbers for two coordinates. 

- The eigenfunctions turn out to be well-known special functions called spherical harmonics $Y(\theta,\phi)$:


``````{admonition} 中文翻译
:class: dropdown

- 写下哈密顿量后，我们现在对其求解，预期会有两个量子数对应两个坐标。
- 本征函数恰好是众所周知的特殊函数，称为球谐函数 $Y(\theta,\phi)$：
``````


$$
\hat{H}Y(\theta, \phi)=E_{J,m}Y(\theta,\phi)
$$


- We are once again able to separate two angular variables and solve the resulting ODE exactly. 
- We expect the energy to depend on two quantum numbers $J$ and $M_J$, which quantize rotational motion across the $\theta$ and $\phi$ angles. 


``````{admonition} 中文翻译
:class: dropdown

- 我们再次能够分离两个角度变量，并精确求解由此产生的常微分方程。
- 我们预期能量取决于两个量子数 $J$ 和 $M_J$，它们量化了 $\theta$ 和 $\phi$ 角上的旋转运动。
``````


### Rotational states of molecules are quantized


:::{important} **Eigenvalues of Rotational States**

$$
E_J = \frac{\hbar^2}{2I}J(J+1) = BJ(J+1)
$$

* The **rotational constant** (has units of energy) is defined 


``````{admonition} 中文翻译
:class: dropdown

- **转动常数**（具有能量单位）定义为
``````

$$
B = \frac{h^2}{8\pi^2 I},
$$
  
:::

* Solving the rigid rotor problem reveals that **rotational energy eigenvalues depend only on the quantum number $J$**. 
* Each energy level is therefore **$(2J + 1)$-fold degenerate**, corresponding to the allowed values of the magnetic quantum number $M_J$.

* The **quantization** of rotational motion arises from the **cyclic boundary condition** rather than from any potential energy term (which is zero for a free rotor).


``````{admonition} 中文翻译
:class: dropdown

- 求解刚性转子问题表明，**转动能量本征值仅取决于量子数$J$**。
- 因此每个能级都是 **$(2J + 1)$ 重简并**，对应磁量子数 $M_J$ 的允许取值。
- 旋转运动的**量化**源于**周期性边界条件**，而非任何势能项（自由转子的势能项为零）。
``````

  $$
  \Phi(0) = \Phi(2\pi),
  $$

* There is **no rotational zero-point energy**, since the $J = 0$ state is allowed.

* The **ground-state rotational wavefunction** corresponds to an isotropic distribution, with equal probability for all orientations.


``````{admonition} 中文翻译
:class: dropdown

- 不存在**旋转零点能**，因为允许 $J = 0$ 态。
- **基态旋转波函数** 对应各向同性分布，所有取向的概率相等。
``````


:::{admonition} **Example**

What are the reduced mass and moment of inertia of $H^{35}Cl$? The equilibrium internuclear distance $R_e$ is 127.5 pm. What are the values of $L, L_z$ and $E$ for the state with $J = 1$? The atomic masses are: $m_H = 1.673470 \cdot 10^{-27}$ kg and $m_{Cl} = 5.806496 \cdot 10^{-26}$ kg.


``````{admonition} 中文翻译
:class: dropdown

氢氯化氢 $H^{35}Cl$ 的简并质量和转动惯量是多少？平衡核间距离 $R_e$ 为 127.5 pm。$J = 1$ 态下 $L, L_z$ 和 $E$ 的值是多少？原子质量为：$m_H = 1.673470 \cdot 10^{-27}$ kg 且 $m_{Cl} = 5.806496 \cdot 10^{-26}$ kg。
``````
:::

:::{note} **Solution**
:class: dropdown

First we calculate the reduced mass:

$$\mu = \frac{m_{\textnormal{H}}m_{^{35}\textnormal{Cl}}}{m_{\textnormal{H}} + m_{^{35}\textnormal{Cl}}} = \frac{(1.673470\times 10^{-27}\textnormal{ kg})(5.806496\times 10^{-26}\textnormal{ kg})}{(1.673470\times 10^{-27}\textnormal{ kg}) + (5.806496\times 10^{-26}\textnormal{ kg})}$$
$$= 1.62665\times 10^{-27}\textnormal{ kg}$$


$$I = \mu R_e^2 = (1.626\times 10^{-27}\textnormal{ kg})(127.5\times 10^{-12}\textnormal{ m})^2 = 2.644\times 10^{-47}\textnormal{ kg m}^2$$

$L$ and $L_z$ are given by the eigenvalue expressions of the respective operators:


``````{admonition} 中文翻译
:class: dropdown

$L$ 和 $L_z$ 由相应算符的本征值表达式给出：
``````

$$L = \sqrt{J(J+1)}\hbar = \sqrt{2}\left(1.054\times 10^{-34}\textnormal{ Js}\right) = 1.491\times 10^{-34}\textnormal{ Js}$$


$$L_z = -\hbar,0,\hbar\textnormal{ (three possible values)}$$

The energy of the $J = 1$ level is given by the eigenvalue expression of the Hamiltonian:


``````{admonition} 中文翻译
:class: dropdown

$J = 1$ 能级的能量由哈密顿量的本征值表达式给出：
``````

$$E = \frac{\hbar^2}{2I}J(J+1) = \frac{\hbar^2}{I} = 4.206\times 10^{-22}\textnormal{ J} = 21\textnormal{ cm}^{-1}$$

This rotational spacing can be observed, for example, in the gas-phase infrared spectrum of HCl.


``````{admonition} 中文翻译
:class: dropdown

例如，这种转动间距可以在 HCl 气相红外光谱中观测到。
``````
:::

### Rotational spectra of diatomic molecules

- We assume that the molecule is a rigid rotor, which means that the molecular geometry does not change during rotation. We have solved this problem already. 

- Energies are typically expressed in wavenumber units ($cm^{-1}$, although the basic SI unit is $m^{-1}$) by dividing $E$ by $hc$. The use of wavenumber units is denoted by a tilde above the variable (e.g., $\tilde{\nu}$). 

- Within the rigid rotor approximation we can derive selection rules by computing the transition dipole moment using properties of the spherical harmonics. 


``````{admonition} 中文翻译
:class: dropdown

- 我们假设分子是刚性转子，这意味着分子几何结构在旋转过程中不发生变化。我们已经解决了这个问题。
- 能量通常用波数单位（$cm^{-1}$，尽管基本SI单位是 $m^{-1}$）表示，通过将 $E$ 除以 $hc$。使用波数单位的变量上方有一波浪号（例如，$\tilde{\nu}$）。
- 在刚性转子近似下，我们可以利用球谐函数的性质计算跃迁偶极矩来推导选择定则。
``````

:::{important} **Rotational energies in spectroscopic units**

$${\tilde{E}_r(J) = \frac{E_r}{hc} = \tilde{B} J(J+1)}$$

- the *rotational constant* expressed in $cm^{-1}$ units is given by:


``````{admonition} 中文翻译
:class: dropdown

- *旋转常数* 以 $cm^{-1}$ 单位表示为：
``````

$${\tilde{B} = \frac{h}{8\pi^2Ic}}$$
:::


:::{important} **Selection rules for rigid rotor model**


- The molecule must possess a permanent dipole moment!


``````{admonition} 中文翻译
:class: dropdown

- 分子必须具有永久偶极矩！
``````

$$\langle J' | \mu | J'' \rangle \neq 0$$

- On top of that, only transitions between adjacent levels are allowed. For example, $\Delta J =0$ and $|\Delta J| > 1$ transitions are forbidden.


``````{admonition} 中文翻译
:class: dropdown

- 此外，仅允许相邻能级之间的跃迁。例如，$\Delta J =0$ 和 $|\Delta J| > 1$ 的跃迁是被禁止的。
``````

$$\boxed{\Delta J = J' - J = \pm 1}$$

:::



### Spectral lines and rotational constant determination 

- When we compute the energy spacing we see that it depends linearly on the quantum level $J$. This means we can take one more difference and easily eliminate it, getting a constant:


``````{admonition} 中文翻译
:class: dropdown

- 当我们计算能量间距时，发现它与量子水平 $J$ 线性相关。这意味着我们可以再取一次差，轻松消去它，得到一个常数：
``````

$${\tilde{\nu_J} = \tilde{E}_r(J + 1) - \tilde{E}_r(J) = \left((J+1)(J+2) - J(J+1)\right)\tilde{B} = 2\tilde{B}(J+1)}$$

:::{important} **Spacing of adjacent spectral lines**

$$\tilde{\nu}_{J+1} - \tilde{\nu_J} = 2\tilde{B}$$

:::

- The successive line positions in the rotational spectrum are given by $2\tilde{B}, 4\tilde{B}, 6\tilde{B},...$. Note that molecules with different atomic isotopes have different moments of inertia and hence different positions for the rotational lines.


``````{admonition} 中文翻译
:class: dropdown

- 光谱中旋转线的位置由 $2\tilde{B}, 4\tilde{B}, 6\tilde{B},...$ 给出。注意，具有不同原子同位素的分子具有不同的惯量，因此旋转线的位置也不同。
``````


:::{figure} ./images/wqual_space.png
:label: fig-rigid-rotor-1
:alt: DeD0
:width: 350px

The rigid rotor model predicts evenly spaced spectral lines.


``````{admonition} 中文翻译
:class: dropdown

刚性转子模型预测谱线均匀分布。
``````
:::


:::{admonition} **Population of rotational states**
:class: info, dropdown

Another factor that affects the line intensities in a rotational spectrum is related to the thermal population of the rotational levels. Thermal populations of the rotational levels is given by the Boltzmann distribution (for a collection of molecules):


``````{admonition} 中文翻译
:class: dropdown

影响旋转谱线强度的另一个因素与转动能级的热人口成正比有关。转动能级的热人口由玻尔兹曼分布给出（对于一组分子）：
``````

$${f_J = \frac{g_Je^{-hc\tilde{E}_r(J) / (k_B T)}}{\sum\limits_{J'}g_{J'}e^{-hc\tilde{E}_r(J') / (k_B T)}} = \frac{g_Je^{-hc\tilde{E}_r(J) / (k_B T)}}{q}}$$

- Here $q$ is called the *partition function*, and $g_J = 2J + 1$ is the degeneracy of state $J$. A useful reference for the thermal energy is $kT$: if the energy of a state is much higher than this, it will not be thermally populated. 
- One expects the intensities to first increase as a function of the initial state $J$, reach a maximum, and then decrease as the thermal populations fall off. In an absorption experiment, one can see the thermal populations of the initial rotational levels.

- Note: for systems where the rotational degrees of freedom may exchange identical nuclei, an additional complication arises from the symmetry requirement on the nuclear wavefunction. Recall that bosons must have symmetric wavefunctions and fermions antisymmetric ones. We will not discuss this in more detail here.


``````{admonition} 中文翻译
:class: dropdown

- 这里 $q$ 被称为配分函数，$g_J = 2J + 1$ 是态 $J$ 的简并度。热能的有用参考是 $kT$：如果态的能量远高于此，则不会被热激发。
- 人们预期强度首先随着初始状态 $J$ 的增加而增大，达到最大值，随后因热人口数的减小而减小。在吸收实验中，可以观察到初始转动能级的热人口数。
- 注：对于可交换核的自转自由度的系统，核波函数的对称性要求会产生额外的复杂性。回想一下，玻色子必须具有对称的波函数，费米子则是反对称的。此处我们将不作更详细的讨论。
``````
:::

:::{note} **Example**

Calculate the relative populations of the first five rotational levels of the ground vibrational state of $H^{35}$Cl at 300 K. The ground vibrational state rotational constant $B_0 = 10.44$ cm$^{-1}$.


``````{admonition} 中文翻译
:class: dropdown

计算氯化氢 $H^{35}$Cl 基态前五个转动能级在300 K时的相对占人口。基态转动常数 $B_0 = 10.44$ cm$^{-1}$。
``````
:::

:::{note} **Solution**
:class: dropdown

The level populations are given by the Boltzmann distribution:


``````{admonition} 中文翻译
:class: dropdown

能级布居由玻尔兹曼分布给出：
``````

$$\frac{N_J}{N_0} = \left(2J + 1\right)e^{-hcJ(J+1)\tilde{B}_0/(k_BT)}$$

where $N_0$ is the number of molecules in the rotational ground state. First we calculate the factor appearing in the exponent:


``````{admonition} 中文翻译
:class: dropdown

其中 $N_0$ 是处于转动基态的分子数。首先我们计算指数中出现的因子：
``````


$$\frac{hc\tilde{B}_0}{k_BT} = \frac{(6.626\times 10^{-34}\textnormal{ Js})(2.998\times 10^8\textnormal{ m/s})(10.44\textnormal{ cm}^{-1})(10^2\textnormal{ cm/m})}{(1.3806\times 10^{-23}\textnormal{ J K}^{-1})(300\textnormal{ K})}$$
$$ = 5.007\times 10^{-2}$$

Then, for example, for $J = 1$ we get:


``````{admonition} 中文翻译
:class: dropdown

那么，例如，对于 $J = 1$，我们得到：
``````

$$\frac{N_1}{N_0} = 3e^{-2(5.007\times 10^{-2})} = 2.71$$

The same way one can get the relative populations as: 1.00, 2.71, 3.70, 3.84, 3.31, and 2.45 for $J = 0, 1, 2, 3, 4, 5$. Note that these are relative populations since we did not calculate the partition function $q$.


``````{admonition} 中文翻译
:class: dropdown

相对占有数可以这样得到：$J = 0, 1, 2, 3, 4, 5$ 时的相对占有数分别为 1.00, 2.71, 3.70, 3.84, 3.31, 和 2.45。注意这些是相对占有数，因为我们没有计算配分函数 $q$。
``````
:::  


### Ro-vibrational spectra, R, P and Q branches

:::{figure} ./images/P_Q_R_branch.png
:label: fig-rigid-rotor-2
:alt: DeD0
:width: 400px

Cartoon of an idealized rovibrational spectrum showing the P, Q, and R branches.


``````{admonition} 中文翻译
:class: dropdown

理想化转动振动光谱示意图，显示 P、Q 和 R 支。
``````
:::

- Often we are interested in transitions among rotational levels that accompany excitation from the ground vibrational state, $v=0\rightarrow v=1$. This can be described by combining the rigid rotor and harmonic oscillator models:


``````{admonition} 中文翻译
:class: dropdown

- 我们常对伴随基态激发 $v=0\rightarrow v=1$ 的转动能级跃迁感兴趣。这可以通过刚性转子和谐振子模型的结合来描述：
``````

$$
\tilde{E}_{v, J} = \tilde{\omega}(v+1/2)+\tilde{B}J(J+1)
$$

- Since at room temperature molecules mostly occupy the vibrational ground state, we are interested in rotational transitions taking place between the ground ($v=0$) and the first excited ($v=1$) vibrational states.

- Rigid rotor model predicts different frequencies for absorption and emission transitions between any two rotational states $J$ and $J'$ given by $\tilde{\nu}_{\Delta J} = {\tilde{E}_{1,J'} - \tilde{E}_{0,J}}$ where the $J = 0,1,2...$ refers to the initial rotational state and $J'$ is the final state. 

 - **The transitions with $\Delta J=+1$ are called R branch**: 


``````{admonition} 中文翻译
:class: dropdown

- 由于在室温下分子大多占据振动基态，我们关注在基态 ($v=0$) 和第一激发态 ($v=1$) 之间进行的转动跃迁。
- 刚性转子模型预测任意两个转态 $J$ 和 $J'$ 之间吸收和发射跃迁的不同频率，由 $\tilde{\nu}_{\Delta J} = {\tilde{E}_{1,J'} - \tilde{E}_{0,J}}$ 给出，其中 $J = 0,1,2...$ 指初始转态，$J'$ 为最终态。
- **$\Delta J=+1$ 的跃迁称为 R 支**：
``````
 
 $$\tilde{\nu}_{\Delta J=+1}=\tilde{\omega} + 2\tilde{B}(J+1)$$

 - **The transitions with $\Delta J=-1$ are called P branch:** 


``````{admonition} 中文翻译
:class: dropdown

- **$\Delta J=-1$ 的跃迁称为 P 支：**
``````
 
 $$\tilde{\nu}_{\Delta J=-1}=\tilde
 {\omega} - 2\tilde{B}J$$

 - **The Q-branch $\Delta J =0$** is predicted to be absent because it is forbidden by the selection rule of the rigid rotor model. 


``````{admonition} 中文翻译
:class: dropdown

- **Q支 $\Delta J =0$** 预测是不存在的，因为它被刚性转子模型的选择定则所禁止。
``````

  $$\tilde{\nu}_{\Delta J=0}=\tilde
 {\omega}$$


### Rigid rotor and real microwave spectra

:::{figure} ./images/ideal.png
:label: fig-rigid-rotor-3
:alt: DeD0
:width: 300px

Idealized rovibrational spectrum predicted by the rigid rotor model.


``````{admonition} 中文翻译
:class: dropdown

刚性转子模型预测的理想化转动振动光谱。
``````
:::


:::{figure} ./images/real.png
:label: fig-rigid-rotor-4
:alt: DeD0
:width: 300px

A real rovibrational spectrum, showing departures from the idealized rigid rotor pattern.


``````{admonition} 中文翻译
:class: dropdown

真实的转动-振动光谱，显示出与理想化刚性转子模式的偏离。
``````
:::

:::{figure} ./images/co_micr.png
:label: fig-rigid-rotor-5
:alt: DeD0
:width: 300px

High-resolution spectrum of CO, with the P and R branches resolved into individual rotational transitions.


``````{admonition} 中文翻译
:class: dropdown

CO的高分辨率光谱，P支和R支分辨为单个旋转跃迁。
``````
:::



### Rovibronic Coupling

* As a diatomic molecule **vibrates**, its **bond length** oscillates. Because the **moment of inertia** depends on the bond length, it also changes during vibration, leading to a variation in the **rotational constant** $B$.

* In earlier approximations, we assumed that the rotational constants of the $R(0)$ and $P(1)$ transitions were identical. In reality, they differ due to this **rovibrational coupling**.

* The dependence of $B$ on the vibrational quantum number $v$ can be expressed as:


``````{admonition} 中文翻译
:class: dropdown

- 作为二原子分子**振动**时，其**键长**会发生振动。因为**转动惯量**取决于键长，因此在振动过程中也会改变，导致**转动常数** $B$ 产生变化。
- 在早期近似中，我们假设 $R(0)$ 和 $P(1)$ 跃迁的转动常数相同。实际上，由于这种 **rovibrational coupling**（rovibronic 耦合），它们存在差异。
- $B$ 对振动量子数 $v$ 的依赖关系可表示为：
``````

  $$
  B_v = B_e - \alpha_e (v + \tfrac{1}{2}),
  $$

- where $B_e$ is the equilibrium rotational constant (for a rigid rotor), and $\alpha_e$ is the **rotation–vibration coupling constant**. From observed band spectra, one can determine $B_0$, $B_1$, and $\alpha_e$ using **combination differences**.



- **R branch (ΔJ = +1) with rovibronic coupling:**


``````{admonition} 中文翻译
:class: dropdown

- 其中 $B_e$ 是刚性转动体的平衡转动常数，$\alpha_e$ 是**转动-振动耦合常数**。从观测到的谱带，可以利用**组合差**确定 $B_0$、$B_1$ 和 $\alpha_e$。
- **R 支（ΔJ = +1）伴随转振电子耦合：**
``````

$$
\tilde{\nu}_{R} = \tilde{\omega} + 2\tilde{B}_1 + (3\tilde{B}_1 - \tilde{B}_0)J + (\tilde{B}_1 - \tilde{B}_0)J^2
$$

- **P branch (ΔJ = −1) with rovibronic coupling:**


``````{admonition} 中文翻译
:class: dropdown

- **P 支（ΔJ = −1）伴随转振电子耦合：**
``````

$$
\tilde{\nu}_{P} = \tilde{\omega} - (\tilde{B}_1 + \tilde{B}_0)J + (\tilde{B}_1 - \tilde{B}_0)J^2
$$

- When  $B_0 = B_1$, these reduce to the **rigid-rotor–harmonic-oscillator** expressions, as expected.


``````{admonition} 中文翻译
:class: dropdown

- 当 $B_0 = B_1$ 时，这些表达式简化为 **刚性转子-谐振子** 表达式，正如预期的那样。
``````



### Centrifugal Distortion

* Real molecules are **not perfectly rigid**. As rotational speed increases, the **centrifugal force** stretches the bond, increasing the moment of inertia and **reducing the energy spacing** between rotational levels.

* This effect represents another type of **rotation–vibration coupling**, but it arises from the **centrifugal stretching** of the bond rather than from vibrational averaging of $B$.

* The correction is introduced by adding a **centrifugal distortion term** to the rigid-rotor energy expression:


``````{admonition} 中文翻译
:class: dropdown

- 真实分子**并非完全刚性**。随着转动速度增加，**离心力**会拉伸化学键，增大转动惯量，从而**减小转动能级间距**。
- 此效应代表另一种**旋转-振动耦合**类型，它源于键的**离心拉伸**而非振动平均的 $B$。
- 通过向刚性转子能量表达式添加**离心畸变项**来引入修正：
``````

  $$
  \tilde{E}_r(J) = \tilde{B} J(J+1) - \tilde{D} J^2 (J+1)^2,
  $$

  where $\tilde{D}$ is the **centrifugal distortion constant** in $cm^{-1}$, and both $\tilde{B}$ and $\tilde{D}$ are positive.


``````{admonition} 中文翻译
:class: dropdown

其中 $\tilde{D}$ 是 **离心畸变常数**，单位为 $cm^{-1}$，且 $\tilde{B}$ 和 $\tilde{D}$ 均为正值。
``````

* The corresponding rotational transition frequencies become:

  $$
  \tilde{\nu} = \tilde{E}_r(J+1) - \tilde{E}_r(J)
  = 2\tilde{B}(J+1) - 4\tilde{D}(J+1)^3, \qquad J = 0, 1, 2, \ldots
  $$



#### Key Difference in two rovibronic couplings

| Effect                     | Physical Origin                                               | Depends on                       | Typical Signature                              |
| :------------------------- | :------------------------------------------------------------ | :------------------------------- | :--------------------------------------------- |
| **Rovibronic coupling**    | Vibrational averaging of $B$ due to bond-length oscillation | Vibrational quantum number $v$ | Causes $B_v$ to decrease linearly with $v$ |
| **Centrifugal distortion** | Bond stretching at high rotational speeds                     | Rotational quantum number $J$  | Causes energy levels to crowd at large $J$   |






### Problems

#### Problem 1

Consider a diatomic molecule with the following constants:


``````{admonition} 中文翻译
:class: dropdown

考虑一个具有以下常数的双原子分子：
``````

- Vibrational constant: $\omega_e = 2100 \, \text{cm}^{-1}$
- Rotational constant: $B_e = 1.4 \, \text{cm}^{-1}$


``````{admonition} 中文翻译
:class: dropdown

- 振动常数: $\omega_e = 2100 \, \text{cm}^{-1}$
- 转动常数: $B_e = 1.4 \, \text{cm}^{-1}$
``````
  
The molecule undergoes a transition from the vibrational ground state ($v = 0$) to the first excited vibrational state ($v = 1$). 


``````{admonition} 中文翻译
:class: dropdown

分子从振动基态 ($v = 0$) 跃迁到第一振动激发态 ($v = 1$)。
``````

1. **Calculate the wavenumbers** of the $P$-branch transitions for $J = 1$ and $J = 2$ in the $v = 0 \rightarrow v = 1$ transition.
2. **Calculate the wavenumbers** of the $R$-branch transitions for $J = 0$ and $J = 1$ in the $v = 0 \rightarrow v = 1$ transition.
3. Explain the nature of the $P$- and $R$-branches in the context of rotational-vibrational spectroscopy and how they appear in the spectrum.


``````{admonition} 中文翻译
:class: dropdown

- **计算** $v = 0 \rightarrow v = 1$ 跃迁中 $J = 1$ 和 $J = 2$ 的 $P$ 分支跃迁的**波数**
- **计算** $v = 0 \rightarrow v = 1$ 跃迁中 $J = 0$ 和 $J = 1$ 的 $R$-支跃迁的**波数**
- 解释旋转-振动光谱中 $P$- 分支和 $R$- 分支的性质，以及它们在光谱中的表现。
``````



:::{admonition} **Solution**
:class: dropdown solution

**Part 1: $P$-Branch Transitions**

The $P$-branch corresponds to transitions where $\Delta J = -1$. For a $v = 0 \rightarrow v = 1$ vibrational transition, the wavenumber of the $P$-branch transition from a state with rotational quantum number $J$ is given by:


``````{admonition} 中文翻译
:class: dropdown

$P$ 分支对应 $\Delta J = -1$ 的跃迁。对于 $v = 0 \rightarrow v = 1$ 振动跃迁，从转动量子数为 $J$ 的态出发的 $P$ 分支跃迁的波数由下式给出：
``````

$$
\tilde{\nu}_{P(J)} = \omega_e - B_e \left[ J (J - 1) \right]
$$

1. **For $J = 1$:**
   $$
   \tilde{\nu}_{P(1)} = \omega_e - B_e \cdot 1 \cdot (1 - 1) = \omega_e - B_e \cdot 0 = 2100 - 0 = 2100 \, \text{cm}^{-1}
   $$

2. **For $J = 2$:**
   $$
   \tilde{\nu}_{P(2)} = \omega_e - B_e \cdot 2 \cdot (2 - 1) = 2100 - 1.4 \cdot 2 = 2100 - 2.8 = 2097.2 \, \text{cm}^{-1}
   $$

So, the wavenumbers for the $P$-branch transitions are:


``````{admonition} 中文翻译
:class: dropdown

因此，$P$ 分支跃迁的波数为：
``````
- $J = 1 \rightarrow J = 0$: $2100 \, \text{cm}^{-1}$
- $J = 2 \rightarrow J = 1$: $2097.2 \, \text{cm}^{-1}$


``````{admonition} 中文翻译
:class: dropdown

- $J = 1 \rightarrow J = 0$：$2100 \, \text{cm}^{-1}$
- $J = 2 \rightarrow J = 1$: $2097.2 \, \text{cm}^{-1}$
``````

**Part 2: $R$-Branch Transitions**

The $R$-branch corresponds to transitions where $\Delta J = +1$. For a $v = 0 \rightarrow v = 1$ vibrational transition, the wavenumber of the $R$-branch transition from a state with rotational quantum number $J$ is given by:


``````{admonition} 中文翻译
:class: dropdown

$R$ 分支对应 $\Delta J = +1$ 的跃迁。对于 $v = 0 \rightarrow v = 1$ 振动跃迁，从转动量子数为 $J$ 的态出发的 $R$ 分支跃迁的波数由下式给出：
``````

$$
\tilde{\nu}_{R(J)} = \omega_e + B_e \left[ (J + 1)(J + 2) \right]
$$

1. **For $J = 0$:**
   $$
   \tilde{\nu}_{R(0)} = \omega_e + B_e \cdot (0 + 1)(0 + 2) = 2100 + 1.4 \cdot 2 = 2100 + 2.8 = 2102.8 \, \text{cm}^{-1}
   $$

2. **For $J = 1$:**
   $$
   \tilde{\nu}_{R(1)} = \omega_e + B_e \cdot (1 + 1)(1 + 2) = 2100 + 1.4 \cdot 6 = 2100 + 8.4 = 2108.4 \, \text{cm}^{-1}
   $$

So, the wavenumbers for the $R$-branch transitions are:


``````{admonition} 中文翻译
:class: dropdown

因此，$R$ 分支跃迁的波数为：
``````
- $J = 0 \rightarrow J = 1$: $2102.8 \, \text{cm}^{-1}$
- $J = 1 \rightarrow J = 2$: $2108.4 \, \text{cm}^{-1}$


``````{admonition} 中文翻译
:class: dropdown

- $J = 0 \rightarrow J = 1$: $2102.8 \, \text{cm}^{-1}$
- $J = 1 \rightarrow J = 2$: $2108.4 \, \text{cm}^{-1}$
``````

**Part 3: Nature of the $P$- and $R$-Branches**


``````{admonition} 中文翻译
:class: dropdown

**第 3 部分：$P$-支和 $R$-支的性质**
``````

In rotational-vibrational spectroscopy:

- The **$P$-branch** consists of transitions where the rotational quantum number decreases by 1 ($\Delta J = -1$). These transitions appear at wavenumbers lower than the vibrational transition frequency $\omega_e$, creating a series of lines that shift progressively to lower energies as $J$ increases.


``````{admonition} 中文翻译
:class: dropdown

- **$P$ 分支** 由旋转量子数减 1 的跃迁组成 ($\Delta J = -1$)。这些跃迁出现在振动跃迁波数 $\omega_e$ 以下，形成一系列线，随着 $J$ 的增加，能量逐渐向低能偏移。
``````
  
- The **$R$-branch** consists of transitions where the rotational quantum number increases by 1 ($\Delta J = +1$). These transitions appear at wavenumbers higher than $\omega_e$, resulting in a series of lines at progressively higher energies as $J$ increases.


``````{admonition} 中文翻译
:class: dropdown

- **$R$-支** 由旋转量子数增加 1 ($\Delta J = +1$) 的跃迁组成。这些跃迁出现在高于 $\omega_e$ 的波数处，随着 $J$ 的增加，形成一系列能量逐渐升高的谱线。
``````

In a spectrum, the $P$-branch lines appear on the lower wavenumber side of the fundamental vibrational frequency, while the $R$-branch lines appear on the higher wavenumber side. These branches provide a characteristic double-sided pattern centered around $\omega_e$, reflecting the rotational structure superimposed on the vibrational transition.


``````{admonition} 中文翻译
:class: dropdown

在光谱中，$P$支线出现在基频振动的低波数一侧，而 $R$支线出现在高波数一侧。这些支线围绕 $\omega_e$ 形成典型的双侧模式，反映了叠加在振动跃迁上的旋转结构。
``````
:::

#### Problem 2

Measurement of pure rotational spectrum of H$^{35}$Cl molecule gave the following positions for the absorption lines:


``````{admonition} 中文翻译
:class: dropdown

H$^{35}$Cl 分子纯转动光谱的测量给出了以下吸收线位置：
``````

$$\tilde{\nu} = \left(20.794\textnormal{cm}^{-1}\right)\left(J+1\right) - \left(0.000164\textnormal{cm}^{-1}\right)\left(J+1\right)^3$$

What is the equilibrium bond length and what is the value of the centrifugal distortion constant?


``````{admonition} 中文翻译
:class: dropdown

平衡键长是多少？离心畸变常数的值是多少？
``````


:::{admonition} **Solution**
:class: dropdown solution

We first write the expression for $\tilde{B}$ and then use the definition of the moment of inertia $I$:


``````{admonition} 中文翻译
:class: dropdown

我们首先写出 $\tilde{B}$ 的表达式，然后使用转动惯量 $I$ 的定义：
``````

$$\tilde{B} = \frac{h}{8\pi^2cI} = \frac{h}{8\pi^2c\mu R_0^2}$$

where $\mu$ is the reduced mass for the molecule and $R_0$ is the equilibrium bond length. Solving for $R_0$ gives:


``````{admonition} 中文翻译
:class: dropdown

其中 $\mu$ 为分子的约化质量，$R_0$ 为平衡键长。解得 $R_0$ 为：
``````

$$R_0 = \sqrt{\frac{h}{8\pi^2c\mu\tilde{B}}} = 129\textnormal{ pm}$$


The centrifugal distortion constant can be obtained by comparing the above equation with the equation for rovibronic coupling:


``````{admonition} 中文翻译
:class: dropdown

通过将上式与转振电子耦合方程比较，可获得离心畸变常数：
``````

$$\tilde{D} = 4.1\times 10^{-5}\textnormal{ cm}^{-1}$$
:::