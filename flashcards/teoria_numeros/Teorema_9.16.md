# Teorema 9.16


Sean $n_1, n_2,\ ...\ , n_k \in \mathbb{N}$ y sea $L = mcm(n_1, n_2,\ ...\ , n_k)$.

$mcd(\frac{L}{n_1}, \frac{L}{n_2},\ ...\ , \frac{L}{n_k}) = 1$


**Demostración**:

Sea $d \in \mathbb{N}$ tal que $d$ es un divisor común de $\frac{L}{n_1}, \frac{L}{n_2},\ ...\ , \frac{L}{n_k}$. Entonces $d \mid \frac{L}{n_i}$, para $1 \leq i \leq k$. Por _Teorema 2.9_, $d \cdot n_i \mid L$, luego, por _Teorema 9.13_, $mcm(d \cdot n_1, d \cdot n_2,\ ...\ , d \cdot n_k) \mid L$. Aplicando el _Teorema 9.12_, $d \cdot mcm(n_1, n_2,\ ...\ , n_k) \mid L$, entonces, $d \cdot L \mid L$. Luego por _Teorema 2.11_, $d \mid 1$, lo que implica por _Teorema 2.2_ que $d = \pm 1$, y como $d$ es positivo, $d = 1$. Por lo tanto, el único divisor común positivo es $1$, luego, $mcd(\frac{L}{n_1}, \frac{L}{n_2},\ ...\ , \frac{L}{n_k}) = 1$.
