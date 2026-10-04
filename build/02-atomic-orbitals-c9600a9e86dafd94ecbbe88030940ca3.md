---
kernelspec:
  name: python3
  display_name: Python 3
---

# Atomic Orbitals

:::{note} **What you will learn**

- **A wavefunction for a one-electron system is called an orbital.** For an atomic system such as the hydrogen atom, it is called an [atomic orbital](http://en.wikipedia.org/wiki/Atomic_orbital).
- The orbital plots demonstrate the shapes of the orbitals, but this does not tell us anything about the radial extent (i.e., how far the orbital reaches).
- As the value of $Z$ is increased, the radial extent decreases. This indicates that for higher nuclear charge the electrons reside closer to the nucleus.
- **The radial wavefunctions have $n - l - 1$ nodes** between distances of zero and infinity.
- **The angular part of the wavefunctions has $l$ nodes.**
- **The total number of nodes is $n - 1$.**


``````{admonition} 中文翻译
:class: dropdown

- **一个电子系统的波函数称为轨道。** 对于原子系统，如氢原子，它称为[原子轨道](http://en.wikipedia.org/wiki/Atomic_orbital)。
- 轨道图展示了轨道的形状，但这并不能告诉我们关于径向范围（即轨道延伸多远）的任何信息。
- 随着 $Z$ 值的增加，径向范围减小。这表明核电荷越高，电子离原子核越近。
- **径向波函数在零到无穷远距离之间有 $n - l - 1$ 个节点**
- **波函数的角向部分有 $l$ 个节点。**
- **总节点数为 $n - 1$。**
``````
:::

:::{important} **Definition of an atomic orbital**

- **Atomic orbital (AO):** a single-electron wavefunction (exact for H-like atoms)


``````{admonition} 中文翻译
:class: dropdown

- **原子轨道 (AO)：** 单电子波函数（对类氢原子为精确解）
``````

$$
\psi_{n\ell m_\ell}(r,\theta,\phi) = R_{n\ell}(r)\,Y_{\ell m_\ell}(\theta,\phi)
$$

- **Principal quantum number:** $n = 1, 2, 3, \ldots$
- **Orbital angular momentum:** $\ell = 0, 1, 2, \ldots, n-1$
- **Magnetic quantum number:** $m_\ell = -\ell, -\ell + 1, \ldots, \ell$


``````{admonition} 中文翻译
:class: dropdown

- **主量子数：** $n = 1, 2, 3, \ldots$
- **轨道角动量：** $\ell = 0, 1, 2, \ldots, n-1$
- **磁量子数：** $m_\ell = -\ell, -\ell + 1, \ldots, \ell$
``````

**Probability distribution (full 3D):**

$$
|\psi|^2 dV = \big|R_{n\ell}(r)\big|^2 \cdot \big|Y_{\ell m_\ell}(\theta,\phi)\big|^2 \cdot r^2\sin\theta \, dr \, d\theta \, d\phi
$$

**Radial probability distribution:**

$$
P_r(r) = r^2\big|R_{n\ell}(r)\big|^2
\quad\text{with}\quad \int_{0}^{\infty} P_r(r) \, dr = 1
$$

**Angular probability density:**

$$
P_\Omega(\theta,\phi) = \big|Y_{\ell m_\ell}(\theta,\phi)\big|^2
\quad\text{with}\quad \int_{0}^{2\pi}\int_{0}^{\pi} P_\Omega \sin \theta \, d\theta \, d\phi = 1
$$

*Notes:*

- $s$ orbitals ($\ell = 0$) are isotropic: $P_\Omega = \tfrac{1}{4\pi}$.
- $p, d, \ldots$ orbitals show angular nodes where $Y_{\ell m_\ell} = 0$, setting the orbital shapes.


``````{admonition} 中文翻译
:class: dropdown

- $s$ 轨道 ($\ell = 0$) 是各向同性的：$P_\Omega = \tfrac{1}{4\pi}$。
- $p, d, \ldots$ 轨道显示出 $Y_{\ell m_\ell} = 0$ 处的角节点，这决定了轨道的形状。
``````
:::

### Radial profiles of atomic orbitals

- When visualizing the radial probabilities, it is possible to either directly plot the square of the radial wavefunction ($R_{nl}^2$) or the radial probability density ($P_{nl}$):


``````{admonition} 中文翻译
:class: dropdown

- 可视化径向概率时，可以直接绘制径向波函数的平方 ($R_{nl}^2$) 或径向概率密度 ($P_{nl}$)：
``````

$${P_{nl}(r) = r^2 N_{nl}^2 R_{nl}^2(r)}$$

:::{figure} images/AO_0.png
:alt: Radial probability densities of hydrogen orbitals
:width: 80%

Fig.1 Radial probability density $P_{nl}(r) = r^2 |R_{nl}(r)|^2$ for several hydrogen orbitals. The peaks mark the most probable distance of the electron from the nucleus.


``````{admonition} 中文翻译
:class: dropdown

图1 径向概率密度 $P_{nl}(r) = r^2 |R_{nl}(r)|^2$ 的若干氢原子轨道。峰标记电子距离核最可能的距离。
``````
:::

- According to this expression, the most probable radius for an electron in the hydrogen-atom $1s$ orbital is $a_0$ (the Bohr radius). The figure above shows examples of $P_{nl}$. Probability densities are useful, for example, in understanding charge distributions in atoms and molecules.


``````{admonition} 中文翻译
:class: dropdown

- 根据该表达式，氢原子 $1s$ 态电子最可能半径为 $a_0$（玻尔半径）。上图展示了 $P_{nl}$ 的示例。概率密度在理解原子和分子电荷分布方面很有用。
``````

:::{figure} images/AO2.jpg
:alt: Radial wavefunctions and probability densities
:width: 80%

Fig.2 Radial wavefunctions $R_{nl}(r)$ and the associated radial probability densities for the lowest hydrogen orbitals.


``````{admonition} 中文翻译
:class: dropdown

图2 径向波函数 $R_{nl}(r)$ 及其对应的径向概率密度，针对最低氢原子轨道。
``````
:::

- As the principal quantum number $n$ increases, the electron moves out to greater distances from the nucleus. The average distance for an electron in a given orbital (with quantum numbers $n$ and $l$) is given by (this is not the same as the most probable value):


``````{admonition} 中文翻译
:class: dropdown

- 随着主量子数 $n$ 的增加，电子移向离核更远的距离。给定轨道（量子数 $n$ 和 $l$）中电子的平均距离（这与最可能值不同）：
``````

$${\langle r\rangle_{nl} = \int_0^\infty r \cdot P_{nl}(r) \, dr = \frac{n^2 a_0}{Z}\left\{ 1 + \frac{1}{2}\left[ 1 - \frac{l(l+1)}{n^2}\right]\right\}}$$

- Note that the expectation value of $r$ and the most probable value of $r$ are not equal. The expectation value can be thought of like *an average*, and the most probable value like a *maximum* value.


``````{admonition} 中文翻译
:class: dropdown

- 注意 $r$ 的期望值和 $r$ 的最可能值不相等。期望值可以被视作*平均值*，而最可能值则像*最大值*。
``````

### 3D shapes of orbitals

- For degenerate states with $l > 0$, we have an additional degree of freedom in choosing how to represent the orbitals. In fact, any linear combination of a given set of $2l + 1$ orthogonal eigenfunctions corresponding to a degenerate set with orbital angular momentum $l$ is also a solution to the Schrödinger equation.


``````{admonition} 中文翻译
:class: dropdown

- 对于 $l > 0$ 的退化态，我们在选择如何表示轨道方面有额外的自由度。事实上，任何一组 $2l + 1$ 个对应于轨道角动量 $l$ 的退化集的正交本征函数的线性组合，也是薛定谔方程的解。
``````

:::{figure} images/AO.png
:alt: Shapes of atomic orbitals
:width: 80%

Fig.3 Shapes of the $s$, $p$, and $d$ atomic orbitals shown as isosurfaces of the probability density.


``````{admonition} 中文翻译
:class: dropdown

图3 以概率密度等值面形式展示的 $s$、$p$ 和 $d$ 原子轨道的形状。
``````
:::

- Two commonly used representations are the Cartesian form, which is real-valued (and, in the case of $l = 1$, denoted $p_x$, $p_y$, and $p_z$), and the eigenfunctions of angular momentum ($\hat{L}^2$ and $\hat{L}_z$), which are complex-valued and denoted $p_{-1}$, $p_0$, and $p_{+1}$. Both polar and Cartesian forms represent the same physical electron density, just in different coordinate frames. The relation between the representations is:


``````{admonition} 中文翻译
:class: dropdown

- 两种常用的表示形式是笛卡尔形式，其为实值（$l = 1$ 时分别表示为 $p_x$、$p_y$、$p_z$），以及角动量算符($\hat{L}^2$ 和 $\hat{L}_z$ )的本征函数，其为复值并表示为 $p_{-1}$、$p_0$、$p_{+1}$。极坐标和笛卡尔形式均代表相同的物理电子密度，只是在不同的坐标系下。两种表示形式之间的关系是：
``````

$${p_x = -\frac{1}{\sqrt{2}}\left( p_{+1} - p_{-1}\right) \propto \sin(\theta)\cos(\phi) \propto x}$$
$${p_y = \frac{i}{\sqrt{2}}\left( p_{+1} + p_{-1}\right) \propto \sin(\theta)\sin(\phi) \propto y}$$
$${p_z = p_0}$$

:::{figure} images/Orbital_p1-px_animation.gif
:alt: Combining complex p orbitals into real p orbitals
:width: 50%

Fig.4 Animation showing how the complex orbitals $p_{+1}$ and $p_{-1}$ combine into the familiar real $p_x$ orbital.


``````{admonition} 中文翻译
:class: dropdown

图 4 动画展示复轨道 $p_{+1}$ 和 $p_{-1}$ 如何组合成熟悉的实轨道 $p_x$。
``````
:::

- By combining $p_x$, $p_y$, and $p_z$, the lobe of the orbital can be made to point in any direction. For $d$-orbitals, we have five degenerate levels:


``````{admonition} 中文翻译
:class: dropdown

- 通过组合 $p_x$、$p_y$ 和 $p_z$，轨道的叶瓣可以指向任意方向。对于 $d$ 轨道，我们有五个简并能级：
``````

:::{figure} images/p-orbitals.png
:alt: Real p orbitals pointing along the axes
:width: 70%

Fig.5 The three real $p$ orbitals ($p_x$, $p_y$, $p_z$) point along the Cartesian axes; their linear combinations can point in any direction.


``````{admonition} 中文翻译
:class: dropdown

图5 三个实 $p$ 轨道（$p_x$、$p_y$、$p_z$）沿笛卡尔轴指向；它们的线性组合可指向任意方向。
``````
:::

$${d_{x^2 - y^2} = \frac{1}{\sqrt{2}}\left(d_{+2} + d_{-2}\right), \quad d_{xy} = -\frac{i}{\sqrt{2}}\left( d_{+2} - d_{-2}\right)}$$
$${d_{xz} = -\frac{1}{\sqrt{2}}\left( d_{+1} - d_{-1}\right), \quad d_{yz} = \frac{i}{\sqrt{2}}\left( d_{+1} + d_{-1}\right)}$$
$${d_{z^2} = d_0}$$

### Table of 2D orbitals

:::{figure} images/hydrogen_probability_densities.png
:alt: 2D probability densities of hydrogen orbitals
:width: 90%

Fig.6 Two-dimensional cross sections of the probability densities $|\psi_{nlm}|^2$ for hydrogen orbitals.


``````{admonition} 中文翻译
:class: dropdown

图 6 氢原子轨道概率密度 $|\psi_{nlm}|^2$ 的二维截面。
``````
:::

### Table of 3D orbitals

:::{figure} images/AO3.png
:alt: 3D shapes of hydrogen orbitals
:width: 90%

Fig.7 Three-dimensional isosurface renderings of hydrogen atomic orbitals.


``````{admonition} 中文翻译
:class: dropdown

图 7 氢原子轨道的三维等值面渲染图。
``````
:::

### Interactive plotter of atomic orbitals

<iframe src="https://al2me6.github.io/evanescence/"
        width="800"
        height="500"
        allowfullscreen>
</iframe>

Or build any orbital yourself; the menus only offer valid quantum numbers, and blue and red are the positive and negative lobes:


``````{admonition} 中文翻译
:class: dropdown

或者自己构建任意轨道；菜单仅提供有效的量子数，蓝色和红色分别代表正负叶瓣：
``````

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
import plotly.graph_objects as go
from scipy.special import sph_harm_y, genlaguerre, factorial
```

```{marimo} python
:hide-code: true

def radial_m(r, n=1, l=0):
    pre = np.sqrt(((2 / n) ** 3 * factorial(n - l - 1)) / (2 * n * factorial(n + l)))
    p = 2 * r / n
    return pre * np.exp(-p / 2) * p**l * genlaguerre(n - l - 1, 2 * l + 1)(p)
```

```{marimo} python
:hide-code: true

n_o = mo.ui.slider(1, 5, step=1, value=3, show_value=True, label="n")
n_o
```

```{marimo} python
:hide-code: true

l_o = mo.ui.dropdown(
    options={str(v): v for v in range(n_o.value)}, value=str(n_o.value - 1), label="l"
)
l_o
```

```{marimo} python
:hide-code: true

m_o = mo.ui.dropdown(
    options={str(v): v for v in range(-l_o.value, l_o.value + 1)}, value="0", label="m"
)
m_o
```

```{marimo} python
:hide-code: true

l_o_eff = l_o.value
m_o_eff = m_o.value

ext = 6.0 * n_o.value
g_o = np.linspace(-ext, ext, 45)
x_o, y_o, z_o = np.meshgrid(g_o, g_o, g_o, indexing="ij")
r_o = np.sqrt(x_o**2 + y_o**2 + z_o**2)
phi_o = np.arctan2(y_o + 1e-10, x_o)
theta_o = np.where(np.isclose(r_o, 0.0), 0.0, np.arccos(z_o / (r_o + 1e-12)))

psi_o = (radial_m(r_o, n_o.value, l_o_eff) * sph_harm_y(l_o_eff, m_o_eff, theta_o, phi_o)).real
amp_o = 0.5 * np.abs(psi_o).max()

fig_o = go.Figure(data=go.Isosurface(
    x=x_o.flatten(), y=y_o.flatten(), z=z_o.flatten(), value=psi_o.flatten(),
    colorscale="RdBu", isomin=-amp_o, isomax=amp_o, surface_count=2,
    showscale=False, caps=dict(x_show=False, y_show=False, z_show=False),
))
fig_o.update_layout(
    scene=dict(aspectmode="data"),
    width=680, height=480,
    title_text=f"orbital ({n_o.value}, {l_o_eff}, {m_o_eff})",
)
fig_o
```

