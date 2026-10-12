# Teorema 2.10


Sea $A \in \mathbb{K}^{m \times n}$. Si $m < n$ entonces el sistema homogéneo $A \cdot X = O$ tiene una solución no trivial.

**Demostración**:

Sea $A \in \mathbb{K}^{m \times n}$ tal que $m < n$. Por _Teorema 2.8_, $A$ es equivalente por filas a una matriz $A'$ escalonada reducida por filas. Por ser equivalentes por filas, por _Teorema 2.6_, los sistemas $A \cdot X = O$ y $A' \cdot X = O$ tienen exactamente las mismas soluciones.

Si $A' = O$ cualquier $X$ será solución al sistema, y por lo tanto $A \cdot X = O$ tendrá soluciones no triviales.

Si $A' \neq O$, entonces sus primeras $r$ filas son no nulas y sus últimas $m-r$ filas son nulas. Sean $k_1 < \ \dots\ < k_r$ las columnas donde ocurren las primeras entradas no nulas de cada una de las primeras $r$ filas.

Sea $L = \{ 1,\ \dots\ , n\} \setminus \{k_1,\ \dots\ , k_r\}$ el conjunto de columnas donde no hay una primera entrada no nula. $L$ tiene $n - r$ elementos y como $r \leq m < n$, $L$ no es vacío.

El sistema de ecuaciones homogéneo asociado a $A'$ tiene $r$ ecuaciones no nulas, donde la $i$-ésima cumple que $(A')_{ij} = 0$ si $j < k_i$, y $(A')_{ij} = 0$ si $j = k_t$ con $t \neq i$, porque $A'$ es escalonada reducida por filas. Por lo tanto la $i$-ésima ecuación puede expresarse como:

$x_{k_i} + \sum\limits_{j \in L} (A')_{ij} \cdot x_j = 0$, de donde se obtiene que $x_{k_i} = - \sum\limits_{j \in L} (A')_{ij} \cdot x_j$. 

Luego, los $x_j$ para $j \in L$ pueden tomar valores arbitrarios de $\mathbb{K}$ y el resto de las incógnitas tendrán el valor especificado por la igualdad anterior. Esto forma una familia de soluciones al sistema $A' \cdot X = O$ por construcción. Si se toman valores para los $x_j$ para $j \in L$ no todos nulos, se obtendrá una solución no trivial. Y por ser $A$ equivalente por filas a $A'$, también será una solución no trivial de $A \cdot X = O$.

## Tags

- algebra_lineal
- sistema_ecuaciones_lineales
