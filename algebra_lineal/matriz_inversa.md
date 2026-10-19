# Matriz elemental

$E \in \mathbb{K}^{n \times n}$ es una matriz elemental si existe una operación elemental de fila $ero$ tal que $E = ero(I_n)$.


# Teorema 3.1

Sean $ero$ una operación elemental de fila, $E \in \mathbb{K}^{m \times m}$ la matriz elemental $E = ero(I_m)$ y $A \in \mathbb{K}^{m \times n}$. 

$ero(A) = E \cdot A$

**Demostración**:

Si $E_1 = ero1_{k, l}(I_m) \in \mathbb{K}^{m \times m}$,

$$
\begin{aligned}

(ero1_{k, l}(A))_{ij} &= 

\begin{cases}
(A)_{lj} &i = k \\
(A)_{kj} &i = l \\
(A)_{ij} &i \neq k \wedge i \neq l \\
\end{cases} \\

&= 
\begin{cases}
(I_m)_{ll} \cdot (A)_{lj} &i = k \\
(I_m)_{kk} \cdot (A)_{kj} &i = l \\
(I_m)_{ii} \cdot (A)_{ij} &i \neq k \wedge i \neq l \\
\end{cases} \\

&= 
\begin{cases}
(E_1)_{kl} \cdot (A)_{lj} &i = k \\
(E_1)_{lk} \cdot (A)_{kj} &i = l \\
(E_1)_{ii} \cdot (A)_{ij} &i \neq k \wedge i \neq l \\
\end{cases} \\

&= 
\begin{cases}
\sum\limits_{t = 1}^m (E_1)_{kt} \cdot (A)_{tj} &i = k \\
\sum\limits_{t = 1}^m (E_1)_{lt} \cdot (A)_{tj} &i = l \\
\sum\limits_{t = 1}^m (E_1)_{it} \cdot (A)_{tj} &i \neq k \wedge i \neq l \\
\end{cases} \\

&= \sum\limits_{t = 1}^m (E_1)_{it} \cdot (A)_{tj} \\
&= (E_1 \cdot A)_{ij} \\

\end{aligned}
$$

Por lo tanto, $ero1_{k, l}(A) = E_1 \cdot A$.

Si $E_2 = ero2_{k, c}(I_m) \in \mathbb{K}^{m \times m}$, con $c \neq 0$,

$$
\begin{aligned}

(ero2_{k, c}(A))_{ij} &= 

\begin{cases}
c \cdot (A)_{ij} &i = k \\
(A)_{ij} &i \neq k \\
\end{cases} \\

&= 
\begin{cases}
(c \cdot (I_m))_{kk} \cdot (A)_{ij} &i = k \\
(I_m)_{ii} \cdot (A)_{ij} &i \neq k \\
\end{cases} \\

&= 
\begin{cases}
(E_2)_{kk} \cdot (A)_{ij} &i = k \\
(E_2)_{ii} \cdot (A)_{ij} &i \neq k \\
\end{cases} \\

&= 
\begin{cases}
\sum\limits_{t = 1}^m (E_2)_{kt} \cdot (A)_{tj} &i = k \\
\sum\limits_{t = 1}^m (E_2)_{it} \cdot (A)_{tj} &i \neq k \\
\end{cases} \\

&= \sum\limits_{t = 1}^m (E_2)_{it} \cdot (A)_{tj} \\
&= (E_2 \cdot A)_{ij} \\

\end{aligned}
$$

Por lo tanto, $ero2_{k, c}(A) = E_2 \cdot A$.

Si $E_3 = ero3_{k, l, c}(I_m) \in \mathbb{K}^{m \times m}$,

$$
\begin{aligned}

(ero3_{k, l, c}(A))_{ij} &= 

\begin{cases}
(A)_{ij} + c \cdot (A)_{lj} &i = k \\
(A)_{ij} &i \neq k \\
\end{cases} \\

