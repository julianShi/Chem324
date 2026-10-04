---
kernelspec:
  name: python3
  display_name: Python 3
---

# Molecular Vibrations

:::{note} **What you need to know**

- **Quantization of vibrations in molecules.** Vibrational degrees of freedom are quantized in molecules. This has implications for infrared and Raman spectroscopies. 
- **Existence of selection rules.** Not all vibrational transitions are observed. Quantum mechanics predicts that for a transition to occur the transition probability needs to be non-zero, which is quantified via the transition dipole moment.  
- **Effects of anharmonicity.** The harmonic oscillator approximation captures the dominant transition frequency but is not fully accurate, because the harmonic shape of the potential describes only the vicinity of the potential energy minimum and becomes less accurate for excited vibrational states of molecules. 


``````{admonition} 中文翻译
:class: dropdown

- **分子振动的量子化.** 分子中的振动自由度是量子化的。这对红外和拉曼光谱学有影响。
- **选则规则的存在。** 并非所有振动跃迁都被观测到。量子力学预测，对于跃迁发生，跃迁概率需要非零，这通过跃迁偶极矩来量化。
- **谐近似的影响。** 谐振子近似捕获了主跃迁频率，但并非完全准确，因为势能的谐振子形状仅描述势能最小值附近的情况，对于分子激发的振动态的精度会降低。
``````
:::

### Vibrational Spectroscopy with Harmonic Oscillator

:::{important} **Harmonic oscillator and spectroscopic units**

$${\tilde{E}_v = \frac{E_v}{hc} = \tilde{\nu}\left(v + \frac{1}{2}\right)}$$

$${\Delta \tilde{ E_v} } = \tilde{ E}_{v+1} - \tilde{ E}_{v}  = \tilde{\nu}$$

$$\tilde{\nu} = \frac{1}{2\pi c}\sqrt{\frac{k}{\mu}}$$

- **The vibrational quantum number:**  $v=0,1,2,...$ 
- **Reduced mass of the diatomic molecule:** $\mu$. 
- **Spring constant $k$:** measures strength of bonds
- **$\tilde{\nu}$ frequency of photon (equal to freq of mol vibrations) $cm^{-1}$ units.**


``````{admonition} 中文翻译
:class: dropdown

- **振动量子数:**  $v=0,1,2,...$
- **二原子分子的归一化质量:** $\mu$。
- **Spring 常数 $k$:** 衡量键的强度
- **$\tilde{\nu}$ 光子频率（等于分子振动频率）单位 $cm^{-1}$。**
``````
:::

- Note that symbols $v$ (quantum number) and $\nu$ (vibrational frequency) look very similar but have different meanings!  
- A typical value for vibrational frequency would be around  $500 - 4000cm^{-1}$. Small values are associated with weak bonds, whereas strong bonds have larger vibrational frequencies.


``````{admonition} 中文翻译
:class: dropdown

- 注意符号 $v$（量子数）和 $\nu$（振动频率）看起来非常相似但含义不同！
- 典型的振动频率值约为 $500 - 4000cm^{-1}$。小值对应弱键，而强键具有较大的振动频率。
``````

:::{note} **Example**

A strong absorption of infrared radiation is observed for $^1H^{35}Cl$ at $2991 cm^{-1}$.


``````{admonition} 中文翻译
:class: dropdown

观察到 $^1H^{35}Cl$ 在 $2991 cm^{-1}$ 处有强红外吸收。
``````

- Calculate the force constant k for this molecule
- By what factor do you expect this frequency to shift if deuterium is substituted for hydrogen in this molecule? The force constant is unaffected by this substitution.


``````{admonition} 中文翻译
:class: dropdown

- 计算该分子的力常数 k
- 如果在该分子中将氘代替氢，你预期该频率会按什么因子偏移？此类置换不影响力常数。
``````
:::

:::{admonition} **Solution**
:class: dropdown solution

- **part a**

$$\tilde{\nu} = \frac{1}{2\pi c}\sqrt{\frac{k}{\mu}}$$


$$k = \Big(2\pi c \tilde{\nu}\Big)^2\cdot \mu=516 N \cdot m^{-1}$$

- **part b**

$$\frac{\nu_{DCl}}{\nu_{HCL}}=\Big(\frac{\mu_{HCl}}{\mu_{DCL}}\Big)^{1/2}=0.717$$
:::



