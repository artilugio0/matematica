# Teorema 9.12


Sean $a, b, k \in \mathbb{Z}$, con $a \neq 0,\ b \neq 0,\ k \geq 1$.

$mcm(k \cdot a, k \cdot b) = k \cdot mcm(a, b)$

**Demostración**:

Por _Teorema 9.6_, $\lvert (k \cdot a) \cdot (k \cdot b) \rvert = mcd(k \cdot a, k \cdot b) \cdot mcm(k \cdot a, k \cdot b)$. Luego, por _Teorema 5.7_, $mcd(k \cdot a, k \cdot b) = k \cdot mcd(a, b)$, por lo tanto, $k \cdot k \cdot \lvert a \cdot b \rvert = k \cdot mcd(a, b) \cdot mcm(k \cdot a, k \cdot b)$. Lo que implica que $k \cdot \frac{\lvert a \cdot b \rvert}{mcd(a, b)} = mcm(k \cdot a, k \cdot b)$. Pero por _Teorema 9.6_, $\frac{\lvert a \cdot b \rvert}{mcd(a, b)} = mcm(a, b)$. Luego, $k \cdot mcm(a, b) = mcm(k \cdot a, k \cdot b)$.
