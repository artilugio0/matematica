# Espacio vectorial

Sean $\mathbb{K}$ un cuerpo, $V$ un conjunto, $+: V \times V \to V$ una
ley de composición interna, y $\cdot: \mathbb{K} \times V \to V$ una
ley de composición externa.

$(V, \mathbb{K}, +, \cdot)$ es un espacio vectorial si se cumple que:

Ley de composición interna:

1. Asociatividad: $\forall\ v_1, v_2, v_3 \in V: (v_1 + v_2) + v_3 = v_1 + (v_2 + v_3)$
2. Neutro: $\exists\ o \in V \mid \forall\ v \in V: v + o = o + v = v$
3. Inverso: $\forall\ v \in V: \exists\ -v \in V \mid v + (-v) = (-v) + v = o$
4. Conmutatividad: $\forall\ v_1, v_2 \in V: v_1 + v_2 = v_2 + v_1$

Ley de composición externa:

5. Neutro: $\forall\ v \in V: 1 \cdot v = v$
6. Asociatividad: $\forall\ \alpha_1, \alpha_2 \in \mathbb{K}: \forall\ v \in V: (\alpha_1 \cdot \alpha_2) \cdot v = \alpha_1 \cdot (\alpha_2 \cdot v)$
7. Distributividad respecto de la suma de vectores: $\forall\ \alpha \in \mathbb{K}: \forall\ v_1, v_2 \in V: \alpha \cdot (v_1 + v_2) = \alpha \cdot v_1 + \alpha \cdot v_2$
8. Distributividad respecto de la suma del cuerpo: $\forall\ \alpha_1, \alpha_2 \in \mathbb{K}: \forall\ v \in V: (\alpha_1 + \alpha_2) \cdot v = \alpha_1 \cdot v + \alpha_2 \cdot v$

A los elementos del conjunto $V$ se los denomina vectores.

A los elementos del cuerpo $\mathbb{K}$ se los denomina escalares.

A $(V, \mathbb{K}, +, \cdot)$ se lo denomina espacio vectorial sobre el cuerpo $\mathbb{K}$.

Cuando las operaciones y/o el cuerpo queden claros del contexto, o se esté hablando de un espacio vectorial en abstracto basta con decir que $V$ es un espacio vectorial.

Notación:

Sean $v_1, v_2 \in V$, "$v_1 + (-v_2)$" puede escribirse como "$v_1 - v_2$".

# Teorema 4.1

Unicidad del neutro aditivo.

Sean $V$ un espacio vectorial y $v_1, v_2 \in V$.

$v_1 + v_2 = v_2 + v_1 = v_2$ si y solo si $v_1 = o$.

**Demostración**:

($\Rightarrow$)

Si $v_1 + v_2 = v_2$, entonces $v_1 + v_2 - v_2 = v_2 - v_2$. Por lo tanto, $v_1 = o$.

($\Leftarrow$)

Si $v_1 = o$, entonces $v_1 + v_2 = o + v_2 = v_2$.


#teorema


# Teorema 4.2

Unicidad del inverso aditivo.

Sean $V$ un espacio vectorial y $v_1, v_2 \in V$.

$v_1 + v_2 = v_2 + v_1 = o$ si y solo si $v_1 = -v_2$.

**Demostración**:

($\Rightarrow$)

Si $v_1 + v_2 = o$, entonces $v_1 + v_2 - v_2 = o - v_2$. Por lo tanto, $v_1 = -v_2$.

($\Leftarrow$)

Si $v_1 = -v_2$, entonces $v_1 + v_2 = -v_2 + v_2 = o$.


#teorema


# Teorema 4.3

Sean $V$ un espacio vectorial y $\alpha \in \mathbb{K}$.

$\alpha \cdot o = o$.

**Demostración**:

$\alpha \cdot o = \alpha \cdot (o + o) = \alpha \cdot o + \alpha \cdot o$.

Por _Teorema 4.1_, $\alpha \cdot o = o$.


#teorema


# Teorema 4.4

Sean $V$ un espacio vectorial y $v \in V$.

$0 \cdot v = o$.

**Demostración**:

$0 \cdot v = (0 + 0) \cdot v = 0 \cdot v + 0 \cdot v$.

Por _Teorema 4.1_, $0 \cdot v = o$.


#teorema


# Teorema 4.5

Sean $V$ un espacio vectorial y $v \in V$.

$-(-v) = v$.

**Demostración**:

$v + (-v) = o$.

Por _Teorema 4.2_, $-(-v) = v$.


#teorema


# Teorema 4.6

Sean $V$ un espacio vectorial y $v \in V$.

$(-1) \cdot v = -v$.

**Demostración**:

$v + (-1) \cdot v = 1 \cdot v + (-1) \cdot v = (1 - 1) \cdot v = 0 \cdot v = o$.

Por _Teorema 4.2_, $(-1) \cdot v = -v$.


#teorema


# Teorema 4.7

Sean $V$ un espacio vectorial, $v \in V$ y $\alpha \in \mathbb{K}$.

$\alpha \cdot v = o$ si y solo si $v = o \lor \alpha = 0$.

**Demostración**:

($\Rightarrow$)

Si $\alpha = 0$, no hay nada que demostrar.

Si $\alpha \neq 0$, entonces $\alpha^{-1} \cdot \alpha \cdot v = \alpha^{-1} \cdot o$. Por _Teorema 4.3_, $1 \cdot v = v = \alpha^{-1} \cdot o = o$.

($\Leftarrow$)

Si $v = o$, por _Teorema 4.3_, $\alpha \cdot v = o$.

Si $\alpha = 0$, por _Teorema 4.4_, $\alpha \cdot v = o$.


#teorema


# Combinación lineal

Sean $V$ un espacio vectorial y $v_1,\ \dots\ , v_k \in V$.

$w$ es una combinación lineal de los vectores $v_1,\ \dots\ , v_k$ si existen $\alpha_1,\ \dots\ , \alpha_k \in \mathbb{K}$ tales que $w = \sum\limits_{i = 1}^k \alpha_i \cdot v_i = \alpha_1 \cdot v_1 +\ \dots\ + \alpha_k \cdot v_k$.


# Teorema 4.8

Sean $V$ un espacio vectorial y $S = \{v_1,\ \dots\ , v_k\} \subseteq V$.

Si $w$ es una combinación lineal de los vectores de $S$, entonces $w \in V$.

**Demostración**:

Se demuestra por inducción sobre la cantidad de vectores de $S$.

Si $S = \{v_1\}$ y $w$ es una combinación lineal de los vectores de $S$, entonces $w = \alpha_1 \cdot v_1$, con $\alpha_1 \in \mathbb{K}$. Por la definición de espacio vectorial, $w \in V$.

Se asume que se cumple para los conjuntos de $k$ vectores.

Si $S = \{v_1,\ \dots\ , v_k, v_{k+1}\} \subseteq V$ y $w$ es una combinación lineal de los vectores de $S$, entonces $w = \sum\limits_{i = 1}^{k + 1} \alpha_i \cdot v_i$, con $\alpha_i \in \mathbb{K}$. Luego, $w = (\sum\limits_{i = 1}^k \alpha_i \cdot v_i) + \alpha_{k+1} \cdot v_{k+1}$. Por hipótesis inductiva, $\sum\limits_{i = 1}^k \alpha_i \cdot v_i \in V$, y por definición de espacio vectorial $\alpha_{k+1} \cdot v_{k+1} \in V$. Por definición de espacio vectorial entonces, $w \in V$.

Por lo tanto, queda demostrado para cualquier conjunto no vacío y finito de vectores.


#teorema