### Beyond the Harmonic Approximation

- The harmonic potential is an approximation that does not allow for molecular dissociation, making it an unrealistic model when far from equilibrium geometry. The harmonic potential is expressed as:


``````{admonition} 中文翻译
:class: dropdown

- 谐势近似不允许分子解离，远离平衡几何构型时是不现实的模型。谐势表示为：
``````

  $$E(R) = \frac{1}{2}k(R - R_e)^2$$

  Here, $k$ is the *force constant*, $R_e$ is the *equilibrium bond length*, and $R$ is the distance between the two atoms. 


``````{admonition} 中文翻译
:class: dropdown

这里，$k$ 是*力常数*，$R_e$ 是*平衡键长*，而 $R$ 是两个原子之间的距离。
``````

- The true potential energy curve, however, can be derived from theoretical calculations or, to some extent, from spectroscopic experiments. Unlike the harmonic potential, this curve has a complex shape, making it challenging to solve the nuclear Schrödinger equation exactly. 

- The harmonic approximation can be understood as a *Taylor series expansion* around $R_e$:


``````{admonition} 中文翻译
:class: dropdown

- 然而，真实的势能曲线可以从理论计算或一定程度上从光谱实验中推导出来。与谐振子势不同，这条曲线形状复杂，使得精确求解核 Schrödinger 方程变得具有挑战性。
- 谐波近似可以理解为在 $R_e$ 处的 *泰勒级数展开*：
``````

  $$E(R) = E(R_e) + \left(\frac{dE}{dR}\right)_{R = R_e}(R - R_e) + \frac{1}{2}\left(\frac{d^2E}{dR^2}\right)_{R = R_e}(R - R_e)^2 + \dots$$

:::{figure} ./images/De.png
:label: fig-molecular-vibrations-1
:alt: Comparison of Harmonic and Morse Potentials
:width: 300px

Harmonic and Morse potentials compared, distinguishing the equilibrium dissociation energy $D_e$ from the spectroscopic dissociation energy $D_0$.


``````{admonition} 中文翻译
:class: dropdown

谐振子势与莫尔斯势的对比，区分平衡解离能 $D_e$ 与光谱解离能 $D_0$。
``````
:::

### Morse potential and dissociation energy 

- The Morse potential provides a more accurate description of molecular vibrations and predicts dissociation as well as changing spacing between energy levels. 


``````{admonition} 中文翻译
:class: dropdown

- 莫尔斯势能为分子振动提供了更准确的描述，并能预测解离以及能级间距的变化。
``````

$$V(R)=D_e(1-e^{-a(R-R_e)^2})$$

- $D_e$ is measured from the bottom of the potential to the dissociation limit whereas $D_0$ is measured from the lowest vibrational level to the dissociation limit. 


``````{admonition} 中文翻译
:class: dropdown

- $D_e$ 从势能底部测量到解离极限，而 $D_0$ 从最低振动水平测量到解离极限。
``````

$$D_0 = D_e-\frac{1}{2}h\nu$$

