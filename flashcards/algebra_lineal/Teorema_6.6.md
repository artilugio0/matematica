# Teorema 6.6


Sea $V$ un espacio vectorial, $G \subseteq V$ finito de $m$ vectores y $S = \langle G \rangle$.

Todo conjunto linealmente independiente de vectores de $S$ es finito y no tiene más de $m$ vectores.

**Demostración**:

Sean $s_1,\ \dots\ , s_n \in S$ vectores distintos y linealmente independientes. Dado que $S = \langle G \rangle$, entonces cada $s_j \in S$ es una combinación lineal de los vectores distintos $g_1,\ \dots\ , g_m \in G$. Por lo tanto, existen $\alpha_{1j},\ \dots\ , \alpha_{mj}$ tales que $s_j = \alpha_{1j} \cdot g_1 +\ \dots\ + \alpha_{mj} \cdot g_m$, con $1 \leq i \leq m$, $1 \leq j \leq n$ y $g_i \in G$ todos distintos.

Sean $x_1,\ \dots\ , x_n \in \mathbb{K}$. Entonces,

$$
\begin{aligned}
x_1 \cdot s_1 +\ \dots\ + x_n \cdot s_n &= x_1 \cdot (\alpha_{11} \cdot g_1 +\ \dots\ + \alpha_{m1} \cdot g_m) +\ \dots\ + x_n \cdot (\alpha_{1n} \cdot g_1 +\ \dots\ + \alpha_{mn} \cdot g_m) \\
&= (x_1 \cdot \alpha_{11} +\ \dots\ + x_n \cdot \alpha_{1n}) \cdot g_1 +\ \dots\ + (x_1 \cdot \alpha_{m1} +\ \dots\ + x_n \cdot \alpha_{mn}) \cdot g_m \\
\end{aligned}
$$

Sea $A \in \mathbb{K}^{m \times n}$ tal que $(A)_{ij} = \alpha_{ij}$. Si $m < n$, entonces por _Teorema 2.10_, el sistema de ecuaciones $A \cdot X = O$ tiene soluciones no triviales. Eso implica que existen $x_1,\ \dots\ , x_n$ no todos nulos tales que $x_1 \cdot \alpha_{i1} +\ \dots\ + x_n \cdot \alpha_{in} = 0$ para $1 \leq i \leq m$, y por lo tanto $x_1 \cdot s_1 +\ \dots\ + x_n \cdot s_n = 0 \cdot g_1 +\ \dots\ + 0 \cdot g_m = o$, lo cual es absurdo porque $s_1,\ \dots\ , s_n$ son vectores linealmente independientes.

Entonces, $n \leq m$.

Sea $U \subseteq S$ un conjunto infinito de vectores. Entonces, $U$ tiene más de $m$ vectores. Sean $u_1,\ \dots\ , u_{m+1} \in U$ vectores distintos. Por lo demostrado anteriormente, ese conjunto de vectores es linealmente dependiente, y por _Teorema 6.1_, $U$ es linealmente dependiente.

Por lo tanto, todo conjunto linealmente independiente de vectores de $S$ es finito y no tiene más de $m$ vectores.

## Tags

- algebra_lineal
- bases_y_dimension
