# Cálculo numérico: Teorema 3.3


Sean $f \in C^4[a, b]$ con $\max\limits_{a \leq x \leq b}\ \lvert f^{(4)}(x) \rvert = M$ y $S$ su interpolador spline cúbico único con clamped boundary en los nodos $a = x_0 < x_1 <\ \dots\ < x_n = b$.

$\forall\ x \in [a, b]: \lvert f(x) - S(x) \rvert \leq \frac{5 \cdot M}{384} \cdot \max\limits_{0 \leq j \leq n-1}\ (x_{j+1} - x_j)^4$

## Tags

- calculo_numerico
