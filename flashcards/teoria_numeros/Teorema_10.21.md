# Teorema 10.21


Sea $c \in \mathbb{Z}$.

$c \cdot a \equiv c \cdot b\ (mod\ n) \Rightarrow a \equiv b\ (mod\ \frac{n}{mcd(n, c)})$.

**Demostración**:

Si $c \cdot a \equiv c \cdot b\ (mod\ n)$, dado que $mcd(n, c) \mid c$ y $mcd(n, c) \mid n$, por _Teorema 10.20_, $\frac{c}{mcd(n, c)} \cdot a \equiv \frac{c}{mcd(n, c)} \cdot b\ (mod\ \frac{n}{mcd(n, c)})$. Por _Teorema 6.2_, $mcd(\frac{c}{mcd(n, c)}, \frac{n}{mcd(n, c)}) = 1$, entonces por _Teorema 10.14_, $a \equiv b\ (mod\ \frac{n}{mcd(n, c)})$.
