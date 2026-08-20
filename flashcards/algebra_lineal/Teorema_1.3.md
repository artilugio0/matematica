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