```{code-cell} python
:tags: [hide-input]
import numpy as np
from scipy.constants import h, hbar, c, u
from scipy.special import genlaguerre, gamma, factorial
from matplotlib import pyplot as plt

# Factor for conversion from cm-1 to J
FAC = 100 * h * c

class Morse:
    """A class representing the Morse oscillator model of a diatomic."""

    def __init__(self, mA, mB, we, wexe, re, Te):
        """Initialize the Morse model for a diatomic molecule.

        mA, mB are the atom masses (atomic mass units).
        we, wexe are the Morse parameters (cm-1).
        re is the equilibrium bond length (m).
        Te is the electronic energy (minimum of the potential well; origin
            of the vibrational state energies).

        """

        self.mA, self.mB = mA, mB
        self.mu = mA*mB/(mA+mB) * u
        self.we, self.wexe = we, wexe
        self.re = re
        self.Te = Te

        self.De = we**2 / 4 / wexe * FAC
        self.ke = (2 * np.pi * c * 100 * we)**2 * self.mu
        #  Morse parameters, a and lambda.
        self.a = self.calc_a()
        self.lam = np.sqrt(2 * self.mu * self.De) / self.a / hbar
        # Maximum vibrational quantum number.
        self.vmax = int(np.floor(self.lam - 0.5))

        self.make_rgrid()
        self.V = self.Vmorse(self.r)

    def make_rgrid(self, n=1000, rmin=None, rmax=None, retstep=False):
        """Make a suitable grid of internuclear separations."""

        self.rmin, self.rmax = rmin, rmax
        if rmin is None:
            # minimum r where V(r)=De on repulsive edge
            self.rmin = self.re - np.log(2) / self.a
        if rmax is None:
            # maximum r where V(r)=f.De
            f = 0.999
            self.rmax = self.re - np.log(1-f)/self.a
        self.r, self.dr = np.linspace(self.rmin, self.rmax, n,
                                      retstep=True)
        if retstep:
            return self.r, self.dr
        return self.r

    def calc_a(self):
        """Calculate the Morse parameter, a.

        Returns the Morse parameter, a, from the equilibrium
        vibrational wavenumber, we in cm-1, and the dissociation
        energy, De in J.

        """

        return (self.we * np.sqrt(2 * self.mu/self.De) * np.pi *
                c * 100)

    def Vmorse(self, r):
        """Calculate the Morse potential, V(r).

        Returns the Morse potential at r (in m) for parameters De
        (in J), a (in m-1) and re (in m).

        """

        return self.De * (1 - np.exp(-self.a*(r - self.re)))**2

    def Emorse(self, v):
        """Calculate the energy of a Morse oscillator in state v.

        Returns the energy of a Morse oscillator parameterized by
        equilibrium vibrational frequency we and anharmonicity
        constant, wexe (both in cm-1).

        """
        vphalf = v + 0.5
        return (self.we * vphalf - self.wexe * vphalf**2) * FAC

    def calc_turning_pts(self, E):
        """Calculate the classical turning points at energy E.

        Returns rm and rp, the classical turning points of the Morse
        oscillator at energy E (provided in J). rm < rp.

        """

        b = np.sqrt(E / self.De)
        return (self.re - np.log(1+b) / self.a,
                self.re - np.log(1-b) / self.a)

    def calc_psi(self, v, r=None, normed=True, psi_max=1):
        """Calculates the Morse oscillator wavefunction, psi_v.

        Returns the Morse oscillator wavefunction at vibrational
        quantum number v. The returned function is "normalized" to
        give peak value psi_max.

        """

        if r is None:
            r = self.r
        z = 2 * self.lam * np.exp(-self.a*(r - self.re))
        alpha = 2*(self.lam - v) - 1
        psi = (z**(self.lam-v-0.5) * np.exp(-z/2) *
               genlaguerre(v, alpha)(z))
        psi *= psi_max / np.max(psi)
        return psi

    def calc_psi_z(self, v, z):
        alpha = 2*(self.lam - v) - 1
        psi = (z**(self.lam-v-0.5) * np.exp(-z/2) *
               genlaguerre(v, alpha)(z))
        Nv = np.sqrt(factorial(v) * (2*self.lam - 2*v - 1) /
                     gamma(2*self.lam - v))
        return Nv * psi

    def plot_V(self, ax, **kwargs):
        """Plot the Morse potential on Axes ax."""

        ax.plot(self.r*1.e10, self.V / FAC + self.Te, **kwargs)

    def get_vmax(self):
        """Return the maximum vibrational quantum number."""

        return int(self.we / 2 / self.wexe - 0.5)

    def draw_Elines(self, vlist, ax, **kwargs):
        """Draw lines on Axes ax representing the energy level(s) in vlist."""

        if isinstance(vlist, int):
            vlist = [vlist]
        for v in vlist:
            E = self.Emorse(v)
            rm, rp = self.calc_turning_pts(E)
            ax.hlines(E / FAC + self.Te, rm*1.e10, rp*1e10, **kwargs)

    def label_levels(self, vlist, ax):
        if isinstance(vlist, int):
            vlist = [vlist]

        for v in vlist:
            E = self.Emorse(v)
            rm, rp = self.calc_turning_pts(E)
            ax.text(s=r'$v={}$'.format(v), x=rp*1e10 + 0.6,
                    y=E / FAC + self.Te, va='center')

    def plot_psi(self, vlist, ax, r_plot=None, scaling=1, **kwargs):
        """Plot the Morse wavefunction(s) in vlist on Axes ax."""
        if isinstance(vlist, int):
            vlist = [vlist]
        for v in vlist:
            E = self.Emorse(v)
            if r_plot is None:
                rm, rp = self.calc_turning_pts(E)
                x = self.r[self.r<rp*1.2]
            else:
                x = r_plot
            psi = self.calc_psi(v, r=x, psi_max=self.we/2)
            psi_plot = psi*scaling + self.Emorse(v)/FAC + self.Te
            ax.plot(x*1.e10, psi_plot, **kwargs)


### Plot for (1H)(35Cl)
mA, mB = 1., 35.
X_re = 1.27455e-10
X_Te = 0
X_we, X_wexe = 2990.945, 52.818595

X = Morse(mA, mB, X_we, X_wexe, X_re, X_Te)
X.make_rgrid()
X.V = X.Vmorse(X.r)

fig, ax = plt.subplots(figsize=(11, 11))
X.plot_V(ax, color='k')

X.draw_Elines(range(X.vmax), ax)
X.draw_Elines(X.get_vmax(), ax, linestyles='--', linewidths=1)
X.plot_psi([0, 5, 10, 20], ax, scaling=2, color='maroon')
X.label_levels([0, 5, 10, 20], ax)

ax.set_xlabel(r'$r[\AA]$')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
```

