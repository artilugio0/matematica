# Identidad de Bezout
Teorema 5.1

## Motivación

El teorema permite caracterizar al máximo común divisor de $a$, $b$ como una combinación lineal entera de ambos números. Esto da lugar a la demostración de nuevas propiedades del máximo común divisor y nuevas aplicaciones.


## Hipótesis

- $a, b \in \mathbb{Z}$, no ambos nulos


## Tesis

Existen $x, y \in \mathbb{Z}$ tales que $a \cdot x + b \cdot y = mcd(a, b)$


## Demostración
### Estrategia

- Definir conjunto D
- Demostrar que tiene elemento mínimo
- Demostrar que $min\ D$ es divisor común de $a$ y $b$
- Demostrar cualquier otro divisor es menor o igual que $min\ D$


### Definir conjunto D

Sea $D = \{ a \cdot x + b \cdot y \mid x,\ y \in \mathbb{Z} \wedge a \cdot x + b \cdot y \geq 1 \}$.


### Demostrar que D tiene un mínimo

Tomando $x = a,\ y = b$. Se tiene $a \cdot a \geq 0$ y $b \cdot b \geq 0$. Y dado que $a$ y $b$ no son ambos nulos $a \cdot a + b \cdot b \geq 1$, y por lo tanto $D$ no está vacío.

Por el principio de buen orden de los números naturales, $D$ tiene un elemento mínimo.


### Demostrar que $min\ D$ es divisor común de $a$ y $b$

Sea $d = min\ D$. Por pertenecer a $D$, existen $x_0,\ y_0 \in \mathbb{Z}$ tales que $d = a \cdot x_0 + b \cdot y_0$.

Usando el _Teorema 1.1_, existen $q, r \in \mathbb{Z}$ tales que $a = d \cdot q + r$, con $0 \leq r < d$ (definición de $D$, $d \geq 1$).

Reemplazando a $d$ en esta última igualdad, se tiene $a = (a \cdot x_0 + b \cdot y_0) \cdot q + r$, entonces $r = a \cdot (1 - x_0 \cdot q) + b \cdot (-y_0 \cdot q)$. Como $0 \leq r < d$, $r$ debe ser $0$, de otra forma pertenecería a $D$ y sería menor a $d$, lo cual es un absurdo.

Como $r = 0$, entonces $a = d \cdot q$. Por lo tanto $d \mid a$.

Utilizando el mismo argumento, se tiene $d \mid b$. Luego $d$ es divisor común de $a$ y $b$.


### Demostrar cualquier otro divisor común es menor o igual que $min\ D$

Sea $d = min\ D = a \cdot x_0 + b \cdot y_0$, y $c \in \mathbb{Z}$ tal que $c \mid a \wedge c \mid b$.

Por _Teorema 2.7_, $c \mid (a \cdot x_0 + b \cdot y_0)$. Por lo tanto $c \mid d$. Y por _Teorema 2.6_, $c \leq \lvert c \rvert \leq \lvert d \rvert = d$. Luego, $c \leq d$.

Por lo tanto $d = mcd(a, b)$.


## Ejemplos simples

- $a = 42,\ b = 69$:

  $3 = 42 \cdot 5 + 69 \cdot (-3)$

- $a = 180,\ b = 144$:

  $36 = 180 \cdot 1 + 144 \cdot (-1)$


## Análisis de hipótesis: ¿por qué son necesarias las hipótesis?

Si $a = 0 \wedge b = 0$, $mcd(a, b)$ no está definido.


# Teorema 5.2

## Enunciado

Sean $a, b\ \in \mathbb{Z}$ no ambos nulos. 

$mcd(a, b)$ es el mínimo entero positivo de la forma $a \cdot x + b \cdot y$, con $x, y\ \in \mathbb{Z}$.

## Demostración

Queda demostrado por la demostración del _Teorema 5.1_.


# Teorema 5.3

## Enunciado

Sea $d \in \mathbb{N}$ y $a, b\ \in \mathbb{Z}$ no ambos nulos.

$mcd(a, b) = d$ si y solo si $d \mid a \wedge d \mid b$ y para todo entero $c$, si $c \mid a \wedge c \mid b$ entonces $c \mid d$.

## Demostración

Si $mcd(a, b) = d$, por definición de máximo común divisor, $d \mid a \wedge d \mid b$.

Sea $c \in \mathbb{Z}$ tal que $c \mid a \wedge c \mid b$. Por el _Teorema 5.1_, existen $x_0, y_0 \in \mathbb{Z}$ tales que $d = a \cdot x_0 + b \cdot y_0$. Por _Teorema 2.7_, $c \mid d$.

Recíproco:

Sea $d \in \mathbb{N}$ tal que $d \mid a \wedge d \mid b$ y para todo entero $c$, si $c \mid a \wedge c \mid b$ entonces $c \mid d$.

Sea $k \in \mathbb{Z}$ tal que $k \mid a \wedge k \mid b$, entonces por hipótesis, $k \mid d$. Por _Teorema 2.6_, $k \leq \lvert k \rvert \leq \lvert d \rvert = d$. Por lo tanto, $d \mid a \wedge d \mid b \wedge d \geq k$, para todo $k$ divisor de $a$ y $b$, es decir, $d = mcd(a, b)$.