&= 
\begin{cases}
(I_m)_{kk} \cdot (A)_{ij} + (c \cdot I_m)_{ll} \cdot (A)_{lj} &i = k \\
(I_m)_{ii} \cdot (A)_{ij} &i \neq k \\
\end{cases} \\

&= 
\begin{cases}
(E_3)_{kk} \cdot (A)_{ij} + (E_3)_{kl} \cdot (A)_{lj} &i = k \\
(E_3)_{ii} \cdot (A)_{ij} &i \neq k \\
\end{cases} \\

&= 
\begin{cases}
\sum\limits_{t = 1}^m (E_3)_{kt} \cdot (A)_{tj} &i = k \\
\sum\limits_{t = 1}^m (E_3)_{it} \cdot (A)_{tj} &i \neq k \\
\end{cases} \\

&= \sum\limits_{t = 1}^m (E_3)_{it} \cdot (A)_{tj} \\
&= (E_3 \cdot A)_{ij} \\

\end{aligned}

$$

Por lo tanto, $ero3_{k, l, c}(A) = E_3 \cdot A$.

Nota: la cuarta igualdad en cada caso hace uso del hecho de que la matriz elemental en cada fila tiene entradas nulas excepto en las entradas que aparecen en el paso anterior.


# Teorema 3.2

Sean $A, B \in \mathbb{K}^{m \times n}$.

$A$ es equivalente por filas a $B$ si y solo si existe $P \in \mathbb{K}^{m \times m}$ tal que $A = P \cdot B$, y $P$ es un producto de matrices elementales.

**Demostración**:

($\Rightarrow$)

Si $A$ es equivalente por filas a $B$, entonces existen las operaciones elementales de fila $ero_1,\ \dots\ , ero_k$ tales que $A = ero_k(\ \dots\ (ero_1(B)))$.
Por _Teorema 3.1_, existen las matrices elementales $E_1,\ \dots\ , E_k \in \mathbb{K}^{m \times m}$ tales que $A = E_k \cdot (\ \dots\ \cdot (E_1 \cdot B))$. Dado que el producto de matrices es asociativo, la igualdad anterior puede expresarse como $A = (E_k \cdot\ \dots\ \cdot E_1) \cdot B$. Sea $P = E_k \cdot\ \dots\ \cdot E_1$, entonces $A = P \cdot B$, siendo $P$ un producto de matrices elementales.

($\Leftarrow$)

Si $P$ es un producto de matrices elementales tal que $A = P \cdot B$, entonces $A = E_k \cdot \ \dots\ \cdot E_1 \cdot B$, siendo las $E_i$ matrices elementales. Luego, por _Teorema 3.1_, $A = ero_k(\ \dots\ (ero_1(B)))$, siendo $ero_i$ la operación elemental de fila correspondiente a la matriz elemental $E_i$. Por lo tanto, $A$ es equivalente por filas a $B$.


# Matrices inversas a izquierda y derecha

Sean $A, B, C \in \mathbb{K}^{n \times n}$.

$B$ es una matriz inversa a izquierda de $A$ si $B \cdot A = I_n$.

$C$ es una matriz inversa a derecha de $A$ si $A \cdot C = I_n$.


# Teorema 3.3

Sean $A, B, C \in \mathbb{K}^{n \times n}$, si $B \cdot A = I_n$ y $A \cdot C = I_n$, entonces $B = C$.


**Demostración**:

$B = B \cdot I_n = B \cdot (A \cdot C) = (B \cdot A) \cdot C = I_n \cdot C = C$.


# Matriz inversa

Sean $A, B \in \mathbb{K}^{n \times n}$.

$B$ es una matriz inversa de $A$ si $B \cdot A = A \cdot B = I_n$.

Si existe una matriz inversa de $A$, se dice que es inversible.


# Teorema 3.4

Sea $A \in \mathbb{K}^{n \times n}$.

Si $A$ tiene matriz inversa, entonces la matriz inversa es única. A la matriz inversa se la denota por $A^{-1}$.

**Demostración**:

