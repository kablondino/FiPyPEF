# Full Model Notes: 9 May 2018

\small\begin{align}
	&\text{Co-dimension 2 cusp bifurcation:} ~~~~ \dot{x} \,=\, a + bx - x^3 \\
	&\text{FitzHugh-Nagumo bifurcation:} ~~~~ \dot{x} \,=\, a - bx - x^3 + cy~,
		~~~~ \dot{y} \,=\, -x - y \\
	&\text{Plasma Dispersion Function:} ~~ X(\zeta) \,=\, i \sqrt{\pi}\,w(\zeta)
		\,=\, i \sqrt{\pi} \, e^{-\zeta^2} \text{erfc}(-i \zeta)
		\,=\, \frac{1}{\sqrt{\pi}} \int_{-\infty}^{+\infty}
		\frac{e^{-t^2}}{t - \zeta} \, \text{d}t~,~~
		\zeta \,\equiv\, \frac{\omega/k}{v_T} \\
	&\text{Approx. SI Units at Edge:} ~~~~ n \,\approx\, 0.5\times 10^{19}~\text{m}^{-3}~,
		~~ T \,\approx\, 100~e\text{V}~,~~ v_{T_i} \,\approx\, 10^5~\text{m}/\text{s}~,
		~~ \rho_{\theta i} \,\approx\, 10^{-4}~\text{m}
\end{align}\normalsize

### Plasma Parameters
All temperatures are in eV.
\small\begin{align}
	\epsilon \,&=\, \frac{a_m}{R}~,~~~ q \,=\,
		\frac{\epsilon \, B_\phi}{B_\theta}~,~~~ v_{T_j} \,=\,
		\sqrt{\frac{2 \, e \, T}{m_j}}~,~~~ \rho_{\theta j} \,=\,
		\frac{m_j \, v_{T_j}}{e \, B_\theta} \,=\,
		\sqrt{\frac{2 \, m_j \, T}{e^2 \, B_\theta^2}} \\
	 B_\theta \,&=\, \frac{\mu_0 \, I_\phi}{2 \pi \, a_m}~,~~~ \omega_t \,=\,
		\frac{v_{T_i}}{q\,R}~,~~~ \omega_{bj} \,=\,
		\frac{\epsilon^{3/2} \, v_{T_j}}{q \, R}~,~~~ w_{bi} \,=\,
		\rho_{\theta i} \, \sqrt{\epsilon} \\
	\nu_{ei} \,&=\, 1.33\times 10^5 \frac{n_{20}}{(T_\text{keV})^{3/2}}
		\,=\, 4.2058\times 10^{-5} \frac{n}{(T_\text{eV})^{3/2}}~,~~~
		\nu_{ii} \,=\, 1.2\, \nu_{ei} \, \sqrt{\frac{m_e}{m_i}}~,~~~
		\nu_{*j} \,=\, \frac{\nu_{ij}}{\omega_{bj}} \\
	\langle \sigma_\text{cx} v \rangle \,&=\, 10^{-14} \sqrt[3]{100 \, T}
		\,=\, 1.985\times 10^{-14} \sqrt{T}~,~~~
		\text{Depricated:}~\nu_{in_0} \,=\, a_{in_0} \, \omega_{bi}~,~~~
		\nu_\text{eff} \,=\, \nu_{ii} + \nu_{in_0} \\
		\nonumber &~~~~~~\text{Itoh 1989} ~~~~~~~~~ \text{Rozhansky 2001} \\
	&\text{Non-formal:} ~~ n_0 \,=\, \frac{n_0(0)}
		{\left(1 + \exp\left[k(x - d)\right]\right)}~,~~~
		n_0(0) \,=\, \frac{\theta \, \Gamma_c}{v_{T_i}} ~~ \text{for} ~~
		0 < \theta \leq 1
\end{align}\normalsize

<!--- OLD CHARGE EXCHANGE REACTION and IONIZATION RATE
	\langle \sigma_\text{cx} v \rangle \,&=\, \frac{C_\text{cx}}{\sqrt{T}} \,
		\exp\left(-\frac{E_0}{T}\right)~,~~~
		\langle \sigma_\text{ion} v \rangle \,=\, \frac{C_\text{ion}}{\sqrt{m_i}} \,
		\exp\left(-\frac{E_0}{T}\right) \\-->

