---
kernelspec:
  name: python3
  display_name: Python 3
---

# Molecular Degrees of Freedom and Classical Vibrations

:::{note} **What you need to know**

Having found that the energy of bound systems is quantized, our next goal is to investigate how quantization shows up in molecules and how experiments probe it via spectroscopy. The coordinates of a molecule split into **translational, rotational, vibrational, and electronic degrees of freedom (DOF)**, and each kind of motion gets its own exactly solvable toy model:


``````{admonition} 中文翻译
:class: dropdown

找到有界系统能量量化这一事实后，我们的下一个目标是研究量化在分子中如何显现，以及实验如何通过光谱学探测它。分子的坐标分解为 **平动、旋转、振动和电子自由度 (DOF)**，每种运动都有自己的精确可解的玩具模型：
``````

- **Particle in a box** (quantization of translational DOF)
- **Harmonic oscillator** (quantization of vibrational DOF)
- **Rigid rotor** (quantization of rotational DOF)


``````{admonition} 中文翻译
:class: dropdown

- **一维势箱中的粒子**（平动自由度的量子化）
- **谐振子** (量子化振动自由度)
- **刚性转子** (转动自由度量化)
``````

The vibrational piece is where the potential lives, so we first master its classical version:


``````{admonition} 中文翻译
:class: dropdown

势能存在于振动部分，因此我们首先掌握其经典版本：
``````

- **Equation of motion**: Hooke's law $F = -kx$ gives $m\ddot{x} + kx = 0$, solved by $x(t) = A\sin(\omega t + \phi)$ with $\omega = \sqrt{k/m}$.
- **Energy** $E = \frac{p^2}{2m} + \frac{kx^2}{2}$ is conserved, sloshing between kinetic and potential forms.
- A vibrating **diatomic** reduces to a single bead with the **reduced mass** $\mu = \frac{m_1 m_2}{m_1 + m_2}$.
- The harmonic form is the **leading Taylor term** of any realistic bond potential near its minimum, which is why one model covers all molecules.


``````{admonition} 中文翻译
:class: dropdown

- **运动方程**：胡克定律 $F = -kx$ 给出 $m\ddot{x} + kx = 0$，其解为 $x(t) = A\sin(\omega t + \phi)$，其中 $\omega = \sqrt{k/m}$。
- **能量** $E = \frac{p^2}{2m} + \frac{kx^2}{2}$ 是守恒的，在动能和势能形式之间来回转换。
- 振动的**双原子**分子可简化为一个具有**约化质量** $\mu = \frac{m_1 m_2}{m_1 + m_2}$ 的单珠。
- 谐波形式是任意真实键势在其极小值附近的**泰勒展开首项**，这也是一个模型能覆盖所有分子的原因。
``````

:::

###  Energies of molecules

Molecules consisting of N nuclei and n electrons are described by wave functions that depend on 3(n+N) variables in 3D space. These coordinates, or degrees of freedom (DOF), are usefully broken down into different kinds of motion classified as translational, rotational, vibrational and electronic. Because molecules are microscopic objects, we expect all of these energies to be quantized. The relative spacings, however, differ significantly because of the boundary conditions that restrict the motions of these DOFs. This is why different kinds of spectroscopy exist for probing the specific degrees of freedom in molecules.


``````{admonition} 中文翻译
:class: dropdown

由 N 个核和 n 个电子组成的分子，其波函数依赖于 3D 空间中的 3(n+N) 个变量。这些坐标，或称为度的自由度（DOF），有用地分解为不同种类的运动，分类为平动、旋转、振动和电子。由于分子是微观物体，我们期望这些能量均被量子化。然而，这些 DOFs 运动的边界条件导致相邻能级的间距差异显著。这就是为什么存在不同种类的光谱学，用于探测分子中特定的度的自由度。
``````

$$E= \epsilon_{trans}+ \epsilon_{rot}+ \epsilon_{vib}+\epsilon_{elec}$$


:::{figure} ./images/Levels1.gif
:label: fig-molecular-degrees-of-freedom-1
:alt: mol deg freed
:width: 500px

Energy levels associated with the different degrees of freedom in molecules.


