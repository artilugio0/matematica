# Cálculo numérico: Punto flotante decimal de k dígitos: Terminación por redondeo


$y = \pm 0.d_1 d_2 \dots d_k d_{k+1} \dots \times 10^{n}$

Se suma $5 \times 10^{n - (k + 1)}$ a $y$, luego se trunca el resultado a $k$ dígitos.

Esto es equivalente a:

$$
\begin{cases}
d_{k+1} \geq 5 &\Rightarrow \text{se suma 1 a } d_k \text{ y luego se trunca a } k \text{ dígitos}\\
d_{k+1} < 5    &\Rightarrow \text{se trunca a } k \text{ dígitos} \\
\end{cases}
$$
