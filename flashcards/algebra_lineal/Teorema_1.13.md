# Teorema 1.13


- Sean $A \in \mathbb{K}^{m \times n}$ y $B, C \in \mathbb{K}^{n \times p}$

  $A \cdot (B + C) = A \cdot B + A \cdot C$


- Sean $A, B \in \mathbb{K}^{m \times n}$ y $C \in \mathbb{K}^{n \times p}$

  $(A + B) \cdot C = A \cdot C + B \cdot C$

**Demostración**:

$$
\begin{aligned}
(A \cdot (B + C))_{ij} &= \sum\limits_{k = 1}^{n} (A)_{ik} \cdot (B + C)_{kj} \\
                       &= \sum\limits_{k = 1}^{n} (A)_{ik} \cdot ((B)_{kj} + (C)_{kj}) \\
                       &= \sum\limits_{k = 1}^{n} ((A)_{ik} \cdot (B)_{kj} + (A)_{ik} \cdot (C)_{kj}) \\
                       &= \sum\limits_{k = 1}^{n} (A)_{ik} \cdot (B)_{kj} + \sum\limits_{k = 1}^{n} (A)_{ik} \cdot (C)_{kj} \\
                       &= (A \cdot B)_{ij} + (A \cdot C)_{ij} \\
                       &= (A \cdot B + A \cdot C)_{ij} \\
\end{aligned}
$$

Por lo tanto, $A \cdot (B + C) = A \cdot B + A \cdot C$.

$$
\begin{aligned}
((A + B) \cdot C)_{ij} &= \sum\limits_{k = 1}^{n} (A + B)_{ik} \cdot (C)_{kj} \\
                      &= \sum\limits_{k = 1}^{n} ((A)_{ik} + (B)_{ik}) \cdot (C)_{kj} \\
                      &= \sum\limits_{k = 1}^{n} ((A)_{ik} \cdot (C)_{kj} + (B)_{ik} \cdot (C)_{kj}) \\
                      &= \sum\limits_{k = 1}^{n} (A)_{ik} \cdot (C)_{kj} + \sum\limits_{k = 1}^{n} (B)_{ik} \cdot (C)_{kj} \\
                      &= (A \cdot C)_{ij} + (B \cdot C)_{ij} \\
                      &= (A \cdot C + B \cdot C)_{ij} \\
\end{aligned}
$$

Por lo tanto, $(A + B) \cdot C = A \cdot C + B \cdot C$.
