# Teorema 6.10


Sean $m, n \in \mathbb{N}$.

$mcd(a, b) = 1$ si y solo si $mcd(a^m, b^n) = 1$.

**Demostración**:

($\Rightarrow$)

Si $mcd(a, b) = 1$, aplicando el _Teorema 6.5_ $n-1$ veces se obtiene que $mcd(a, b^n) = 1$. Aplicando nuevamente el mismo teorema $m-1$ veces, esta vez dejando fijo a $b^n$, se obtiene $mcd(a^m, b^n) = 1$.


($\Leftarrow$)

Si $mcd(a^m, b^n) = 1$:

Si $a = 0$, entonces por _Teorema 3.2_, $mcd(a^m, b^n) = mcd(0, b^n) = \lvert b^n \rvert = 1$. Por lo tanto $b = \pm 1$, y por _Teorema 3.3_, $mcd(0, \pm 1) = mcd(a, b) = 1$.

Si $a \neq 0$, como $a \mid a^m$, por _Teorema 6.6_ $mcd(a, b^n) = 1$. Y dado que $b \mid b^n$, por el mismo teorema, $mcd(a, b) = 1$.
