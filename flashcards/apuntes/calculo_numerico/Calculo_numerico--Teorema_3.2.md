# Cálculo numérico: Teorema 3.2


Sea $f: [a, b] \subseteq \mathbb{R} \to \mathbb{R}$ diferenciable en $a$ y $b$, y los nodos $a = x_0 < x_1 <\ \dots\ < x_n = b$.

$f$ tiene un único interpolador spline cúbico $S$ sobre esos nodos que cumple las condiciones de clamped boundary, es decir $S'(x_0) = f'(x_0) \wedge S'(x_n) = f'(x_n)$.
