# Contraejemplos


- $A \cdot B \neq B \cdot A$:
  $$
  \begin{pmatrix}
  1 & 2 \\
  3 & 4 \\
  \end{pmatrix} \cdot 
  \begin{pmatrix}
  4 & 3 \\
  2 & 1 \\
  \end{pmatrix} \neq
  \begin{pmatrix}
  4 & 3 \\
  2 & 1 \\
  \end{pmatrix} \cdot 
  \begin{pmatrix}
  1 & 2 \\
  3 & 4 \\
  \end{pmatrix}
  $$

- $A \cdot B = N \wedge A \neq N \wedge B \neq N$:
  $$
  \begin{pmatrix}
  1 & 2 \\
  3 & 6 \\
  \end{pmatrix} \cdot 
  \begin{pmatrix}
  -2 & -4 \\
  1  & 2 \\
  \end{pmatrix} =
  \begin{pmatrix}
  0 & 0 \\
  0 & 0 \\
  \end{pmatrix}
  $$

- $(A + B)^2 \neq A^2 + 2 \cdot A \cdot B + B^2$:
  $$
  \left(
  \begin{pmatrix}
  1 & 1 \\
  0 & 1 \\
  \end{pmatrix} +
  \begin{pmatrix}
  1 & 0 \\
  1 & 1 \\
  \end{pmatrix}
  \right)^2 =
  \begin{pmatrix}
  5 & 4 \\
  4 & 5 \\
  \end{pmatrix} \neq
  \begin{pmatrix}
  6 & 4 \\
  4 & 4 \\
  \end{pmatrix} =
  \begin{pmatrix}
  1 & 1 \\
  0 & 1 \\
  \end{pmatrix}^2 + 2 \cdot
  \begin{pmatrix}
  1 & 1 \\
  0 & 1 \\
  \end{pmatrix} \cdot
  \begin{pmatrix}
  1 & 0 \\
  1 & 1 \\
  \end{pmatrix} +
  \begin{pmatrix}
  1 & 0 \\
  1 & 1 \\
  \end{pmatrix}^2
  $$
