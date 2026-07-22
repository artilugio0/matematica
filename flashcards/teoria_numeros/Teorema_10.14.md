# Teorema 10.14


Sea $c \in \mathbb{Z}$ tal que $mcd(n, c) = 1$.

Si $c \cdot a \equiv c \cdot b\ (mod\ n) \Rightarrow a \equiv b\ (mod\ n)$.

**Demostración**:

Si $c \cdot a \equiv c \cdot b\ (mod\ n)$, entonces $n \mid c \cdot a - c \cdot b$. Por lo tanto, $n \mid c \cdot (a - b)$. Luego, dado que $mcd(n, c) = 1$, por _Teorema 6.4_, $n \mid a - b$. Entonces, $a \equiv b\ (mod\ n)$.
