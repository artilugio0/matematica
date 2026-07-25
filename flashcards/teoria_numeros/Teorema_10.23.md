# Teorema 10.23


Sea $P(x) = \sum\limits_{k=0}^{m} C_k \cdot x^k$ un polinomio con coeficientes enteros.

Si $a \equiv b\ (mod\ n)$, entonces $P(a) \equiv P(b)\ (mod\ n)$.

**Demostración**:

Si $a \equiv b\ (mod\ n)$, sea $k \in \mathbb{Z}$ tal que $0 \leq k \leq m$. Por _Teorema 10.10_, $a^k \equiv b^k\ (mod\ n)$. Y _Teorema 10.9_, $C_k \cdot a^k \equiv C_k \cdot b^k\ (mod\ n)$. Luego, aplicando el _Teorema 10.6_ $m$ veces, $C_0 \cdot a^0 + C_1 \cdot a^1 +\ ...\ + C_m \cdot a^m \equiv C_0 \cdot b^0 + C_1 \cdot b^1 +\ ...\ + C_m \cdot b^m\ (mod\ n)$. Por lo tanto, $P(a) \equiv P(b)\ (mod\ n)$.
