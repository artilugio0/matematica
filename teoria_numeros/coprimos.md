# Coprimos

## Definición

Sean $a, b \in \mathbb{Z}$, no ambos nulos.

$a$ y $b$ son coprimos si $mcd(a, b) = 1$.


## Motivación

Los números coprimos tienen propiedades importantes relacionadas a divisibilidad que no son válidas en general, lo que los vuelve importantes en la teoría de números y otras areas de la matemática.


## Ejemplos

Coprimos:

- $mcd(9, 16) = 1$
- $mcd(14, 15) = 1$
- $mcd(7, 11) = 1$

No coprimos:

- $mcd(9, 12) = 3$


## Ejemplos destacables

Coprimos

- $mcd(9, 1) = 1$
- $mcd(14, -1) = 1$
- $mcd(1, 1) = 1$
- $mcd(-1, -1) = 1$

No coprimos:

- $mcd(7, 0) = 7$


# Teorema 6.1

$a$ y $b$ son coprimos si y solo si existen $x, y \in \mathbb{Z}$ tales que $a \cdot x + b \cdot y = 1$.

Demostración:

($\Rightarrow$)

Si $a$ y $b$ son coprimos, entonces $mcd(a, b) = 1$. Por _Teorema 5.1_, existen $x, y \in \mathbb{Z}$ tales que $a \cdot x + b \cdot y = 1$.


($\Leftarrow$)

Si existen $x, y \in \mathbb{Z}$ tales que $a \cdot x + b \cdot y = 1$, por _Teorema 5.4_ $mcd(a, b) \mid 1$. Luego, por _Teorema 2.2_, $mcd(a, b) = \pm 1$. Como $mcd(a, b) > 0$, entonces $mcd(a, b) = 1$.


# Teorema 6.2

Si $mcd(a,b) = d$, entonces $mcd(\frac{a}{d}, \frac{b}{d}) = 1$.

Demostración:

Si $mcd(a,b) = d$, por _Teorema 5.1_, existen $x, y \in \mathbb{Z}$ tales que $a \cdot x + b \cdot y = d$. Por definición, $d \mid a \wedge d \mid b$, y $d > 0$. Por lo tanto, se puede dividir ambos miembros de la igualdad por $d$ obteniendo $\frac{a}{d} \cdot x + \frac{b}{d} \cdot y = 1$, donde $\frac{a}{d}, \frac{b}{d} \in \mathbb{Z}$. Luego, por _Teorema 6.1_ son coprimos y por lo tanto $mcd(\frac{a}{d}, \frac{b}{d}) = 1$.



# Teorema 6.3

Si $a \mid c \wedge b \mid c \wedge mcd(a, b) = 1$, entonces $a \cdot b \mid c$.

Demostración:

Por _Teorema 6.1_, existen $x, y \in \mathbb{Z}$ tales que $a \cdot x + b \cdot y = 1$. Multiplicando por $c$ se tiene que $a \cdot c \cdot x + b \cdot c \cdot y = c$. Luego, como $a \mid c \wedge b \mid c$, existen $k_1, k_2 \in \mathbb{Z}$ tales que $c = a \cdot k_1$ y $c = b \cdot k_2$. Reemplazando en la igualdad anterior se tiene que $a \cdot b \cdot (k_2 \cdot x + k_1 \cdot y) = c$. Por lo tanto, $a \cdot b \mid c$.

# Teorema 6.4

Si $a \mid b \cdot c$ y $mcd(a,b) = 1$, entonces $a \mid c$.

Demostración:

Como $mcd(a, b) = 1$, existen $x, y \in \mathbb{Z}$ tales que $a \cdot x + b \cdot y = 1$. Multiplicando cada miembro por $c$, se tiene que $a \cdot c \cdot x + b \cdot c \cdot y = c$.

$a \mid a$, y por hipótesis $a \mid b \cdot c$. Entonces por _Teorema 2.7_, $a \mid (a \cdot c \cdot x + b \cdot c \cdot y)$. Por lo tanto $a \mid c$.


# Teorema 6.5

