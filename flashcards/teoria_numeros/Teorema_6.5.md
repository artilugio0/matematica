# Teorema 6.5


Si $mcd(a, b) = 1 \wedge mcd(a, c) = 1 \Rightarrow mcd(a, b \cdot c) = 1$.

Demostración:

Como $mcd(a, b) = 1 \wedge mcd(a, c) = 1$, por _Teorema 6.1_, existen $x_0, x_1, y_0, y_1 \in \mathbb{Z}$ tales que:

$$
\begin{aligned}
mcd(a, b) &= a \cdot x_0 + b \cdot y_0 = 1 \\
mcd(a, c) &= a \cdot x_1 + c \cdot y_1 = 1
\end{aligned}
$$

Multiplicando ambas igualdades se obtiene:

$$
a^2 \cdot x_0 \cdot x_1 + a \cdot c \cdot x_0 \cdot y_1 + a \cdot b \cdot x_1 \cdot y_0 + b \cdot c \cdot y_0 \cdot y_1 = 1
$$

Sea $d \in \mathbb{N}$, tal que $d \mid a \wedge d \mid b \cdot c$. Luego, por _Teorema 2.3_, $d$ divide cada uno de los términos de la ecuación anterior, entonces por _Teorema 2.7_, $d \mid 1$. Como $1 \mid a \wedge 1 \mid b \cdot c$, y para cualquier divisor comun $d$, $d \mid 1$, se tiene por _Teorema 5.3_ que $mcd(a, b \cdot c) = 1$.
