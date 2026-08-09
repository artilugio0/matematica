# Teorema 11.4


Generalización del teorema chino del resto

Sean $n_1, n_2,\ ...\ , n_k \in \mathbb{N}$.

Dado el sistema de ecuaciones de congruencia

$$
\begin{aligned}
&x \equiv a_1\ (mod\ n_1) \\
&x \equiv a_2\ (mod\ n_2) \\
&... \\
&x \equiv a_k\ (mod\ n_k) \\
\end{aligned}
$$

El sistema tiene solución si y solo si se cumple que $a_i \equiv a_j\ (mod\ mcd(n_i, n_j))$ con $1 \leq i, j \leq k$. Y si tiene solución, la solución es única módulo $mcm(n_1, n_2,\ ...\ , n_k)$.

**Demostración**:

($\Rightarrow$)

Si el sistema de ecuaciones tiene solución, entonces se tiene que $x \equiv a_i\ (mod\ n_i)$ y $x \equiv a_j\ (mod\ n_j)$ para $1 \leq i, j \leq k$. Por lo tanto, por _Teorema 10.12_, $a_i \equiv a_j\ (mod\ mcd(n_i, n_j))$.

($\Leftarrow$)

Se asume que $a_i \equiv a_j\ (mod\ mcd(n_i, n_j))$ con $1 \leq i, j \leq k$.

Sea $L = mcm(n_1, n_2,\ ...\ , n_k)$, por _Teorema 9.16_, $mcd(\frac{L}{n_1}, \frac{L}{n_2},\ ...\ , \frac{L}{n_k}) = 1$, entonces por _Teorema 5.1_, existen $u_1, u_2,\ ...\ , u_k$ tales que $\frac{L}{n_1} \cdot u_1 + \frac{L}{n_2} \cdot u_2 +\ ...\ + \frac{L}{n_k} \cdot u_k = 1$.

A continuación se demuestra que $x = a_1 \cdot \frac{L}{n_1} \cdot u_1 + a_2 \cdot \frac{L}{n_2} \cdot u_2 +\ ...\ + a_k \cdot \frac{L}{n_k} \cdot u_k$ es solución al sistema de congruencias.

Tomando un $a_j$ arbitrario, con $1 \leq j \leq k$:

$$
\begin{aligned}
x - a_j &= a_1 \cdot \frac{L}{n_1} \cdot u_1 + a_2 \cdot \frac{L}{n_2} \cdot u_2 +\ ...\ + a_k \cdot \frac{L}{n_k} \cdot u_k - a_j \\
&= a_1 \cdot \frac{L}{n_1} \cdot u_1 + a_2 \cdot \frac{L}{n_2} \cdot u_2 +\ ...\ + a_k \cdot \frac{L}{n_k} \cdot u_k - a_j \cdot 1 \\
&= a_1 \cdot \frac{L}{n_1} \cdot u_1 + a_2 \cdot \frac{L}{n_2} \cdot u_2 +\ ...\ + a_k \cdot \frac{L}{n_k} \cdot u_k - a_j \cdot (\frac{L}{n_1} \cdot u_1 + \frac{L}{n_2} \cdot u_2 +\ ...\ + \frac{L}{n_k} \cdot u_k) \\
&= (a_1 - a_j) \cdot \frac{L}{n_1} \cdot u_1 + (a_2 - a_j) \cdot \frac{L}{n_2} \cdot u_2 +\ ...\ + (a_k - a_j) \cdot \frac{L}{n_k} \cdot u_k \\
\end{aligned}
$$

Como $a_i \equiv a_j\ (mod\ mcd(n_i, n_j))$, entonces existe $\alpha_i \in \mathbb{Z}$ tal que $a_i - a_j = mcd(n_i, n_j) \cdot \alpha_i$, y por _Teorema 9.6_, $mcd(n_i, n_j) = \frac{n_i \cdot n_j}{mcm(n_i, n_j)}$. Reemplazando en la igualdad anterior se tiene:

$$
\begin{aligned}
x - a_j &= \alpha_1 \cdot \frac{n_1 \cdot n_j}{mcm(n_1, n_j)} \cdot \frac{L}{n_1} \cdot u_1 + \alpha_2 \cdot \frac{n_2 \cdot n_j}{mcm(n_2, n_j)} \cdot \frac{L}{n_2} \cdot u_2 +\ ...\ + \alpha_k \cdot \frac{n_k \cdot n_j}{mcm(n_k, n_j)} \cdot \frac{L}{n_k} \cdot u_k \\
&= n_j \cdot \alpha_1 \cdot \frac{L}{mcm(n_1, n_j)} \cdot u_1 + n_j \cdot \alpha_2 \cdot \frac{L}{mcm(n_2, n_j)} \cdot u_2 +\ ...\ + n_j \cdot \alpha_k \cdot \frac{L}{mcm(n_k, n_j)} \cdot u_k \\
&= n_j \cdot (\alpha_1 \cdot \frac{L}{mcm(n_1, n_j)} \cdot u_1 + \alpha_2 \cdot \frac{L}{mcm(n_2, n_j)} \cdot u_2 +\ ...\ + \alpha_k \cdot \frac{L}{mcm(n_k, n_j)} \cdot u_k) \\
\end{aligned}
$$

Y como $L$ es múltiplo común de $n_i$ y $n_j$, entonces por _Teorema 9.5_, $mcm(n_i, n_j) \mid L$ y $\frac{L}{mcm(n_i, n_j)} \in \mathbb{Z}$. Por lo tanto, por la última igualdad, $n_j \mid x - a_j$. Es decir $x \equiv a_j\ (mod\ n_j)$, y como $1 \leq j \leq k$, $x = a_1 \cdot \frac{L}{n_1} \cdot u_1 + a_2 \cdot \frac{L}{n_2} \cdot u_2 +\ ...\ + a_k \cdot \frac{L}{n_k} \cdot u_k$ es solución del sistema de congruencias.

Luego, sea $x'$ otra solución al sistema de congruencias, entonces se cumple que $x \equiv a_i\ (mod\ n_i)$ y $x' \equiv a_i\ (mod\ n_i)$, y por _Teorema 10.4_ y _Teorema 10.5_, $x \equiv x' (mod\ n_i)$. Luego por _Teorema 10.13_, $x \equiv x'\ (mod\ mcm(n_1, n_2,\ ...\ , n_k))$. Por lo tanto, la solución es única módulo $mcm(n_1, n_2,\ ...\ , n_k)$.

Finalmente, sea $x$ una solución al sistema de congruencias y $x'$ tal que $x \equiv x'\ (mod\ mcm(n_1, n_2,\ ...\ , n_k))$. Por _Teorema 10.19_, como $n_i \mid mcm(n_1, n_2,\ ...\ , n_k)$ se cumple que $x \equiv x'\ (mod\ n_i)$, y por _Teorema 10.4_ y _Teorema 10.5_, $x' \equiv a_i\ (mod\ n_i)$, y por lo tanto $x'$ es solución al sistema de congruencias.