``````{admonition} 中文翻译
:class: dropdown

分子中不同自由度相关的能级。
``````
:::




### 3N Nuclear degrees of freedom 

- The *Born-Oppenheimer approximation* allows us to separate the nuclear and electronic degrees of freedom. The nuclear Hamiltonian for $N$ nuclei can now be written in such a way that the electronic part appears as a potential term:


``````{admonition} 中文翻译
:class: dropdown

- **鲍恩-奥本海默近似** 允许我们分离核和电子的自由度。现在可以以这样的方式编写 $N$ 个核的核哈密顿量，以至于电子部分作为一个势项出现：
``````

$${\hat{H} = \sum\limits_{i=1}^{N} -\frac{\hbar^2}{2m_i}\nabla_{R_i}^2 + E(R_1, R_2, ..., R_N)}$$


:::{figure} ./images/mol-DOF.jpg
:label: fig-molecular-degrees-of-freedom-2
:alt: mol deg freed
:width: 500px

The different degrees of freedom in molecules: translational, rotational and vibrational motion.


``````{admonition} 中文翻译
:class: dropdown

分子的不同自由度：平动、转动和振动运动。
``````
:::


- In the absence of external electric or magnetic fields, the potential term $E$ depends only on the relative positions of the nuclei, as shown above, and not on the overall position of the molecule or its orientation in space. The above Hamiltonian $H$ can often be approximately written as a sum of the following terms:


``````{admonition} 中文翻译
:class: dropdown

- 在没有外部电场或磁场的情况下，势能项 $E$ 仅取决于原子核的相对位置，如上所示，而不取决于分子在空间中的整体位置或取向。上述哈密顿量 $H$ 经常可以近似地写成以下项的和：
``````

$${\hat{H} = \hat{H}_{tr} + \hat{H}_{rot} + \hat{H}_{vib}}$$

where $H_{tr}$ is the translational, $H_{rot}$ the rotational, and $H_{vib}$ the vibrational Hamiltonian. The translational and rotational terms have no potential part, but the vibrational part contains the potential $E$, which depends on the distances between the nuclei.


``````{admonition} 中文翻译
:class: dropdown

其中 $H_{tr}$ 为平动哈密顿，$H_{rot}$ 为转动哈密顿，$H_{vib}$ 为振动哈密顿。平动和转动项没有势能部分，但振动部分包含势能 $E$，该势能取决于原子间的距离。
``````

> In some cases the different degrees of freedom become coupled and one cannot use the following separation technique. Separation of $H$ means that we can write the wavefunction as a product:


``````{admonition} 中文翻译
:class: dropdown

> 在某些情况下，不同的自由度会耦合，无法使用下面的分离技术。分离 $H$ 意味着我们可以将波函数写成乘积：
``````

$${\psi = \psi_{tr}\psi_{rot}\psi_{vib}}$$

### Separation of degrees of freedom

The resulting three Schrödinger equations are then:

$${\hat{H}_{tr}\psi_{tr} = E_{tr}\psi_{tr}}$$

$${\hat{H}_{rot}\psi_{rot} = E_{rot}\psi_{rot}}$$

$${\hat{H}_{vib}\psi_{vib} = E_{vib}\psi_{vib}}$$

- The translational part is not interesting, since there is no external potential or boundary condition that could lead to quantization (i.e., it produces a continuous spectrum).


``````{admonition} 中文翻译
:class: dropdown

- 平动部分不感兴趣，因为没有外部势或边界条件可能导致量子化（即，它产生连续谱）。
``````
  
- On the other hand, the rotational part is subject to a cyclic boundary condition and the vibrational part to the potential $E$, so we expect these to produce quantization, which can be probed by spectroscopic methods.

- The original number of variables in the Hamiltonian is $3\times N$ (i.e. the $x,y,z$ coordinates for each nucleus). We can neglect the translational motion, and we are left with $3N - 3$ coordinates.


``````{admonition} 中文翻译
:class: dropdown

- 另一方面，旋转部分受循环边界条件约束，振动部分受势能 $E$ 约束，所以我们期望这些会产生量子化，可通过光谱学方法探测。
- Hamiltonian 中变量的原始数量为 $3\times N$（即每个核的 $x,y,z$ 坐标）。我们可以忽略平动运动，剩下 $3N - 3$ 个坐标。
``````
  
