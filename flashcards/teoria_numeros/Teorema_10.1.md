# Teorema 10.1


$a \equiv b\ (mod\ n)$ si y solo si $a$ y $b$ tienen el mismo resto en la división por $n$.

**Demostración**:

($\Rightarrow$)

Por _Teorema 1.1_, existen $q, q', r, r' \in \mathbb{Z}$ tales que $a = n \cdot q + r$ y $b = n \cdot q' + r'$, con $0 \leq r, r' < \lvert n \rvert$. Luego, $a - b = n \cdot (q - q') + (r - r')$. Como $a \equiv b\ (mod\ n)$, entonces $n \mid a - b$. Entonces, por _Teorema 2.8_, $n \mid r - r'$. Pero $\lvert r - r'\rvert < n$, por lo tanto se debe dar que $r - r' = n \cdot 0 = 0$. Luego, $r = r'$, es decir, $a$ y $b$ tienen el mismo resto en la división por $n$.

($\Leftarrow$)

Si $a$ y $b$ tienen el mismo resto en la división por $n$, entonces por _Teorema 1.1_, existen $q, q', r \in \mathbb{Z}$ tales que $a = n \cdot q + r$ y $b = n \cdot q' + r$, con $0 \leq r < \lvert n \rvert$. Restando las igualdades se tiene que $a - b = n \cdot (q - q')$. Luego $n \mid a - b$, por lo tanto $a \equiv b\ (mod\ n)$.