Si $mcd(a, b) = 1 \wedge mcd(a, c) = 1 \Rightarrow mcd(a, b \cdot c) = 1$.

Demostración:

Como $mcd(a, b) = 1 \wedge mcd(a, c) = 1$, por _Teorema 6.1_, existen $x_0, x_1, y_0, y_1 \in \mathbb{Z}$ tales que:

$$
\begin{aligned}
mcd(a, b) &= a \cdot x_0 + b \cdot y_0 = 1 \\
mcd(a, c) &= a \cdot x_1 + c \cdot y_1 = 1
\end{aligned}
$$

Multiplicando ambas igualdades se obtiene:

$$
a^2 \cdot x_0 \cdot x_1 + a \cdot c \cdot x_0 \cdot y_1 + a \cdot b \cdot x_1 \cdot y_0 + b \cdot c \cdot y_0 \cdot y_1 = 1
$$

Sea $d \in \mathbb{N}$, tal que $d \mid a \wedge d \mid b \cdot c$. Luego, por _Teorema 2.3_, $d$ divide cada uno de los términos de la ecuación anterior, entonces por _Teorema 2.7_, $d \mid 1$. Como $1 \mid a \wedge 1 \mid b \cdot c$, y para cualquier divisor comun $d$, $d \mid 1$, se tiene por _Teorema 5.3_ que $mcd(a, b \cdot c) = 1$.


# Teorema 6.6

Si $mcd(a, b) = 1 \wedge c \mid a$, entonces $mcd(c, b) = 1$.

Demostración:

Como $mcd(a, b) = 1$, existen $x, y \in \mathbb{Z}$ tales que $a \cdot x + b \cdot y = 1$. Y dado que $c \mid a$, existe $k \in \mathbb{Z}$ tal que $c \cdot k = a$. Reemplazando en la primera igualdad, se tiene que $c \cdot k \cdot x + b \cdot y = 1$. Por _Teorema 6.1_, $mcd(c, b) = 1$.


# Teorema 6.7

Si $mcd(a, b) = 1$, entonces $mcd(a \cdot c, b) = mcd(c, b)$.

Demostración:

Como $mcd(a, b) = 1$, existen $x_0, y_0 \in \mathbb{Z}$ tales que $a \cdot x_0 + b \cdot y_0 = 1$. Multiplicando por $c$ se tiene que $a \cdot c \cdot x_0 + b \cdot c \cdot y_0 = c$. Por _Teorema 2.3_, $mcd(a \cdot c, b)$ divide a cada termino del lado izquierdo de la igualdad, entonces por _Teorema 2.7_, $mcd(a \cdot c, b) \mid c$.

Por lo tanto $mcd(a \cdot c, b) \mid b \wedge mcd(a \cdot c, b) \mid c$.

Sea $d \in \mathbb{N}$ tal que $d \mid b \wedge d \mid c$. Por _Teorema 5.1_, existen $x_1, y_1 \in \mathbb{Z}$ tales que $mcd(a \cdot c, b) = a \cdot c \cdot x_1 + b \cdot y_1$. Por _Teorema 2.3_, $d$ divide a los términos de la derecha de la igualdad, entonces por _Teorema 2.7_, $d \mid mcd(a \cdot c, b)$. Luego, por _Teorema 5.3_, $mcd(a \cdot c, b) = mcd(c, b)$.


# Teorema 6.8

Si $mcd(a, b) = 1 \wedge c \mid (a + b) \Rightarrow mcd(a, c) = mcd(b, c) = 1$.

Demostración:

Como $mcd(a, b) = 1$, existen $x, y \in \mathbb{Z}$ tales que $a \cdot x + b \cdot y = 1$. Y dado que $c \mid (a + b)$, existe $k \in \mathbb{Z}$ tal que $c \cdot k = a + b$, por lo tanto, $a = c \cdot k - b$ y $b = c \cdot k - a$.

Combinando las igualdades anteriores se tiene:

