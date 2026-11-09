# Cálculo numérico: Cuadratura Gaussiana: Cambio de variables para integral de $a$ a $b$


$$
\begin{aligned}
t &= \frac{2 \cdot x - a - b}{b - a} \\
x &= \frac{(b - a) \cdot t + a + b}{2} \\
\int\limits_{a}^b f(x)dx &= \int\limits_{-1}^1 f \left(\frac{(b - a) \cdot t + a + b}{2} \right) \cdot \frac{b - a}{2} dt
\end{aligned}
$$

## Tags

- calculo_numerico
