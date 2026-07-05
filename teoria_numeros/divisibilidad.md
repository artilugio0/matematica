# Divisibilidad

## Definición

Sean $a, b \in \mathbb{Z}$, con $a \neq 0$. Se dice que $a$ divide a $b$ si existe $c \in \mathbb{Z}$ tal que $b = ac$.

Se simboliza: $a \mid b$.

## Motivación

- La definición de divisibilidad es el punto de partida del estudio de la teoría de números. Otras definiciones importantes como la de _número primo_ se basan en la de divisibilidad.
- En general la división entre dos números enteros no tiene como resultado otro número entero. La relación de divisibilidad identifica los casos en los que sí es posible realizar la división y obtener un entero como resultado.

## Ejemplos

- $6 \mid 24$
- $7 \nmid 20$
- El signo no afecta la divisibilidad: $3 \mid 6$, $-3 \mid 6$, $3 \mid -6$ y $-3 \mid -6$
- La relación no es simétrica: $3 \mid 12$, pero $12 \nmid 3$

## Ejemplos destacables
Para todo $a \in \mathbb{Z},\ a \neq 0$:

- $a \mid 0$: $10 \mid 0$
- $a \mid a$: $10 \mid 10$

Para todo $a \in \mathbb{Z}$:

- $\pm 1 \mid a$: $1 \mid 10$, $-1 \mid 10$

## Restricciones

Si $a \mid b$, $a$ no puede ser $0$. Hay dos casos a analizar:

Si $a = 0 \wedge b \neq 0$, no existe $c \in \mathbb{Z}$ tal que $b = ac$, porque $ac = 0\ \forall\ c \in \mathbb{Z}$.

Si $a = 0 \wedge b = 0$, $c$ puede tomar cualquier valor y $0 = 0c$ se cumple. Si bien la definición de divisibilidad no requiere que $c$ sea único, este es el único caso en el que se da esta situación. Esta es la razón por la cual la división por $0$ no está definida.

# Teorema 2.1

- $a \mid 0$
- $a \mid a$
- $\pm 1 \mid a$

**Demostración**:

- $0 = a0 \Rightarrow a \mid 0$
- $a = a1 \Rightarrow a \mid a$
- $a = 1a = (-1)(-a) \Rightarrow 1 \mid a \wedge -1 \mid a$

# Teorema 2.2

$a \mid \pm 1 \Leftrightarrow a = \pm 1$

**Demostración**:

Si $a \mid \pm 1$, entonces existe $c \in \mathbb{Z}$ tal que $\pm 1 = ac$. Eso implica que $1 = \lvert ac \rvert = \lvert a \rvert \lvert c \rvert$, y que $a \neq 0$ y $c \neq 0$ (sino $\lvert a \rvert \lvert c \rvert = 0$). Entonces $\lvert c \rvert \geq 1$, lo que implica que $\lvert a \rvert \leq 1$. Y dado que $a$ no puede ser $0$, $\lvert a \rvert = 1$, es decir, $a = \pm 1$.

Si $a = \pm 1$, tomando $c = a$ se tiene $1 = ac \wedge -1 = a(-c)$. Por lo tanto $a \mid \pm 1$.

# Teorema 2.3

$a \mid b \wedge c \mid d \Rightarrow ac \mid bd$. En particular $a \mid b \Rightarrow a \mid b \cdot d$

**Demostración**:

Si $a \mid b \wedge c \mid d$, entonces existen $k_1, k_2 \in \mathbb{Z}$ tales que $b = ak_1$ y $d = ck_2$. Multiplicando miembro a miembro se tiene $bd = (ac)(k_1 k_2)$. Por lo tanto, $ac \mid bd$.

En particular $1 \mid d$, por lo tanto $a \mid b \cdot d$.


# Teorema 2.4

$a \mid b \wedge b \mid c \Rightarrow a \mid c$

**Demostración**:

Si $a \mid b \wedge b \mid c$, entonces existen $k_1, k_2 \in \mathbb{Z}$ tales que $b = ak_1$ y $c = bk_2$. Reemplazando a $b$ en la segunda igualdad se tiene que $c = a(k_1 k_2)$. Por lo tanto $a \mid c$.

# Teorema 2.5

Sean $a, b \in \mathbb{Z}$ no nulos.

