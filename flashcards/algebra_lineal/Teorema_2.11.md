# Teorema 2.11


Sea $A \in \mathbb{K}^{m \times n}$. Si $A$ es equivalente por filas a una matriz escalonada reducida por filas con $p$ filas no nulas, y $p < n$ entonces el sistema homogéneo $A \cdot X = O$ tiene una solución no trivial.

**Demostración**:

Sea $A \in \mathbb{K}^{m \times n}$ equivalente por filas a $A'$ escalonada reducida por filas con $p$ filas no nulas y $p < n$.

Si $p = 0$ entonces $A' = O$ y el sistema $A' \cdot X = O$ tiene como solución cualquier $n$-upla con elementos de $\mathbb{K}$, que por _Teorema 2.6_ también son soluciones de $A \cdot X = O$. Por lo tanto $A \cdot X = O$ tiene una solución no trivial.

Si $p > 0$, sea $B$ la submatriz de $A'$ que contiene las primeras $p$ filas no nulas. Los sistemas de ecuaciones $A' \cdot X = O$ y $B \cdot X = O$ tienen las mismas ecuaciones excepto por las ecuaciones triviales correspondientes a las filas nulas de $A'$ que no agregan restricciones al sistema. Por lo tanto ambos sistemas tienen las mismas soluciones. Como $B$ tiene $p$ filas y $p < n$, por _Teorema 2.10_, $B \cdot X = O$ tiene una solución no trivial, y por lo tanto $A' \cdot X = O$ tiene una solución no trivial. Por _Teorema 2.6_, eso implica que $A \cdot X = O$ tiene una solución no trivial.

## Tags

- algebra_lineal
- sistema_ecuaciones_lineales
