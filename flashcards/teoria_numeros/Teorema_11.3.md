# Teorema 11.3


Teorema chino del resto

Sean $n_1, n_2,\ ...\ , n_r \in \mathbb{N}$ coprimos de a pares, y las congruencias

$$
\begin{aligned}
&x \equiv a_1\ (mod\ n_1) \\
&x \equiv a_2\ (mod\ n_2) \\
&... \\
&x \equiv a_r\ (mod\ n_r) \\
\end{aligned}
$$

con $a_i \in \mathbb{Z}$.

Entonces el sistema de ecuaciones tiene solución, y todas las soluciones son congruentes módulo $n_1 \cdot n_2 \cdot\ ...\ \cdot n_r$.

**Demostración**:

La demostración es constructiva. Primero se busca un posible valor de $x$ para la primera congruencia. Tomando el entero $N_1 = \frac{n_1 \cdot n_2 \cdot n_3\ ... \cdot n_r}{n_1} = n_2 \cdot n_3\ ... \cdot n_r$, se cumple que $a_1 \cdot N_1 \equiv 0\
(mod\ n_i)$ para $1 \leq i \leq r \wedge i \neq 1$. Dado que $n_2, n_3,\ ...\ , n_r$ son coprimos con $n_1$, por _Teorema 6.5_, $mcd(n_1, N_1) = 1$. Luego, por _Teorema 11.2_, existe $Y_1 \in \mathbb{N}$ tal que $N_1 \cdot Y_1 \equiv 1\ (mod\ n_1)$. Por lo tanto, se cumple que $a_1 \cdot N_1 \cdot Y_1 \equiv a_1\ (mod\ n_1)$ y también $a_1 \cdot N_1 \cdot Y_1 \equiv 0\ (mod\ n_i)$ para $1 \leq i \leq r \wedge i \neq 1$.

Siguiendo el mismo procedimiento se llega a resultados análogos con $a_2 \cdot N_2 \cdot Y_2$, $a_3 \cdot N_3 \cdot Y_3$, ..., $a_r \cdot N_r \cdot Y_r$. En general $a_j \cdot N_j \cdot Y_j \equiv a_j\ (mod\ n_j)$ y también $a_j \cdot N_j \cdot Y_j \equiv 0\ (mod\ n_i)$ para $1 \leq i, j \leq r
\wedge i \neq j$.

Por lo tanto, $x = a_1 \cdot N_1 \cdot Y_1 + a_2 \cdot N_2 \cdot Y_2 +\ ...\ + a_r \cdot N_r \cdot Y_r$ es solución de todas las congruencias.

Sea $x'$ otra solución de todas las congruencias. Por _Teorema 10.4_ y _Teorema 10.5_, $x \equiv a_i \equiv x'\ (mod\ n_i)$, por lo tanto $x \equiv x'\ (mod\ n_i)$, con $1 \leq i \leq r$. Luego, $n_i \mid x - x'$. Y por _Teorema 6.3_ como cada $n_i$ es coprimo con el resto, entonces $n_1 \cdot n_2 \cdot\ ...\ \cdot n_r \mid x - x'$, lo que implica que $x \equiv x'\ (mod\ n_1 \cdot n_2 \cdot\ ...\ \cdot n_r)$.
