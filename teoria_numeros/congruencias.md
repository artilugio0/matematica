# Congruencias


## Definición

Sean $a, b \in \mathbb{Z}$ y $n \in \mathbb{N}$.

$a$ es congruente con $b$ módulo $n$ si $a - b$ es divisible por $n$.

$a \equiv b\ (mod\ n) \Leftrightarrow n \mid a - b$


## Motivación

- La relación de congruencia permite efectuar cálculos donde solo importa el valor del resto de la división por $n$ de una forma conveniente.
- El concepto es una de las bases de la teoría de números.
- También utilizado en otras áreas de la matemática como estructuras algebraicas.


## Ejemplos

- $n$ no primo: $10 \equiv 34\ (mod\ 4)$
- $n$ primo: $13 \equiv 18\ (mod\ 5)$
- $a$ negativo: $-9 \equiv 15\ (mod\ 6)$


## Ejemplos destacables

- $n \mid a$:
  - $10 \equiv 0\ (mod\ 5)$

- $b = -1$:
  - $11 \equiv -1\ (mod\ 12)$

- $n = 2$:
  - $10 \equiv 0\ (mod\ 2)$ - 10 es par
  - $11 \equiv 1\ (mod\ 2)$ - 11 es impar


## Contraejemplos

- $a \equiv b\ (mod\ n) \not\Rightarrow -a \equiv b\ (mod\ n)$
  - $9 \equiv 33\ (mod\ 4)$, pero $-9 \not\equiv 33\ (mod\ 4)$

- $a^2 \equiv b^2\ (mod\ n) \not\Rightarrow a \equiv b\ (mod\ n)$
  - $3^2 \equiv 4^2\ (mod\ 7)$, pero $3 \not\equiv 4\ (mod\ 7)$

- $a^k \equiv b^k\ (mod\ n) \wedge k \equiv j\ (mod\ n) \not\Rightarrow a^j \equiv b^j\ (mod\ n)$
  - $3^2 \equiv 4^2\ (mod\ 7) \wedge 9 \equiv 2\ (mod\ 7)$, pero $3^9 \not\equiv 4^9\ (mod\ 7)$

- $a \cdot c \equiv b \cdot c\ (mod\ n) \not\Rightarrow a \equiv b\ (mod\ n)$
  - $6 \cdot 2 \equiv 2 \cdot 2\ (mod\ 8)$, pero $6 \not\equiv 2\ (mod\ 8)$


# Teorema 10.1

$a \equiv b\ (mod\ n)$ si y solo si $a$ y $b$ tienen el mismo resto en la división por $n$.

**Demostración**:

($\Rightarrow$)

