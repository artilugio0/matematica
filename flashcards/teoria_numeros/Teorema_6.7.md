# Teorema 6.7


Si $mcd(a, b) = 1$, entonces $mcd(a \cdot c, b) = mcd(c, b)$.

**Demostración**:

Como $mcd(a, b) = 1$, existen $x_0, y_0 \in \mathbb{Z}$ tales que $a \cdot x_0 + b \cdot y_0 = 1$. Multiplicando por $c$ se tiene que $a \cdot c \cdot x_0 + b \cdot c \cdot y_0 = c$. Por _Teorema 2.3_, $mcd(a \cdot c, b)$ divide a cada termino del lado izquierdo de la igualdad, entonces por _Teorema 2.7_, $mcd(a \cdot c, b) \mid c$.

Por lo tanto $mcd(a \cdot c, b) \mid b \wedge mcd(a \cdot c, b) \mid c$.

Sea $d \in \mathbb{N}$ tal que $d \mid b \wedge d \mid c$. Por _Teorema 5.1_, existen $x_1, y_1 \in \mathbb{Z}$ tales que $mcd(a \cdot c, b) = a \cdot c \cdot x_1 + b \cdot y_1$. Por _Teorema 2.3_, $d$ divide a los términos de la derecha de la igualdad, entonces por _Teorema 2.7_, $d \mid mcd(a \cdot c, b)$. Luego, por _Teorema 5.3_, $mcd(a \cdot c, b) = mcd(c, b)$.
