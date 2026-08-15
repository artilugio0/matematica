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
