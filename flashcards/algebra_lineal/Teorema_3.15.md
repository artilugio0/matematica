# Teorema 3.15


Sea $A \in \mathbb{K}^{n \times n}$.

Si $A$ tiene una inversa a derecha o tiene una inversa a izquierda, entonces $A$ es inversible.

**Demostración**:

Sea $B \in \mathbb{K}^{n \times n}$ una inversa a izquierda de $A$. Dado el sistema de ecuaciones lineales homogéneo $A \cdot X = O$, multiplicando a izquierda a ambos lados de la igualdad se obtiene que $B \cdot A \cdot X = X = B \cdot O = O$. Por lo tanto el sistema solo tiene la solución trivial, y por _Teorema 3.10_, $A$ es inversible.

Sea $B \in \mathbb{K}^{n \times n}$ una inversa a derecha de $A$, entonces $A \cdot B = I_n$, que implica que $A$ es una inversa a izquierda de $B$. Por lo demostrado anteriormente, $B$ es inversible. Multiplicando a derecha por $B^{-1}$ en ambos lados de la última igualdad se tiene que $A = B^{-1}$, y por _Teorema 3.5_, $A$ es inversible y su inversa es $B$.

## Tags

- algebra_lineal
- matriz_inversa
