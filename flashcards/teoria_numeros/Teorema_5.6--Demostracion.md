# Teorema 5.6: Demostración


Sean $a, b, c \in \mathbb{Z}$ tales que $a \mid b \cdot c$.

Usando _Teorema 5.1_, existen $x_0, x_1, y_0, y_1 \in \mathbb{Z}$ tales que $mcd(a, b) = a \cdot x_0 + b \cdot y_0$, y $mcd(a, c) = a \cdot x_1 + c \cdot y_1$.

Multiplicando miembro a miembro:
$$
\begin{align}
mcd(a, b) \cdot mcd(a, c) &= (a \cdot x_0 + b \cdot y_0) \cdot (a \cdot x_1 + c \cdot y_1) \\
&= a^2 \cdot x_0 \cdot x_1 + a \cdot c \cdot x_0 \cdot y_1 + a \cdot b \cdot x_1 \cdot y_0 + b \cdot c \cdot y_0 \cdot y_1
\end{align}
$$

Por _Teorema 2.1 - Propiedad 3_, $a$ divide a los primeros tres términos de la última suma, y por hipótesis $a \mid b \cdot c$, por lo tanto también divide al último término. Luego por _Teorema 2.1 - Propiedad 7_, $a \mid mcd(a, b) \cdot mcd(a, c)$.
