# Teorema 3.6


Sean $A, B \in \mathbb{K}^{n \times n}$ matrices inversibles. Entonces $(A \cdot B)^{-1} = B^{-1} \cdot A^{-1}$.

En general, sean $A_1,\ \dots\ , A_k \in \mathbb{K}^{n \times n}$ matrices inversibles. Entonces $(A_1 \cdot\ \dots\ \cdot A_k)^{-1} = {A_k}^{-1} \cdot\ \dots\ \cdot {A_1}^{-1}$.

**Demostración**:

Si $A, B$ son matrices inversibles, entonces existen $A^{-1}$ y $B^{-1}$. Luego,

$(A \cdot B) \cdot (B^{-1} \cdot A^{-1}) = A \cdot (B \cdot B^{-1}) \cdot A^{-1} = A \cdot I_n \cdot A^{-1} = A \cdot A^{-1} = I_n$.

$(B^{-1} \cdot A^{-1}) \cdot (A \cdot B) = B^{-1} \cdot (A^{-1} \cdot A) \cdot B = B^{-1} \cdot I_n \cdot B = B^{-1} \cdot B = I_n$.

Por lo tanto, $(A \cdot B)^{-1} = B^{-1} \cdot A^{-1}$.

El caso para $k \in \mathbb{N}$ matrices se demuestra por inducción.

Para el caso $k = 1$ no hay nada que demostrar, y el caso $k = 2$ ya fue demostrado.

Se asume que se cumple para un $k \in \mathbb{N}$ con $k \geq 2$. Sean $A_1,\ \dots\ , A_k, A_{k+1} \in \mathbb{K}^{n \times n}$ matrices inversibles.

$$
\begin{aligned}
(A_1 \cdot\ \dots\ \cdot A_k \cdot A_{k+1})^{-1} &= ((A_1 \cdot\ \dots\ \cdot A_k) \cdot A_{k+1})^{-1} &\text{(siendo } A_1 \cdot\ \dots\ \cdot A_k \text{ inversible por hipótesis inductiva)} \\
&= {A_{k+1}}^{-1} \cdot (A_1 \cdot\ \dots\ \cdot A_k)^{-1} &\text{(por el caso } k = 2 \text{)} \\
&= {A_{k+1}}^{-1} \cdot ({A_k}^{-1} \cdot\ \dots\ \cdot {A_1}^{-1}) &\text{(por hipótesis inductiva)} \\
&= {A_{k+1}}^{-1} \cdot {A_k}^{-1} \cdot\ \dots\ \cdot {A_1}^{-1}
\end{aligned}
$$

Por lo tanto $(A_1 \cdot\ \dots\ \cdot A_k)^{-1} = A_k^{-1} \cdot\ \dots\ \cdot {A_1}^{-1}$ para todo $k \in \mathbb{N}$.

## Tags

- algebra_lineal
- matriz_inversa
