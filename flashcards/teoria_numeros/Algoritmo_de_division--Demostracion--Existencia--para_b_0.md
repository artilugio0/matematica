# Algoritmo de división: Demostración: Existencia: para $b > 0$

Sean $a, b \in \mathbb{Z}$ con $b > 0$.

Se considera el conjunto $R = \{ a - bq \mid q \in \mathbb{Z} \wedge a - bq \geq 0 \}$.

El conjunto no está vacío porque tomando $q = -\lvert a \rvert$, se tiene $a - bq = a - b(-\lvert a \rvert) = a + b \lvert a \rvert$. Como $b \geq 1$, entonces $a + b\lvert a \rvert \geq 0$, y por lo tanto pertenece a $R$.

Por el principio del buen orden de $\mathbb{N_0}$, existe un elemento mínimo en $R$. Sea $r_0 = a - bq_0$ el elemento mínimo de $R$.
Por definición de $q_0$ y $r_0$ se tiene que $a = bq_0 + r_0$, y $r_0 \geq 0$.

$r_0$ debe ser menor que $b$,
de otra forma se tiene $r_1 = r_0 - b = a - b(q_0 + 1) \in R$, y $0 \leq r_1 < r_0$. Por lo tanto $r_0$ no sería el mínimo de $R$, lo cual es una contradicción.

De esta forma queda demostrada la existencia de $q_0, r_0$ que cumplen las condiciones del teorema.
