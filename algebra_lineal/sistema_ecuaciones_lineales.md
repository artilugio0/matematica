# Sistema de ecuaciones lineales

Sean $\mathbb{K}$ un cuerpo, y $m, n \in \mathbb{N}$.

Un sistema de ecuaciones lineales es un listado de $m$ ecuaciones donde cada ecuación es una suma
de $n$ incógnitas multiplicadas cada una por un elemento de $\mathbb{K}$ igualada a un elemento
de $\mathbb{K}$.

$$
\begin{cases}
a_{11} \cdot x_1 + \dots + a_{1n} \cdot x_n = y_1 \\
a_{21} \cdot x_1 + \dots + a_{2n} \cdot x_n = y_2 \\
\vdots \\
a_{m1} \cdot x_1 + \dots + a_{mn} \cdot x_n = y_m \\
\end{cases}
$$

Con $a_{ij}, y_i \in \mathbb{K}$, para $1 \leq i \leq m$ y $1 \leq j \leq n$.


# Solución de un sistema de ecuaciones lineales

Dado un sistema de ecuaciones lineales de $m$ ecuaciones y $n$ incógnitas, una solución del sistema
es una $n$-upla $(x_1, \dots, x_n)$ de elementos de $\mathbb{K}$ que satisfacen las $m$ ecuaciones del sistema.


# Sistema de ecuaciones lineales homogéneo

Dado el sistema de ecuaciones lineales

$$
\begin{cases}
a_{11} \cdot x_1 + \dots + a_{1n} \cdot x_n = y_1 \\
a_{21} \cdot x_1 + \dots + a_{2n} \cdot x_n = y_2 \\
\vdots \\
a_{m1} \cdot x_1 + \dots + a_{mn} \cdot x_n = y_m \\
\end{cases}
$$

El sistema es homogéneo si $y_1 = y_2 =\ \dots\ = y_m = 0$.


# Combinación lineal de ecuaciones lineales

Dado el sistema de ecuaciones lineales

$$
\begin{cases}
a_{11} \cdot x_1 + \dots + a_{1n} \cdot x_n = y_1 \\
a_{21} \cdot x_1 + \dots + a_{2n} \cdot x_n = y_2 \\
\vdots \\
a_{m1} \cdot x_1 + \dots + a_{mn} \cdot x_n = y_m \\
\end{cases}
$$

Una ecuación es una combinación lineal de las ecuaciones de ese sistema si puede obtenerse como suma de un múltiplo por un escalar de $\mathbb{K}$ (posiblemente nulo) de cada una de las ecuaciones del sistema.


# Teorema 2.1

Dado un sistema de ecuaciones lineales, toda solución del sistema también es solución de cualquier ecuación que sea una combinación lineal de las ecuaciones del sistema.

**Demostración**:

Dado el sistema de $m$ ecuaciones lineales con $n$ incógnitas

$$
\begin{cases}
a_{11} \cdot x_1 + \dots + a_{1n} \cdot x_n = y_1 \\
a_{21} \cdot x_1 + \dots + a_{2n} \cdot x_n = y_2 \\
\vdots \\
a_{m1} \cdot x_1 + \dots + a_{mn} \cdot x_n = y_m \\
\end{cases}
$$

y una solución $(v_1,\ \dots\ , v_n)$.

Una ecuación que es una combinación lineal de las $m$ ecuaciones del sistema tendrá la forma:

$C_1 \cdot (a_{11} \cdot x_1 + \dots + a_{1n} \cdot x_n) +\ \dots\ + C_m \cdot (a_{m1} \cdot x_1 + \dots + a_{mn} \cdot x_n) = C_1 \cdot y_1 +\ \dots\ + C_m \cdot y_m$

Con $C_i \in \mathbb{K}$, para $1 \leq i \leq m$.

Como $(v_1,\ \dots\ , v_n)$ es solución del sistema, se cumple que:

$$
\begin{cases}
a_{11} \cdot v_1 + \dots + a_{1n} \cdot v_n = y_1 \\
a_{21} \cdot v_1 + \dots + a_{2n} \cdot v_n = y_2 \\
\vdots \\
a_{m1} \cdot v_1 + \dots + a_{mn} \cdot v_n = y_m \\
\end{cases}
$$

Multiplicando la $i$-ésima ecuación por $C_i$, y sumando las igualdades se obtiene:

