# Teorema 1.17


Sean $A \in \mathbb{K}^{m \times n},\ B \in \mathbb{K}^{n \times p}$.

$(A \cdot B)^T = B^T \cdot A^T$

**Demostración**:

Sean $i \in \mathbb{N}_p,\ j \in \mathbb{N}_m$.

$$
\begin{aligned}
((A \cdot B)^T)_{ij} &= (A \cdot B)_{ji} \\
                     &= \sum\limits_{k = 1}^{n} (A)_{jk} \cdot (B)_{ki} \\
                     &= \sum\limits_{k = 1}^{n} (A^T)_{kj} \cdot (B^T)_{ik} \\
                     &= \sum\limits_{k = 1}^{n} (B^T)_{ik} \cdot (A^T)_{kj} \\
                     &= (B^T \cdot A^T)_{ij}
\end{aligned}
$$

Por lo tanto, $(A \cdot B)^T = B^T \cdot A^T$.
