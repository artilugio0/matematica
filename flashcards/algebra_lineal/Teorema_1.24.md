# Teorema 1.24


Sean $A \in \mathbb{K}^{n \times n}$ una matriz triangular y $P(x)$ un polinomio con coeficientes en $\mathbb{K}$.

$P(A)$ es triangular del mismo tipo que $A$.

**Demostración**:

$P(A) = a_0 \cdot I_n + a_1 \cdot A + a_2 \cdot A^2 +\ \dots\ + a_k \cdot A^k$, y por el _Teorema 1.23_, el primer término es triangular superior e inferior dado que es una matriz diagonal. También el resto de los términos en la suma son triangulares del mismo tipo que $A$. Por el mismo teorema, la suma de todos los términos también es triangular del mismo tipo. Por lo tanto, $P(A)$ es triangular del mismo tipo que $A$.
