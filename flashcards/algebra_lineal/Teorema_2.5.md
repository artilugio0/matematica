# Teorema 2.5


Sean $A, B \in \mathbb{K}^{m \times n}$. Si $A$ y $B$ son equivalentes por filas entonces las filas de $A$ son combinaciones lineales de las filas de $B$.

**Demostración**:

Se demuestra por inducción sobre la cantidad de operaciones elementales de fila.

Si $A$ es equivalente por filas a $B$ por medio de una única operación elemental de fila, entonces $A = ero1_{k, l}(B) \lor A = ero2_{k, c}(B) \lor A = ero3_{k, l, c}(B)$.

Si $A = ero1_{k, l}(B)$, las filas de $A$ son las mismas filas que las de $B$ en distinto orden. Por lo tanto son combinaciones lineales de las filas de $B$.

Si $A = ero2_{k, c}(B)$, todas las filas de $A$ excepto la fila $k$ son las mismas filas que las de $B$, y la fila $k$ es un múltiplo de la fila $k$ de $B$. Por lo tanto son combinaciones lineales de las filas de $B$.

Si $A = ero3_{k, l, c}(B)$, todas las filas de $A$ excepto la fila $k$ son las mismas filas que las de $B$, y la fila $k$ es la fila $k$ de $B$ más un múltiplo de la fila $l$ de $B$. Por lo tanto son combinaciones lineales de las filas de $B$.

Se asume que para cualquier par de matrices $A, B$ se cumple que si $A$ es equivalente por filas a $B$ por medio de $p$ operaciones elementales, entonces las filas de $A$ son combinaciones lineales de las filas de $B$.

Si $A$ es equivalente por filas a $B$ por medio de $p+1$ operaciones elementales de fila, entonces $A = ero_{p+1}(ero_p(\ \dots\ (ero_1(B))))$. Por la hipótesis inductiva, $A = ero_{p+1}(B')$, donde $B'$ es una matriz cuyas filas son combinaciones lineales de las filas de $B$.

Si $A = ero1_{k', l'}(B')$, las filas de $A$ son las mismas filas que las de $B'$ en distinto orden, que son combinaciones lineales de las filas de $B$. Por lo tanto son combinaciones lineales de las filas de $B$.

Si $A = ero2_{k', c'}(B')$, todas las filas de $A$ excepto la fila $k'$ son las mismas filas que las de $B'$, y por lo tanto son combinaciones lineales de las filas de $B$. Y la fila $k'$ es un múltiplo de la fila $k'$ de $B'$, como la fila $k'$ de $B'$ es una combinación lineal de las filas de $B$, la fila $k'$ de $A$ también es una combinación lineal de las filas de $B$. Por lo tanto todas las filas son combinaciones lineales de las filas de $B$.

Si $A = ero3_{k', l', c'}(B')$, todas las filas de $A$ excepto la fila $k'$ son las mismas filas que las de $B'$, y por lo tanto son combinaciones lineales de las filas de $B$. Y la fila $k'$ es la fila $k'$ de $B'$ más un múltiplo de la fila $l'$ de $B'$, que ambas son combinaciones lineales de las filas de $B$, y por lo tanto también es una combinación lineal de las filas de $B$. Por lo tanto las filas son combinaciones lineales de las filas de $B$.

## Tags

- algebra_lineal
- sistema_ecuaciones_lineales
