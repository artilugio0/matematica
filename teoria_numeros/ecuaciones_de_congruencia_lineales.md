# Teorema 11.1

$a \cdot x \equiv b\ (mod\ n)$ tiene solución si y solo si $mcd(a, n) \mid b$.

Si tiene solución, entonces tiene $mcd(a, n)$ soluciones incongruentes módulo $n$.

**Demostración**:

Si $a \cdot x \equiv b\ (mod\ n)$, por definición de congruencia se tiene que $n \mid a \cdot x - b$. Y por definición de divisibilidad, existe un $k \in \mathbb{Z}$ tal que $a \cdot x - b = n \cdot k$. Es decir que la ecuación de congruencia tendrá solución si y solo si la ecuación $a \cdot x + (-n) \cdot k = b$ tiene solución (donde $x$ y $k$ son las incógnitas). Por _Teorema 5.4_, la ecuación tiene solución si y solo si $mcd(a, n) \mid b$.

Si la ecuación de congruencia tiene solución, sea $x_0$ una solución particular. Por lo anteriormente expuesto y por _Teorema 7.1_, cualquier otra solución será de la forma $x_0 - \frac{n}{mcd(a, n)} \cdot t$, con $t$ tomando cualquier valor de $\mathbb{Z}$.

Sean $t, t' \in \mathbb{Z}$ tales que las soluciones a la ecuación de congruencia sean congruentes módulo $n$. Entonces, $x_0 - \frac{n}{mcd(a, n)} \cdot t \equiv x_0 - \frac{n}{mcd(a, n)} \cdot t'\ (mod\ n)$. Lo que implica que $\frac{n}{mcd(a, n)} \cdot t \equiv \frac{n}{mcd(a, n)} \cdot t'\ (mod\ n)$. Luego, como $mcd(n, \frac{n}{mcd(a, n)}) = \frac{n}{mcd(a, n)}$, por _Teorema 10.21_, $t \equiv t'\ (mod\ mcd(a, n))$. Por lo tanto, si se toman valores de $t$ incongruentes módulo $mcd(a, n)$, las soluciones serán incongruentes módulo $n$.

Si se toman $t, t'$ congruentes módulo $mcd(a, n)$, sean $x_t, x_{t'}$ las soluciones asociadas a esos valores. Luego se tiene que $x_t - x_{t'} = (x_0 - \frac{n}{mcd(a, n)} \cdot t) - (x_0 - \frac{n}{mcd(a, n)} \cdot t') = \frac{n}{mcd(a, n)} \cdot (t' - t)$. Y como $mcd(a, n) \mid t' - t$, entonces $x_t - x_{t'} = \frac{n}{mcd(a, n)} \cdot k' \cdot mcd(a, n) = n \cdot k'$, para algún $k' \in \mathbb{Z}$. Por lo tanto $n \mid x_t - x_{t'}$, es decir, $x_t \equiv x_{t'}\ (mod\ n)$.

En conclusión, todas las soluciones incongruentes módulo $n$ se obtienen tomando valores incongruentes de $t$ módulo $mcd(a, n)$. Y dado que todo entero es congruente a algún valor entre $0$ y $mcd(a, n) - 1$, entonces $mcd(a, n)$ es la cantidad total de soluciones incongruentes módulo $n$.


# Teorema 11.2

La ecuación $a \cdot x \equiv 1\ (mod\ n)$ tiene solución si y solo si $mcd(a, n) = 1$ y la solución es única módulo $n$.

**Demostración**:

Por _Teorema 11.1_, la ecuación tiene solución si y solo si $mcd(a, n) \mid 1$. Y por _Teorema 2.2_, tendrá solución si y solo si $mcd(a, n) = 1$. Luego, si tiene solución, por _Teorema 11.1_, la solución será única módulo $n$.


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
