# Teorema 6.13


Sean $a, b \in \mathbb{Z}$ no ambos nulos, y $n \in \mathbb{N}$.

Si $mcd(a, b) = d$, entonces $mcd(a^n, b^n) = d^n$.

**Demostración**:

Si $mcd(a, b) = d$, por _Teorema 6.2_, $mcd(\frac{a}{d}, \frac{b}{d}) = 1$. Luego, por _Teorema 6.10_, $mcd((\frac{a}{d})^n, (\frac{b}{d})^n) = 1$. Por _Teorema 5.7_, $mcd(a^n, b^n) = mcd(d^n \cdot \frac{a^n}{d^n}, d^n \cdot \frac{b^n}{d^n}) = d^n \cdot mcd(\frac{a^n}{d^n}, \frac{b^n}{d^n}) = d^n$. Por lo tanto, $mcd(a^n, b^n) = d^n$.
