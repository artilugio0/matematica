# Teorema 5.7


Sean $V$ un espacio vectorial y $S_1,\ \dots\ , S_k$ subespacios vectoriales de $V$.

$S_1 +\ \dots\ + S_k = \langle S_1 \cup\ \dots\ \cup S_k \rangle$.

**Demostración**:

Sea $s_1 +\ \dots\ + s_k \in (S_1 +\ \dots\ + S_k)$. Como $s_1,\ \dots, s_k \in (S_1 \cup\ \dots\ \cup S_k)$, y $s_1 +\ \dots\ + s_k$ es una combinación lineal de $(S_1 \cup\ \dots\ \cup S_k)$, entonces $s_1 +\ \dots\ + s_k \in \langle S_1 \cup\ \dots\ \cup S_k \rangle$, y $(S_1 +\ \dots\ + S_k) \subseteq \langle S_1 \cup\ \dots\ \cup S_k \rangle$.

Sea $s \in \langle S_1 \cup\ \dots\ \cup S_k \rangle$, $s$ es una combinación lineal de los vectores de $S_1 \cup\ \dots\ \cup S_k$. Por la propiedad conmutativa, $s$ puede expresarse como $s = \sum\limits_{i \in I_1} \alpha_{1_i} \cdot s_{1_i} +\ \dots\ + \sum\limits_{i \in I_k} \alpha_{k_i} \cdot s_{k_i}$. Como $\sum\limits_{i \in I_j} \alpha_{j_i} \cdot s_{j_i} \in S_j$, entonces $s \in (S_1 +\ \dots\ + S_k)$, y $\langle S_1 \cup\ \dots\ \cup S_k \rangle \subseteq (S_1 +\ \dots\ + S_k)$.

Por lo tanto, $S_1 +\ \dots\ + S_k = \langle S_1 \cup\ \dots\ \cup S_k \rangle$.

## Tags

- algebra_lineal
- subespacios
- teorema
