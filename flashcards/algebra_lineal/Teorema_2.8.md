# Teorema 2.8


Toda matriz es equivalente por filas a una matriz escalonada reducida por filas.

**Demostración**:

Por _Teorema 2.7_, toda matriz $A$ es equivalente por filas a una matriz $A'$ reducida por filas. Por ser $A'$ reducida por filas, cada columna que contenga una primera entrada no nula tendrá $0$ en el resto de sus entradas. Para que $A'$ sea escalonada reducida por filas solo es necesario ordenar las filas para que cumplan la definición. Si se reordenan las filas de la matriz $A'$, la matriz resultante seguirá siendo reducida por filas porque las entradas de las filas no cambian.

Las filas se pueden reordenar utilizando la operación elemental $ero1$. Por lo tanto puede obtenerse una matriz $A''$ escalonada reducida por filas que es equivalente por filas a $A'$, y por transitividad (_Teorema 2.4_) equivalente por filas a $A$.

## Tags

- algebra_lineal
- sistema_ecuaciones_lineales
