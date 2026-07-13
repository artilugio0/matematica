# Teorema 8.8


Sea $a \in \mathbb{Z}$ tal que $\lvert a \rvert > 1$ y $b, n \in \mathbb{N}$.

$a = \pm b^n$ si y solo si en su forma canónica las potencias de cada primo divisor de $a$ son múltiplos de $n$.

**Demostración**:

($\Rightarrow$)

Expresando a $b$ en su forma canónica, se obtiene:

$$
\begin{aligned}
a &= \pm (p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot\ ... \cdot p_k^{\alpha_k})^n \\
&= \pm p_1^{n \cdot \alpha_1} \cdot p_2^{n \cdot \alpha_2} \cdot\ ...\ \cdot p_k^{n \cdot \alpha_k}
\end{aligned}
$$

Por lo tanto, todos los divisores primos de $a$ tienen potencias múltiplos de $n$.

($\Leftarrow$)

Si $a = \pm p_1^{n \cdot \alpha_1} \cdot p_2^{n \cdot \alpha_2} \cdot\ ... \cdot p_k^{n \cdot \alpha_k}$, entonces $a = \pm (p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot\ ...\ \cdot p_k^{\alpha_k})^n = \pm b^n$.
