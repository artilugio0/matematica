# Teorema 8.3


Sea $p \in \mathbb{Z}$ un número primo. Si $p \mid q_1 \cdot q_2 \cdot\ ...\cdot\ q_n$, donde cada $q_i$ es primo, entonces $p = \pm q_m$ con $1 \leq m \leq n$.

**Demostración**:

Se demuestra por inducción sobre $n$. Si $p \mid q_1$, entonces $p = \pm 1 \lor p = \pm q_1$. Pero $p$ no puede ser $\pm 1$ porque es primo. Entonces $p = \pm q_1$.

Se asume que se cumple para $n = k$, y $p \mid q_1 \cdot q_2 \cdot\ ...\cdot\ q_k \cdot q_{k+1}$, con $q_i$ primos. Si $p \mid q_1$, por el caso demostrado anteriormente, $p = \pm q_1$. Sino, por _Teorema 8.2_, $p \mid q_2 \cdot q_3 \cdot\ ...\ \cdot q_k \cdot q_{k+1}$. Luego, como $p$ divide un producto de $k$ factores, por la hipótesis inductiva $p = \pm q_m$ para $2 \leq m \leq k + 1$.

Por lo tanto queda demostrado para todo $n \in \mathbb{N}$.
