# Teorema 5.4


Sea $V$ un espacio vectorial y $G \subseteq V$.

$\langle G \rangle$ es un subespacio vectorial de $V$.

**Demostración**:

Si $G = \emptyset$, entonces $\langle G \rangle = \{o\}$, que es un subespacio vectorial de $V$.

Si $G \neq \emptyset$, entonces $\langle G \rangle \neq \emptyset$. Sean $v_1, v_2 \in \langle G \rangle$. Entonces $v_1 = \alpha_1 \cdot v_{1_1} +\ \dots\ + \alpha_k \cdot v_{1_k}$ y $v_2 = \beta_1 \cdot v_{2_1} +\ \dots\ + \beta_l \cdot v_{2_l}$, con $v_{1_i}, v_{2_j} \in G$, $\alpha_i, \beta_j \in \mathbb{K}$ para $1 \leq i \leq k$ y $1 \leq j \leq l$.

Sea $\gamma \in \mathbb{K}$,

$$
\begin{aligned}
\gamma \cdot v_1 + v_2 &= \gamma \cdot (\alpha_1 \cdot v_{1_1} +\ \dots\ + \alpha_k \cdot v_{1_k}) + \beta_1 \cdot v_{2_1} +\ \dots\ + \beta_l \cdot v_{2_l} \\
&= (\gamma \cdot \alpha_1) \cdot v_{1_1} +\ \dots\ + (\gamma \cdot \alpha_k) \cdot v_{1_k} + \beta_1 \cdot v_{2_1} +\ \dots\ + \beta_l \cdot v_{2_l} \\
\end{aligned}
$$

Por lo tanto, $\gamma \cdot v_1 + v_2$ es una combinación lineal de los vectores de $G$. Entonces, $\gamma \cdot v_1 + v_2 \in \langle G \rangle$. Por lo tanto, por _Teorema 5.2_, $\langle G \rangle$ es un subespacio vectorial de $V$.

## Tags

- algebra_lineal
- subespacios
- teorema
