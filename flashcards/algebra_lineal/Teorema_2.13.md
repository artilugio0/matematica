# Teorema 2.13


Sean $A \in \mathbb{K}^{m \times n}$, el sistema de ecuaciones lineales $A \cdot X = Y$ y $A'$ su matriz aumentada.

$(x_1,\ \cdots,\ x_n)$ es solución del sistema de ecuaciones $A \cdot X = Y$ si y solo si $(x_1,\ \cdots\ , x_n, -1)$ es solución del sistema $A' \cdot X' = O$.

**Demostración**:

La $i$-ésima ecuación del sistema $A \cdot X = Y$ es $\sum\limits_{k=1}^n (A)_{ik} \cdot x_k = (Y)_{i1}$ para $1 \leq i \leq m$.

Que tiene las mismas soluciones que la ecuación $(\sum\limits_{k=1}^n (A)_{ik} \cdot x_k) + (-1) \cdot (Y)_{i1} = 0$.

Que tiene las mismas soluciones que la ecuación $(\sum\limits_{k=1}^n (A')_{ik} \cdot x_k) + (A')_{i(n+1)} \cdot x_{n+1} = 0$, con $x_{n+1} = -1$, por definición de la matriz aumentada.

Que es la misma ecuación que la $i$-ésima ecuación del sistema $A' \cdot X' = O$, con $x_{n+1} = -1$.

Como se cumple para todo $1 \leq i \leq m$, si $(x_1,\ \cdots,\ x_n)$ es solución del sistema original, entonces $(x_1,\ \cdots,\ x_n, -1)$ es solución del sistema extendido. Y si $(x_1,\ \cdots,\ x_n, -1)$ es solución del sistema extendido, entonces $(x_1,\ \cdots,\ x_n)$ es solución del sistema original.

## Tags

- algebra_lineal
- sistema_ecuaciones_lineales
