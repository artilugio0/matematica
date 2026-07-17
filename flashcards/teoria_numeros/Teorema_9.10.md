# Teorema 9.10


Sean $a, b \in \mathbb{Z}$ no nulos.

$mcm(a, b) = mcd(a, b)$ si y solo si $\lvert a \rvert = \lvert b \rvert$

**Demostración**:

($\Rightarrow$)

Si $mcm(a, b) = mcd(a, b)$, por definición $a \mid mcm(a, b)$. Como $mcm(a, b) = mcd(a, b)$, por definición de máximo común divisor, $mcm(a, b) \mid a$. Luego, por _Teorema 2.5_, $mcm(a, b) = \pm a$. Por el mismo razonamiento, $mcm(a, b) = \pm b$. Por lo tanto, $\lvert a \rvert = \lvert b \rvert$.

($\Leftarrow$)

Si $\lvert a \rvert = \lvert b \rvert$, entonces por _Teorema 9.7_, $mcm(a, b) = mcm(\lvert a \rvert, \lvert b \rvert) = mcm(\lvert a \rvert, \lvert a \rvert)$. Luego por _Teorema 9.1_, $mcm(a, b) = mcm(\lvert a \rvert, \lvert a \rvert) = \lvert a \rvert$.

Y por _Teorema 3.7_, $mcd(a, b) = mcd(\lvert a \rvert, \lvert b \rvert) = mcd(\lvert a \rvert, \lvert a \rvert)$. Luego por _Teorema 3.1_, $mcd(a, b) = mcd(\lvert a \rvert, \lvert a \rvert) = \lvert a \rvert$.

Por lo tanto, $mcm(a, b) = mcd(a, b)$.