### Anharmonic oscillator

We can account for the deviation from harmonic behavior by adding higher-order polynomial terms to $\tilde{E}_v$. The addition of new terms allows for eventual dissociation to happen when a molecule is excited to high vibrational energy states. 


``````{admonition} 中文翻译
:class: dropdown

我们可以通过在 $\tilde{E}_v$ 中加入高阶多项式项来解释偏离谐振子行为的情况。新项的加入允许在分子被激发到高振动能态时最终解离。
``````

:::{important} **Anharmonic oscillator**

$${\tilde{E}_v = \tilde{\nu}_e(v + \frac{1}{2}) - \tilde{\nu}_ex_e(v + \frac{1}{2})^2 + ...}$$

$${\tilde{\nu}_{v\rightarrow v+1} = \tilde{E}_{v+1} - \tilde{E}_v = \tilde{\nu}_e[1- 2x_e  (v+1)] }$$

- $\tilde{\nu}_e$ is the vibrational wavenumber
-  $x_e$ and $y_e$ are anharmonicity constants
- $v$ is the vibrational quantum number. Usually the third term is ignored and we can write the vibrational transition frequencies as ($v\rightarrow v+1$):


``````{admonition} 中文翻译
:class: dropdown

- $\tilde{\nu}_e$ is the vibrational wavenumber
- $x_e$ 和 $y_e$ 是非调和常数。
- $v$ 是振动量子数。通常忽略第三项，我们可以将振动跃迁频率写为（$v\rightarrow v+1$）：
``````
:::

### Overtone transitions


:::{figure} ./images/vib_modes.jpeg
:label: fig-molecular-vibrations-2
:alt: DeD0
:width: 300px

Illustration of overtone transitions
:::


- The higher order terms are small but they give rise to overtone transitions with $\Delta v = \pm 2, \pm 3, ...$ with rapidly decreasing intensities.


``````{admonition} 中文翻译
:class: dropdown

- 高阶项很小，但它们导致了 $\Delta v = \pm 2, \pm 3, ...$ 的泛音跃迁，其强度迅速减小。
``````

$${\tilde{\nu}_{0\rightarrow v}  = \tilde{E}_{v} - \tilde{E}_0 = \tilde{\nu}_e \cdot v - \tilde{\nu}_ex_e \cdot v (v+1)}$$

:::{note} **Example**

Given  $\tilde{\nu}=536 cm^{-1}$ and $x_e\tilde{\nu}=3.4 cm^{-1}$ for the $^{23}Na^{19}F$ molecule, calculate the frequencies of the first two overtones.


``````{admonition} 中文翻译
:class: dropdown

已知 $^{23}Na^{19}F$ 分子的 $\tilde{\nu}=536 cm^{-1}$ 和 $x_e\tilde{\nu}=3.4 cm^{-1}$，计算前两个泛音的频率。
``````
:::

:::{note} **Solution**
:class: dropdown

We make use of the equation ${\tilde{\nu}_{0\rightarrow v} = \tilde{\nu}_e \cdot v - 2\tilde{\nu}_ex_e v (v+1)}$ to compute transitions to levels 1 (fundamental), 2 (first overtone) and 3 (second overtone)


