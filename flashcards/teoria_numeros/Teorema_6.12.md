# Teorema 6.12


Sea $n \in \mathbb{N}$.

$a^n \mid b^n$ si y solo si $a \mid b$.

**Demostración**:

($\Rightarrow$)

Sea $d = mcd(a, b)$. Por _Teorema 6.2_, $mcd(\frac{a}{d}, \frac{b}{d}) = 1$. Luego, por _Teorema 6.10_, $mcd((\frac{a}{d})^n, (\frac{b}{d})^n) = mcd(\frac{a^n}{d^n}, \frac{b^n}{d^n}) = 1$.

Si $a^n \mid b^n$, entonces existe $k \in \mathbb{Z}$ tal que $b^n = a^n \cdot k$. Por lo tanto, se tiene que $mcd(\frac{a^n}{d^n}, \frac{a^n \cdot k}{d^n}) = 1$. Como $\frac{a^n}{d^n}$ es divisor común, entonces por _Teorema 5.3_, $\frac{a^n}{d^n} \mid 1$. Luego, Por _Teorema 2.2_, $\frac{a^n}{d^n} = \pm 1$, de donde se obtiene que $a^n = \pm d^n$, lo que implica que $d = \lvert a \rvert$. Luego, dado que $a \mid \lvert a \rvert = d \wedge d \mid b$, por _Teorema 2.4_, $a \mid b$.


($\Leftarrow$)

Si $a \mid b$, entonces existe $k \in \mathbb{Z}$ tal que $b = a \cdot k$. Multiplicando esta igualdad consigo misma $n$ veces se obtiene $b^n = a^n \cdot k^n$. Por lo tanto $a^n \mid b^n$.
