# Matriz triangular por bloques


Una matriz cuadrada por bloques $A$ de $p \times p$ bloques es triangular superior por bloques si los bloques debajo de los bloques de la diagonal son matrices nulas:

$$
\forall\ k, l \in \mathbb{N}_p \mid k > l: A_{kl} = N
$$

Una matriz cuadrada por bloques $A$ de $p \times p$ bloques es triangular inferior por bloques si los bloques sobre los bloques de la diagonal son matrices nulas:

$$
\forall\ k, l \in \mathbb{N}_p \mid k < l: A_{kl} = N
$$

Ejemplo:

$$
U = \left(
\begin{array}{cc|cc|c}
1  & 2  & 3   & 4   & 5  \\
6  & 7  & 8   & 9   & 10 \\ \hline
0  & 0  & 13  & 14  & 15 \\
0  & 0  & 18  & 19  & 20 \\ \hline
0  & 0  & 0   & 0   & 25 \\
\end{array}
\right)
$$

$$
L = \left(
\begin{array}{cc|cc|c}
1  & 2  & 0  & 0  & 0  \\
6  & 7  & 0  & 0  & 0  \\ \hline
11 & 12 & 13 & 14 & 0  \\
16 & 17 & 18 & 19 & 0  \\ \hline
21 & 22 & 23 & 24 & 25 \\
\end{array}
\right)
$$