$$
\begin{aligned}
C_1 \cdot (a_{11} \cdot v_1 + \dots + a_{1n} \cdot v_n) +\ \dots\ + C_m \cdot (a_{m1} \cdot v_1 + \dots + a_{mn} \cdot v_n) = C_1 \cdot y_1 +\ \dots\ + C_m \cdot y_m
\end{aligned}
$$

Por lo tanto, $(v_1,\ \dots\ , v_n)$ también es una solución de la ecuación.


# Sistema de ecuaciones lineales equivalentes

Dos sistemas de ecuaciones lineales son equivalentes si todas las ecuaciones de ambos sistemas son combinaciones lineales de las ecuaciones del otro.


# Teorema 2.2

Si dos sistemas de ecuaciones lineales son equivalentes entonces tienen las mismas soluciones.

**Demostración**:

Sean dos sistemas de ecuaciones lineales equivalentes, y $S_1, S_2$ los conjuntos de soluciones de cada uno.

Como son sistemas equivalentes, todas las ecuaciones del primer sistema son combinaciones lineales de las ecuaciones del segundo sistema. Por _Teorema 2.1_, cada solución del segundo sistema es solución de cada una de las ecuaciones del primer sistema, por lo tanto $S_2 \subseteq S_1$.

También, todas las ecuaciones del segundo sistema son combinaciones lineales de las ecuaciones del primer sistema. Por _Teorema 2.1_, cada solución del primer sistema es solución de cada una de las ecuaciones del segundo sistema, por lo tanto $S_1 \subseteq S_2$.

Lo que implica que $S_1 = S_2$.


# Sistema de ecuaciones lineales en forma matricial

Todo sistema de $m$ ecuaciones lineales y $n$ incógnitas puede expresarse como una ecuación matricial.

Dado el sistema

$$
\begin{cases}
a_{11} \cdot x_1 + \dots + a_{1n} \cdot x_n = y_1 \\
a_{21} \cdot x_1 + \dots + a_{2n} \cdot x_n = y_2 \\
\vdots \\
a_{m1} \cdot x_1 + \dots + a_{mn} \cdot x_n = y_m \\
\end{cases}
$$

El mismo sistema puede expresarse como

$A \cdot X = Y$

Se definen las matrices como:

- $A \in \mathbb{K}^{m \times n}$ es la matriz de coeficientes, siendo $(A)_{ij} = a_{ij}$.
- $X \in \mathbb{K}^{n \times 1}$ es la matriz de incógnitas, siendo $(X)_{j1} = x_{j}$.
- $Y \in \mathbb{K}^{m \times 1}$ es la matriz de términos independientes, siendo $(Y)_{i1} = y_{i}$.

Para $1 \leq i \leq m$ y $1 \leq j \leq n$.


# Operaciones elementales de fila sobre matrices

Son tres funciones que se definen sobre la familia de matrices de $m$ filas sobre el cuerpo $\mathbb{K}$:

- $ero1_{k, l}$: Intercambiar fila $k$ por fila $l$
- $ero2_{k, c}$: Multiplicar fila $k$ por un escalar $c \in \mathbb{K}, c \neq 0$
- $ero3_{k, l, c}$: Sumarle a la fila $k$ otra fila distinta $l$ multiplicada por un escalar $c \in \mathbb{K}$

Dada $A \in \mathbb{K}^{m \times n}$:

$$
\begin{aligned}

\left( ero1_{k, l}(A) \right)_{ij} &=
\begin{cases}
(A)_{lj} &i = k \\
(A)_{kj} &i = l \\
(A)_{ij} &i \neq k \wedge i \neq l \\
\end{cases} \\
\\

\left( ero2_{k, c}(A) \right)_{ij} &=
\begin{cases}
c \cdot (A)_{ij} &i = k \\
(A)_{ij} &i \neq k \\
\end{cases} \\
\\

\left( ero3_{k, l, c}(A) \right)_{ij} &=
\begin{cases}
(A)_{ij} + c \cdot (A)_{lj} &i = k \\
(A)_{ij} &i \neq k \\
\end{cases} \\

\end{aligned}
$$


# Teorema 2.3

Para toda operación elemental de fila existe una operación elemental de fila del mismo tipo tal que si se aplica una seguida de la otra se obtiene la matriz original.

Se dice que esa operación es una operación inversa de la original.

