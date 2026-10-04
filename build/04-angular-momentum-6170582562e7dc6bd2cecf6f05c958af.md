---
kernelspec:
  name: python3
  display_name: Python 3
---

# Angular Momentum

:::{note} **What You Need to Know**

- **Angular momentum** is essential in both classical and quantum mechanics. In classical mechanics, all isolated systems conserve angular momentum (along with energy and linear momentum). This conservation law simplifies calculations for systems such as planetary orbits, rotations of rigid bodies, and many other dynamic systems.
- In **quantum mechanics**, angular momentum is similarly fundamental, especially in understanding atomic structure and other systems with rotational symmetry. 
- Angular momentum in QM is represented by an operator, a vector operator to be specific, much like the momentum operator. 
- However, unlike the linear momentum operator, the three components of the angular momentum operator **do not commute**.


``````{admonition} 中文翻译
:class: dropdown

- **角动量** 在经典力学和量子力学中都至关重要。在经典力学中，所有孤立系统都守恒角动量（以及能量和线动量）。这种守恒定律简化了行星轨道、刚体旋转以及许多其他动力系统的计算。
- 在**量子力学**中，角动量同样具有基础性地位，特别是在理解原子结构和其他具有旋转对称性的体系时。
- 量子力学中的角动量由算符表示，具体来说是矢量算符，这与动量算符非常相似。
- 然而，与线动量算符不同，角动量算符的三个分量**不交换**。
``````

:::

| **Property**                | **Linear Momentum**                               | **Angular Momentum**                              |   
| --------------------------- | ------------------------------------------------- | ------------------------------------------------- | 
| **Physical nature**         | Motion along a straight line                      | Rotation about an axis                            |    
| **Vector form**             | $\vec{p} = m\vec{v}$                              | $\vec{L} = \vec{r} \times \vec{p}$                |  
| **Effective mass**          | $m$                                               | $I = m r^2$                                       |   
| **Velocity**                | $v$                                               | $\omega=\frac{v}{r}$                              |
| **Magnitude (scalar form)** | $\mid\vec{p}\mid   = m v$                         | $\mid\vec{L}\mid  = I \omega$                     |
| **Kinetic energy**          | $E_k = \dfrac{p^2}{2m}$                           | $E_\text{rot} = \dfrac{L^2}{2I}$                  |    
| **Quantum operator**        | $\hat{p}_x = -i\hbar\dfrac{\partial}{\partial x}$ | $\hat{L}_x = \hat{y}\hat{p}_z - \hat{z}\hat{p}_y$ |    
| **Conservation law**        | Conserved if no net **external force** acts       | Conserved if no net **external torque** acts      |    
| **Conservation condition**  | $\sum \vec{F}_\text{ext} = 0$                     | $\sum \vec{\tau}_\text{ext} = 0$                  |    

:::{tip} **velocity vs angular velocity**
:class: dropdown

In circular motion, **angular velocity** ($\omega$) measures how fast the angle changes, while **linear velocity** ($v$) measures how fast the object moves along the circular path.


``````{admonition} 中文翻译
:class: dropdown

在圆周运动中，**角速度** ($\omega$) 表示角度变化的快慢，而**线速度** ($v$) 表示物体沿圆周运动的快慢。
``````

For a full rotation, the **arc length** traveled is related to the **angle** by


``````{admonition} 中文翻译
:class: dropdown

对于完整的一圈旋转，所经过的 **弧长** 与 **角度** 的关系为
``````

$$s = r\theta.$$

Differentiating with respect to time gives

$$\frac{ds}{dt} = r\frac{d\theta}{dt},$$

or equivalently,

$$v = r\omega \quad \Rightarrow \quad \omega = \frac{v}{r}.$$

Thus, angular velocity is the **rate of rotation per unit radius**: objects farther from the axis move faster linearly for the same angular speed.


``````{admonition} 中文翻译
:class: dropdown

因此，角速度是**单位半径的旋转速率**：对于相同的角速度，离轴越远的物体线速度越快。
``````

:::


:::{tip} **Moment of inertia**
:class: dropdown


Consider a rigid body rotating about a fixed axis with **angular velocity** $\omega$. 
Each particle $i$ of mass $m_i$ at distance $r_i$ from the axis moves with **linear velocity**


``````{admonition} 中文翻译
:class: dropdown

考虑一个绕固定轴旋转的刚体，其**角速度** $\omega$。
每个质量为 $m_i$、距离轴 $r_i$ 的粒子 $i$ 都有**线速度**
``````


$$
v_i = r_i \omega.
$$

The **kinetic energy** of that particle is

$$
E_i = \tfrac{1}{2} m_i v_i^2 = \tfrac{1}{2} m_i (r_i \omega)^2 = \tfrac{1}{2} m_i r_i^2 \omega^2.
$$

For the whole body, total rotational kinetic energy is the sum over all particles:


``````{admonition} 中文翻译
:class: dropdown

对于整个物体，总转动动能是所有粒子转动动能之和：
``````

$$
E_\text{rot} = \sum_i E_i = \tfrac{1}{2} \omega^2 \sum_i m_i r_i^2.
$$

We define the term in parentheses as the **moment of inertia**:


``````{admonition} 中文翻译
:class: dropdown

我们将括号中的项定义为**转动惯量**：
``````

$$
I = \sum_i m_i r_i^2,
$$

$$
E_\text{rot} = \tfrac{1}{2} I \omega^2.
$$



**Interpretation**

The $r_i^2$ factor naturally appears from the **kinetic energy** of rotational motion: it weights each mass element by how far it lies from the axis, determining its contribution to rotational inertia.


``````{admonition} 中文翻译
:class: dropdown

$r_i^2$ 因子自然出自**旋转动能**的推导：它通过每个质点距离轴线的远近来加权，决定其对转动惯量的贡献。
``````

:::

### Conservation of momentum is due to symmetry


:::{tip} **Noether's beautiful theorem**

> **Every continuous symmetry of the laws of physics corresponds to a conserved quantity.**


``````{admonition} 中文翻译
:class: dropdown

> **物理定律的每一个连续对称性都对应一个守恒量。**
``````

- In quantum mechanics, this means that if a system's Hamiltonian is unchanged (invariant) under a certain transformation (e.g., time change, rotation, or translation), there exists a corresponding conserved observable:

    * **Translational symmetry** → conservation of **momentum**
    * **Rotational symmetry** → conservation of **angular momentum**
    * **Time-translation symmetry** → conservation of **energy**


