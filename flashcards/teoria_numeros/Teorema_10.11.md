# Teorema 10.11


$a \equiv b\ (mod\ n)$, entonces $mcd(a, n) = mcd(b, n)$.

**Demostración**:

Sea $d = mcd(b, n)$. Por definición, $d \mid b \wedge d \mid n$. Como $n \mid a - b$, entonces por _Teorema 2.4_, $d \mid a - b$. Luego, por _Teorema 2.8_, $d \mid a$. Por lo tanto $d$ es divisor común de $a$ y $n$.

Sea $d'$ un divisor común de $a$ y $n$. Como $n \mid a - b$, entonces por _Teorema 2.4_, $d' \mid a - b$, y por _Teorema 2.8_, $d' \mid b$. Luego, por ser divisor común de $b$ y $n$, por _Teorema 5.3_, $d' \mid d$. Por lo tanto, por el mismo teorema, $d = mcd(a, n)$.
