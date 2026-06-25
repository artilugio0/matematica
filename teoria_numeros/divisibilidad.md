# Divisibilidad

## Definición

Sean $a, b \in \mathbb{Z}$, con $a \neq 0$. Se dice que $a$ divide a $b$ si existe $c \in \mathbb{Z}$ tal que $b = ac$.

Se simboliza: $a \mid b$.

## Motivación

La definición de divisibilidad es el punto de partida del estudio de la teoría de números. Otras definiciones importantes como la de _número primo_ se basan en la de divisibilidad.

## Casos límite
Para todo $a \in \mathbb{Z},\ a \neq 0$:

- $a \mid 0$
- $1 \mid a$
- $a \mid a$

## Restricciones

Si $a \mid b$, $a$ no puede ser $0$. Hay dos casos a analizar:

Si $a = 0 \wedge b \neq 0$, no existe $c \in \mathbb{Z}$ tal que $b = ac$, porque $ac = 0\ \forall\ c \in \mathbb{Z}$.

Si $a = 0 \wedge b = 0$, $c$ puede tomar cualquier valor y $0 = 0c$ se cumple. Si bien la definición de divisibilidad no requiere que $c$ sea único, este es el único caso en el que se da esta situación.

## Teorema 1
### Enunciado

Propiedades básicas de la divisibilidad.

### Propiedad 1
#### Enunciado

- $a \mid 0$
- $1 \mid a$
- $a \mid a$

#### Demostración

- $0 = a0 \Rightarrow a \mid 0$
- $a = 1a \Rightarrow 1 \mid a$
- $a = a1 \Rightarrow a \mid a$

### Propiedad 2
#### Enunciado

$a \mid 1 \Leftrightarrow a = \pm 1$

#### Demostración

Si $a \mid 1$, entonces existe $c \in \mathbb{Z}$ tal que $1 = ac$. Eso implica que $1 = \lvert ac \rvert = \lvert a \rvert \lvert c \rvert$. Como $a \neq 0$, $\lvert a \rvert \geq 1$, por lo tanto $1 \geq \lvert c \rvert$. Y dado que $c$ no puede ser $0$ (de otra forma $ac = 0 \neq 1$), entonces $\lvert c \rvert = 1$. Consecuentemente, $\lvert a \rvert = 1$, es decir, $a = \pm 1$.

Si $a = \pm 1$, tomando $c = a$ se tiene $1 = ac$. Por lo tanto $a \mid 1$.

### Propiedad 3
#### Enunciado

$a \mid b \wedge c \mid d \Rightarrow ac \mid bd$

#### Demostración

Si $a \mid b \wedge c \mid d$, entonces existen $k_1, k_2 \in \mathbb{Z}$ tales que $b = ak_1$ y $d = ck_2$. Multiplicando miembro a miembro se tiene $bd = (ac)(k_1 k_2)$. Por lo tanto, $ac \mid bd$.


### Propiedad 4
#### Enunciado

$a \mid b \wedge b \mid c \Rightarrow a \mid c$

#### Demostración

Si $a \mid b \wedge b \mid c$, entonces existen $k_1, k_2 \in \mathbb{Z}$ tales que $b = ak_1$ y $c = bk_2$. Reemplazando a $b$ en la segunda igualdad se tiene que $c = a(k_1 k_2)$. Por lo tanto $a \mid c$.

### Propiedad 5
#### Enunciado

$a \mid b \wedge b \mid a \Leftrightarrow a = \pm b$

#### Demostración

Si $a \mid b \wedge b \mid a$, entonces existen $k_1, k_2 \in \mathbb{Z}$ tales que $b = ak_1$ y $a = bk_2$. Reemplazando $a$ en la primera igualdad se tiene que $b = b(k_1 k_2)$. Como $b \neq 0$ (porque $b \mid a$), eso implica que $k_1 k_2 = 1$, luego $(k_1 = 1 \wedge k_2 = 1) \lor (k_1 = -1 \wedge k_2 = -1)$. Por lo tanto, $a = b \lor a = -b$, es decir, $a = \pm b$.

Si $a = \pm b$, entonces $a = b1 \lor a = b(-1)$, lo que implica que $b \mid a$. Por otro lado, si $a = \pm b$, entonces $b = \pm a$, lo que implica que $a \mid b$.

Luego, $a \mid b \wedge b \mid a$.

### Propiedad 6
#### Enunciado

$a \mid b \wedge b \neq 0 \Rightarrow \lvert a \rvert \leq \lvert b \rvert$

#### Demostración

Si $a \mid b \wedge b \neq 0$, entonces existe $c \in \mathbb{Z}$ tal que $b = ac$. Llevándolo a valores absolutos, se tiene que $\lvert b \rvert = \lvert ac \rvert = \lvert a \rvert \lvert c \rvert$. Como $b \neq 0$, debe ser $c \neq 0$, lo que implica que $\lvert c \rvert \geq 1$, y por lo tanto $\lvert a \rvert \leq \lvert a \rvert \lvert c \rvert = \lvert b \rvert$. Es decir, $\lvert a \rvert \leq \lvert b \rvert$.


### Propiedad 7
#### Enunciado

$a \mid b \wedge a \mid c \Rightarrow a \mid (bx + cy) \text{,  } \forall\ x, y \in \mathbb{Z}$

#### Demostración

Si $a \mid b \wedge a \mid c$, entonces existen $k_1, k_2 \in \mathbb{Z}$ tales que $b = ak_1$ y $c = ak_2$.

Sean $x, y \in \mathbb{Z}$, entonces $bx + cy = a k_1 x + a k_2 y = a(k_1 x + k_2 y) \Rightarrow a \mid (bx + cy)$.


## Teorema 2

### Enunciado

Todo entero no nulo tiene un número finito de divisores

### Demostración

Sea $a, d \in \mathbb{Z}$, y $a \neq 0, d \neq 0$ tales que $d \mid a$. Por _Teorema 1 - propiedad 6_, $\lvert d \rvert \leq \lvert a \rvert$. Por lo tanto, no puede haber más de $2|a|$ divisores de $a$, ya que hay $2\lvert a \rvert$ enteros $d$ tales que $-\lvert a \rvert \leq d \leq \lvert a \rvert$, con $d \neq 0$. Como la cantidad de divisores posibles es acotada, es una cantidad finita, lo cual demuestra el teorema.
