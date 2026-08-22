# Teorema 1.25


Sean $A \in \mathbb{K}^{m \times n}$ una matriz de $p \times q$ bloques, donde cada bloque es $A_{kl} \in \mathbb{K}^{m_k \times n_l}$, y $B \in \mathbb{K}^{n \times r}$ una matriz de $q \times s$ bloques donde cada bloque es $B_{lt} \in \mathbb{K}^{n_l \times r_t}$.

Si $C = A \cdot B$, entonces $C$ es una matriz de $p \times s$ bloques donde cada bloque $C_{kt} = \sum\limits_{l = 1}^{q} A_{kl} \cdot B_{lt} \in \mathbb{K}^{m_k \times r_t}$.

**Demostración**:

Sean $M_k = \sum\limits_{a = 1}^{k} m_a$, $N_l = \sum\limits_{a = 1}^{l} n_a$, $R_t = \sum\limits_{a = 1}^{t} r_a$. Por su definición $M_0 = N_0 = R_0 = 0$ y también $M_p = m$, $N_q = n$ y $R_s = r$.

Dados $i \in \mathbb{N}_m$ y $j \in \mathbb{N}_r$, ambos enteros pueden expresarse de manera única en términos de $M_{k-1}$ y $R_{t-1}$ como $i = M_{k-1} + i'$ y $j = R_{t-1} + j'$, para $1 \leq k \leq p,\ 1 \leq i' \leq m_k$ y $1 \leq t \leq s,\ 1 \leq j' \leq r_t$.

Luego desarrollando $(C)_{ij}$, se obtiene:

$$
\begin{aligned}
(C)_{ij} &= \sum\limits_{x = 1}^{n} (A)_{ix} \cdot (B)_{xj} \\
         &= \sum\limits_{x = N_0 + 1}^{N_1} (A)_{ix} \cdot (B)_{xj} + \sum\limits_{x = N_1 + 1}^{N_2} (A)_{ix} \cdot (B)_{xj} +\ \dots\ + \sum\limits_{x = N_{q - 1} + 1}^{N_q} (A)_{ix} \cdot (B)_{xj} \\
         &= \sum\limits_{x = N_0 + 1}^{N_1} (A)_{(M_{k-1} + i') x} \cdot (B)_{x (R_{t - 1} + j')} + \sum\limits_{x = N_1 + 1}^{N_2} (A)_{(M_{k-1} + i') x} \cdot (B)_{x (R_{t - 1} + j')} +\ \dots\ + \sum\limits_{x = N_{q - 1} + 1}^{N_q} (A)_{(M_{k-1} + i') x} \cdot (B)_{x (R_{t - 1} + j')} \\
         &= (A_{k1} \cdot B_{1t})_{i'j'} + (A_{k2} \cdot B_{2t})_{i'j'} +\ \dots\ + (A_{kq} \cdot B_{qt})_{i'j'} \\
         &= \sum\limits_{l = 1}^{q} (A_{kl} \cdot B_{lt})_{i'j'} \\
         &= \left(\sum\limits_{l = 1}^{q} A_{kl} \cdot B_{lt} \right)_{i'j'} \\
         &= (C_{kt})_{i'j'} \\
\end{aligned}
$$

Cada paso se justifica de la siguiente forma:

1. Definición de producto de matrices
2. División de la sumatoria por límites coincidentes
3. Reemplazo de $i$ y $j$ de acuerdo a su expresión en términos de $M_{k-1}$ y $R_{t-1}$
4. Definición de bloques de $A$ y $B$, y producto de submatrices $A_{kl}$ y $B_{lt}$, para cada $l$ tal que $1 \leq l \leq q$
5. Simplificación de la expresión usando sumatoria
6. Definición del término $i'j'$ de la suma de matrices
7. Definición de $C_{kt}$

Por lo tanto, por definición de matriz por bloques, $C$ es una matriz de $p \times s$ bloques donde cada bloque $C_{kt} = \sum\limits_{l = 1}^{q} A_{kl} \cdot B_{lt} \in \mathbb{K}^{m_k \times r_t}$.
