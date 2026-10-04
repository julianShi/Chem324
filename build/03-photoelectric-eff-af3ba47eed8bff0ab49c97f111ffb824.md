
# Photoelectric effect


:::{note} **What you will learn**

- **Photoelectric Effect:** Electrons are ejected from the surface of a material when it is exposed to radiation with a frequency exceeding a specific threshold frequency.
- **Threshold Frequency:** No electrons are ejected if the radiation's frequency is below this threshold, regardless of the light's intensity (brightness).
- **Classical vs. Quantum:** The photoelectric effect cannot be explained using classical mechanics, where energy is thought to increase continuously with light intensity. However, in quantum mechanics, energy is quantized. Radiation is treated as a stream of photons, which are discrete packets of energy.
- **Photon-Electron Interaction:** A single photon can eject a single electron if the photon has sufficient energy. Any excess energy is converted into the kinetic energy of the ejected electron, causing it to move faster.
- **Insufficient Energy:** Photons with energy below the threshold will not eject electrons; instead, they scatter off the material.
- **High-Intensity Light:** Even high-intensity light, which means more photons per unit area per unit time, cannot eject electrons if the photons lack sufficient energy.


``````{admonition} 中文翻译
:class: dropdown

- **光电效应:** 当材料表面暴露在阈值频率以上的辐射时，会从表面射出电子。
- **阈值频率：** 如果辐射频率低于此阈值，无论光强（亮度）如何，都不会发射电子。
- **经典与量子:** 光电效应无法用经典力学解释，其中能量被认为随着光强连续增加。然而，在量子力学中，能量是量子化的。辐射被视为光子流，光子是离散的能量包。
- **光子-电子相互作用：** 单个光子可以在具有足够能量的情况下击出单个电子。任何多余的能量都转化为击出的电子的动能，导致其运动加快。
- **能量不足：** 能量低于阈值的光子不会激发电子；相反，它们会被材料散射。
- **高强度光：** 即使是高强度光，这意味着单位面积单位时间内光子数更多，如果光子能量不足，也无法射出电子。
``````
:::


### Photoelectric effect challenges classical mechanical thinking.

:::{figure} ./images/lect2_Eflying.png
:label: fig-photoelectric-effect-1
:alt: applied photoelectric
:width: 70%

Effect of radiation on a material depending on frequency. Frequency increases from left to right.


``````{admonition} 中文翻译
:class: dropdown

辐射对材料的影响取决于频率。频率从左向右增加。
``````
:::

- When you shine radiation on a metal surface, above some **threshold frequency** electrons start flying off the surface. 
- Below this frequency no electrons are ejected, regardless of the intensity of the radiation. 
- This experiment challenged the classical way of thinking about radiation, according to which the energy of radiation is proportional to the amplitude of the wave, that is, its intensity or the brightness of the light. 


``````{admonition} 中文翻译
:class: dropdown

- 当你用辐射照射金属表面时，超过某个**阈值频率**，电子就会从表面飞出。
- 低于此频率时，无论辐射强度如何，都不会有电子被激发出来。
- 该实验挑战了关于辐射的经典思维，根据经典观点，辐射的能量与波的振幅成正比，即辐射的强度或光的亮度。
``````

### Introducing Photon

- Recall that to reconcile experiment with theory, Planck was already forced to introduce quantization of black bodies modeled as springs that can only assume discrete energies: $0, h\nu, 2h\nu, 3h\nu, …$ giving off radiation with the same frequencies! 

- At that time, this discreteness introduced by Planck was thought to be nothing more than a temporary mathematical trick to fit the experimental curve. 

- Einstein, on the other hand, was more imaginative and saw in Planck’s prescription more than just a math trick. He suggested that light can behave like a stream of particles with discrete, countable energy packets, which he called photons. This view was instrumental in making sense of the photoelectric experiment. 


``````{admonition} 中文翻译
:class: dropdown

- 回想一下，为了使实验与理论相符，普朗克不得不引入黑体（模型为只能假设离散能量的弹簧）的量化：$0, h\nu, 2h\nu, 3h\nu, …$ 并发出相同频率的辐射！
- 当时，普朗克引入的这种离散性被认为只不过是拟合实验曲线的一种暂时的数学技巧。
- 爱因斯坦另一方面更具想象力，他在普朗克的处方中看到了数学技巧之外的东西。他建议光可以像具有离散、可计数能量包的粒子流一样行为。这种观点在理解光电实验中起到了关键作用。
``````

