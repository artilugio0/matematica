# Matriz diagonal por bloques


Una matriz cuadrada por bloques $A$ de $p \times p$ bloques es diagonal por bloques si los bloques fuera de la diagonal son matrices nulas:

$$
\forall\ k, l \in \mathbb{N}_p \mid k \neq l: A_{kl} = O
$$

Ejemplo:

$$
D = \left(
\begin{array}{cc|cc|c}
1  & 2  & 0   & 0   & 0  \\
6  & 7  & 0   & 0   & 0  \\ \hline
0  & 0  & 13  & 14  & 0  \\
0  & 0  & 18  & 19  & 0  \\ \hline
0  & 0  & 0   & 0   & 25 \\
\end{array}
\right)
$$

## Tags

- algebra_lineal
- matrices
