Sea $n \in \mathbb{N}$.

# Clases de congruencia módulo $n$

Sea $\sim$ la relación binaria definida sobre $\mathbb{Z}$:

$a \sim b \Leftrightarrow a \equiv b\ (mod\ n)$

Por _Teorema 10.3_, _Teorema 10.4_ y _Teorema 10.5_, $\sim$ es una relación de equivalencia.

Sea $a \in \mathbb{Z}$, se llama **clase de congruencia de $a$ módulo $n$** al conjunto

$$
\overline{a} = \{b \in \mathbb{Z} \mid a \sim b\} = \{b \in \mathbb{Z} \mid a \equiv b\ (mod\ n)\}
$$

Y el conjunto de todas las clases de equivalencia es
$$
\mathbb{Z}/n\mathbb{Z} = \{\overline{a} \mid a \in \mathbb{Z}\}
$$


# Sistema completo de residuos módulo $n$

Es un conjunto de $n$ elementos de $\mathbb{Z}$ tal que no haya dos elementos congruentes módulo $n$.

$R$ es un sistema completo de residuos módulo $n$ $\Leftrightarrow \lvert R \rvert = n \wedge \forall\ a,b \in R: a \equiv b\ (mod\ n) \Rightarrow a = b$.


# Sistema reducido de residuos módulo $n$

Un sistema reducido de residuos módulo $n$ es un conjunto cuyos elementos son coprimos con $n$ y no congruentes módulo $n$ entre sí, y para todo entero coprimo con $n$ existe un elemento en el conjunto que es congruente a él módulo $n$.

$R$ es un sistema reducido de residuos módulo $n$ si:

- $\forall\ a \in R: mcd(a, n) = 1$
- $\forall\ c \in \mathbb{Z}$ tal que $mcd(c, n) = 1: \exists\ a \in R \mid a \equiv c\ (mod\ n)$
- $\forall\ a, b \in R: a \equiv b\ (mod\ n) \Rightarrow a = b$


# Teorema 12.1

Sea $R = \{r_1, r_2,\ ...\ r_k\}$ un sistema reducido de residuos módulo $n$, y $a \in \mathbb{Z}$ tal que $mcd(a, n) = 1$.

El conjunto $R' = \{a \cdot r_i \mid 1 \leq i \leq k\}$ es un sistema reducido de residuos módulo $n$.

**Demostración**:

Sea $a \cdot r_i \in R'$, por hipótesis $mcd(a, n) = 1$ y por definición $mcd(r_i, n) = 1$, entonces por _Teorema 6.5_, $mcd(a \cdot r_i, n) = 1$.

Dado que $mcd(a, n) = 1$, por _Teorema 11.2_, existe $x \in \mathbb{Z}$ tal que $a \cdot x \equiv 1\ (mod\ n)$. Entonces $x \cdot a - n \cdot d = 1$ para algún $d \in \mathbb{Z}$, y por _Teorema 6.1_, $mcd(x, n) = 1$. Sea $c \in \mathbb{Z}$ tal que $mcd(c, n) = 1$. Por _Teorema 6.5_, $mcd(x \cdot c, n) = 1$, por lo tanto hay un $r_j \in R$ tal que $r_j \equiv x \cdot c\ (mod\ n)$. Y por lo tanto por _Teorema 10.5_ y _Teorema 10.9_, $a \cdot r_j \equiv a \cdot x \cdot c \equiv c\ (mod\ n)$. Entonces para todo $c \in \mathbb{Z}$ tal que $mcd(c, n) = 1$ existe un $a \cdot r_j \in R'$ cumpliendo la segunda condición de un sistema reducido de residuos módulo $n$.

Sean $a \cdot r_\alpha, a \cdot r_\beta \in R'$ tales que $a \cdot r_\alpha \equiv a \cdot r_\beta\ (mod\ n)$, por _Teorema 10.14_, $r_\alpha \equiv r_\beta\ (mod\ n)$. Como $r_\alpha, r_\beta \in R$, entonces $r_\alpha = r_\beta$, y por lo tanto $a \cdot r_\alpha = a \cdot r_\beta$, cumpliendo la tercera propiedad.

