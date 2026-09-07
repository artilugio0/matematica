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

Se suma $5 \times 10^{n - (k + 1)}$ a $y$, luego se trunca a $k$ digitos del resultado.

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