### Model Forms
Domain with boundary:
\small\begin{align}
	\Omega \,=\, \left\{x, t \,\in\, \mathbb{R}^2 \,|\, (0 \leq x \leq L)
		~\text{and}~ (t \geq 0)\right\}, ~~~~ \delta\Omega \,=\,
		\{x, t \,\in\, \Omega \,|\, x = 0 ~\text{and}~ x = L \}
\end{align}\normalsize

Electric field normalization, energy definition, diffusivity relation, dielectric constant, and viscosity:
\small\begin{align}
	Z \,\equiv\, \frac{e \, \rho_\theta \, E_r}{T}~, ~~~~
		U \,=\, \frac{n\,T}{\gamma - 1}~, ~~~~
		\chi \,=\, \frac{D}{\zeta(\gamma - 1)}~, ~~~~
		\epsilon \,=\, \frac{B_\theta^2}{B^2 \nu_i}~, ~~~~
		\mu \approx m_i \, n \, v_{T_i} \, \lambda
\end{align}\normalsize

The following form of the model references particle and heat fluxes, $\Gamma$ and $q$:
\small\begin{align}
	\frac{\partial n}{\partial t} \,&=\, -\frac{\partial \Gamma}{\partial x}~,~~&
	\frac{\partial U}{\partial t} \,&=\, -\frac{\partial q}{\partial x}~,~~&
	\epsilon \frac{\partial Z}{\partial t} \,&=\,
		\mu \frac{\partial^2 Z}{\partial x^2} + \frac{c_n \, T}{n^2}
		\frac{\partial n}{\partial x} +
		\frac{c_T}{n} \frac{\partial T}{\partial x} + G(Z) \\
	\Gamma \,&=\, -D \, \frac{\partial n}{\partial x}~,~~&
	q \,&=\, -\chi \, n \frac{\partial T}{\partial x} +
		\frac{\Gamma\,T}{\gamma - 1}~,~~&
	&G \,=\, a + b(Z - Z_S) + c(Z - Z_S)^3
\end{align}\normalsize

Reducing down to equations of only $n$ and $T$ (of 2 possible forms): $\dfrac{\partial n}{\partial t} \,=\, \dfrac{\partial}{\partial x}\left[D \, \dfrac{\partial n}{\partial x}\right]$
\small\begin{align}
	\frac{\partial(n\,T)}{\partial t} \,&=\,
		\frac{\partial}{\partial x}\left[\frac{D\,n}{\zeta} \,
		\frac{\partial T}{\partial x}\right] \,+\,
		\frac{\partial}{\partial x}\left[D\,T \,
		\frac{\partial n}{\partial x}\right]~, ~~~~
	  \frac{\partial T}{\partial t} \,=\, \frac{\partial }{\partial x}
		\left[\frac{D}{\zeta} \, \frac{\partial T}{\partial x}\right] \,+\,
		\left(\frac{1}{\zeta} + 1\right) \frac{D}{n} \,
		\frac{\partial n}{\partial x} \, \frac{\partial T}{\partial x}
\end{align}\normalsize

<!---
Staps reduced the model to the following vector form:
\small\begin{align}
	\dfrac{\partial}{\partial t} \mathbf{v}(x,t) \,=\, \dfrac{\partial}{\partial x} F&\left(x, t, \mathbf{v}, \dfrac{\partial\mathbf{v}}{\partial x}\right) \,+\, S\left(x, t, \mathbf{v}, \dfrac{\partial\mathbf{v}}{\partial x}\right) \\
\mathbf{v} \,=\,\begin{bmatrix} n \\[1ex] T \\[1ex] Z \end{bmatrix}~,~~~~
\mathbf{F} \,=\, &\begin{bmatrix}
			D\,\, n^\prime \\[1ex]
			\dfrac{D}{\zeta}\,\, T^\prime \\[2ex]
			\dfrac{\mu D}{\epsilon}\,\, Z^\prime
			\end{bmatrix}~,~~~~