``````{admonition} 中文翻译
:class: dropdown

我们使用方程 ${\tilde{\nu}_{0\rightarrow v} = \tilde{\nu}_e \cdot v - 2\tilde{\nu}_ex_e v (v+1)}$ 来计算到 1 级（基态）、2 级（第一谐波）和 3 级（第二谐波）的跃迁
``````

- $\tilde{\nu}_{0\rightarrow 1} = 1\tilde{\nu}_e  - 2\tilde{\nu}_ex_e= 1\cdot536-2\cdot3.4=529 cm^{-1}$
- ${\tilde{\nu}_{0\rightarrow 2} = 2\tilde{\nu}_e  - 6\tilde{\nu}_ex_e= 2\cdot536-6\cdot3.4}=1059 cm^{-1}$
- ${\tilde{\nu}_{0\rightarrow 3} = 3\tilde{\nu}_e  - 12\tilde{\nu}_ex_e= 3\cdot536-12\cdot3.4}=1567 cm^{-1}$


``````{admonition} 中文翻译
:class: dropdown

- $\tilde{\nu}_{0\rightarrow 1} = 1\tilde{\nu}_e  - 2\tilde{\nu}_ex_e= 1\cdot536-2\cdot3.4=529 cm^{-1}$
- ${\tilde{\nu}_{0\rightarrow 2} = 2\tilde{\nu}_e  - 6\tilde{\nu}_ex_e= 2\cdot536-6\cdot3.4}=1059 cm^{-1}$
- ${\tilde{\nu}_{0\rightarrow 3} = 3\tilde{\nu}_e  - 12\tilde{\nu}_ex_e= 3\cdot536-12\cdot3.4}=1567 cm^{-1}$
``````
:::

:::{admonition} **Population of vibrational states**
:class: info, dropdown

- Out of all possible vibrational states which states do molecules occupy at room temperature? For harmonic oscillator, the Boltzmann distribution  gives the statistical weight for the $v$ level:


``````{admonition} 中文翻译
:class: dropdown

- 所有可能的振动态中，分子在室温下占据哪些态？对于谐振子，玻尔兹曼分布给出 $v$ 级的统计权重：
``````

$${f_v = \frac{e^{-(v + 1/2)h\nu/(k_BT)}}{\sum\limits_{v=0}^\infty e^{-(v+1/2)h\nu/(k_BT)}}}
{= \frac{e^{-vh\nu/(k_BT)}}{\sum\limits_{v=0}^\infty e^{-vh\nu/(k_BT)}}}$$

- Note that the degeneracy factor is identically one because there is no degeneracy in one dimensional harmonic oscillator. To proceed, we recall geometric series:


``````{admonition} 中文翻译
:class: dropdown

- 注意简并因子恒等于 1，因为一维谐振子没有简并。继续推导，我们回顾等比数列求和公式：
``````

$${\sum\limits_{v=0}^\infty x^v = \frac{1}{1 - x}\textnormal{ with }x < 1}$$


$${\sum\limits_{v=0}^\infty e^{-vh\nu/(k_BT)} = \frac{1}{1 - e^{-h\nu/(k_BT)}}}$$


$${f_v = \left(1 - e^{-h\nu/(k_BT)}\right)e^{-vh\nu/(k_BT)}}$$

- For example, for $H^{35}Cl$ the thermal population of the first vibrational level $v = 1$ is very small about $9\times$ $10^{-7}$.
-  **This is why generally the excited vibrational levels do not contribute to the (IR) spectrum.**


``````{admonition} 中文翻译
:class: dropdown

- 例如，对于 $H^{35}Cl$，第一振动能级 $v = 1$ 的热布居数非常小，约为 $9\times$ $10^{-7}$。
- **这也是通常激发振动能级不参与（红外）光谱的原因。**
``````

:::

### Vibrational modes of molecules

- A molecule has translational and rotational motion as a whole, while each atom has its own motion. The vibrational modes can be IR or Raman active. For a mode to be observed in the IR spectrum, a change must occur in the permanent dipole (i.e. not homonuclear diatomic molecules). Homonuclear diatomic molecules are observed in the Raman spectrum but not in the IR spectrum. This is because such molecules have one band and no permanent dipole, and therefore a single vibration. Examples would be $O_2$ or $N_2$.


