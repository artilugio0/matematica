# Algoritmo de Euclides

## Motivación

Es un algoritmo que permite encontrar el máximo común divisor de dos números de forma eficiente.

## Enunciado
Sean $a, b \in \mathbb{Z}$, no ambos nulos. Sin pérdida de generalidad, se asume $b \neq 0$.

Se definen: $r_{-1} = \lvert a \rvert, r_0 = \lvert b \rvert$

Luego para cada $i \in \mathbb{N}$, usando el _Algoritmo de división_ con los enteros $r_{i-2}, r_{i-1}$, se encuentran $q_{i}, r_{i}$ tales que $r_{i-2} = r_{i-1}q_i + r_i$. Se repite el procedimiento incrementando $i$ hasta llegar a $i = n+1$ tal que $r_{n+1} = 0$. Entonces se tendrá: $r_{n-1} = r_n q_{n+1} + 0$, en este punto se finaliza el algoritmo.

El último resto no nulo será el máximo común divisor de $a$ y $b$: $r_n = mcd(a, b)$

Nota: El algoritmo siempre finaliza porque el _Algoritmo de división_ garantiza que $0 \leq r_i < r_{i-1}$. Por lo que se tiene una sucesión estrictamente decreciente de números enteros no negativos que tendrá como máximo $\lvert b \rvert$ elementos.


## Demostración

### Estrategia

1. Demostrar que $r_n \mid a \wedge r_n \mid b$ iterando desde el último paso al primero
2. Demostrar que si $d \mid a \wedge d \mid b$ entonces $d \mid r_n$, iterando desde el primer paso hasta el último

### Paso 1: $r_n$ es divisor común

Siguiendo el algoritmo de Euclides, se tiene la sucesión de pasos:

$r_{-1} = r_0 q_1 + r_1$

$r_{0} = r_1 q_2 + r_2$

$r_{1} = r_2 q_3 + r_3$

...

$r_{n-2} = r_{n-1} q_n + r_n$

$r_{n-1} = r_n q_{n+1} + 0$

Por definición de divisibilidad, $r_n \mid r_{n-1}$. Entonces, por _Divisibilidad - Teorema 1 - Propiedad 3_, $r_n \mid r_{n-1} q_n$. Entonces, por _Divisibilidad - Teorema 1 - Propiedad 7_, $r_n \mid r_{n-2}$. Iterando de esta forma sobre todos los $r_i$, se llega a que $r_n \mid r_0 \wedge r_n \mid r_{-1}$.

Como $r_{-1} = \lvert a \rvert$ y $r_0 = \lvert b \rvert$, entonces $r_n \mid \pm \lvert a \rvert \wedge r_n \mid \pm \lvert b \rvert$. Por lo tanto, $r_n \mid a \wedge r_n \mid b$.


### Paso 2: $r_n$ es mayor o igual a cualquier otro divisor

Sea $d \in \mathbb{Z}$ tal que $d \mid a \wedge d \mid b$. Entonces $d \mid r_{-1} \wedge d \mid r_0$. De $r_{-1} = r_0 q_1 + r_1$ se tiene que $r_{-1} + r_0 (-q_1) = r_1$, y por _Divisibilidad - Teorema 1 - Propiedad 7_, $d \mid r_1$. Por el mismo argumento aplicado a cada $r_i$, se tiene que $d \mid r_2$, $d \mid r_3$, ..., $d \mid r_n$.

Por _Divisibilidad - Teorema 1 - Propiedad 6_, $d \leq \lvert d \rvert \leq \lvert r_n \rvert = r_n$. Por lo tanto, $d \leq r_n$.


## Ejemplos

- $a = 66, b = 18$:

  $66 = 18 \cdot 3 + 12$

  $18 = 12 \cdot 1 + 6$

  $12 = 6 \cdot 2 + 0$

  Entonces, $mcd(66, 18) = 6$.

- $a = 5, b = 8$ (con $a < b$ el algoritmo igual funciona):

  $5 = 8 \cdot 0 + 5$

  $8 = 5 \cdot 1 + 3$

  $5 = 3 \cdot 1 + 2$

  $3 = 2 \cdot 1 + 1$

  $2 = 1 \cdot 2 + 0$

  Entonces, $mcd(5, 8) = 1$.


## Ejemplos destacables

- Uno de los enteros es nulo: $a = 0, b = 9$:

  $0 = 9 \cdot 0 + 0$

  El último $r_i$ no nulo es $r_0 = 9$, por lo tanto $mcd(0, 9) = 9$.
- Entero negativo: $a = -66, b = 18$:

  $\lvert -66 \rvert = 66 = 18 \cdot 3 + 12$

  $18 = 12 \cdot 1 + 6$

  $12 = 6 \cdot 2 + 0$

  Entonces, $mcd(-66, 18) = 6$.


## Análisis de hipótesis: ¿por qué son necesarias las hipótesis?

El máximo común divisor está definido cuando $a$ y $b$ no son ambos nulos, y el _Algoritmo de división_ requiere que $b$ no sea nulo.


## Aplicaciones

- Expresar un entero como combinación lineal de otros dos
- Resolución de ecuaciones diofánticas lineales
