# Matriz

Sean $m, n \in \mathbb{N}$ y $\mathbb{K}$ un cuerpo.

Una **matriz de $m \times n$ sobre el cuerpo $\mathbb{K}$** es una función $A: \mathbb{N}_m \times \mathbb{N}_n \to \mathbb{K}$.

Nota: $\mathbb{N}_h = \{1, 2,\ \dots\ , h - 1, h\}$

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


# Traspuesta

Sea $A \in \mathbb{K}^{m \times n}$.

Se define $A^T \in \mathbb{K}^{n \times m}$ tal que:

$(A^T)_{ij} = (A)_{ji}$


# Traza

Sea $A \in \mathbb{K}^{n \times n}$.

$\text{tr}(A) = \sum\limits_{i = 1}^n (A)_{ii}$


# Matriz Identidad

$$
I_n \in \mathbb{K}^{n \times n} \mid (I_n)_{ij} =
\begin{cases}
1 & \text{si } i = j \\
0 & \text{si } i \neq j \\
\end{cases}
$$

Ejemplo:

$$
I_3 =
\begin{pmatrix}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1 \\
\end{pmatrix}
$$


# Matrices Canónicas

$$
E^{kl} \in \mathbb{K}^{m \times n} \mid (E^{kl})_{ij} =
\begin{cases}
1 & \text{si } i = k \wedge j = l \\
0 & \text{si } i \neq k \lor j \neq l \\
\end{cases}
$$

Ejemplo:

