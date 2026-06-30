# Identidad de Bezout


## Motivación

El teorema sirve para expresar al máximo común divisor de $a$, $b$ como una combinación lineal entera de ambos números. Esto da lugar a la demostración de nuevas propiedades del máximo común divisor y nuevas aplicaciones.


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

Usando el _Algoritmo de división_, existen $q, r \in \mathbb{Z}$ tales que $a = d \cdot q + r$, con $0 \leq r < d$ (definición de $D$, $d \geq 1$).

Reemplazando a $d$ en esta última igualdad, se tiene $a = (a \cdot x_0 + b \cdot y_0) \cdot q + r$, entonces $r = a \cdot (1 - x_0 \cdot q) + b \cdot (-y_0 \cdot q)$. Como $0 \leq r < d$, $r$ debe ser $0$, de otra forma pertenecería a $D$ y sería menor a $d$, lo cual es un absurdo.

Como $r = 0$, entonces $a = d \cdot q$. Por lo tanto $d \mid a$.

Utilizando el mismo argumento, se tiene $d \mid b$. Luego $d$ es divisor común de $a$ y $b$.


### Demostrar cualquier otro divisor común es menor o igual que $min\ D$

Sea $d = min\ D = a \cdot x_0 + b \cdot y_0$, y $c \in \mathbb{Z}$ tal que $c \mid a \wedge c \mid b$.

Por _Divisibilidad - Teorema 1 - Propiedad 7_, $c \mid (a \cdot x_0 + b \cdot y_0)$. Por lo tanto $c \mid d$. Y por _Divisibilidad - Teorema 1 - Propiedad 6_, $c \leq \lvert c \rvert \leq \lvert d \rvert = d$. Luego, $c \leq d$.

Por lo tanto $d = mcd(a, b)$.


## Ejemplos simples

- $a = 42,\ b = 69$:

  $3 = 42 \cdot 5 + 69 \cdot (-3)$

- $a = 180,\ b = 144$:

  $36 = 180 \cdot 1 + 144 \cdot (-1)$


## Análisis de hipótesis: ¿por qué son necesarias las hipótesis?

Si $a = 0 \wedge b = 0$, $mcd(a, b)$ no está definido.


## Aplicaciones

- Resolución de ecuaciones diofánticas lineales