Sean $B, C \in \mathbb{K}^{n \times n}$ matrices inversas de $A$. Entonces,

$B = B \cdot I_n = B \cdot (A \cdot C) = (B \cdot A) \cdot C = I_n \cdot C = C$.


# Teorema 3.5

Sea $A \in \mathbb{K}^{n \times n}$ una matriz inversible.

$(A^{-1})^{-1} = A$

**Demostración**:

Como $A$ es inversible y por definición de la matriz inversa, $A \cdot A^{-1} = A^{-1} \cdot A = I_n$. Por lo tanto $A$ es una matriz inversa de $A^{-1}$, y por _Teorema 3.4_, es la única matriz inversa de $A^{-1}$. Es decir, $(A^{-1})^{-1} = A$.


# Teorema 3.6

Sean $A, B \in \mathbb{K}^{n \times n}$ matrices inversibles. Entonces $(A \cdot B)^{-1} = B^{-1} \cdot A^{-1}$.

En general, sean $A_1,\ \dots\ , A_k \in \mathbb{K}^{n \times n}$ matrices inversibles. Entonces $(A_1 \cdot\ \dots\ \cdot A_k)^{-1} = {A_k}^{-1} \cdot\ \dots\ \cdot {A_1}^{-1}$.

**Demostración**:

Si $A, B$ son matrices inversibles, entonces existen $A^{-1}$ y $B^{-1}$. Luego,

$(A \cdot B) \cdot (B^{-1} \cdot A^{-1}) = A \cdot (B \cdot B^{-1}) \cdot A^{-1} = A \cdot I_n \cdot A^{-1} = A \cdot A^{-1} = I_n$.

$(B^{-1} \cdot A^{-1}) \cdot (A \cdot B) = B^{-1} \cdot (A^{-1} \cdot A) \cdot B = B^{-1} \cdot I_n \cdot B = B^{-1} \cdot B = I_n$.

Por lo tanto, $(A \cdot B)^{-1} = B^{-1} \cdot A^{-1}$.

El caso para $k \in \mathbb{N}$ matrices se demuestra por inducción.

Para el caso $k = 1$ no hay nada que demostrar, y el caso $k = 2$ ya fue demostrado.

Se asume que se cumple para un $k \in \mathbb{N}$ con $k \geq 2$. Sean $A_1,\ \dots\ , A_k, A_{k+1} \in \mathbb{K}^{n \times n}$ matrices inversibles.

$$
\begin{aligned}
(A_1 \cdot\ \dots\ \cdot A_k \cdot A_{k+1})^{-1} &= ((A_1 \cdot\ \dots\ \cdot A_k) \cdot A_{k+1})^{-1} &\text{(siendo } A_1 \cdot\ \dots\ \cdot A_k \text{ inversible por hipótesis inductiva)} \\
&= {A_{k+1}}^{-1} \cdot (A_1 \cdot\ \dots\ \cdot A_k)^{-1} &\text{(por el caso } k = 2 \text{)} \\
&= {A_{k+1}}^{-1} \cdot ({A_k}^{-1} \cdot\ \dots\ \cdot {A_1}^{-1}) &\text{(por hipótesis inductiva)} \\
&= {A_{k+1}}^{-1} \cdot {A_k}^{-1} \cdot\ \dots\ \cdot {A_1}^{-1}
\end{aligned}
$$

Por lo tanto $(A_1 \cdot\ \dots\ \cdot A_k)^{-1} = A_k^{-1} \cdot\ \dots\ \cdot {A_1}^{-1}$ para todo $k \in \mathbb{N}$.


# Potencias negativas de una matriz inversible

Sean $A \in \mathbb{K}^{n \times n}$ inversible y $k \in \mathbb{N}$. Se define

$A^{-k} = (A^{-1})^{k}$


# Teorema 3.7

Sean $A \in \mathbb{K}^{n \times n}$ inversible y $k \in \mathbb{N}$.

$A^{-k} = (A^k)^{-1}$

**Demostración**:

