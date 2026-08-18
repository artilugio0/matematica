# Teorema 1.21


Sean $A, B \in \mathbb{K}^{n \times n}$.

$\operatorname{tr}(A \cdot B) = \operatorname{tr}(B \cdot A)$

**Demostración**:

$$
\begin{aligned}
\operatorname{tr}(A \cdot B) &= \sum\limits_{i = 1}^{n} (A \cdot B)_{ii} \\
                             &= \sum\limits_{i = 1}^{n} (\sum\limits_{k = 1}^{n} (A)_{ik} \cdot (B)_{ki}) \\
                             &= \sum\limits_{k = 1}^{n} (\sum\limits_{i = 1}^{n} (A)_{ik} \cdot (B)_{ki}) \\
                             &= \sum\limits_{k = 1}^{n} (\sum\limits_{i = 1}^{n} (B)_{ki} \cdot (A)_{ik}) \\
                             &= \sum\limits_{k = 1}^{n} (B \cdot A)_{kk} \\
                             &= \operatorname{tr}(B \cdot A) \\
\end{aligned}
$$