``````{admonition} 中文翻译
:class: dropdown

- 分子整体具有平动和转动运动，而每个原子都有自己的运动。振动模式可以是红外活性的或拉曼活性的。要在红外光谱中观察到某个模式，必须发生永久偶极矩的变化（即双原子同核分子除外）。双原子同核分子可以在拉曼光谱中观察到，但不能在红外光谱中观察到。这是因为此类分子只有一个带，且没有永久偶极矩，因此只有一个振动模式。例如 $O_2$ 或 $N_2$。
``````


:::{figure} images/CO2_modes.jpg
:label: fig-molecular-vibrations-3
:alt: co2-mode
:width: 300px

Normal modes of $CO_2$ with associated vibrational frequencies


``````{admonition} 中文翻译
:class: dropdown

$CO_2$ 的正常模及其相关的振动频率
``````
:::


- However, heteronuclear diatomic molecules (e.g. CN) do absorb in the IR spectrum. Polyatomic molecules undergo more complex vibrations that can be summed or resolved into normal modes of vibration. For polyatomic molecules, the normal modes of vibration are: asymmetric, symmetric, wagging, twisting, scissoring, and rocking.


``````{admonition} 中文翻译
:class: dropdown

- 然而，异核二原子分子（如 CN）在红外光谱中有吸收。多原子分子经历更复杂的振动，可以求和或分解为正常振动模式。对于多原子分子，正常振动模式包括：非对称、对称、摆动、扭转、剪切和摇摆。
``````

:::{figure} images/watervib.gif
:label: fig-molecular-vibrations-4
:alt: amide-ir
:width: 400px

Vibrational modes of water
:::

:::{figure} images/protein.gif
:label: fig-molecular-vibrations-5
:alt: amide-ir
:width: 300px

Slowest vibrational mode in a protein, linked to its catalytic function.


``````{admonition} 中文翻译
:class: dropdown

蛋白质中最慢的振动模式，与其催化功能相关。
``````
:::

:::{important} **Vibrational degrees of freedom in molecules**

- **Linear** Molecules with N atoms:

$$N_{modes} = 3N−5$$
 
- **Non-linear** molecules with N atoms

$$N_{modes} = 3N−6$$

:::

### Selection rules and Transition Dipole Moment

- Selection rules in spectroscopy are fundamental principles that dictate whether a transition is allowed or forbidden during the absorption or emission of electromagnetic radiation, such as in infrared (IR) or Raman spectroscopy. The origins of these rules lie in the fact that a photon can induce coupling between the initial and final quantum states only under specific conditions. 

- In spectroscopy, **allowed transitions** are those with a **non-zero transition dipole moment** between the initial and final states.

- Mathematically, the molecular dipole moment can be expanded around its equilibrium geometry $R_e$. Here we will use the displacement from equilibrium geometry $x = R - R_e$ for convenience,


``````{admonition} 中文翻译
:class: dropdown

- 光谱中的选取规则是基本原则，决定在吸收或发射电磁辐射（如红外 (IR) 或 Raman 光谱）过程中跃迁是被允许还是被禁用。这些规则的由来在于，光子只能在特定条件下诱导初态和末态之间的耦合。
- 在光谱学中，**允许跃迁** 是指初态和末态之间具有**非零跃迁偶极矩**的跃迁。
- 在数学上，分子偶极矩可以围绕其平衡几何结构 $R_e$ 展开。此处我们将平衡几何结构的位移 $x = R - R_e$ 作为便利变量，
``````

$$
\mu_z(x) = \mu_e + \left( \frac{\partial \mu}{\partial x} \right)_{R_e} x+
\cdot \frac{1}{2} \left( \frac{\partial^2 \mu}{\partial x^2} \right)_{R_e} x^2 + \dots
  $$

- the transition dipole matrix element between vibrational states $|v\rangle$ and $|v'\rangle$ becomes:


``````{admonition} 中文翻译
:class: dropdown

- 振动态 $|v\rangle$ 与 $|v'\rangle$ 之间的跃迁偶极矩阵元变为：
``````

$$
\langle v | \mu_z | v' \rangle = \mu_e \langle v | v' \rangle + \cdot \left( \frac{\partial \mu}{\partial x} \right)_{R_e} \langle v | x | v' \rangle
+  \frac{1}{2} \left( \frac{\partial^2 \mu}{\partial x^2} \right)_{R_e} \langle v | x^2 | v' \rangle
+ \dots
  $$

