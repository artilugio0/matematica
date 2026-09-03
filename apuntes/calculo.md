# Sucesiones


## Definición de sucesión real

Una sucesión real es una función cuyo dominio es el conjunto $\mathbb{N}$ o $\mathbb{N}_0$ y su codominio es el conjunto $\mathbb{R}$.

$$
a: \mathbb{N} \to \mathbb{R}
$$

**Notación**:

$$
\begin{aligned}
a_i &= a(i) \\
\{a_n\} &= a_1, a_2, a_3, ... \\
\end{aligned}
$$


## Limites de una sucesión

Convergente: $\lim\limits_{n \to \infty} a_n = L \in \mathbb{R}$

Divergente: $\lim\limits_{n \to \infty} a_n = \infty$

Oscilante: $\not\exists \lim\limits_{n \to \infty} a_n$


# Series numericas


## Sumas parciales

Dada una sucesión $a: \mathbb{N} \to \mathbb{R}$, se definen a las sumas parciales de $a$ como:

$$
\begin{aligned}
S_1 &= \sum\limits_{k = 1}^{1} a_k = a_1 \\
S_2 &= \sum\limits_{k = 1}^{2} a_k = a_1 + a_2 = S_1 + a_2 \\
&\vdots \\
S_n &= \sum\limits_{k = 1}^{n} a_k = a_1 + a_2 +\ \dots\ + a_n = S_{n-1} + a_n \\
\end{aligned}
$$


## Sucesión de sumas parciales

Sea $\{a_n\}$ una sucesión, su sucesión de sumas parciales se define como:

$$
S_n: \mathbb{N} \to \mathbb{R} \mid S_n = \sum\limits_{k = 1}^{n} a_k
$$


## Definición de Serie

Sea $\{a_n\}$ una sucesión y $\{S_n\}$ su sucesión de sumas parciales. Se define la serie asociada a $\{a_n\}$ como:

$$
S = \sum\limits_{n = 1}^{\infty} a_n = \lim\limits_{n \to \infty} S_n \\
$$

Si el límite $\lim\limits_{n \to \infty} S_n$ existe y es $L \in \mathbb{R}$, entonces se dice que la serie es convergente y su valor es $L$. Si el límite no existe, entonces se dice que la serie es divergente.


## Serie de términos positivos

Sea $\sum\limits_{n = 1}^{\infty} a_n$ una serie, se dice que la serie es de términos positivos si cumple que $\forall\ n \in \mathbb{N}: a_n \geq 0$.

Sea $\{b_n\}$ una sucesión, su serie de términos positivos se define como:

$$
\sum\limits_{n = 1}^{\infty} \lvert b_n \rvert \\
$$


## Serie alternada

$$
\sum\limits_{n = 1}^{\infty} (-1)^{n} \cdot a_n
$$

$$
\sum\limits_{n = 1}^{\infty} (-1)^{n-1} \cdot a_n
$$

Con $\{a_n\}$ sucesión real tal que $a_n \geq 0$.


## Condición necesaria de convergencia

$$
\sum\limits_{n = 1}^{\infty} a_n \text{ convergente } \Rightarrow \lim\limits_{n \to \infty} a_n = 0
$$


## Propiedad 1

La convergencia o divergencia no es afectada por un número finito de términos.

Si $\sum\limits_{n = 1}^{\infty} a_n$ y $\sum\limits_{n = 1}^{\infty} b_n$ son series tales que $\exists\ m \in \mathbb{N} \mid \forall\ k > m: a_k = b_k$, entonces ambas series convergen o ambas series divergen.


## Propiedad 2

Si $\sum\limits_{n = 1}^{\infty} a_n = S \Rightarrow \forall\ c \in \mathbb{R}:\ \sum\limits_{n = 1}^{\infty} c \cdot a_n = c \cdot S$.


## Propiedad 3

Si $\sum\limits_{n = 1}^{\infty} a_n$ diverge $\Rightarrow \forall\ c \in \mathbb{R} - \{0\}:\ \sum\limits_{n = 1}^{\infty} c \cdot a_n$ diverge.


## Propiedad 4

Sea $\{a_n\}$ una sucesion tal que $\forall\ n \in \mathbb{N}:\ a_n > 0 \Rightarrow$ su sucesión de sumas parciales $\{S_n\}$ es creciente.


## Propiedad 5

Sea $\{a_n\}$ una sucesion tal que $\forall\ n \in \mathbb{N}:\ a_n > 0$.

$\sum\limits_{n = 1}^{\infty} a_n$ converge $\Leftrightarrow \{S_n\}$ es acotada.


## Criterios de convergencia para series de términos positivos

### Criterio 1

