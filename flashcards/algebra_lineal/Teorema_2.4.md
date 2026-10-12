# Teorema 2.4


La relación de equivalencia por filas de matrices es una relación de equivalencia.

**Demostración**:

Sean $A, B, C \in \mathbb{K}^{m \times n}$.

*Reflexividad*:

$A = ero1_{1,1}(A)$. Por lo tanto, $A$ es equivalente por filas a $A$.

*Simetría*:

Se demuestra por inducción sobre la cantidad de operaciones elementales aplicadas.

Si $A$ es equivalente por filas a $B$ por medio de una única operación elemental, entonces $A = ero(B)$. Por _Teorema 2.3_, existe una operación inversa $ero'$. Luego $ero'(A) = ero'(ero(B)) = B$. Por lo tanto, $B$ es equivalente por filas a $A$.

Se asume que para cualquier par de matrices $A, B$ se cumple que si $A$ es equivalente por filas a $B$ por medio de $p$ operaciones elementales, entonces $B$ es equivalente por filas a $A$.

Si $A$ es equivalente por filas a $B$ por medio de $p+1$ operaciones elementales, entonces $A = ero_{p+1}(ero_p(\ \dots\ (ero_1(B))))$. Por _Teorema 2.3_, existe la operación $ero'_{p+1}$ que es inversa a $ero_{p+1}$. Luego, $ero'_{p+1}(A) = ero_{p+1}'(ero_{p+1}(ero_p(\ \dots\ (ero_1(B)))))$, y como $ero_{p+1}'$ y $ero_{p+1}$ se cancelan entre sí, se tiene que $ero'_{p+1}(A) = ero_p(\ \dots\ (ero_1(B)))$. Por la hipótesis inductiva, $B$ es equivalente por filas a $ero'_{p+1}(A)$, por lo tanto existen $\alpha$ operaciones elementales tales que $B = ero^{*}_\alpha(\ \dots\ (ero^{*}_1(ero'_{p+1}(A))))$. Lo que implica que $B$ es equivalente por filas a $A$.

*Transitividad*:

Si $A$ es equivalente por filas a $B$, y $B$ es equivalente por filas a $C$. Entonces $A = ero_\alpha(\ \dots\ (ero_1(B)))$ y $B = ero^{*}_\beta(\ \dots\ (ero^{*}_1(C)))$. Reemplazando a $B$ en la primera igualdad se tiene que $A = ero_\alpha(\ \dots\ (ero_1(ero^{*}_\beta(\ \dots\ (ero^{*}_1(C))))))$. Por lo tanto, $A$ es equivalente por filas a $C$.

## Tags

- algebra_lineal
- sistema_ecuaciones_lineales
