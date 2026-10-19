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

## Tags

- algebra_lineal
- matriz_inversa