$a \mid b \wedge b \mid a \Leftrightarrow a = \pm b$

**Demostración**:

Si $a \mid b \wedge b \mid a$, entonces existen $k_1, k_2 \in \mathbb{Z}$ tales que $b = ak_1$ y $a = bk_2$. Reemplazando $a$ en la primera igualdad se tiene que $b = b(k_1 k_2)$. Como $b \neq 0$ (porque $b \mid a$), eso implica que $k_1 k_2 = 1$, luego $(k_1 = 1 \wedge k_2 = 1) \lor (k_1 = -1 \wedge k_2 = -1)$. Por lo tanto, $a = b \lor a = -b$, es decir, $a = \pm b$.

Si $a = \pm b$, entonces $a = b1 \lor a = b(-1)$, lo que implica que $b \mid a$. Por otro lado, si $a = \pm b$, entonces $b = \pm a$, lo que implica que $a \mid b$.

Luego, $a \mid b \wedge b \mid a$.

# Teorema 2.6

$a \mid b \wedge b \neq 0 \Rightarrow \lvert a \rvert \leq \lvert b \rvert$

**Demostración**:

Si $a \mid b \wedge b \neq 0$, entonces existe $c \in \mathbb{Z}$ tal que $b = ac$. Llevándolo a valores absolutos, se tiene que $\lvert b \rvert = \lvert ac \rvert = \lvert a \rvert \lvert c \rvert$. Como $b \neq 0$, debe ser $c \neq 0$, lo que implica que $\lvert c \rvert \geq 1$, y por lo tanto $\lvert a \rvert \leq \lvert a \rvert \lvert c \rvert = \lvert b \rvert$. Es decir, $\lvert a \rvert \leq \lvert b \rvert$.


# Teorema 2.7

$a \mid b \wedge a \mid c \Rightarrow a \mid (bx + cy) \text{,  } \forall\ x, y \in \mathbb{Z}$

**Demostración**:

Si $a \mid b \wedge a \mid c$, entonces existen $k_1, k_2 \in \mathbb{Z}$ tales que $b = ak_1$ y $c = ak_2$.

Sean $x, y \in \mathbb{Z}$, entonces $bx + cy = a k_1 x + a k_2 y = a(k_1 x + k_2 y) \Rightarrow a \mid (bx + cy)$.


# Teorema 2.8

$a \mid (b \pm c) \wedge a \mid b \Rightarrow a \mid \pm c$

**Demostración**:

Si $a \mid (b \pm c) \wedge a \mid b$, entonces existe $k_1, k_2 \in \mathbb{Z}$ tales que $ak_1 = b \pm c \wedge ak_2 = b$. Sustituyendo en la primera igualdad se tiene que $ak_1 = b \pm c = ak_2 \pm c \Rightarrow a(k_1 - k_2) = \pm c$. Por lo tanto $a \mid \pm c$.


# Teorema 2.9

$a \mid b \Leftrightarrow ac \mid bc, \forall\ c \in \mathbb{Z}, c \neq 0$

**Demostración**:

Si $a \mid b$, entonces existe $k \in \mathbb{Z}$ tal que $ak = b$. Sea $c \in \mathbb{Z}, c \neq 0$, multiplicando la igualdad por $c$ se obtiene $(ac)k = bc$. Por lo tanto $ac \mid bc$.

Si $ac \mid bc$ con $c \neq 0$, entonces existe $k \in \mathbb{Z}$ tal que $ack = bc$. Dado que $c \neq 0$, se puede dividir ambos miembros por $c$ obteniendo $ak = b$. Por lo tanto $a \mid b$.


# Teorema 2.10

Todo entero no nulo tiene un número finito de divisores.

**Demostración**:

Sean $a, d \in \mathbb{Z}$, y $a \neq 0, d \neq 0$ tales que $d \mid a$. Por _Teorema 2.6_, $\lvert d \rvert \leq \lvert a \rvert$. Por lo tanto, no puede haber más de $2 \lvert a \rvert$ divisores de $a$, ya que hay $2\lvert a \rvert$ enteros $d$ tales que $-\lvert a \rvert \leq d \leq \lvert a \rvert$, con $d \neq 0$. Como la cantidad de divisores posibles es acotada, es una cantidad finita, lo cual demuestra el teorema.
