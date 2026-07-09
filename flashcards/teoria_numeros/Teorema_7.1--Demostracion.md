# Teorema 7.1: Demostración


Por _Teorema 5.4_, la ecuación tiene solución si y solo si $mcd(a, b) \mid c$.

Sea $(x_0, y_0)$ una solución particular de la ecuación, y sea $(x, y)$ cualquier otra solución, entonces:

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

Si $a = 0$ entonces se obtiene $y = y_0$, y $x$ puede tomar cualquier valor. De modo que las soluciones tienen la forma indicada por el teorema. Lo mismo ocurre si $b = 0$. Por lo tanto, en adelante se puede asumir que $a \neq 0$ y $b \neq 0$.

Dado que $mcd(a, b)$ es divisor común de $a$ y $b$, dividiendo ambos lados de la ecuación se tiene que $\frac{a}{mcd(a,b)} \cdot (x - x_0) = \frac{b}{mcd(a,b)} \cdot (y_0 - y)$. Por lo tanto $\frac{b}{mcd(a,b)} \mid \frac{a}{mcd(a,b)} \cdot (x - x_0)$. Como $\frac{b}{mcd(a,b)}$ y $\frac{a}{mcd(a,b)}$ son coprimos (por _Teorema 6.2_), entonces por _Teorema 6.4_,  $\frac{b}{mcd(a,b)} \mid (x - x_0)$. Por lo tanto, $x - x_0 = \frac{b}{mcd(a,b)} \cdot t$ para algún $t \in \mathbb{Z}$. De donde se obtiene que $x = x_0 + \frac{b}{mcd(a,b)} \cdot t$. Reemplazando $(x - x_0)$ en $(1)$ y despejando $y$ se obtiene que $y = y_0 - \frac{a}{mcd(a,b)} \cdot t$.

Con esto queda demostrado que toda solución debe ser de la forma que el teorema establece (la solución particular inicial también lo cumple con $t = 0$).

Por otro lado, sea $t \in \mathbb{Z}$, si se toma la forma general de la solución y se reemplaza en la ecuación original se tiene:

$$
\begin{align}
a \cdot (x_0 + \frac{b}{mcd(a, b)} \cdot t) + b \cdot (y_0 - \frac{a}{mcd(a, b)} \cdot t) &= a \cdot x_0 + \frac{a \cdot b}{mcd(a, b)} \cdot t + b \cdot y_0 - \frac{a \cdot b}{mcd(a, b)} \cdot t \\
&= a \cdot x_0 + b \cdot y_0 \\
&= c
\end{align}
$$

Lo que implica que cualquier par de enteros de esa forma es solución de la ecuación para cualquier valor de $t$.

Por lo tanto, queda demostrado que si hay una solución, entonces hay infinitas soluciones, y todas las soluciones son de la forma anteriormente mencionada.
