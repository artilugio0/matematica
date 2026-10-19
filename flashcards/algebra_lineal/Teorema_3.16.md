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

## Tags

- algebra_lineal
- matriz_inversa
