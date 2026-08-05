# Teorema 9.14


Sean $a, b, c \in \mathbb{Z}$ tales que $b \neq 0$ y $c \neq 0$.

$mcd(a, mcm(b, c)) = mcm(mcd(a, b), mcd(a, c))$


**Demostración**:

Como $mcd(a, b) \mid a$, $mcd(a, b) \mid b$ y por _Teorema 2.4_ $mcd(a, b) \mid mcm(b,c)$, entonces por _Teorema 5.3_, $mcd(a, b) \mid mcd(a, mcm(b, c))$. De manera análoga se tiene que $mcd(a, c) \mid mcd(a, mcm(b, c))$. Por lo tanto, por _Teorema 9.13_, $mcm(mcd(a, b), mcd(a, c)) \mid mcd(a, mcm(b, c))$.

Por otro lado, por _Teorema 9.6_,

$$
\begin{aligned}
mcm(mcd(a, b), mcd(a, c)) &= \frac{mcd(a, b) \cdot mcd(a, c)}{mcd(mcd(a, b), mcd(a, c))} \\
&= \frac{mcd(a, b) \cdot mcd(a, c)}{mcd(a, b, c)} \\
&= \frac{(a \cdot x_1 + b \cdot y_1) \cdot (a \cdot x_2 + c \cdot y_2)}{mcd(a, b, c)} \\
&= \frac{a \cdot a \cdot x_1 \cdot x_2}{mcd(a, b, c)} + \frac{a \cdot b \cdot x_2 \cdot y_1}{mcd(a, b, c)} + \frac{a \cdot c \cdot x_1 \cdot y_2}{mcd(a, b, c)} + \frac{b \cdot c \cdot y_1 \cdot y_2}{mcd(a, b, c)} \\
\end{aligned}
$$

Donde $x_1, x_2, y_1, y_2 \in \mathbb{Z}$ y cuya existencia es garantizada por _Teorema 5.1_.

Los cuatro términos son enteros dado que $mcd(a, b, c)$ divide a $a$, $b$ y $c$. También los primeros tres términos son divisibles por $a$. Y el último es divisible por $mcm(b, c)$ por la siguiente razón:

$mcd(a, b, c) \mid mcd(b, c)$, entonces por _Teorema 9.6_, $mcd(a, b, c) \cdot k = \frac{\lvert b \cdot c \rvert}{mcm(b, c)}$, por lo tanto, $mcm(b, c) \cdot k = \frac{\lvert b \cdot c \rvert}{mcd(a, b, c)}$, es decir, $mcm(b, c) \mid \frac{\lvert b \cdot c \rvert}{mcd(a, b, c)}$ lo que implica que $mcm(b, c) \mid \frac{b \cdot c}{mcd(a, b, c)}$. Por lo tanto, por _Teorema 2.3_, $mcm(b, c)$ divide al último término.

Dado que $mcd(a, mcm(b, c))$ divide a $a$ y $mcm(b, c)$, por _Teorema 2.4_, $mcd(a, mcm(b, c))$ divide a los cuatro términos. Entonces, por _Teorema 2.7_, $mcd(a, mcm(b, c)) \mid mcm(mcd(a, b), mcd(a, c))$. Luego, por _Teorema 2.5_, $mcd(a, mcm(b, c)) = \pm mcm(mcd(a, b), mcd(a, c))$, y dado que ambos lados de la ecuación son positivos por definición, $mcd(a, mcm(b, c)) = mcm(mcd(a, b), mcd(a, c))$.
