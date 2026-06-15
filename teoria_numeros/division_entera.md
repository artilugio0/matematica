# Divisibilidad

## Teorema de la division entera

### Hipotesis
- $a, b\ \in \mathbb{Z}$
- $b\ \neq 0$

### Tesis
- Existen $q, r\ \in \mathbb{Z}$
- $a = bq + r$
- $0 \leq r < b$

### Demostracion
#### Estrategia
1. Demostrar existencia para $a, b\ \in \mathbb{N}$
2. Demostrar unicidad para $a, b\ \in \mathbb{N}$
3. Demostrar el caso $b < 0$

#### Existencia para $a, b\ \in \mathbb{N}$
Sean $a, b\ \in \mathbb{N_0}$ con $b > 0$, sin perdida de generalidad se puede asumir $a \geq b$.

Se considera el conjunto $R = \{ a - bq \mid q\ \in \mathbb{N_0} \wedge a - bq \geq 0 \}$.

El conjunto no esta vacio, dado que $a = a - b0$ pertenece al conjunto.

Por el pricipio del buen orden de $\mathbb{N}$, existe un elemento minimo en $R$. Sea $r_0 = a - bq_0$ el elemento minimo de $R$.
Por definicion de $q_0 y r_0$ se tiene que $a = bq_0 + r_0$, y $q_0, r_0 \geq 0$. $r_0$ debe ser menor que $b$,
de otra forma $0 \leq r_1 = r_0 - b = a - b(q_0 + 1) < r_0$ y por lo tanto $r_0$ no seria el minimo de $R$, lo cual es una contradiccion.

De esta forma queda demostrada la existencia de $q_0, r_0$ que cumplen las condiciones del teorema.


#### Unicidad para $a, b\ \in \mathbb{N}$
Sean $a, b\ \in \mathbb{N_0}, con $a \geq b$ y $q_0, r_0\ \in mathbb{N_0}$ tales que $a = bq_0 + r_0$, con $0 \leq r_0 < b$ (su existencia ya fue demostrada). Y sean tambien
$q_1, r_1\ \in mathbb{N_0}$ tales que $a = bq_1 + r_1$, con $0 \leq r_1 < b$. Sin perdida de generalidad, se puede asumir $r_0 \leq r_1$, y por lo tanto, $q_1 \leq q_0$.
)
De $a = bq_1 + r_1$ de $a = bq_0 + r_0$, tenemos que $r_1 = b(q_0-q_1) + r_0 \geq 0$, por lo tanto se tiene que $r_1 \leq r_0$, lo cual implica que $r_1 = r_0$ (porque $r_0 \leq r_1$) y por lo tanto $q_1 = q_0$.

Quedando asi demostrada la unicidad de $r$ y $q$.


#### Caso $a \geq 0,\ b < 0$
Sean $a\ in \mathbb{N_0}, b\ \in \mathbb{Z}$, con $b < 0$.

Existen $q, r\ \in \mathbb{N_0}$ unicos tales que $a = (-b)q + r$, con $0 \leq r < -b$, y por lo tanto, $a = b(-q) + r$, con $-q\ \in \mathbb{Z}$.
Quedando asi demostrado el teorema para el caso $b < 0$.

#### Caso $a < 0$
Sean $a\ in \mathbb{Z}, b\ \in \mathbb{Z}$, con $a < 0$ y $b \neq 0$.

Existen $r_0\ \in \mathbb{N_0}$ y $q_0\ \in \mathbb{Z}$ unicos tales que $-a = bq + r$, con $0 \leq r < \lvert b \rvert$.

Luego, $a = b(-q) - r$. Sumando y restando $b$ del lado derecho de la igualdad se tiene
- Si $b > 0$: $a = b(-q -1) + (b - r)$, donde $b - r > 0$, definiendo $q_0 = -q - 1$ y $r_0 = b - r$.
- Si $b < 0$: $a = b(-q +1) + (-b - r)$, donde $-b - r > 0$, definiendo $q_0 = -q + 1$ y $r_0 = -b - r$.

Por lo tanto existen valores unicos de $q_0, r_0$ que cumplen las condiciones del teorema.


### Ejemplos simples
- $a > 0$ y $b > 0$:

$$
a = 16,\, b = 3 \\
16 = 3 \cdot 5 + 1
$$

- $a > 0$ y $b < 0$:

$$
a = 16,\, b = -3 \\
16 = (-3) \cdot (5) + 1
$$

- $a < 0$ y $b > 0$:

$$
a = -16,\, b = 3 \\
-16 = 3 \cdot (-6) + 2
$$

- $a < 0$ y $b < 0$:

$$
a = -16,\, b = -3 \\
-16 = (-3) \cdot 6 + 2
$$


### Ejemplos limites
- $a = 0$:

$$
a = 0,\, b = 3 \\
0 = 3 \cdot 0 + 0
$$

- $a$ es multiplo de $b$

$$
a = 15,\, b = 5 \\
15 = 5 \cdot 3 + 0
$$

### Ejemplo donde no se cumple la hipotesis
Si $b = 0$, no se pueden encontrar $q, r$ que cumplan las condiciones del teorema, dado que no hay valor posible para $0 \leq r < \lvert b \rvert$.

- $r$ no cumple la condicion si $a \neq 0$:
$$
a = 10,\, b = 0 \\
10 = 0 \cdot 1 + 10
$$

- $r$ tampoco cumple la condicion si $a = 0$, porque $0 \geq b$:
$$
a = 0,\, b = 0 \\
0 = 0 \cdot 1 + 0
$$


### Analisis de hipotesis: por que son necesarias la hipotesis?

### Demostracion
