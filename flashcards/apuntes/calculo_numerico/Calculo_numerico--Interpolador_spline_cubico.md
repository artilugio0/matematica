# Cálculo numérico: Interpolador spline cúbico


Sea $f: [a, b] \subseteq \mathbb{R} \to \mathbb{R}$ y los nodos $a = x_0 < x_1 <\ \dots\ < x_n = b$, un interpolador spline cúbico $S$ de $f$ es una función que cumple:

1. $S(x)$ es un polinomio cúbico, denotado por $S_j(x)$, en cada intervalo $[x_j, x_{j+1}]$ para $j = 0, 1,\ \dots\ , n-1$
2. $S_j(x_j) = f(x_j) \wedge S_{j}(x_{j+1}) = f(x_{j+1})$ para $j = 0, 1,\ \dots\ , n-1$
3. $S_{j+1}(x_{j+1}) = S_j(x_{j+1})$ para $j = 0, 1,\ \dots\ , n-2$
4. $S_{j+1}'(x_{j+1}) = S_j'(x_{j+1})$ para $j = 0, 1,\ \dots\ , n-2$
5. $S_{j+1}''(x_{j+1}) = S_j''(x_{j+1})$ para $j = 0, 1,\ \dots\ , n-2$
6. Satisface alguna de las siguientes condiciones de frontera:
    1. $S''(x_0) = S''(x_n) = 0$ (natural (or free) boundary)
    2. $S'(x_0) = f'(x_0) \wedge S'(x_n) = f'(x_n)$ (clamped boundary)

## Tags

- calculo_numerico