**Demostración**:

Sea $A \in \mathbb{K}^{m \times n}$.

Para $ero1_{k,l}$, una operación inversa es $ero1_{l,k}$ dado que $\left( ero1_{k,l}(ero1_{l,k}(A)) \right)_{ij} = A_{ij}$ y $\left( ero1_{l,k}(ero1_{k,l}(A)) \right)_{ij} = A_{ij}$.

Para $ero2_{k,c}$ con $c \neq 0$, una operación inversa es $ero2_{k,c^{-1}}$ dado que $\left( ero2_{k,c}(ero2_{k,c^{-1}}(A)) \right)_{ij} = A_{ij}$ y $\left( ero2_{k,c^{-1}}(ero2_{k,c}(A)) \right)_{ij} = A_{ij}$.

Para $ero3_{k,l,c}$, una operación inversa es $ero3_{k,l,-c}$ dado que $\left( ero3_{k,l,c}(ero3_{k,l,-c}(A)) \right)_{ij} = A_{ij}$ y $\left( ero3_{k,l,-c}(ero3_{k,l,c}(A)) \right)_{ij} = A_{ij}$.


# Matrices equivalentes por filas

Dos matrices son equivalentes por filas si se puede obtener una aplicando una secuencia finita de operaciones elementales de fila a la otra.


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


# Combinación lineal de filas de una matriz

Sea $A \in \mathbb{K}^{m \times n}$ y $B \in \mathbb{K}^{p \times n}$. Una fila $k$ de $B$ es una combinación lineal de las filas de $A$ si existen $C_1,\ \dots\ , C_m \in \mathbb{K}$ tales que $(B)_{kj} = \sum\limits_{i = 1}^m C_{i} \cdot (A)_{ij}$ para todo $1 \leq j \leq n$.


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


# Teorema 2.6

Sean $A, B \in \mathbb{K}^{m \times n}$. Si $A$ y $B$ son equivalentes por filas entonces los sistemas de ecuaciones lineales $A \cdot X = O$ y $B \cdot X = O$ tienen exactamente las mismas soluciones.

**Demostración**:

Si $A$ es equivalente por filas a $B$, por _Teorema 2.4_, $B$ es equivalente por filas a $A$. Por _Teorema 2.5_, las filas de $A$ son combinaciones lineales de las de $B$ y también las filas de $B$ son combinaciones lineales de las de $A$. Como la matriz de términos independientes es nula en los sistemas de ecuaciones homogéneos $A \cdot X = O$ y $B \cdot X = O$, las ecuaciones de cada sistema son combinaciones lineales de las ecuaciones del otro sistema y por lo tanto son equivalentes. Luego, por _Teorema 2.2_, tienen exactamente las mismas soluciones.


# Matriz reducida por filas

Una matriz $A \in \mathbb{K}^{m \times n}$ es reducida por filas si cumple:

- La primera entrada no nula de cada fila es $1$
- Si la fila $i$ tiene su primera entrada no nula en la columna $j$, entonces $(A)_{kj} = 0$ para todo $k \neq i$


# Teorema 2.7

Toda matriz es equivalente por filas a una matriz reducida por filas.

**Demostración**:

La demostración es constructiva.

Sea $A \in \mathbb{K}^{m \times n}$. Si $A = O$, entonces $A$ es una matriz reducida por filas, y por lo tanto es equivalente por filas a una matriz reducida por filas (_Teorema 2.4_).

Si $A \neq O$, entonces existe una entrada no nula $d = (A)_{kl}$ tal que $(A)_{ij} = 0$ si $j < l$. Se obtiene la matriz equivalente por filas $A' = ero2_{1, d^{-1}}(ero1_{1, k}(A))$. $A'$ tiene en su primera fila su primera entrada no nula igual a $1$. Y todas las entradas de las columnas anteriores a la de esa entrada son $0$.