$$
E^{24} =
\begin{pmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 \\
\end{pmatrix}
$$


# Matriz Nula

$N \in \mathbb{K}^{m \times n} \mid (N)_{ij} = 0$

Ejemplo:

$$
N \in \mathbb{R}^{3 \times 4} \mid N =
\begin{pmatrix}
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 \\
\end{pmatrix}
$$


# Matriz Escalar

$\lambda \cdot I_n \in \mathbb{K}^{n \times n}$, con $\lambda \in \mathbb{K}$.

Ejemplo:

$$
A =
\begin{pmatrix}
5 & 0 & 0 \\
0 & 5 & 0 \\
0 & 0 & 5 \\
\end{pmatrix}
$$


# Matriz Diagonal

$A \in \mathbb{K}^{n \times n}$ es diagonal $\Leftrightarrow (A)_{ij} = 0$ si $i \neq j$.

Ejemplo:

$$
A =
\begin{pmatrix}
1 & 0 & 0 \\
0 & 2 & 0 \\
0 & 0 & 3 \\
\end{pmatrix}
$$


# Matriz Cuadrada

Una matriz es cuadrada si tiene la misma cantidad de filas que de columnas.

$$
A =
\begin{pmatrix}
1 & 2 & 3 \\
0 & 2 & 0 \\
1 & 0 & 3 \\
\end{pmatrix}
$$


# Matriz Triangular Superior

$A \in \mathbb{K}^{n \times n}$ es triangular superior $\Leftrightarrow (A)_{ij} = 0$ si $i > j$.

$$
A =
\begin{pmatrix}
1 & 0 & 3 & 4\\
0 & 4 & 5 & 0\\
0 & 0 & 0 & 1\\
0 & 0 & 0 & 7\\
\end{pmatrix}
$$


# Matriz Triangular Inferior

$A \in \mathbb{K}^{n \times n}$ es triangular inferior $\Leftrightarrow (A)_{ij} = 0$ si $i < j$.

$$
A =
\begin{pmatrix}
1 & 0 & 0 & 0\\
2 & 4 & 0 & 0\\
5 & 0 & 0 & 0\\
1 & 2 & 3 & 7\\
\end{pmatrix}
$$


# Potencias de matrices

Sean $A \in \mathbb{K}^{n \times n}$ y $p \in \mathbb{N}$.

Se definen:

$A^0 = I_n$

$A^p = A^{p - 1} \cdot A$


# Polinomio de matrices

Sean los escalares $a_0, a_1,\ \dots\ , a_k \in \mathbb{K}$ y $A \in \mathbb{K}^{n \times n}$.

Dado el polinomio $P(x) = a_0 + a_1 \cdot x + a_2 \cdot x^2 +\ \dots\ + a_k \cdot x^k$, se define:

$P(A) = a_0 \cdot I_n + a_1 \cdot A + a_2 \cdot A^2 +\ \dots\ + a_k \cdot A^k$


# Matriz Idempotente

$A \in \mathbb{K}^{n \times n}$ es idempotente $\Leftrightarrow A^2 = A$.

Ejemplos:

$$
\begin{pmatrix}
1 & 0 \\
2 & 0 \\
\end{pmatrix}^2 =
\begin{pmatrix}
1 & 0 \\
2 & 0 \\
\end{pmatrix}
$$

$$
\begin{pmatrix}
\frac{1}{2} & \frac{1}{2} \\
\frac{1}{2} & \frac{1}{2} \\
\end{pmatrix}^2 =
\begin{pmatrix}
\frac{1}{2} & \frac{1}{2} \\
\frac{1}{2} & \frac{1}{2} \\
\end{pmatrix}
$$


# Matriz Involutiva

$A \in \mathbb{K}^{n \times n}$ es involutiva $\Leftrightarrow A^2 = I_n$.

Ejemplo:

$$
\begin{pmatrix}
2  & 3 \\
-1 & -2 \\
\end{pmatrix}^2 =
\begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
$$


# Matriz Nilpotente

$A \in \mathbb{K}^{n \times n}$ es nilpotente $\Leftrightarrow \exists\ p \in \mathbb{N} \mid A^p = N$.

Ejemplo:

$$
\begin{pmatrix}
2  & 4 \\
-1 & -2 \\
\end{pmatrix}^2 =
\begin{pmatrix}
0 & 0 \\
0 & 0 \\
\end{pmatrix}
$$


# Matriz Simétrica

$A \in \mathbb{K}^{n \times n}$ es simétrica $\Leftrightarrow A = A^T$.

Ejemplo:

$$
A =
\begin{pmatrix}
1 & 2 & 3 \\
2 & 2 & 0 \\
3 & 0 & 3 \\
\end{pmatrix}
$$


# Matriz Antisimétrica

$A \in \mathbb{K}^{n \times n}$ es antisimétrica $\Leftrightarrow A = -A^T$.

Ejemplo:

$$
A =
\begin{pmatrix}
0 & 2 & 3 \\
-2 & 0 & -1 \\
-3 & 1 & 0 \\
\end{pmatrix}
$$


# Matriz Real Normal

$A \in \mathbb{R}^{n \times n}$ es normal $\Leftrightarrow A \cdot A^T = A^T \cdot A$.

Ejemplo:

$$
\begin{pmatrix}
0  & 2 \\
-2 & 0 \\
\end{pmatrix} \cdot
\begin{pmatrix}
0 & -2 \\
2 & 0 \\
\end{pmatrix} =
\begin{pmatrix}
0 & -2 \\
2 & 0 \\
\end{pmatrix} \cdot
\begin{pmatrix}
0  & 2 \\
-2 & 0 \\
\end{pmatrix} =
\begin{pmatrix}
4 & 0 \\
0 & 4 \\
\end{pmatrix}
$$


# Matriz Conjugada

$A \in \mathbb{C}^{m \times n}$, su matriz conjugada se define como $\overline{A} \in \mathbb{C}^{m \times n} \mid (\overline{A})_{ij} = \overline{(A)_{ij}}$.

Ejemplo:

$$
A =
\begin{pmatrix}
0  & 2 + i & 3 - 2i \\
-2 & 4i    & -1 \\
-3 & 1     & 1 + i \\
\end{pmatrix}
$$

$$
\overline{A} =
\begin{pmatrix}
0  & 2 - i & 3 + 2i \\
-2 & -4i   & -1 \\
-3 & 1     & 1 - i \\
\end{pmatrix}
$$


# Matriz Traspuesta Conjugada

$A \in \mathbb{C}^{m \times n}$, su matriz traspuesta conjugada se define como $A^H \in \mathbb{C}^{n \times m} \mid (A^H)_{ij} = (\overline{A})_{ji}$.

Ejemplo:

$$
A =
\begin{pmatrix}
0  & 2 + i & 3 - 2i & i \\
-2 & 4i    & -1     & 3 \\
-3 & 1     & 1 + i  & 2 + i\\
\end{pmatrix}
$$

$$
A^H =
\begin{pmatrix}
0      & -2   & -3 \\
2 - i  & -4i  & 1 \\
3 + 2i & -1   & 1 - i \\
-i     & 3   & 2 - i \\
\end{pmatrix}
$$


# Matriz Hermitiana

$A \in \mathbb{C}^{n \times n}$ es hermitiana $\Leftrightarrow A = A^H$.

Ejemplo:

$$
\begin{pmatrix}
1     & 1 + i \\
1 - i & 2 \\
\end{pmatrix} = \\
\begin{pmatrix}
1     & 1 + i \\
1 - i & 2 \\
\end{pmatrix}^H
$$


# Matriz Antihermitiana

$A \in \mathbb{C}^{n \times n}$ es antihermitiana $\Leftrightarrow A = -A^H$.

Ejemplo:

$$
\begin{pmatrix}
0      & 1 + i \\
-1 + i & 0 \\
\end{pmatrix} = - \\
\begin{pmatrix}
0      & 1 + i \\
-1 + i & 0 \\
\end{pmatrix}^H
$$


# Matriz Compleja Normal

$A \in \mathbb{C}^{n \times n}$ es normal $\Leftrightarrow A \cdot A^H = A^H \cdot A$.

Ejemplo:

$$
\begin{pmatrix}
1 & 1 \\
i & -i \\
\end{pmatrix} \cdot
\begin{pmatrix}
1 & -i \\
1 & i \\
\end{pmatrix} =
\begin{pmatrix}
1 & -i \\
1 & i \\
\end{pmatrix} \cdot
\begin{pmatrix}
1 & 1 \\
i & -i \\
\end{pmatrix} =
\begin{pmatrix}
2 & 0 \\
0 & 2 \\
\end{pmatrix}
$$


# Matriz Inversa

Sea $A \in \mathbb{K}^{n \times n}$.

Una matriz $A^{-1} \in \mathbb{K}^{n \times n}$ es inversa de $A$ si cumple que $A \cdot A^{-1} = A^{-1} \cdot A = I_n$.

Si existe una matriz inversa de $A$, entonces se dice que $A$ es invertible.


# Grupo lineal general

$GL(n, \mathbb{K}) = \{A \in \mathbb{K}^{n \times n} \mid A \text{ es invertible}\}$


# Matriz Real Ortogonal

$A \in \mathbb{R}^{n \times n}$ es ortogonal $\Leftrightarrow A^{-1} = A^T$.

Ejemplo:

$$
\begin{pmatrix}
0  & 1 \\
-1 & 0 \\
\end{pmatrix} \cdot
\begin{pmatrix}
0 & -1 \\
1 & 0 \\
\end{pmatrix} =
\begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
$$


# Matriz Unitaria

$A \in \mathbb{C}^{n \times n}$ es unitaria $\Leftrightarrow A^{-1} = A^H$.

Ejemplo:

$$
\begin{pmatrix}
\frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} \\
\frac{\sqrt{2}}{2}i & -\frac{\sqrt{2}}{2}i \\
\end{pmatrix} \cdot
\begin{pmatrix}
\frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2}i \\
\frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2}i \\
\end{pmatrix} =
\begin{pmatrix}
\frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{2}i \\
\frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2}i \\
\end{pmatrix} \cdot
\begin{pmatrix}
\frac{\sqrt{2}}{2}  & \frac{\sqrt{2}}{2} \\
\frac{\sqrt{2}}{2}i & -\frac{\sqrt{2}}{2}i \\
\end{pmatrix} =
\begin{pmatrix}
1 & 0 \\
0 & 1 \\
\end{pmatrix}
$$


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

