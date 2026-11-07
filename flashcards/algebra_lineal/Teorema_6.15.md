# Teorema 6.15


Sea $V$ un espacio vectorial de dimensión finita, y $W_1, W_2$ subespacios de $V$.

$W_1 + W_2$ es de dimensión finita, y $dim\ (W_1 + W_2) = dim\ W_1 + dim\ W_2 - dim\ (W_1 \cap W_2)$

**Demostración**:

$W_1 \cap W_2$ es un subespacio vectorial de $W_1$, por _Teorema 6.13_, $W_1 \cap W_2$ tiene una base finita de $k$ elementos $\{v_1,\ \dots\ , v_k\}$. Por _Teorema 6.12_, $\{v_1,\ \dots\ , v_k\}$ puede extenderse a una base de $W_1$ de $k + m$ vectores de la forma $\{v_1,\ \dots\ , v_k, t_1,\ \dots\ , t_m\}$.

De forma análoga, se puede encontrar una base de $W_2$ de $k + n$ vectores de la forma $\{v_1,\ \dots\ , v_k, u_1,\ \dots\ , u_n\}$.

La unión de ambas bases es $\{v_1,\ \dots\ , v_k, t_1,\ \dots\ , t_m, u_1,\ \dots\ , u_n\}$ y está incluida en $W_1 + W_2$, dado que todos los vectores pertenecen a $W_1$ o a $W_2$.

Sea $(w_1 + w_2) \in (W_1 + W_2)$, tal que $w_1 \in W_1$ y $w_2 \in W_2$. Como $W_1, W_2 \subseteq \langle \{v_1,\ \dots\ , v_k, t_1,\ \dots\ , t_m, u_1,\ \dots\ , u_n\} \rangle$, entonces $(w_1 + w_2) \in \langle \{v_1,\ \dots\ , v_k, t_1,\ \dots\ , t_m, u_1,\ \dots\ , u_n\} \rangle$. Por lo tanto, $\langle \{v_1,\ \dots\ , v_k, t_1,\ \dots\ , t_m, u_1,\ \dots\ , u_n\} \rangle = W_1 + W_2$.

Sean $\alpha_1,\ \dots\ , \alpha_k, \beta_1,\ \dots\ , \beta_m, \gamma_1,\ \dots\ , \gamma_n \in \mathbb{K}$ tales que $\alpha_1 \cdot v_1 + \ \dots\ + \alpha_k \cdot v_k + \beta_1 \cdot t_1 +\ \dots\ + \beta_m \cdot t_m + \gamma_1 \cdot u_1 +\ \dots\ + \gamma_n \cdot u_n = o$. Entonces $\gamma_1 \cdot u_1 +\ \dots\ + \gamma_n \cdot u_n = -\alpha_1 \cdot v_1 - \ \dots\ - \alpha_k \cdot v_k - \beta_1 \cdot t_1 -\ \dots\ - \beta_m \cdot t_m$. Por lo tanto, $\gamma_1 \cdot u_1 +\ \dots\ + \gamma_n \cdot u_n$ pertenece a $W_1$ por ser una combinación lineal de vectores de $W_1$, y también pertenece a $W_2$ por ser una combinación lineal de vectores de $W_2$, lo que implica que pertenece a $W_1 \cap W_2$. 

Entonces, existen $\delta_1,\ \dots\ , \delta_k$ tales que  $\gamma_1 \cdot u_1 +\ \dots\ + \gamma_n \cdot u_n = \delta_1 \cdot v_1 +\ \dots\ + \delta_k \cdot v_k$. Como $\{v_1,\ \dots\ , v_k, u_1,\ \dots\ , u_n\}$ es linealmente independiente, la igualdad anterior implica que $\gamma_1 =\ \dots\ = \gamma_n = 0$.

Por lo tanto, de la primera igualdad se tiene que $\alpha_1 \cdot v_1 + \ \dots\ + \alpha_k \cdot v_k + \beta_1 \cdot t_1 +\ \dots\ + \beta_m \cdot t_m = o$. Dado que $\{v_1,\ \dots\ , v_k, t_1,\ \dots\ , t_m\}$ es linealmente independiente, eso implica que $\alpha_1 =\ \dots\ = \alpha_k = \beta_1 =\ \dots\ = \beta_m = 0$. Lo que implica que $\{v_1,\ \dots\ , v_k, t_1,\ \dots\ , t_m, u_1,\ \dots\ , u_n\}$ es linealmente independiente y es una base de $W_1 + W_2$.

Luego,

$$
\begin{aligned}
dim\ (W_1 + W_2) &= k + m + n \\
&= k + m + n + k - k \\
&= (k + m) + (k + n) - k \\
&= dim\ W_1 + dim\ W_2 - dim\ (W_1 \cap W_2) \\
\end{aligned}
$$

## Tags

- algebra_lineal
- bases_y_dimension
