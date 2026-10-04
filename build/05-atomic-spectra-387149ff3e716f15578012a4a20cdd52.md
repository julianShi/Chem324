---
kernelspec:
  name: python3
  display_name: Python 3
---
# Atomic spectra

:::{note} **What you will learn**

- Excited atoms emit light only at **discrete wavelengths**. Each element has its own line spectrum, an atomic fingerprint that classical physics cannot explain.
- The hydrogen lines are captured by the empirical **Rydberg formula**, $\tilde{\nu} = R_H(1/n_1^2 - 1/n_2^2)$, whose integers $n_1, n_2$ hinted that something in the atom is quantized.
- **Bohr's model** (1913) adds one quantum rule to classical orbits, angular momentum in units of $\hbar$, and from it derives the orbit radii $r_n = n^2 a_0$, the energy levels $E_n = -13.6\,\text{eV}/n^2$, and the Rydberg constant from fundamental constants.
- Spectral lines are **transitions between energy levels**: a photon carries away exactly the energy difference, $h\nu = E_{n_2} - E_{n_1}$. The same formulas work for any one-electron ion once the nuclear charge $Z$ is included.
- Bohr's model nonetheless **fails** past hydrogen: no helium, no line intensities, no fine structure, and an orbit that the uncertainty principle forbids. Keep the quantization, discard the orbit.


``````{admonition} 中文翻译
:class: dropdown

- 激发原子仅在**离散波长**处发光。每种元素都有其特有的线谱，这是经典物理学无法解释的原子指纹。
- 氢谱由经验 **莱德伯格公式** 捕获，$\tilde{\nu} = R_H(1/n_1^2 - 1/n_2^2)$，其整数 $n_1, n_2$ 提示原子内部有量子化现象。
- **Bohr的模型** (1913) 在经典轨道上增加了一个量子规则，将角动量量化为 $\hbar$ 的整数倍，并由此推导出轨道半径 $r_n = n^2 a_0$、能级 $E_n = -13.6\,\text{eV}/n^2$ 以及里德伯常数。
- 光谱线是**能级之间的跃迁**：光子携带恰好能量差，$h\nu = E_{n_2} - E_{n_1}$。对于任何单电子离子，只要包含核电荷 $Z$，同样的公式都适用。
- 玻尔模型尽管 **失效** 超过氢原子：没有氦，没有线强度，没有细结构，且轨道被不确定性原理禁止。保持量子化，抛弃轨道。
``````
:::


### Spectroscopy of Atoms


- **Spectroscopy** is the study of the interaction between matter and electromagnetic radiation.  
- By analyzing the emitted or absorbed light, spectroscopy reveals information about the **structure and composition** of atoms and molecules.  
- When heated or subjected to electrical discharge, atoms emit radiation at characteristic frequencies. The resulting spectrum is **unique for each element**, serving as a kind of atomic fingerprint.  


``````{admonition} 中文翻译
:class: dropdown

- **光谱学** 是研究物质与电磁辐射相互作用的学科。
- 通过分析发射或吸收的光，光谱学揭示了原子和分子的 **结构和组成** 信息。
- 当受热或受电放电时，原子在特征频率发射辐射。产生的光谱是 **每种元素独有的**，作为一种原子指纹。
``````


:::{figure} images/lec1_AtomicSpectrum.png
:label: fig-atomic-spectra-1
:alt: Hydrogen atomic spectrum
:width: 70%

**Atomic spectroscopy of the hydrogen atom.**  
Hydrogen in a gas-discharge tube emits light at discrete wavelengths, which appear as distinct spectral lines when passed through a prism.


``````{admonition} 中文翻译
:class: dropdown

**氢原子的原子光谱。**
氢气放电管中的氢原子在特定波长发射光，当这些光通过棱镜时，会显现为离散的光谱线。
``````
:::

Every element produces its own set of lines. Below is what a spectrograph records from a
discharge lamp of each gas: no two patterns are alike, which is why a spectrum taken through
a telescope tells you what a star is made of.


``````{admonition} 中文翻译
:class: dropdown

每个元素都有自己的线集。下面是光谱仪记录的每种气体放电灯的记录：没有两种模式是相同的，这也是为什么通过望远镜获得的光谱能告诉你恒星由什么组成的原因。
``````

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt

def wl_to_rgb(wl):
    """Approximate sRGB colour of a single wavelength in nm."""
    if wl < 440:    r, g, b = -(wl - 440) / 60, 0.0, 1.0
    elif wl < 490:  r, g, b = 0.0, (wl - 440) / 50, 1.0
    elif wl < 510:  r, g, b = 0.0, 1.0, -(wl - 510) / 20
    elif wl < 580:  r, g, b = (wl - 510) / 70, 1.0, 0.0
    elif wl < 645:  r, g, b = 1.0, -(wl - 645) / 65, 0.0
    else:           r, g, b = 1.0, 0.0, 0.0
    return (min(r, 1.0), min(g, 1.0), min(b, 1.0))

# (wavelength in nm, relative brightness) for the strong visible lines
spectra = {
    "H":  [(656.3, 1.0), (486.1, 0.6), (434.0, 0.4), (410.2, 0.3)],
    "He": [(447.1, 0.5), (471.3, 0.3), (492.2, 0.3), (501.6, 0.6),
           (587.6, 1.0), (667.8, 0.5), (706.5, 0.4)],
    "Na": [(498.3, 0.2), (568.8, 0.3), (589.0, 1.0), (589.6, 1.0), (615.4, 0.3)],
    "Hg": [(404.7, 0.6), (435.8, 1.0), (546.1, 1.0), (577.0, 0.6), (579.1, 0.6)],
    "Ne": [(585.2, 0.8), (588.2, 0.6), (594.5, 0.7), (607.4, 0.5), (614.3, 0.7),
           (621.7, 0.5), (626.6, 0.6), (633.4, 0.8), (640.2, 1.0), (650.7, 0.6),
           (659.9, 0.5), (692.9, 0.4), (703.2, 0.5)],
}

fig, axes = plt.subplots(len(spectra), 1, figsize=(9, 4.0), sharex=True)
for ax, (name, lines) in zip(axes, spectra.items()):
    ax.set_facecolor("black")
    for wl, intensity in lines:
        ax.axvline(wl, color=wl_to_rgb(wl), lw=1.8, alpha=0.35 + 0.65 * intensity)
    ax.set_yticks([])
    ax.set_ylabel(name, rotation=0, ha="right", va="center", fontsize=12, labelpad=14)
    for spine in ax.spines.values():
        spine.set_visible(False)
axes[-1].set_xlim(380, 750)
axes[-1].set_xlabel("wavelength (nm)")
fig.suptitle("Fig. Visible emission lines of five elements. Each element has its own fingerprint.",
             fontsize=10)
