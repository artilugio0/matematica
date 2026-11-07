# Teorema 6.11


Sea $V$ un espacio vectorial y $U \subseteq V$ un conjunto linealmente independiente.

Si $v \in V$ y $v \not\in \langle U \rangle$, entonces $U \cup \{v\}$ es linealmente independiente.

**Demostración**:

Si $U \cup \{v\}$ es linealmente dependiente, entonces existen $u_1,\ \dots\ , u_k \in U$ y $\alpha_1,\ \dots\ , \alpha_{k+1} \in \mathbb{K}$ no todos nulos tales que $\alpha_1 \cdot u_1 +\ \cdots\ + \alpha_k \cdot u_k + \alpha_{k+1} \cdot v = o$.

Si $\alpha_{k+1} = 0$ entonces $\alpha_1 \cdot u_1 +\ \cdots\ + \alpha_k \cdot u_k = o$ con $\alpha_1,\ \dots\ , \alpha_k$ no todos nulos. Eso implica que $U$ es linealmente dependiente, lo cual es absurdo.

Si $\alpha_{k+1} \neq 0$ entonces $v = (-{\alpha_{k+1}}^{-1} \cdot \alpha_1) \cdot u_1 +\ \cdots\ + (-{\alpha_{k+1}}^{-1} \cdot \alpha_k) \cdot u_k$, por lo tanto $v \in \langle U \rangle$, lo cual es absurdo.

Por lo tanto, $U \cup \{v\}$ es linealmente independiente.

## Tags

- algebra_lineal
- bases_y_dimension
