# Teorema 10.5


$a \equiv b\ (mod\ n)$ y $b \equiv c\ (mod\ n)$ entonces $a \equiv c\ (mod\ n)$.

**Demostración**:

Si $a \equiv b\ (mod\ n)$ y $b \equiv c\ (mod\ n)$, entonces $n \mid a - b$ y $n \mid b - c$. Por lo tanto, $n \cdot k = a - b$ y $n \cdot k' = b - c$, para algunos $k, k' \in \mathbb{Z}$. Sumando ambas igualdades se tiene que $n \cdot (k + k') = a - c$. Por lo tanto $n \mid a - c$, lo que implica que $a \equiv c\ (mod\ n)$.
