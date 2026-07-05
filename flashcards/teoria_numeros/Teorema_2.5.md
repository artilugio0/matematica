# Teorema 2.5


Sean $a, b \in \mathbb{Z}$ no nulos.

$a \mid b \wedge b \mid a \Leftrightarrow a = \pm b$

**Demostración**:

Si $a \mid b \wedge b \mid a$, entonces existen $k_1, k_2 \in \mathbb{Z}$ tales que $b = ak_1$ y $a = bk_2$. Reemplazando $a$ en la primera igualdad se tiene que $b = b(k_1 k_2)$. Como $b \neq 0$ (porque $b \mid a$), eso implica que $k_1 k_2 = 1$, luego $(k_1 = 1 \wedge k_2 = 1) \lor (k_1 = -1 \wedge k_2 = -1)$. Por lo tanto, $a = b \lor a = -b$, es decir, $a = \pm b$.

Si $a = \pm b$, entonces $a = b1 \lor a = b(-1)$, lo que implica que $b \mid a$. Por otro lado, si $a = \pm b$, entonces $b = \pm a$, lo que implica que $a \mid b$.

Luego, $a \mid b \wedge b \mid a$.
