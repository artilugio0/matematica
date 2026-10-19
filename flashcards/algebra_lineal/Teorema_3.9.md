# Teorema 3.9


Sea $A \in \mathbb{K}^{n \times n}$.

$A$ es inversible si y solo si es equivalente por filas a $I_n$.

**Demostración**:

($\Rightarrow$)

Sea el sistema $A \cdot X = O$. Como $A$ es inversible, existe $A^{-1}$. Multiplicando a izquierda ambos lados de la igualdad anterior se tiene que $A^{-1} \cdot A \cdot X = A^{-1} \cdot O$. Entonces, $X = O$, y el sistema homogéneo solo tiene la solución trivial. Por _Teorema 2.12_, $A$ es equivalente por filas a $I_n$.

($\Leftarrow$)

Si $A$ es equivalente por filas a $I_n$, por _Teorema 3.2_, $A = E_k \cdot\ \dots\ \cdot E_1 \cdot I_n = E_k \cdot\ \dots\ \cdot E_1$, donde las $E_i$ son matrices elementales. Por _Teorema 3.8_, las matrices $E_i$ son inversibles, y por _Teorema 3.6_, el producto de matrices $E_k \cdot\ \dots\ \cdot E_1$ es una matriz inversible. Por lo tanto $A$ es una matriz inversible.

## Tags

- algebra_lineal
- matriz_inversa