fig.tight_layout()
```

:::{figure} images/spectra.png
:label: fig-atomic-spectra-2
:alt: Solar spectra
:width: 70%

**Spectroscopy of the Sun.**  
By analyzing spectral lines, one can identify the presence of different elements in the solar atmosphere.  


``````{admonition} 中文翻译
:class: dropdown

**太阳光谱学。**  
通过分析谱线，可以识别太阳大气中不同元素的存在。
``````
:::


### Spectral lines and Rydberg's formula

- The existence of discrete spectral lines is impossible to describe with classical mechanics.  In 1885, Johann Balmer demonstrated that a subset of the hydrogen atom spectrum (the Balmer series) could be described by the equation


``````{admonition} 中文翻译
:class: dropdown

- 离散光谱线的存在在经典力学中无法描述。1885年，Johann Balmer展示了氢原子光谱的一部分（巴尔末系列）可以用下面的公式描述：
``````

$$\lambda = B\,\frac{n^2}{n^2-4}, \qquad B = 364.6\ \text{nm}$$

where $n=3,4,5,...$. Written in terms of the wavenumber $\tilde{\nu} = 1/\lambda$ this is $\tilde{\nu} = \frac{4}{B}\left(\frac{1}{2^2}-\frac{1}{n^2}\right)$ with $4/B = 1.097\times10^{7}\ \text{m}^{-1}$.  Later, Johannes Rydberg generalized this formula to account for the entire hydrogen atom spectrum yielding the Rydberg formula


``````{admonition} 中文翻译
:class: dropdown

其中 $n=3,4,5,...$。以波数 $\tilde{\nu} = 1/\lambda$ 表示为 $\tilde{\nu} = \frac{4}{B}\left(\frac{1}{2^2}-\frac{1}{n^2}\right)$，其中 $4/B = 1.097\times10^{7}\ \text{m}^{-1}$。后来，Johannes Rydberg 将此公式推广以涵盖整个氢原子光谱，得到瑞德伯公式
``````

:::{important} **Rydberg formula**


$$\tilde{\nu} = R_H\left(\frac{1}{n_1^2}-\frac{1}{n_2^2}\right)$$

where 
- $R_H = 1.097 \times 10^7 \ \text{m}^{-1}$ is the Rydberg constant.
- $n_1 = 1,2,3,...$, and $n_2 = n_1+1,n_1+2,...$.  


``````{admonition} 中文翻译
:class: dropdown

- $R_H = 1.097 \times 10^7 \ \text{m}^{-1}$ 是里德伯常数。
- $n_1 = 1,2,3,...$，且 $n_2 = n_1+1,n_1+2,...$。
``````

:::

- While these equations fit the hydrogen atom spectrum nicely, they do not prescribe any physics to the system.  They do not present a model of the hydrogen atom but rather a heuristic equation that fits the data.  Nonetheless, scientists were perplexed by the presence of the integers $n_1$ and $n_2$. 


``````{admonition} 中文翻译
:class: dropdown

- 虽然这些方程很好地拟合氢原子光谱，但它们并未规定系统的任何物理。它们并未提出氢原子的模型，而只是一个拟合数据的经验方程。尽管如此，科学家们仍被整数 $n_1$ 和 $n_2$ 的存在所困惑。
``````


:::{figure} images/bohr_series_orbits.png
:label: fig-atomic-spectra-3
:alt: atomic series
:width: 30%

Atomic spectral lines are named after their discoverers. Each series contains all transitions to a distinct lower level $n=1,2,3$.


``````{admonition} 中文翻译
:class: dropdown

原子谱线以其发现者命名。每个系包含所有跃迁到不同的低能级 $n=1,2,3$。
``````
:::


### Bohr's Model of the Hydrogen Atom

:::{figure} images/evolution_atom.png
:label: fig-atomic-spectra-4
:alt: Evolution of atomic models
:width: 70%

**Evolution of atomic models.**  
From pre-quantum pictures of atoms to the modern quantum mechanical description.  


``````{admonition} 中文翻译
:class: dropdown

**原子模型的演变。**  
从量子力学前的原子图像到现代量子力学描述。
``````
:::

- In 1913, Niels Bohr proposed a model of the hydrogen atom that successfully explained its **discrete emission spectrum**.  
- The atom was pictured as an electron moving in **circular orbits** around a central proton. Because the proton is far more massive than the electron, it was treated as fixed in space.  
- To prevent the electron from spiraling into the nucleus, Bohr introduced a new **quantization rule**: the electron’s orbital motion must accommodate an integer number of standing wave modes, $n = 1, 2, 3, \ldots$  
- This postulate leads directly to an expression for the allowed **energy levels of hydrogen**, each labeled by a principal quantum number $n$.  


``````{admonition} 中文翻译
:class: dropdown

- 1913 年，尼尔斯·玻尔提出氢原子模型，成功解释了其 **离散发射光谱**。
- 原子被想象为电子在质子周围做 **circular orbits**（圆轨道）运动。由于质子远比电子重，因此将其视为固定在空间中。
- 为了防止电子螺旋落入核心，玻尔引入了一个新的**量子化规则**：电子的轨道运动必须容纳整数个驻波模，$n = 1, 2, 3, \ldots$
- 这一假设直接导出了氢原子允许的**能级**表达式，每个能级由主量子数 $n$ 标记。
``````

:::{figure} images/bohring.png
:label: fig-atomic-spectra-5
:alt: Niels Bohr horseshoe anecdote
:width: 20%

**Anecdote about Niels Bohr.**  
A visitor once noticed a horseshoe (a Scandinavian good-luck charm) hanging above Bohr’s door:  


``````{admonition} 中文翻译
:class: dropdown

**关于尼尔斯·玻尔的轶事。**  
一位访客曾注意到玻尔门上方挂着一只马蹄铁（斯堪的纳维亚的吉祥物）：
``````

*"But Niels, you are a scientist! Surely you don’t believe in this superstition?"*  


``````{admonition} 中文翻译
:class: dropdown

*"但尼尔斯，你是个科学家！你肯定不信这迷信吧？"*
``````

*"Of course I don’t,"* Bohr replied. *"But I am told it works even if you don’t believe in it!"*  


``````{admonition} 中文翻译
:class: dropdown

*"我当然不信，"* 玻尔回答道。*"但我听说即使你不信它也管用！"*
``````
:::


### Quantizing the States of the Electron in the Hydrogen Atom

:::{figure} images/bohr_standing_waves.png
:label: fig-atomic-spectra-6
:alt: Quantized orbits of the electron
:width: 60%

Bohr rationalized discrete orbits by requiring that an integer number of electron wavelengths fit around the circumference of each orbit: four waves close on themselves (a), four and a half do not (b).


``````{admonition} 中文翻译
:class: dropdown

波尔通过要求每个轨道周长上整数个电子波长相合，使离散轨道合理化：四个波长闭合（a），四个半波长不闭合（b）。
``````
:::

- Imposing this condition gives the relation  

$$
2\pi r = n \lambda_e, \quad n = 1, 2, 3, \ldots
$$

- Here, $\lambda_e$ is the **de Broglie wavelength** of the electron:  


``````{admonition} 中文翻译
:class: dropdown

- 这里，$\lambda_e$ 是电子的 **德布罗意波长**：
``````

$$
\lambda_e = \frac{h}{m_e v}.
$$

- Substituting this expression for $\lambda_e$ into the quantization condition yields  


``````{admonition} 中文翻译
:class: dropdown

- 将此 $\lambda_e$ 表达式代入量子化条件可得
``````

$$
m_e v r = \frac{n h}{2\pi} = n \hbar.
$$

- We introduce the shorthand $\hbar = \tfrac{h}{2\pi}$ because it appears frequently in quantum mechanics. The left-hand side, $m_e v r$, represents the **angular momentum** of the electron.  
- Thus, Bohr’s model predicts that the electron’s angular momentum is **quantized** in integer multiples of $\hbar$.  


``````{admonition} 中文翻译
:class: dropdown

- 我们引入简记 $\hbar = \tfrac{h}{2\pi}$，因为它在量子力学中频繁出现。左边，$m_e v r$，代表电子的**角动量**
- 因此，玻尔模型预测电子的角动量以 $\hbar$ 的整数倍**量子化**。
``````

:::{note} **A word on history**

Bohr's 1913 paper contains no de Broglie waves, because matter waves were still eleven
years away. Bohr simply postulated that angular momentum comes in whole units of $\hbar$
and defended the postulate by showing it reproduces classical physics for very large
orbits. The standing-wave picture above is de Broglie's 1924 reading of the same rule, and
it is the one worth remembering: confinement plus waves gives quantization, here and
everywhere else in this course.


``````{admonition} 中文翻译
:class: dropdown

Bohr 1913年的论文中不包含德布罗意波，因为物质波当时相差十一年。Bohr 仅仅假设角动量以 $\hbar$ 的整数倍出现，并通过展示这对于非常大的轨道能还原经典物理而辩护该假设。上述的 standing-wave 图像是德布罗意 1924 年对同一规则的阅读，而且这是值得记住的：约束加波给出了量子化，这里以及这门课程中到处都是。
``````
:::


### Force Balance

After introducing his quantization rule, Bohr turned back to **classical mechanics** to determine the allowed electron energies. He assumed that, in a stationary orbit, the **electrostatic attraction** between the proton and electron is exactly balanced by the **centrifugal force** of the orbiting electron.  


``````{admonition} 中文翻译
:class: dropdown

引入量子规则后，波尔回到**经典力学**以确定电子的允许能量。他假设在稳定轨道中，质子与电子之间的**静电吸引力**恰好与轨道电子的**离心力**相平衡。
``````

**Electrostatic force**  

$$
f_{\text{el}} = \frac{e^2}{4\pi\varepsilon_0 r^2},
$$  

where $e$ is the elementary charge and the factor $4\pi \varepsilon_0$ ensures SI units.  


``````{admonition} 中文翻译
:class: dropdown

其中 $e$ 为基本电荷，因子 $4\pi \varepsilon_0$ 保证国际单位制（SI）单位。
``````

**Centrifugal force**  

$$
f_{\text{cf}} = \frac{m_e v^2}{r},
$$  

where $m_e$ is the electron mass and $v$ its orbital velocity.  


``````{admonition} 中文翻译
:class: dropdown

其中 $m_e$ 是电子质量，$v$ 是其轨道速度。
``````

Equating these two forces gives  

$$
\frac{e^2}{4\pi\varepsilon_0 r^2} = \frac{m_e v^2}{r}.
$$  

:::{warning} **Careful: the centrifugal force is fictitious**

In the laboratory frame there is only one force on the electron, the Coulomb pull, and it
is unbalanced: it supplies the **centripetal acceleration** $a = v^2/r$ that keeps bending
the velocity into a circle. The **centrifugal force** appears only when you ride along with
the electron, in the rotating frame, where it exactly cancels the Coulomb pull and the
electron sits still. Both bookkeepings give the same equation above, which is why Bohr
could write it either way.


``````{admonition} 中文翻译
:class: dropdown

在实验室参考系中，电子只受一个力，库仑引力，且该力是不平衡的：它提供 **离心加速度** $a = v^2/r$ 使得速度保持弯曲成圆周。只有当你随电子一起运动，处于旋转参考系时，**离心力** 才会出现，它恰好抵消库仑引力，电子保持静止。这两种记账方式给出相同的上述方程，因此 Bohr 可以用任一方式书写它。
``````
:::

::::{admonition} **Watch it move: position, velocity and acceleration on a circular orbit**
:class: dropdown tip

The three vectors keep constant length and only turn. The velocity is always tangent, the
acceleration always points at the nucleus, and the centrifugal arrow is its mirror image in
the rotating frame. The right panel is worth remembering for later: each component of
circular motion is simple harmonic motion, with $v_x$ a quarter cycle ahead of $x$ and
$a_x$ exactly opposite to it. The same machinery returns for angular momentum in Chapter 4
and the rigid rotor in Chapter 5.


``````{admonition} 中文翻译
:class: dropdown

这三个向量保持恒定长度并仅仅转动。速度始终切向，加速度始终指向核心，离心箭镜像则在旋转参考系中是其镜像。右侧面板值得记住以备后用：圆周运动的每个分量都是简谐运动，$v_x$ 比 $x$ 提前四分之一周期，且 $a_x$ 完全相反。同样的机制在第四章的角动量和第五章的刚性转子中也会返回。
``````

```{code-cell} python
:tags: [hide-input]
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Circle
from IPython.display import HTML