$$
\begin{aligned}
a \cdot x + (c \cdot k - a) \cdot y &= a \cdot (x - y) + c \cdot k \cdot y = 1 && (1) \\
(c \cdot k - b) \cdot x + b \cdot y &= c \cdot k \cdot x + b \cdot (y - x) = 1 && (2)
\end{aligned}
$$

Por _Teorema 2.3_, $mcd(a, c)$ divide a los términos de $(1)$, entonces por _Teorema 2.7_, $mcd(a, c) \mid 1$. Y por _Teorema 2.2_, $mcd(a, c) = 1$.

Por _Teorema 2.3_, $mcd(b, c)$ divide a los términos de $(2)$, entonces por _Teorema 2.7_, $mcd(b, c) \mid 1$. Y por _Teorema 2.2_, $mcd(b, c) = 1$.


# Teorema 6.9

Si $mcd(a, b) = 1 \wedge d \mid a \cdot c \wedge d \mid b \cdot c$, entonces $d \mid c$.

Demostración:

Como $mcd(a, b) = 1$, existen $x, y \in \mathbb{Z}$ tales que $a \cdot x + b \cdot y = 1$. Multiplicando por $c$ se tiene que $a \cdot c \cdot x + b \cdot c \cdot y = c$. Por _Teorema 2.3_, $d$ divide a los términos de la igualdad, entonces por _Teorema 2.7_, $d \mid c$.


# Teorema 6.10

Sean $m, n \in \mathbb{N}$.

$mcd(a, b) = 1$ si y solo si $mcd(a^m, b^n) = 1$.

Demostración:

($\Rightarrow$)

Paso 1: Primero se demuestra que $mcd(a, b) = 1 \Rightarrow mcd(a, b^n) = 1$ por inducción sobre $n$.

Si $mcd(a, b) = 1$, entonces la proposición es verdadera para $n = 1$. Se asume cierta para $n = k$. Si $mcd(a, b) = 1$, entonces $mcd(a, b^k) = 1$. Por _Teorema 6.5_, como $mcd(a, b) = 1 \wedge mcd(a, b^k) = 1$, entonces $mcd(a, b^k \cdot b) = mcd(a, b^{k+1}) = 1$. Por lo tanto, se cumple para todo $n \in \mathbb{N}$.

Paso 2: Se demuestra que $mcd(a, b) = 1 \Rightarrow mcd(a^m, b^n) = 1$ por inducción sobre $m$.

Si $mcd(a, b) = 1$, por lo demostrado en _Paso 1_, $mcd(a, b^n) = 1$. Entonces la proposición es verdadera para $m = 1$.

Se asume cierta para $m = k$. Si $mcd(a, b) = 1$, entonces $mcd(a^k, b^n) = 1$.

Por lo demostrado en _Paso 1_, si $mcd(a, b) = 1$, entonces $mcd(a, b^n) = 1$. Luego, $mcd(a, b^n) = 1 \wedge mcd(a^k, b^n) = 1$. Entonces por _Teorema 6.5_, $mcd(a^k \cdot a, b^n) = mcd(a^{k+1}, b^n) = 1$. Por lo tanto, se cumple para todo $m \in \mathbb{N}$.

De esta forma queda demostrado para todo $m, n \in \mathbb{N}$

($\Leftarrow$)

Si $mcd(a^m, b^n) = 1$:

Si $a = 0$, entonces por _Teorema 3.2_, $mcd(a^m, b^n) = mcd(0, b^n) = \lvert b^n \rvert = 1$. Por lo tanto $b = \pm 1$, y por _Teorema 3.3_, $mcd(0, \pm 1) = mcd(a, b) = 1$.

Si $a \neq 0$, como $a \mid a^m$, por _Teorema 6.6_ $mcd(a, b^n) = 1$. Y dado que $b \mid b^n$, por el mismo teorema, $mcd(a, b) = 1$.

# Teorema 6.11

$mcd(a, a + 1) = 1$.

Demostración:

Por el _Teorema 3.5_, $mcd(a, a + 1) \mid 1$. Entonces, por _Teorema 2.2_, $mcd(a, a + 1) = \pm 1$. Por lo tanto $mcd(a, a + 1) = 1$
