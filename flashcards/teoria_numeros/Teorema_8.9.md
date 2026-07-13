# Teorema 8.9


Sea $a \in \mathbb{Z}$ tal que su representación canónica es $a = \pm p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot\ ... \cdot p_k^{\alpha_k}$.

$d \mid a$ si y solo si $d = \pm p_1^{\beta_1} \cdot p_2^{\beta_2} \cdot\ ... \cdot p_k^{\beta_k}$ con $0 \leq \beta_i \leq \alpha_i$.

**Demostración**:

($\Rightarrow$)

Para llegar a una contradicción, se asume que $d$ tiene un factor en su representación canónica que no cumple las condiciones del teorema. Esto puede ocurrir en dos formas, que tenga un $p_i^{\beta_i}$ donde $p_i$ no es un factor primo que aparezca en la representación canónica de $a$, o que $p_i = p_j$ con $1 \leq j \leq k$ y $\beta_i > \alpha_j$.

Si $p_i$ no es un factor primo de $a$, entonces por el contrarrecíproco de _Teorema 8.3_, $p_i \nmid a$. Pero dado que $p_i \mid d \wedge d \mid a$, entonces por _Teorema 2.4_, $p_i \mid a$, llegando a un absurdo.

Si $p_i$ es un factor primo de $a$ pero $\beta_i > \alpha_j$, dado que $p_i^{\beta_i} \mid d \wedge d \mid a$, entonces por _Teorema 2.4_, $p_i^{\beta_i} \mid a$. Luego $a = p_i^{\beta_i} \cdot c$ para algún $c \in \mathbb{Z}$. Si se toma la representación canónica de $c$, el exponente de $p_i$ será mayor o igual a $0$, y por lo tanto el exponente de $p_i$ de $a$ será mayor o igual a $\beta_i$, y por lo tanto mayor a $\alpha_j$, llegando a un absurdo.

Por lo tanto $d = \pm p_1^{\beta_1} \cdot p_2^{\beta_2} \cdot\ ... \cdot p_k^{\beta_k}$ con $0 \leq \beta_i \leq \alpha_i$.

($\Leftarrow$)

Si $d = \pm p_1^{\beta_1} \cdot p_2^{\beta_2} \cdot\ ... \cdot p_k^{\beta_k}$ con $0 \leq \beta_i \leq \alpha_i$, entonces $a = \pm d \cdot (p_1^{\alpha_1 - \beta_1} \cdot p_2^{\alpha_2 - \beta_2} \cdot\ ...\ \cdot p_k^{\alpha_k - \beta_k})$, y por lo tanto $d \mid a$.
