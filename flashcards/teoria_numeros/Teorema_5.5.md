# Teorema 5.5


Dados dos enteros $a, b$ no ambos nulos, si existen enteros $x, y$ para los que $mcd(a, b) = a \cdot x + b \cdot y$, entonces $mcd(x, y) = 1$.

**Demostración**:

Sea $mcd(a, b) = a \cdot x_0 + b \cdot y_0$.

Como $mcd(x_0, y_0) \mid x_0 \wedge mcd(x_0, y_0) \mid y_0$. Entonces existen $k_1, k_2\ \in \mathbb{Z}$ tales que $mcd(x_0, y_0) \cdot k_1 = x_0$ y $mcd(x_0, y_0) \cdot k_2 = y_0$. Por lo tanto $mcd(a, b) = a \cdot mcd(x_0, y_0) \cdot k_1 + b \cdot mcd(x_0, y_0) \cdot k_2$. Lo que implica que $mcd(x_0, y_0) \mid mcd(a, b)$. Dividiendo ambos miembros por $mcd(x_0, y_0)$ se obtiene $\frac{mcd(a, b)}{mcd(x_0, y_0)} = a \cdot k_1 + b \cdot k_2$.

Dado que $mcd(a, b)$ y $mcd(x_0, y_0)$ son enteros positivos, y que $mcd(a, b)$ es el menor entero positivo de la forma $a \cdot x + b \cdot y$, $\frac{mcd(a, b)}{mcd(x_0, y_0)}$ debe ser igual a $mcd(a, b)$, y por lo tanto $mcd(x_0, y_0) = 1$.
