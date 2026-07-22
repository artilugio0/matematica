# Teorema 9.13


Si $a \mid c$ y $b \mid c$, entonces $mcm(a, b) \mid c$.

**Demostración**:

Si $a \mid c \wedge b \mid c$ y $d = mcd(a, b)$, por _Teorema 2.4_, $d \mid c$. Luego, por _Teorema 2.11_, $\frac{a}{d} \mid \frac{c}{d}$ y $\frac{b}{d} \mid \frac{c}{d}$. Y como $mcd(\frac{a}{d}, \frac{b}{d}) = 1$ (por _Teorema 6.2_), entonces por _Teorema 6.3_, $\frac{a}{d} \cdot \frac{b}{d} \mid \frac{c}{d}$. Luego, por _Teorema 2.9_, $\frac{a \cdot b}{d} \mid c$, lo que implica que $\frac{\lvert a \cdot b \rvert}{d} \mid c$. Finalmente, por _Teorema 9.6_, $\frac{\lvert a \cdot b \rvert}{d} = mcm(a, b)$, por lo tanto, $mcm(a, b) \mid c$.
