# Teorema 4.8


Sean $V$ un espacio vectorial y $S = \{v_1,\ \dots\ , v_k\} \subseteq V$.

Si $w$ es una combinación lineal de los vectores de $S$, entonces $w \in V$.

**Demostración**:

Se demuestra por inducción sobre la cantidad de vectores de $S$.

Si $S = \{v_1\}$ y $w$ es una combinación lineal de los vectores de $S$, entonces $w = \alpha_1 \cdot v_1$, con $\alpha_1 \in \mathbb{K}$. Por la definición de espacio vectorial, $w \in V$.

Se asume que se cumple para los conjuntos de $k$ vectores.

Si $S = \{v_1,\ \dots\ , v_k, v_{k+1}\} \subseteq V$ y $w$ es una combinación lineal de los vectores de $S$, entonces $w = \sum\limits_{i = 1}^{k + 1} \alpha_i \cdot v_i$, con $\alpha_i \in \mathbb{K}$. Luego, $w = (\sum\limits_{i = 1}^k \alpha_i \cdot v_i) + \alpha_{k+1} \cdot v_{k+1}$. Por hipótesis inductiva, $\sum\limits_{i = 1}^k \alpha_i \cdot v_i \in V$, y por definición de espacio vectorial $\alpha_{k+1} \cdot v_{k+1} \in V$. Por definición de espacio vectorial entonces, $w \in V$.

Por lo tanto, queda demostrado para cualquier conjunto no vacío y finito de vectores.

## Tags

- algebra_lineal
- espacios_vectoriales
- teorema
