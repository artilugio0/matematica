# Teorema 5.7


Sean $a, b \in \mathbb{Z}$ no ambos nulos.
$\forall\ k \in \mathbb{N}: mcd(k \cdot a, k \cdot b) = k \cdot mcd(a, b)$

**Demostración**:

Por definición $mcd(a, b) \mid a \wedge mcd(a, b) \mid b$. Por _Teorema 2.9_, $k \cdot mcd(a, b) \mid k \cdot a \wedge k \cdot mcd(a, b) \mid k \cdot b$.

Sea $d \in \mathbb{Z}$, tal que $d \mid k \cdot a \wedge d \mid k \cdot b$. Por _Teorema 5.1_, existen $x_0, y_0 \in \mathbb{Z}$ tales que $k \cdot mcd(a, b) = k \cdot (a \cdot x_0 + b \cdot y_0) = k \cdot a \cdot x_0 + k \cdot b \cdot y_0$. Por _Teorema 2.7_, $d \mid k \cdot mcd(a, b)$. Luego, por _Teorema 5.3_, $mcd(k \cdot a, k \cdot b) = k \cdot mcd(a, b)$.
