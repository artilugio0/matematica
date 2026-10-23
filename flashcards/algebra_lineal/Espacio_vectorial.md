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

## Tags

- algebra_lineal
- espacios_vectoriales