TEAL, CARDINAL, GRAY, PURPLE = "#107895", "#C8102E", "#6c757d", "#6a3d9a"
R2, N_FR, OM = 1.0, 72, 1.0           # radius, frames, angular velocity
SV, SA = 0.62, 0.48                   # arrow scale factors
th_seq = np.linspace(0, 2 * np.pi, N_FR, endpoint=False)

fig_cm, (cx, dx) = plt.subplots(1, 2, figsize=(10.4, 4.5),
                                gridspec_kw={"width_ratios": [1.15, 1.2]})

cx.add_patch(Circle((0, 0), R2, fill=False, color=GRAY, lw=1.2, ls="--"))
cx.plot(0, 0, "o", color=CARDINAL, ms=11)
cx.text(0.10, -0.22, "nucleus", color=CARDINAL, fontsize=8)
(bead,) = cx.plot([], [], "o", color="k", ms=9, zorder=6)

def arrow(color, ls="-", lw=2.2):
    return cx.annotate("", xy=(0, 0), xytext=(0, 0), zorder=5,
                       arrowprops=dict(arrowstyle="-|>", color=color, lw=lw,
                                       ls=ls, shrinkA=0, shrinkB=0))

a_r, a_v, a_a, a_cf = arrow(GRAY, lw=1.3), arrow(TEAL), arrow(PURPLE), arrow(CARDINAL, "--")
a_r.arrow_patch.set_alpha(0.45)
cx.set_xlim(-1.75, 1.75)
cx.set_ylim(-1.6, 1.6)
cx.set_aspect("equal")
cx.axis("off")
cx.legend(handles=[plt.Line2D([], [], color=GRAY, lw=1.3, alpha=0.45, label=r"$\vec{r}$  position"),
                   plt.Line2D([], [], color=TEAL, lw=2.2, label=r"$\vec{v}$  velocity (tangent)"),
                   plt.Line2D([], [], color=PURPLE, lw=2.2, label=r"$\vec{a}$  centripetal (inward)"),
                   plt.Line2D([], [], color=CARDINAL, lw=2.2, ls="--",
                              label="centrifugal (rotating frame)")],
          loc="lower center", bbox_to_anchor=(0.5, -0.16), fontsize=7.5, frameon=False)

