# Teorema 1.11


Sean $A \in \mathbb{K}^{m \times n}, B \in \mathbb{K}^{n \times p}, C \in \mathbb{K}^{p \times q}$.

$(A \cdot B) \cdot C = A \cdot (B \cdot C)$

**Demostración**:

$$
\begin{aligned}
((A \cdot B) \cdot C)_{ij} &= \sum\limits_{k = 1}^p (A \cdot B)_{ik} \cdot (C)_{kj} \\
                           &= \sum\limits_{k = 1}^p (\sum\limits_{l = 1}^{n} (A)_{il} \cdot (B)_{lk}) \cdot (C)_{kj} \\
                           &= \sum\limits_{k = 1}^p (\sum\limits_{l = 1}^{n} (A)_{il} \cdot (B)_{lk} \cdot (C)_{kj}) \\
                           &= \sum\limits_{l = 1}^{n}(\sum\limits_{k = 1}^p (A)_{il} \cdot (B)_{lk} \cdot (C)_{kj}) \\
                           &= \sum\limits_{l = 1}^{n} ((A)_{il} \cdot \sum\limits_{k = 1}^p (B)_{lk} \cdot (C)_{kj}) \\
                           &= \sum\limits_{l = 1}^{n} ((A)_{il} \cdot (B \cdot C)_{lj}) \\
                           &= (A \cdot (B \cdot C))_{ij}
\end{aligned}
$$

Por lo tanto, $(A \cdot B) \cdot C = A \cdot (B \cdot C)$.
