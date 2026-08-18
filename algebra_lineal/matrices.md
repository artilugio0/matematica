# Matriz

Sean $m, n \in \mathbb{N}$ y $\mathbb{K}$ un cuerpo.

Una **matriz de $m \times n$ sobre el cuerpo $\mathbb{K}$** es una función $A: \mathbb{N}_m \times \mathbb{N}_n \to \mathbb{K}$.

Nota: $\mathbb{N}_h = \{1, 2,\ ...\ , h - 1, h\}$

**Notación**:

$$
\begin{aligned}
(A)_{ij} = A(i, j) \\
a_{ij} = A(i, j) \\
\end{aligned}
$$

$$
A =
\begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}
$$

# $\mathbb{K}^{m \times n}$

Es el conjunto de matrices de $m \times n$ sobre el cuerpo $\mathbb{K}$.

$$
\mathbb{K}^{m \times n} = \left\{
\begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}
\mid a_{ij} \in \mathbb{K},\ i \in \mathbb{N}_m,\ j \in \mathbb{N}_n
\right\}
$$

# Igualdad entre matrices

Sean $A, B \in \mathbb{K}^{m \times n}$.

$A = B \Leftrightarrow \forall\ i \in \mathbb{N}_m,\ j \in \mathbb{N}_n:\ (A)_{ij} = (B)_{ij}$


# Suma entre matrices

Sean $A, B \in \mathbb{K}^{m \times n}$.

Se define $A + B \in \mathbb{K}^{m \times n}$ tal que:

$(A + B)_{ij} = (A)_{ij} + (B)_{ij}$


# Ley de composición externa o acción de $\mathbb{K}$ en $\mathbb{K}^{m \times n}$

$\cdot: \mathbb{K} \times \mathbb{K}^{m \times n} \to \mathbb{K}^{m \times n} \mid (\lambda \cdot A)_{ij} = \lambda \cdot (A)_{ij}$


# Producto de matrices

Sean $A \in \mathbb{K}^{m \times n}, B \in \mathbb{K}^{n \times p}$.

Se define $A \cdot B \in \mathbb{K}^{m \times p}$ tal que:

$(A \cdot B)_{ij} = \sum\limits_{k=1}^{n} (A)_{ik} \cdot (B)_{kj}$


# Interpretaciones de producto de matrices

TODO:

- Por filas
- Por columnas

# Traspuesta

Sea $A \in \mathbb{K}^{m \times n}$.

Se define $A^T \in \mathbb{K}^{n \times m}$ tal que:

$(A^T)_{ij} = (A)_{ji}$


# Traza

Sea $A \in \mathbb{K}^{n \times n}$.

$\operatorname{tr}(A) = \sum\limits_{i = 1}^n (A)_{ii}$


# Matriz Identidad

$I_n \in \mathbb{K}^{n \times n} \mid (I_n)_{ij} =
\begin{cases}
1 & \text{si } i = j \\
0 & \text{si } i \neq j \\
\end{cases}$

Ejemplo:

$I_3 =
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{pmatrix}$


# Matrices canónicas

$E^{kl} \in \mathbb{K}^{m \times n} \mid (E^{kl})_{ij} =
\begin{cases}
1 & \text{si } i = k \wedge j = l \\
0 & \text{si } i \neq k \lor j \neq l \\
\end{cases}$

Ejemplo:

