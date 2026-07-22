# Teorema 10.12


$a \equiv b\ (mod\ n_1)$ y $a \equiv c\ (mod\ n_2)$, entonces $b \equiv c\ (mod\ mcd(n_1, n_2))$.

**Demostración**:

Si $a \equiv b\ (mod\ n_1)$ y $a \equiv c\ (mod\ n_2)$, entonces $n_1 \mid a - b$ y $n_2 \mid a - c$. Como $mcd(n_1, n_2)$ es divisor común de $n_1$ y $n_2$, por _Teorema 2.4_, $mcd(n_1, n_2) \mid a - b$ y $mcd(n_1, n_2) \mid a - c$. Por _Teorema 2.7_, $mcd(n_1, n_2) \mid b - c$. Luego, $b \equiv c\ (mod\ mcd(n_1, n_2))$.
