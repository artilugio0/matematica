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

## Tags

- algebra_lineal
- sistema_ecuaciones_lineales