Por lo tanto, $(A + B) + C = A + (B + C)$.


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

Sea $A \in \mathbb{K}^{m \times n}$. Se define $B \in \mathbb{K}^{m \times n} \mid (B)_{ij} = -(A)_{ij}$.

$$
\begin{aligned}
(A + B)_{ij} &= (A)_{ij} + (B)_{ij} \\
             &= (A)_{ij} + (-(A)_{ij}) \\
             &= 0 \\
             &= (N)_{ij} \\
\end{aligned}
$$

Por lo tanto, $A + B = N$.

$$
\begin{aligned}
(B + A)_{ij} &= (B)_{ij} + (A)_{ij} \\
             &= (-(A)_{ij}) + (A)_{ij} \\
             &= 0 \\
\end{aligned}
$$

Por lo tanto, $B + A = N$.

Sean $B, B' \in \mathbb{K}^{m \times n}$ tales que $A + B = B + A = N \wedge A + B' = B' + A = N$.

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

Por lo tanto, la matriz $B$ es única.


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

Por lo tanto, por el _Teorema 1.3_, $(-1) \cdot A = -A$.


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

La segunda igualdad se da porque $(I_m)_{ik}$ es $0$ cuando $i \neq k$.

De igual forma,

$$
\begin{aligned}
(A \cdot I_n)_{ij} &= \sum\limits_{k = 1}^n (A)_{ik} \cdot (I_n)_{kj} \\
                   &= (A)_{ij} \cdot (I_n)_{jj} \\
                   &= (A)_{ij} \cdot 1 \\
                   &= (A)_{ij} \\