t_full = th_seq / OM
dx.plot(t_full, R2 * np.cos(th_seq), color=GRAY, lw=1.6, label=r"$x = R\cos\omega t$")
dx.plot(t_full, -OM * R2 * np.sin(th_seq), color=TEAL, lw=1.6, label=r"$v_x = -\omega R\sin\omega t$")
dx.plot(t_full, -OM**2 * R2 * np.cos(th_seq), color=PURPLE, lw=1.6,
        label=r"$a_x = -\omega^2 R\cos\omega t$")
sweep = dx.axvline(0, color="k", lw=0.9, alpha=0.45)
(m_x,) = dx.plot([], [], "o", color=GRAY, ms=7)
(m_v,) = dx.plot([], [], "o", color=TEAL, ms=7)
(m_a,) = dx.plot([], [], "o", color=PURPLE, ms=7)
dx.axhline(0, color="k", lw=0.6, alpha=0.3)
dx.set_xlim(0, t_full[-1])
dx.set_ylim(-1.5, 1.9)
dx.set_xlabel("time")
dx.set_yticks([])
dx.legend(loc="upper right", fontsize=7.5, frameon=False)
dx.set_title("each component is simple harmonic motion", fontsize=9)
for sp in ("top", "right", "left"):
    dx.spines[sp].set_visible(False)

fig_cm.suptitle("Fig. Circular motion: position, velocity and centripetal acceleration.\n"
                "The magnitudes never change, only the directions.", fontsize=10)
fig_cm.tight_layout()

def frame_cm(i):
    th = th_seq[i]
    p = np.array([R2 * np.cos(th), R2 * np.sin(th)])
    rhat, that = p / R2, np.array([-np.sin(th), np.cos(th)])
    bead.set_data([p[0]], [p[1]])
    a_r.xy = p
    a_r.set_position((0, 0))
    a_v.xy = p + SV * OM * R2 * that
    a_v.set_position(p)
    a_a.xy = p - SA * OM**2 * R2 * rhat
    a_a.set_position(p)
    a_cf.xy = p + SA * OM**2 * R2 * rhat
    a_cf.set_position(p)
    sweep.set_xdata([t_full[i], t_full[i]])
    m_x.set_data([t_full[i]], [p[0]])
    m_v.set_data([t_full[i]], [-OM * R2 * np.sin(th)])
    m_a.set_data([t_full[i]], [-OM**2 * R2 * np.cos(th)])
    return bead, a_r, a_v, a_a, a_cf, sweep, m_x, m_v, m_a

ani_cm = FuncAnimation(fig_cm, frame_cm, frames=N_FR, interval=50, blit=False)
plt.close(fig_cm)
HTML(ani_cm.to_jshtml())
```
::::

---

The **force-balance equation** together with the **quantized angular momentum condition** restricts the allowed radii $r$ of electron orbits. Solving step by step:  


``````{admonition} 中文翻译
:class: dropdown

**力平衡方程** 与 **量子化角动量条件** 共同限制了电子轨道允许的半径 $r$。分步求解如下：
``````

1. From angular momentum quantization:  

   $$
   m_e v r = n\hbar \quad \Rightarrow \quad v = \frac{n\hbar}{m_e r}.
   $$  

2. Substituting into the force-balance equation:  

   $$
   \frac{e^2}{4\pi\varepsilon_0 r^2} = \frac{m_e}{r} \left( \frac{n\hbar}{m_e r} \right)^2.
   $$  

3. Simplifying:  

   $$
   \frac{e^2}{4\pi\varepsilon_0} = \frac{(n\hbar)^2}{m_e r}.
   $$  

4. Solving for $r$:  

   $$
   r = \frac{4\pi \varepsilon_0 (n\hbar)^2}{m_e e^2} = n^2 a_0, \quad n = 1, 2, 3, \ldots
   $$  

- where the constant $a_0$ is the **Bohr radius**, corresponding to the size of the ground-state orbit.  
- We see clearly that the radius of an orbit grows with increasing quantum number $n=1,2,3$.


``````{admonition} 中文翻译
:class: dropdown

- 其中常数 $a_0$ 是**玻尔半径**，对应基态轨道的大小。
- 我们清楚地看到，轨道半径随量子数 $n=1,2,3$ 的增加而增大。
``````


:::{tip} **Bohr radius**

$$
a_0 = \frac{4\pi \varepsilon_0 \hbar^2}{m_e e^2}
$$  

$$a_0 \approx 0.529 \,\text{Å}$$

- We will encounter the Bohr radius many times. It sets the fundamental length scale for atomic physics!


``````{admonition} 中文翻译
:class: dropdown

- 我们将多次遇到玻尔半径。它设定了原子物理学的基本长度尺度！
``````
:::


### Energy of the Hydrogen Atom

The total energy of the electron-proton system is the sum of the electron’s **kinetic energy** and the **Coulomb potential energy**:  


``````{admonition} 中文翻译
:class: dropdown

电子-质子系统的总能量是电子的**动能**与**库仑势能**之和：
``````

$$
E(r) = \tfrac{1}{2} m_e v^2 - \frac{e^2}{4\pi\varepsilon_0 r}.
$$  

Using the force-balance relation  

$$
m_e v^2 = \frac{e^2}{4\pi\varepsilon_0 r},
$$  

we substitute into the energy expression:  

$$
\begin{align}
E(r) &= \tfrac{1}{2}\frac{e^2}{4\pi\varepsilon_0 r} - \frac{e^2}{4\pi\varepsilon_0 r} \\
     &= -\tfrac{1}{2}\frac{e^2}{4\pi\varepsilon_0 r}.
\end{align}
$$  

Next, inserting the quantized orbital radius  

$$
r = \frac{4\pi \varepsilon_0 (n\hbar)^2}{m_e e^2},
$$  

gives the **Bohr energy levels**:  

$$
E_n = -\frac{m_e e^4}{8 \varepsilon_0^2 h^2} \cdot \frac{1}{n^2}, 
\quad n = 1, 2, 3, \ldots
$$  


:::{important} **Bohr Energy formula**

$$
E_n = -13.6\frac{ 1}{n^2} \,\,\,[eV]
$$  

- This is the most useful form for problem solving. You can quickly compute the energy of any hydrogenic level just by inserting the principal quantum number $n$.  

- Ionization energy corresponds to taking the electron from $n=1$ to $n \to \infty$, requiring exactly 13.6 eV.  

- You can compute the energy (or frequency) of the photon for a jump from state $n$ to $m$ by taking the difference between energy levels: $\Delta E_{n\rightarrow m} = 13.6\,(1/m^2-1/n^2)\,\text{eV} = h\nu$ for an emission from a higher level $n$ down to a lower level $m$  


``````{admonition} 中文翻译
:class: dropdown

- 这是解题最有用的形式。只需代入主量子数 $n$，就能快速计算任意类氢原子能级的能量。
- 电离能对应将电子从 $n=1$ 转移到 $n \to \infty$，恰好需要 13.6 eV。
- 可以通过计算从态 $n$ 跃迁到态 $m$ 的光子能量（或频率），方法是能级差：$\Delta E_{n\rightarrow m} = 13.6\,(1/m^2-1/n^2)\,\text{eV} = h\nu$ 对应从高能级 $n$ 跃迁到低能级 $m$ 的发射
``````

:::



### Spectral lines and the Rydberg constant  

The energy difference between two levels $n_1$ and $n_2$ is  


``````{admonition} 中文翻译
:class: dropdown

两个能级 $n_1$ 和 $n_2$ 之间的能量差为
``````

$$
\Delta E = \frac{m_e e^4}{8 \varepsilon_0^2 h^2}
\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right).
$$  

Relating this to photon energy $E = h\nu$ and the wavenumber $\tilde{\nu} = \nu/c$ gives  


``````{admonition} 中文翻译
:class: dropdown

将其与光子能量 $E = h\nu$ 及波数 $\tilde{\nu} = \nu/c$ 联系起来可得
``````

$$
\tilde{\nu} = \frac{m_e e^4}{8 \varepsilon_0^2 c h^3}
\left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right)
= R_H \left(\frac{1}{n_1^2} - \frac{1}{n_2^2}\right),
$$  

where $R_H$ is the **Rydberg constant**, which we now know expressed in fundamental constants rather than obtained as the result of an experimental fit!


``````{admonition} 中文翻译
:class: dropdown

其中 $R_H$ 是 **里德伯常数**，我们现在知道它可以用基本常数表示，而不是作为实验拟合的结果获得！
``````

$$
R_H = \frac{m_e e^4}{8 \varepsilon_0^2 c h^3}
$$  

:::{figure} images/hydrogen_levels_series.png
:label: fig-atomic-spectra-7
:alt: Hydrogen energy levels with Lyman, Balmer and Paschen transitions
:width: 75%

Fig. Hydrogen energy levels and the three lowest spectral series. Every series shares one
lower level, and the lines of a series crowd together as $n_2$ grows, converging on the
series limit where the electron is set free.


``````{admonition} 中文翻译
:class: dropdown

图。氢能级和三个最低光谱系列。每个系列共享一个下级，随着 $n_2$ 增长，系列的线靠拢，收敛于系列极限，此时电子被释放。
``````
:::


:::{tip} **A note about wavenumbers and $cm^{-1}$ units**

- Wavenumbers $\tilde{\nu}$ in **cm⁻¹** are standard in spectroscopy.  
- To convert to wavelength: $\lambda = 1 / \tilde{\nu}$ (with $\tilde{\nu}$ in cm⁻¹, $\lambda$ will come out in cm).  


``````{admonition} 中文翻译
:class: dropdown

- 以 **cm⁻¹** 为单位的波数 $\tilde{\nu}$ 是光谱学的标准。
- 转换为波长：$\lambda = 1 / \tilde{\nu}$（其中 $\tilde{\nu}$ 单位为 cm⁻¹，则 $\lambda$ 单位为 cm）。
``````


$$
\tilde{\nu}\ \text{(cm}^{-1}\text{)} 
= R_H \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right),
\quad n_2 > n_1,
$$  

- $R_H = 1.097 \times 10^5 \ \text{cm}^{-1}$ is the Rydberg constant in spectroscopic units.


``````{admonition} 中文翻译
:class: dropdown

- $R_H = 1.097 \times 10^5 \ \text{cm}^{-1}$ 是光谱单位下的里德伯常数。
``````
:::

### Hydrogen-like atoms

- For one-electron atoms such as $He^{+}$ and $Li^{2+}$, the Bohr model still works, but we have to account for the increased nuclear charge $Z$.


``````{admonition} 中文翻译
:class: dropdown

- 对于 $He^{+}$ 和 $Li^{2+}$ 等单电子原子，玻尔模型仍然适用，但必须考虑增加的核电荷 $Z$。
``````

$$
E_n = -13.6 \frac{Z^2}{n^2}, [eV]
$$

- E.g. for the $H$ atom $Z=1$, for $He^{+}$ $Z=2$, etc.


``````{admonition} 中文翻译
:class: dropdown

- 例如，对于 $H$ 原子 $Z=1$，对于 $He^{+}$ $Z=2$，等等。
``````

### Explore the hydrogen spectrum

Every spectral series is the set of transitions that end on one lower level. Slide $n_1$ to move from the Lyman series (ultraviolet) through Balmer (the visible lines of a hydrogen lamp) to Paschen and Brackett (infrared). Raise $Z$ to see how a one-electron ion like $He^+$ pulls all levels down by $Z^2$ and pushes every line to shorter wavelengths.


``````{admonition} 中文翻译
:class: dropdown

每个光谱系列都是以一个低能级为终点的跃迁集合。将 $n_1$ 向下滑动，从朗曼系列（紫外）经过巴尔默（氦灯的可见线）到帕申和布拉肯特（红外）。升高 $Z$ 可看到单电子离子如 $He^+$ 如何用 $Z^2$ 拉低所有能级，并将每条线推向更短的波长。
``````

```{marimo-config}
---
pyproject: |
  requires-python = ">=3.10"
  dependencies = [
      "numpy",
      "matplotlib",
  ]
