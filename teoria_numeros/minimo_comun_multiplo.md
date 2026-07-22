# Mínimo común múltiplo

## Definición

Sean $a, b \in \mathbb{Z}$ no nulos, el mínimo común múltiplo de $a$ y $b$ es el número $m \in \mathbb{N}$ tal que:

- $a \mid m \wedge b \mid m$
- $\forall\ c \in \mathbb{N}: a \mid c \wedge b \mid c \Rightarrow m \leq c$

Se suele simbolizar de las siguientes formas:

- $mcm(a, b)$
- $lcm(a, b)$
- $[a : b]$

Nota: su existencia está garantizada ya que $\lvert a \cdot b \rvert$ es un múltiplo común, y por lo tanto el conjunto de múltiplos comunes no está vacío. Luego, por principio de buen orden de $\mathbb{N}$ debe haber un múltiplo común que sea el menor.

## Motivación

Es un concepto relacionado al máximo común divisor. Tiene propiedades similares y es útil en otras áreas de la matemática como combinatoria y estructuras algebraicas.

## Ejemplos

- $mcm(15, 10) = mcm(-15, 10) = mcm(15, -10) = mcm(-15, -10) = 30$
- $mcm(3, 9) = 9$
- $mcm(8, 21) = 168$
- $mcm(6, 6) = 6$

## Ejemplos destacables

- $mcm(\pm 1, a) = \lvert a \rvert$:
  - $mcm(1, 21) = 21$
  - $mcm(-1, 21) = 21$
  - $mcm(1, -21) = 21$
  - $mcm(-1, -21) = 21$

## Restricciones

$a$ y $b$ no pueden ser $0$, dado que $a$ y $b$ deben dividir al mínimo común múltiplo.


# Teorema 9.1

$mcm(a, a) = \lvert a \rvert$

**Demostración**:

$a \mid \lvert a \rvert$.

Sea $m \in \mathbb{N}$ tal que $a \mid m$. Por _Teorema 2.6_, $\lvert a \rvert \leq m$. Por lo tanto $mcm(a, a) = \lvert a \rvert$.


# Teorema 9.2

$mcm(a, b) \geq \lvert a \rvert$

**Demostración**:

Sea $m = mcm(a, b)$. Por definición $a \mid m$. Por _Teorema 2.6_, $\lvert a \rvert \leq \lvert m \rvert = m$. Por lo tanto $mcm(a, b) \geq \lvert a \rvert$.


# Teorema 9.3

$mcm(\pm 1, \pm a) = \lvert a \rvert$

**Demostración**:

$\pm a \mid \lvert a \rvert \wedge \pm 1 \mid \lvert a \rvert$.

Sea $m \in \mathbb{N}$ tal que $\pm a \mid m \wedge \pm 1 \mid m$.

Por _Teorema 2.6_, $\lvert a \rvert \leq m$. Por lo tanto $mcm(\pm 1, \pm a) = \lvert a \rvert$.


# Teorema 9.4

$mcm(a, b) = mcm(b, a)$

**Demostración**:

Sea $m = mcm(a, b)$, entonces $a \mid m \wedge b \mid m$ y $\forall\ c \in \mathbb{N}: a \mid c \wedge b \mid c \Rightarrow m \leq c$. Luego, $m$ cumple con la definición de $mcm(b, a)$.


# Teorema 9.5

Sea $m \in \mathbb{N}$.

$m = mcm(a, b)$ si y solo si cumple:

- $a \mid m \wedge b \mid m$
- $\forall\ c \in \mathbb{N}: a \mid c \wedge b \mid c \Rightarrow m \mid c$

**Demostración**:

($\Rightarrow$)

Sea $m = mcm(a, b)$. Por definición $a \mid m \wedge b \mid m$.

Sea $c \in \mathbb{N}$ tal que $a \mid c \wedge b \mid c$. Por _Teorema 1.1_, existen $q, r \in \mathbb{Z}$ únicos tales que $c = m \cdot q + r$ y $0 \leq r < \lvert m \rvert = m$. Por lo tanto $r = c - m \cdot q$. Si $r > 0$, dado que $c$ y $m$ son múltiplos comunes de $a$ y $b$, entonces por _Teorema 2.7_, $r$ también es un múltiplo común. Pero por definición de $r$, debe ser menor a $m$, lo que es un absurdo por ser $m$ el mínimo común múltiplo. Luego, debe ser que $r = 0$. Lo que implica que $m \mid c$.

($\Leftarrow$)

Sea $m \in \mathbb{N}$ tal que $a \mid m \wedge b \mid m$ y $\forall\ c \in \mathbb{N}: a \mid c \wedge b \mid c \Rightarrow m \mid c$.