Por lo tanto $R'$ es un sistema reducido de residuos módulo $n$.


# Teorema 12.2

Pequeño teorema de Fermat

Sea $p \in \mathbb{N}$ un número primo y $a \in \mathbb{Z}$ un número no divisible por $p$.

$a^{p-1} \equiv 1\ (mod\ p)$

**Demostración**:

Sea el conjunto $R = \{1, 2,\ ...\ , p-2, p-1\}$. Como sus elementos son enteros positivos menores a $p$, ninguno es divisible por $p$, y por _Teorema 8.1_, todos son coprimos con $p$. También todos son incongruentes entre sí módulo $p$, dado que son posibles restos distintos de la división por $p$. Y dado cualquier $c \in \mathbb{Z}$, si $mcd(c, p) = 1$ entonces $p \nmid c$, por lo tanto su resto en la división por $p$ es uno de los elementos de $R$, es decir, $c$ es congruente con uno de los elementos de $R$. Por lo tanto, $R$ es un sistema reducido de residuos módulo $p$.

Como $p \nmid a$, por _Teorema 8.1_, $mcd(a, p) = 1$. Entonces, multiplicando todos los elementos de $R$ por $a$, por _Teorema 12.1_, se obtiene un nuevo conjunto que también es un sistema reducido de residuos módulo $p$: $R' = \{1 \cdot a, 2 \cdot a,\ ...\ , (p-1) \cdot a\}$. Por ser $R$ y $R'$ sistemas reducidos de residuos módulo $p$, sus elementos son coprimos con $p$, y por lo tanto, todo elemento de $R'$ es congruente con uno de $R$ y todo elemento de $R$ es congruente con uno de $R'$. Y como dentro de cada conjunto los elementos son incongruentes entre si, la relación entre los elementos de $R$ y $R'$ es uno a uno. Es decir, se tienen las siguiente congruencias:

$$
\begin{aligned}
&1 \cdot a \equiv r_1\ (mod\ p) \\
&2 \cdot a \equiv r_2\ (mod\ p) \\
&... \\
&(p-1) \cdot a \equiv r_{p-1}\ (mod\ p) \\
\end{aligned}
$$

Donde cada $r_i \in R$, y $r_i \neq r_j$ si $i \neq j$, para $1 \leq i \leq p-1$.

Luego, por _Teorema 10.7_, multiplicando las congruencias se tiene que $1 \cdot 2 \cdot\ ...\ \cdot (p-1) \cdot a^{p-1} \equiv r_1 \cdot r_2 \cdot\ ...\ \cdot r_{p-1}\ (mod\ p)$. Como el producto de los $r_i$ es el producto de los primeros $p-1$ enteros positivos, su producto es $(p-1)!$, entonces se obtiene que $(p-1)! \cdot a^{p-1} \equiv (p-1)!\ (mod\ p)$. Y dado que $p$ no divide a ninguno de los factores de $(p-1)!$ por ser menores que $p$, entonces por _Teorema 8.2_, $p \nmid (p-1)!$. Finalmente, por _Teorema 10.15_, $a^{p-1} \equiv 1\ (mod\ p)$.


# Teorema 12.3

Sea $p \in \mathbb{N}$ un número primo y $a \in \mathbb{Z}$.

$a^p \equiv a\ (mod\ p)$

**Demostración**:

TODO


# Teorema 12.4

Sea $n \in \mathbb{N}$ y $a, r \in \mathbb{Z}$ con $a$ no divisible por $p$ y $r \geq 0$.

$n \equiv r\ (mod\ p-1) \Rightarrow a^n \equiv a^r\ (mod\ p)$

**Desmostración**:

TODO

(verificar si todas las hipotesis son necesarias)