Sean $c_\alpha = (A')_{\alpha l}$ para $2 \leq \alpha \leq m$. Se obtiene la matriz equivalente por filas $A''$ aplicando las $m-1$ operaciones elementales $ero3_{2, 1, -c_2},\ \dots\ , ero3_{m, 1, -c_m}$ a $A'$. Luego, $A''$ es una matriz equivalente por filas a $A$ tal que su primera entrada no nula en la fila $1$ es $1$, y cualquier otra entrada en esa misma columna o en columnas anteriores es $0$.

Luego, se repite el procedimiento nuevamente con la fila $2$, dejando en la fila $2$ una fila tal que su primera entrada no nula es $1$ y el resto de las entradas de esa columna son $0$, y también las entradas de columnas anteriores son $0$ excepto por la primera entrada no nula de la fila $1$. Esto último está garantizado ya que la fila $2$ tiene entrada nula en la columna correspondiente a esa entrada en la fila $1$.

Repitiendo el procedimiento con las filas restantes hasta que no haya más filas no nulas se obtiene una matriz reducida por filas. Por lo tanto $A$ es equivalente por filas a una matriz reducida por filas.


# Matriz escalonada reducida por filas

Una matriz $A \in \mathbb{K}^{m \times n}$ es escalonada reducida por filas si cumple:

- Es reducida por filas
- Todas las filas nulas son posteriores a las filas no nulas
- Si $A$ tiene $r$ filas no nulas, y la fila $i$ de $A$ tiene su primera entrada no nula en la columna $k_i$, entonces se cumple que $k_1 < k_2 <\ \dots\ < k_r$.


# Teorema 2.8

Toda matriz es equivalente por filas a una matriz escalonada reducida por filas.

**Demostración**:

Por _Teorema 2.7_, toda matriz $A$ es equivalente por filas a una matriz $A'$ reducida por filas. Por ser $A'$ reducida por filas, cada columna que contenga una primera entrada no nula tendrá $0$ en el resto de sus entradas. Para que $A'$ sea escalonada reducida por filas solo es necesario ordenar las filas para que cumplan la definición. Si se reordenan las filas de la matriz $A'$, la matriz resultante seguirá siendo reducida por filas porque las entradas de las filas no cambian.

Las filas se pueden reordenar utilizando la operación elemental $ero1$. Por lo tanto puede obtenerse una matriz $A''$ escalonada reducida por filas que es equivalente por filas a $A'$, y por transitividad (_Teorema 2.4_) equivalente por filas a $A$.


# Teorema 2.9

Sea $A \in \mathbb{K}^{n \times n}$. $A$ es una matriz escalonada reducida por filas sin filas nulas si y solo si $A = I_n$.

**Demostración**:

($\Rightarrow$)

Sea $A \in \mathbb{K}^{n \times n}$ una matriz escalonada reducida por filas sin filas nulas. Por no tener filas nulas, toda fila tiene una entrada no nula, y por ser escalonada y reducida por filas, las primeras entradas no nulas son $1$ y están en las columnas $k_1 < k_2 <\ \dots\ < k_n$. Como la matriz tiene $n$ columnas, eso fuerza a que la fila $i$ tenga su primera entrada no nula en la columna $i$. Finalmente, por ser reducida por filas, toda columna tiene únicamente una entrada no nula. Es decir, $(A)_{ij} = 1$ si $i = j$, y $(A)_{ij} = 0$ si $i \neq j$. Por lo tanto, $A = I_n$.


($\Leftarrow$)

Si $A = I_n$, $A$ tiene su primera entrada no nula en cada fila igual a $1$, cada entrada no nula en la fila $i$ ocurre en la columna $i$, el resto de las entradas de la matriz son $0$, y no tiene filas nulas. Por lo tanto $A$ es escalonada reducida por filas y no tiene filas nulas.


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


# Teorema 2.11

Sea $A \in \mathbb{K}^{m \times n}$. Si $A$ es equivalente por filas a una matriz escalonada reducida por filas con $p$ filas no nulas, y $p < n$ entonces el sistema homogéneo $A \cdot X = O$ tiene una solución no trivial.

**Demostración**:

Sea $A \in \mathbb{K}^{m \times n}$ equivalente por filas a $A'$ escalonada reducida por filas con $p$ filas no nulas y $p < n$.

Si $p = 0$ entonces $A' = O$ y el sistema $A' \cdot X = O$ tiene como solución cualquier $n$-upla con elementos de $\mathbb{K}$, que por _Teorema 2.6_ también son soluciones de $A \cdot X = O$. Por lo tanto $A \cdot X = O$ tiene una solución no trivial.

Si $p > 0$, sea $B$ la submatriz de $A'$ que contiene las primeras $p$ filas no nulas. Los sistemas de ecuaciones $A' \cdot X = O$ y $B \cdot X = O$ tienen las mismas ecuaciones excepto por las ecuaciones triviales correspondientes a las filas nulas de $A'$ que no agregan restricciones al sistema. Por lo tanto ambos sistemas tienen las mismas soluciones. Como $B$ tiene $p$ filas y $p < n$, por _Teorema 2.10_, $B \cdot X = O$ tiene una solución no trivial, y por lo tanto $A' \cdot X = O$ tiene una solución no trivial. Por _Teorema 2.6_, eso implica que $A \cdot X = O$ tiene una solución no trivial.


# Teorema 2.12

Sea $A \in \mathbb{K}^{n \times n}$. $A$ es equivalente por filas a $I_n$ si y solo si el sistema de ecuaciones $A \cdot X = O$ solo tiene la solución trivial.

**Demostración**:

($\Rightarrow$)

Si $A$ es equivalente por filas a $I_n$, entonces por _Teorema 2.6_, $A \cdot X = O$ tiene exactamente las mismas soluciones que $I_n \cdot X = O$, que es un sistema de ecuaciones trivial donde cada incógnita toma el valor $0$, por lo tanto solo tiene la solución trivial. Luego, $A \cdot X = O$ tiene únicamente la solución trivial.

($\Leftarrow$)

Sea $A \in \mathbb{K}^{n \times n}$ tal que $A \cdot X = O$ solo tiene la solución trivial. Por _Teorema 2.8_, $A$ es equivalente por filas a una matriz escalonada reducida por filas $A'$. $A'$ no debe tener filas nulas, porque de otra forma la cantidad de filas no nulas sería menor a la cantidad de columnas, y por _Teorema 2.11_, $A' \cdot X = O$ tendría soluciones no triviales, lo que implicaría por _Teorema 2.6_ que $A \cdot X = O$ tendría soluciones no triviales.

Por lo tanto $A'$ es una matriz de $n$ filas y $n$ columnas escalonada reducida por filas sin filas nulas. Por _Teorema 2.9_, $A' = I_n$. Luego, $A$ es equivalente por filas a $I_n$.


# Matriz aumentada de un sistema de ecuaciones lineales

Sea el sistema de ecuaciones lineales $A \cdot X = Y$, con $A \in \mathbb{K}^{m \times n}$ y $Y \in \mathbb{K}^{m \times 1}$. La matriz aumentada del sistema es la matriz $A' \in \mathbb{K}^{m \times (n+1)}$ tal que:

$$
(A')_{ij} =
\begin{cases}
(A)_{ij} &1 \leq j \leq n \\
(Y)_{i1} &j = n + 1 \\
\end{cases}
$$


# Teorema 2.13

Sean $A \in \mathbb{K}^{m \times n}$, el sistema de ecuaciones lineales $A \cdot X = Y$ y $A'$ su matriz aumentada.

$(x_1,\ \cdots,\ x_n)$ es solución del sistema de ecuaciones $A \cdot X = Y$ si y solo si $(x_1,\ \cdots\ , x_n, -1)$ es solución del sistema $A' \cdot X' = O$.

**Demostración**:

La $i$-ésima ecuación del sistema $A \cdot X = Y$ es $\sum\limits_{k=1}^n (A)_{ik} \cdot x_k = (Y)_{i1}$ para $1 \leq i \leq m$.

Que tiene las mismas soluciones que la ecuación $(\sum\limits_{k=1}^n (A)_{ik} \cdot x_k) + (-1) \cdot (Y)_{i1} = 0$.

Que tiene las mismas soluciones que la ecuación $(\sum\limits_{k=1}^n (A')_{ik} \cdot x_k) + (A')_{i(n+1)} \cdot x_{n+1} = 0$, con $x_{n+1} = -1$, por definición de la matriz aumentada.

Que es la misma ecuación que la $i$-ésima ecuación del sistema $A' \cdot X' = O$, con $x_{n+1} = -1$.

Como se cumple para todo $1 \leq i \leq m$, si $(x_1,\ \cdots,\ x_n)$ es solución del sistema original, entonces $(x_1,\ \cdots,\ x_n, -1)$ es solución del sistema extendido. Y si $(x_1,\ \cdots,\ x_n, -1)$ es solución del sistema extendido, entonces $(x_1,\ \cdots,\ x_n)$ es solución del sistema original.
