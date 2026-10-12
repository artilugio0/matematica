# Teorema 2.1


Dado un sistema de ecuaciones lineales, toda solución del sistema también es solución de cualquier ecuación que sea una combinación lineal de las ecuaciones del sistema.

**Demostración**:

Dado el sistema de $m$ ecuaciones lineales con $n$ incógnitas

$$
\begin{cases}
a_{11} \cdot x_1 + \dots + a_{1n} \cdot x_n = y_1 \\
a_{21} \cdot x_1 + \dots + a_{2n} \cdot x_n = y_2 \\
\vdots \\
a_{m1} \cdot x_1 + \dots + a_{mn} \cdot x_n = y_m \\
\end{cases}
$$

y una solución $(v_1,\ \dots\ , v_n)$.

Una ecuación que es una combinación lineal de las $m$ ecuaciones del sistema tendrá la forma:

$C_1 \cdot (a_{11} \cdot x_1 + \dots + a_{1n} \cdot x_n) +\ \dots\ + C_m \cdot (a_{m1} \cdot x_1 + \dots + a_{mn} \cdot x_n) = C_1 \cdot y_1 +\ \dots\ + C_m \cdot y_m$

Con $C_i \in \mathbb{K}$, para $1 \leq i \leq m$.

Como $(v_1,\ \dots\ , v_n)$ es solución del sistema, se cumple que:

$$
\begin{cases}
a_{11} \cdot v_1 + \dots + a_{1n} \cdot v_n = y_1 \\
a_{21} \cdot v_1 + \dots + a_{2n} \cdot v_n = y_2 \\
\vdots \\
a_{m1} \cdot v_1 + \dots + a_{mn} \cdot v_n = y_m \\
\end{cases}
$$

Multiplicando la $i$-ésima ecuación por $C_i$, y sumando las igualdades se obtiene:

$$
\begin{aligned}
C_1 \cdot (a_{11} \cdot v_1 + \dots + a_{1n} \cdot v_n) +\ \dots\ + C_m \cdot (a_{m1} \cdot v_1 + \dots + a_{mn} \cdot v_n) = C_1 \cdot y_1 +\ \dots\ + C_m \cdot y_m
\end{aligned}
$$

Por lo tanto, $(v_1,\ \dots\ , v_n)$ también es una solución de la ecuación.

## Tags

- algebra_lineal
- sistema_ecuaciones_lineales
