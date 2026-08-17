# Teorema 1.14


Sean $A \in \mathbb{K}^{m \times n},\ B \in \mathbb{K}^{n \times p}$, y $\lambda \in \mathbb{K}$.

$(\lambda \cdot A) \cdot B = \lambda \cdot (A \cdot B) = A \cdot (\lambda \cdot B)$

**Demostración**:

$$
\begin{aligned}
((\lambda \cdot A) \cdot B)_{ij} &= \sum\limits_{k = 1}^{n} (\lambda \cdot A)_{ik} \cdot (B)_{kj} \\
                           &= \sum\limits_{k = 1}^{n} (\lambda \cdot (A)_{ik}) \cdot (B)_{kj} \\
                           &= \sum\limits_{k = 1}^{n} \lambda \cdot ((A)_{ik} \cdot (B)_{kj}) \\
                           &= \lambda \cdot \sum\limits_{k = 1}^{n} (A)_{ik} \cdot (B)_{kj} \\
                           &= \lambda \cdot (A \cdot B)_{ij} \\
                           &= (\lambda \cdot (A \cdot B))_{ij} \\
\end{aligned}
$$

Por lo tanto, $(\lambda \cdot A) \cdot B = \lambda \cdot (A \cdot B)$.

$$
\begin{aligned}
((\lambda \cdot A) \cdot B)_{ij} &= \sum\limits_{k = 1}^{n} (\lambda \cdot A)_{ik} \cdot (B)_{kj} \\
                           &= \sum\limits_{k = 1}^{n} (\lambda \cdot (A)_{ik}) \cdot (B)_{kj} \\
                           &= \sum\limits_{k = 1}^{n} ((A)_{ik} \cdot \lambda) \cdot (B)_{kj} \\
                           &= \sum\limits_{k = 1}^{n} (A)_{ik} \cdot (\lambda \cdot (B)_{kj}) \\
                           &= \sum\limits_{k = 1}^{n} (A)_{ik} \cdot (\lambda \cdot B)_{kj} \\
                           &= (A \cdot (\lambda \cdot B))_{ij}
\end{aligned}
$$

Por lo tanto, $(\lambda \cdot A) \cdot B = A \cdot (\lambda \cdot B)$.

Luego, $(\lambda \cdot A) \cdot B = \lambda \cdot (A \cdot B) = A \cdot (\lambda \cdot B)$.
