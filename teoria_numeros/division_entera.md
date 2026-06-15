# Divisibilidad

## Teorema de la division entera

### Hipotesis
- $a, b\ \in \mathbb{Z}$
- $b\ \neq 0$

### Tesis
- Existen $q, r\ \in \mathbb{Z}$
- $a = bq + r$
- $0 \leq r < \lvert b \rvert$

### Demostracion
#### Estrategia
1. Demostrar existencia para $a, b\ \in \mathbb{N}$
2. Demostrar unicidad para $a, b\ \in \mathbb{N}$
3. Demostrar el caso $a > 0,\ b < 0$
4. Demostrar el caso $a < 0$

#### Existencia para $a, b\ \in \mathbb{N}$
Sean $a, b\ \in \mathbb{N_0}$ con $b > 0$.

Se considera el conjunto $R = \{ a - bq \mid q\ \in \mathbb{N_0} \wedge a - bq \geq 0 \}$.

El conjunto no esta vacio, dado que $a = a - b0$ pertenece al conjunto.

Por el pricipio del buen orden de $\mathbb{N_0}$, existe un elemento minimo en $R$. Sea $r_0 = a - bq_0$ el elemento minimo de $R$.
Por definicion de $q_0$ y $r_0$ se tiene que $a = bq_0 + r_0$, y $q_0, r_0 \geq 0$.

$r_0$ debe ser menor que $b$,
de otra forma se tiene $r_1 = r_0 - b = a - b(q_0 + 1)$, y $0 \leq r_1 < r_0$, por lo tanto $r_0$ no seria el minimo de $R$, lo cual es una contradiccion.

De esta forma queda demostrada la existencia de $q_0, r_0$ que cumplen las condiciones del teorema.


#### Unicidad para $a, b\ \in \mathbb{N}$
Sean $a, b\ \in \mathbb{N_0},\ b > 0$ y $q_0, r_0\ \in \mathbb{N_0}$ tales que $a = bq_0 + r_0$, con $0 \leq r_0 < b$ (su existencia ya fue demostrada).

Y sean tambien $q_1, r_1\ \in \mathbb{N_0}$ tales que $a = bq_1 + r_1$, con $0 \leq r_1 < b$.

Sin perdida de generalidad, se puede asumir $r_0 \leq r_1$, y por lo tanto, $q_1 \leq q_0$.


De $a = bq_1 + r_1$ y $a = bq_0 + r_0$, tenemos que $r_1 - r_0 = b(q_0-q_1)$. Pero $0 \leq r_1 - r_0 < b$, porque $r_0 \leq r_1 < b$. Entonces se debe dar que $q_0 - q_1 = 0$, y por lo tanto, $q_1 = q_0$. De donde sigue que $r_1 = r_0$.

Quedando asi demostrada la unicidad de $r$ y $q$.


#### Caso $a \geq 0,\ b < 0$
Sean $a\ \in \mathbb{N_0}, b\ \in \mathbb{Z}$, con $b < 0$.

Existen $q_0, r_0\ \in \mathbb{N_0}$ unicos tales que $a = (-b)q_0 + r_0$, con $0 \leq r_0 < \lvert b \rvert$, y por lo tanto, $a = b(-q_0) + r_0$, con $-q_0\ \in \mathbb{Z}$.

Definiendo $q_1 = -q_0,\ r_1 = r_0$, se tienen los valores $q_1, r_1$ que demuestran el teorema para el caso $b < 0$.

La unicidad de $q_1$ y $r_1$ queda garantizada por la unicidad de $q_0$ y $r_0$.

#### Caso $a < 0$
Sean $a\ \in \mathbb{Z}, b\ \in \mathbb{Z}$, con $a < 0$ y $b \neq 0$.

Existen $r_0\ \in \mathbb{N_0}$ y $q_0\ \in \mathbb{Z}$ unicos tales que $-a = bq_0 + r_0$, con $0 \leq r_0 < \lvert b \rvert$.

Luego, $a = b(-q_0) - r_0$. Si $r_0 = 0$, entonces $a = b(-q_0)$ con $q_1 = -q_0,\ r_1 = 0$ cumpliendo el teorema. De no ser asi, se tiene:

- Si $b > 0$: $a = b(-q_0 -1) + (b - r_0)$, donde $0 < b - r_0 < \lvert b \rvert$, definiendo $q_1 = -q_0 - 1$ y $r_1 = b - r_0$.
- Si $b < 0$: $a = b(-q_0 +1) + (-b - r_0)$, donde $0 < -b - r_0 < \lvert b \rvert$, definiendo $q_1 = -q_0 + 1$ y $r_1 = -b - r_0$.

Por lo tanto existen valores unicos de $q_1, r_1$ que cumplen las condiciones del teorema.

La unicidad de $q_1$ y $r_1$ queda garantizada por la unicidad de $q_0$ y $r_0$.


### Ejemplos simples
- $a > 0$ y $b > 0$:

$$
\begin{aligned}
a = 16,\ b = 3 \\
16 = 3 \cdot 5 + 1
\end{aligned}
$$

- $a > 0$ y $b < 0$:

$$
\begin{aligned}
a = 16,\ b = -3 \\
16 = (-3) \cdot (-5) + 1
\end{aligned}
$$

- $a < 0$ y $b > 0$:

$$
\begin{aligned}
a = -16,\ b = 3 \\
-16 = 3 \cdot (-6) + 2
\end{aligned}
$$

- $a < 0$ y $b < 0$:

$$
\begin{aligned}
a = -16,\ b = -3 \\
-16 = (-3) \cdot 6 + 2
\end{aligned}
$$


### Ejemplos limites
- $a = 0$:

$$
\begin{aligned}
a = 0,\ b = 3 \\
0 = 3 \cdot 0 + 0
\end{aligned}
$$

- $a$ es multiplo de $b$

$$
\begin{aligned}
a = 15,\ b = 5 \\
15 = 5 \cdot 3 + 0
\end{aligned}
$$

### Ejemplo donde no se cumple la hipotesis
Si $b = 0$, no se pueden encontrar $q,\ r$ que cumplan las condiciones del teorema, dado que no hay valor posible para $r$ tal que $0 \leq r < \lvert b \rvert$.

- $r$ no cumple la condicion si $a \neq 0$:
$$
\begin{aligned}
a = 10,\ b = 0 \\
10 = 0 \cdot 1 + 10
\end{aligned}
$$

- Si $a = 0$, $r$ tampoco cumple la condicion porque $0 \leq r < \lvert b \rvert$ implica $0 < 0$:
$$
\begin{aligned}
a = 0,\ b = 0 \\
0 = 0 \cdot 1 + 0
\end{aligned}
$$


### Analisis de hipotesis: por que son necesarias la hipotesis?

### Demostracion
