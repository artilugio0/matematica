# Subespacio vectorial

Sean $(V, \mathbb{K}, +, \cdot)$ un espacio vectorial, y sea $S \subseteq V$. $S$ es un subespacio de $V$ si $S$ es un espacio vectorial sobre $\mathbb{K}$ restringiendo el dominio de las operaciones de $+$ y $\cdot$ a $S$.


# Teorema 5.1

Sean $V$ un espacio vectorial, y $S \subseteq V$.

$S$ es un subespacio vectorial si y solo si:

1. $o \in S$
2. $\forall\ s_1, s_2 \in S: s_1 + s_2 \in S$
3. $\forall\ s \in S: \forall\ \alpha \in \mathbb{K}: \alpha \cdot s \in S$

**Demostración**:

($\Rightarrow$)

Si $S$ es un subespacio vectorial de $V$, entonces $S$ es un espacio vectorial. Por lo tanto existe el neutro aditivo $o_s$ y cumple que $o_s + o_s = o_s$. Como $o_s \in V$, por _Teorema 4.1_, $o_s = o$.

Por otro lado, por definición de espacio vectorial, las condiciones 2 y 3 se cumplen.

($\Leftarrow$)

Por las condiciones 2 y 3, las operaciones $+$ y $\cdot$ son cerradas en $S$.

Si $s_1, s_2, s_3 \in S$, entonces $s_1, s_2, s_3 \in V$. Por lo tanto, $(s_1 + s_2) + s_3 = s_1 + (s_2 + s_3)$.

Si $s \in S$, entonces $s \in V$, por lo tanto $s + o = o + s = s$.

Si $s \in S$, entonces $(-1) \cdot s = -s \in S$, y $s + (- s) = (-s) + s = o$.

Si $s_1, s_2 \in S$, entonces $s_1, s_2 \in V$. Por lo tanto, $s_1 + s_2 = s_2 + s_1$.

Si $\alpha_1, \alpha_2 \in \mathbb{K}$ y $s \in S$, entonces $s \in V$. Por lo tanto, $(\alpha_1 \cdot \alpha_2) \cdot s = \alpha_1 \cdot (\alpha_2 \cdot s)$.

Si $s \in S$, entonces $1 \cdot s = s$.

Si $\alpha \in \mathbb{K}$ y $s_1, s_2 \in S$, entonces $s_1, s_2 \in V$. Por lo tanto, $\alpha \cdot (s_1 + s_2) = \alpha \cdot s_1 + \alpha \cdot s_2$.

Si $\alpha_1, \alpha_2 \in \mathbb{K}$ y $s \in S$, entonces $s \in V$. Por lo tanto, $(\alpha_1 + \alpha_2) \cdot s = \alpha_1 \cdot s + \alpha_2 \cdot s$.

Por lo tanto, $S$ es un espacio vectorial.


#teorema


# Teorema 5.2

Sean $V$ un espacio vectorial, $S \subseteq V$ y $S \neq \emptyset$.

$S$ es un subespacio vectorial de $V$ si y solo si para todo $\alpha \in \mathbb{K}$ y para todos $s, t \in S$ se cumple que $\alpha \cdot s + t \in S$.

**Demostración**:

($\Rightarrow$)

Si $S$ es un subespacio vectorial de $V$, por _Teorema 4.8_, $\alpha \cdot s + t \in S$ para todo $\alpha \in \mathbb{K}$ y para todos $s, t \in S$.

($\Leftarrow$)

Si para todo $\alpha \in \mathbb{K}$ y para todos $s, t \in S$ se cumple que $\alpha \cdot s + t \in S$:

- Sea $s \in S$, $(-1) \cdot s + s = -s + s = o \in S$. Por lo tanto, $o \in S$. 
- Sean $s, t \in S$, $1 \cdot s + t \in S$. Por lo tanto, $s + t \in S$.
- Sean $s \in S$ y $\alpha \in \mathbb{K}$, $\alpha \cdot s + o \in S$. Por lo tanto, $\alpha \cdot s \in S$.

Por _Teorema 5.1_, $S$ es un subespacio vectorial de $V$.


#teorema


# Teorema 5.3

Sean $V$ un espacio vectorial, $S_1,\ \dots\ , S_k$ subespacios vectoriales de $V$.

$\bigcap\limits_{i = 1}^k S_i$ es un subespacio vectorial de $V$.

**Demostración**:

