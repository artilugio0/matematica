# Teorema 3.2


Sean $A, B \in \mathbb{K}^{m \times n}$.

$A$ es equivalente por filas a $B$ si y solo si existe $P \in \mathbb{K}^{m \times m}$ tal que $A = P \cdot B$, y $P$ es un producto de matrices elementales.

**Demostración**:

($\Rightarrow$)

Si $A$ es equivalente por filas a $B$, entonces existen las operaciones elementales de fila $ero_1,\ \dots\ , ero_k$ tales que $A = ero_k(\ \dots\ (ero_1(B)))$.
Por _Teorema 3.1_, existen las matrices elementales $E_1,\ \dots\ , E_k \in \mathbb{K}^{m \times m}$ tales que $A = E_k \cdot (\ \dots\ \cdot (E_1 \cdot B))$. Dado que el producto de matrices es asociativo, la igualdad anterior puede expresarse como $A = (E_k \cdot\ \dots\ \cdot E_1) \cdot B$. Sea $P = E_k \cdot\ \dots\ \cdot E_1$, entonces $A = P \cdot B$, siendo $P$ un producto de matrices elementales.

($\Leftarrow$)

Si $P$ es un producto de matrices elementales tal que $A = P \cdot B$, entonces $A = E_k \cdot \ \dots\ \cdot E_1 \cdot B$, siendo las $E_i$ matrices elementales. Luego, por _Teorema 3.1_, $A = ero_k(\ \dots\ (ero_1(B)))$, siendo $ero_i$ la operación elemental de fila correspondiente a la matriz elemental $E_i$. Por lo tanto, $A$ es equivalente por filas a $B$.

## Tags

- algebra_lineal
- matriz_inversa
