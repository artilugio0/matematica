# Cálculo numérico: Método de Rayleigh-Ritz: Base de funciones lineales a trozos


Nodos: 

$$
\begin{aligned}
&0 = x_0 < x_1 <\ \dots\ < x_n < x_{n+1} = 1 \\
&\phi_i(x) =
\begin{cases}
0 &0 \leq x < x_{i-1} \\
\frac{x - x_{i-1}}{x_i - x_{i-1}} &x_{i-1} \leq x < x_i \\
\frac{x - x_{i+1}}{x_i - x_{i+1}} &x_i \leq x < x_{i+1} \\
0 &x_{i+1} \leq x \leq 1 \\
\end{cases} \\
&i \in \{1,\ \dots\ , n\}
\end{aligned}
$$

## Tags

- calculo_numerico
