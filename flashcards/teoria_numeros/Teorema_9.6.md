# Teorema 9.6


$\lvert a \cdot b \rvert = mcd(a, b) \cdot mcm(a, b)$

**Demostración**:

$a \mid \lvert a \rvert \cdot \frac{\lvert b \rvert}{mcd(a, b)}$ y $b \mid \frac{\lvert a \rvert}{mcd(a, b)} \cdot \lvert b \rvert$. Por lo tanto $\frac{\lvert a \cdot b \rvert}{mcd(a, b)}$ es un múltiplo común de $a$ y $b$.

Sea $c \in \mathbb{N}$ tal que $a \mid c \wedge b \mid c$. Por _Teorema 2.4_ dado que $mcd(a,b)$ es divisor de $a$ y $b$, $mcd(a, b) \mid c$, y por lo tanto se tiene que $\frac{a}{mcd(a,b)} \mid \frac{c}{mcd(a,b)}$ y $\frac{b}{mcd(a,b)} \mid \frac{c}{mcd(a,b)}$. Por _Teorema 6.2_, $\frac{a}{mcd(a,b)}$ y $\frac{b}{mcd(a,b)}$ son coprimos, y por _Teorema 6.3_, $\frac{a}{mcd(a,b)} \cdot \frac{b}{mcd(a,b)} \mid \frac{c}{mcd(a,b)}$. Luego, por _Teorema 2.9_, $\frac{a \cdot b}{mcd(a,b)} \mid c$. Por lo tanto, $\frac{\lvert a \cdot b \rvert}{mcd(a,b)} \mid c$. Entonces, por _Teorema 9.5_, $\frac{\lvert a \cdot b \rvert}{mcd(a,b)} = mcm(a,b)$. Es decir, $\lvert a \cdot b \rvert = mcd(a,b) \cdot mcm(a,b)$.
