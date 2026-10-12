# Matriz aumentada de un sistema de ecuaciones lineales


Sea el sistema de ecuaciones lineales $A \cdot X = Y$, con $A \in \mathbb{K}^{m \times n}$ y $Y \in \mathbb{K}^{m \times 1}$. La matriz aumentada del sistema es la matriz $A' \in \mathbb{K}^{m \times (n+1)}$ tal que:

$$
(A')_{ij} =
\begin{cases}
(A)_{ij} &1 \leq j \leq n \\
(Y)_{i1} &j = n + 1 \\
\end{cases}
$$

## Tags

- algebra_lineal
- sistema_ecuaciones_lineales
