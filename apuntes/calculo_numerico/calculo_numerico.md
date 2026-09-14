# Cálculo numérico

## TODO

- Límite de una función en un punto
- Límite de una sucesión
- Función continua
- Función diferenciable
- Integral de Riemann

## Teorema 1.1

Equivalencia continuidad

Sea $f: A \subseteq \mathbb{R} \to \mathbb{R}$ y $x_0 \in A$.

$f$ es continua en $x_0 \Leftrightarrow \forall\ \{a_n\}_{n=1}^{\infty} \mid a_i \in A: \left[ \lim\limits_{n \to \infty} a_n = x_0 \Rightarrow \lim\limits_{n \to \infty} f(a_n) = f(x_0) \right]$


## Teorema 1.2

Continuidad de una función diferenciable.

Sea $f: A \subseteq \mathbb{R} \to \mathbb{R}$ y $x_0 \in A$.

$f$ es diferenciable en $x_0 \Rightarrow f$ continua en $x_0$.


## Teorema 1.3

Teorema del valor intermedio.

Sea $f \in C[a, b]$.

Si $f(a) \leq f(b) \wedge k \in (f(a), f(b)): \exists\ c \in (a, b) \mid f(c) = k$

Si $f(a) > f(b) \wedge k \in (f(b), f(a)): \exists\ c \in (a, b) \mid f(c) = k$


## Teorema 1.4

Teorema del Rolle

Sea $f \in C[a, b]$ y diferenciable en $(a, b)$.

Si $f(a) = f(b) \Rightarrow \exists\ c \in (a, b) \mid f'(c) = 0$


## Teorema 1.5

Teorema del Rolle Generalizado

Sea $f \in C[a, b]$ y diferenciable $n$ veces en $(a, b)$.

Si $\exists\ a \leq x_0 < x_1 < \dots < x_n \leq b \mid f(x_i) = 0 \Rightarrow \exists\ c \in (x_0, x_n) \subseteq (a, b) \mid f^{(n)}(c) = 0$


## Teorema 1.6

Teorema del valor medio

Sea $f \in C[a, b]$ y diferenciable en $(a, b)$.

$\exists\ c \in (a, b) \mid f'(c) = \frac{f(b) - f(a)}{b - a}$


## Teorema 1.7

Teorema del valor extremo

Sea $f \in C[a, b]$

$\exists\ c_1, c_2 \in [a, b] \mid \forall\ x \in [a, b]:\ f(c_1) \leq f(x) \leq f(c_2)$

