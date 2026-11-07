# Teorema 6.16


Sean $V$ un espacio vectorial de dimensión finita y $W$ un subespacio vectorial de $V$.

Existe $U$, un subespacio vectorial de $V$, tal que $W \oplus U = V$.

**Demostración**:

Por _Teorema 6.13_, $W$ tiene una base finita $\{w_1,\ \dots\ , w_m\}$, y por _Teorema 6.12_, se puede extender a una base de $V$ $\{w_1,\ \dots\ , w_m, u_1,\ \dots\ , u_n \}$. Sea $U = \langle \{u_1,\ \dots\ , u_n \} \rangle$. Sea $v \in V$, entonces existen $\alpha_1,\ \dots\ , \alpha_m, \beta_1,\ \dots\ , \beta_n$ tales que:

$$
\begin{aligned}
v &= \alpha_1 \cdot w_1 +\ \dots\ + \alpha_m \cdot w_m + \beta_1 \cdot u_1 +\ \dots\ + \beta_n \cdot u_n \\
v &= (\alpha_1 \cdot w_1 +\ \dots\ + \alpha_m \cdot w_m) + (\beta_1 \cdot u_1 +\ \dots\ + \beta_n \cdot u_n) \\
v &= w + u \quad w \in W,\ u \in U \\
\end{aligned}
$$

Por lo tanto $V = W + U$.

Sea $t \in W \cap U$, entonces $t \in W$ y $t \in U$, entonces $t = \alpha_1' \cdot w_1 +\ \dots\ + \alpha_m' \cdot w_m$ y $t = \beta_1' \cdot u_1 +\ \dots\ + \beta_n' \cdot u_n$. Por lo tanto, $\alpha_1' \cdot w_1 +\ \dots\ + \alpha_m' \cdot w_m = \beta_1' \cdot u_1 +\ \dots\ + \beta_n' \cdot u_n$, lo que implica que $\alpha_1' =\ \dots\ = \alpha_m' = \beta_1' =\ \dots\ = \beta_n' = 0$ porque $\{w_1,\ \dots\ , w_m, u_1,\ \dots\ , u_n \}$ es linealmente independiente. Luego $t = o$ y $W \cap U = \{o\}$. Por lo tanto, por _Teorema 5.9_, $W + U$ es una suma directa.

Entonces, $W \oplus U = V$.

## Tags

- algebra_lineal
- bases_y_dimension