$$
\begin{aligned}
A^{-k} &= (A^{-1})^k \\
&= \prod_{i = 1}^k A^{-1} \\
&= \left( \prod_{i = 1}^k A \right)^{-1} &\text{(por Teorema 3.6)}\\
&= (A^k)^{-1}
\end{aligned}
$$


# Teorema 3.8

Las matrices elementales son inversibles.

**Demostración**:

Utilizando las operaciones inversas definidas en _Teorema 2.3_:

Sean $E_1, E_1' \in \mathbb{K}^{n \times n}$ tales que $E_1 = ero1_{i,j}(I_n)$ y $E_1' = ero1_{j,i}(I_n)$. Por _Teorema 3.1_, $E_1 \cdot E_1' = ero1_{i,j}(ero1_{j,i}(I_n)) = I_n$, y $E_1' \cdot E_1 = ero1_{j,i}(ero1_{i,j}(I_n)) = I_n$. Por lo tanto, $E_1$ es inversible.

Sean $E_2, E_2' \in \mathbb{K}^{n \times n}$ tales que $E_2 = ero2_{i,k}(I_n)$ y $E_2' = ero2_{i,k^{-1}}(I_n)$, con $k \neq 0$. Por _Teorema 3.1_, $E_2 \cdot E_2' = ero2_{i,k}(ero2_{i,k^{-1}}(I_n)) = I_n$, y $E_2' \cdot E_2 = ero2_{i,k^{-1}}(ero2_{i,k}(I_n)) = I_n$. Por lo tanto, $E_2$ es inversible.

Sean $E_3, E_3' \in \mathbb{K}^{n \times n}$ tales que $E_3 = ero3_{i,j,k}(I_n)$ y $E_3' = ero3_{i,j,-k}(I_n)$, con $i \neq j$. Por _Teorema 3.1_, $E_3 \cdot E_3' = ero3_{i,j,k}(ero3_{i,j,-k}(I_n)) = I_n$, y $E_3' \cdot E_3 = ero3_{i,j,-k}(ero3_{i,j,k}(I_n)) = I_n$. Por lo tanto, $E_3$ es inversible.

Por lo tanto todas las matrices elementales son inversibles.


# Teorema 3.9

Sea $A \in \mathbb{K}^{n \times n}$.

$A$ es inversible si y solo si es equivalente por filas a $I_n$.

**Demostración**:

($\Rightarrow$)

Sea el sistema $A \cdot X = O$. Como $A$ es inversible, existe $A^{-1}$. Multiplicando a izquierda ambos lados de la igualdad anterior se tiene que $A^{-1} \cdot A \cdot X = A^{-1} \cdot O$. Entonces, $X = O$, y el sistema homogéneo solo tiene la solución trivial. Por _Teorema 2.12_, $A$ es equivalente por filas a $I_n$.

($\Leftarrow$)

Si $A$ es equivalente por filas a $I_n$, por _Teorema 3.2_, $A = E_k \cdot\ \dots\ \cdot E_1 \cdot I_n = E_k \cdot\ \dots\ \cdot E_1$, donde las $E_i$ son matrices elementales. Por _Teorema 3.8_, las matrices $E_i$ son inversibles, y por _Teorema 3.6_, el producto de matrices $E_k \cdot\ \dots\ \cdot E_1$ es una matriz inversible. Por lo tanto $A$ es una matriz inversible.


# Teorema 3.10

Sea $A \in \mathbb{K}^{n \times n}$.

$A$ es inversible si y solo si el sistema de ecuaciones lineales homogéneo $A \cdot X = O$ solo tiene la solución trivial.

**Demostración**:

Por _Teorema 3.9_, $A$ es inversible si y solo si $A$ es equivalente por filas a $I_n$. Y por _Teorema 2.12_, $A$ es equivalente por filas a $I_n$ si y solo si $A \cdot X = O$ solo tiene la solución trivial. Por lo tanto, $A$ es inversible si y solo si $A \cdot X = O$ solo tiene la solución trivial.