- Each term corresponds to an **expectation value** of powers of $x$. We can interpret these terms as follows:

  * **First term:** $\mu_e \langle v | v' \rangle = 0 $ for $v \neq v'$ because the vibrational wavefunctions are orthogonal.
  * **Second term:** The term involving $\langle v | x | v' \rangle$ can be nonzero **only if** the dipole moment changes with internuclear distance, i.e., $\frac{\partial \mu}{\partial x} \neq 0$.
  * **Higher-order terms:** Usually small, but can contribute to overtones ($\Delta v = 2, 3, \dots $) when $\mu(R)$  is strongly anharmonic.


``````{admonition} 中文翻译
:class: dropdown

- 每一项对应于 $x$ 的幂的**期望值**。我们可以这样解释这些项：
- **第一项：** $\mu_e \langle v | v' \rangle = 0 $ 对于 $v \neq v'$ 成立，因为振动波函数是正交的。
- **高阶项：** 通常很小，但当 $\mu(R)$ 强烈非谐时，可对泛音（$\Delta v = 2, 3, \dots $）有贡献。
``````

:::{important} **Selection Rules for harmonic oscillator**


- A **vibrational transition is allowed** only if the molecular dipole moment **changes with the bond length**:


``````{admonition} 中文翻译
:class: dropdown

- **振动跃迁允许**仅当分子偶极矩**随键长变化**时：
``````

$$
\left( \frac{\partial \mu}{\partial x} \right)_{R_e} \neq 0.
$$

$$P_{v\rightarrow v'} \sim \langle v | x | v' \rangle $$

$$\Delta v = \pm 1$$

- $P_{v\rightarrow v'}$ probability of making transition from $v$ to $v'$ vibrational energy level 


``````{admonition} 中文翻译
:class: dropdown

- $P_{v\rightarrow v'}$ 从振动能级 $v$ 跃迁到 $v'$ 的概率
``````

:::


:::{figure} images/selection_rule.jpg
:label: fig-molecular-vibrations-6
:alt: amide-ir
:width: 400px

2D IR spectroscopy probing a protein by detecting amide $C=O$ vibrations in different parts of the molecule.


``````{admonition} 中文翻译
:class: dropdown

二维红外光谱通过检测分子不同部分的酰胺 $C=O$ 振动来探测蛋白质。
``````
:::

- All homonuclear diatomic molecules (e.g., $H_2$, $O_2$, etc.) have zero dipole moment, which cannot change as a function of $R$. Hence these molecules do not show vibrational spectra. 
- In general, all molecules that have a dipole moment have vibrational spectra, as a change in $R$ also results in a change of dipole moment. We still have the integral present in the second term. 
- For the harmonic oscillator approximation, this integral is zero unless $v'' = v'\pm 1$. This provides an additional selection rule, which says that the vibrational quantum number may either decrease or increase by one.


``````{admonition} 中文翻译
:class: dropdown

- 所有同核二原子分子 (如 $H_2$，$O_2$ 等) 具有零偶极矩，该矩随 $R$ 的变化不能改变。因此这些分子不显示振动谱。
- 一般来说，所有具有偶极矩的分子都有振动光谱，因为 $R$ 的变化也会导致偶极矩的变化。我们仍然在第二项中保留积分。
- 对于谐振子近似，除非 $v'' = v'\pm 1$，否则该积分为零。这提供了一个额外的选取规则，即振动量子数可以减少或增加一个。
``````

### IR spectra

:::{figure} images/IR-sp.png
:label: fig-molecular-vibrations-7
:alt: ir spectra
:width: 500px

IR spectral frequencies arising from the vibrations of different bonds in organic molecules.


``````{admonition} 中文翻译
:class: dropdown

有机分子中不同键的振动产生的 IR 光谱频率。
``````
:::


:::{figure} images/amide_modes.png
:label: fig-molecular-vibrations-8
:alt: amide-ir
:width: 500px

2D IR spectroscopy probing a protein by detecting amide $C=O$ vibrations in different parts of the molecule.


``````{admonition} 中文翻译
:class: dropdown

二维红外光谱通过检测分子不同部分的酰胺 $C=O$ 振动来探测蛋白质。
``````
:::
