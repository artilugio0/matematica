# Teorema 1.12


Sea $A \in \mathbb{K}^{m \times n}$.

$I_m \cdot A = A \cdot I_n = A$

**Demostración**:

$$
\begin{aligned}
(I_m \cdot A)_{ij} &= \sum\limits_{k = 1}^{m} (I_m)_{ik} \cdot (A)_{kj} \\
                   &= (I_m)_{ii} \cdot (A)_{ij} \\
                   &= 1 \cdot (A)_{ij} \\
                   &= (A)_{ij} \\
\end{aligned}
$$

La segunda igualdad se da porque $(I_m)_{ik}$ es $0$ cuando $i \neq k$.

De igual forma,

$$
\begin{aligned}
(A \cdot I_n)_{ij} &= \sum\limits_{k = 1}^n (A)_{ik} \cdot (I_n)_{kj} \\
                   &= (A)_{ij} \cdot (I_n)_{jj} \\
                   &= (A)_{ij} \cdot 1 \\
                   &= (A)_{ij} \\
\end{aligned}
$$

Por lo tanto, $I_m \cdot A = A \cdot I_n = A$.