- To account for molecular rotation, three variables are required, or only two variables for a linear molecule. Therefore the vibrational part must have either $3N - 6$ variables for a non-linear molecule or $3N - 5$ variables for a linear molecule. These are referred to as *vibrational degrees of freedom* or *internal coordinates*.


``````{admonition} 中文翻译
:class: dropdown

- 为考虑分子转动，需要三个变量，线性分子仅需要两个变量。因此，振动部分必须有非线性分子的 $3N - 6$ 变量或线性分子的 $3N - 5$ 变量。这些被称为*振动自由度*或*内坐标*。
``````

:::{note} **Example: counting the vibrations**

- **Water** (H$_2$O, nonlinear, $N=3$): $9$ coordinates $= 3$ translations $+ 3$ rotations $+ 3$ vibrations (symmetric stretch, bend, asymmetric stretch).
- **Carbon dioxide** (CO$_2$, linear, $N=3$): $9 = 3 + 2 + 4$ vibrations (a linear molecule spins about only two useful axes, so one extra coordinate lands in the vibrational pool).
- **Benzene** ($N=12$): $3N - 6 = 30$ vibrational modes, which is why its infrared spectrum is so rich.


``````{admonition} 中文翻译
:class: dropdown

- **水** (H$_2$O，非线性，$N=3$)：$9$ 个坐标 $= 3$ 个平动 $+ 3$ 个转动 $+ 3$ 个振动（对称伸缩、弯曲、反对称伸缩）。
- **二氧化碳** (CO$_2$，线性，$N=3$)：$9 = 3 + 2 + 4$ 个振动（线性分子仅绕两个有用轴旋转，所以一个额外的坐标进入振动池）。
- **苯** ($N=12$)：$3N - 6 = 30$ 种振动模式，这也是其红外光谱如此丰富的原因。
``````

:::

## Classical vibrations: the harmonic oscillator

Translations and rotations carry no potential energy, and the electronic problem is deferred to later chapters. The vibrational Hamiltonian is where the potential $E(R_1, ..., R_N)$ lives, and near any stable geometry that potential looks like a spring. Before quantizing the oscillator in the next lecture, we need full command of its classical mechanics.


``````{admonition} 中文翻译
:class: dropdown

平移和旋转不携带势能，电子问题推迟到后续章节。振动哈密顿量是势能 $E(R_1, ..., R_N)$ 所在的地方，且在任何稳定几何结构附近，该势能看起来像弹簧。在下一讲量子化振动子之前，我们需要完全掌握其经典力学。
``````

### Bead, spring and a wall

- The classical **harmonic oscillator** is a system of a bead attached to a wall with a spring. 
- When the bead is displaced from its equilibrium or resting position $r_0$ to some point $r$, it experiences a restoring force $F$ proportional to the displacement $x=r-r_0$:


``````{admonition} 中文翻译
:class: dropdown

- 经典的**谐振子**是一个由小珠通过弹簧连接在墙上的系统。
- 当珠子从其平衡或静止位置 $r_0$ 移动到某点 $r$ 时，它会受到与位移 $x=r-r_0$ 成正比的恢复力 $F$：
``````


:::{figure} images/harm-osc1.png
:label: fig-classical-harmonic-oscillator-1
:alt: compton
:width: 500px

Harmonic motion governed by Hooke's law. Any deviation from the equilibrium position is met with a restoring force, and in the absence of friction the bead oscillates indefinitely about equilibrium.


``````{admonition} 中文翻译
:class: dropdown

由胡克定律支配的谐振动。任何偏离平衡位置都会受到恢复力，在没有摩擦的情况下，珠子会无限期地关于平衡位置振动。
``````
:::



$$
F=-kx
$$

- This is **Hooke's law**, where the minus sign indicates that the direction of the force is always toward restoring the equilibrium location. 
- The constant $k$ characterizes the stiffness of the spring and is called the **spring constant.**


``````{admonition} 中文翻译
:class: dropdown

