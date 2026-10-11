# Series de funciones: Series de Taylor: Cuándo es la suma igual a la función?


Sean $f: A \subseteq \mathbb{R} \to \mathbb{R}$ derivable para todo orden de derivación en un entorno $E(x_0)$, $P_n(x)$ el polinomio de Taylor de grado $n$ de la función centrado en $x_0$ y $R_n(x)$ su resto n-ésimo.

Entonces:

$f(x) = P_n(x) + R_n(x)$

Luego,

$$
\begin{aligned}
f(x) = \lim\limits_{n \to \infty} P_n(x) &\Leftrightarrow \lim\limits_{n \to \infty} R_n(x) = 0 \\
              &\Leftrightarrow \forall\ x \in DCV: \lim\limits_{n \to \infty} \frac{f^{(n+1)}(\theta)}{(n + 1)!} \cdot (x - x_0)^{n + 1} = 0 \\
\end{aligned}
$$

## Tags

- calculo
