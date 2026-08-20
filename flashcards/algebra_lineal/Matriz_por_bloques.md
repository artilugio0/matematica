# Matriz por bloques


Sea $A \in \mathbb{K}^{m \times n}$.

Sean $p, q \in \mathbb{N}$ y $m_1,\ \dots\ , m_p \in \mathbb{N}$, $n_1,\ \dots\ , n_q \in \mathbb{N}$ tales que $\sum\limits_{r = 1}^{p} m_r = m$ y $\sum\limits_{r = 1}^{q} n_r = n$.

Se definen $M_k = \sum\limits_{r = 1}^{k} m_r$ y $N_l = \sum\limits_{r = 1}^{l} n_r$ (nótese que $M_0 = N_0 = 0$).

Se define el bloque $A_{kl} \in \mathbb{K}^{m_k \times n_l}$, con $1 \leq k \leq p$ y $1 \leq l \leq q$, como la submatriz de $A$ tal que $(A_{kl})_{ij} = (A)_{(M_{k-1} + i) (N_{l-1}+j)}$, para $1 \leq i \leq m_k$ y $1 \leq j \leq n_l$.

Una matriz por bloques de $A$ es una representación de $A$ de la forma:

$$
A = \begin{pmatrix}
A_{11} & A_{12} & \dots & A_{1q} \\
A_{21} & A_{22} & \dots & A_{2q} \\
\vdots & \vdots & \ddots & \vdots \\
A_{p1} & A_{p2} & \dots & A_{pq}
\end{pmatrix}
$$

En esta representación los bloques que comparten fila tienen la misma cantidad de filas y los que comparten columna tienen la misma cantidad de columnas.

Ejemplo:

Sea $A \in \mathbb{K}^{3 \times 4}$ tal que

$$
A = \left(
\begin{array}{cc|c|c}
1 &  2 &  3 & 4 \\
5 &  6 &  7 & 8 \\ \hline
9 & 10 & 11 & 12
\end{array}
\right)
$$

Con $p = 2, q = 3, m_1 = 2, m_2 = 1$, y $n_1 = 2, n_2 = 1, n_3 = 1$. Los bloques son:

$$
A_{11} = \begin{pmatrix}
1 &  2 \\
5 &  6 \\
\end{pmatrix}
\qquad
A_{12} = \begin{pmatrix}
3 \\
7 \\
\end{pmatrix}
\qquad
A_{13} = \begin{pmatrix}
4 \\
8 \\
\end{pmatrix}
$$

$$
A_{21} = \begin{pmatrix}
9 &  10 \\
\end{pmatrix}
\qquad
A_{22} = \begin{pmatrix}
11 \\
\end{pmatrix}
\qquad
A_{23} = \begin{pmatrix}
12 \\
\end{pmatrix}
$$
