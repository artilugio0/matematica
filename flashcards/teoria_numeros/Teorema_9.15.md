# Teorema 9.15


Sean $a, b, c \in \mathbb{Z}$ no nulos.

$mcm(a, mcd(b, c)) = mcd(mcm(a, b), mcm(a, c))$


**Demostración**:

$a \mid mcm(a, b)$ y $a \mid mcm(a, c)$. También $mcd(b, c) \mid b$ y $mcd(b, c) \mid c$, por _Teorema 2.4_, $mcd(b, c) \mid mcm(a, b)$ y $mcd(b, c) \mid mcm(a, c)$. Por _Teorema 5.3_, $a$ y $mcd(b, c)$ dividen a $mcd(mcm(a, b), mcm(a, c))$. Luego, por _Teorema 9.13_, $mcm(a, mcd(b, c)) \mid mcd(mcm(a, b), mcm(a, c))$.

Por otro lado, por _Teorema 9.6_,

$$
\begin{aligned}
mcm(a, mcd(b, c)) &= \frac{\lvert a \cdot mcd(b, c) \rvert}{mcd(a, mcd(b, c))} \\
&= \frac{\lvert a \rvert \cdot (b \cdot x + c \cdot y)}{mcd(a, b, c)} \\
&= \frac{\lvert a \rvert \cdot b \cdot x}{mcd(a, b, c)} + \frac{\lvert a \rvert \cdot c \cdot y}{mcd(a, b, c)} \\
\end{aligned}
$$

Donde $x, y \in \mathbb{Z}$ y cuya existencia es garantizada por _Teorema 5.1_.

También se tiene por _Teorema 9.6_ que $mcm(a, b) = \frac{\lvert a \cdot b \rvert}{mcd(a, b)}$. Como $mcd(a, b, c) \mid mcd(a, b)$, existe $k \in \mathbb{Z}$ tal que $mcm(a, b) = \frac{\lvert a \cdot b \rvert}{k \cdot mcd(a, b, c)}$, por lo tanto, $mcm(a, b) \cdot k = \frac{\lvert a \cdot b \rvert}{mcd(a, b, c)}$, es decir $mcm(a, b) \mid \frac{\lvert a \cdot b \rvert}{mcd(a, b, c)}$. De manera análoga $mcm(a, c) \mid \frac{\lvert a \cdot c \rvert}{mcd(a, b, c)}$. Entonces, por _Teorema 2.4_ y _Teorema 2.3_, $mcd(mcm(a, b), mcm(a, c))$ divide a $\frac{\pm a \cdot b}{mcd(a, b, c)}$ y $\frac{\pm a \cdot c}{mcd(a, b, c)}$. Luego, por _Teorema 2.7_, $mcd(mcm(a, b), mcm(a, c)) \mid \frac{\lvert a \rvert \cdot b \cdot x}{mcd(a, b, c)} + \frac{\lvert a \rvert \cdot c \cdot y}{mcd(a, b, c)}$, es decir, $mcd(mcm(a, b), mcm(a, c)) \mid mcm(a, mcd(b, c))$.

Finalmente, por _Teorema 2.5_, $mcm(a, mcd(b, c)) = \pm mcd(mcm(a, b), mcm(a, c))$, y como ambos valores son enteros positivos, $mcm(a, mcd(b, c)) = mcd(mcm(a, b), mcm(a, c))$.
