# Teorema 3.6


Para $a, b \in \mathbb{Z}$, no ambos nulos: $mcd(a, b) = mcd(a, b + a \cdot k)$, para $k \in \mathbb{Z}$.

**Demostración**:

Sea $d = mcd(a, b + a \cdot k)$.

Por definición, $d \mid a$, y por _Teorema 2.3_, $d \mid a \cdot k$.

Por definición, $d \mid (b + a \cdot k)$. Y como $d \mid a \cdot k$, Por _Teorema 2.8_, $d \mid b$.

Por lo tanto, $d$ es divisor común de $a$ y $b$.

Sea $d'$ un divisor común de $a$ y $b$. Por _Teorema 2.7_, $d' \mid (b + a \cdot k)$. Por lo tanto, $d'$ es un divisor común de $a$ y $b + a \cdot k$. Como $d = mcd(a, b + a \cdot k)$, se tiene que $d' \leq d$. Por lo tanto $d$ es mayor o igual a cualquier otro divisor de $a$, $b$. Lo que implica que $d = mcd(a, b)$.
