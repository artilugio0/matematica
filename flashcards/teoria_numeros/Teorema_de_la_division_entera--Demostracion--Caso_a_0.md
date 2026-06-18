# Teorema de la división entera: Demostración: Caso $a < 0$

Sean $a \in \mathbb{Z}, b \in \mathbb{Z}$, con $a < 0$ y $b \neq 0$.

Existen $r_0 \in \mathbb{N_0}$ y $q_0 \in \mathbb{Z}$ únicos tales que $-a = bq_0 + r_0$, con $0 \leq r_0 < \lvert b \rvert$.

Luego, $a = b(-q_0) - r_0$. Si $r_0 = 0$, entonces $a = b(-q_0)$ con $q_1 = -q_0,\ r_1 = 0$ cumpliendo el teorema. De no ser así, se tiene:

- Si $b > 0$: $a = b(-q_0 -1) + (b - r_0)$, donde $0 < b - r_0 < \lvert b \rvert$, definiendo $q_1 = -q_0 - 1$ y $r_1 = b - r_0$.
- Si $b < 0$: $a = b(-q_0 +1) + (-b - r_0)$, donde $0 < -b - r_0 < \lvert b \rvert$, definiendo $q_1 = -q_0 + 1$ y $r_1 = -b - r_0$.

Por lo tanto existen valores únicos de $q_1, r_1$ que cumplen las condiciones del teorema.

La unicidad de $q_1$ y $r_1$ queda garantizada por la unicidad de $q_0$ y $r_0$.