Por ser subespacios vectoriales, $o$ pertenece a cada uno de los subespacios $S_1,\ \dots\ , S_k$, y por lo tanto $o \in \bigcap\limits_{i = 1}^k S_i$. Entonces, $\bigcap\limits_{i = 1}^k S_i \neq \emptyset$.

Sean $s, t \in \bigcap\limits_{i = 1}^k S_i$ y $\alpha \in \mathbb{K}$. $s, t$ pertenecen a cada uno de los $S_1,\ \dots\ , S_k$, y por _Teorema 4.8_, $\alpha \cdot s + t$ también pertenece a cada uno de los subespacios. Por lo tanto, $\alpha \cdot s + t \in \bigcap\limits_{i = 1}^k S_i$.

Por _Teorema 5.2_, $\bigcap\limits_{i = 1}^k S_i$ es un subespacio vectorial de $V$.


#teorema


# Conjunto generado

Sea $V$ un espacio vectorial y $S \subseteq V$.

Se define al conjunto generado por $S$ como:

$\langle S \rangle = \{s \mid s \text{ es combinación lineal de los vectores de } S \}$

Se define a $\langle \emptyset \rangle = \{o\}$.


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


#teorema


# Teorema 5.5

Sea $V$ un espacio vectorial y $G \subseteq V$.

$\langle G \rangle$ es la intersección de todos los subespacios de $V$ que contienen a $G$.

**Demostración**:

Sea $W$ la intersección de todos los subespacios de $V$ que contienen a $G$.

Sea $g \in \langle G \rangle$, entonces $g$ es una combinación lineal de los vectores de $G$. Como $G$ está incluido en todos los subespacios en la intersección que define a $W$, por _Teorema 4.8_, $g$ pertenece a cada uno de esos subespacios. Entonces $g \in W$, y por lo tanto, $\langle G \rangle \subseteq W$.


Como $G \subseteq V$, por _Teorema 5.4_, $\langle G \rangle$ es un subespacio de $V$. Entonces, $\langle G \rangle$ es uno de los subespacios de $V$ en la intersección que define a $W$. Si $w \in W$, entonces $w \in \langle G \rangle$. Por lo tanto, $W \subseteq \langle G \rangle$.

De donde se concluye que $\langle G \rangle = W$.


#teorema


# Suma de conjuntos de vectores

Sean $V$ un espacio vectorial y $W_1,\ \dots\ , W_k \subseteq V$.

Se define la suma de los conjuntos como:

$W_1 +\ \dots\ + W_k = \{ w_1 +\ \dots\ + w_k \mid w_i \in W_i \}$


# Teorema 5.6

Sean $V$ un espacio vectorial y $S_1,\ \dots\ , S_k$ subespacios vectoriales de $V$.

$S_1 +\ \dots\ + S_k$ es un subespacio vectorial de $V$.

**Demostración**:

$o$ pertenece a $S_1,\ \dots\, S_k$, entonces $\sum\limits_{i = 1}^k o = o \in (S_1 +\ \dots\ + S_k)$. Por lo tanto $S_1 +\ \dots\ + S_k \neq \emptyset$.

Sean $s, t \in (S_1 +\ \dots\ + S_k)$. Entonces $s = s_1 +\ \dots\ + s_k$ y $t = t_1 +\ \dots\ + t_k$, con $s_i, t_i \in S_i$.

Sea $\alpha \in \mathbb{K}$,

$$
\begin{aligned}
\alpha \cdot s + t &= \alpha \cdot (s_1 +\ \dots\ + s_k) + t_1 +\ \dots\ + t_k \\
&= \alpha \cdot s_1 +\ \dots\ + \alpha \cdot s_k + t_1 +\ \dots\ + t_k \\
&= (\alpha \cdot s_1 + t_1) +\ \dots\ + (\alpha \cdot s_k + t_k) \\
\end{aligned}
$$

Como $\alpha \cdot s_i + t_i \in S_i$, entonces $\alpha \cdot s + t \in S_1 +\ \dots\ + S_k$. Por _Teorema 5.2_, $S_1 +\ \dots\ + S_k$ es subespacio vectorial de $V$.


#teorema


# Teorema 5.7

Sean $V$ un espacio vectorial y $S_1,\ \dots\ , S_k$ subespacios vectoriales de $V$.

$S_1 +\ \dots\ + S_k = \langle S_1 \cup\ \dots\ \cup S_k \rangle$.

**Demostración**:

