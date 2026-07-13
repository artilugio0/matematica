# Teorema 8.10


Sea $a = \pm p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot\ ... \cdot p_k^{\alpha_k}$.

$a \mid b$ si y solo si cada $p_i^{\alpha_i}$ divide a $b$.

**Demostración**:

($\Rightarrow$)

Si $a \mid b$, dado que cada $p_i^{\alpha_i} \mid a$, por _Teorema 2.4_, cada $p_i^{\alpha_i} \mid b$.

($\Leftarrow$)

Si cada $p_i^{\alpha_i}$ divide a $b$, dado que $mcd(p_i^{\alpha_i}, p_j^{\alpha_j}) = 1$ para $i \neq j$, por _Teorema 6.3_, $p_1^{\alpha_1} \cdot p_2^{\alpha_2} \mid b$.

Luego, como $mcd(p_3^{\alpha_3}, p_1^{\alpha_1}) = 1$ y $mcd(p_3^{\alpha_3}, p_2^{\alpha_2}) = 1$, entonces por _Teorema 6.5_, $mcd(p_3^{\alpha_3}, p_1^{\alpha_1} \cdot p_2^{\alpha_2}) = 1$. Y por _Teorema 6.3_, $p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot p_3^{\alpha_3} \mid b$.

Aplicando el mismo procedimiento con cada factor restante se llega a que $p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot\ ...\ \cdot p_k^{\alpha_k} \mid b$, por lo tanto $a \mid b$.
