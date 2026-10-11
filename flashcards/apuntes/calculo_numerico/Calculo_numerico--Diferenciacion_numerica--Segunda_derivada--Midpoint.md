# Cálculo numérico: Diferenciación numérica: Segunda derivada: Midpoint


$f''(x_0) = \frac{1}{h^2} \cdot [f(x_0 - h) - 2 \cdot f(x_0) + f(x_0 + h)] - \frac{h^2}{24} \cdot [f^{(4)}(\xi_1) + f^{(4)}(\xi_{-1})]$

Con $x_0 - h < \xi_{-1} < x_0 < \xi_1 < x_0 + h$.

Si $f^{(4)}$ es continua en $[x_0 - h, x_0 + h]$, entonces el término de error puede simplificarse a $-\frac{h^2}{12} \cdot f^{(4)}(\xi)$, con $x_0 - h < \xi < x_0 + h$.

## Tags

- calculo_numerico