Sea $c \in \mathbb{N}$ tal que $a \mid c \wedge b \mid c$. Por _Teorema 2.6_, $m = \lvert m \rvert \leq \lvert c \rvert = c$. Por lo tanto, $mcm(a, b) = m$.


# Teorema 9.6

$\lvert a \cdot b \rvert = mcd(a, b) \cdot mcm(a, b)$

**Demostración**:

$a \mid \lvert a \rvert \cdot \frac{\lvert b \rvert}{mcd(a, b)}$ y $b \mid \frac{\lvert a \rvert}{mcd(a, b)} \cdot \lvert b \rvert$. Por lo tanto $\frac{\lvert a \cdot b \rvert}{mcd(a, b)}$ es un múltiplo común de $a$ y $b$.

Sea $c \in \mathbb{N}$ tal que $a \mid c \wedge b \mid c$. Por _Teorema 2.4_ dado que $mcd(a,b)$ es divisor de $a$ y $b$, $mcd(a, b) \mid c$, y por lo tanto se tiene que $\frac{a}{mcd(a,b)} \mid \frac{c}{mcd(a,b)}$ y $\frac{b}{mcd(a,b)} \mid \frac{c}{mcd(a,b)}$. Por _Teorema 6.2_, $\frac{a}{mcd(a,b)}$ y $\frac{b}{mcd(a,b)}$ son coprimos, y por _Teorema 6.3_, $\frac{a}{mcd(a,b)} \cdot \frac{b}{mcd(a,b)} \mid \frac{c}{mcd(a,b)}$. Luego, por _Teorema 2.9_, $\frac{a \cdot b}{mcd(a,b)} \mid c$. Por lo tanto, $\frac{\lvert a \cdot b \rvert}{mcd(a,b)} \mid c$. Entonces, por _Teorema 9.5_, $\frac{\lvert a \cdot b \rvert}{mcd(a,b)} = mcm(a,b)$. Es decir, $\lvert a \cdot b \rvert = mcd(a,b) \cdot mcm(a,b)$.


# Teorema 9.7

$mcm(a, b) = mcm(\lvert a \rvert, \lvert b \rvert)$

**Demostración**:

Por definición, $a \mid mcm(a, b) \wedge b \mid mcm(a, b)$. Como $\lvert a \rvert \mid a$ y $\lvert b \rvert \mid b$, por _Teorema 2.4_, $\lvert a \rvert \mid mcm(a, b) \wedge \lvert b \rvert \mid mcm(a, b)$.

Sea $m \in \mathbb{N}$ un múltiplo común de $\lvert a \rvert$ y $\lvert b \rvert$. Dado que $a \mid \lvert a \rvert \wedge b \mid \lvert b \rvert$, por _Teorema 2.4_, $a \mid m \wedge b \mid m$. Luego, por _Teorema 9.5_, $mcm(a, b) \mid m$. Luego, por _Teorema 9.5_ nuevamente, $mcm(a, b) = mcm(\lvert a \rvert, \lvert b \rvert)$.


# Teorema 9.8

Sean $a, b \in \mathbb{N}$.

El mínimo común múltiplo de $a$ y $b$ es el producto de los factores primos de $a$ y $b$ elevados a la mayor potencia con la que aparecen en las respectivas representaciones canónicas.

**Demostración**:

Sea $m = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot\ ...\ \cdot p_n^{\alpha_n}$ tal que $p_i$ es un divisor primo de $a$ o de $b$, y $\alpha_i$ es la mayor potencia de $p_i$ tal que $p_i^{\alpha_i}$ divida a $a$ o $b$.

Por _Teorema 8.9_, $a \mid m \wedge b \mid m$.

Sea $m'$ un múltiplo común de $a$ y $b$. Por definición, $p_i^{\alpha_i} \mid a \lor p_i^{\alpha_i} \mid b$. Entonces, por _Teorema 2.4_, $p_i^{\alpha_i} \mid m'$. Y como $mcd(p_i^{\alpha_i}, p_j^{\alpha_j}) = 1$ para $i \neq j$, entonces por _Teorema 6.3_, $p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot\ ...\ \cdot p_n^{\alpha_n} \mid m'$. Por lo tanto $m \mid m'$. Luego, por _Teorema 9.5_, $mcm(a, b) = m$.


# Teorema 9.9

Sean $a, b \in \mathbb{Z}$, con $a \neq 0,\ b \geq 1$.

$mcm(a, b) = b$ si y solo si $a \mid b$

**Demostración**:

($\Rightarrow$)

Si $mcm(a, b) = b$, por definición $a \mid mcm(a, b)$, entonces $a \mid b$.

($\Leftarrow$)

Si $a \mid b$, entonces $b$ es un múltiplo común de $a$ y $b$. Cualquier otro múltiplo común será múltiplo de $b$. Entonces por _Teorema 9.5_, $mcm(a, b) = b$.