``````{admonition} 中文翻译
:class: dropdown

- 在量子力学中，这意味着如果系统的哈密顿算子在某种变换（如时间变换、旋转或位移）下不变（不变），则存在一个相应的守恒可观测量：
- **平移对称性** → 守恒 **动量**
- **旋转对称性** → 守恒 **角动量**
- **时间平移对称性** → **能量**守恒
``````
:::


:::{figure} ./images/E-noether.png
:label: fig-angular-momentum-1
:alt: DeD0
:width: 300px

Emmy Noether, a German mathematician whose first and second theorems are fundamental to mathematical physics. See more about her [here](https://en.wikipedia.org/wiki/Emmy_Noether).


``````{admonition} 中文翻译
:class: dropdown

艾米·诺特，一位德国数学家，她的第一和第二定理是数学物理的基石。关于她的更多信息，请见 [这里](https://en.wikipedia.org/wiki/Emmy_Noether)。
``````
:::


:::{tip} **Conservation of momenta**
:class: dropdown

* **Linear momentum** is defined as $\vec{p} = m\vec{v}$


``````{admonition} 中文翻译
:class: dropdown

- **线动量**定义为 $\vec{p} = m\vec{v}$
``````


From Newton's second law,

$$
\frac{d\vec{p}}{dt} = \sum \vec{F}_\text{ext}.
$$

Thus, when **no external force** acts on a system,


``````{admonition} 中文翻译
:class: dropdown

因此，当 **没有外力** 作用在系统上时，
``````

$$
  \sum \vec{F}_\text{ext} = 0 ;\Rightarrow; \frac{d\vec{p}}{dt} = 0,
$$

meaning **linear momentum is conserved**.

* **Angular momentum** is defined as $\vec{L} = \vec{r} \times \vec{p}$.


``````{admonition} 中文翻译
:class: dropdown

- **角动量** 定义为 $\vec{L} = \vec{r} \times \vec{p}$。
``````


  Taking the time derivative gives

  $$
  \frac{d\vec{L}}{dt} = \vec{r} \times \frac{d\vec{p}}{dt} = \sum \vec{\tau}_\text{ext}.
  $$

Therefore, when **no external torque** acts on the system,


``````{admonition} 中文翻译
:class: dropdown

因此，当系统不受 **外力矩** 作用时，
``````
    
$$
  \sum \vec{\tau}_\text{ext} = 0 ;\Rightarrow; \frac{d\vec{L}}{dt} = 0,
$$
  so **angular momentum is conserved**.

**Summary:**

* No external **force** → **linear momentum** conserved.
* No external **torque** → **angular momentum** conserved.


``````{admonition} 中文翻译
:class: dropdown

- 无外部 **力** → **线性动量** 守恒。
- 无外部 **力矩** → **角动量** 守恒。
``````
:::

### Classical angular momentum 

:::{figure} ./images/L.png
:label: fig-angular-momentum-2
:alt: DeD0
:width: 300px

Classical angular momentum, a vector given by the cross product of position and linear momentum. Its direction follows the right-hand rule.


``````{admonition} 中文翻译
:class: dropdown

经典角动量，一个由位置和线动量叉积给出的矢量。其方向遵循右手定则。
``````
:::

- In classical mechanics, the [angular momentum](http://en.wikipedia.org/wiki/Angular_momentum) is defined via a cross product of position and linear momentum. The cross product is convenient to write using a [determinant](http://en.wikipedia.org/wiki/Determinant):


``````{admonition} 中文翻译
:class: dropdown

- 在经典力学中，[角动量](http://en.wikipedia.org/wiki/Angular_momentum) 是通过位置和线性动量的外积定义的。外积用[行列式](http://en.wikipedia.org/wiki/Determinant)的形式书写很方便：
``````

$${\vec{L} = \vec{r}\times\vec{p} =
\begin{vmatrix}
\vec{i} & \vec{j} & \vec{k}\\
x & y & z\\
p_x & p_y & p_z\\
\end{vmatrix}= \left(yp_z - zp_y\right)\vec{i} + \left(zp_x - xp_z\right)\vec{j} + \left(xp_y - yp_x\right)\vec{k}}$$


- where $\vec{i}, \vec{j}$ and $\vec{k}$ denote [unit vectors](http://en.wikipedia.org/wiki/Unit_vector) along the $x, y$ and $z$ axes. $p_x$ and $L_x$ are components of linear and angular momentum, respectively. 


``````{admonition} 中文翻译
:class: dropdown

- 其中 $\vec{i}, \vec{j}$ 和 $\vec{k}$ 分别表示 $x, y$ 和 $z$ 轴方向的[单位向量](http://en.wikipedia.org/wiki/Unit_vector)。$p_x$ 和 $L_x$ 分别是线动量和角动量的分量。
``````

:::{important} **The Cartesian components of angular momentum**

$${L_x = yp_z - zp_y}$$

$${L_y = zp_x - xp_z}$$

$${L_z = xp_y - yp_x}$$

$${\vec{L}^2 = \vec{L}\cdot\vec{L} = L_x^2 + L_y^2 + L_z^2}$$
:::

### Classical picture: Rotating dumbbell


:::{figure} ./images/conserv_L.png
:label: fig-angular-momentum-3
:alt: DeD0
:width: 300px

Conservation of angular momentum: with no external torque, total angular momentum stays constant, so lowering the moment of inertia speeds up rotation and raising it slows rotation down.


``````{admonition} 中文翻译
:class: dropdown

角动量守恒：在没有外力偶的情况下，总角动量保持不变，因此降低转动惯量会加速旋转，而升高转动惯量会减慢旋转。
``````
:::


- The rigid rotor is a model of a rotating dumbbell: two unequal masses held together via a rigid stick.  The system is not acted upon by any external potential; hence the only energy is the kinetic energy of rotation: 


``````{admonition} 中文翻译
:class: dropdown

- 刚体转动是一个旋转双子星的模型：两个不等质量通过刚性杆相连。系统不受外势作用；因此只有旋转的动能：
``````

$$
K=\frac{m_1 v_1^2}{2}+\frac{m_2 v_2^2}{2}=\frac{m_1 r_1^2+m_2 r^2_2}{2}\omega^2
$$

- where we have plugged in $v_1=\omega r_1$ and $v_2=\omega_2 r$, the rotational velocities of the two masses rotating with frequency $\omega$. The classical mechanical problem of two masses is once again reducible to a single reduced mass $\mu$ rotating at constant radius $r=r_1+r_2$ around the center of mass $m_1 r_1=m_2 r_2$.


``````{admonition} 中文翻译
:class: dropdown

- 其中我们代入了 $v_1=\omega r_1$ 和 $v_2=\omega_2 r$，两个转动频率为 $\omega$ 的质量的转动速度。两个质量的经典力学问题再次可简化为一个转动惯性量 $\mu$ 以常数半径 $r=r_1+r_2$ 绕质心 $m_1 r_1=m_2 r_2$ 旋转。
``````



$$
K=\frac{I \omega^2}{2}=\frac{L^2}{2I}
$$


- here $L=I \omega$ is the angular momentum, $I=\mu r^2$ is the moment of inertia, and $\mu=\frac{m_1 m_2}{m_1+m_2}$.


``````{admonition} 中文翻译
:class: dropdown

- 此处 $L=I \omega$ 为角动量，$I=\mu r^2$ 为转动惯量，且 $\mu=\frac{m_1 m_2}{m_1+m_2}$。
``````

:::{figure} ./images/Angular_momentum_conservation.gif
:label: fig-angular-momentum-4
:alt: DeD0
:width: 450px

Angular momentum conservation
:::

### Spherical coordinates

- Spherical coordinates are more convenient for rotational problems where we replace $(x,y,z)$ by $(r, \phi, \theta)$. 
- For instance when considering rotation with fixed orbit $r=const$ we are able to eliminate one degree of freedom associated with radial direction.


``````{admonition} 中文翻译
:class: dropdown

- 球坐标对于旋转问题更方便，我们用 $(r, \phi, \theta)$ 替换 $(x,y,z)$。
- 例如，当考虑固定轨道 $r=const$ 的旋转时，我们能够消除与径向方向相关的一个自由度。
``````

:::{figure} ./images/spherical_coord.png
:label: fig-angular-momentum-5
:alt: DeD0
:width: 450px

The spherical coordinate system, defined by radial coordinate $r$, azimuthal angle $\phi$, and polar angle $\theta$.


``````{admonition} 中文翻译
:class: dropdown

球坐标系，由径向坐标 $r$、方位角 $\phi$ 和极角 $\theta$ 定义。
``````
:::

:::{important} **Cartesian to spherical conversion**

$$x={\color{blue} r}{\color{green}sin\theta} {\color{orange} cos\phi}$$
$$y={\color{blue} r}{\color{green} sin\theta}  {\color{orange} sin\phi}$$
$$z={\color{blue} r} {\color{green} cos\theta}$$

$$Radius:\,\,\,{\color{blue} 0<{r}<\infty}$$
$$Azimuthal\, angle:{\color{orange}\,\,\,0<\phi<2\pi}$$
$$Polar\, angle:\,\,\,{\color{green} 0<\theta<\pi}$$

:::


:::{important} **Volume Element**

$$
dV = {\color{blue} r^2} {\color{blue} dr} \cdot {\color{green}\sin \theta} {\color{green}d\theta} \cdot {\color{orange}d\phi}
$$

:::



**Laplacian**

::::{tab-set} 
:::{tab-item} Cartesian

$$
\nabla^2 = \frac{{\partial^2}}{{\partial x^2}} + \frac{{\partial^2}}{{\partial y^2}} + \frac{{\partial^2}}{{\partial z^2}}
$$

:::

:::{tab-item} Polar
$$
\nabla^2 = {\color{blue}\frac{1}{r^2} \frac{\partial}{\partial r} \left(r^2 \frac{\partial}{\partial r}\right)} + {\color{green}\frac{1}{{\color{blue} r^2} \sin(\theta)}} {\color{green} \frac{\partial}{\partial \theta} \left(\sin(\theta) \frac{\partial}{\partial \theta}\right)} + { \frac{{\color{green} 1}}{{\color{blue} r^2} {\color{green} \sin^2(\theta)}} {\color{orange}\frac{\partial^2}{\partial \phi^2}}}
$$ 
:::
::::

:::{note} **Example**
Compute the volume of a cube and a sphere using Cartesian and spherical coordinates by integrating volume elements.


``````{admonition} 中文翻译
:class: dropdown

通过积分体积元，分别用直角坐标和球坐标计算立方体和球体的体积。
``````
:::

:::{note} **Solution**
:class: dropdown

$$\int^a_0\int^b_0\int^c_0 dxdydz=a\cdot b\cdot c$$

$$\int^r_0\int^{2\pi}_0\int^\pi_0 r^2 \sin \theta \, dr \, d\theta \, d\phi=\frac{r^3}{3}\Big|^r_0 \cdot 2\pi \cdot (-cos\theta) \Big|^\pi_0\cdot 2\pi=\frac{4\pi r^3}{3}$$
:::

:::{note} **Example**

Write down the Laplacian for a rigid rotor problem $r=const$. Show what equations result when you separate the two angular variables by plugging in $\psi(r, \theta, \phi)$.


``````{admonition} 中文翻译
:class: dropdown

对于刚体问题 $r=const$ 的拉普拉斯算子。当你把 $\psi(r, \theta, \phi)$ 代入并分离两个角变量时，得到什么方程：
``````
:::

:::{note} **Solution**
:class: dropdown

$$
\nabla^2 =  {\color{blue}\frac{1}{{ r^2}}}\Big[  {\color{green}\frac{1}{\sin(\theta)}}{\color{green}\frac{{\partial}}{{\partial \theta}} \left(\sin(\theta) \frac{{\partial}}{{\partial \theta}}\right)} + {{\color{green}\frac{1}{{ \sin^2(\theta)}}} {\color{orange} \frac{{\partial^2}}{{\partial \phi^2}}}}\Big] = {\color{blue}\frac{1}{r^2}}\nabla^2_{\theta, \phi}
$$
:::

### Quantum angular momentum 

- In quantum mechanics, the classical angular momentum is replaced by the corresponding
quantum mechanical operator.

- In [spherical coordinates](http://en.wikipedia.org/wiki/Spherical_coordinate_system), the angular momentum operators can be written in the following form. The derivations are [quite tedious](https://planetmath.org/derivationofthelaplacianfromrectangulartosphericalcoordinates), involving multiple applications of the chain rule, but they are just a straightforward mathematical procedure. Note that the choice of $z$-axis here was arbitrary. Sometimes the physical system implies such an axis naturally (for example, the direction of an external magnetic field). 


``````{admonition} 中文翻译
:class: dropdown

- 在量子力学中，经典角动量被相应的量子力学算符所取代。
- 在[球坐标系](http://en.wikipedia.org/wiki/Spherical_coordinate_system)中，角动量算子可以写成以下形式。推导过程[相当繁琐](https://planetmath.org/derivationofthelaplacianfromrectangulartosphericalcoordinates)，涉及多次链式法则的应用，但它们只是 straightforward 的数学过程。注意这里 $z$ 轴的选择是任意的。有时物理系统会自然暗示这样的轴（例如，外磁场的方向）。
``````


::::{tab-set} 
:::{tab-item} Cartesian

$${\hat{L}_x = -i\hbar\left(y\frac{\partial}{\partial z} - z\frac{\partial}{\partial y}\right)}$$

$${\hat{L}_y = -i\hbar\left(z\frac{\partial}{\partial x} - x\frac{\partial}{\partial z}\right)}$$

$${\hat{L}_z = -i\hbar\left(x\frac{\partial}{\partial y} - y\frac{\partial}{\partial x}\right)}$$

$$\hat{L}^2=\hat{L_x}^2+\hat{L_y}^2+\hat{L_z}^2$$
:::

:::{tab-item} Polar
$${\hat{L}_x = i\hbar\left(\sin(\phi)\frac{\partial}{\partial\theta} + \cot(\theta)\cos(\phi)\frac{\partial}{\partial\phi}\right)}$$

$${\hat{L}_y = i\hbar\left(-\cos(\phi)\frac{\partial}{\partial\theta} + \cot(\theta)\sin(\phi)\frac{\partial}{\partial\phi}\right)}$$

$${\hat{L}_z = -i\hbar\frac{\partial}{\partial\phi}}$$

$${\vec{\hat{L}}^2 = -\hbar^2\underbrace{\left[\frac{1}{\sin(\theta)}\frac{\partial}{\partial\theta}\left(\sin(\theta)\frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2(\theta)}\frac{\partial^2}{\partial\phi^2}\right]}_{\equiv \Lambda^2}}$$
:::
::::


:::{note} **Example**

Find the eigenfunctions and eigenvalues of the operator $\hat{L}_z$:


``````{admonition} 中文翻译
:class: dropdown

求算符 $\hat{L}_z$ 的本征函数和本征值：
``````

$$\hat{L}_z = -i\hbar\frac{\partial}{\partial\phi}$$

:::

:::{note} **Solution**
:class: dropdown

The eigenvalue equation is:

$$\hat{L}_z f(\phi) = a f(\phi)$$

Substituting the operator gives

$$-i\hbar\frac{df}{d\phi} = a f(\phi)$$


$$f(\phi) = e^{im\phi}, \quad a = \hbar m$$

Thus, the eigenfunctions of $\hat{L}_z$ are $e^{im\phi}$ and the corresponding eigenvalues are $\hbar m$, where $m$ is an integer quantum number.


``````{admonition} 中文翻译
:class: dropdown

因此，$\hat{L}_z$ 的本征函数是 $e^{im\phi}$，对应的本征值是 $\hbar m$，其中 $m$ 是整数量子数。
``````

:::

### Components of angular momentum do not commute!

- Unlike linear momentum, the components of angular momentum do not commute! 
- This implies that it is not possible to measure any of the Cartesian angular momentum pairs simultaneously with an infinite precision (the Heisenberg uncertainty relation).


``````{admonition} 中文翻译
:class: dropdown

- 与线动量不同，角动量的各分量不交换！
- 这意味着不可能同时无限精确地测量任意笛卡尔角动量对（海森堡不确定性原理）。
``````

:::{important} **Commutation relations of angular momentum**

$$
{\left[\hat{L}_x,\hat{L}_y\right] = i\hbar\hat{L}_z, \left[\hat{L}_y,\hat{L}_z\right] = i\hbar\hat{L}_x,\left[\hat{L}_z,\hat{L}_x\right] = i\hbar\hat{L}_y} \\ 


``````{admonition} 中文翻译
:class: dropdown

{\left[\hat{L}_x,\hat{L}_y\right] = i\hbar\hat{L}_z, \left[\hat{L}_y,\hat{L}_z\right] = i\hbar\hat{L}_x,\left[\hat{L}_z,\hat{L}_x\right] = i\hbar\hat{L}_y} \\
``````

{\left[\hat{L}_x,\vec{\hat{L}}^2\right] = \left[\hat{L}_y,\vec{\hat{L}}^2\right] = \left[\hat{L}_z,\vec{\hat{L}}^2\right] = 0}
$$

:::

- Note the cyclical nature of the commutators between components.


``````{admonition} 中文翻译
:class: dropdown

- 注意分量之间对易子的循环性质。
``````

### Eigenfunctions and eigenvalues of $L$ and $L_z$

- Since the operators for a component and the angular momentum square commute, it is possible to find functions that are eigenfunctions of both $\vec{\hat{L}}^2$ and $\hat{L}_z$. 


``````{admonition} 中文翻译
:class: dropdown

- 由于分量算符与角动量平方算符交换，可以找到同时是 $\vec{\hat{L}}^2$ 和 $\hat{L}_z$ 的特征函数。
``````

:::{important} Eigenfunctions and eigenvalues of angular momentum

$${{\hat{L}}^2 Y_l^m(\theta,\phi) = \hbar^2 l(l+1)\cdot Y_l^m(\theta,\phi)}$$

$${\hat{L}_zY^m_l(\theta,\phi) = \hbar m \cdot Y_l^m(\theta,\phi)}$$

- **Eigenfunctions:** $Y_l^m(\theta,\phi) $
- **Angular quantum number:** $l = 0,1,2,...$ 
- **Magnetic quantum number:** $|m| \leq l$ and takes $2l+1$ integer values $(-l, ... 0, ...l)$. 


``````{admonition} 中文翻译
:class: dropdown

- **Eigenfunctions:** $Y_l^m(\theta,\phi) $
- **角动量量子数:** $l = 0,1,2,...$
- **磁量子数：** $|m| \leq l$ 并取 $2l+1$ 个整数值 $(-l, ... 0, ...l)$。
``````
:::

- Note that here $m$ has nothing to do with magnetism but the name originates from the fact that (electron or nuclear) spins follow the same laws of angular momentum. 
- $m$ describes the projections of $L$ on the z axis. E.g., for l=2 there are five projections $(-2, -1, 0, 1, 2)$.
- Functions $Y_l^m$ are called [spherical harmonics](http://en.wikipedia.org/wiki/Spherical_harmonics). Examples of spherical harmonics with various values of $l$ and $m$ are given below (with the [Condon-Shortley phase convention](http://en.wikipedia.org/wiki/Spherical_harmonics\#Condon-Shortley_phase)).


``````{admonition} 中文翻译
:class: dropdown

- 注意此处 $m$ 与磁性无关，但该名称源于（电子或核）自旋遵循相同的角动量定律。
- $m$ 描述 $L$ 在 z 轴上的投影。例如，当 l=2 时有五个投影 $(-2, -1, 0, 1, 2)$。
- 函数 $Y_l^m$ 称为 [球谐函数](http://en.wikipedia.org/wiki/Spherical_harmonics)。下面给出了各种 $l$ 和 $m$ 值的球谐函数示例（采用 [康登-短利相位约定](http://en.wikipedia.org/wiki/Spherical_harmonics\#Condon-Shortley_phase)）。
``````


:::{figure} ./images/L_z_quant.png
:label: fig-angular-momentum-6
:alt: DeD0
:width: 450px

**Angular momentum is quantized.** Its magnitude can take specific values dictated by $l$. Projections of angular momentum are also quantized and can take specific discrete values dictated by $m$ which can take $2l+1$ values never exceeding $l$.  


``````{admonition} 中文翻译
:class: dropdown

**角动量是量子化的。** 其大小只能取由 $l$ 规定的特定值。角动量的投影也量子化，只能取由 $m$ 规定的特定离散值，$m$ 的取值为 $2l+1$ 且永不超过 $l$。
``````
:::

### Spherical harmonics 

- Spherical harmonics, denoted as $Y_{lm}(\theta, \phi)$ or $|l, m\rangle$ are important in many theoretical and practical applications, e.g., the representation of multipole electrostatic and electromagnetic fields, computation of [atomic orbital](https://en.wikipedia.org/wiki/Atomic_orbital) [electron configurations](https://en.wikipedia.org/wiki/Electron_configuration), representation of gravitational fields,  MRI imaging for streamline tractography, and the magnetic fields of planetary bodies and stars.
- Spherical harmonics emerge from the angular part of the solutions to the Laplace equation $\nabla^2 f=0$ in spherical coordinates, which is the type of equation we obtained for the rigid rotor problem and will see once more in the hydrogen atom problem.


``````{admonition} 中文翻译
:class: dropdown

- 球谐函数，记作 $Y_{lm}(\theta, \phi)$ 或 $|l, m\rangle$，在许多理论和实际应用中都很重要，例如多极静电场和电磁场的表示、[原子轨道](https://en.wikipedia.org/wiki/Atomic_orbital) [电子构型](https://en.wikipedia.org/wiki/Electron_configuration) 的计算、引力场的表示、用于流线纤维追踪的 MRI 成像，以及行星和恒星的磁场。
- 球谐函数是球坐标下拉普拉斯方程 $\nabla^2 f=0$ 角部分的解，这是刚体问题得到的方程类型，且将在氢原子问题中再次出现。
``````

| $ Y_{lm}(\theta, \phi) $ | Expression | Colatitudinal Nodes | Azimuthal Nodes |
|----------------------------|------------|----------------------|------------------|
| $ Y_{00} $               | $ \frac{1}{\sqrt{4\pi}} $ | 0 | 0 |
| $ Y_{10} $               | $ \sqrt{\frac{3}{4\pi}} \cos(\theta) $ | 1 (equatorial) | 0 |
| $ Y_{1-1} $              | $ \sqrt{\frac{3}{4\pi}} \sin(\theta) e^{-i\phi} $ | 0 | 1 |
| $ Y_{20} $               | $ \sqrt{\frac{5}{16\pi}} (3\cos^2(\theta) - 1) $ | 2 (colatitudinal rings) | 0 |
| $ Y_{2-1} $              | $ \sqrt{\frac{15}{4\pi}} \sin(\theta) \cos(\theta) e^{-i\phi} $ | 1 (equatorial) | 1 |
| $ Y_{2-2} $              | $ \sqrt{\frac{15}{4\pi}} \sin^2(\theta) e^{-2i\phi} $ | 0 | 2 |


#### Nodes of Spherical Harmonics

The nodal structure of spherical harmonics is influenced by both the degree $ l $ and the order $m$, defining the number and type of nodes as follows:


``````{admonition} 中文翻译
:class: dropdown

球谐函数的节点结构受次数 $ l $ 和级数 $m$ 双重影响，决定了节点的数量和类型，具体如下：
``````

1. **Colatitudinal Nodes (Polar Nodes)**: The variable $ \theta $ defines "polar" nodes, which appear as circular bands around the sphere. The expression in $ \cos(\theta) $ or $ \sin(\theta) $ creates colatitudinal nodes:
   - For example, $ Y_{10} $ with $ \cos(\theta) $ has a single node at $ \theta = \pi/2 $, creating an equatorial node.
   - $ Y_{20} $, with $ (3\cos^2(\theta) - 1) $, introduces two polar nodes, dividing the sphere into three regions along the colatitude.

2. **Azimuthal Nodes (Longitudinal Nodes)**: The variable $ \phi $ defines "azimuthal" nodes due to the terms $e^{im\phi}$, which create lines of longitude where the function changes phase. The number of azimuthal nodes is determined by $ |m| $:
   - If $ m = 0 $, there are no azimuthal nodes, as seen in $ Y_{00} $ and $ Y_{10} $.
   - For $ m = \pm 1 $, a single azimuthal node occurs (e.g., $ Y_{1-1} $, $ Y_{2-1} $), and for $ m = \pm 2 $, two azimuthal nodes appear (e.g., $ Y_{2-2} $).

3. **Total Nodes:** equal to the sum of the polar and longitudinal nodes, and exactly equal to $l$. For instance, $l=0$ has no nodes and $l=4$ has four nodes. 


``````{admonition} 中文翻译
:class: dropdown

- **极向节点（极向节）**：变量 $ \theta $ 定义“极向”节点，它们在球体上表现为圆形带。 $ \cos(\theta) $ 或 $ \sin(\theta) $ 表达式产生极向节点：
- 例如，$ Y_{10} $ 含 $ \cos(\theta) $，在 $ \theta = \pi/2 $ 处有一个节点，形成赤道节点。
- $ Y_{20} $，含有 $ (3\cos^2(\theta) - 1) $，引入两个极性节点，将球面沿余纬线分成三个区域。
- **经向节点（纵向节点）**：变量 $ \phi $ 因 $e^{im\phi}$ 项而定义“经向”节点，这些节点形成经线，函数在此处相位改变。经向节点的数量由 $ |m| $ 决定：
- 如果 $ m = 0 $，则没有方位节点，如 $ Y_{00} $ 和 $ Y_{10} $ 所示。
- 对于 $ m = \pm 1 $，出现单个方位节点（例如 $ Y_{1-1} $、$ Y_{2-1} $），而对于 $ m = \pm 2 $，出现两个方位节点（例如 $ Y_{2-2} $）。
- **总节点数：** 等于极性节点和纵向节点之和，且恰好等于 $l$。例如，$l=0$ 没有节点，$l=4$ 有四个节点。
``````


#### Orthogonality of Spherical Harmonics

The orthogonality of spherical harmonics is expressed as:


``````{admonition} 中文翻译
:class: dropdown

球谐函数的正交性表达为：
``````

$$
\langle l', m'| l, m \rangle = \delta_{l,l'}\delta_{m,m'}
$$

This orthogonality condition can be explicitly written as:


``````{admonition} 中文翻译
:class: dropdown

这个正交条件可以显式地写为：
``````

$$
\int_0^{\pi} \int_0^{2\pi} Y_{l'}^{m'*}(\theta, \phi) Y_l^m(\theta, \phi) \sin(\theta) \, d\theta \, d\phi = \delta_{l,l'}\delta_{m,m'}
$$

```{code-cell} python
:tags: [hide-input]
import numpy as np
from scipy.special import sph_harm_y
from scipy.integrate import dblquad

def orthogonality_test(l1, m1, l2, m2):
    """
    Computes the orthogonality integral of spherical harmonics Y(l1, m1) and Y(l2, m2).
    
    Parameters:
    l1, m1 (int): Degree and order of the first spherical harmonic.
    l2, m2 (int): Degree and order of the second spherical harmonic.
    
    Returns:
    float: The result of the orthogonality integral.
    """
    # Define the integrand for the orthogonality condition
    def integrand(theta, phi):
        Y_lm1 = sph_harm_y(l1, m1, theta, phi)
        Y_lm2 = sph_harm_y(l2, m2, theta, phi)
        return np.real(Y_lm1 * np.conj(Y_lm2)) * np.sin(theta)
    
    # Perform the integration over theta (0 to pi) and phi (0 to 2*pi)
    integral, error = dblquad(integrand, 0, 2 * np.pi, lambda _: 0, lambda _: np.pi)
    return integral

# Test orthogonality between different spherical harmonics
print("Orthogonality Tests:")
print(f"∫ Y(1,0) * Y(1,0)* = {orthogonality_test(1, 0, 1, 0):.5f} (should be close to 1)")
print(f"∫ Y(1,0) * Y(1,1)* = {orthogonality_test(1, 0, 1, 1):.5f} (should be close to 0)")
print(f"∫ Y(1,1) * Y(2,1)* = {orthogonality_test(1, 1, 2, 1):.5f} (should be close to 0)")
print(f"∫ Y(2,1) * Y(2,1)* = {orthogonality_test(2, 1, 2, 1):.5f} (should be close to 1)")
print(f"∫ Y(2,0) * Y(2,-1)* = {orthogonality_test(2, 0, 2, -1):.5f} (should be close to 0)")
```

### Plotting Spherical Harmonics

- Here we will visualize a spherical harmonic on a 3D sphere of radius 1. The radius is fixed, so there are only two variables that dictate the nodal features:

- **Colatitudinal nodes** depend on $ l $ and represent bands around the sphere, arising from terms in $ \cos(\theta) $ or $ \sin(\theta) $.
- **Azimuthal nodes** depend on $ |m| $ and create longitudinal nodes based on $ e^{im\phi} $.


``````{admonition} 中文翻译
:class: dropdown

- 这里我们将在半径为 1 的三维球面上可视化球谐函数。半径固定，因此只有两个变量决定节点特征：
- **余纬度节点**取决于 $ l $，表示球面上的带状区域，源自 $ \cos(\theta) $ 或 $ \sin(\theta) $ 项。
- **方位节点**取决于 $ |m| $ 并根据 $ e^{im\phi} $ 形成经向节点。
``````

```{code-cell} python
:tags: [hide-input]
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from scipy.special import sph_harm_y
from mpl_toolkits.mplot3d import Axes3D

def generate_spherical_harmonic_data(l, m):
    """
    Generates the data needed to plot the spherical harmonic for given l and m values.
    
    Parameters:
    l (int): Degree of the spherical harmonic.
    m (int): Order of the spherical harmonic.

    Returns:
    tuple: (x, y, z, fcolors_normalized) where:
        - x, y, z are the Cartesian coordinates of the spherical surface,
        - fcolors_normalized is the color data for plotting.
    """
    
    # Define theta and phi grids
    phi = np.linspace(0, np.pi, 100)          # colatitude
    theta = np.linspace(0, 2 * np.pi, 100)    # azimuth
    phi, theta = np.meshgrid(phi, theta)

    # Cartesian coordinates for the unit sphere
    x = np.sin(phi) * np.cos(theta)
    y = np.sin(phi) * np.sin(theta)
    z = np.cos(phi)

    # Calculate the spherical harmonic Y(l, m) and normalize it to [-1, 1] for color mapping
    fcolors = sph_harm_y(l, m, phi, theta).real
    fcolors_normalized = (fcolors - fcolors.min()) / (fcolors.max() - fcolors.min())
    
    return x, y, z, fcolors_normalized
```

#### $l=1$ harmonics

```{code-cell} python
:tags: [hide-input]
# Define the range of m and l values for the first three spherical harmonics
harmonics = [(0, 1), (1, 1), (-1, 1)]  # List of (m, l) pairs to plot

# Create a figure to hold three subplots in one row
fig = plt.figure(figsize=(18, 6))
fig.suptitle("First Three Spherical Harmonics", fontsize=16)

for i, (m, l) in enumerate(harmonics, start=1):

    x, y, z, fcolors_normalized = generate_spherical_harmonic_data(l, m)

    # Create a subplot for each (m, l) pair in one row
    ax = fig.add_subplot(1, 3, i, projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=cm.seismic(fcolors_normalized), 
                    linewidth=0, antialiased=False)

    # Customize each subplot
    ax.set_title(f"$Y_{{{l},{m}}}$", fontsize=14)
    ax.set_box_aspect([1, 1, 1])  # Ensures spherical aspect ratio
    ax.set_axis_off()             # Turn off axes for clarity

# Adjust layout for a clear view of all subplots in one row
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
```

#### $l=2$ harmonics

```{code-cell} python
:tags: [hide-input]
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
from scipy.special import sph_harm_y
from mpl_toolkits.mplot3d import Axes3D

# Define l and the range of m values for spherical harmonics with l=2
l = 2
m_values = [-2, -1, 0, 1, 2]

# Create a figure to hold five subplots in a 2x3 layout
fig = plt.figure(figsize=(15, 10))
fig.suptitle("Spherical Harmonics with l=2", fontsize=18)

for i, m in enumerate(m_values, start=1):

    # Calculate the spherical harmonic Y(l, m) and normalize it to [-1, 1] for color mapping
    x, y, z, fcolors_normalized = generate_spherical_harmonic_data(l, m) 

    # Create a subplot for each (m, l) pair in a 2x3 grid
    ax = fig.add_subplot(2, 3, i, projection='3d')
    ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=cm.seismic(fcolors_normalized),
                    linewidth=0, antialiased=False)

    # Customize each subplot
    ax.set_title(f"$Y_{{2,{m}}}$", fontsize=16)
    ax.set_box_aspect([1, 1, 1])  # Ensures spherical aspect ratio
    ax.set_axis_off()             # Turn off axes for clarity

# Adjust layout for a clear view of all subplots in a 2x3 grid
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
```

#### Total number of nodes =  $l$

```{code-cell} python
:tags: [hide-input]
import plotly.io as pio
pio.renderers.default = "plotly_mimetype"   # interactive in Jupyter-Book
import numpy as np
import plotly.graph_objects as go
from scipy.special import sph_harm_y

# Define the range of m and l values for the first three spherical harmonics
harmonics = [(1, 1), (1, 2), (2, 3)]  # List of (m, l) pairs to plot

# Initialize the figure
fig = go.Figure()


# Loop over each harmonic and create a separate subplot
for i, (m, l) in enumerate(harmonics, start=1):
    
    # Calculate the spherical harmonic Y(l, m) and normalize it to [0, 1]
    x, y, z, fcolors_normalized = generate_spherical_harmonic_data(l, m) 
    
    # Add the spherical harmonic to the figure as a surface in a new scene
    fig.add_trace(go.Surface(
        x=x, y=y, z=z,
        surfacecolor=fcolors_normalized,
        colorscale='rdbu',
        showscale=False,
        name=f"Y_{{{l},{m}}}",
        scene=f'scene{i}'  # Assign each plot to a different scene
    ))

# Update layout to arrange scenes in a row and add titles as annotations
fig.update_layout(
    title="Three Spherical Harmonics: m=1, l=1, 2, 3",
    scene=dict(domain=dict(x=[0, 0.33]), xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False), aspectmode='cube'),
    scene2=dict(domain=dict(x=[0.33, 0.66]), xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False), aspectmode='cube'),
    scene3=dict(domain=dict(x=[0.66, 1]), xaxis=dict(visible=False), yaxis=dict(visible=False), zaxis=dict(visible=False), aspectmode='cube'),
    annotations=[
        dict(text="Y_{2,0}", x=0.16, y=1.05, showarrow=False, xref="paper", yref="paper", font=dict(size=14)),
        dict(text="Y_{2,1}", x=0.5, y=1.05, showarrow=False, xref="paper", yref="paper", font=dict(size=14)),
        dict(text="Y_{2,-1}", x=0.83, y=1.05, showarrow=False, xref="paper", yref="paper", font=dict(size=14))
    ]
)

# Display the figure
fig.show()
```

### Alternative visualizations of Spherical Harmonics

- Before, we visualized spherical harmonics on the unit sphere $|r|=1$. However, there are times when we want to visualize how the magnitude of a spherical harmonic changes in space. 
- For instance, to visualize $Y_{1,-1}\sim cos(\theta)$ we could either plot its values on a unit sphere, or we could plot how $\cos(\theta)$ changes as we move around in space. 


``````{admonition} 中文翻译
:class: dropdown

- 以前，我们在单位球面 $|r|=1$ 上可视化球谐函数。然而，有时我们想要可视化空间中球谐函数幅值的变化。
- 例如，为了可视化 $Y_{1,-1}\sim cos(\theta)$，我们可以在单位球面上绘制其值，或者可以绘制随着我们在空间中移动而变化的 $\cos(\theta)$。
``````

```{code-cell} python
:tags: [hide-input]
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from scipy.special import sph_harm_y

# Set up the subplots with two side-by-side 3D plots
fig = make_subplots(rows=1, cols=2, specs=[[{'is_3d': True}, {'is_3d': True}]])

# Define theta and phi grids for spherical coordinates
theta = np.linspace(0, np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

# Convert spherical to Cartesian coordinates for the surface plots
x = np.sin(theta) * np.cos(phi)
y = np.sin(theta) * np.sin(phi)
z = np.cos(theta)

# Compute the spherical harmonic Y_{1,-1}
m, l = -1, 1
r0a = np.sqrt(3 / (4 * np.pi)) * y  # Y_{1,-1} harmonic on y-axis
r0 = np.abs(r0a)  # Absolute value for magnitude scaling

# First plot: Scaled by the spherical harmonic (bead-like structure)
fig.add_trace(
    go.Surface(
        x=r0 * x, y=r0 * y, z=r0 * z,  # Scale coordinates by |Y_{1,-1}|
        surfacecolor=r0a,  # Color by Y_{1,-1} values
        colorscale='RdBu'
    ),
    row=1, col=1
)

# Second plot: Standard unit sphere with grayscale color
fig.add_trace(
    go.Surface(
        x=x, y=y, z=z,  # Unit sphere without scaling
        surfacecolor=z,  # Color by z-coordinate for simplicity
        colorscale='RdBu'
    ),
    row=1, col=2
)

# Update layout for both plots
fig.update_layout(
    font_family="JuliaMono",
    showlegend=False,
    margin=dict(l=0, r=0, b=0, t=0),
    paper_bgcolor='rgba(0,0,0,0)',
)

# Set scene properties with adjusted axis limits for each plot
fig.update_scenes(
    dict(
        xaxis=dict(nticks=4, range=[-0.5, 0.5]),  # Limit range to reduce empty space
        yaxis=dict(nticks=4, range=[-0.5, 0.5]),
        zaxis=dict(nticks=4, range=[-0.5, 0.5]),
        aspectratio=dict(x=1, y=1, z=1)
    ),
    row=1, col=1
)
fig.update_scenes(
    dict(
        xaxis=dict(nticks=4, range=[-1.8, 1.8]),
        yaxis=dict(nticks=4, range=[-1.8, 1.8]),
        zaxis=dict(nticks=4, range=[-1.8, 1.8]),
        aspectratio=dict(x=1, y=1, z=1)
    ),
    row=1, col=2
)

# Hide color scales for a cleaner look
fig.update_traces(showscale=False)

# Show the plot
fig.show()
```

```{code-cell} python
:tags: [hide-input]
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from matplotlib import cm
import matplotlib
import matplotlib.pyplot as plt

# Define theta (angle) values
theta = np.linspace(0, 2 * np.pi, 100)

# Compute spherical harmonic values (scaled sin(theta) for two-lobe structure)
Y_1m1_values = np.sin(theta)  # Y_{1,-1} varies with sin(theta) for the two-lobe shape
r_values = np.abs(Y_1m1_values)  # Radial scaling based on |Y_{1,-1}|

# Set up the color map
cmap = matplotlib.colormaps["RdBu"]
norm = plt.Normalize(vmin=-1, vmax=1)

# Create subplots for two polar plots
fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'polar'}, {'type': 'polar'}]])

# First polar plot: Two-lobed structure with color gradient
for i in range(len(theta) - 1):
    fig.add_trace(
        go.Scatterpolar(
            r=[r_values[i], r_values[i + 1]],
            theta=[np.degrees(theta[i]), np.degrees(theta[i + 1])],
            mode="lines",
            line=dict(color=matplotlib.colors.to_hex(cmap(norm(Y_1m1_values[i]))), width=5),
            showlegend=False
        ),
        row=1, col=1
    )

# Second polar plot: Unit circle with consistent color gradient
for i in range(len(theta) - 1):
    fig.add_trace(
        go.Scatterpolar(
            r=[1, 1],  # Fixed radius for unit circle
            theta=[np.degrees(theta[i]), np.degrees(theta[i + 1])],
            mode="lines",
            line=dict(color=matplotlib.colors.to_hex(cmap(norm(Y_1m1_values[i]))), width=5),
            showlegend=False
        ),
        row=1, col=2
    )

# Update layout for both polar plots with fixed radius range and equal appearance
fig.update_layout(
    font_family="JuliaMono",
    showlegend=False,
    margin=dict(l=0, r=0, b=0, t=0),
    polar=dict(radialaxis=dict(range=[0, 1.2])),  # First plot axis range
    polar2=dict(radialaxis=dict(range=[0, 1.2]))  # Second plot axis range
)

# Show the plot
fig.show()
```

```{marimo-config}
---
pyproject: |
  requires-python = ">=3.10"
  dependencies = [
      "numpy",
      "scipy",
      "matplotlib",
      "plotly",
  ]
---
```

```{marimo} python
:hide-code: true

import marimo as mo
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.dpi"] = 150
import plotly.graph_objects as go
from scipy.special import sph_harm_y
```

```{marimo} python
:hide-code: true

l_s = mo.ui.slider(0, 8, step=1, value=3, show_value=True, label="l")
l_s
```

```{marimo} python
:hide-code: true

m_s = mo.ui.dropdown(
    options={str(v): v for v in range(-l_s.value, l_s.value + 1)}, value="0", label="m"
)
m_s
```

```{marimo} python
:hide-code: true

m_eff5 = m_s.value
ph_m = np.linspace(0, np.pi, 90)
th_m = np.linspace(0, 2 * np.pi, 90)
ph_m, th_m = np.meshgrid(ph_m, th_m)
Y_m = sph_harm_y(l_s.value, m_eff5, ph_m, th_m).real

xs5 = np.sin(ph_m) * np.cos(th_m)
ys5 = np.sin(ph_m) * np.sin(th_m)
zs5 = np.cos(ph_m)
fc5 = (Y_m - Y_m.min()) / (Y_m.max() - Y_m.min() + 1e-12)

fig5 = plt.figure(figsize=(6, 6))
ax5 = fig5.add_subplot(111, projection="3d")
ax5.plot_surface(xs5, ys5, zs5, facecolors=plt.cm.seismic(fc5), rstride=1, cstride=1)
ax5.set_axis_off()
ax5.set_title(f"Y(l={l_s.value}, m={m_eff5}) on the unit sphere", fontsize=11)
fig5
```

```{marimo} python
:hide-code: true

r5 = np.abs(Y_m)
fig5b = go.Figure(data=[go.Surface(
    x=r5 * np.sin(ph_m) * np.cos(th_m),
    y=r5 * np.sin(ph_m) * np.sin(th_m),
    z=r5 * np.cos(ph_m),
    surfacecolor=Y_m, colorscale="RdBu", showscale=False,
)])
fig5b.update_layout(
    width=650, height=480, scene=dict(aspectmode="data"),
    title_text=f"r = |Y(l={l_s.value}, m={m_eff5})|",
)
fig5b
```

### Learn More about Spherical Harmonics


<html>
<iframe width="560" height="315" src="https://www.youtube.com/embed/5PMqf3Hj-Aw?si=FnrUFzZT8d1R18w-"  frameborder="0" allowfullscreen>
</iframe>
</html>
