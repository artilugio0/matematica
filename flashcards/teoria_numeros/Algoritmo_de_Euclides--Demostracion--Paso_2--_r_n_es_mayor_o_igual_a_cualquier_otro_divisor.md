# Algoritmo de Euclides: Demostración: Paso 2: $r_n$ es mayor o igual a cualquier otro divisor


Sea $d \in \mathbb{Z}$ tal que $d \mid a \wedge d \mid b$. Entonces $d \mid r_{-1} \wedge d \mid r_0$. De $r_{-1} = r_0 q_1 + r_1$ se tiene que $r_{-1} + r_0 (-q_1) = r_1$, y por _Divisibilidad - Teorema 1 - Propiedad 7_, $d \mid r_1$. Por el mismo argumento aplicado a cada $r_i$, se tiene que $d \mid r_2$, $d \mid r_3$, ..., $d \mid r_n$.

Por _Divisibilidad - Teorema 1 - Propiedad 6_, $d \leq \lvert d \rvert \leq \lvert r_n \rvert = r_n$. Por lo tanto, $d \leq r_n$.
