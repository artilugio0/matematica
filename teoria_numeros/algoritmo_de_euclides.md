# Algoritmo de Euclides
Teorema 5

## Motivación

Es un algoritmo que permite encontrar el máximo común divisor de dos números de forma eficiente.

## Enunciado
Sean $a, b \in \mathbb{Z}$, no ambos nulos. Sin pérdida de generalidad, se asume $b \neq 0$.

Si $a \mid b$, entonces $mcd(a, b) = \lvert a \rvert$. Si $b \mid a$, entonces $mcd(a, b) = \lvert b \rvert$. Para cualquier otro caso se sigue el siguiente procedimiento.

Se definen: $r_{-1} = a, r_0 = b$

Luego para cada $i \in \mathbb{N}$, usando el _Teorema 1_ con los enteros $r_{i-2}, r_{i-1}$, se encuentran $q_{i}, r_{i}$ tales que $r_{i-2} = r_{i-1}q_i + r_i$. Se repite el procedimiento incrementando $i$ hasta llegar a $i = n+1$ tal que $r_{n+1} = 0$. Entonces se tendrá: $r_{n-1} = r_n q_{n+1} + 0$, en este punto se finaliza el algoritmo.

El último resto no nulo será el máximo común divisor de $a$ y $b$: $mcd(a, b) = r_n$.

Nota: El algoritmo siempre finaliza porque el _Teorema 1_ garantiza que $0 \leq r_i < \lvert r_{i-1} \rvert$. Por lo que se tiene una sucesión estrictamente decreciente de números enteros no negativos que tendrá como máximo $\lvert b \rvert$ elementos.


## Demostración

### Estrategia

1. Demostrar que $r_n \mid a \wedge r_n \mid b$ iterando desde el último paso al primero
2. Demostrar que si $d \mid a \wedge d \mid b$ entonces $d \mid r_n$, iterando desde el primer paso hasta el último

### Paso 1: $r_n$ es divisor común

Siguiendo el algoritmo de Euclides, se tiene la sucesión de pasos:

$a = b q_1 + r_1$

$b = r_1 q_2 + r_2$

$r_{1} = r_2 q_3 + r_3$

...

$r_{n-2} = r_{n-1} q_n + r_n$

$r_{n-1} = r_n q_{n+1} + 0$

Por definición de divisibilidad, $r_n \mid r_{n-1}$. Entonces, por _Teorema 2 - Propiedad 3_, $r_n \mid r_{n-1} q_n$. Entonces, por _Teorema 2 - Propiedad 7_, $r_n \mid r_{n-2}$. Iterando de esta forma sobre todos los $r_i$ decreciendo el valor de $i$, se llega a que $r_n \mid a \wedge r_n \mid b$.


### Paso 2: $r_n$ es mayor o igual a cualquier otro divisor

Sea $d \in \mathbb{Z}$ tal que $d \mid a \wedge d \mid b$. De $a = b q_1 + r_1$ se tiene que $a + b (-q_1) = r_1$, y por _Teorema 2 - Propiedad 7_, $d \mid r_1$. Por el mismo argumento aplicado a cada $r_i$, se tiene que $d \mid r_2$, $d \mid r_3$, ..., $d \mid r_n$.

Como el procedimiento se aplica al caso en que $a \nmid b$ y $b \nmid a$, se tiene $r_1 \neq 0$, luego $n \geq 1$ y por lo tanto $r_n > 0$, es decir $\lvert r_n \rvert = r_n$.

Por _Teorema 2 - Propiedad 6_, $d \leq \lvert d \rvert \leq \lvert r_n \rvert = r_n$. Por lo tanto, $d \leq r_n$.


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

El máximo común divisor está definido cuando $a$ y $b$ no son ambos nulos, y el _Teorema 1_ requiere que $b$ no sea nulo.


## Aplicaciones

### Listado
- Expresar un entero como combinación lineal entera de otros dos
- Resolución de ecuaciones diofánticas lineales

### Expresar un entero como combinación lineal entera de otros dos

Sean $a, b, c \in \mathbb{Z}, b \neq 0$ tales que $mcd(a, b) \mid c$. Para expresar a $c$ como una combinación lineal entera de $a$ y $b$ se sigue el siguiente procedimiento:

Inicialmente se definen $\alpha_{-1} = 1,\ \beta_{-1} = 0$ y $\alpha_0 = 0,\ \beta_0 = 1$.

Siguiendo el algoritmo de Euclides:

- $a = b \cdot q_1 + r_1 \Rightarrow r_1 = a \cdot 1 + b \cdot (-q_1)$.

  Se define $\alpha_1 = 1 = \alpha_{-1} - \alpha_0 \cdot q_1$.

  Se define $\beta_1 = -q_1 = \beta_{-1} - \beta_0 \cdot q_1$.

  $\Rightarrow r_1 = a \cdot \alpha_1 + b \cdot \beta_1$

- $b = r_1 \cdot q_2 + r_2 \Rightarrow r_2 = b - r_1 \cdot q_2 \Rightarrow r_2 = a \cdot (-q_2) + b \cdot (1 + q_1 \cdot q_2)$.

  Se define $\alpha_2 = -q_2 = \alpha_0 - \alpha_1 \cdot q_2$.

  Se define $\beta_2 = 1 + q_1 \cdot q_2 = \beta_0 - \beta_1 \cdot q_2$.

  $\Rightarrow r_2 = a \cdot \alpha_2 + b \cdot \beta_2$

Siguiendo este procedimiento se llega a:

- $r_{i-2} = a \cdot \alpha_{i-2} + b \cdot \beta_{i-2}$
- $r_{i-1} = a \cdot \alpha_{i-1} + b \cdot \beta_{i-1}$

Por el Teorema 1:

- $r_{i-2} = r_{i-1} \cdot q_i + r_i$

  $\Rightarrow r_i = a \cdot (\alpha_{i-2} - \alpha_{i-1} \cdot q_i) + b \cdot (\beta_{i-2} - \beta_{i-1} \cdot q_i)$

Por lo tanto en cada paso se obtiene:

$\alpha_i = \alpha_{i-2} - \alpha_{i-1} \cdot q_i$

$\beta_i = \beta_{i-2} - \beta_{i-1} \cdot q_i$

Al continuar con el algoritmo hasta el final, se obtiene:

$r_n = a \cdot \alpha_n + b \cdot \beta_n$

Luego, como $mcd(a, b) \mid c$, existe $k \in \mathbb{Z}$ tal que $c = mcd(a,b) \cdot k = r_n \cdot k$. Por lo tanto:

$c = r_n \cdot k = a \cdot (k \cdot \alpha_n) + b \cdot (k \cdot \beta_n)$

Dejando expresado a $c$ como una combinación lineal entera de $a$ y $b$.