Por _Teorema 1.1_, existen $q, q', r, r' \in \mathbb{Z}$ tales que $a = n \cdot q + r$ y $b = n \cdot q' + r'$, con $0 \leq r, r' < \lvert n \rvert$. Luego, $a - b = n \cdot (q - q') + (r - r')$. Como $a \equiv b\ (mod\ n)$, entonces $n \mid a - b$. Entonces, por _Teorema 2.8_, $n \mid r - r'$. Pero $\lvert r - r'\rvert < n$, por lo tanto se debe dar que $r - r' = n \cdot 0 = 0$. Luego, $r = r'$, es decir, $a$ y $b$ tienen el mismo resto en la división por $n$.

($\Leftarrow$)

Si $a$ y $b$ tienen el mismo resto en la división por $n$, entonces por _Teorema 1.1_, existen $q, q', r \in \mathbb{Z}$ tales que $a = n \cdot q + r$ y $b = n \cdot q' + r$, con $0 \leq r < \lvert n \rvert$. Restando las igualdades se tiene que $a - b = n \cdot (q - q')$. Luego $n \mid a - b$, por lo tanto $a \equiv b\ (mod\ n)$.


# Teorema 10.2

$a \equiv 0\ (mod\ n)$ si y solo si $n \mid a$.

**Demostración**:

($\Rightarrow$)

Si $a \equiv 0\ (mod\ n)$, entonces $n \mid a - 0$, es decir $n \mid a$.

($\Leftarrow$)

Si $n \mid a$, entonces $n \mid a - 0$, es decir $a \equiv 0\ (mod\ n)$.


# Teorema 10.3

$a \equiv a\ (mod\ n)$

**Demostración**:

$n \mid 0$, por lo tanto, $n \mid a - a$. Luego, $a \equiv a\ (mod\ n)$.


# Teorema 10.4

$a \equiv b\ (mod\ n)$ entonces $b \equiv a\ (mod\ n)$.

**Demostración**:

Si $a \equiv b\ (mod\ n)$ entonces $n \mid a - b$. Por lo tanto, $n \mid b - a$. Luego, $b \equiv a\ (mod\ n)$.


# Teorema 10.5

$a \equiv b\ (mod\ n)$ y $b \equiv c\ (mod\ n)$ entonces $a \equiv c\ (mod\ n)$.

**Demostración**:

Si $a \equiv b\ (mod\ n)$ y $b \equiv c\ (mod\ n)$, entonces $n \mid a - b$ y $n \mid b - c$. Por lo tanto, $n \cdot k = a - b$ y $n \cdot k' = b - c$, para algunos $k, k' \in \mathbb{Z}$. Sumando ambas igualdades se tiene que $n \cdot (k + k') = a - c$. Por lo tanto $n \mid a - c$, lo que implica que $a \equiv c\ (mod\ n)$.


# Teorema 10.6

$a \equiv b\ (mod\ n)$ y $c \equiv d\ (mod\ n)$ entonces $a + c \equiv b + d\ (mod\ n)$.

**Demostración**:

$a \equiv b\ (mod\ n)$ y $c \equiv d\ (mod\ n)$ entonces $n \mid a - b$ y $n \mid c - d$. Por _Teorema 2.7_, $n \mid (a + c) - (b + d)$. Luego, $a + c \equiv b + d\ (mod\ n)$.


# Teorema 10.7

$a \equiv b\ (mod\ n)$ y $c \equiv d\ (mod\ n)$ entonces $a \cdot c \equiv b \cdot d\ (mod\ n)$.

**Demostración**:

Si $a \equiv b\ (mod\ n)$ y $c \equiv d\ (mod\ n)$, entonces $n \mid a - b$ y $n \mid c - d$. Luego, existen $k, k' \in \mathbb{Z}$ tales que $n \cdot k = a - b$ y $n \cdot k' = c - d$. Multiplicando la primera igualdad por $c$ se tiene que $n \cdot k \cdot c = a \cdot c - b \cdot c$, entonces $n \cdot k \cdot c + b \cdot c = a \cdot c$. Restando $b \cdot d$ se llega a que $n \cdot k \cdot c + b \cdot (c - d) = a \cdot c - b \cdot d$. Dado que $n$ divide a ambos términos del lado izquierdo de la igualdad, por _Teorema 2.7_, $n \mid a \cdot c - b \cdot d$. Luego, $a \cdot c \equiv b \cdot d\ (mod\ n)$.


# Teorema 10.8

$a \equiv b\ (mod\ n)$, entonces $a + c \equiv b + c\ (mod\ n)$.

**Demostración**:

Si $a \equiv b\ (mod\ n)$, por _Teorema 10.3_, $c \equiv c\ (mod\ n)$. Luego por _Teorema 10.6_, $a + c \equiv b + c\ (mod\ n)$.


# Teorema 10.9

$a \equiv b\ (mod\ n)$, entonces $a \cdot c \equiv b \cdot c\ (mod\ n)$.

**Demostración**:

Si $a \equiv b\ (mod\ n)$, por _Teorema 10.3_, $c \equiv c\ (mod\ n)$. Luego por _Teorema 10.7_, $a \cdot c \equiv b \cdot c\ (mod\ n)$.


# Teorema 10.10

Sea $k \in \mathbb{N}$.

$a \equiv b\ (mod\ n)$, entonces $a^k \equiv b^k\ (mod\ n)$.

**Demostración**:

Si $a \equiv b\ (mod\ n)$, aplicando el _Teorema 10.7_ con la misma congruencia $k - 1$ veces se llega a que $a^k \equiv b^k\ (mod\ n)$.


# Teorema 10.11

$a \equiv b\ (mod\ n)$, entonces $mcd(a, n) = mcd(b, n)$.

**Demostración**:

Sea $d = mcd(b, n)$. Por definición, $d \mid b \wedge d \mid n$. Como $n \mid a - b$, entonces por _Teorema 2.4_, $d \mid a - b$. Luego, por _Teorema 2.8_, $d \mid a$. Por lo tanto $d$ es divisor común de $a$ y $n$.

Sea $d'$ un divisor común de $a$ y $n$. Como $n \mid a - b$, entonces por _Teorema 2.4_, $d' \mid a - b$, y por _Teorema 2.8_, $d' \mid b$. Luego, por ser divisor común de $b$ y $n$, por _Teorema 5.3_, $d' \mid d$. Por lo tanto, por el mismo teorema, $d = mcd(a, n)$.


# Teorema 10.12

$a \equiv b\ (mod\ n_1)$ y $a \equiv c\ (mod\ n_2)$, entonces $b \equiv c\ (mod\ mcd(n_1, n_2))$.

**Demostración**:

Si $a \equiv b\ (mod\ n_1)$ y $a \equiv c\ (mod\ n_2)$, entonces $n_1 \mid a - b$ y $n_2 \mid a - c$. Como $mcd(n_1, n_2)$ es divisor común de $n_1$ y $n_2$, por _Teorema 2.4_, $mcd(n_1, n_2) \mid a - b$ y $mcd(n_1, n_2) \mid a - c$. Por _Teorema 2.7_, $mcd(n_1, n_2) \mid b - c$. Luego, $b \equiv c\ (mod\ mcd(n_1, n_2))$.


# Teorema 10.13

$a \equiv b\ (mod\ n_1)$ y $a \equiv b\ (mod\ n_2)$, entonces $a \equiv b\ (mod\ mcm(n_1, n_2))$.

**Demostración**:

Si $a \equiv b\ (mod\ n_1)$ y $a \equiv b\ (mod\ n_2)$, entonces $n_1 \mid a - b$ y $n_2 \mid a - b$. Luego, por _Teorema 9.13_, $mcm(n_1, n_2) \mid a - b$. Por lo tanto, $a \equiv b\ (mod\ mcm(n_1, n_2))$.


# Teorema 10.14

Sea $c \in \mathbb{Z}$ tal que $mcd(n, c) = 1$.

Si $c \cdot a \equiv c \cdot b\ (mod\ n) \Rightarrow a \equiv b\ (mod\ n)$.

**Demostración**:

Si $c \cdot a \equiv c \cdot b\ (mod\ n)$, entonces $n \mid c \cdot a - c \cdot b$. Por lo tanto, $n \mid c \cdot (a - b)$. Luego, dado que $mcd(n, c) = 1$, por _Teorema 6.4_, $n \mid a - b$. Entonces, $a \equiv b\ (mod\ n)$.


# Teorema 10.15

Sea $p \in \mathbb{N}$ un número primo.

Si $p \nmid c$ y $c \cdot a \equiv c \cdot b\ (mod\ p) \Rightarrow a \equiv b\ (mod\ p)$. 

**Demostración**:

Si $p \nmid c$, entonces por _Teorema 8.1_, $mcd(p, c) = 1$. Entonces, por _Teorema 10.14_, $a \equiv b\ (mod\ p)$. 


# Teorema 10.16

Si $mcd(a, n) = 1$ y $a \cdot b \equiv 0\ (mod\ n) \Rightarrow b \equiv 0\ (mod\ n)$.

**Demostración**:

Si $mcd(a, n) = 1$ y $a \cdot b \equiv 0\ (mod\ n)$, entonces $a \cdot b \equiv a \cdot 0\ (mod\ n)$. Por _Teorema 10.14_, $b \equiv 0\ (mod\ n)$.


# Teorema 10.17

Si $a \cdot b \equiv c \cdot d\ (mod\ n)$ y $mcd(b, n) = 1$ y $b \equiv d\ (mod\ n) \Rightarrow a \equiv c\ (mod\ n)$.

**Demostración**:

Si $b \equiv d\ (mod\ n)$, por _Teorema 10.9_, $c \cdot b \equiv c \cdot d\ (mod\ n)$. Luego, si $a \cdot b \equiv c \cdot d\ (mod\ n)$, por _Teorema 10.4_ y _Teorema 10.5_, $a \cdot b \equiv c \cdot b\ (mod\ n)$. Dado que $mcd(b, n) = 1$, entonces por _Teorema 10.14_, $a \equiv c\ (mod\ n)$.


# Teorema 10.18

Sea $c \in \mathbb{N}$.

$a \equiv b\ (mod\ n) \Rightarrow c \cdot a \equiv c \cdot b\ (mod\ c \cdot n)$.

**Demostración**:

Si $a \equiv b\ (mod\ n)$, entonces $n \mid a - b$. Por _Teorema 2.9_, $c \cdot n \mid c \cdot a - c \cdot b$. Por lo tanto, $c \cdot a \equiv c \cdot b\ (mod\ c \cdot n)$.


# Teorema 10.19

$a \equiv b\ (mod\ n) \wedge m \mid n \Rightarrow a \equiv b\ (mod\ m)$.

**Demostración**:

Si $a \equiv b\ (mod\ n)$, entonces $n \mid a - b$. Por _Teorema 2.4_, $m \mid a - b$. Por lo tanto, $a \equiv b\ (mod\ m)$.


# Teorema 10.20

Sea $d \in \mathbb{N}$ tal que $d \mid a \wedge d \mid b \wedge d \mid n$.

$a \equiv b\ (mod\ n) \Rightarrow \frac{a}{d} \equiv \frac{b}{d}\ (mod\ \frac{n}{d})$.

**Demostración**:

Si $a \equiv b\ (mod\ n)$, entonces $n \mid a - b$. Por _Teorema 2.11_, $\frac{n}{d} \mid \frac{a}{d} - \frac{b}{d}$. Por lo tanto, $\frac{a}{d} \equiv \frac{b}{d}\ (mod\ \frac{n}{d})$.


# Teorema 10.21

Sea $c \in \mathbb{Z}$.

$c \cdot a \equiv c \cdot b\ (mod\ n) \Rightarrow a \equiv b\ (mod\ \frac{n}{mcd(n, c)})$.

**Demostración**:

Si $c \cdot a \equiv c \cdot b\ (mod\ n)$, dado que $mcd(n, c) \mid c$ y $mcd(n, c) \mid n$, por _Teorema 10.20_, $\frac{c}{mcd(n, c)} \cdot a \equiv \frac{c}{mcd(n, c)} \cdot b\ (mod\ \frac{n}{mcd(n, c)})$. Por _Teorema 6.2_, $mcd(\frac{c}{mcd(n, c)}, \frac{n}{mcd(n, c)}) = 1$, entonces por _Teorema 10.14_, $a \equiv b\ (mod\ \frac{n}{mcd(n, c)})$.
