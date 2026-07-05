# Teorema 6.8


Si $mcd(a, b) = 1 \wedge c \mid (a + b) \Rightarrow mcd(a, c) = mcd(b, c) = 1$.

**Demostración**:

Como $mcd(a, b) = 1$, existen $x, y \in \mathbb{Z}$ tales que $a \cdot x + b \cdot y = 1$. Y dado que $c \mid (a + b)$, existe $k \in \mathbb{Z}$ tal que $c \cdot k = a + b$, por lo tanto, $a = c \cdot k - b$ y $b = c \cdot k - a$.

Combinando las igualdades anteriores se tiene:

$$
\begin{aligned}
a \cdot x + (c \cdot k - a) \cdot y &= a \cdot (x - y) + c \cdot k \cdot y = 1 && (1) \\
(c \cdot k - b) \cdot x + b \cdot y &= c \cdot k \cdot x + b \cdot (y - x) = 1 && (2)
\end{aligned}
$$

Por _Teorema 2.3_, $mcd(a, c)$ divide a los términos de $(1)$, entonces por _Teorema 2.7_, $mcd(a, c) \mid 1$. Y por _Teorema 2.2_, $mcd(a, c) = 1$.

Por _Teorema 2.3_, $mcd(b, c)$ divide a los términos de $(2)$, entonces por _Teorema 2.7_, $mcd(b, c) \mid 1$. Y por _Teorema 2.2_, $mcd(b, c) = 1$.
