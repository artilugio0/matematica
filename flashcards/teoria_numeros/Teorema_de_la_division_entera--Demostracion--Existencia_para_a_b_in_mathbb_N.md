# Teorema de la división entera: Demostración: Existencia para $a, b \in \mathbb{N}$

Sean $a, b \in \mathbb{N_0}$ con $b > 0$.

Se considera el conjunto $R = \{ a - bq \mid q \in \mathbb{N_0} \wedge a - bq \geq 0 \}$.

El conjunto no está vacío, dado que $a = a - b0$ pertenece al conjunto.

Por el principio del buen orden de $\mathbb{N_0}$, existe un elemento mínimo en $R$. Sea $r_0 = a - bq_0$ el elemento mínimo de $R$.
Por definición de $q_0$ y $r_0$ se tiene que $a = bq_0 + r_0$, y $q_0, r_0 \geq 0$.

$r_0$ debe ser menor que $b$,
de otra forma se tiene $r_1 = r_0 - b = a - b(q_0 + 1)$, por lo que $r_1 \in R$, y $0 \leq r_1 < r_0$, por lo tanto $r_0$ no sería el mínimo de $R$, lo cual es una contradicción.

De esta forma queda demostrada la existencia de $q_0, r_0$ que cumplen las condiciones del teorema.