\end{aligned}
$$

Por lo tanto, $I_m \cdot A = A \cdot I_n = A$.


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

Sean $A \in \mathbb{K}^{m \times n},\ B \in \mathbb{K}^{n \times p}$ y $\lambda \in \mathbb{K}$.

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

$\text{tr}(A + B) = \text{tr}(A) + \text{tr}(B)$

**Demostración**:

$\text{tr}(A + B) = \sum\limits_{i = 1}^{n} (A + B)_{ii} = \sum\limits_{i = 1}^{n} ((A)_{ii} + (B)_{ii}) = \sum\limits_{i = 1}^{n} (A)_{ii} + \sum\limits_{i = 1}^{n} (B)_{ii} = \text{tr}(A) + \text{tr}(B)$


# Teorema 1.20

Sean $A \in \mathbb{K}^{n \times n}$ y $\lambda \in \mathbb{K}$.

$\text{tr}(\lambda \cdot A) = \lambda \cdot \text{tr}(A)$

**Demostración**:

$\text{tr}(\lambda \cdot A)
= \sum\limits_{i = 1}^{n} (\lambda \cdot A)_{ii}
= \sum\limits_{i = 1}^{n} \lambda \cdot (A)_{ii}
= \lambda \cdot \sum\limits_{i = 1}^{n} (A)_{ii}
= \lambda \cdot \text{tr}(A)$


# Teorema 1.21

Sean $A, B \in \mathbb{K}^{n \times n}$.

$\text{tr}(A \cdot B) = \text{tr}(B \cdot A)$

**Demostración**:

$$
\begin{aligned}
\text{tr}(A \cdot B) &= \sum\limits_{i = 1}^{n} (A \cdot B)_{ii} \\
                             &= \sum\limits_{i = 1}^{n} (\sum\limits_{k = 1}^{n} (A)_{ik} \cdot (B)_{ki}) \\
                             &= \sum\limits_{k = 1}^{n} (\sum\limits_{i = 1}^{n} (A)_{ik} \cdot (B)_{ki}) \\
                             &= \sum\limits_{k = 1}^{n} (\sum\limits_{i = 1}^{n} (B)_{ki} \cdot (A)_{ik}) \\
                             &= \sum\limits_{k = 1}^{n} (B \cdot A)_{kk} \\
                             &= \text{tr}(B \cdot A) \\
\end{aligned}
$$


# Teorema 1.22

Sea $A \in \mathbb{K}^{n \times n}$.

$\text{tr}(A^T) = \text{tr}(A)$

**Demostración**:

$\text{tr}(A^T)
= \sum\limits_{i = 1}^{n} (A^T)_{ii}
= \sum\limits_{i = 1}^{n} (A)_{ii}
= \text{tr}(A)$


# Teorema 1.23

Sean $A, B \in \mathbb{K}^{n \times n}$ matrices triangulares del mismo tipo, $\lambda \in \mathbb{K}$ y $p \in \mathbb{Z}$, $p \geq 0$.

$A + B$, $\lambda \cdot A$, $A \cdot B$, $A^p$ son matrices triangulares del mismo tipo que $A$ y $B$.

**Demostración**:

Sean $A, B$ matrices triangulares superiores.

**Suma**: $(A + B)_{ij} = (A)_{ij} + (B)_{ij}$. Si $i > j$, entonces $(A)_{ij} = 0$ y $(B)_{ij} = 0$, luego $(A + B)_{ij} = 0$. Por lo tanto, $A + B$ es triangular superior.

**Producto por escalar**: $(\lambda \cdot A)_{ij} = \lambda \cdot (A)_{ij}$. Si $i > j$, entonces $(A)_{ij} = 0$, luego $\lambda \cdot (A)_{ij} = 0$. Por lo tanto, $\lambda \cdot A$ es triangular superior.

**Multiplicación**:
Si $i > j$:

$$
\begin{aligned}
(A \cdot B)_{ij} &= \sum\limits_{k = 1}^{n} (A)_{ik} \cdot (B)_{kj} \\
             &= \sum\limits_{k = 1}^{i - 1} (A)_{ik} \cdot (B)_{kj} + \sum\limits_{k = i}^{n} (A)_{ik} \cdot (B)_{kj} \\
             &= 0 + 0 \\
             &= 0 \\