\mathbf{S} \,=\, \begin{bmatrix}
			0 \\[1ex]
			\left(\dfrac{\zeta + 1}{\zeta}\right) \dfrac{D}{n} \, n^\prime \, T^\prime \\[2ex]
			\dfrac{c_n T}{\epsilon n^2} \, n^\prime \,+\, \dfrac{c_T}{\epsilon n} \, T^\prime \,+\, \dfrac{G(Z)}{\epsilon}
			\end{bmatrix}~.
\end{align}\normalsize
-->

The diffusivity function $D(\mathcal{E})$ is given in a few forms:
\small\begin{align}
	D(Z) \,&=\, \frac{D_\text{max} + D_\text{min}}{2} +
		\frac{(D_\text{max} - D_\text{min})\tanh(Z)}{2} ~~~~~~ &\text{Zohm} \\
	D(Z^\prime) \,&=\, D_\text{min} \,+\, \frac{D_\text{max} - D_\text{min}}
		{1 + \alpha_\text{sup}(Z^\prime)^\beta}~,~~~ \beta \approx 2 ~~~~~~
		&\text{Staps} \\
	D(Z, Z^\prime) \,&=\, D_\text{min} + \frac{D_\text{max} - D_\text{min}}
		{1 + a_1\,Z^2 + a_2\,Z Z^\prime + a_3\left(Z^\prime\right)^2} ~~~~~~
		&\text{Flow-Shear}
\end{align}\normalsize

### Boundary Conditions, Initial Conditions, and Steady-State Solutions

Generalized versions for boundary conditions at the plasma edge ($x=0$):
\small\begin{align}
	n^\prime(0) \,=\, \frac{n}{\lambda_n}~,~~~~ T^\prime(0) \,=\,
		\frac{T}{\lambda_T}~,~~~~ Z^\prime(0) \,=\, \frac{Z}{\lambda_Z}~~~
		\text{or} ~~~ Z^\prime(0) \,=\, 0;
\end{align}\normalsize

...towards the core ($x=L$):
\small\begin{align}
	\Gamma(L) \,=\, \Gamma_c ~\longrightarrow~ n^\prime(L) \,=\,
		-\frac{\Gamma_c}{D}~; ~~~~
		q(L) \,=\, q_c ~\longrightarrow~ T^\prime(L) \,=\
		\frac{\zeta\left(T \Gamma_c - (\gamma - 1) q_c\right)}{n\,D}~; ~~~~
		Z^\prime(L) \,=\, 0
\end{align}\normalsize

<!---
For Matlab, the Neumann and Robin boundary conditions can be expressed in the form of
\small\begin{align}
	&p\left(x, t, \mathbf{v}\right) \,+\, F\left(x, t, \mathbf{v}, \dfrac{\partial\mathbf{v}}{\partial x}\right) \,=\, 0 ~~~ \text{for} ~~~ (x, t) \in \delta\Omega \\
&p(0, t) \,=\, -\begin{bmatrix}
				D \, \dfrac{n}{\lambda_n}\\[2ex]
				\dfrac{D}{\zeta} \, \dfrac{T}{\lambda_T} \\[2ex]
				\dfrac{\mu D}{\epsilon} \, \dfrac{Z}{\lambda_Z}
				\end{bmatrix}_{x = 0}
~~ \text{and} ~~
p(L, t) \,=\, \begin{bmatrix}
				\Gamma_c(t) \\[1ex]
				\dfrac{(\gamma - 1) q_c - T\Gamma_c(t)}{n} \\[2ex]
				0
				\end{bmatrix}_{x=L}~.
\end{align}\normalsize
-->

Paquay's initial conditions for density and temperature, and Staps' initial condition for $Z$:
\small\begin{align}
	n(x,0) \,&=\, -\dfrac{\Gamma_\infty \lambda_n}{D} \,
		\left(1 + \frac{x}{\lambda_n}\right)~, ~~~~ T(x,0) \,=\, q_\infty \,
		\dfrac{\gamma - 1}{\Gamma_\infty} \, \left[1
		- \frac{\lambda_n}{\zeta \lambda_T + \lambda_n} \, \left(1
		+ \frac{x}{\lambda_n}\right)^{-\zeta}\right]~.
\end{align}\normalsize