Sea $s_1 +\ \dots\ + s_k \in (S_1 +\ \dots\ + S_k)$. Como $s_1,\ \dots, s_k \in (S_1 \cup\ \dots\ \cup S_k)$, y $s_1 +\ \dots\ + s_k$ es una combinación lineal de $(S_1 \cup\ \dots\ \cup S_k)$, entonces $s_1 +\ \dots\ + s_k \in \langle S_1 \cup\ \dots\ \cup S_k \rangle$, y $(S_1 +\ \dots\ + S_k) \subseteq \langle S_1 \cup\ \dots\ \cup S_k \rangle$.

Sea $s \in \langle S_1 \cup\ \dots\ \cup S_k \rangle$, $s$ es una combinación lineal de los vectores de $S_1 \cup\ \dots\ \cup S_k$. Por la propiedad conmutativa, $s$ puede expresarse como $s = \sum\limits_{i \in I_1} \alpha_{1_i} \cdot s_{1_i} +\ \dots\ + \sum\limits_{i \in I_k} \alpha_{k_i} \cdot s_{k_i}$. Como $\sum\limits_{i \in I_j} \alpha_{j_i} \cdot s_{j_i} \in S_j$, entonces $s \in (S_1 +\ \dots\ + S_k)$, y $\langle S_1 \cup\ \dots\ \cup S_k \rangle \subseteq (S_1 +\ \dots\ + S_k)$.

Por lo tanto, $S_1 +\ \dots\ + S_k = \langle S_1 \cup\ \dots\ \cup S_k \rangle$.


#teorema


# Suma directa

Sean $V$ un espacio vectorial y $W_1,\ \dots\ , W_k$ subespacios vectoriales de $V$.

$W_1 +\ \dots\ + W_k$ es una suma directa si se cumple que todo vector $v \in (W_1 +\ \dots\ + W_k)$ puede representarse de forma única como $v = w_1 +\ \dots\ + w_k$, con $w_i \in W_i$ para $1 \leq i \leq k$.

Si $W_1 +\ \dots\ + W_k$ es suma directa, se denota como $W_1 \oplus\ \dots\ \oplus W_k$


# Teorema 5.8

Sean $V$ un espacio vectorial y $W_1,\ \dots\ , W_k$ subespacios vectoriales de $V$.

$W_1 +\ \dots\ + W_k$ es una suma directa si y solo si se cumple: si $o = w_1 +\ \dots\ + w_k$ con $w_i \in W_i$, entonces $w_1 = \dots = w_k = o$.

**Demostración**:

($\Rightarrow$)

Sea $W_1 +\ \dots\ + W_k$ una suma directa. Si $o = w_1 +\ \dots\ + w_k$ con $w_i \in W_i$, dado que es suma directa y $o = o +\ \dots\ + o$, entonces $w_1 = \dots\ = w_k = o$.

($\Leftarrow$)

Se asume que $o = w_1 +\ \dots\ + w_k$ con $w_i \in W_i$ implica $w_1 = \dots\ = w_k = o$.

Sea $v = w_1 +\ \dots\ + w_k$ y $v = u_1 +\ \dots\ + u_k$, con $w_i, u_i \in W_i$. Entonces, $v - v = w_1 +\ \dots\ + w_k  - (u_1 +\ \dots\ + u_k)$. Lo que implica que $o = (w_1 - u_1) +\ \dots\ + (w_k - u_k)$. Entonces, por hipótesis, $w_1 - u_1 = o,\ \dots\ , w_k - u_k = o$. Por lo tanto, $w_1 = u_1,\ \dots\ , w_k = u_k$. Lo que quiere decir que $W_1 +\ \dots\ + W_k$ es suma directa.


#teorema


# Teorema 5.9

Sean $V$ un espacio vectorial y $U, W$ subespacios vectoriales de $V$.

$U + W$ es suma directa si y solo si $U \cap W = \{o\}$.

**Demostración**:

($\Rightarrow$)

Si $U + W$ es suma directa, sea $v \in U \cap W$. $v$ puede representarse de dos formas: $v = v + o$ con $v \in U, o \in W$, y $v = o + v, o \in U$ y $v \in W$. Estas dos representaciones deben ser iguales dado que $U + W$ es una suma directa. Entonces $v = o$. Por lo tanto $U \cap W = \{o\}$.

($\Leftarrow$)

Si $U \cap W = \{o\}$. Si $o = u + w$ con $u \in U, w \in W$, entonces $u = -w$. Por lo tanto, $-w \in U$ y $u \in W$. Dado que $U \cap W = \{o\}$, $u = o$ y $w = o$. Por _Teorema 5.8_, $U + W$ es suma directa.
 

#teorema
