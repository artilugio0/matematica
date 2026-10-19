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

## Tags

- algebra_lineal
- matriz_inversa
