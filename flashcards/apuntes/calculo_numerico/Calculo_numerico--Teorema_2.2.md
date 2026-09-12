# Cálculo numérico: Teorema 2.2


Polinomio interpolador de Lagrange

Sean $x_0, x_1, \dots\ , x_n \in A \subseteq \mathbb{R}$ todos distintos y $f: A \to \mathbb{R}$.

$\exists!\ P(x) \in \mathbb{R}_n[x] \mid f(x_k) = P(x_k)$ para cada $k = 0, 1, \dots\ , n$.

El polinomio está definido por $P(x) = \sum\limits_{k = 0}^n f(x_k) \cdot L_{k,n}(x)$

Siendo
$$
L_{k,n}(x) = \prod\limits_{\substack{i = 0 \\ i \neq k}}^n \frac{x - x_i}{x_k - x_i} = \frac{(x - x_0) \cdot (x - x_1) \cdot\ \dots\ \cdot (x - x_{k-1}) \cdot (x - x_{k+1}) \cdot\ \dots\ \cdot (x - x_n)}{(x_k - x_0) \cdot (x_k - x_1) \cdot\ \dots\ \cdot (x_k - x_{k-1}) \cdot (x_k - x_{k+1}) \cdot\ \dots\ \cdot (x_k - x_n)}
$$
