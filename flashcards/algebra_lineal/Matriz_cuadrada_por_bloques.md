# Matriz cuadrada por bloques


Una matriz por bloques $A \in \mathbb{K}^{m \times n}$ de $p \times q$ bloques es cuadrada por bloques si, siendo cada bloque $A_{kl} \in \mathbb{K}^{m_k \times n_l}$, se cumple que:

- $A$ es una matriz cuadrada: $m = n$
- $A$ tiene la misma cantidad de filas de bloques que de columnas de bloques: $p = q$
- Los bloques en la diagonal principal son cuadrados: $\forall\ k \in \mathbb{N}_p:\ m_k = n_k$

Ejemplo:

$$
A = \left(
\begin{array}{cc|cc|c}
1   & 2   & 3   & 4   & 5  \\
6   & 7   & 8   & 9   & 10 \\ \hline
11  & 12  & 13  & 14  & 15 \\
16  & 17  & 18  & 19  & 20 \\ \hline
21  & 22  & 23  & 24  & 25 \\
\end{array}
\right)
$$
