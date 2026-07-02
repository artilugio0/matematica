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

No coprimos:

- $mcd(7, 0) = 7$


# Teorema 6.1

Sean $a, b \in \mathbb{Z}$. $a$ y $b$ son coprimos si y solo si existen $x, y \in \mathbb{Z}$ tales que $a \cdot x + b \cdot y = 1$.

Demostración:

($\Rightarrow$)
Si $a$ y $b$ son coprimos, entonces $mcd(a, b) = 1$. Por _Teorema 5.1_, existen $x, y \in \mathbb{Z}$ tales que $a \cdot x + b \cdot y = 1$.


($\Leftarrow$)
Si existen $x, y \in \mathbb{Z}$ tales que $a \cdot x + b \cdot y = 1$, por _Teorema 5.5_ $mcd(a, b) \mid 1$. Pero como $mcd(a, b) > 0$, entonces $mcd(a, b) = 1$.


# Teorema 6.2

Si $mcd(a,b) = d$, $\frac{a}{d}$ y $\frac{b}{d}$ son coprimos.

Demostración:

Si $mcd(a,b) = d$, por _Teorema 6.1_, existen $x, y \in \mathbb{Z}$ tales que $a \cdot x + b \cdot y = d$. Por definición, $d \mid a \wedge d \mid b$, y $d > 0$. Por lo tanto, se puede dividir ambos miembros de la igualdad por $d$ obteniendo $\frac{a}{d} \cdot x + \frac{b}{d} \cdot y = 1$, donde $\frac{a}{d}, \frac{b}{d} \in \mathbb{Z}$. Luego, por _Teorema 6.1_ son coprimos.



# Teorema 6.3

Si $a \mid c \wedge b \mid c \wedge mcd(a, b) = 1$, entonces $a \cdot b \mid c$.

Demostración:

Por _Teorema 6.1_, existen $x, y \in \mathbb{Z}$ tales que $a \cdot x + b \cdot y = 1$. Multiplicando por $c$ se tiene que $a \cdot c \cdot x + b \cdot c \cdot y = c$. Luego, como $a \mid c \wedge b \mid c$, existen $k_1, k_2 \in \mathbb{Z}$ tales que $c = a \cdot k_1$ y $c = b \cdot k_2$. Reemplazando en la igualdad anterior se tiene que $a \cdot b \cdot (k_2 \cdot x + k_1 \cdot y) = c$. Por lo tanto, $a \cdot b \mid c$.

# Teorema 6.4

a|bc y mcd(a,b) = 1, entonces a|c


# Teorema 6.5

(a) If gcd(a, b)= 1, and gcd(a, c)= 1, then gcd(a, bc)= 1.


# Teorema 6.6

(b) If gcd(a, b)= 1, and c I a, then gcd(b, c)= 1.


# Teorema 6.7

(c) If gcd(a, b)= 1, then gcd( ac, b) = gcd(c, b).


# Teorema 6.8

(d) If gcd(a, b)= 1, and c I a+b, then gcd(a, c)= gcd(b, c) = 1.


# Teorema 6.9

(e) If gcd(a, b)= 1, d I ac, and d I be, then d I c.


# Teorema 6.10

(f ) If gcd(a, b)= 1, then gcd( a2, b2)= 1.


# Teorema 6.11

a, b coprimos => a^m b^n coprimos


# Teorema 6.12

gcd(a, a+ 1) = 1.