- 这就是 **胡克定律**，其中负号表示力的方向总是指向恢复平衡位置。
- 常数 $k$ 表征弹簧的刚度，称为 **弹簧常数**。
``````

### Solving harmonic oscillator problem

- The classical equation of motion for a one-dimensional simple harmonic oscillator with a particle of mass m attached to a spring having spring constant k generates mechanical waves.


``````{admonition} 中文翻译
:class: dropdown

- 一维简单谐振子的运动方程，质量为 m 的粒子附于弹簧常数为 k 的弹簧上，产生机械波。
``````

$$m \ddot x=−kx$$

$$m \ddot x+kx = 0 \,\,\,\,\rightarrow \,\,\,\, \ddot{x}+\omega^2 x =0$$

- The introduced constant $\omega$ will be seen as the **frequency of oscillations**. Note that the frequency is inversely proportional to mass (heavier objects with the same spring constant oscillate more slowly around equilibrium) and increases with the spring constant (stiffer springs increase oscillations around equilibrium for the same mass).


``````{admonition} 中文翻译
:class: dropdown

- 引入的常数 $\omega$ 将被视为 **振动频率**。注意频率与质量成反比（相同弹簧常数下，重物围绕平衡位置摆动得更慢），并随弹性系数增加而增大（相同质量下，更硬的弹簧增加围绕平衡位置的摆动）。
``````

$$\omega=\Big(\frac{k}{m}\Big)^{1/2}$$

- The differential equation is a simple second-order, linear ODE which can be solved by the standard trick of plugging in an exponential $x(t)=e^{\alpha t}$ and converting the problem to an algebraic equation. The solution is


``````{admonition} 中文翻译
:class: dropdown

- 这是一个简单的二阶线性常微分方程，可通过标准方法求解：代入指数函数 $x(t)=e^{\alpha t}$ 并将问题转化为代数方程。其解为
``````

$$
x(t)= A sin(\omega t+\phi)
$$ 

- The two constants are: $A$, the **amplitude of oscillations**, and $\phi$, a constant specifying the initial position of the bead. 


``````{admonition} 中文翻译
:class: dropdown

- 这两个常数是：$A$，**振幅**，和 $\phi$，一个指定小珠初始位置的常数。
``````

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML

def sho_anim(m, k=1.0, A=0.9, phi=0.0, duration=4.0, fps=30):
    ω = np.sqrt(k/m)
    t = np.linspace(0, duration, int(fps*duration))
    x = A*np.sin(ω*t + phi)

    fig, axes = plt.subplots(1, 2, figsize=(8, 2.5))
    ax_mass, ax_wave = axes

    # --- left: oscillating mass ---
    ax_mass.set_xlim(-1.2, 1.2)
    ax_mass.set_ylim(-0.5, 0.5)
    ax_mass.axis("off")
    ax_mass.set_title(f"Mass–Spring (m={m:g})")
    (mass_point,) = ax_mass.plot([], [], "o", ms=12)
    (trace_line,) = ax_mass.plot([], [], lw=2)

    # --- right: sinusoidal wave ---
    ax_wave.set_xlim(0, duration)
    ax_wave.set_ylim(-1.2*A, 1.2*A)
    ax_wave.set_xlabel("time t")
    ax_wave.set_ylabel("x(t)")
    ax_wave.grid(True, ls="--", alpha=0.4)
    ax_wave.set_title("x(t) = A sin (ωt + φ)")
    (wave_line,) = ax_wave.plot([], [], lw=2)
    (wave_point,) = ax_wave.plot([], [], "o")

    def init():
        for line in (mass_point, trace_line, wave_line, wave_point):
            line.set_data([], [])
        return mass_point, trace_line, wave_line, wave_point

    def update(i):
        xi = x[i]
        mass_point.set_data([xi], [0])
        trace_line.set_data(x[:i+1], np.zeros(i+1))
        wave_line.set_data(t[:i+1], x[:i+1])
        wave_point.set_data([t[i]], [xi])
        return mass_point, trace_line, wave_line, wave_point

    return FuncAnimation(fig, update, init_func=init, frames=len(t), interval=1000/fps, blit=True)