---
```

```{marimo} python
:hide-code: true

import marimo as mo
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.dpi"] = 150
```

```{marimo} python
:hide-code: true

n_low = mo.ui.slider(1, 4, step=1, value=2, show_value=True, label="lower level n1")
Z_h = mo.ui.slider(1, 3, step=1, value=1, show_value=True, label="nuclear charge Z")
mo.vstack([n_low, Z_h])
```

```{marimo} python
:hide-code: true

E_ry = 13.6
n1_h, Z1 = n_low.value, Z_h.value
levels_h = np.arange(1, 9)
E_h = -E_ry * Z1**2 / levels_h**2
series_names = {1: "Lyman", 2: "Balmer", 3: "Paschen", 4: "Brackett"}
def wl_color(w):                       # true colour of a line, grey outside the visible
    if w < 380 or w > 750: return "#8c8c8c"
    if w < 440: return "#7b2fbe"
    if w < 490: return "#2b6fd6"
    if w < 510: return "#12b5a6"
    if w < 580: return "#3aa93a"
    if w < 645: return "#e0a521"
    return "#C8102E"
fig4, (axL, axR) = plt.subplots(1, 2, figsize=(9, 3.8), gridspec_kw={"width_ratios": [1, 1.4]})
for n_i, E_i in zip(levels_h, E_h):
    axL.hlines(E_i, 0, 1, color="C3" if n_i == n1_h else "k", lw=1.6)
    if n_i <= 3:
        axL.text(1.03, E_i, f"n = {n_i}", va="center", fontsize=8)
axL.hlines(0, 0, 1, color="gray", ls="--", lw=1)
axL.text(1.03, 0, "n = ∞", va="center", fontsize=8, color="gray")
lam_lines = []
for k_i, n2_i in enumerate(range(n1_h + 1, n1_h + 7)):
    dE_i = E_ry * Z1**2 * (1 / n1_h**2 - 1 / n2_i**2)
    lam_lines.append(1239.84 / dE_i)
    c_i = wl_color(lam_lines[-1])
    x_i = 0.12 + 0.13 * k_i
    axL.annotate("", xy=(x_i, E_h[n1_h - 1]), xytext=(x_i, -E_ry * Z1**2 / n2_i**2),
                 arrowprops=dict(arrowstyle="->", color=c_i, lw=1.3))
    axR.axvline(lam_lines[-1], color=c_i, lw=2)
