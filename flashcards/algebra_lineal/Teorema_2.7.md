# Teorema 2.7


Toda matriz es equivalente por filas a una matriz reducida por filas.

**Demostración**:

La demostración es constructiva.

Sea $A \in \mathbb{K}^{m \times n}$. Si $A = O$, entonces $A$ es una matriz reducida por filas, y por lo tanto es equivalente por filas a una matriz reducida por filas (_Teorema 2.4_).

Si $A \neq O$, entonces existe una entrada no nula $d = (A)_{kl}$ tal que $(A)_{ij} = 0$ si $j < l$. Se obtiene la matriz equivalente por filas $A' = ero2_{1, d^{-1}}(ero1_{1, k}(A))$. $A'$ tiene en su primera fila su primera entrada no nula igual a $1$. Y todas las entradas de las columnas anteriores a la de esa entrada son $0$.

Sean $c_\alpha = (A')_{\alpha l}$ para $2 \leq \alpha \leq m$. Se obtiene la matriz equivalente por filas $A''$ aplicando las $m-1$ operaciones elementales $ero3_{2, 1, -c_2},\ \dots\ , ero3_{m, 1, -c_m}$ a $A'$. Luego, $A''$ es una matriz equivalente por filas a $A$ tal que su primera entrada no nula en la fila $1$ es $1$, y cualquier otra entrada en esa misma columna o en columnas anteriores es $0$.

Luego, se repite el procedimiento nuevamente con la fila $2$, dejando en la fila $2$ una fila tal que su primera entrada no nula es $1$ y el resto de las entradas de esa columna son $0$, y también las entradas de columnas anteriores son $0$ excepto por la primera entrada no nula de la fila $1$. Esto último está garantizado ya que la fila $2$ tiene entrada nula en la columna correspondiente a esa entrada en la fila $1$.

Repitiendo el procedimiento con las filas restantes hasta que no haya más filas no nulas se obtiene una matriz reducida por filas. Por lo tanto $A$ es equivalente por filas a una matriz reducida por filas.

## Tags

- algebra_lineal
- sistema_ecuaciones_lineales