# --- Two animations: normal mass and heavier mass ---
anim1 = sho_anim(m=1.0, duration=10.0)
anim2 = sho_anim(m=10.0, duration=10.0)  # slower oscillation

# Inline display in Jupyter / Jupyter Book
plt.close()  # Prevents static display of the last frame
HTML(anim1.to_jshtml() + "<br><hr><br>" + anim2.to_jshtml())
```

### Energy of the harmonic oscillator

- In classical mechanics, when we have a conservative system (no friction, energy conserved) the **force is the gradient of a potential energy**


``````{admonition} 中文翻译
:class: dropdown

- 在经典力学中，当我们有一个保守系统（无摩擦，能量守恒）时，**力是势能的梯度**
``````

$$F = - \frac{\partial V(x)}{\partial x}$$

- This means the steeper the potential, the larger the force, and the minus sign indicates that the force restores the system to its equilibrium position. 

- The potential energy can be obtained by integrating:


``````{admonition} 中文翻译
:class: dropdown

- 这意味着势能越陡峭，力越大，负号表示力将系统恢复到平衡位置。
- 势能可以通过积分获得：
``````

$$ V(x)= - \int F dx = - \int (-kx) dx =\frac{kx^2}{2}+C$$

- Thus the potential energy for a simple harmonic oscillator is a parabolic function of displacement. It is convenient to set $C=0$ and measure potential energy relative to the equilibrium state $V(x=0)=0$. 

- The total energy, consisting of kinetic and potential energies, will be used to obtain the Schrodinger equation.


``````{admonition} 中文翻译
:class: dropdown

- 因此，简单谐振子的势能是位移的二次函数。为方便起见，设 $C=0$ 并相对于平衡态测量势能 $V(x=0)=0$。
- 总能量由动能和势能组成，将用于得到薛定谔方程。
``````

$$E=\frac{p^2}{2m} + \frac{kx^2}{2}$$

:::{figure} images/ext_shm_graphs.gif
:label: fig-classical-harmonic-oscillator-2
:alt: compton
:width: 300px

A harmonic oscillator in vacuum is conservative: kinetic and potential energy interconvert with no total energy dissipated into the environment. Position $x(t)$, velocity $v=\dot{x}(t)$, and acceleration $a=\ddot{x(t)}$ all oscillate at the same constant frequency $\omega$ but with different amplitudes.


``````{admonition} 中文翻译
:class: dropdown

真空中的谐振子是守恒的：动能和势能相互转换，无能量耗散到环境中。位置 $x(t)$、速度 $v=\dot{x}(t)$ 和加速度 $a=\ddot{x(t)}$ 都以相同的常数频率 $\omega$ 振荡，但振幅不同。
``````
:::


### Diatomic molecules and two-body problem

:::{figure} images/osc-2.jpeg
:label: fig-classical-harmonic-oscillator-3
:alt: compton
:width: 300px

We can reduce the two-body problem of vibrating atoms to a one-body problem of a single particle with an effective reduced mass $\frac{1}{\mu}=\frac{1}{m_1}+\frac{1}{m_2}$, so $\mu=\frac{m_1 m_2}{m_1+m_2}$.


``````{admonition} 中文翻译
:class: dropdown

我们可以将振动原子的两体问题简化为单粒子的一体问题，其有效简并质量满足 $\frac{1}{\mu}=\frac{1}{m_1}+\frac{1}{m_2}$，所以 $\mu=\frac{m_1 m_2}{m_1+m_2}$。
``````

$$\ddot{x}=\ddot{x_2} - \ddot{x_1} =-\Big(\frac{1}{m_1}+\frac{1}{m_2} \Big)kx=-\frac{k}{\mu}x$$


:::{tip} **Derivation**
:class: dropdown

Equations of motion for diatomic molecule modeled as beads bound by a spring are:


``````{admonition} 中文翻译
:class: dropdown

模拟为由弹簧连接的珠子的双原子分子的运动方程为：
``````

$$F_1=m_1 \ddot{x_1}=k(x_2-x_1-l_0)$$

$$F_2=m_2 \ddot{x_2}=-k(x_2-x_1-l_0)$$

where $F_1=-F_2$, a reflection of Newton's third law. By introducing more convenient coordinates in the form of the relative distance $x$ and the center of mass $x_{com}$, we now reduce the two-body problem to a one-body problem.


``````{admonition} 中文翻译
:class: dropdown

其中 $F_1=-F_2$，这是牛顿第三定律的反映。通过引入更方便的坐标，即相对距离 $x$ 和质心 $x_{com}$，我们将两体问题简化为单体问题。
``````

$$x=x_2-x_1-l_0$$

$$x_{com}=\frac{m_1x_2+x_2 m_2}{m_1+m_2}$$
:::

- The diatomic molecule is stable because the same force acts on both ends


``````{admonition} 中文翻译
:class: dropdown

- 双原子分子之所以稳定，是因为相同的力作用在两端
``````

$$m_1\ddot{x_1}=kx \\  m_2\ddot{x_2}=-kx$$

- By expressing the equations of motion in terms of the center of mass, we find that the center of mass moves freely without acceleration. 


``````{admonition} 中文翻译
:class: dropdown

- 通过用质心坐标表达运动方程，可知质心做无加速度的自由运动。
``````

$$m_1\ddot{x_1}+ m_2\ddot{x_2}=0\,\,\,\, \rightarrow \frac{m_1\ddot{x_1}+ m_2\ddot{x_2}}{m_1+m_2}=\ddot{x}_{com}=0$$

- Next, by taking the difference between the coordinates $\ddot{x_2}=-\frac{k}{m_2}x_2$ and $\ddot{x_1}=\frac{k}{m_1}x_1$, we express the equations of motion in terms of the relative distance


``````{admonition} 中文翻译
:class: dropdown

- 接下来，通过坐标 $\ddot{x_2}=-\frac{k}{m_2}x_2$ 和 $\ddot{x_1}=\frac{k}{m_1}x_1$ 的差来表达运动方程，以相对距离
``````


$$\ddot{x}=\ddot{x_2} - \ddot{x_1} =-\Big(\frac{1}{m_1}+\frac{1}{m_2} \Big)kx=-\frac{k}{\mu}x$$

- This equation looks identical to the problem of a bead anchored to a wall with a spring. We have thus managed to reduce the two-body problem to a one-body problem by replacing the masses of the bodies with a reduced mass $\frac{1}{\mu}=\frac{1}{m_1}+\frac{1}{m_2}$, so $\mu=\frac{m_1 m_2}{m_1+m_2}$


``````{admonition} 中文翻译
:class: dropdown

- 这道方程与珠子固定在墙上弹簧的问题完全相同。我们通过将两个物体的质量替换为有效质量 $\frac{1}{\mu}=\frac{1}{m_1}+\frac{1}{m_2}$，从而将两体问题简化为单体问题，所以 $\mu=\frac{m_1 m_2}{m_1+m_2}$
``````
:::

### Beads and springs model of molecules

- Before discussing the harmonic oscillator approximation, let us reflect on when it is a good approximation and under which circumstances it breaks down. For an arbitrary potential energy function of $x$, we can carry out a Taylor expansion around the equilibrium bond length $x_0$, obtaining an infinite series. 


``````{admonition} 中文翻译
:class: dropdown

- 在讨论谐振子近似之前，让我们思考何时是一个好的近似以及在何种情况下会失效。对于任意的势能函数 $x$，我们可以关于平衡键长 $x_0$ 展开 Taylor 级数，得到一个无限级数。
``````

$$U(x) = U(x_0)+U'(x_0)(x-x_0)+\frac{1}{2!}U''(x_0)(x-x_0)^2+\frac{1}{3!}U'''(x_0)(x-x_0)^3+...$$


:::{figure} images/harm_approx.png
:label: fig-classical-harmonic-oscillator-4
:alt: harmls
:width: 300px

Deviation of the true potential (blue) from the simple harmonic approximation (red), with the cubic correction shown in green.


``````{admonition} 中文翻译
:class: dropdown

真实势能（蓝色）与简谐近似（红色）的偏差，三次修正项用绿色表示。
``````
:::

- Setting the energy scale relative to $U(x_0)=0$ and recognizing that the first derivative vanishes at the minimum $x_0$, we have


``````{admonition} 中文翻译
:class: dropdown

- 将能量标度设定为相对于 $U(x_0)=0$，并认识到在最小值 $x_0$ 处一阶导数为零，我们得到
``````

$$U(x) = \frac{1}{2!}k(x-x_0)^2+\frac{1}{3!}\gamma(x-x_0)^3+...$$

- Hence we see that the harmonic approximation keeps only the first non-vanishing term! Furthermore, the spring constant $k$ and the subsequent anharmonicity constants such as $\gamma$ are higher-order derivatives of the potential energy. That is, the more nonlinear the potential, the larger the contribution of these terms. Conversely, the closer the potential is to a quadratic form, the more accurate the harmonic assumption. 


``````{admonition} 中文翻译
:class: dropdown

- 因此我们看到，谐近似只保留第一个非零项！此外，弹性常数 $k$ 以及随后的非谐性常数如 $\gamma$ 是势能的高阶导数。也就是说，势能非线性越强，这些项的贡献越大。反之，势能越接近二次形式，谐近似的精度就越高。
``````

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt

# Define the range for x values, focusing on the dissociation region
x = np.linspace(0, 2.5, 500)

# Define the harmonic potential (quadratic term)
harmonic = 0.5 * x**2

# Define the harmonic + cubic potential
harmonic_cubic = 0.5 * x**2 - 0.2 * x**3

# Define the harmonic + cubic + quartic potential
harmonic_cubic_quartic = 0.5 * x**2 - 0.2 * x**3 + 0.05 * x**4

# Define the harmonic + cubic + quartic + higher-order polynomial (5th and 6th order)
polynomial_approx = 0.5 * x**2 - 0.2 * x**3 + 0.05 * x**4 - 0.01 * x**5 + 0.001 * x**6

# Define the Morse potential
def morse_potential(x, D=1, a=1):
    return D * (1 - np.exp(-a * x))**2

# Set parameters for Morse potential
D = 1  # Depth of the potential well
a = 1  # Width of the potential well

# Compute Morse potential
morse = morse_potential(x, D, a)

# Plot all the potentials, showing progression
plt.figure(figsize=(8, 6))

# Harmonic only
plt.plot(x, harmonic, label='Harmonic: $0.5  x^2$', color='b', lw=2)

# Harmonic + Cubic
plt.plot(x, harmonic_cubic, label='Harmonic + Cubic: $0.5  x^2 - 0.2  x^3$', color='g', lw=2)

# Harmonic + Cubic + Quartic
plt.plot(x, harmonic_cubic_quartic, label='Harmonic + Cubic + Quartic: $0.5  x^2 - 0.2  x^3 + 0.05  x^4$', color='r', lw=2)

# Polynomial approximation (up to 6th order)
plt.plot(x, polynomial_approx, label='Polynomial Approx (up to $x^6$)', color='c', lw=2)

# Morse potential
plt.plot(x, morse, label='Morse Potential', color='k', lw=3)

# Add labels and legend
plt.title('Polynomial Approximation of Harmonic Oscillator vs. Morse Potential')
plt.xlabel('x (dissociation region)')
plt.ylabel('Potential Energy')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True)
plt.legend()
plt.ylim([0, 2])
```

