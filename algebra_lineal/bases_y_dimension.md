# Conjunto linealmente dependiente

Sea $V$ un espacio vectorial y $S \subseteq V$.

$S$ es linealmente dependiente si y solo si existen $s_1, \dots\ , s_k \in S$ distintos y $\alpha_1, \dots\ , \alpha_k \in \mathbb{K}$ tales que $\alpha_1 \cdot s_1 + \dots\ + \alpha_k \cdot s_k = o$ y no todos los $\alpha_i$ son nulos.

$S$ es linealmente independiente si y solo si $S$ no es linealmente dependiente.


# Teorema 6.1

Sea $V$ un espacio vectorial, $S \subseteq V$ y $U \subseteq S$.

Si $U$ es linealmente dependiente, entonces $S$ es linealmente dependiente.

**Demostración**:

Si $U$ es linealmente dependiente, entonces existen $u_1,\ \dots\ , u_k \in U$ distintos y $\alpha_1,\ \dots\ , \alpha_k \in \mathbb{K}$ tales que $\alpha_1 \cdot u_1 +\ \dots\ + \alpha_k \cdot u_k = o$ y no todos los $\alpha_i$ son nulos. Como $U \subseteq S$, entonces $u_1,\ \dots\ , u_k \in S$. Por lo tanto $S$ es linealmente dependiente.


# Teorema 6.2

Sea $V$ un espacio vectorial, $S \subseteq V$ y $U \subseteq S$.

Si $S$ es linealmente independiente, entonces $U$ es linealmente independiente.

**Demostración**:

Es el contrarrecíproco de _Teorema 6.1_.


# Teorema 6.3

Sea $V$ un espacio vectorial, $S \subseteq V$.

Si $o \in S$, entonces $S$ es linealmente dependiente.

**Demostración**:

Si $o \in S$, entonces $1 \cdot o = o$, por lo tanto $S$ es linealmente dependiente.


# Teorema 6.4

Sea $V$ un espacio vectorial, $S = \{s_1,\ \dots\ , s_k\} \subseteq V$, siendo los $s_i$ todos distintos.

$S$ es linealmente independiente si y solo si $\alpha_1 \cdot s_1 +\ \dots\ + \alpha_k \cdot s_k = o$ implica que $\alpha_1 =\ \dots\ = \alpha_k = 0$.

**Demostración**:

($\Rightarrow$)

Sea $S$ linealmente independiente. Si $\alpha_1 \cdot s_1 +\ \dots\ + \alpha_k \cdot s_k = o$, entonces se debe cumplir que $\alpha_i = 0$, de otra forma $S$ sería linealmente dependiente.

($\Leftarrow$)

Si $\alpha_1 \cdot s_1 +\ \dots\ + \alpha_k \cdot s_k = o$ implica que $\alpha_1 =\ \dots\ = \alpha_k = 0$, entonces $S$ no puede ser linealmente dependiente, porque eso implicaría que al menos un $\alpha_i \neq 0$, lo cual es una contradicción.


# Teorema 6.5

Sea $V$ un espacio vectorial, $S = \{s_1,\ \dots\ , s_k\} \subseteq V$.

$S$ es linealmente independiente si y solo si todo subconjunto de $S$ es linealmente independiente.

**Demostración**:

($\Rightarrow$)

Si $S$ es linealmente independiente, entonces todo subconjunto de $S$ debe ser linealmente independiente, de otra forma, por _Teorema 6.1_, $S$ sería linealmente dependiente, que sería una contradicción.

($\Leftarrow$)

Si todo subconjunto de $S$ es linealmente independiente, $S$ es linealmente independiente porque $S \subseteq S$.


# Base de un espacio vectorial

Sea $V$ un espacio vectorial y $B \subseteq V$.

$B$ es una base de $V$ si y solo si $B$ es linealmente independiente y $\langle B \rangle = V$.

Si $B$ es un conjunto finito, se dice que $V$ es un espacio de dimensión finita, sino $V$ es de dimensión infinita.


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


# Teorema 6.7

Sea $V$ un espacio vectorial de dimensión finita.

Toda base de $V$ tiene la misma cantidad de elementos.

**Demostración**:

Como $V$ es un espacio vectorial de dimensión finita, $V$ tiene una base $B_1$ finita de $k_1$ elementos. Sea $B_2$ una base de $V$, entonces por definición $B_2$ es linealmente independiente, por lo tanto por _Teorema 6.6_ $B_2$ es un conjunto finito. Sea $k_2$ la cantidad de elementos de $B_2$. Como $B_1$ y $B_2$ son bases de $V$, entonces $B_1, B_2 \subseteq V$ y $V = \langle B_1 \rangle$ y $V = \langle B_2 \rangle$. Entonces, por _Teorema 6.6_, $k_2 \leq k_1$ y $k_1 \leq k_2$, por lo tanto $k_1 = k_2$. Es decir, toda base de $V$ tiene la misma cantidad de elementos.