$E^{24} =
\begin{pmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 \\
\end{pmatrix}$


# Matriz Nula

$N \in \mathbb{K}^{m \times n} \mid (N)_{ij} = 0$

Ejemplo:

$N \in \mathbb{R}^{3 \times 4} \mid N =
\begin{pmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
\end{pmatrix}$


# Matriz Escalar

$\lambda \cdot I_n \in \mathbb{K}^{n \times n}$, con $\lambda \in \mathbb{K}$.

Ejemplo:

$A =
\begin{pmatrix}
5 & 0 & 0 \\
0 & 5 & 0 \\
0 & 0 & 5 \\
\end{pmatrix}$


# Matriz Diagonal

$A \in \mathbb{K}^{n \times n}$ es diagonal $\Leftrightarrow (A)_{ij} = 0$ si $i \neq j$.

Ejemplo:

$A =
\begin{pmatrix}
1 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 3 \\
\end{pmatrix}$


# Matriz Cuadrada

Una matriz es cuadrada si tiene la misma cantidad de filas que de columnas.

$A =
\begin{pmatrix}
1 & 2 & 3 \\
0 & 2 & 0 \\
1 & 0 & 3 \\
\end{pmatrix}$


# Matriz Triangular Superior

$A \in \mathbb{K}^{n \times n}$ es triangular superior $\Leftrightarrow (A)_{ij} = 0$ si $i > j$.

$A =
\begin{pmatrix}
1 & 0 & 3 & 4\\
0 & 4 & 5 & 0\\
0 & 0 & 0 & 1\\
0 & 0 & 0 & 7\\
\end{pmatrix}$


# Matriz Triangular Inferior

$A \in \mathbb{K}^{n \times n}$ es triangular inferior $\Leftrightarrow (A)_{ij} = 0$ si $i < j$.

$A =
\begin{pmatrix}
1 & 0 & 0 & 0\\
2 & 4 & 0 & 0\\
5 & 0 & 0 & 0\\
1 & 2 & 3 & 7\\
\end{pmatrix}$


# Matriz Idempotente

$A \in \mathbb{K}^{n \times n}$ es idempotente $\Leftrightarrow A^2 = A$.


# Matriz Involutiva

$A \in \mathbb{K}^{n \times n}$ es involutiva $\Leftrightarrow A^2 = I_n$.


# Matriz Nilpotente

$A \in \mathbb{K}^{n \times n}$ es nilpotente $\Leftrightarrow \exists\ p \in \mathbb{N} \mid A^p = N$.

Ejemplo:

TODO


# Matriz Simétrica

$A \in \mathbb{K}^{n \times n}$ es simétrica $\Leftrightarrow A = A^T$.

Ejemplo:

$A =
\begin{pmatrix}
1 & 2 & 3 \\
2 & 2 & 0 \\
3 & 0 & 3 \\
\end{pmatrix}$


# Matriz Antisimétrica

$A \in \mathbb{K}^{n \times n}$ es antisimétrica $\Leftrightarrow A = -A^T$.

Ejemplo:

$A =
\begin{pmatrix}
0 & 2 & 3 \\
-2 & 0 & -1 \\
-3 & 1 & 0 \\
\end{pmatrix}$


# Matriz Real Ortogonal

$A \in \mathbb{R}^{n \times n}$ es ortogonal $\Leftrightarrow A^{-1} = A^T$.

Ejemplo:

TODO


# Matriz Real Normal

$A \in \mathbb{R}^{n \times n}$ es normal $\Leftrightarrow A \cdot A^T = A^T \cdot A$.

Ejemplo:

TODO


# Matriz Conjugada

$A \in \mathbb{C}^{m \times n}$, su matriz conjugada se define como $\overline{A} \in \mathbb{C}^{m \times n} \mid (\overline{A})_{ij} = \overline{(A)_{ij}}$.

Ejemplo:

$A =
\begin{pmatrix}
0  & 2 + i & 3 - 2i \\
-2 & 4i    & -1 \\
-3 & 1     & 1 + i \\
\end{pmatrix}$

$\overline{A} =
\begin{pmatrix}
0  & 2 - i & 3 + 2i \\
-2 & -4i   & -1 \\
-3 & 1     & 1 - i \\
\end{pmatrix}$


# Matriz Traspuesta Conjugada

$A \in \mathbb{C}^{m \times n}$, su matriz traspuesta conjugada se define como $A^H \in \mathbb{C}^{n \times m} \mid (A^H)_{ij} = (\overline{A})_{ji}$.

Ejemplo:

$A =
\begin{pmatrix}
0  & 2 + i & 3 - 2i & i \\
-2 & 4i    & -1     & 3 \\
-3 & 1     & 1 + i  & 2 + i\\
\end{pmatrix}$

$A^H =
\begin{pmatrix}
0      & -2   & -3 \\
2 - i  & -4i  & 1 \\
3 + 2i & -1   & 1 - i \\
-i     & 3   & 2 - i \\
\end{pmatrix}$


# Matriz Hermitiana

$A \in \mathbb{C}^{n \times n}$ es hermitiana $\Leftrightarrow A = A^H$.


# Matriz Antihermitiana

$A \in \mathbb{C}^{n \times n}$ es antihermitiana $\Leftrightarrow A = -A^H$.


# Matriz Unitaria

$A \in \mathbb{C}^{n \times n}$ es unitaria $\Leftrightarrow A^{-1} = A^H$.

Ejemplo:

TODO


# Matriz Compleja Normal

$A \in \mathbb{C}^{n \times n}$ es normal $\Leftrightarrow A \cdot A^H = A^H \cdot A$.

Ejemplo:

TODO


# Teorema 1.1

Sean $A, B, C \in \mathbb{K}^{m \times n}$.

$(A + B) + C = A + (B + C)$

**Demostración**:

$$
\begin{aligned}
((A + B) + C)_{ij} &= (A + B)_{ij} + (C)_{ij} \\
&= ((A)_{ij} + (B)_{ij}) + (C)_{ij} \\
&= (A)_{ij} + ((B)_{ij} + (C)_{ij}) \\
&= (A)_{ij} + (B + C)_{ij} \\
&= (A + (B + C))_{ij} \\
\end{aligned}
$$

Por lo tanto $(A + B) + C = A + (B + C)$.


# Teorema 1.2

Sea $A \in \mathbb{K}^{m \times n}$.

$A + N = N + A = A$

**Demostración**:

$(A + N)_{ij} = (A)_{ij} + (N)_{ij} = (A)_{ij} + 0 = (A)_{ij}$

$(N + A)_{ij} = (N)_{ij} + (A)_{ij} = 0 + (A)_{ij} = (A)_{ij}$

Por lo tanto, $A + N = N + A = A$.


# Teorema 1.3

$\forall\ A \in \mathbb{K}^{m \times n}:\ \exists!\ B \in \mathbb{K}^{m \times n} \mid A + B = B + A = N$.

A la matriz $B$ se la denota por $-A$.

**Demostración**:

Sea $A \in \mathbb{K}^{m \times n}$, se define $B \in \mathbb{K}^{m \times n} \mid (B)_{ij} = -(A)_{ij}$.

$$
\begin{aligned}
(A + B)_{ij} &= (A)_{ij} + (B)_{ij} \\
             &= (A)_{ij} + (-(A)_{ij}) \\
             &= 0 \\
             &= (N)_{ij} \\
\end{aligned}
$$

Por lo tanto $A + B = N$.

$$
\begin{aligned}
(B + A)_{ij} &= (B)_{ij} + (A)_{ij} \\
             &= (-(A)_{ij}) + (A)_{ij} \\
             &= 0 \\
\end{aligned}
$$

Por lo tanto $B + A = N$.

Sean $B, B' \in \mathbb{K}^{m \times n}$ tal que $A + B = B + A = N \wedge A + B' = B' + A = N$.

Entonces
$$
\begin{aligned}
&A + B = N = A + B' \\
&\Rightarrow A + B = A + B' \\
&\Rightarrow B + (A + B) = B + (A + B') \\
&\Rightarrow (B + A) + B = (B + A) + B' \\
&\Rightarrow N + B       = N + B' \\
&\Rightarrow B           = B' \\
\end{aligned}
$$

Por lo tanto la matriz $B$ es única.


# Teorema 1.4

Sean $A, B \in \mathbb{K}^{m \times n}$.

$A + B = B + A$

**Demostración**:

$$
\begin{aligned}
(A + B)_{ij} &= (A)_{ij} + (B)_{ij} \\
             &= (B)_{ij} + (A)_{ij} \\
             &= (B + A)_{ij} \\
\end{aligned}
$$

Por lo tanto, $A + B = B + A$.


# Teorema 1.5

Sean $A \in \mathbb{K}^{m \times n}$ y $\lambda, \lambda' \in \mathbb{K}$.

$(\lambda \cdot \lambda') \cdot A = \lambda \cdot (\lambda' \cdot A)$

**Demostración**:

$$
\begin{aligned}
((\lambda \cdot \lambda') \cdot A)_{ij} &= (\lambda \cdot \lambda') \cdot (A)_{ij} \\
                        &= \lambda \cdot (\lambda' \cdot (A)_{ij}) \\
                        &= (\lambda \cdot (\lambda' \cdot A))_{ij} \\
\end{aligned}
$$

Por lo tanto, $(\lambda \cdot \lambda') \cdot A = \lambda \cdot (\lambda' \cdot A)$.


# Teorema 1.6

Sean $A \in \mathbb{K}^{m \times n}$ y $1 \in \mathbb{K}$ el neutro multiplicativo de $\mathbb{K}$.

$1 \cdot A = A$

**Demostración**:

$(1 \cdot A)_{ij} = (1 \cdot (A)_{ij}) = (A)_{ij}$

Por lo tanto, $1 \cdot A = A$.


# Teorema 1.7

Sean $A \in \mathbb{K}^{m \times n}$ y $0 \in \mathbb{K}$ el neutro aditivo de $\mathbb{K}$.

$0 \cdot A = N$

**Demostración**:

$(0 \cdot A)_{ij} = (0 \cdot (A)_{ij}) = 0 = (N)_{ij}$

Por lo tanto, $0 \cdot A = N$.


# Teorema 1.8

Sean $A \in \mathbb{K}^{m \times n}$ y $-1 \in \mathbb{K}$.

$(-1) \cdot A = -A$

**Demostración**:

$((-1) \cdot A)_{ij} = ((-1) \cdot (A)_{ij}) = -(A)_{ij}$.

Luego, $(A + ((-1) \cdot A))_{ij} = (A)_{ij} + (-(A)_{ij}) = 0 = (N)_{ij}$.

Por lo tanto, por _Teorema 1.3_, $(-1) \cdot A = -A$.


# Teorema 1.9

Sean $A, B \in \mathbb{K}^{m \times n}$ y $\lambda \in \mathbb{K}$.

$\lambda \cdot (A + B) = \lambda \cdot A + \lambda \cdot B$

**Demostración**:

$$
\begin{aligned}
(\lambda \cdot (A+B))_{ij} &= \lambda \cdot (A + B)_{ij} \\
                     &= \lambda \cdot ((A)_{ij} + (B)_{ij}) \\
                     &= \lambda \cdot (A)_{ij} + \lambda \cdot (B)_{ij} \\
                     &= (\lambda \cdot A)_{ij} + (\lambda \cdot B)_{ij} \\
                     &= (\lambda \cdot A + \lambda \cdot B)_{ij} \\
\end{aligned}
$$

Por lo tanto, $\lambda \cdot (A + B) = \lambda \cdot A + \lambda \cdot B$.


# Teorema 1.10

Sean $A \in \mathbb{K}^{m \times n}$ y $\lambda, \lambda' \in \mathbb{K}$.

$(\lambda + \lambda') \cdot A = \lambda \cdot A + \lambda' \cdot A$

**Demostración**:

$$
\begin{aligned}
((\lambda + \lambda') \cdot A)_{ij} &= (\lambda + \lambda') \cdot (A)_{ij} \\
                        &= \lambda \cdot (A)_{ij} + \lambda' \cdot (A)_{ij} \\
                        &= (\lambda \cdot A + \lambda' \cdot A)_{ij} \\
\end{aligned}
$$

Por lo tanto, $(\lambda + \lambda') \cdot A = \lambda \cdot A + \lambda' \cdot A$.


# Teorema 1.11

Sean $A \in \mathbb{K}^{m \times n}, B \in \mathbb{K}^{n \times p}, C \in \mathbb{K}^{p \times q}$.

$(A \cdot B) \cdot C = A \cdot (B \cdot C)$

**Demostración**:

$$
\begin{aligned}
((A \cdot B) \cdot C)_{ij} &= \sum\limits_{k = 1}^p (A \cdot B)_{ik} \cdot (C)_{kj} \\
                           &= \sum\limits_{k = 1}^p (\sum\limits_{l = 1}^{n} (A)_{il} \cdot (B)_{lk}) \cdot (C)_{kj} \\
                           &= \sum\limits_{k = 1}^p (\sum\limits_{l = 1}^{n} (A)_{il} \cdot (B)_{lk} \cdot (C)_{kj}) \\
                           &= \sum\limits_{l = 1}^{n}(\sum\limits_{k = 1}^p (A)_{il} \cdot (B)_{lk} \cdot (C)_{kj}) \\
                           &= \sum\limits_{l = 1}^{n} ((A)_{il} \cdot \sum\limits_{k = 1}^p (B)_{lk} \cdot (C)_{kj}) \\
                           &= \sum\limits_{l = 1}^{n} ((A)_{il} \cdot (B \cdot C)_{lj}) \\
                           &= (A \cdot (B \cdot C))_{ij}
\end{aligned}
$$

Por lo tanto, $(A \cdot B) \cdot C = A \cdot (B \cdot C)$.


# Teorema 1.12

Sea $A \in \mathbb{K}^{m \times n}$.

$I_m \cdot A = A \cdot I_n = A$

**Demostración**:

$$
\begin{aligned}
(I_m \cdot A)_{ij} &= \sum\limits_{k = 1}^{m} (I_m)_{ik} \cdot (A)_{kj} \\
                   &= (I_m)_{ii} \cdot (A)_{ij} \\
                   &= 1 \cdot (A)_{ij} \\
                   &= (A)_{ij} \\
\end{aligned}
$$

Donde la segunda igualdad se da porque $(I_m)_{ik}$ es $0$ cuando $i \neq k$.

De igual forma,

$$
\begin{aligned}
(A \cdot I_n)_{ij} &= \sum\limits_{k = 1}^n (A)_{ik} \cdot (I_n)_{kj} \\
                   &= (A)_{ij} \cdot (I_n)_{jj} \\
                   &= (A)_{ij} \cdot 1 \\
                   &= (A)_{ij} \\
\end{aligned}
$$

Por lo tanto $I_m \cdot A = A \cdot I_n = A$.


# Teorema 1.13

- Sean $A \in \mathbb{K}^{m \times n}$ y $B, C \in \mathbb{K}^{n \times p}$

  $A \cdot (B + C) = A \cdot B + A \cdot C$


- Sean $A, B \in \mathbb{K}^{m \times n}$ y $C \in \mathbb{K}^{n \times p}$

  $(A + B) \cdot C = A \cdot C + B \cdot C$

**Demostración**:

$$
\begin{aligned}
(A \cdot (B + C))_{ij} &= \sum\limits_{k = 1}^{n} (A)_{ik} \cdot (B + C)_{kj} \\
                       &= \sum\limits_{k = 1}^{n} (A)_{ik} \cdot ((B)_{kj} + (C)_{kj}) \\
                       &= \sum\limits_{k = 1}^{n} ((A)_{ik} \cdot (B)_{kj} + (A)_{ik} \cdot (C)_{kj}) \\
                       &= \sum\limits_{k = 1}^{n} (A)_{ik} \cdot (B)_{kj} + \sum\limits_{k = 1}^{n} (A)_{ik} \cdot (C)_{kj} \\
                       &= (A \cdot B)_{ij} + (A \cdot C)_{ij} \\
                       &= (A \cdot B + A \cdot C)_{ij} \\
\end{aligned}
$$

Por lo tanto, $A \cdot (B + C) = A \cdot B + A \cdot C$.

$$
\begin{aligned}
((A + B) \cdot C)_{ij} &= \sum\limits_{k = 1}^{n} (A + B)_{ik} \cdot (C)_{kj} \\
                      &= \sum\limits_{k = 1}^{n} ((A)_{ik} + (B)_{ik}) \cdot (C)_{kj} \\
                      &= \sum\limits_{k = 1}^{n} ((A)_{ik} \cdot (C)_{kj} + (B)_{ik} \cdot (C)_{kj}) \\
                      &= \sum\limits_{k = 1}^{n} (A)_{ik} \cdot (C)_{kj} + \sum\limits_{k = 1}^{n} (B)_{ik} \cdot (C)_{kj} \\
                      &= (A \cdot C)_{ij} + (B \cdot C)_{ij} \\
                      &= (A \cdot C + B \cdot C)_{ij} \\
\end{aligned}
$$

Por lo tanto, $(A + B) \cdot C = A \cdot C + B \cdot C$.


# Teorema 1.14

Sean $A \in \mathbb{K}^{m \times n},\ B \in \mathbb{K}^{n \times p}$, y $\lambda \in \mathbb{K}$.

$(\lambda \cdot A) \cdot B = \lambda \cdot (A \cdot B) = A \cdot (\lambda \cdot B)$

**Demostración**:

$$
\begin{aligned}
((\lambda \cdot A) \cdot B)_{ij} &= \sum\limits_{k = 1}^{n} (\lambda \cdot A)_{ik} \cdot (B)_{kj} \\
                           &= \sum\limits_{k = 1}^{n} (\lambda \cdot (A)_{ik}) \cdot (B)_{kj} \\
                           &= \sum\limits_{k = 1}^{n} \lambda \cdot ((A)_{ik} \cdot (B)_{kj}) \\
                           &= \lambda \cdot \sum\limits_{k = 1}^{n} (A)_{ik} \cdot (B)_{kj} \\
                           &= \lambda \cdot (A \cdot B)_{ij} \\
                           &= (\lambda \cdot (A \cdot B))_{ij} \\
\end{aligned}
$$

Por lo tanto, $(\lambda \cdot A) \cdot B = \lambda \cdot (A \cdot B)$.

$$
\begin{aligned}
((\lambda \cdot A) \cdot B)_{ij} &= \sum\limits_{k = 1}^{n} (\lambda \cdot A)_{ik} \cdot (B)_{kj} \\
                           &= \sum\limits_{k = 1}^{n} (\lambda \cdot (A)_{ik}) \cdot (B)_{kj} \\
                           &= \sum\limits_{k = 1}^{n} ((A)_{ik} \cdot \lambda) \cdot (B)_{kj} \\
                           &= \sum\limits_{k = 1}^{n} (A)_{ik} \cdot (\lambda \cdot (B)_{kj}) \\
                           &= \sum\limits_{k = 1}^{n} (A)_{ik} \cdot (\lambda \cdot B)_{kj} \\
                           &= (A \cdot (\lambda \cdot B))_{ij}
\end{aligned}
$$

Por lo tanto, $(\lambda \cdot A) \cdot B = A \cdot (\lambda \cdot B)$.

Luego, $(\lambda \cdot A) \cdot B = \lambda \cdot (A \cdot B) = A \cdot (\lambda \cdot B)$.


# Teorema 1.15

Sean $A, B \in \mathbb{K}^{m \times n}$.

$(A + B)^T = A^T + B^T$

**Demostración**:

Sean $i \in \mathbb{N}_n,\ j \in \mathbb{N}_m$.

$((A + B)^T)_{ij} = (A + B)_{ji} = (A)_{ji} + (B)_{ji} = (A^T)_{ij} + (B^T)_{ij} = (A^T + B^T)_{ij}$

Por lo tanto, $(A + B)^T = A^T + B^T$.


# Teorema 1.16

Sean $A \in \mathbb{K}^{m \times n}$ y $\lambda \in \mathbb{K}$.

$(\lambda \cdot A)^T = \lambda \cdot (A^T)$

**Demostración**:

Sean $i \in \mathbb{N}_n,\ j \in \mathbb{N}_m$.

$((\lambda \cdot A)^T)_{ij} = (\lambda \cdot A)_{ji} = \lambda \cdot (A)_{ji} = \lambda \cdot (A^T)_{ij} = (\lambda \cdot (A^T))_{ij}$

Por lo tanto, $(\lambda \cdot A)^T = \lambda \cdot (A^T)$.


# Teorema 1.17

Sean $A \in \mathbb{K}^{m \times n},\ B \in \mathbb{K}^{n \times p}$.

$(A \cdot B)^T = B^T \cdot A^T$

**Demostración**:

Sean $i \in \mathbb{N}_p,\ j \in \mathbb{N}_m$.

$$
\begin{aligned}
((A \cdot B)^T)_{ij} &= (A \cdot B)_{ji} \\
                     &= \sum\limits_{k = 1}^{n} (A)_{jk} \cdot (B)_{ki} \\
                     &= \sum\limits_{k = 1}^{n} (A^T)_{kj} \cdot (B^T)_{ik} \\
                     &= \sum\limits_{k = 1}^{n} (B^T)_{ik} \cdot (A^T)_{kj} \\
                     &= (B^T \cdot A^T)_{ij}
\end{aligned}
$$

Por lo tanto, $(A \cdot B)^T = B^T \cdot A^T$.


# Teorema 1.18

Sea $A \in \mathbb{K}^{m \times n}$.

$(A^T)^T = A$

**Demostración**:

Sean $i \in \mathbb{N}_m,\ j \in \mathbb{N}_n$.

$((A^T)^T)_{ij} = (A^T)_{ji} = (A)_{ij}$

Por lo tanto, $(A^T)^T = A$.


# Teorema 1.19

Sean $A, B \in \mathbb{K}^{n \times n}$.

$\operatorname{tr}(A + B) = \operatorname{tr}(A) + \operatorname{tr}(B)$

**Demostración**:

$\operatorname{tr}(A + B) = \sum\limits_{i = 1}^{n} (A + B)_{ii} = \sum\limits_{i = 1}^{n} ((A)_{ii} + (B)_{ii}) = \sum\limits_{i = 1}^{n} (A)_{ii} + \sum\limits_{i = 1}^{n} (B)_{ii} = \operatorname{tr}(A) + \operatorname{tr}(B)$


# Teorema 1.20

Sean $A \in \mathbb{K}^{n \times n}$, y $\lambda \in \mathbb{K}$.

$\operatorname{tr}(\lambda \cdot A) = \lambda \cdot \operatorname{tr}(A)$

**Demostración**:

$\operatorname{tr}(\lambda \cdot A)
= \sum\limits_{i = 1}^{n} (\lambda \cdot A)_{ii}
= \sum\limits_{i = 1}^{n} \lambda \cdot (A)_{ii}
= \lambda \cdot \sum\limits_{i = 1}^{n} (A)_{ii}
= \lambda \cdot \operatorname{tr}(A)$


# Teorema 1.21

Sean $A, B \in \mathbb{K}^{n \times n}$.

$\operatorname{tr}(A \cdot B) = \operatorname{tr}(B \cdot A)$

**Demostración**:

$$
\begin{aligned}
\operatorname{tr}(A \cdot B) &= \sum\limits_{i = 1}^{n} (A \cdot B)_{ii} \\
                             &= \sum\limits_{i = 1}^{n} (\sum\limits_{k = 1}^{n} (A)_{ik} \cdot (B)_{ki}) \\
                             &= \sum\limits_{k = 1}^{n} (\sum\limits_{i = 1}^{n} (A)_{ik} \cdot (B)_{ki}) \\
                             &= \sum\limits_{k = 1}^{n} (\sum\limits_{i = 1}^{n} (B)_{ki} \cdot (A)_{ik}) \\
                             &= \sum\limits_{k = 1}^{n} (B \cdot A)_{kk} \\
                             &= \operatorname{tr}(B \cdot A) \\
\end{aligned}
$$


# Teorema 1.22

Sea $A \in \mathbb{K}^{n \times n}$.

$\operatorname{tr}(A^T) = \operatorname{tr}(A)$

**Demostración**:

$\operatorname{tr}(A^T)
= \sum\limits_{i = 1}^{n} (A^T)_{ii}
= \sum\limits_{i = 1}^{n} (A)_{ii}
= \operatorname{tr}(A)$


# Grupo lineal general

# Matriz Inversa

# Calculo Matriz Inversa

# Potencias de matrices

# Polinomio de matrices

# Teoremas de triangulares
- A+B, cA, AB triangulares si A, B son triangulares del mismo tipo
- Polinomios de triangulares, triangulares
- Inversible si y solo si no hay 0 en la diagonal

# Matrices en bloques

# Matrices cuadradas en bloques

# Matrices diagonales en bloques

# Contraejemplos matrices
Conmutatividad en multiplicacion
Divisores de 0
