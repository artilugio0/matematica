# Algoritmo de Euclides: Demostración: Paso 2: $r_n$ es mayor o igual a cualquier otro divisor


Sea $d \in \mathbb{Z}$ tal que $d \mid a \wedge d \mid b$. De $a = b q_1 + r_1$ se tiene que $a + b (-q_1) = r_1$, y por _Teorema 2.1 - Propiedad 7_, $d \mid r_1$. Por el mismo argumento aplicado a cada $r_i$, se tiene que $d \mid r_2$, $d \mid r_3$, ..., $d \mid r_n$.

Como el procedimiento se aplica al caso en que $a \nmid b$ y $b \nmid a$, se tiene $r_1 \neq 0$, luego $n \geq 1$ y por lo tanto $r_n > 0$, es decir $\lvert r_n \rvert = r_n$.

Por _Teorema 2.1 - Propiedad 6_, $d \leq \lvert d \rvert \leq \lvert r_n \rvert = r_n$. Por lo tanto, $d \leq r_n$.