## Problems

#### Problem 1: Count the degrees of freedom

How many vibrational modes do (a) HCl, (b) ammonia NH$_3$ (nonlinear), and (c) acetylene C$_2$H$_2$ (linear) have?


``````{admonition} 中文翻译
:class: dropdown

(a) HCl、(b) 氨 NH$_3$（非线性）和 (c) 乙炔 C$_2$H$_2$（线性）各有多少个振动模式？
``````

:::{admonition} **Solution**
:class: dropdown solution

(a) HCl: $N=2$, linear, so $3N - 5 = 1$ vibration (the bond stretch).
(b) NH$_3$: $N=4$, nonlinear, so $3N - 6 = 6$ vibrations.
(c) C$_2$H$_2$: $N=4$, linear, so $3N - 5 = 7$ vibrations.


``````{admonition} 中文翻译
:class: dropdown

(a) HCl: $N=2$，线性，所以 $3N - 5 = 1$ 振动（键拉伸）。
(b) NH$_3$: $N=4$，非线性，所以 $3N - 6 = 6$ 振动。
(c) C$_2$H$_2$: $N=4$，线性，所以 $3N - 5 = 7$ 振动。
``````
:::

#### Problem 2: Vibrational frequency of HCl

The force constant of the H$^{35}$Cl bond is $k = 516$ N/m. Compute the reduced mass and the angular frequency $\omega = \sqrt{k/\mu}$, and convert to a wavenumber $\tilde{\nu} = \omega / (2\pi c)$.


