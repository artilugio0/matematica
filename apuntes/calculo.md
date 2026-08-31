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


## Condición necesaria de convergencia

$$
\sum\limits_{n = 1}^{\infty} a_n \Rightarrow \lim\limits_{n \to \infty} a_n = 0
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

Sea $\{a_n\}$ y $\{b_n\}$ sucesiones tales que $\forall\ n \in \mathbb{N}: a_n \geq 0$  y $b_n \geq 0$.

Si $\lim\limits_{n \to \infty} \frac{a_n}{b_n} = c > 0 \Rightarrow \sum\limits_{n = 1}^{\infty} a_n$ y $\sum\limits_{n = 1}^{\infty} b_n$ ambas convergen o ambas divergen.


### Criterio 4

Sea $\{a_n\}$ y $\{b_n\}$ sucesiones tales que $\forall\ n \in \mathbb{N}: a_n \geq 0$  y $b_n \geq 0$.

Si $\lim\limits_{n \to \infty} \frac{a_n}{b_n} = 0 \wedge \sum\limits_{n = 1}^{\infty} b_n$ converge $\Rightarrow \sum\limits_{n = 1}^{\infty} a_n$ converge.


### Criterio 5

Sea $\{a_n\}$ y $\{b_n\}$ sucesiones tales que $\forall\ n \in \mathbb{N}: a_n \geq 0$  y $b_n \geq 0$.

Si $\lim\limits_{n \to \infty} \frac{a_n}{b_n} = +\infty \wedge \sum\limits_{n = 1}^{\infty} b_n$ diverge $\Rightarrow \sum\limits_{n = 1}^{\infty} a_n$ diverge.


### Criterio de D'Alambeert

Sea $\{a_n\}$ una sucesión tal que $\forall\ n \in \mathbb{N}: a_n \geq 0$.

$$
\lim\limits_{n \to \infty} \frac{a_n}{a_{n+1}} = l \Rightarrow
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

Sean $\{a_n\}$ una sucesión tal que $$a_n \geq 0 \wedge a_n \geq a_{n+1}$, y $f: \mathbb{R} \to \mathbb{R}$ contínua no creciente tal que $\forall\ n \in \mathbb{N}:\ f(n) = a_n$.

Si $\int\limits_{1}^{\infty} f(x)dx = k \Rightarrow \sum\limits_{n = 1}^{\infty} a_n$ converge.

Si $\int\limits_{1}^{\infty} f(x)dx$ diverge $\Rightarrow \sum\limits_{n = 1}^{\infty} a_n$ diverge.


### Criterio de Leibnitz

Sea una sucesión $\{a_n\}$ tal que $a_n \geq 0$, $a_n \geq a_{n+1}$ y $\lim\limits_{n \to \infty} a_n = 0 \Rightarrow \sum\limits_{n = 1}^{\infty} a_n$ converge.


## Convergencia absoluta

Una serie converge absolutamente si se cumple que $\sum\limits_{n = 1}^{\infty} a_n$ converge y $\sum\limits_{n = 1}^{\infty} \lvert a_n \rvert$ converge.


## Convergencia condicional

Una serie converge condicionalmente si se cumple que $\sum\limits_{n = 1}^{\infty} a_n$ converge y $\sum\limits_{n = 1}^{\infty} \lvert a_n \rvert$ diverge.


## Propiedad 6

$\sum\limits_{n = 1}^{\infty} \lvert a_n \rvert$ converge $\Rightarrow \sum\limits_{n = 1}^{\infty} a_n$ converge.


# Series de funciones

## Serie de funciones mayorante

## Serie de potencias

### Definicion

### Teorema de Abel

### Propiedades

### Ejemplos importantes

## Series de Taylor

## Series de Fourier

### Integrales basicas
