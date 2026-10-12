# Sistema de ecuaciones lineales en forma matricial


Todo sistema de $m$ ecuaciones lineales y $n$ incógnitas puede expresarse como una ecuación matricial.

Dado el sistema

$$
\begin{cases}
a_{11} \cdot x_1 + \dots + a_{1n} \cdot x_n = y_1 \\
a_{21} \cdot x_1 + \dots + a_{2n} \cdot x_n = y_2 \\
\vdots \\
a_{m1} \cdot x_1 + \dots + a_{mn} \cdot x_n = y_m \\
\end{cases}
$$

El mismo sistema puede expresarse como

$A \cdot X = Y$

Se definen las matrices como:

- $A \in \mathbb{K}^{m \times n}$ es la matriz de coeficientes, siendo $(A)_{ij} = a_{ij}$.
- $X \in \mathbb{K}^{n \times 1}$ es la matriz de incógnitas, siendo $(X)_{j1} = x_{j}$.
- $Y \in \mathbb{K}^{m \times 1}$ es la matriz de términos independientes, siendo $(Y)_{i1} = y_{i}$.

Para $1 \leq i \leq m$ y $1 \leq j \leq n$.

## Tags

- algebra_lineal
- sistema_ecuaciones_lineales