:::{important} **Energy of Photon**

$$
E_{photon} = h\nu = \frac{hc}{\lambda}
$$

- $E_{photon}$ energy of a photon.
- $\nu$ frequency of a single photon.


``````{admonition} 中文翻译
:class: dropdown

- $E_{photon}$ 光子能量。
- $\nu$ 频率的单光子。
``````

:::

- Thus we see that both matter and radiation are quantized and given by the same relation of frequency times the Planck constant.


``````{admonition} 中文翻译
:class: dropdown

- 因此我们看到，物质和辐射都是量子化的，且由相同的频率乘以普朗克常数的关系给出。
``````

### Kinetic energy: frequency vs intensity


:::{figure} ./images/photoelectric_ke.png
:label: fig-photoelectric-effect-2
:alt: applied photoelectric
:width: 70%

Dependence of electron kinetic energy on the frequency of radiation hitting the material surface (left) and on the intensity of light for frequencies below and above threshold (right).


``````{admonition} 中文翻译
:class: dropdown

电子动能对照射材料表面的辐射频率的依赖性 (左) 和光强的依赖性，频率低于和高于阈值 (右)。
``````
:::


1. Frequency $\nu$ determines whether electrons will be ejected: $\nu>\nu_0$, but it does not affect the number of electrons (current)


2. Kinetic energy of an ejected electron is a linearly increasing function of the frequency of light with no dependence on the intensity: $KE\sim \nu$ 


``````{admonition} 中文翻译
:class: dropdown

- 频率 $\nu$ 决定电子是否会被激发出来：$\nu>\nu_0$，但不影响电子的数量（电流）
- 逸出电子的动能是光频率的线性增函数，与光强无关：$KE\sim \nu$
``````
   
3.  Contrary to the wave theory of light, increasing the intensity (brightness) of light does not eject electrons when the frequency is below the threshold $\nu < \nu_0$


``````{admonition} 中文翻译
:class: dropdown

- 与光波理论相反，当光的频率低于阈值 $\nu < \nu_0$ 时，增加光的强度（亮度）不会射出电子
``````

   

### Electric current: frequency vs intensity

:::{figure} ./images/photoelectric_current.png
:label: fig-photoelectric-effect-3
:alt: applied photoelectric
:width: 70%

Dependence of electron current on the frequency of radiation hitting the material surface (left) and on the intensity of light for a frequency above threshold (right).


``````{admonition} 中文翻译
:class: dropdown

辐射频率对材料表面电子电流的依赖（左）和阈值频率以上光强对电子电流的依赖（右）。
``````
:::

1. Once the threshold is reached $\nu>\nu_0$, frequency has no effect on electron current (number of electrons)

2. Once the threshold is reached $\nu>\nu_0$, increasing the intensity of light, on the other hand, increases the current linearly.


``````{admonition} 中文翻译
:class: dropdown

- 一旦达到阈值 $\nu>\nu_0$，频率对电子电流（电子数）没有影响
- 一旦达到阈值 $\nu>\nu_0$，另一方面，增加光强会使电流线性增加。
``````



### Photons explain photoelectric effect 

- **Light consists of photons**: tiny packets of energy carrying $E_{photon}=h\nu$ energy. 
- **Intensity of light**  quantifies number of photons. 
- **Frequency of light**  quantifies energy of photons. 
- If light radiates $n$ photons per second, then the total energy radiated per second is $nh\nu$
- **Particle nature of light:** 1 photon can "collide" with 1 electron and eject it if the photon has sufficient energy.


``````{admonition} 中文翻译
:class: dropdown

- **光由光子组成**：携带 $E_{photon}=h\nu$ 能量的微小能量包。
- **光强** 量化光子数量。
- **光频** 量化光子能量。
- 如果光每秒辐射 $n$ 个光子，则每秒辐射的总能量为 $nh\nu$
- **光的粒子性：** 1个光子可以与1个电子“碰撞”并将其弹出，前提是光子具有足够的能量。
``````


:::{important} **Energy of photon = work function + kinetic energy of electron**

$${E_{photon} = W_0 + KE}$$

$${h\nu = h\nu_0 + \frac{mv_e^2}{2}}$$

