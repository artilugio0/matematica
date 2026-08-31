# Series de funciones: Serie de funciones mayorante


Sea $\sum\limits_{n = 1}^{\infty} f_n(x)$ una serie de funciones con dominio de convergencia $DCV$.

Se dice que la serie de funciones es mayorante en un intervalo $A \subseteq DCV$ si existe una serie numérica $\sum\limits_{n = 1}^{\infty} a_n$ de términos positivos y convergente tal que $\forall\ x \in A: \lvert f_n(x) \rvert \leq a_n$.

Si una serie de funciones es mayorante, entonces:

- Si las funciones $f_n$ son contínuas $\Rightarrow S(x) = \sum\limits_{n = 1}^{\infty} f_n(x)$ es contínua.
- Si las funciones $f_n$ son derivables $\Rightarrow S(x) = \sum\limits_{n = 1}^{\infty} f_n(x)$ es derivable y su derivada es $\sum\limits_{n = 1}^{\infty} f_n'(x)$.
- Si las funciones $f_n$ son integrables $\Rightarrow S(x) = \sum\limits_{n = 1}^{\infty} f_n(x)$ es integrable y $\int\limits_{a}^{b} S(x)dx = \sum\limits_{n = 1}^{\infty} \left[\int\limits_{a}^{b} f_n(x)dx \right]$.