# Teorema 3.11

Sea $A \in \mathbb{K}^{n \times n}$.

$A$ es inversible si y solo si es un producto de matrices elementales.

**Demostración**:

($\Rightarrow$)

Si $A$ es inversible, por _Teorema 3.9_, $A$ es equivalente por filas a $I_n$. Entonces, por _Teorema 3.2_, $A = P \cdot I_n = P$, siendo $P$ un producto de matrices elementales.

($\Leftarrow$)

Si $A$ es un producto de matrices elementales, por _Teorema 3.8_, $A$ es un producto de matrices inversibles, y entonces, por _Teorema 3.6_, $A$ es inversible.


# Teorema 3.12

Sean $A, B \in \mathbb{K}^{m \times n}$.

$A$ es equivalente por filas a $B$ si y solo si existe una matriz inversible $P \in \mathbb{K}^{m \times m}$ tal que $A = P \cdot B$.

**Demostración**:

($\Rightarrow$)

Si $A$ es equivalente por filas a $B$, por _Teorema 3.2_, existe una matriz $P$ producto de matrices elementales tal que $A = P \cdot B$. Y por _Teorema 3.11_, $P$ es inversible.

($\Leftarrow$)

Si $P$ es una matriz inversible tal que $A = P \cdot B$, por _Teorema 3.11_, $P$ es un producto de matrices elementales. Y por _Teorema 3.2_, $A$ es equivalente por filas a $B$.


# Teorema 3.13

Sea $A \in \mathbb{K}^{n \times n}$.

Si una secuencia de operaciones elementales transforma a $A$ en $I_n$, esa misma secuencia transforma a $I_n$ en $A^{-1}$.

**Demostración**:

Sea $ero_1,\ \dots\ , ero_k$ una secuencia de operaciones elementales de fila que transforman a $A$ en $I_n$. Por definición, $I_n$ es equivalente por filas a $A$ y por _Teorema 2.4_ $A$ es equivalente por filas a $I_n$. Entonces, por _Teorema 3.9_, $A$ es inversible y existe $A^{-1}$. También, por _Teorema 3.1_, $E_k \cdot\ \dots\ \cdot E_1 \cdot A = I_n$ siendo $E_i$ las matrices elementales correspondientes a las operaciones elementales de fila $ero_i$. Multiplicando a derecha en ambos lados de la igualdad por $A^{-1}$ se obtiene $E_k \cdot\ \dots\ \cdot E_1 \cdot A \cdot A^{-1} = I_n \cdot A^{-1}$ y por lo tanto, $E_k \cdot\ \dots\ \cdot E_1 \cdot I_n = A^{-1}$. Luego, por _Teorema 3.1_, las mismas operaciones elementales de fila transforman a $I_n$ en $A^{-1}$.


# Teorema 3.14

Sea $A \in \mathbb{K}^{n \times n}$.

$A$ es inversible si y solo si el sistema de ecuaciones lineales $A \cdot X = Y$ tiene solución para toda $Y \in \mathbb{K}^{n \times 1}$.

**Demostración**:


($\Rightarrow$)

Si $A$ es inversible, entonces existe $A^{-1}$. Como $A \cdot A^{-1} \cdot Y = Y$, entonces $A^{-1} \cdot Y$ es solución al sistema.

($\Leftarrow$)

Por _Teorema 2.8_, existe una matriz $R$ escalonada reducida por filas equivalente por filas a $A$. Por _Teorema 3.12_, existe una matriz $P \in \mathbb{K}^{n \times n}$ tal que $A = P \cdot R$ y $P$ es inversible. Sea $e_n \in \mathbb{K}^{n \times 1}$ tal que

$$
(e_n)_{i1} =
\begin{cases}
0 &i \neq n \\
1 &i = n \\
\end{cases}
$$

Si $A \cdot X = Y$ tiene solución para toda $Y$, entonces en particular tiene solución para $P \cdot e_n$.