# Teorema 9.10

Sean $a, b \in \mathbb{Z}$ no nulos.

$mcm(a, b) = mcd(a, b)$ si y solo si $\lvert a \rvert = \lvert b \rvert$

**Demostración**:

($\Rightarrow$)

Si $mcm(a, b) = mcd(a, b)$, por definición $a \mid mcm(a, b)$. Como $mcm(a, b) = mcd(a, b)$, por definición de máximo común divisor, $mcm(a, b) \mid a$. Luego, por _Teorema 2.5_, $mcm(a, b) = \pm a$. Por el mismo razonamiento, $mcm(a, b) = \pm b$. Por lo tanto, $\lvert a \rvert = \lvert b \rvert$.

($\Leftarrow$)

Si $\lvert a \rvert = \lvert b \rvert$, entonces por _Teorema 9.7_, $mcm(a, b) = mcm(\lvert a \rvert, \lvert b \rvert) = mcm(\lvert a \rvert, \lvert a \rvert)$. Luego por _Teorema 9.1_, $mcm(a, b) = mcm(\lvert a \rvert, \lvert a \rvert) = \lvert a \rvert$.

Y por _Teorema 3.7_, $mcd(a, b) = mcd(\lvert a \rvert, \lvert b \rvert) = mcd(\lvert a \rvert, \lvert a \rvert)$. Luego por _Teorema 3.1_, $mcd(a, b) = mcd(\lvert a \rvert, \lvert a \rvert) = \lvert a \rvert$.

Por lo tanto, $mcm(a, b) = mcd(a, b)$.


# Teorema 9.11

Sean $a, b \in \mathbb{Z}$ no nulos.

$mcm(a, b) = \lvert a \cdot b \rvert$ si y solo si $mcd(a, b) = 1$

**Demostración**:

($\Rightarrow$)

Por _Teorema 9.6_, $\lvert a \cdot b \rvert = mcd(a, b) \cdot mcm(a, b)$. Por lo tanto, si $mcm(a, b) = \lvert a \cdot b \rvert$, entonces $mcm(a, b) = mcm(a, b) \cdot mcd(a, b)$. Luego $mcd(a, b) = 1$.

($\Leftarrow$)

Por _Teorema 9.6_, $\lvert a \cdot b \rvert = mcd(a, b) \cdot mcm(a, b)$. Si $mcd(a, b) = 1$, entonces $\lvert a \cdot b \rvert = mcm(a, b)$. 


# Teorema 9.12

Sean $a, b, k \in \mathbb{Z}$, con $a \neq 0,\ b \neq 0,\ k \geq 1$.

$mcm(k \cdot a, k \cdot b) = k \cdot mcm(a, b)$

**Demostración**:

Por _Teorema 9.6_, $\lvert (k \cdot a) \cdot (k \cdot b) \rvert = mcd(k \cdot a, k \cdot b) \cdot mcm(k \cdot a, k \cdot b)$. Luego, por _Teorema 5.7_, $mcd(k \cdot a, k \cdot b) = k \cdot mcd(a, b)$, por lo tanto, $k \cdot k \cdot \lvert a \cdot b \rvert = k \cdot mcd(a, b) \cdot mcm(k \cdot a, k \cdot b)$. Lo que implica que $k \cdot \frac{\lvert a \cdot b \rvert}{mcd(a, b)} = mcm(k \cdot a, k \cdot b)$. Pero por _Teorema 9.6_, $\frac{\lvert a \cdot b \rvert}{mcd(a, b)} = mcm(a, b)$. Luego, $k \cdot mcm(a, b) = mcm(k \cdot a, k \cdot b)$.


# Teorema 9.13

Si $a \mid c$ y $b \mid c$, entonces $mcm(a, b) \mid c$.

**Demostración**:

Si $a \mid c \wedge b \mid c$ y $d = mcd(a, b)$, por _Teorema 2.4_, $d \mid c$. Luego, por _Teorema 2.11_, $\frac{a}{d} \mid \frac{c}{d}$ y $\frac{b}{d} \mid \frac{c}{d}$. Y como $mcd(\frac{a}{d}, \frac{b}{d}) = 1$ (por _Teorema 6.2_), entonces por _Teorema 6.3_, $\frac{a}{d} \cdot \frac{b}{d} \mid \frac{c}{d}$. Luego, por _Teorema 2.9_, $\frac{a \cdot b}{d} \mid c$, lo que implica que $\frac{\lvert a \cdot b \rvert}{d} \mid c$. Finalmente, por _Teorema 9.6_, $\frac{\lvert a \cdot b \rvert}{d} = mcm(a, b)$, por lo tanto, $mcm(a, b) \mid c$.
