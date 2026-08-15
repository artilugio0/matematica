# Teorema 12.1


Sea $R = \{r_1, r_2,\ ...\ r_k\}$ un sistema reducido de residuos módulo $n$, y $a \in \mathbb{Z}$ tal que $mcd(a, n) = 1$.

El conjunto $R' = \{a \cdot r_i \mid 1 \leq i \leq k\}$ es un sistema reducido de residuos módulo $n$.

**Demostración**:

Sea $a \cdot r_i \in R'$, por hipótesis $mcd(a, n) = 1$ y por definición $mcd(r_i, n) = 1$, entonces por _Teorema 6.5_, $mcd(a \cdot r_i, n) = 1$.

Dado que $mcd(a, n) = 1$, por _Teorema 11.2_, existe $x \in \mathbb{Z}$ tal que $a \cdot x \equiv 1\ (mod\ n)$. Entonces $x \cdot a - n \cdot d = 1$ para algún $d \in \mathbb{Z}$, y por _Teorema 6.1_, $mcd(x, n) = 1$. Sea $c \in \mathbb{Z}$ tal que $mcd(c, n) = 1$. Por _Teorema 6.5_, $mcd(x \cdot c, n) = 1$, por lo tanto hay un $r_j \in R$ tal que $r_j \equiv x \cdot c\ (mod\ n)$. Y por lo tanto por _Teorema 10.5_ y _Teorema 10.9_, $a \cdot r_j \equiv a \cdot x \cdot c \equiv c\ (mod\ n)$. Entonces para todo $c \in \mathbb{Z}$ tal que $mcd(c, n) = 1$ existe un $a \cdot r_j \in R'$ cumpliendo la segunda condición de un sistema reducido de residuos módulo $n$.

Sean $a \cdot r_\alpha, a \cdot r_\beta \in R'$ tales que $a \cdot r_\alpha \equiv a \cdot r_\beta\ (mod\ n)$, por _Teorema 10.14_, $r_\alpha \equiv r_\beta\ (mod\ n)$. Como $r_\alpha, r_\beta \in R$, entonces $r_\alpha = r_\beta$, y por lo tanto $a \cdot r_\alpha = a \cdot r_\beta$, cumpliendo la tercera propiedad.

Por lo tanto $R'$ es un sistema reducido de residuos módulo $n$.