- **The work function $W_0=h\nu_0$** is the minimum amount of energy needed to remove an electron from a metal's surface, and it has different values for different materials. 
- The $\nu_0$ is the **threshold frequency:** the minimum frequency needed to eject an electron. If the frequency is lower than the threshold, the photon does not transfer any energy to the electron! 
- Any extra energy gets converted into kinetic energy $KE=mv_e^2/2$ of the ejected electron, where $v_e$ is the magnitude of the ejected electron's velocity. 


``````{admonition} 中文翻译
:class: dropdown

- **工作函数 $W_0=h\nu_0$** 是从金属表面移除电子所需的最小能量，不同材料具有不同的值。
- $\nu_0$ 是**阈值频率**：射出电子所需的最小频率。如果频率低于阈值，光子将不向电子传递任何能量！
- 多余的能量转化为弹出电子的动能 $KE=mv_e^2/2$，其中 $v_e$ 是弹出电子速度的大小。
``````
:::




### Applications of photoelectric effect

:::{figure} ./images/lec2_applic.jpg
:label: fig-photoelectric-effect-4
:alt: applied photoelectric
:width: 70%

Besides its historical role in the establishment of QM, the photoelectric effect has many practical applications. It is relevant to the design of solar cells, photovoltaics, photoelectron spectroscopy, night vision, and more.


``````{admonition} 中文翻译
:class: dropdown

除了在量子力学确立中的历史角色外，光电效应还有许多实际应用。它与太阳能电池、光伏、光电子谱、夜视等的设计相关。
``````
:::


### Explore photoelectric effect

Pick a metal and a wavelength. The line is Einstein's equation $KE_{max} = h\nu - W_0$ for that metal: its slope is always $h$, and only the intercept (the threshold $\nu_0$) moves when you change the metal. The marker shows the light you chose: a dot on the line when electrons come out, a cross on the axis when the photon energy falls short.


``````{admonition} 中文翻译
:class: dropdown

选一个金属和一个波长。光电效应中，线是爱因斯坦方程 $KE_{max} = h\nu - W_0$ 对于该金属：其斜率永远是 $h$，只有截距（阈值 $\nu_0$）在改变金属时移动。标记显示你选择的光：当电子出来时在线上的一个点，当光子能量不足时在轴上的一个叉。
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

metal_pe = mo.ui.dropdown(
    options={
        "cesium (W0 = 2.14 eV)": 2.14,
        "sodium (W0 = 2.28 eV)": 2.28,
        "potassium (W0 = 2.30 eV)": 2.30,
        "zinc (W0 = 4.33 eV)": 4.33,
        "copper (W0 = 4.70 eV)": 4.70,
        "platinum (W0 = 5.65 eV)": 5.65,
    },
    value="sodium (W0 = 2.28 eV)",
    label="metal",
)
lam_pe = mo.ui.slider(150, 800, step=5, value=400, show_value=True, label="light wavelength (nm)")
mo.vstack([metal_pe, lam_pe])
```

```{marimo} python
:hide-code: true

h_eV, c_pe = 4.1357e-15, 2.998e8
W_pe = metal_pe.value
nu0_pe = W_pe / h_eV
nu_light = c_pe / (lam_pe.value * 1e-9)
E_light = h_eV * nu_light
KE_light = E_light - W_pe
nu_ax = np.linspace(0, 2.5e15, 500)
ke_ax = np.where(nu_ax > nu0_pe, h_eV * nu_ax - W_pe, np.nan)
fig3, ax3 = plt.subplots(figsize=(6.5, 3.6))
ax3.plot(nu_ax / 1e14, ke_ax, lw=2, color="C3", label="KE_max = hν - W0")
ax3.plot([0, nu0_pe / 1e14], [0, 0], lw=5, color="gray", alpha=0.4, solid_capstyle="butt", label="no emission")
ax3.axhline(0, color="k", lw=0.8)
ax3.axvline(nu0_pe / 1e14, color="gray", ls=":", lw=1)
ax3.text(nu0_pe / 1e14 + 0.3, 6.3, "ν0", fontsize=10, color="gray")
if KE_light > 0:
    ax3.plot(nu_light / 1e14, KE_light, "o", ms=9, color="C0", zorder=5)
else:
    ax3.plot(nu_light / 1e14, 0, "x", ms=11, mew=2.5, color="C0", zorder=5)
