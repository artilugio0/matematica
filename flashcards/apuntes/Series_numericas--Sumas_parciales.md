# Series numericas: Sumas parciales


Dada una sucesión $a: \mathbb{N} \to \mathbb{R}$, se definen a las sumas parciales de $a$ como:

$$
\begin{aligned}
S_1 &= \sum\limits_{k = 1}^{1} a_k = a_1 \\
S_2 &= \sum\limits_{k = 1}^{2} a_k = a_1 + a_2 = S_1 + a_2 \\
&\vdots \\
S_n &= \sum\limits_{k = 1}^{n} a_k = a_1 + a_2 +\ \dots\ + a_n = S_{n-1} + a_n \\
\end{aligned}
$$