# Dimensión de un espacio vectorial

Sea $V$ un espacio vectorial de dimensión finita con base $B$.

Se define a la dimensión de $V$ como:

$dim\ V = \text{cantidad de elementos de } B$.

Se define $dim\ \{o\} = 0$.


# Teorema 6.8

Sea $V$ un espacio vectorial de dimensión $n$.

Todo subconjunto de $V$ de menos de $n$ elementos no genera a $V$.

**Demostración**:

Sea $U \subseteq V$ de $m$ elementos, siendo $m < n$.

Si $V = \langle U \rangle$, entonces por _Teorema 6.6_ todo subconjunto linealmente independiente de $V$ no tiene más de $m$ elementos. Pero si $dim\ V = n$, entonces cualquier base de $V$ es un subconjunto de $V$ linealmente independiente de $n$ elementos, y $n > m$, lo cual es una contradicción. Por lo tanto, $U$ no puede generar a $V$.


# Teorema 6.9

Sea $V$ un espacio vectorial de dimensión $n$.

Si $U \subseteq V$ es linealmente independiente y tiene $n$ elementos, entonces $U$ es una base de $V$.

**Demostración**:

Sean $u_1,\ \dots\ , u_n \in U$ vectores distintos y linealmente independientes, y sea $B = \{b_1,\ \dots\ , b_n\}$ una base de $V$.

Dado que $B$ es una base de $V$, los vectores $u_1,\ \dots\ , u_n$ pueden expresarse como combinaciones lineales de los vectores de $B$ como $u_j = \alpha_{1j} \cdot b_1 +\ \dots\ + \alpha_{nj} \cdot b_n$, con $1 \leq j \leq n$.

Entonces, toda combinación lineal de $U$ puede expresarse como:

$$
\begin{aligned}
x_1 \cdot u_1 +\ \dots\ + x_n \cdot u_n &= x_1 \cdot (\alpha_{11} \cdot b_1 +\ \dots\ + \alpha_{n1} \cdot b_n) +\ \dots\ + x_n \cdot (\alpha_{1n} \cdot b_1 +\ \dots\ + \alpha_{nn} \cdot b_n) \\
&= (x_1 \cdot \alpha_{11} +\ \dots\ + x_n \cdot \alpha_{1n}) \cdot b_1 +\ \dots\ + (x_1 \cdot \alpha_{n1} +\ \dots\ + x_n \cdot \alpha_{nn}) \cdot b_n \\
\end{aligned}
$$


Sean $P \in \mathbb{K}^{n \times n}$ tal que $(P)_{ij} = \alpha_{ij}$ y $X \in \mathbb{K}^{n \times 1}$ tal que $(X)_{i1} = x_i$.

Si $x_1 \cdot u_1 +\ \dots\ + x_n \cdot u_n = o$, dado que $U$ es linealmente independiente, eso implica que $x_1 =\ \dots\ = x_n = 0$, por lo tanto por el desarrollo anterior, $P \cdot X = O$ solo tiene la solución trivial, y por _Teorema 3.10_, $P$ es inversible.

Dado un vector arbitrario $v \in V$, el vector puede expresarse como combinación lineal de la base $B$ como $v = \beta_1 \cdot b_1 +\ \dots\ + \beta_n \cdot b_n$.

Sea $Y \in \mathbb{K}^{n \times 1}$ tal que $(Y)_{i1} = \beta_i$. Como $P$ es inversible, por _Teorema 3.14_, el sistema de ecuaciones $P \cdot X = Y$ tiene solución, lo que implica por el desarrollo de la combinación lineal de los vectores de $U$, que cualquier vector de $V$ puede ser expresado como una combinación lineal de $U$. Por lo tanto $V = \langle U \rangle$, y por ser $U$ linealmente independiente, $U$ es una base de $V$.


# Teorema 6.10

Sea $V$ un espacio vectorial de dimensión $n$.

Todo subconjunto de $V$ con más de $n$ vectores es linealmente dependiente.

**Demostración**:

Sea $U \subseteq V$ con más de $n$ vectores. Por el contrarrecíproco de _Teorema 6.6_, $U$ es linealmente dependiente.


# Teorema 6.11

Sea $V$ un espacio vectorial y $U \subseteq V$ un conjunto linealmente independiente.

Si $v \in V$ y $v \not\in \langle U \rangle$, entonces $U \cup \{v\}$ es linealmente independiente.