<!---
Staps' initial condition for $Z$ in H-mode:
\small\begin{align}
	Z(x,0) \,&=\, Z_S\left[1 - \tanh\left(\dfrac{L\,x - L}{2}\right)\right]
		\,=\, Z_S\left[1 - \frac{\exp(L\,x - L) - 1}{\exp(L\,x - L)
		+ 1}\right]~.
\end{align}\normalsize
-->

Steady-State Solutions
\small\begin{align}
	&\bar{n}(x) \,=\, \bar{n}(0) - \int_0^x \frac{\Gamma_c}{D(\bar{Z}(x))}~\text{d}x~,
		~~ \bar{T}(x) \,=\, \frac{(\gamma - 1) q_c}{\Gamma_c} \left(1 - \lambda_g\left(\frac{\bar{n}(x)}{\bar{n}(0)}\right)^{-\zeta}\right) \\
	&\bar{n}(0) \,=\, -\frac{\Gamma_c \lambda_n}{D(\bar{Z}(0))},
		~~ \lambda_g \,=\, \frac{\frac{\lambda_n}{\zeta \lambda_T}}{1 + \frac{\lambda_n}{\zeta \lambda_T}}~,
		~~ c_g \,=\, \frac{\zeta c_T - c_n}{1 + \zeta \frac{\lambda_T}{\lambda_n}}~, ~~ G(\bar{Z}(x)) \,=\, \theta\,D(\bar{Z}(x)) \\
	\text{Staps':}& ~ \theta \,=\, \frac{(\gamma - 1) q_c}{\Gamma_c^2 \lambda_n^2} (c_n + c_g), ~~ \text{Paquay's:} ~ \theta \,=\, \frac{\Gamma_c^2 \lambda_n^2}{q_c \zeta (\gamma - 1)} \, \frac{\lambda_n + \zeta\lambda_T}{c_n\lambda_T + c_T\lambda_n} \,=\, \frac{1}{\text{Staps}} \,=\, \text{Weymiens}
\end{align}\normalsize

### Physical Model
As a starting point, the nonambipolar currents are used, rather than some cubic polynomial.
Start with Staps' derivation, now known to be slightly incorrect, since the polarization current is defined slightly incorrectly in his version:
<!--
\small\begin{align}
	&\frac{m_i n T}{e \rho_{\theta i} B^2} \, \frac{\partial Z}{\partial t}
		\,=\, \frac{m_i \mu_i n T}{e \rho_{\theta i} B_\theta^2} \,
		\frac{\partial^2 Z}{\partial x^2} \,+\, \left(g_n^\text{an} -
		g_n^\text{cx}\right) \frac{n^\prime}{n} \,+\, \left(g_T^\text{an} -
		g_T^\text{cx}\right) \frac{T^\prime}{T} \,+\, \left(g_Z^\text{an} -
		g_Z^\text{cx}\right) Z - e\Gamma_i^{\pi\parallel} - e\Gamma_i^\text{ol}
\end{align}\normalsize
-->
\small\begin{align}
	&\frac{m_i \, n \, T}{e^2 \, \rho_{\theta i} \, B^2}
		\frac{\partial Z}{\partial t} \,=\,
		\frac{m_i \, \mu \, n \, T}{e^2 \rho_{\theta i} \, B_\theta^2} \,
		\frac{\partial^2 Z}{\partial x^2} \,+\, \Gamma_e^\text{an} \,-\,
		\Gamma_i^{\pi\parallel} \,-\, \Gamma_i^\text{cx} \,-\,
		\Gamma_i^\text{ol}
\end{align}\normalsize

Corrected version, which is used:
\small\begin{align}
	\text{Currents:} ~~~~ \frac{e \, n \, \rho_{\theta i}}{2} \,
		\frac{\partial Z}{\partial t} \,&=\, \frac{e \, \rho_{\theta i}}
		{2} \, \frac{\partial}{\partial x} \left[\mu \, n \, \frac{\partial Z}
		{\partial x}\right] \,+\, \sum_\text{k} e \, \Gamma^\text{k} \\
	\text{Reduced:} ~~~~ n \, \frac{\partial Z}{\partial t} \,&=\, 
		\frac{\partial}{\partial x} \left[\mu \, n \,
		\frac{\partial Z}{\partial x} \right] \,+\, \frac{2}{\rho_{\theta i}}
		\sum_\text{k} \Gamma^\text{k}~, ~~~ \sum_\text{k} \Gamma^\text{k}
		\,=\, \Gamma_e^\text{an} \,-\, \Gamma_i^\text{cx}
		\,-\, \Gamma_i^{\pi\parallel} \,-\, \Gamma_i^\text{ol}