# Teorema 5.4

## Enunciado

Dados dos enteros $a, b$ no ambos nulos, existen enteros $x, y$ para los que $c = a \cdot x + b \cdot y$ si y solo si $mcd(a, b) \mid c$.

## Demostración

Sean $c, x, y\ \in \mathbb{Z}$ tales que $c = a \cdot x + b \cdot y$. Dado que $mcd(a, b)$ divide a $a$ y $b$, por _Teorema 2.7_, $mcd(a, b) \mid c$.

Sea $c \in \mathbb{Z}$ tal que $mcd(a, b) \mid c$. Entonces, existe $k \in \mathbb{Z}$ tal que $mcd(a, b) \cdot k = c$. Por el _Teorema 5.1_, existen $x, y\ \in \mathbb{Z}$ tales que $(a \cdot x + b \cdot y) \cdot k = c$. Por lo tanto, $a \cdot (x \cdot k) + b \cdot (y \cdot k) = c$. Luego, existen los enteros $(x \cdot k),\ (y \cdot k)$ que cumplen la condición del teorema.


# Teorema 5.5

## Enunciado

Dados dos enteros $a, b$ no ambos nulos, si existen enteros $x, y$ para los que $mcd(a, b) = a \cdot x + b \cdot y$, entonces $mcd(x, y) = 1$.

## Demostración

Sea $mcd(a, b) = a \cdot x_0 + b \cdot y_0$.

Como $mcd(x_0, y_0) \mid x_0 \wedge mcd(x_0, y_0) \mid y_0$. Entonces existen $k_1, k_2\ \in \mathbb{Z}$ tales que $mcd(x_0, y_0) \cdot k_1 = x_0$ y $mcd(x_0, y_0) \cdot k_2 = y_0$. Por lo tanto $mcd(a, b) = a \cdot mcd(x_0, y_0) \cdot k_1 + b \cdot mcd(x_0, y_0) \cdot k_2$. Lo que implica que $mcd(x_0, y_0) \mid mcd(a, b)$. Dividiendo ambos miembros por $mcd(x_0, y_0)$ se obtiene $\frac{mcd(a, b)}{mcd(x_0, y_0)} = a \cdot k_1 + b \cdot k_2$.

Dado que $mcd(a, b)$ y $mcd(x_0, y_0)$ son enteros positivos, y que $mcd(a, b)$ es el menor entero positivo de la forma $a \cdot x + b \cdot y$, $\frac{mcd(a, b)}{mcd(x_0, y_0)}$ debe ser igual a $mcd(a, b)$, y por lo tanto $mcd(x_0, y_0) = 1$.


# Teorema 5.6

## Enunciado

Si $a \mid b \cdot c$, entonces $a \mid mcd(a, b) \cdot mcd(a, c)$.

## Demostración

Sean $a, b, c \in \mathbb{Z}$ tales que $a \mid b \cdot c$.

Usando _Teorema 5.1_, existen $x_0, x_1, y_0, y_1 \in \mathbb{Z}$ tales que $mcd(a, b) = a \cdot x_0 + b \cdot y_0$, y $mcd(a, c) = a \cdot x_1 + c \cdot y_1$.

Multiplicando miembro a miembro:
$$
\begin{aligned}
mcd(a, b) \cdot mcd(a, c) &= (a \cdot x_0 + b \cdot y_0) \cdot (a \cdot x_1 + c \cdot y_1) \\
&= a^2 \cdot x_0 \cdot x_1 + a \cdot c \cdot x_0 \cdot y_1 + a \cdot b \cdot x_1 \cdot y_0 + b \cdot c \cdot y_0 \cdot y_1
\end{aligned}
$$

Por _Teorema 2.3_, $a$ divide a los primeros tres términos de la última suma, y por hipótesis $a \mid b \cdot c$, por lo tanto también divide al último término. Luego por _Teorema 2.7_, $a \mid mcd(a, b) \cdot mcd(a, c)$.


# Teorema 5.7

## Enunciado

Sean $a, b \in \mathbb{Z}$ no ambos nulos.
$\forall\ k \in \mathbb{N}: mcd(k \cdot a, k \cdot b) = k \cdot mcd(a, b)$

## Demostración

Por definición $mcd(a, b) \mid a \wedge mcd(a, b) \mid b$. Por _Teorema 2.9_, $k \cdot mcd(a, b) \mid k \cdot a \wedge k \cdot mcd(a, b) \mid k \cdot b$.

Sea $d \in \mathbb{Z}$, tal que $d \mid k \cdot a \wedge d \mid k \cdot b$. Por _Teorema 5.1_, existen $x_0, y_0 \in \mathbb{Z}$ tales que $k \cdot mcd(a, b) = k \cdot (a \cdot x_0 + b \cdot y_0) = k \cdot a \cdot x_0 + k \cdot b \cdot y_0$. Por _Teorema 2.7_, $d \mid k \cdot mcd(a, b)$. Luego, por _Teorema 5.3_, $mcd(k \cdot a, k \cdot b) = k \cdot mcd(a, b)$.