Si $f$ es diferenciable en $(a, b) \Rightarrow c_1, c_2 \in \{a, b\} \cup \{c \in (a, b) \mid f'(c) = 0\}$


## Teorema 1.8

Teorema del valor medio para integrales generalizado

Sea $f \in C[a, b]$ y $g$ integrable en $[a, b]$ tal que no cambie de signo en $[a, b]$.

$\exists\ c \in (a, b) \mid \int\limits_{a}^{b} f(x)g(x)dx = f(c)\int\limits_{a}^{b}g(x)dx$


## Teorema 1.9

Teorema del Taylor

Sea $f$ derivable $n+1$ veces en $[a, b]$ y $x_0 \in [a, b]$.

$\forall\ x \in [a, b]: \exists\ \xi_x$ entre $x_0$ y $x$ tal que $f(x) = P_n(x) + R_n(x)$

Siendo

$P_n(x) = \sum\limits_{k = 0}^{n} \frac{f^{(k)}(x_0)}{k!} \cdot (x - x_0)^k$

$R_n(x) = \frac{f^{(n + 1)}(\xi_x)}{(n + 1)!} \cdot (x - x_0)^{n + 1}$


## Punto flotante en base 2

Se representa un número real con 64 bits divididos de la siguiente forma:

- $s$: Signo (1 bit)
- $c$: Característica (11 bits)
- $f$: Mantisa (52 bits)

$$
(-1)^{s} \cdot 2^{c - 1023} \cdot (1 +f)
$$

TODO: agregar metodos de traduccion


## Valor mínimo positivo de punto flotante en base 2

- $s = 0$
- $c = 1$
- $f = 0$

$(-1)^0 \cdot 2^{1 - 1023} \cdot (1 + 0)$


## Punto flotante decimal de k dígitos

### Terminación por truncado

$y = \pm 0.d_1 d_2 \dots d_k d_{k+1} \dots \times 10^{n}$

$fl(y) = \pm 0.d_1 d_2 \dots d_k \times 10^{n}$


### Terminación por redondeo

$y = \pm 0.d_1 d_2 \dots d_k d_{k+1} \dots \times 10^{n}$

Se suma $5 \times 10^{n - (k + 1)}$ a $y$, luego se trunca el resultado a $k$ dígitos.

Esto es equivalente a:

$$
\begin{cases}
d_{k+1} \geq 5 &\Rightarrow \text{se suma 1 a } d_k \text{ y luego se trunca a } k \text{ dígitos}\\
d_{k+1} < 5    &\Rightarrow \text{se trunca a } k \text{ dígitos} \\
\end{cases}
$$


## Error de aproximación

Sea $p^{*}$ una aproximación de $p$. El error de aproximación es:

$p - p^{*}$


## Error de aproximación absoluto

Sea $p^{*}$ una aproximación de $p$. El error de aproximación absoluto es:

$\lvert p - p^{*} \rvert$


## Error de aproximación relativo

Sea $p^{*}$ una aproximación de $p$. El error de aproximación relativo es:

$\frac{\lvert p - p^{*} \rvert}{\lvert p \rvert}$, si $p \neq 0$.


## Forma anidada de polinomios

Es conveniente evaluar polinomios en su forma anidada porque reduce la cantidad de operaciones aritméticas.

Ejemplo:

La forma anidada de $x^3 - 6.1 \cdot x^2 + 3.2 \cdot x + 1.5$ es $((x - 6.1) \cdot x + 3.2) \cdot x + 1.5$.


## Teorema 2.1

Teorema de aproximación de Weierstrass

Sea $f \in C[a,b]$.

$\forall\ \epsilon > 0: \exists\ P(x) \text{ polinomio} \mid \lvert f(x) - P(x) \rvert < \epsilon\ \forall\ x \in [a, b]$


## Teorema 2.2

Polinomio interpolador de Lagrange

Sean $x_0, x_1, \dots\ , x_n \in A \subseteq \mathbb{R}$ todos distintos y $f: A \to \mathbb{R}$.

$\exists!\ P(x) \in \mathbb{R}_n[x] \mid f(x_k) = P(x_k)$ para cada $k = 0, 1, \dots\ , n$.

El polinomio está definido por $P(x) = \sum\limits_{k = 0}^n f(x_k) \cdot L_{k,n}(x)$

Siendo
$$
L_{k,n}(x) = \prod\limits_{\substack{i = 0 \\ i \neq k}}^n \frac{x - x_i}{x_k - x_i} = \frac{(x - x_0) \cdot (x - x_1) \cdot\ \dots\ \cdot (x - x_{k-1}) \cdot (x - x_{k+1}) \cdot\ \dots\ \cdot (x - x_n)}{(x_k - x_0) \cdot (x_k - x_1) \cdot\ \dots\ \cdot (x_k - x_{k-1}) \cdot (x_k - x_{k+1}) \cdot\ \dots\ \cdot (x_k - x_n)}
$$


## Teorema 2.3

Sean $x_0, x_1, \dots\ , x_n \in [a, b] \subseteq \mathbb{R}$, $f \in C^{n+1}[a, b]$ y $P(x)$ su polinomio interpolador de Lagrange para $f$ en esos puntos.

$\forall\ x \in [a, b]: \exists\ \xi(x) \in (a, b) \mid f(x) = P(x) + \frac{f^{(n+1)}(\xi(x))}{(n + 1)!} \cdot (x - x_0) \cdot (x - x_1) \cdot\ \dots\ \cdot (x - x_n)$


## Interpolador spline cúbico

Sea $f: [a, b] \subseteq \mathbb{R} \to \mathbb{R}$ y los nodos $a = x_0 < x_1 <\ \dots\ < x_n = b$, un interpolador spline cúbico $S$ de $f$ es una función que cumple:

1. $S(x)$ es un polinomio cúbico, denotado por $S_j(x)$, en cada intervalo $[x_j, x_{j+1}]$ para $j = 0, 1,\ \dots\ , n-1$
2. $S_j(x_j) = f(x_j) \wedge S_{j}(x_{j+1}) = f(x_{j+1})$ para $j = 0, 1,\ \dots\ , n-1$
3. $S_{j+1}(x_{j+1}) = S_j(x_{j+1})$ para $j = 0, 1,\ \dots\ , n-2$
4. $S_{j+1}'(x_{j+1}) = S_j'(x_{j+1})$ para $j = 0, 1,\ \dots\ , n-2$
5. $S_{j+1}''(x_{j+1}) = S_j''(x_{j+1})$ para $j = 0, 1,\ \dots\ , n-2$
6. Satisface alguna de las siguientes condiciones de frontera:
    1. $S''(x_0) = S''(x_n) = 0$ (natural (or free) boundary)
    2. $S'(x_0) = f'(x_0) \wedge S'(x_n) = f'(x_n)$ (clamped boundary)


## Teorema 3.1

Sea $f: [a, b] \subseteq \mathbb{R} \to \mathbb{R}$ y los nodos $a = x_0 < x_1 <\ \dots\ < x_n = b$.

$f$ tiene un único interpolador spline cúbico $S$ sobre esos nodos que cumple las condiciones de natural boundary, es decir $S''(x_0) = S''(x_n) = 0$.


## Teorema 3.2

Sea $f: [a, b] \subseteq \mathbb{R} \to \mathbb{R}$ diferenciable en $a$ y $b$, y los nodos $a = x_0 < x_1 <\ \dots\ < x_n = b$.

$f$ tiene un único interpolador spline cúbico $S$ sobre esos nodos que cumple las condiciones de clamped boundary, es decir $S'(x_0) = f'(x_0) \wedge S'(x_n) = f'(x_n)$.


## Teorema 3.3

Sean $f \in C^4[a, b]$ con $\max\limits_{a \leq x \leq b}\ \lvert f^{(4)}(x) \rvert = M$ y $S$ su interpolador spline cúbico único con clamped boundary en los nodos $a = x_0 < x_1 <\ \dots\ < x_n = b$.

$\forall\ x \in [a, b]: \lvert f(x) - S(x) \rvert \leq \frac{5 \cdot M}{384} \cdot \max\limits_{0 \leq j \leq n-1}\ (x_{j+1} - x_j)^4$


## Polinomios de Hermite cúbicos para curvas paramétricas

Dados los nodos $(x_0, y_0), (x_1, y_1)$. Las ecuaciones paramétricas con polinomios de Hermite que interpolan esos nodos en $t \in [0, 1]$ cumpliendo $x'(0) = \alpha_0,\ x'(1) = \alpha_1,\ y'(0) = \beta_0,\ y'(1) = \beta_1$ son:

$x(t) = [2 \cdot (x_0 - x_1) + (\alpha_0 + \alpha_1)] \cdot t^3 + [-3 \cdot (x_0 - x_1) - (2 \cdot \alpha_0 + \alpha_1)] \cdot t^2 + \alpha_0 \cdot t + x_0$

$y(t) = [2 \cdot (y_0 - y_1) + (\beta_0 + \beta_1)] \cdot t^3 + [-3 \cdot (y_0 - y_1) - (2 \cdot \beta_0 + \beta_1)] \cdot t^2 + \beta_0 \cdot t + y_0$


## Diferenciación numérica

### Primera derivada: Fórmulas de 3 puntos

#### Endpoint

$f'(x_0) = \frac{1}{2 \cdot h} \cdot [-3 \cdot f(x_0) + 4 \cdot f(x_0 + h) - f(x_0 + 2 \cdot h)] + \frac{h^2}{3} \cdot f^{(3)}(\xi_0)$

Con $\xi_0$ entre $x_0$ y $x_0 + 2 \cdot h$.


#### Midpoint

$f'(x_0) = \frac{1}{2 \cdot h} \cdot [f(x_0 + h) - f(x_0 - h)] - \frac{h^2}{6} \cdot f^{(3)}(\xi_1)$

Con $\xi_1$ entre $x_0 - h$ y $x_0 + h$.


#### Cota de error

$\frac{\epsilon}{h} + \frac{h^2}{6} \cdot M$

Siendo $\epsilon > 0$ una cota superior a todos los errores de redondeo, $\frac{\epsilon}{h}$ el error de redondeo y $\frac{h^2}{6} \cdot M$ el error de truncado, donde $M > 0$ es la cota superior de $\lvert f^{(3)}(\xi) \rvert$ con $x_0 - h < \xi < x_0 + h$.


### Segunda derivada: Midpoint

$f''(x_0) = \frac{1}{h^2} \cdot [f(x_0 - h) - 2 \cdot f(x_0) + f(x_0 + h)] - \frac{h^2}{24} \cdot [f^{(4)}(\xi_1) + f^{(4)}(\xi_{-1})]$

Con $x_0 - h < \xi_{-1} < x_0 < \xi_1 < x_0 + h$.

Si $f^{(4)}$ es continua en $[x_0 - h, x_0 + h]$, entonces el término de error puede simplificarse a $-\frac{h^2}{12} \cdot f^{(4)}(\xi)$, con $x_0 - h < \xi < x_0 + h$.