\end{aligned}
$$

La tercera línea se da porque en la primera sumatoria se cumple que $i > i - 1 \geq k$, por lo tanto $(A)_{ik} = 0$, y en la segunda sumatoria $k \geq i > j$, por lo tanto $(B)_{kj} = 0$.

Por lo tanto, $A \cdot B$ es triangular superior.

**Potencia**:

Se demuestra por inducción sobre el exponente. $A^0 = I_n$ por definición, que es una matriz diagonal y por lo tanto triangular superior. Si se cumple que $A^k$ es triangular superior (con $k \in \mathbb{Z}$, $k \geq 0$), $A^{k+1} = A^k \cdot A$ es un producto de dos matrices triangulares superiores y por lo demostrado anteriormente $A^{k+1}$ es triangular superior. Por lo tanto, $A^{p}$ es triangular superior para todo $p \geq 0$.

Para el caso en el que las matrices $A, B$ son triangulares inferiores, las demostraciones son análogas.


# Teorema 1.24

Sean $A \in \mathbb{K}^{n \times n}$ una matriz triangular y $P(x)$ un polinomio con coeficientes en $\mathbb{K}$.

$P(A)$ es triangular del mismo tipo que $A$.

**Demostración**:

$P(A) = a_0 \cdot I_n + a_1 \cdot A + a_2 \cdot A^2 +\ \dots\ + a_k \cdot A^k$, y por el _Teorema 1.23_, el primer término es triangular superior e inferior dado que es una matriz diagonal. También el resto de los términos en la suma son triangulares del mismo tipo que $A$. Por el mismo teorema, la suma de todos los términos también es triangular del mismo tipo. Por lo tanto, $P(A)$ es triangular del mismo tipo que $A$.


# Matriz por bloques

Sea $A \in \mathbb{K}^{m \times n}$.

Sean $p, q \in \mathbb{N}$ y $m_1,\ \dots\ , m_p \in \mathbb{N}$, $n_1,\ \dots\ , n_q \in \mathbb{N}$ tales que $\sum\limits_{r = 1}^{p} m_r = m$ y $\sum\limits_{r = 1}^{q} n_r = n$.

Se definen $M_k = \sum\limits_{r = 1}^{k} m_r$ y $N_l = \sum\limits_{r = 1}^{l} n_r$ (nótese que $M_0 = N_0 = 0$).

Se define el bloque $A_{kl} \in \mathbb{K}^{m_k \times n_l}$, con $1 \leq k \leq p$ y $1 \leq l \leq q$, como la submatriz de $A$ tal que $(A_{kl})_{ij} = (A)_{(M_{k-1} + i) (N_{l-1}+j)}$, para $1 \leq i \leq m_k$ y $1 \leq j \leq n_l$.

Una matriz por bloques de $A$ es una representación de $A$ de la forma:

$$
A = \begin{pmatrix}
A_{11} & A_{12} & \dots & A_{1q} \\
A_{21} & A_{22} & \dots & A_{2q} \\
\vdots & \vdots & \ddots & \vdots \\
A_{p1} & A_{p2} & \dots & A_{pq}
\end{pmatrix}
$$

En esta representación los bloques que comparten fila tienen la misma cantidad de filas y los que comparten columna tienen la misma cantidad de columnas.

Ejemplo:

Sea $A \in \mathbb{K}^{3 \times 4}$ tal que

$$
A = \left(
\begin{array}{cc|c|c}
1 &  2 &  3 & 4 \\
5 &  6 &  7 & 8 \\ \hline
9 & 10 & 11 & 12
\end{array}
\right)
$$

Con $p = 2, q = 3, m_1 = 2, m_2 = 1$, y $n_1 = 2, n_2 = 1, n_3 = 1$. Los bloques son:

$$
A_{11} = \begin{pmatrix}
1 &  2 \\
5 &  6 \\
\end{pmatrix}
\qquad
A_{12} = \begin{pmatrix}
3 \\
7 \\
\end{pmatrix}
\qquad
A_{13} = \begin{pmatrix}
4 \\
8 \\
\end{pmatrix}
$$

$$
A_{21} = \begin{pmatrix}
9 &  10 \\
\end{pmatrix}
\qquad
A_{22} = \begin{pmatrix}
11 \\
\end{pmatrix}
\qquad
A_{23} = \begin{pmatrix}
12 \\
\end{pmatrix}
$$


