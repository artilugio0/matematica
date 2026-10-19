# Teorema 3.13


Sea $A \in \mathbb{K}^{n \times n}$.

Si una secuencia de operaciones elementales transforma a $A$ en $I_n$, esa misma secuencia transforma a $I_n$ en $A^{-1}$.

**Demostración**:

Sea $ero_1,\ \dots\ , ero_k$ una secuencia de operaciones elementales de fila que transforman a $A$ en $I_n$. Por definición, $I_n$ es equivalente por filas a $A$ y por _Teorema 2.4_ $A$ es equivalente por filas a $I_n$. Entonces, por _Teorema 3.9_, $A$ es inversible y existe $A^{-1}$. También, por _Teorema 3.1_, $E_k \cdot\ \dots\ \cdot E_1 \cdot A = I_n$ siendo $E_i$ las matrices elementales correspondientes a las operaciones elementales de fila $ero_i$. Multiplicando a derecha en ambos lados de la igualdad por $A^{-1}$ se obtiene $E_k \cdot\ \dots\ \cdot E_1 \cdot A \cdot A^{-1} = I_n \cdot A^{-1}$ y por lo tanto, $E_k \cdot\ \dots\ \cdot E_1 \cdot I_n = A^{-1}$. Luego, por _Teorema 3.1_, las mismas operaciones elementales de fila transforman a $I_n$ en $A^{-1}$.

## Tags

- algebra_lineal
- matriz_inversa
