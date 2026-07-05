# Teorema 6.3


Si $a \mid c \wedge b \mid c \wedge mcd(a, b) = 1$, entonces $a \cdot b \mid c$.

**Demostración**:

Por _Teorema 6.1_, existen $x, y \in \mathbb{Z}$ tales que $a \cdot x + b \cdot y = 1$. Multiplicando por $c$ se tiene que $a \cdot c \cdot x + b \cdot c \cdot y = c$. Luego, como $a \mid c \wedge b \mid c$, existen $k_1, k_2 \in \mathbb{Z}$ tales que $c = a \cdot k_1$ y $c = b \cdot k_2$. Reemplazando en la igualdad anterior se tiene que $a \cdot b \cdot (k_2 \cdot x + k_1 \cdot y) = c$. Por lo tanto, $a \cdot b \mid c$.