axL.set_xlim(0, 1.5)
axL.set_ylim(E_h[0] * 1.08, 0.08 * E_ry * Z1**2)
axL.set_xticks([])
axL.set_ylabel("energy (eV)")
axR.axvspan(380, 750, color="gold", alpha=0.15)
axR.set_title("shaded band: visible light", fontsize=8, color="darkgoldenrod")
axR.set_xscale("log")
axR.set_xlim(10, 5000)
axR.set_yticks([])
axR.set_xlabel("wavelength (nm), log scale")
fig4.suptitle(f"Fig. {series_names[n1_h]} series for Z = {Z1}, lines from {lam_lines[-1]:.0f} nm to {lam_lines[0]:.0f} nm", fontsize=10)
fig4.tight_layout()
fig4
```

### Where Bohr's model breaks down

Bohr's model reproduces the hydrogen spectrum to four digits, and that success is exactly
why its failures matter. Within a decade it was clear that the model was a lucky halfway
house rather than the final theory.


``````{admonition} 中文翻译
:class: dropdown

玻尔模型将氢谱再现到四位小数，这种成功正是
为什么它的失败很重要。几十年内人们清楚，该模型只是一个幸运的折中方案，而不是最终理论。
``````

- **It fails for every atom with more than one electron.** Applied to neutral helium it
  misses the measured ionization energy of 24.6 eV badly, and it says nothing at all about
  the periodic table.
- **It predicts where lines are but not how bright.** Real spectra have strong lines, weak
  lines, and transitions that never appear at all. Bohr's rules give no intensities and no
  selection rules.
- **It cannot see fine structure.** At high resolution each Balmer line splits into closely
  spaced components, and a magnetic field splits them further (the Zeeman effect). A single
  quantum number $n$ has no room for this.
- **It assumes an orbit at all.** A definite radius together with a definite speed violates
  the uncertainty principle from the previous lecture. The ground state of hydrogen in fact
  has zero orbital angular momentum, not $\hbar$.


``````{admonition} 中文翻译
:class: dropdown

- **它对于多电子原子均失效。** 当应用于中性氦时，它严重偏离测得的电离能 24.6 eV，且对周期律一无所知。
- **它能预测线的位置，但不能预测亮度。** 真实光谱包含强线、弱线，以及根本不出现的过渡。玻尔的规则既不给出强度，也不给出选取规则。
- **它看不了细结构。** 在高分辨率下，每一条巴尔mer线都分裂成密仄分量，且在磁场进一步分裂（塞曼效应）。单一的量子数 $n$ 没有容纳这一点的空间。
- **它假设所有情况都有轨道。** 确定的半径加上确定的速度违反了上一讲的不确定性原理。氢原子的基态实际上没有轨道角动量，是 0，而不是 $\hbar$。
``````

What survives is the physics, not the picture: energies are quantized, the quantum number
is an integer, and light is emitted when the atom drops from one level to another. Chapter
5 replaces the orbit with a wavefunction and gets the levels right for the right reason,
Chapter 6 supplies the missing selection rules, and Chapter 7 takes on helium.


``````{admonition} 中文翻译
:class: dropdown

幸存的是物理，而非图像：能量是量子化的，量子数是整数，当原子从一个能级下跃到另一个能级时发射光。第5章用波函数取代轨道，并用正确的原因得到正确的能级；第6章补充缺失的选取规则，第7章处理氦原子。
``````

### Problems

#### Problem 1: Lyman alpha

The so-called Lyman series of lines in the emission spectrum of hydrogen corresponds to transitions from various excited states to the n = 1 orbit. Calculate the wavelength of the lowest-energy line in the Lyman series to three significant figures. In what region of the electromagnetic spectrum does it occur?


``````{admonition} 中文翻译
:class: dropdown

氢原子发射光谱中所谓的朗德系列对应于各种激发态向 n = 1 轨道的跃迁。计算朗德系列最低能线的波长，并保留三位有效数字。它位于电磁谱的哪个区域？
``````

:::{admonition} **Solution**
:class: dropdown solution

**A** We can use the Rydberg equation  to calculate the wavelength for the Lyman series, $n_1 = 1$.


``````{admonition} 中文翻译
:class: dropdown

**A** 我们可以使用里德伯公式来计算莱曼系列的波长，$n_1 = 1$。
``````

$$
\dfrac{1}{\lambda }=R_H \left ( \dfrac{1}{n_{1}^{2}} - \dfrac{1}{n_{2}^{2}}\right )
$$

The lowest energy results from a transition to or from the nearest energy level, hence $n_2 = n_1+1$.


``````{admonition} 中文翻译
:class: dropdown

最低能量来自于向最近能级或从最近能级的跃迁，因此 $n_2 = n_1+1$。
``````

$$
\begin{align*} \dfrac{1}{\lambda } &=R_H \left ( \dfrac{1}{n_{1}^{2}} - \dfrac{1}{n_{2}^{2}}\right ) \\[4pt] &=1.097 \times 10^{7}\, m^{-1}\left ( \dfrac{1}{1}-\dfrac{1}{4} \right )\\[4pt] &= 8.228 \times 10^{6}\; m^{-1} \end{align*}
$$


Spectroscopists often talk about energy and frequency as equivalent. The $cm^{-1}$ unit (wavenumbers) is particularly convenient. We can convert the answer in part A to $cm^{-1}$


``````{admonition} 中文翻译
:class: dropdown

光谱学家经常把能量和频率当作等价的。$cm^{-1}$ 单位（波数）特别方便。我们可以把 A 部分的答案转换为 $cm^{-1}$
``````

$$
\begin{align*} \widetilde{\nu} &=\dfrac{1}{\lambda } \\[4pt] &= 8.228\times 10^{6}\cancel{m^{-1}}\left (\dfrac{\cancel{m}}{100\;cm} \right ) \\[4pt] &= 82,280\: cm^{-1} \end{align*}
$$

and

$$\lambda = 1.215 \times 10^{−7}\; m = 122 \,\,nm$$

This emission line is called Lyman alpha. It is the strongest atomic emission line from the Sun and drives the chemistry of the upper atmosphere of all the planets, producing ions by stripping electrons from atoms and molecules. It is completely absorbed by oxygen in the upper stratosphere, dissociating O2 molecules into O atoms, which react with other O2 molecules to form stratospheric ozone.


``````{admonition} 中文翻译
:class: dropdown

这条发射线称为朗曼 alpha。它是太阳上最强的原子发射线，驱动所有行星大气层的化学反应，通过剥离原子和分子上的电子产生离子。它完全被上层平流层的氧气吸收，将 O2 分子解离成 O 原子，这些 O 原子与其他 O2 分子反应形成平流层臭氧。
``````

**B** This wavelength is in the UV region of the spectrum.


``````{admonition} 中文翻译
:class: dropdown

**B** 该波长位于光谱的紫外区域。
``````
:::

#### Problem 2: Photon from n = 4 to n = 1

- A. Calculate the energy of a photon that is produced when an electron in a hydrogen atom goes from an orbit with $n=4$ to an orbit with $n=1$.
- B. What happens to the energy of the photon as the initial value of $n$ approaches infinity?


``````{admonition} 中文翻译
:class: dropdown

- A. 计算当氢原子中的电子从 $n=4$ 轨道跃迁到 $n=1$ 轨道时产生的光子能量。
- B. 当 $n$ 的初始值趋于无穷大时，光子的能量会发生什么变化？
``````


:::{admonition} **Solution**
:class: dropdown solution

**A.**  We will use Bohr's formula in electron volts, $E_n = -13.6 \frac{1}{n^2}$, to calculate the energy of a photon.


``````{admonition} 中文翻译
:class: dropdown

**A.** 我们将使用玻尔公式（以电子伏特为单位），$E_n = -13.6 \frac{1}{n^2}$，来计算光子的能量。
``````

$$\Delta E = 13.6  \Big ( \frac{1}{1^2} - \frac{1}{4^2} \Big) = 13.6 \cdot 0.9375 = 12.75\,\, \text{eV}$$

**B.** The energy of the photon goes up as the electron starts from higher and higher levels, but it saturates. As $n \rightarrow \infty$ the photon energy approaches the ionization energy of hydrogen: $E = 13.6 \cdot \Big( \frac{1}{1^2} - \frac{1}{\infty} \Big) = 13.6\,\, \text{eV}$. Lines pile up against this limit, which is why each spectral series ends in a continuum.


``````{admonition} 中文翻译
:class: dropdown

**B.** 光子能量随着电子从更高能级开始而增加，但它会饱和。随着 $n \rightarrow \infty$，光子能量趋近于氢的电离能：$E = 13.6 \cdot \Big( \frac{1}{1^2} - \frac{1}{\infty} \Big) = 13.6\,\, \text{eV}$。光谱线聚集在该极限附近，这就是每个光谱系列以连续谱结尾的原因。
``````
:::

#### Problem 3: First lines of the Lyman series

Use Rydberg's formula to calculate the first few lines of the Lyman series ($n_1=1$).


``````{admonition} 中文翻译
:class: dropdown

用里德伯公式计算莱曼系（$n_1=1$）的前几条谱线。
``````

:::{admonition} **Solution**
:class: dropdown solution
The Rydberg formula is given by:

$$
\frac{1}{\lambda} = R_H \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right)
$$

For the Lyman series, $n_1 = 1$, and $n_2 = 2, 3, 4, \dots$. The Rydberg constant for hydrogen is:


``````{admonition} 中文翻译
:class: dropdown

对于莱曼系，$n_1 = 1$，且 $n_2 = 2, 3, 4, \dots$。氢的里德伯常数为：
``````

$$
R_H = 1.097 \times 10^7 \ \text{m}^{-1}
$$

**First few lines of the Lyman series:**

For $n_2 = 2$:

$$
\frac{1}{\lambda} = 1.097 \times 10^7 \left( \frac{1}{1^2} - \frac{1}{2^2} \right)
$$

$$
\lambda = 1.2157 \times 10^{-7} \ \text{m} = 121.57 \ \text{nm}
$$

For $n_2 = 3$:

$$
\frac{1}{\lambda} = 1.097 \times 10^7 \left( \frac{1}{1^2} - \frac{1}{3^2} \right)
$$

$$
\lambda = 1.0257 \times 10^{-7} \ \text{m} = 102.57 \ \text{nm}
$$

For $n_2 = 4$:

$$
\frac{1}{\lambda} = 1.097 \times 10^7 \left( \frac{1}{1^2} - \frac{1}{4^2} \right)
$$

$$
\lambda = 9.724 \times 10^{-8} \ \text{m} = 97.24 \ \text{nm}
$$

So, the first three wavelengths of the Lyman series are approximately $121.57$ nm, $102.57$ nm, and $97.24$ nm.


``````{admonition} 中文翻译
:class: dropdown

因此，莱曼系的前三个波长约为 $121.57$ nm、$102.57$ nm 和 $97.24$ nm。
``````


:::

#### Problem 4: Which level did the electron come from?

A line in the Lyman series of hydrogen has a wavelength of $1.03 \cdot 10^{-7} m$. Find the original level of the electron.


``````{admonition} 中文翻译
:class: dropdown

氢原子莱曼系的一条谱线波长为 $1.03 \cdot 10^{-7} m$。求电子原本所在的能级。
``````

:::{admonition} **Solution**
:class: dropdown solution

We are given a wavelength $\lambda = 1.03 \times 10^{-7} \ \text{m}$ and asked to find the original level $n_2$ of the electron in the Lyman series (where $n_1 = 1$).


``````{admonition} 中文翻译
:class: dropdown

已知波长 $\lambda = 1.03 \times 10^{-7} \ \text{m}$，要求求出朗伯系列中电子的原始能级 $n_2$（其中 $n_1 = 1$）。
``````

Using the Rydberg formula:

$$
\frac{1}{\lambda} = R_H \left( \frac{1}{n_1^2} - \frac{1}{n_2^2} \right)
$$

For the Lyman series, $n_1 = 1$, so the equation becomes:


``````{admonition} 中文翻译
:class: dropdown

对于莱曼系，$n_1 = 1$，因此方程变为：
``````

$$
\frac{1}{\lambda} = R_H \left( 1 - \frac{1}{n_2^2} \right)
$$

Rearranging to solve for $n_2$:

$$
\frac{1}{n_2^2} = 1 - \frac{1}{R_H \lambda}
$$

Substituting the values:

$$
R_H = 1.097 \times 10^7 \ \text{m}^{-1}
$$

$$
\frac{1}{n_2^2} = 1 - \frac{1}{(1.097 \times 10^7) \times (1.03 \times 10^{-7})}
$$

$$
\frac{1}{n_2^2} = 1 - \frac{1}{1.13091} = 1 - 0.884 = 0.116
$$

Now, solving for $n_2$:

$$
n_2^2 = \frac{1}{0.116} = 8.621
$$

$$
n_2 = \sqrt{8.621} \approx 2.94
$$

Since $n_2$ must be an integer, we round it to $n_2 = 3$.


``````{admonition} 中文翻译
:class: dropdown

由于 $n_2$ 必须是整数，我们将其取整为 $n_2 = 3$。
``````

Thus, the original level of the electron is $n_2 = 3$.


``````{admonition} 中文翻译
:class: dropdown

因此，电子的原始能级为 $n_2 = 3$。
``````


:::


#### Problem 5: Ionization energy of He+

Using Bohr theory calculate the ionization energy of singly ionized helium $He^{+}$.


``````{admonition} 中文翻译
:class: dropdown

利用玻尔理论计算单电离氦离子 $He^{+}$ 的电离能。
``````

:::{admonition} **Solution**
:class: dropdown solution

The ionization energy is the energy required to remove an electron from its ground state to infinity. Using Bohr's theory, the energy of an electron in an orbit is given by:


``````{admonition} 中文翻译
:class: dropdown

ionization energy 是将电子从基态移除到无穷远所需的能量。 使用玻尔理论，电子在轨道上的能量由：
``````

$$
E_n = -\frac{Z^2 E_{\text{Ry}}}{n^2}
$$

Where:
- $Z$ is the atomic number,
- $E_{\text{Ry}} = 13.6 \ \text{eV}$ is the Rydberg energy, the ionization energy of hydrogen (not to be confused with the Rydberg constant $R_H$ in $\text{m}^{-1}$, which is $E_{\text{Ry}}/hc$),
- $n$ is the principal quantum number.


``````{admonition} 中文翻译
:class: dropdown

- $Z$ 是原子序数，
- $E_{\text{Ry}} = 13.6 \ \text{eV}$ 是瑞德伯能量，氢的电离能（不可与单位为 $\text{m}^{-1}$ 的瑞德伯常数 $R_H$ 混淆，后者为 $E_{\text{Ry}}/hc$），
- $n$ 是主量子数。
``````

For singly ionized helium $He^+$, the atomic number $Z = 2$. In the ground state, $n = 1$.


``````{admonition} 中文翻译
:class: dropdown

对于单电离氦 $He^+$，原子序数 $Z = 2$。基态下 $n = 1$。
``````

Thus, the energy in the ground state is:


``````{admonition} 中文翻译
:class: dropdown

因此，基态的能量为：
``````

$$
E_1 = -\frac{Z^2 E_{\text{Ry}}}{1^2} = -\frac{(2)^2 \times 13.6 \ \text{eV}}{1^2} = -4 \times 13.6 \ \text{eV} = -54.4 \ \text{eV}
$$

The ionization energy is the negative of this ground state energy (since we want to bring the electron to $n = \infty$):


``````{admonition} 中文翻译
:class: dropdown

电离能是该基态能量的负值（因为我们要将电子带到 $n = \infty$ 处）：
``````

$$
E_{\text{ionization}} = 54.4 \ \text{eV}
$$

Therefore, the ionization energy of singly ionized helium $He^+$ is $54.4 \ \text{eV}$.


``````{admonition} 中文翻译
:class: dropdown

因此，单电离氦 $He^+$ 的电离能为 $54.4 \ \text{eV}$。
``````

:::

#### Problem 6: Bohr radii

- Calculate the radii of the Bohr orbits for the first few levels. 

- (Optional) Using python plot $r_n$ vs $n$


``````{admonition} 中文翻译
:class: dropdown

- 计算前几个能级的玻尔轨道半径。
- (Optional) Using python plot $r_n$ vs $n$
``````

:::{admonition} **Solution**
:class: dropdown solution

The radius of the Bohr orbit is given by the formula:


``````{admonition} 中文翻译
:class: dropdown

玻尔轨道的半径由以下公式给出：
``````

$$
r_n = \frac{n^2 a_0}{Z}
$$

Where:
- $n$ is the principal quantum number (level),
- $a_0 = 5.29 \times 10^{-11} \ \text{m}$ is the Bohr radius for hydrogen,
- $Z$ is the atomic number (for hydrogen, $Z = 1$).


``````{admonition} 中文翻译
:class: dropdown

- $n$ 是主量子数（能级），
- $a_0 = 5.29 \times 10^{-11} \ \text{m}$ 是氢原子的玻尔半径，
- $Z$ 是原子序数（对于氢，$Z = 1$）。
``````

For hydrogen ($Z = 1$), the radii for the first few levels are:


``````{admonition} 中文翻译
:class: dropdown

对于氢原子（$Z = 1$），前几个能级的半径为：
``````

**For $n = 1$:**
$$
r_1 = \frac{1^2 \times 5.29 \times 10^{-11} \ \text{m}}{1} = 5.29 \times 10^{-11} \ \text{m}
$$

**For $n = 2$:**
$$
r_2 = \frac{2^2 \times 5.29 \times 10^{-11} \ \text{m}}{1} = 4 \times 5.29 \times 10^{-11} \ \text{m} = 2.116 \times 10^{-10} \ \text{m}
$$

**For $n = 3$:**
$$
r_3 = \frac{3^2 \times 5.29 \times 10^{-11} \ \text{m}}{1} = 9 \times 5.29 \times 10^{-11} \ \text{m} = 4.761 \times 10^{-10} \ \text{m}
$$

**For $n = 4$:**
$$
r_4 = \frac{4^2 \times 5.29 \times 10^{-11} \ \text{m}}{1} = 16 \times 5.29 \times 10^{-11} \ \text{m} = 8.464 \times 10^{-10} \ \text{m}
$$

Therefore, the radii of the Bohr orbits for the first few levels are:


``````{admonition} 中文翻译
:class: dropdown

因此，玻尔轨道在前几个能级的半径为：
``````
- $r_1 = 5.29 \times 10^{-11} \ \text{m}$,
- $r_2 = 2.116 \times 10^{-10} \ \text{m}$,
- $r_3 = 4.761 \times 10^{-10} \ \text{m}$,
- $r_4 = 8.464 \times 10^{-10} \ \text{m}$.


``````{admonition} 中文翻译
:class: dropdown

- $r_1 = 5.29 \times 10^{-11} \ \text{m}$,
- $r_2 = 2.116 \times 10^{-10} \ \text{m}$,
- $r_3 = 4.761 \times 10^{-10} \ \text{m}$,
- $r_4 = 8.464 \times 10^{-10} \ \text{m}$.
``````

:::

#### Problem 7: The color of H-alpha

The brightest visible line of hydrogen, H-alpha, is the $n = 3 \to 2$ transition of the Balmer series. Compute its wavelength and name its color. Do the same for $n = 4 \to 2$ (H-beta). These two lines are what you see in a hydrogen discharge tube, and they give emission nebulae their red glow.


``````{admonition} 中文翻译
:class: dropdown

氢原子最亮的可见光谱线，H-alpha，是巴尔末系列的 $n = 3 \to 2$ 跃迁。计算其波长并命名其颜色。对 $n = 4 \to 2$ (H-beta) 同样处理。这两条线就是在氢放电管中看到的，它们赋予发射星云它们的红光。
``````

#### Problem 8: A coincidence between He+ and H

Show that the $n = 4 \to 2$ transition of $He^+$ emits a photon of exactly the same energy as the $n = 2 \to 1$ (Lyman alpha) transition of hydrogen. Find the general rule: which $He^+$ transitions coincide with hydrogen lines, and why?


``````{admonition} 中文翻译
:class: dropdown

证明 $He^+$ 的 $n = 4 \to 2$ 跃迁发射的光子能量正好与氢原子的 $n = 2 \to 1$（兰伯尔德 alpha）跃迁能量相同。找出一般规则：哪些 $He^+$ 跃迁与氢谱线重合，以及原因是什么？
``````

#### Problem 9: How fast is the electron?

Using $m_e v r = n\hbar$ and $r = n^2 a_0$, find the speed of the electron in the ground state of hydrogen and express it as a fraction of the speed of light. This dimensionless ratio is the fine-structure constant $\alpha \approx 1/137$. What does it say about the need for relativity in hydrogen, and what happens to the innermost electron of uranium ($Z = 92$)?


``````{admonition} 中文翻译
:class: dropdown

利用 $m_e v r = n\hbar$ 和 $r = n^2 a_0$，求氢原子基态电子的速度，并表示为光速的分数。这个无量纲比值是微结构常数 $\alpha \approx 1/137$。这对氢原子是否需要相对论说了什么，以及锕系元素铀（$Z = 92$）最内层电子会怎样？
``````

#### Problem 10: The edge of a series

Every spectral series has a longest wavelength (its first line) and a shortest (the series limit, $n_2 \to \infty$). Compute both for the Paschen series ($n_1 = 3$). In which region of the electromagnetic spectrum do they fall, and can the Paschen lines ever overlap with the Balmer lines?

``````{admonition} 中文翻译
:class: dropdown

每个光谱系列都有最长波长（其第一条线）和最短波长（系列极限，$n_2 \to \infty$）。计算帕申系列 ($n_1 = 3$) 的两者。它们位于电磁波谱的哪个区域？帕申线是否可能与巴尔mer 线重叠？
``````

