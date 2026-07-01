# Máximo común divisor

## Definición

Sean $a, b \in \mathbb{Z}$ no ambos nulos, el máximo común divisor de $a$ y $b$ es el número $d \in \mathbb{N}$ tal que:

- $d \mid a \wedge d \mid b$
- $\forall\ c \in \mathbb{Z}: c \mid a \wedge c \mid b \Rightarrow c \leq d$

Se suele simbolizar de las siguientes formas:

- $mcd(a, b)$
- $gcd(a, b)$
- $(a : b)$

Nota: su existencia está garantizada ya que $1 \mid a \wedge 1 \mid b$, y dado que $a$ y $b$ no son ambos nulos. Por _Divisibilidad - Teorema 2_, la cantidad de divisores comunes es finita, y por lo tanto habrá uno que sea el máximo.

## Motivación

Su definición y estudio es importante porque es un concepto utilizado en el estudio de teoría de números, estructuras algebráicas, combinatoria, etc.

## Ejemplos

- $mcd(15, 10) = mcd(-15, 10) = mcd(15, -10) = mcd(-15, -10) = 5$
- $mcd(3, 9) = 3$
- $mcd(8, 21) = 1$
- $mcd(6, 6) = 6$

## Ejemplos destacables

- $mcd(0, a) = \lvert a \rvert$:
  - $mcd(0, 21) = 21$
  - $mcd(0, -21) = 21$
- $mcd(\pm 1, a) = 1$:

## Restricciones

$a$ y $b$ no pueden ser ambos $0$, dado que $0$ tiene infinitos divisores y por lo tanto no hay uno que sea máximo.

## Teorema 1
### Enunciado

Propiedades básicas del máximo común divisor.

### Propiedad 1

#### Enunciado

$mcd(a, a) = \lvert a \rvert$

#### Demostración

Si $a > 0$ , $a = \lvert a \rvert \cdot 1$. Si $a < 0$, $a = \lvert a \rvert \cdot (-1)$. Entonces $\lvert a \rvert \mid a$.

Si $d \mid a$, por _Divisibilidad - Teorema 1 - propiedad 6_: $d \leq \lvert d \rvert \leq \lvert a \rvert$.

Por lo tanto $mcd(a, a) = \lvert a \rvert$.

### Propiedad 2

#### Enunciado

$mcd(a, 0) = \lvert a \rvert$

#### Demostración

$\lvert a \rvert \mid 0 \wedge \lvert a \rvert \mid a$. 

Si $d \mid a$, por _Divisibilidad - Teorema 1 - propiedad 6_: $d \leq \lvert d \rvert \leq \lvert a \rvert$. Entonces, cualquier divisor común de $a$ y $0$ será menor o igual a $\lvert a \rvert$.

Por lo tanto $mcd(a, 0) = \lvert a \rvert$.
 

### Propiedad 3

#### Enunciado

$mcd(\pm 1, a) = 1$

#### Demostración

Si $d \mid a \wedge d \mid \pm 1$, entonces por _Divisibilidad - Teorema 1 - propiedad 2_: $d = \pm 1$. Luego el mayor de los divisores comunes es $1$, por lo tanto $mcd(\pm 1, a) = 1$.

### Propiedad 4

#### Enunciado

$mcd(a, b) = mcd(b, a)$

#### Demostración

Si $mcd(a, b) = d$, entonces $d \mid a \wedge d \mid b$, y para todo $c \in \mathbb{Z}$ tal que $c \mid a \wedge c \mid b$ se cumple que $c \leq d$. Por definición eso implica que $mcd(b, a) = d$. Por lo tanto, $mcd(a, b) = mcd(b, a)$.


### Propiedad 5

#### Enunciado

Para $a, b \in \mathbb{Z}$, no ambos nulos: $mcd(a, a+b) \mid b$

#### Demostración

Sean $a, b \in \mathbb{Z}$, no ambos nulos, y sea $d = mcd(a, a+b)$.

Por definición de $d$, $d \mid a \wedge d \mid (a+b)$. Por _Divisibilidad - Teorema 1 - Propiedad 8_, $d \mid b$.


### Propiedad 6

#### Enunciado

Para $a, b \in \mathbb{Z}$, no ambos nulos: $mcd(a, b) = mcd(a, b + a \cdot k)$, para $k \in \mathbb{Z}$.

#### Demostración

Sea $d = mcd(a, b + a \cdot k)$.

Por definición, $d \mid a$, y por _Divisibilidad - Teorema 1 - Propiedad 3_, $d \mid a \cdot k$.

Por definición, $d \mid (b + a \cdot k)$. Y como $d \mid a \cdot k$, Por _Divisibilidad - Teorema 1 - Propiedad 8_, $d \mid b$.

Por lo tanto, $d$ es divisor común de $a$ y $b$.

Sea $d'$ un divisor común de $a$ y $b$. Por _Divisibilidad - Teorema 1 - Propiedad 7_, $d' \mid (b + a \cdot k)$. Por lo tanto, $d'$ es un divisor común de $a$ y $b + a \cdot k$. Como $d = mcd(a, b + a \cdot k)$, se tiene que $d' \leq d$. Por lo tanto $d$ es mayor o igual a cualquier otro divisor de $a$, $b$. Lo que implica que $d = mcd(a, b)$.
