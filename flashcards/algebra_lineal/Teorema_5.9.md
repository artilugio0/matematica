# Teorema 5.9


Sean $V$ un espacio vectorial y $U, W$ subespacios vectoriales de $V$.

$U + W$ es suma directa si y solo si $U \cap W = \{o\}$.

**Demostración**:

($\Rightarrow$)

Si $U + W$ es suma directa, sea $v \in U \cap W$. $v$ puede representarse de dos formas: $v = v + o$ con $v \in U, o \in W$, y $v = o + v, o \in U$ y $v \in W$. Estas dos representaciones deben ser iguales dado que $U + W$ es una suma directa. Entonces $v = o$. Por lo tanto $U \cap W = \{o\}$.

($\Leftarrow$)

Si $U \cap W = \{o\}$. Si $o = u + w$ con $u \in U, w \in W$, entonces $u = -w$. Por lo tanto, $-w \in U$ y $u \in W$. Dado que $U \cap W = \{o\}$, $u = o$ y $w = o$. Por _Teorema 5.8_, $U + W$ es suma directa.

## Tags

- algebra_lineal
- subespacios
- teorema
