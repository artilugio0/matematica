# Teorema 6.9


Sea $V$ un espacio vectorial de dimensión $n$.

Si $U \subseteq V$ es linealmente independiente y tiene $n$ elementos, entonces $U$ es una base de $V$.

**Demostración**:

Sean $u_1,\ \dots\ , u_n \in U$ vectores distintos y linealmente independientes, y sea $B = \{b_1,\ \dots\ , b_n\}$ una base de $V$.

Dado que $B$ es una base de $V$, los vectores $u_1,\ \dots\ , u_n$ pueden expresarse como combinaciones lineales de los vectores de $B$ como $u_j = \alpha_{1j} \cdot b_1 +\ \dots\ + \alpha_{nj} \cdot b_n$, con $1 \leq j \leq n$.

Entonces, toda combinación lineal de $U$ puede expresarse como:

$$
\begin{aligned}
x_1 \cdot u_1 +\ \dots\ + x_n \cdot u_n &= x_1 \cdot (\alpha_{11} \cdot b_1 +\ \dots\ + \alpha_{n1} \cdot b_n) +\ \dots\ + x_n \cdot (\alpha_{1n} \cdot b_1 +\ \dots\ + \alpha_{nn} \cdot b_n) \\
&= (x_1 \cdot \alpha_{11} +\ \dots\ + x_n \cdot \alpha_{1n}) \cdot b_1 +\ \dots\ + (x_1 \cdot \alpha_{n1} +\ \dots\ + x_n \cdot \alpha_{nn}) \cdot b_n \\
\end{aligned}
$$


Sean $P \in \mathbb{K}^{n \times n}$ tal que $(P)_{ij} = \alpha_{ij}$ y $X \in \mathbb{K}^{n \times 1}$ tal que $(X)_{i1} = x_i$.

Si $x_1 \cdot u_1 +\ \dots\ + x_n \cdot u_n = o$, dado que $U$ es linealmente independiente, eso implica que $x_1 =\ \dots\ = x_n = 0$, por lo tanto por el desarrollo anterior, $P \cdot X = O$ solo tiene la solución trivial, y por _Teorema 3.10_, $P$ es inversible.

Dado un vector arbitrario $v \in V$, el vector puede expresarse como combinación lineal de la base $B$ como $v = \beta_1 \cdot b_1 +\ \dots\ + \beta_n \cdot b_n$.

Sea $Y \in \mathbb{K}^{n \times 1}$ tal que $(Y)_{i1} = \beta_i$. Como $P$ es inversible, por _Teorema 3.14_, el sistema de ecuaciones $P \cdot X = Y$ tiene solución, lo que implica por el desarrollo de la combinación lineal de los vectores de $U$, que cualquier vector de $V$ puede ser expresado como una combinación lineal de $U$. Por lo tanto $V = \langle U \rangle$, y por ser $U$ linealmente independiente, $U$ es una base de $V$.

## Tags

- algebra_lineal
- bases_y_dimension
