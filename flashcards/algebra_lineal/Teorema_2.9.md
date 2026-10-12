# Teorema 2.9


Sea $A \in \mathbb{K}^{n \times n}$. $A$ es una matriz escalonada reducida por filas sin filas nulas si y solo si $A = I_n$.

**Demostración**:

($\Rightarrow$)

Sea $A \in \mathbb{K}^{n \times n}$ una matriz escalonada reducida por filas sin filas nulas. Por no tener filas nulas, toda fila tiene una entrada no nula, y por ser escalonada y reducida por filas, las primeras entradas no nulas son $1$ y están en las columnas $k_1 < k_2 <\ \dots\ < k_n$. Como la matriz tiene $n$ columnas, eso fuerza a que la fila $i$ tenga su primera entrada no nula en la columna $i$. Finalmente, por ser reducida por filas, toda columna tiene únicamente una entrada no nula. Es decir, $(A)_{ij} = 1$ si $i = j$, y $(A)_{ij} = 0$ si $i \neq j$. Por lo tanto, $A = I_n$.


($\Leftarrow$)

Si $A = I_n$, $A$ tiene su primera entrada no nula en cada fila igual a $1$, cada entrada no nula en la fila $i$ ocurre en la columna $i$, el resto de las entradas de la matriz son $0$, y no tiene filas nulas. Por lo tanto $A$ es escalonada reducida por filas y no tiene filas nulas.

## Tags

- algebra_lineal
- sistema_ecuaciones_lineales