``````{admonition} 中文翻译
:class: dropdown

H$^{35}$Cl 键的力常数为 $k = 516$ N/m。计算简并质量和角频率 $\omega = \sqrt{k/\mu}$，并转换为波数 $\tilde{\nu} = \omega / (2\pi c)$。
``````

:::{admonition} **Solution**
:class: dropdown solution

$\mu = \frac{m_H m_{Cl}}{m_H + m_{Cl}} = \frac{(1.008)(34.97)}{35.98}\,\text{amu} = 0.980\,\text{amu} = 1.63\times 10^{-27}\,\text{kg}$


``````{admonition} 中文翻译
:class: dropdown

$\mu = \frac{m_H m_{Cl}}{m_H + m_{Cl}} = \frac{(1.008)(34.97)}{35.98}\,\text{amu} = 0.980\,\text{amu} = 1.63\times 10^{-27}\,\text{kg}$
``````

$\omega = \sqrt{k/\mu} = \sqrt{516 / 1.63\times 10^{-27}} = 5.63\times 10^{14}\,\text{rad/s}$


``````{admonition} 中文翻译
:class: dropdown

$\omega = \sqrt{k/\mu} = \sqrt{516 / 1.63\times 10^{-27}} = 5.63\times 10^{14}\,\text{rad/s}$
``````