\end{align}\normalsize

Some of the fluxes take this form: $\Gamma_j^\text{k} \,=\, g_n^\text{k}\,\dfrac{n^\prime}{n} \,+\, g_T^\text{k}\,\dfrac{T^\prime}{T} \,+\, g_Z^\text{k}\,Z$

+ Ion Bulk Viscosity: <!--- $N \,=\, \dfrac{\nu_{*i}\,\epsilon^{3/2}\,\nu_{ei}}{\nu_{ii}} ~~~\text{and}~~~ \eta \,=\, \dfrac{\epsilon^2 \sqrt{\pi}}{8 a_m} m_i \,n\, (v_{T_i})^2$
\small\begin{align}
	\begin{bmatrix}\xi_\theta \\[1ex] \xi_\phi \end{bmatrix} \,&=\, \dfrac{1}{\pi} \int_0^{\sqrt{\nu_{*i}}} \begin{bmatrix} 1 \\[1ex] \frac{5}{2} - x \end{bmatrix} x^2 \exp(-x) \, \tan^{-1}\left(\dfrac{2 N \sqrt{x}}{N^2 + Z^2 - x}\right) \text{d}x \\
	g_n^{\pi\parallel} \,=\, \eta \, \rho_{\theta i}& B_\theta \, \xi_\theta~,~~~~ g_n^{\pi\parallel} \,=\, \eta \, \rho_{\theta i} \left(B_\theta\,\xi_\theta - B\,\xi_\phi\right)~,~~~~ g_Z^{\pi\parallel} \,=\, 2\eta \, B_\theta \, \xi_\theta \\
\end{align}\normalsize
-->

\small\begin{align}
	D_{\pi\parallel} \,=\, \frac{\epsilon^2}{(x - a_m) \sqrt{\pi}}\,
		\frac{\rho_{\theta i} \, T}{B}~,~~~
	e \Gamma_i^{\pi\parallel} \,=\, e\,n_e\,D_{\pi\parallel}
		\left(\frac{n^\prime}{n} + \frac{Z}{\rho_{\theta i}}\right) \,
		\text{Im}\left[X\left(Z + \frac{i \, \nu_{ii}}{\omega_t}\right)\right]
\end{align}\normalsize

+ Electron Anomalous Diffusion:
\small\begin{align}
	D_\text{an} \,&=\, \frac{\epsilon^2 \sqrt{\pi}}{2 a_m}
		\frac{\rho_{\theta e} T}{B}~,~~
		g_n^\text{an} \,=\, -e \,n\, D_\text{an}~,~~
		g_T^\text{an} \,=\, \alpha_\text{an}\, g_n^\text{an}~,~~
		g_Z^\text{an} \,=\, \frac{g_n^\text{an}}{\rho_{\theta i}}
\end{align}\normalsize

+ Charge Exchange Friction:
\small\begin{align}
	g_n^\text{cx} \,=\,
		-\frac{m_i \,n_0 \langle\sigma_\text{cx} v\rangle \,n \,T}{B_\theta^2}
		\left[\frac{B_\theta^2}{\epsilon^2 B_\phi^2} + 2\right]~,~~~~
		g_T^\text{cx} \,=\, \alpha_\text{cx}\,g_n^\text{cx}~,~~~~
		g_Z^\text{cx} \,=\, \pm\frac{g_n^\text{cx}}{\rho_{\theta i}}~?
\end{align}\normalsize

+ Ion Orbit Loss:
\small\begin{align}
	g^\text{ol} \,=\, e \,n\, \nu_{ii} \, \nu_{*i} \, \rho_{\theta i}~,~~~~
	e\Gamma_i^\text{ol} \,=\, g^\text{ol} \, \frac{
		\exp\left[-\sqrt{\nu_{*i} + Z^4 + \frac{x^4}{w_{bi}^4}}\right]}
		{\sqrt{\nu_{*i} + Z^4 + \frac{x^4}{w_{bi}^4}}}
\end{align}\normalsize