Sea $\{a_n\}$ y $\{b_n\}$ sucesiones tales que $\forall\ n \in \mathbb{N}: a_n \geq 0$  y $b_n \geq 0$.

Si $\sum\limits_{n = 1}^{\infty} b_n$ converge y $\forall\ n \in \mathbb{N}:\ a_n \leq b_n \Rightarrow \sum\limits_{n = 1}^{\infty} a_n$ converge.


### Criterio 2

Sea $\{a_n\}$ y $\{b_n\}$ sucesiones tales que $\forall\ n \in \mathbb{N}: a_n \geq 0$  y $b_n \geq 0$.

Si $\sum\limits_{n = 1}^{\infty} a_n$ diverge y $\forall\ n \in \mathbb{N}:\ a_n \leq b_n \Rightarrow \sum\limits_{n = 1}^{\infty} b_n$ diverge.


### Criterio 3

Sea $\{a_n\}$ y $\{b_n\}$ sucesiones tales que $\forall\ n \in \mathbb{N}: a_n \geq 0$  y $b_n > 0$.

Si $\lim\limits_{n \to \infty} \frac{a_n}{b_n} = c > 0 \wedge c < \infty \Rightarrow \sum\limits_{n = 1}^{\infty} a_n$ y $\sum\limits_{n = 1}^{\infty} b_n$ ambas convergen o ambas divergen.


### Criterio 4

Sea $\{a_n\}$ y $\{b_n\}$ sucesiones tales que $\forall\ n \in \mathbb{N}: a_n \geq 0$  y $b_n > 0$.

Si $\lim\limits_{n \to \infty} \frac{a_n}{b_n} = 0 \wedge \sum\limits_{n = 1}^{\infty} b_n$ converge $\Rightarrow \sum\limits_{n = 1}^{\infty} a_n$ converge.


### Criterio 5

Sea $\{a_n\}$ y $\{b_n\}$ sucesiones tales que $\forall\ n \in \mathbb{N}: a_n \geq 0$  y $b_n > 0$.

Si $\lim\limits_{n \to \infty} \frac{a_n}{b_n} = +\infty \wedge \sum\limits_{n = 1}^{\infty} b_n$ diverge $\Rightarrow \sum\limits_{n = 1}^{\infty} a_n$ diverge.


### Criterio de D'Alembert

Sea $\{a_n\}$ una sucesión tal que $\forall\ n \in \mathbb{N}: a_n > 0$.

$$
\lim\limits_{n \to \infty} \frac{a_{n+1}}{a_n} = l \Rightarrow
\begin{cases}
l < 1              &\Rightarrow \text{converge} \\
l > 1 \lor +\infty &\Rightarrow \text{diverge} \\
l = 1              &\Rightarrow \text{no define} \\
\end{cases}
$$


### Criterio de Cauchy

Sea $\{a_n\}$ una sucesión tal que $\forall\ n \in \mathbb{N}: a_n \geq 0$.

$$
\lim\limits_{n \to \infty} \sqrt[n]{a_n} = l \Rightarrow
\begin{cases}
l < 1              &\Rightarrow \text{converge} \\
l > 1 \lor +\infty &\Rightarrow \text{diverge} \\
l = 1              &\Rightarrow \text{no define} \\
\end{cases}
$$


### Criterio de la integral

Sean $\{a_n\}$ una sucesión tal que $a_n \geq 0 \wedge a_n \geq a_{n+1}$, y $f: [1, \infty) \to \mathbb{R}$ contínua no creciente tal que $\forall\ n \in \mathbb{N}:\ f(n) = a_n$.

Si $\int\limits_{1}^{\infty} f(x)dx$ converge $\Rightarrow \sum\limits_{n = 1}^{\infty} a_n$ converge.

Si $\int\limits_{1}^{\infty} f(x)dx$ diverge $\Rightarrow \sum\limits_{n = 1}^{\infty} a_n$ diverge.


### Criterio de Leibniz

Sea una sucesión $\{a_n\}$ tal que $a_n \geq 0$, $a_n \geq a_{n+1}$ y $\lim\limits_{n \to \infty} a_n = 0 \Rightarrow \sum\limits_{n = 1}^{\infty} (-1)^n \cdot a_n$ converge.


## Convergencia absoluta

Una serie converge absolutamente si se cumple que $\sum\limits_{n = 1}^{\infty} \lvert a_n \rvert$ converge.


## Convergencia condicional

Una serie converge condicionalmente si se cumple que $\sum\limits_{n = 1}^{\infty} a_n$ converge y $\sum\limits_{n = 1}^{\infty} \lvert a_n \rvert$ diverge.


