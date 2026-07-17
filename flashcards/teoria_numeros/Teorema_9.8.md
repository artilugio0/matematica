# Teorema 9.8


Sean $a, b \in \mathbb{N}$.

El mínimo común múltiplo de $a$ y $b$ es el producto de los factores primos de $a$ y $b$ elevados a la mayor potencia con la que aparecen en las respectivas representaciones canónicas.

**Demostración**:

Sea $m = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot\ ...\ \cdot p_n^{\alpha_n}$ tal que $p_i$ es un divisor primo de $a$ o de $b$, y $\alpha_i$ es la mayor potencia de $p_i$ tal que $p_i^{\alpha_i}$ divida a $a$ o $b$.

Por _Teorema 8.9_, $a \mid m \wedge b \mid m$.

Sea $m'$ un múltiplo común de $a$ y $b$. Por definición, $p_i^{\alpha_i} \mid a \lor p_i^{\alpha_i} \mid b$. Entonces, por _Teorema 2.4_, $p_i^{\alpha_i} \mid m'$. Y como $mcd(p_i^{\alpha_i}, p_j^{\alpha_j}) = 1$ para $i \neq j$, entonces por _Teorema 6.3_, $p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot\ ...\ \cdot p_n^{\alpha_n} \mid m'$. Por lo tanto $m \mid m'$. Luego, por _Teorema 9.5_, $mcm(a, b) = m$.
