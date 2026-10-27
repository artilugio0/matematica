# Teorema 4.8


Sean $V$ un espacio vectorial, $v_1,\ \dots\ , v_k \in V$ y $\alpha_1,\ \dots\ , \alpha_k \in \mathbb{K}$.

$\sum\limits_{i = 1}^k \alpha_i \cdot v_i = \alpha_1 \cdot v_1 +\ \dots\ + \alpha_k \cdot v_k \in V$


**Demostración**:

Se demuestra por inducción sobre la cantidad de vectores.

Sean $v_1 \in V$ y $\alpha_1 \in \mathbb{K}$, por la definición de espacio vectorial, $\alpha_1 \cdot v_1 \in V$.

Se asume que se cumple para $k$ vectores.

Si $w = \sum\limits_{i = 1}^{k + 1} \alpha_i \cdot v_i$, con $v_i \in V$ y $\alpha_i \in \mathbb{K}$, entonces $w = (\sum\limits_{i = 1}^k \alpha_i \cdot v_i) + \alpha_{k+1} \cdot v_{k+1}$. Por hipótesis inductiva, $\sum\limits_{i = 1}^k \alpha_i \cdot v_i \in V$, y por definición de espacio vectorial $\alpha_{k+1} \cdot v_{k+1} \in V$. Por definición de espacio vectorial entonces, $w \in V$.

Por lo tanto, queda demostrado para todo $k \geq 1$.

## Tags

- algebra_lineal
- espacios_vectoriales
- teorema