$\tilde{\nu} = \frac{\omega}{2\pi c} = \frac{5.63\times 10^{14}}{2\pi \cdot 3\times 10^{10}\,\text{cm/s}} \approx 2990\,\text{cm}^{-1}$, matching the observed HCl stretch near $2886$ cm$^{-1}$.


``````{admonition} 中文翻译
:class: dropdown

$\tilde{\nu} = \frac{\omega}{2\pi c} = \frac{5.63\times 10^{14}}{2\pi \cdot 3\times 10^{10}\,\text{cm/s}} \approx 2990\,\text{cm}^{-1}$，与观察到的 HCl 拉伸峰 $2886$ cm$^{-1}$ 匹配。
``````
:::

#### Problem 3: Isotope shift

Without recomputing from scratch, predict how $\omega$ changes when H$^{35}$Cl is replaced by D$^{35}$Cl. The force constant $k$ does not change. Why not?


``````{admonition} 中文翻译
:class: dropdown

无需从头重新计算，预测当 H$^{35}$Cl 被 D$^{35}$Cl 取代时 $\omega$ 如何变化。力常数 $k$ 不变。为什么？
``````

#### Problem 4: Spring constant from a potential

A bond is described by $U(x) = D\left(1 - e^{-ax}\right)^2$ (the Morse potential, with $x$ the displacement from equilibrium). Taylor expand around $x=0$ to show that the effective spring constant is $k = 2Da^2$.


``````{admonition} 中文翻译
:class: dropdown

一个键由 $U(x) = D\left(1 - e^{-ax}\right)^2$ 描述（Morse 潜势，$x$ 为平衡位移处的位移）。在 $x=0$ 处展开泰勒级数，以证明有效弹性常数为 $k = 2Da^2$。
``````

#### Problem 5: Energy bookkeeping

A classical oscillator has amplitude $A$. At what displacement $x$ is the energy split exactly half kinetic, half potential? Sketch $V(x)$, $T(x)$, and $E$ on one plot.

``````{admonition} 中文翻译
:class: dropdown

一个经典谐振子的幅度为 $A$。能量在何处的位移 $x$ 时恰好动能势能各半？在同一张图上绘制 $V(x)$、$T(x)$ 和 $E$。
``````

