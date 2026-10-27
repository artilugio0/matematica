# Teorema 5.6


Sean $V$ un espacio vectorial y $S_1,\ \dots\ , S_k$ subespacios vectoriales de $V$.

$S_1 +\ \dots\ + S_k$ es un subespacio vectorial de $V$.

**Demostración**:

$o$ pertenece a $S_1,\ \dots\, S_k$, entonces $\sum\limits_{i = 1}^k o = o \in (S_1 +\ \dots\ + S_k)$. Por lo tanto $S_1 +\ \dots\ + S_k \neq \emptyset$.

Sean $s, t \in (S_1 +\ \dots\ + S_k)$. Entonces $s = s_1 +\ \dots\ + s_k$ y $t = t_1 +\ \dots\ + t_k$, con $s_i, t_i \in S_i$.

Sea $\alpha \in \mathbb{K}$,

$$
\begin{aligned}
\alpha \cdot s + t &= \alpha \cdot (s_1 +\ \dots\ + s_k) + t_1 +\ \dots\ + t_k \\
&= \alpha \cdot s_1 +\ \dots\ + \alpha \cdot s_k + t_1 +\ \dots\ + t_k \\
&= (\alpha \cdot s_1 + t_1) +\ \dots\ + (\alpha \cdot s_k + t_k) \\
\end{aligned}
$$

Como $\alpha \cdot s_i + t_i \in S_i$, entonces $\alpha \cdot s + t \in S_1 +\ \dots\ + S_k$. Por _Teorema 5.2_, $S_1 +\ \dots\ + S_k$ es subespacio vectorial de $V$.

## Tags

- algebra_lineal
- subespacios
- teorema
