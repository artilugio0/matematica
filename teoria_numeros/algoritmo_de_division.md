# Algoritmo de división

## Motivación
- El teorema formaliza el procedimiento conocido de división con resto, y lo extiende para los casos en los que $a$ y $b$ son números enteros.
- Permite clasificar a los números enteros por su resto en la división por un número entero dado.
Esto permite transformar el estudio de los infinitos números enteros al estudio de un número finito de casos.

## Hipótesis
- $a, b \in \mathbb{Z}$
- $b\ \neq 0$

## Tesis
Existen $q, r \in \mathbb{Z}$ únicos tales que:

- $a = bq + r$
- $0 \leq r < \lvert b \rvert$

## Demostración
### Estrategia
1. Demostrar existencia para $b > 0$
2. Demostrar unicidad
3. Demostrar para el caso $b < 0$


### Existencia: para $b > 0$
Sean $a, b \in \mathbb{Z}$ con $b > 0$.

Se considera el conjunto $R = \{ a - bq \mid q \in \mathbb{Z} \wedge a - bq \geq 0 \}$.

El conjunto no está vacío porque tomando $q = -\lvert a \rvert$, se tiene $a - bq = a - b(-\lvert a \rvert) = a + b \lvert a \rvert$. Como $b \geq 1$, entonces $a + b\lvert a \rvert \geq 0$, y por lo tanto pertenece a $R$.

Por el principio del buen orden de $\mathbb{N_0}$, existe un elemento mínimo en $R$. Sea $r_0 = a - bq_0$ el elemento mínimo de $R$.
Por definición de $q_0$ y $r_0$ se tiene que $a = bq_0 + r_0$, y $r_0 \geq 0$.

$r_0$ debe ser menor que $b$,
de otra forma se tiene $r_1 = r_0 - b = a - b(q_0 + 1) \in R$, y $0 \leq r_1 < r_0$. Por lo tanto $r_0$ no sería el mínimo de $R$, lo cual es una contradicción.

De esta forma queda demostrada la existencia de $q_0, r_0$ que cumplen las condiciones del teorema.


### Unicidad para $b > 0$
Sean $a, b \in \mathbb{Z},\ b > 0$ y $q_0, r_0 \in \mathbb{Z}$ tales que $a = bq_0 + r_0$, con $0 \leq r_0 < b$ (su existencia ya fue demostrada).

Y sean también $q_1, r_1 \in \mathbb{Z}$ tales que $a = bq_1 + r_1$, con $0 \leq r_1 < b$.

Sin pérdida de generalidad, se puede asumir $r_0 \leq r_1$, y por lo tanto, $q_1 \leq q_0$.


De $a = bq_1 + r_1$ y $a = bq_0 + r_0$, tenemos que $r_1 - r_0 = b(q_0-q_1)$. Pero $0 \leq r_1 - r_0 < b$, porque $r_0 \leq r_1 < b$. Entonces se debe dar que $q_0 - q_1 = 0$, y por lo tanto, $q_1 = q_0$. De donde sigue que $r_1 = r_0$.

Quedando así demostrada la unicidad de $r$ y $q$.


### Caso $b < 0$
Sean $a, b \in \mathbb{Z}$, con $b < 0$.

Existen $q_0, r_0 \in \mathbb{Z}$ únicos tales que $a = (-b)q_0 + r_0$, con $0 \leq r_0 < \lvert b \rvert$, y por lo tanto, $a = b(-q_0) + r_0$, con $-q_0 \in \mathbb{Z}$.

Definiendo $q_1 = -q_0,\ r_1 = r_0$, se tienen los valores $q_1, r_1$ que demuestran el teorema para el caso $b < 0$.

La unicidad de $q_1$ y $r_1$ queda garantizada por la unicidad de $q_0$ y $r_0$.


## Ejemplos simples
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


## Ejemplos límites
- $a = 0$:

$$
\begin{aligned}
a = 0,\ b = 3 \\
0 = 3 \cdot 0 + 0
\end{aligned}
$$

- $a$ es múltiplo de $b$

$$
\begin{aligned}
a = 15,\ b = 5 \\
15 = 5 \cdot 3 + 0
\end{aligned}
$$

## Ejemplo donde no se cumple la hipótesis
Si $b = 0$, no se pueden encontrar $q,\ r$ que cumplan las condiciones del teorema, dado que no hay valor posible para $r$ tal que $0 \leq r < \lvert b \rvert$.

- $q$ no es único y $r$ no cumple la condición si $a \neq 0$:
$$
\begin{aligned}
a = 10,\ b = 0 \\
10 = 0 \cdot 1 + 10
\end{aligned}
$$

- Si $a = 0$, $q$ tampoco es único y $r$ tampoco cumple la condición porque $0 \leq r < \lvert b \rvert$ implica $0 < 0$:
$$
\begin{aligned}
a = 0,\ b = 0 \\
0 = 0 \cdot 1 + 0
\end{aligned}
$$


## Análisis de hipótesis: ¿por qué son necesarias las hipótesis?
- $a, b \in \mathbb{Z}$: La división con resto tiene sentido cuando $a$ y $b$ son enteros, donde no hay inversos multiplicativos. En conjuntos donde sí hay inversos multiplicativos para todos los elementos excepto el $0$, siempre se puede efectuar la división sin resto (cuando $b \neq 0$).

- $b\ \neq 0$: Si $b = 0$, no se pueden hallar valores de $q$ y $r$ que cumplan las condiciones del teorema. $q$ podría tomar cualquier valor, pero no hay valor posible para $r$, ya que eso implicaría $0 < 0$. Intuitivamente esto se traduce en que la división por $0$ no está definida.


## Aplicaciones
- El cuadrado de un entero tiene resto $0$ o $1$ en la división por $4$
- El cuadrado de un número impar es de la forma $8k + 1$
