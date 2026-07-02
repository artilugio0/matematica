# Algoritmo de Euclides: Enunciado

Sean $a, b \in \mathbb{Z}$, no ambos nulos. Sin pérdida de generalidad, se asume $b \neq 0$.

Si $a \mid b$, entonces $mcd(a, b) = \lvert a \rvert$. Si $b \mid a$, entonces $mcd(a, b) = \lvert b \rvert$. Para cualquier otro caso se sigue el siguiente procedimiento.

Se definen: $r_{-1} = a, r_0 = b$

Luego para cada $i \in \mathbb{N}$, usando el _Teorema 1.1_ con los enteros $r_{i-2}, r_{i-1}$, se encuentran $q_{i}, r_{i}$ tales que $r_{i-2} = r_{i-1}q_i + r_i$. Se repite el procedimiento incrementando $i$ hasta llegar a $i = n+1$ tal que $r_{n+1} = 0$. Entonces se tendrá: $r_{n-1} = r_n q_{n+1} + 0$, en este punto se finaliza el algoritmo.

El último resto no nulo será el máximo común divisor de $a$ y $b$: $mcd(a, b) = r_n$.

Nota: El algoritmo siempre finaliza porque el _Teorema 1.1_ garantiza que $0 \leq r_i < \lvert r_{i-1} \rvert$. Por lo que se tiene una sucesión estrictamente decreciente de números enteros no negativos que tendrá como máximo $\lvert b \rvert$ elementos.