## Propiedad 6

$\sum\limits_{n = 1}^{\infty} \lvert a_n \rvert$ converge $\Rightarrow \sum\limits_{n = 1}^{\infty} a_n$ converge.


## Serie geométrica

Dados $a, q \in \mathbb{R}$.

$$
\sum\limits_{n = 0}^{\infty} a \cdot q^n =
\begin{cases}
\frac{a}{1 - q} &\lvert q \rvert < 1 \\
\text{diverge}  &\lvert q \rvert \geq 1 \\
\end{cases}
$$


# Series de funciones

## Definición

Sea la famila de funciones $f_n: A \subseteq \mathbb{R} \to \mathbb{R},\ \forall\ n \in \mathbb{N}$.

Se define la serie de funciones como $\sum\limits_{n = 1}^{\infty} f_n(x)$.

Es una serie donde sus términos son funciones.


## Dominio de convergencia

Sea $\sum\limits_{n = 1}^{\infty} f_n(x)$ una serie de funciones, donde $f_n: A \subseteq \mathbb{R} \to \mathbb{R}$.

Se define el dominio de convergencia de la serie como:

$DCV = \{x_0 \in A \mid \sum\limits_{n = 1}^{\infty} f_n(x_0) \text{ es convergente} \}$

Nota: en la definición, $\sum\limits_{n = 1}^{\infty} f_n(x_0)$ es una serie numérica.


## Suma de la serie de funciones

Sea $\sum\limits_{n = 1}^{\infty} f_n(x)$ una serie de funciones con dominio de convergencia $DCV$.

La suma de la serie de funciones es la funcion $S: DCV \to \mathbb{R} \mid S(x) = \sum\limits_{n = 1}^{\infty} f_n(x)$


## Resto n-ésimo

Sea $\sum\limits_{n = 1}^{\infty} f_n(x)$ una serie de funciones, tal que su suma es $S(x)$ sobre el dominio de convergencia $DCV$.

Sea $S_n(x)$ la $n$-ésima suma parcial de la serie de funciones, se define al resto $n$-ésimo como:

$R_n(x) = S(x) - S_n(x)$

Y se cumple que $\lim\limits_{n \to \infty} R_n(x) = 0$.


## Definición alternativa de la suma de funciones

Sea $\sum\limits_{n = 1}^{\infty} f_n(x)$ una serie de funciones.

Sea $S_n(x)$ la $n$-ésima suma parcial de la serie de funciones, se define la suma de la serie de funciones como:

$S(x) = \lim\limits_{n \to \infty} S_n(x)$


## Serie de funciones mayorante

Sea $\sum\limits_{n = 1}^{\infty} f_n(x)$ una serie de funciones con dominio de convergencia $DCV$.

Se dice que la serie de funciones es mayorante en un intervalo $A \subseteq DCV$ si existe una serie numérica $\sum\limits_{n = 1}^{\infty} a_n$ de términos positivos y convergente tal que $\forall\ x \in A: \lvert f_n(x) \rvert \leq a_n$.

Si una serie de funciones es mayorante, entonces:

- Si las funciones $f_n$ son contínuas $\Rightarrow S(x) = \sum\limits_{n = 1}^{\infty} f_n(x)$ es contínua.
- Si las funciones $f_n$ son integrables $\Rightarrow S(x) = \sum\limits_{n = 1}^{\infty} f_n(x)$ es integrable y $\int\limits_{a}^{b} S(x)dx = \sum\limits_{n = 1}^{\infty} \left[\int\limits_{a}^{b} f_n(x)dx \right]$.


## Serie de potencias

### Definición

$\sum\limits_{n = 0}^{\infty} a_n \cdot x^n = a_0 + a_1 \cdot x + a_2 \cdot x^2 + \dots + a_n \cdot x^n + \dots$


### Teorema de Abel

Sea la serie de potencias $a_0 + a_1 \cdot x + a_2 \cdot x^2 + \dots + a_n \cdot x^n + \dots$
 
- Si la serie de potencias es convergente en $x_0 \neq 0 \Rightarrow \forall\ x / \lvert x \rvert < \lvert x_0 \rvert$: la serie es absolutamente convergente.
- Si la serie de potencias es divergente en $x_0 \Rightarrow \forall\ x / \lvert x_0 \rvert < \lvert x \rvert$: la serie es divergente.

**Demostración**: TODO


### Radio e intervalo de convergencia

Sea la serie de potencias $a_0 + a_1 \cdot x + a_2 \cdot x^2 + \dots + a_n \cdot x^n + \dots$.

