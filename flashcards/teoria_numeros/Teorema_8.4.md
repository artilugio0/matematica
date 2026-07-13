# Teorema 8.4


Si $a \in \mathbb{Z}$ con $\lvert a \rvert > 1$, su mínimo divisor mayor a 1 es primo.

**Demostración**:

Si $a$ es primo, por definición su mínimo divisor mayor a $1$ es $\lvert a \rvert$, que es primo.

Si $a$ no es primo, entonces sea $D$ el conjunto de divisores de $a$ mayores a $1$. El conjunto no está vacío, dado que $\lvert a \rvert \in D$. Por lo tanto, tiene un mínimo. Sea $p_1 = min\ D$, $p_1$ debe ser primo, porque si hubiera un divisor de $p_1$ distinto de $1$ y $p_1$, entonces por _Teorema 2.4_ también dividiría a $a$, y por lo tanto por _Teorema 2.6_ habría un divisor de $a$ mayor a $1$ y menor a $p_1$, lo cual es un absurdo. Por lo tanto su mínimo divisor mayor a $1$ debe ser primo.
