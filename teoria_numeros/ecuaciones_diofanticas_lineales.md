# Ecuaciones diofánticas lineales

## Definición

Ecuación lineal donde las incógnitas son números enteros.

# Teorema 7.1

Sean $a, b \in \mathbb{Z}$.

La ecuación $a \cdot x + b \cdot y = c$ tiene solución si y solo si $mcd(a, b) \mid c$. 

También, si la ecuación tiene solución, entonces tiene infinitas soluciones. Si $(x_0, y_0)$ es una solución particular de la ecuación, entonces todas las soluciones están dadas por:

$$
\begin{align}
&x = x_0 + \frac{b}{mcd(a, b)} \cdot t \\
&y = y_0 - \frac{a}{mcd(a, b)} \cdot t \\
&\text{con } t \in \mathbb{Z}
\end{align}
$$

Demostración:

Por _Teorema 5.4_, la ecuación tiene solución si y solo si $mcd(a, b) \mid c$.

Sea $(x_0, y_0)$ es una solución particular de la ecuación, y sea $(x, y)$ cualquier otra solución, entonces:

$$
\begin{align}
a \cdot x_0 + b \cdot y_0 &= c \\
a \cdot x + b \cdot y &= c
\end{align}
$$

Reemplazando y reacomodando se obtiene:
$$
\begin{align}
a \cdot (x - x_0) &= b \cdot (y_0 - y) & (1)\\
\end{align}
$$

Dado que $mcd(a, b)$ es divisor común de $a$ y $b$, dividiendo ambos lados de la ecuación se tiene que $\frac{a}{mcd(a,b)} \cdot (x - x_0) = \frac{b}{mcd(a,b)} \cdot (y_0 - y)$. Por lo tanto $\frac{b}{mcd(a,b)} \mid \frac{a}{mcd(a,b)} \cdot (x - x_0)$. Como $\frac{b}{mcd(a,b)}$ y $\frac{a}{mcd(a,b)}$ son coprimos (por _Teorema 6.2_), entonces por _Teorema 6.4_,  $\frac{b}{mcd(a,b)} \mid (x - x_0)$. Por lo tanto, $x - x_0 = \frac{b}{mcd(a,b)} \cdot t$ para algún $t \in \mathbb{Z}$. De donde se obtiene que $x = x_0 + \frac{b}{mcd(a,b)} \cdot t$. Reemplazando $(x - x_0)$ en $(1)$ y despejando $y$ se obtiene que $y = y_0 - \frac{a}{mcd(a,b)} \cdot t$.

Con esto queda demostrado que toda solución debe ser de la forma que el teorema establece (la solución particular incial también lo cumple con $t = 0$).

Por otro lado, sea $t \in \mathbb{Z}$, si se toma la forma general de la solución y se reemplaza en la ecuación original se tiene:

$$
\begin{align}
a \cdot (x_0 + \frac{b}{mcd(a, b)} \cdot t) + b \cdot (y_0 - \frac{a}{mcd(a, b)} \cdot t) &= c \\
a \cdot x_0 + \frac{a \cdot b}{mcd(a, b)} \cdot t + b \cdot y_0 - \frac{a \cdot b}{mcd(a, b)} \cdot t &= c \\
a \cdot x_0 + b \cdot y_0 &= c \\
c &= c
\end{align}
$$

Lo que implica que cualquier par de enteros de esa forma es solución de la ecuación para cualquier valor de $t$.

Por lo tanto, queda demostrado que si hay una solución, entonces hay infinitas soluciones, y todas las soluciones son de la forma anteriormente mencionada.
