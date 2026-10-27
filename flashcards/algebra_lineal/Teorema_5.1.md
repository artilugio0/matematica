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

## Tags

- algebra_lineal
- subespacios
- teorema