**Demostración**:

Si $U \cup \{v\}$ es linealmente dependiente, entonces existen $u_1,\ \dots\ , u_k \in U$ y $\alpha_1,\ \dots\ , \alpha_{k+1} \in \mathbb{K}$ no todos nulos tales que $\alpha_1 \cdot u_1 +\ \cdots\ + \alpha_k \cdot u_k + \alpha_{k+1} \cdot v = o$.

Si $\alpha_{k+1} = 0$ entonces $\alpha_1 \cdot u_1 +\ \cdots\ + \alpha_k \cdot u_k = o$ con $\alpha_1,\ \dots\ , \alpha_k$ no todos nulos. Eso implica que $U$ es linealmente dependiente, lo cual es absurdo.

Si $\alpha_{k+1} \neq 0$ entonces $v = (-{\alpha_{k+1}}^{-1} \cdot \alpha_1) \cdot u_1 +\ \cdots\ + (-{\alpha_{k+1}}^{-1} \cdot \alpha_k) \cdot u_k$, por lo tanto $v \in \langle U \rangle$, lo cual es absurdo.

Por lo tanto, $U \cup \{v\}$ es linealmente independiente.


# Teorema 6.12

Sea $V$ un espacio vectorial de dimensión finita.

Todo subconjunto linealmente independiente de $V$ es finito y forma parte de una base de $V$.

**Demostración**:

Sea $dim\ V = n$.

Sea $U \subseteq V$ linealmente independiente. Por _Teorema 6.6_, $U$ es finito y no tiene más de $n$ vectores.

Si $U$ tiene $n$ vectores, entonces por _Teorema 6.9_, $U$ es una base de $V$ y por lo tanto forma parte de una base de $V$.

Si $U$ tiene $m$ vectores con $m < n$, entonces $U$ no es una base de $V$ y $\langle U \rangle \neq V$. Sea $v_1 \in V \setminus \langle U \rangle$, como $v_1 \not\in U$, por _Teorema 6.11_, $U \cup \{v_1\}$ es linealmente independiente. Si $U \cup \{v_1\}$ tiene $n$ elementos, entonces por _Teorema 6.9_, es una base de $V$ y por lo tanto $U$ es parte de una base de $V$. Si $U \cup \{v_1\}$ tiene menos de $n$ elementos, puede repetirse el procedimiento obteniendo un vector $v_2 \in V \setminus \langle U \cup \{v_1\} \rangle$, de manera que se obtiene un nuevo conjunto linealmente independiente $U \cup \{v_1, v_2\}$. Repitiendo el procedimiento $n - m$ veces, se obtiene un conjunto de vectores linealmente independientes de $n$ elementos, que por _Teorema 6.9_, será una base de $V$.

Por lo tanto $U$ es parte de una base.


# Teorema 6.13

Sea $V$ un espacio vectorial de dimensión finita.

Todo subespacio de $V$ tiene una base finita.

**Demostración**:

Sea $dim\ V = n$.

Sea $U$ un subespacio vectorial de $V$. Por _Teorema 6.6_, todo subconjunto linealmente independiente de $U$, por ser un subconjunto de $V$, tiene como máximo $n$ elementos. Sea $B \subseteq U$ un conjunto linealmente independiente con la máxima cantidad de elementos posible, por lo mencionado anteriormente $B$ tiene una cantidad finita de elementos.

Por _Teorema 5.4_, $\langle B \rangle$ es un subespacio vectorial de $U$, entonces $\langle B \rangle \subseteq U$.

Si $u \in U$ entonces $u \in \langle B \rangle$, sino por _Teorema 6.11_, $B \cup \{u\}$ sería linealmente independiente y sería un conjunto linealmente independiente con más elementos que $B$, lo cual es absurdo. Por lo tanto $U \subseteq \langle B \rangle$, lo que implica que $\langle B \rangle = U$, y $B$ es una base de $U$.

Por lo tanto todo subespacio de $V$ tiene una base finita.


# Teorema 6.14

Sea $V$ un espacio vectorial de dimensión finita y $U$ un subespacio vectorial propio de $V$.

$dim\ U < dim\ V$.

**Demostración**:

Sea $dim\ V = n$.

Por _Teorema 6.13_, $U$ tiene una base finita. Sea $B$ una base de $U$. Por _Teorema 6.6_, $B$ no tiene más de $n$ elementos. $B$ no puede tener $n$ elementos, sino por _Teorema 6.9_ $B$ sería una base de $V$, y por lo tanto $U = \langle B \rangle = V$, con lo cual $U$ no sería un subespacio vectorial propio de $V$. Por lo tanto, $dim\ U < dim\ V$. 


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