ax3.axvspan(c_pe / 750e-9 / 1e14, c_pe / 380e-9 / 1e14, color="gold", alpha=0.15)
ax3.set_xlim(0, 25)
ax3.set_ylim(-0.5, 7)
ax3.set_xlabel(r"frequency $\nu$ ($10^{14}$ Hz)")
ax3.set_ylabel("KE$_{max}$ (eV)")
ax3.set_title(f"Fig. Photoelectron KE vs light frequency, threshold {nu0_pe / 1e14:.1f} x 10^14 Hz, shaded band is visible light", fontsize=9)
ax3.legend(frameon=False, fontsize=9, loc="center right")
fig3.tight_layout()
fig3
```

```{marimo} python
:hide-code: true

verdict_pe = (
    f"electrons fly off with KE_max = **{KE_light:.2f} eV**"
    if KE_light > 0
    else "**no electrons**, no matter how bright the light"
)
mo.md(f"Photon energy **{E_light:.2f} eV** at {lam_pe.value} nm versus work function **{W_pe:.2f} eV**: {verdict_pe}.")
```


### Problems

#### Problem 1: Threshold frequency

A certain metal has a work function of 4.5 eV. Calculate the threshold frequency ($\nu_0$) required to emit electrons from the metal surface.


``````{admonition} 中文翻译
:class: dropdown

某种金属的逸出功为 4.5 eV。计算从金属表面发射电子所需的阈值频率 ($\nu_0$)。
``````

:::{admonition} **Solution**
:class: dropdown solution

The threshold frequency $\nu_0$ is related to the work function $\phi$ by the equation:


``````{admonition} 中文翻译
:class: dropdown

阈值频率 $\nu_0$ 与逸出功 $\phi$ 由以下方程关联：
``````

$$
\phi = h\nu_0
$$

Where:
- $\phi = 4.5 \, \text{eV}$
- $h = 4.1357 \times 10^{-15} \, \text{eV} \cdot \text{s}$ (Planck's constant)


``````{admonition} 中文翻译
:class: dropdown

- $\phi = 4.5 \, \text{eV}$
- $h = 4.1357 \times 10^{-15} \, \text{eV} \cdot \text{s}$ （普朗克常数）
``````

Now, solve for $\nu_0$:

$$
\nu_0 = \frac{\phi}{h} = \frac{4.5 \, \text{eV}}{4.1357 \times 10^{-15} \, \text{eV} \cdot \text{s}} \approx 1.088 \times 10^{15} \, \text{Hz}
$$
:::

#### Problem 2: Maximum kinetic energy of photoelectrons

Ultraviolet light with a wavelength of 250 nm is incident on a metal surface with a work function of 3.0 eV. Calculate the maximum kinetic energy of the emitted photoelectrons.


``````{admonition} 中文翻译
:class: dropdown

波长为 250 nm 的紫外线照射在工作函数为 3.0 eV 的金属表面上。计算发射光电子的最大动能。
``````

:::{admonition} **Solution**
:class: dropdown solution

First, calculate the energy of the incident photons:


``````{admonition} 中文翻译
:class: dropdown

首先，计算入射光子的能量：
``````

$$
E_{\text{photon}} = \frac{hc}{\lambda}
$$

Where:
- $h = 6.626 \times 10^{-34} \, \text{J} \cdot \text{s}$
- $c = 3.00 \times 10^8 \, \text{m/s}$
- $\lambda = 250 \, \text{nm} = 250 \times 10^{-9} \, \text{m}$


``````{admonition} 中文翻译
:class: dropdown

- $h = 6.626 \times 10^{-34} \, \text{J} \cdot \text{s}$
- $c = 3.00 \times 10^8 \, \text{m/s}$
- $\lambda = 250 \, \text{nm} = 250 \times 10^{-9} \, \text{m}$
``````

$$
E_{\text{photon}} = \frac{6.626 \times 10^{-34} \times 3.00 \times 10^8}{250 \times 10^{-9}} \, \text{J} = 7.95 \times 10^{-19} \, \text{J}
$$

Convert this energy to eV:

$$
E_{\text{photon}} = \frac{7.95 \times 10^{-19} \, \text{J}}{1.602 \times 10^{-19} \, \text{J/eV}} \approx 4.96 \, \text{eV}
$$

The maximum kinetic energy $K_{\text{max}}$ of the emitted photoelectrons is given by:


``````{admonition} 中文翻译
:class: dropdown

发射光电子的最大动能 $K_{\text{max}}$ 由下式给出：
``````

$$
K_{\text{max}} = E_{\text{photon}} - \phi = 4.96 \, \text{eV} - 3.0 \, \text{eV} = 1.96 \, \text{eV}
$$
:::

#### Problem 3: Photoelectric current and light intensity

Explain how the intensity of incident light affects the photoelectric current, assuming the frequency of the light is above the threshold frequency.


``````{admonition} 中文翻译
:class: dropdown

假设光的频率高于阈值频率，解释入射光强度如何影响光电流。
``````

:::{admonition} **Solution**
:class: dropdown solution

In the photoelectric effect, the intensity of the incident light is proportional to the number of photons striking the metal surface per unit time. If the frequency of the light is above the threshold frequency, each photon has sufficient energy to eject an electron.


``````{admonition} 中文翻译
:class: dropdown

在光电效应中，入射光的强度与每单位时间击中金属表面的光子数成正比。如果光的频率高于阈值频率，每个光子都有足够的能量将电子击出。
``````

As the intensity increases, more photons hit the surface, leading to the emission of more photoelectrons. Consequently, the photoelectric current, which is proportional to the number of emitted electrons, increases with the intensity of the incident light. However, the kinetic energy of the emitted electrons remains the same and is determined by the energy of the individual photons, not the intensity of the light.


``````{admonition} 中文翻译
:class: dropdown

随着强度增加，更多光子击中表面，导致发射出更多光电子。 consequently，光电流（与发射电子数量成正比）随入射光的强度增加而增加。然而，发射出的电子的动能保持不变，由单个光子的能量决定，而非光的强度。
``````
:::

#### Problem 4: Which metal is it?

Light of wavelength 300 nm shines on an unknown metal, and the fastest photoelectrons are stopped by a reverse voltage of 1.85 V (so $KE_{max} = 1.85$ eV). Find the work function and identify the metal from this list: cesium 2.14 eV, sodium 2.28 eV, zinc 4.33 eV, copper 4.70 eV. What is the longest wavelength that still ejects electrons from it?


``````{admonition} 中文翻译
:class: dropdown

波长 300 nm 的光照射在一个未知金属上，最快的光电子被反向电压 1.85 V（所以 $KE_{max} = 1.85$ eV）停止。求功函数并从以下列表中识别该金属：铯 2.14 eV，钠 2.28 eV，锌 4.33 eV，铜 4.70 eV。还有什么是仍能从它中射出电子的最长波长？
``````

#### Problem 5: From photons to current

A 2.0 mW beam of 400 nm light falls on a potassium surface (work function 2.30 eV). (a) How many photons hit the surface per second? (b) If one photon in twenty ejects an electron, what current flows? (c) How does the answer to (b) change if the intensity doubles? And if the wavelength is halved at the same power?


``````{admonition} 中文翻译
:class: dropdown

一束功率为 2.0 mW、波长为 400 nm 的光束照射在钾表面（功函 2.30 eV）上。 (a) 每秒有多少光子撞击表面？ (b) 如果每 20 个光子中有 1 个射出电子，流过的电流是多少？ (c) 如果光强加倍，对 (b) 的答案有何变化？ 如果在相同功率下波长减半，又会怎样？
``````

#### Problem 6: Visible light and cesium

Cesium has the lowest work function of the common metals, 2.14 eV. Find its threshold wavelength. Which colors of visible light can eject electrons from cesium and which cannot? Suggest why cesium-coated cathodes were the material of choice for early photocells and night-vision tubes.


``````{admonition} 中文翻译
:class: dropdown

碱金属中铯的工作函数最低，为2.14 eV。求其阈波长。可见光中哪些颜色的光能射出电子，哪些不能？建议为什么碱化铯被用作早期光电池和夜视管的材料。
``````

#### Problem 7: The missing time delay

In the wave picture an electron would have to soak up energy gradually from the light wave. For a very dim source of intensity $10^{-10}$ W/m$^2$, estimate how long an atom of cross-sectional area $10^{-20}$ m$^2$ would need to collect the 2 eV required to escape. Experimentally, photoelectrons appear within nanoseconds of switching on the light, however dim. What does this tell you about how light delivers its energy?

``````{admonition} 中文翻译
:class: dropdown

在波动图像中，电子必须逐渐从光波中汲取能量。对于光强为 $10^{-10}$ W/m$^2$ 的非常微弱的光源，估计一个横截面积为 $10^{-20}$ m$^2$ 的原子需要多长时间才能积聚逃逸所需的 2 eV 能量。然而，无论光多么微弱，光电子在开启光的纳秒级时间内均出现。这说明了光如何传递能量？
``````