Luego, si $A \cdot X = P \cdot e_n$, entonces $P \cdot R \cdot X = P \cdot e_n$. Multiplicando por $P^{-1}$ en ambos lados de la igualdad se obtiene que $R \cdot X = e_n$.

De la última igualdad se tiene que $(e_n)_{n1} = \sum\limits_{k = 1}^n (R)_{nk} \cdot (X)_{k1} = 1$. Por lo tanto, la última fila de $R$ no es nula, lo que implica que $R$ no tiene filas nulas por ser escalonada reducida por filas. Eso implica, por _Teorema 2.9_, $R = I_n$, y por lo tanto $A$ es equivalente por filas a $I_n$, lo que implica, por _Teorema 3.9_, que $A$ es inversible.


# Teorema 3.15

Sea $A \in \mathbb{K}^{n \times n}$.

Si $A$ tiene una inversa a derecha o tiene una inversa a izquierda, entonces $A$ es inversible.

**Demostración**:

Sea $B \in \mathbb{K}^{n \times n}$ una inversa a izquierda de $A$. Dado el sistema de ecuaciones lineales homogéneo $A \cdot X = O$, multiplicando a izquierda a ambos lados de la igualdad se obtiene que $B \cdot A \cdot X = X = B \cdot O = O$. Por lo tanto el sistema solo tiene la solución trivial, y por _Teorema 3.10_, $A$ es inversible.

Sea $B \in \mathbb{K}^{n \times n}$ una inversa a derecha de $A$, entonces $A \cdot B = I_n$, que implica que $A$ es una inversa a izquierda de $B$. Por lo demostrado anteriormente, $B$ es inversible. Multiplicando a derecha por $B^{-1}$ en ambos lados de la última igualdad se tiene que $A = B^{-1}$, y por _Teorema 3.5_, $A$ es inversible y su inversa es $B$.


# Teorema 3.16

Sean $A_1,\ \dots\ , A_k \in \mathbb{K}^{n \times n}$.

$A = A_1 \cdot\ \dots\ \cdot A_k$ es inversible si y solo si cada una de las matrices $A_1,\ \dots\ , A_k$ es inversible.

**Demostración**:

($\Rightarrow$)

Se demuestra por inducción.

Si $A = A_1$ y $A$ es inversible, entonces $A_1$ es inversible.

Se asume que se cumple para $k$ matrices. Sea $A = A_1 \cdot\ \dots\ \cdot A_k \cdot A_{k+1}$, tal que $A$ es inversible. Multiplicando a izquierda por $A^{-1}$ a ambos lados de la igualdad se obtiene que $I_n = A^{-1} \cdot A_1 \cdot\ \dots\ \cdot A_k \cdot A_{k+1}$. Por lo tanto $A^{-1} \cdot A_1 \cdot\ \dots\ \cdot A_k$ es una inversa a izquierda de $A_{k+1}$, y por _Teorema 3.15_, $A_{k+1}$ es inversible. Luego, por _Teorema 3.6_, $A \cdot {A_{k+1}}^{-1}$ es inversible. Como $A \cdot {A_{k+1}}^{-1} = A_1 \cdot\ \dots\ \cdot A_k \cdot A_{k+1} \cdot {A_{k+1}}^{-1} = A_1 \cdot\ \dots\ \cdot A_k$, por hipótesis inductiva, $A_1,\ \dots\ , A_k$ son inversibles. En consecuencia, cada una de las matrices $A_1,\ \dots\ , A_k, A_{k+1}$ es inversible.

Por lo tanto, para todo $k \in \mathbb{N}$: si $A = A_1 \cdot\ \dots\ \cdot A_k$ es inversible, entonces cada una de las matrices $A_1,\ \dots\ , A_k$ es inversible.

($\Leftarrow$)

Si $A = A_1 \cdot\ \dots\ \cdot A_k$ y cada una de las matrices $A_1,\ \dots\ , A_k$ es inversible, entonces, por _Teorema 3.6_, $A$ es inversible.
