# Teorema 3.8


Las matrices elementales son inversibles.

**Demostración**:

Utilizando las operaciones inversas definidas en _Teorema 2.3_:

Sean $E_1, E_1' \in \mathbb{K}^{n \times n}$ tales que $E_1 = ero1_{i,j}(I_n)$ y $E_1' = ero1_{j,i}(I_n)$. Por _Teorema 3.1_, $E_1 \cdot E_1' = ero1_{i,j}(ero1_{j,i}(I_n)) = I_n$, y $E_1' \cdot E_1 = ero1_{j,i}(ero1_{i,j}(I_n)) = I_n$. Por lo tanto, $E_1$ es inversible.

Sean $E_2, E_2' \in \mathbb{K}^{n \times n}$ tales que $E_2 = ero2_{i,k}(I_n)$ y $E_2' = ero2_{i,k^{-1}}(I_n)$, con $k \neq 0$. Por _Teorema 3.1_, $E_2 \cdot E_2' = ero2_{i,k}(ero2_{i,k^{-1}}(I_n)) = I_n$, y $E_2' \cdot E_2 = ero2_{i,k^{-1}}(ero2_{i,k}(I_n)) = I_n$. Por lo tanto, $E_2$ es inversible.

Sean $E_3, E_3' \in \mathbb{K}^{n \times n}$ tales que $E_3 = ero3_{i,j,k}(I_n)$ y $E_3' = ero3_{i,j,-k}(I_n)$, con $i \neq j$. Por _Teorema 3.1_, $E_3 \cdot E_3' = ero3_{i,j,k}(ero3_{i,j,-k}(I_n)) = I_n$, y $E_3' \cdot E_3 = ero3_{i,j,-k}(ero3_{i,j,k}(I_n)) = I_n$. Por lo tanto, $E_3$ es inversible.

Por lo tanto todas las matrices elementales son inversibles.

## Tags

- algebra_lineal
- matriz_inversa
