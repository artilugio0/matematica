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