El radio de convergencia es $R \in \mathbb{R} \cup \{\infty\}, R \geq 0 \mid \forall\ x \in (-R, R)$ la serie es absolutamente convergente y $(-\infty, -R) \cup (R, \infty)$ es divergente.

A $(-R, R)$ se le llama intervalo de convergencia ($ICV$).

$ICV \subseteq DCV$. Pueden ser distintos, hay que ver que ocurre en los extremos del $ICV$.


### Como encontrar el $ICV$ y $DCV$?

Usar el criterio de D'Alembert.

$\lim\limits_{n \to \infty} \frac{\lvert a_{n+1} \cdot x^{n+1} \rvert}{\lvert a_n \cdot x^n \rvert} = \lvert x \rvert \cdot \lim\limits_{n \to \infty} \lvert \frac{a_{n+1}}{a_n} \rvert < 1$

Despejar $x$ para obtener el $ICV$.

Para obtener el $DCV$ hay que analizar las series numéricas resultantes al evaluar la serie de potencias en los extremos del $ICV$.


### Propiedades

1. Es mayorante en todo intervalo $[-r, r] \subset ICV$
2. Es contínua en todo su dominio
3. Su integral es la suma de las integrales de sus términos en $ICV$
4. Su derivada es la suma de las derivadas de sus términos en $ICV$


## Series de Taylor

### Definición

Sean $x_0 \in \mathbb{R}$ y $f: A \subseteq \mathbb{R} \to \mathbb{R}$ derivable para todo orden de derivación en un entorno $E(x_0)$.

La serie de Taylor de la función $f$ es la serie de potencias definida como:

$S(x) = \frac{f(x_0)}{0!} + \frac{f'(x_0)}{1!} \cdot (x - x_0) + \frac{f''(x_0)}{2!} \cdot (x - x_0)^2 + \dots + \frac{f^{(n)}(x_0)}{n!} \cdot (x - x_0)^n + \dots$


### Cuándo es la suma igual a la función?

Sean $f: A \subseteq \mathbb{R} \to \mathbb{R}$ derivable para todo orden de derivación en un entorno $E(x_0)$, $P_n(x)$ el polinomio de Taylor de grado $n$ de la función centrado en $x_0$ y $R_n(x)$ su resto n-ésimo.

Entonces:

$f(x) = P_n(x) + R_n(x)$

Luego,

$$
\begin{aligned}
f(x) = \lim\limits_{n \to \infty} P_n(x) &\Leftrightarrow \lim\limits_{n \to \infty} R_n(x) = 0 \\
              &\Leftrightarrow \forall\ x \in DCV: \lim\limits_{n \to \infty} \frac{f^{(n+1)}(\theta)}{(n + 1)!} \cdot (x - x_0)^{n + 1} = 0 \\
\end{aligned}
$$


## Series de Fourier

### Serie de funciones trigonométricas

$S(x) = \frac{a_0}{2} + \sum\limits_{n = 1}^{\infty} \left[a_n \cdot cos(n \cdot x) + b_n \cdot sen(n \cdot x) \right]$

La suma $S(x)$, en caso de existir, es periódica de período $2 \pi$.


### Coeficientes de Fourier

$\frac{a_0}{2} = \frac{1}{2 \pi} \cdot \int\limits_{-\pi}^{\pi} f(x)\ dx$

$a_n = \frac{1}{\pi} \cdot \int\limits_{-\pi}^{\pi} f(x) \cdot cos(n \cdot x)\ dx$

$b_n = \frac{1}{\pi} \cdot \int\limits_{-\pi}^{\pi} f(x) \cdot sen(n \cdot x)\ dx$


### Cuándo es la suma igual a la función?

Si se cumple:

- $f$ de período $2 \pi$
- $f$ acotada en $[-\pi, \pi]$
- $f$ monótona por trozos

Entonces, la serie de Fourier de $f$:

- Converge para todo $x \in \mathbb{R}$
- Si $f$ es contínua en $c \Rightarrow S(c) = f(c)$ 
- Si $f$ no es contínua en $c \Rightarrow S(c) = \frac{1}{2} \cdot (\lim\limits_{x \to c^{-}} f(x) + \lim\limits_{x \to c^{+}} f(x))$ 


### Serie de Fourier para funcion de período 2l

$\frac{a_0}{2} = \frac{1}{2 l} \cdot \int\limits_{-l}^{l} f(x)\ dx$

$a_n = \frac{1}{l} \cdot \int\limits_{-l}^{l} f(x) \cdot cos(\frac{n \cdot \pi}{l} \cdot x)\ dx$

$b_n = \frac{1}{l} \cdot \int\limits_{-l}^{l} f(x) \cdot sen(\frac{n \cdot \pi}{l} \cdot x)\ dx$