# Teorema 1.25

Sean $A \in \mathbb{K}^{m \times n}$ una matriz de $p \times q$ bloques, donde cada bloque es $A_{kl} \in \mathbb{K}^{m_k \times n_l}$, y $B \in \mathbb{K}^{n \times r}$ una matriz de $q \times s$ bloques donde cada bloque es $B_{lt} \in \mathbb{K}^{n_l \times r_t}$.

Si $C = A \cdot B$, entonces $C$ es una matriz de $p \times s$ bloques donde cada bloque $C_{kt} = \sum\limits_{l = 1}^{q} A_{kl} \cdot B_{lt} \in \mathbb{K}^{m_k \times r_t}$.

**Demostración**:

Sean $M_k = \sum\limits_{a = 1}^{k} m_a$, $N_l = \sum\limits_{a = 1}^{l} n_a$, $R_t = \sum\limits_{a = 1}^{t} r_a$. Por su definición $M_0 = N_0 = R_0 = 0$ y también $M_p = m$, $N_q = n$ y $R_s = r$.

Dados $i \in \mathbb{N}_m$ y $j \in \mathbb{N}_r$, ambos enteros pueden expresarse de manera única en términos de $M_{k-1}$ y $R_{t-1}$ como $i = M_{k-1} + i'$ y $j = R_{t-1} + j'$, para $1 \leq k \leq p,\ 1 \leq i' \leq m_k$ y $1 \leq t \leq s,\ 1 \leq j' \leq r_t$.

Luego desarrollando $(C)_{ij}$, se obtiene:

$$
\begin{aligned}
(C)_{ij} &= \sum\limits_{x = 1}^{n} (A)_{ix} \cdot (B)_{xj} \\
         &= \sum\limits_{x = N_0 + 1}^{N_1} (A)_{ix} \cdot (B)_{xj} + \sum\limits_{x = N_1 + 1}^{N_2} (A)_{ix} \cdot (B)_{xj} +\ \dots\ + \sum\limits_{x = N_{q - 1} + 1}^{N_q} (A)_{ix} \cdot (B)_{xj} \\
         &= \sum\limits_{x = N_0 + 1}^{N_1} (A)_{(M_{k-1} + i') x} \cdot (B)_{x (R_{t - 1} + j')} + \sum\limits_{x = N_1 + 1}^{N_2} (A)_{(M_{k-1} + i') x} \cdot (B)_{x (R_{t - 1} + j')} +\ \dots\ + \sum\limits_{x = N_{q - 1} + 1}^{N_q} (A)_{(M_{k-1} + i') x} \cdot (B)_{x (R_{t - 1} + j')} \\
         &= (A_{k1} \cdot B_{1t})_{i'j'} + (A_{k2} \cdot B_{2t})_{i'j'} +\ \dots\ + (A_{kq} \cdot B_{qt})_{i'j'} \\
         &= \sum\limits_{l = 1}^{q} (A_{kl} \cdot B_{lt})_{i'j'} \\
         &= \left(\sum\limits_{l = 1}^{q} A_{kl} \cdot B_{lt} \right)_{i'j'} \\
         &= (C_{kt})_{i'j'} \\
\end{aligned}
$$

Cada paso se justifica de la siguiente forma:

1. Definición de producto de matrices
2. División de la sumatoria por límites coincidentes
3. Reemplazo de $i$ y $j$ de acuerdo a su expresión en términos de $M_{k-1}$ y $R_{t-1}$
4. Definición de bloques de $A$ y $B$, y producto de submatrices $A_{kl}$ y $B_{lt}$, para cada $l$ tal que $1 \leq l \leq q$
5. Simplificación de la expresión usando sumatoria
6. Definición del término $i'j'$ de la suma de matrices
7. Definición de $C_{kt}$

Por lo tanto, por definición de matriz por bloques, $C$ es una matriz de $p \times s$ bloques donde cada bloque $C_{kt} = \sum\limits_{l = 1}^{q} A_{kl} \cdot B_{lt} \in \mathbb{K}^{m_k \times r_t}$.



# Matrices TODO

- Matrices cuadradas por bloques
- Matrices diagonales por bloques
- Contraejemplos matrices
  - Conmutatividad en la multiplicación
  - Divisores de 0
- Interpretaciones del producto de matrices
  - Por filas
  - Por columnas
