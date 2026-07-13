# Teorema 8.12


Sean $a, b \in \mathbb{N}$.

El máximo común divisor de $a$ y $b$ es el producto de los factores primos comunes de $a$ y $b$ elevados a la menor potencia con la que aparece en las respectivas representaciones canónicas.

**Demostración**:

Sea $d = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot\ ... \cdot p_k^{\alpha_k}$ tal que cada $p_i$ es un primo que aparece en las formas canónicas de $a$ y $b$ y $\alpha_i$ la menor de las potencias que tiene $p_i$ en ambas formas canónicas.

Por _Teorema 8.9_, $d \mid a \wedge d \mid b$.

Sea $d'$ otro divisor común de $a$ y $b$, por ser divisor común y por _Teorema 8.9_, $d' = p_1^{\beta_1} \cdot p_2^{\beta_2} \cdot\ ... \cdot p_k^{\beta_k}$, con $0 \leq \beta_i \leq \alpha_i$. Nuevamente por _Teorema 8.9_, $d' \mid d$. Por lo tanto, por _Teorema 5.3_, $mcd(a, b) = d$.
