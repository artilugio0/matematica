# Números primos

## Definición

Un número entero $p$ es primo si tiene exactamente cuatro divisores: $\pm 1$ y $\pm p$.


## Motivación

Los números primos cumplen un rol fundamental en la teoría de números. Es un concepto que aparece en el resto de los temas estudiados en adelante. Tienen propiedades que no se cumplen en general para todos los números.


# Teorema 8.1

Sean $a, p \in \mathbb{Z}$ y $p$ primo. $p \nmid a$ si y solo si $mcd(p, a) = 1$.

Demostración:

($\Rightarrow$)

Los divisores positivos de $p$ son $1$ y $\lvert p \rvert$. Por lo tanto $mcd(p, a)$ debe ser uno de esos dos números. Si $p \nmid a$, entonces $\lvert p \rvert$ no puede ser el máximo común divisor. Por lo tanto $mcd(p, a) = 1$.

($\Leftarrow$)

Si $mcd(p, a)$ = 1, entonces $p$ no puede ser un divisor de $a$, de otra forma $mcd(p, a) = \lvert p \rvert$, lo cual es un absurdo.


# Teorema 8.2

Sea $p \in \mathbb{Z}$ tal que $\lvert p \rvert > 1$. $p$ es primo si y solo si se cumple: si $p \mid a \cdot b$, entonces $p \mid a \lor p \mid b$ para todo $a, b \in \mathbb{Z}$.

Demostración:

($\Rightarrow$)

Sea $p \in \mathbb{Z}$ primo tal que $p \mid a \cdot b$. Si $p \mid a$, entonces queda demostrado. Si $p \nmid a$, entonces por _Teorema 8.1_, $mcd(p, a) = 1$. Luego, por _Teorema 6.4_, $p \mid b$.

($\Leftarrow$)

Sea $p \in \mathbb{Z}$ y $\lvert p \rvert > 1$, tal que si $p \mid a \cdot b$, entonces $p \mid a \lor p \mid b$ para todo $a, b \in \mathbb{Z}$.

Si $p$ no es primo, entonces existe $x \in \mathbb{Z}$ tal que $x \mid p \wedge x \neq \pm 1 \wedge x \neq \pm p$. Por lo tanto, $p = x \cdot k$ para algún $k \in \mathbb{Z}$. Dado que $x \neq \pm 1$, entonces $k \neq \pm p$. Luego $p \mid x \cdot k$, pero $p \nmid x \wedge p \nmid k$, lo cual es un absurdo. Por lo tanto, $p$ debe ser un número primo.


# Teorema 8.3

Sea $p \in \mathbb{Z}$ un número primo. Si $p \mid q_1 \cdot q_2 \cdot\ ...\cdot\ q_n$, donde cada $q_i$ es primo, entonces $p = \pm q_m$ con $1 \leq m \leq n$.

Demostración:

Se demuestra por inducción sobre $n$. Si $p \mid q_1$, entonces $p = \pm 1 \lor p = \pm q_1$. Pero $p$ no puede ser $\pm 1$ porque es primo. Entonces $p = \pm q_1$.

Se asume que se cumple para $n = k$, y $p \mid q_1 \cdot q_2 \cdot\ ...\cdot\ q_k \cdot q_{k+1}$, con $q_i$ primos. Si $p \mid q_1$, por el caso demostrado anteriormente, $p = \pm q_1$. Sino, por _Teorema 8.2_, $p \mid q_2 \cdot q_3 \cdot\ ...\ \cdot q_k \cdot q_{k+1}$. Luego, como $p$ divide un producto de $k$ factores, por la hipótesis inductiva $p = \pm q_m$ para $2 \leq m \leq k + 1$.

Por lo tanto queda demostrado para todo $n \in \mathbb{N}$.


# Teorema 8.4

Si $a \in \mathbb{Z}$ con $a > 1$, su mínimo divisor mayor a 1 es primo.


# Teorema 8.5

Teorema fundamental de la aritmética.

## Enunciado

Sea $a \in \mathbb{N}$ tal que $a > 1$.

$a$ es primo o puede representarse como un producto de números primos positivos de forma única, sin tener en cuenta el orden de los factores.


## Demostración

Sea $a \in \mathbb{N}$ tal que $a > 1$.

Si $a$ es primo, entonces el teorema se cumple.

Si $a$ no es primo, entonces sea $D$ el conjunto de divisores de $a$ mayores a $1$. El conjunto no está vacío, dado que $a \in D$. Por lo tanto, tiene un mínimo. Sea $p_1 = min\ D$, $p_1$ debe ser primo, porque si hubiera un divisor de $p_1$ distinto de $1$ y $p_1$, entonces por _Teorema 2.4_ también dividiría a $a$, y por lo tanto por _Teorema 2.6_ habría un divisor de $a$ mayor a $1$ y menor a $p_1$, lo cual es un absurdo.

Luego, $a = p_1 \cdot a_1$, con $a_1 \in \mathbb{N}$. Si $a_1$ es primo, entonces el teorema se cumple, sino, aplicando el mismo procedimiento anterior con $a_1$, se llega a que $a = p_1 \cdot p_2 \cdot a_2$, donde $p_2, a_2 \in \mathbb{N}$ y $p_2$ es primo. Se continúa de esta forma hasta llegar a un $a_n = 1$. Esto debe suceder dado que $a_i = p_{i+1} \cdot a_{i+1}$, y por lo tanto $0 < a_{i+1} < a_i$. Como los $a_i$ forman una sucesión estrictamente descendente de números naturales, debe tener un último elemento que será $1$.

Por lo tanto queda demostrado que $a$ es primo o puede ser expresado como un producto de primos.

Para demostrar que los factores son únicos, sea $a = p_1 \cdot p_2 \cdot\ ...\ \cdot p_\alpha = q_1 \cdot q_2 \cdot\ ...\ \cdot q_\beta$, donde cada $p_i, q_j$ son primos positivos, y $\alpha \leq \beta$. También se asume que los factores están ordenados de forma que $p_1 \leq p_2 \leq ... \leq p_\alpha$ y $q_1 \leq q_2 \leq ... \leq q_\beta$.

De la definición de los productos se tiene que $p_1 \mid q_1 \cdot q_2 \cdot\ ...\ \cdot q_\beta$. Por _Teorema 8.3_, $p_1 = q_k$, para algún $k$, por lo tanto $p_1 \geq q_1$. Con el mismo razonamiento sobre $q_1$, se llega a que $q_1 \geq p_1$. Por lo tanto $p_1 = q_1$.

Luego, $p_2 \cdot p_3 \cdot\ ...\ \cdot p_\alpha = q_2 \cdot q_3 \cdot\ ...\ \cdot q_\beta$. Repitiendo este procedimiento se llega a que $p_1 = q_1,\ p_2 = q_2,\ ...\ ,\ p_\alpha = q_\alpha$.

$\alpha$ y $\beta$ deben ser iguales, sino luego de repetir el procedimiento $\alpha$ veces, se llega a que $1 =\ ...\ \cdot q_{\beta - 1} \cdot q_\beta$, lo cual es un absurdo.

Por lo tanto, todos los factores de ambos productos deben coincidir y la representación de $a$ como un producto de números primos es única.


# Teorema 8.6

Sea $a \in \mathbb{Z}$ tal que $\lvert a \rvert > 1$. $a$ puede representarse como un producto único de la forma $\pm p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot\ ... \cdot p_k^{\alpha_k}$, donde $p_i$ es un primo positivo, $p_1 < p_2 <\ ...\ < p_k$ y $\alpha_i \in \mathbb{N}$.


A dicha representación se la llama _forma canónica_.

Demostración:

Si $a > 1$, por _Teorema 8.5_, puede expresarse de forma única como un producto de números primos. Si los factores se ordenan de menor a mayor y se agrupan los factores iguales como potencias se llega al resultado deseado.

Si $a < -1$, se aplica el mismo procedimiento con $\lvert a \rvert$, luego $a = - \lvert a \rvert = - p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot\ ... \cdot p_k^{\alpha_k}$.


# Teorema 8.7

Teorema de Euclides: existen infinitos números primos.  

Demostración:

Sea $p_1, p_2,\ ...\ ,p_n$ una lista finita de números primos.

El entero $p_1 \cdot p_2 \cdot \ ...\ \cdot p_n + 1$ es mayor a $1$ y por lo tanto, por _Teorema 8.5_, es divisible por algún número primo $p_k$. Si $p_k$ es alguno de $p_1, p_2,\ ...\ ,p_n$, entonces $p_k \mid p_1 \cdot p_2 \cdot \ ...\ \cdot p_n$, y por _Teorema 2.8_, $p_k \mid 1$ , lo que es absurdo.

Luego, $p_k$ no se encuentra en la lista inicial de números primos. Por lo tanto, ninguna lista finita de números primos puede estar completa, lo que implica que existen infinitos números primos.


# Teorema 8.8

Sea $b \in \mathbb{N}$.

$a = \pm b^n$ si y solo si en su forma canónica las potencias de cada primo divisor de $a$ son multiplos de $n$.

Demostración:

($\Rightarrow$)

Expresando a $b$ en su forma canónica, se obtiene:

$$
\begin{aligned}
a &= \pm (p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot\ ... \cdot p_k^{\alpha_k})^n \\
&= \pm p_1^{n \cdot \alpha_1} \cdot p_2^{n \cdot \alpha_2} \cdot\ ...\ \cdot p_k^{n \cdot \alpha_k}
\end{aligned}
$$

Por lo tanto, todos los divisores primos de $a$ tienen potencias múltiplos de $n$.

($\Leftarrow$)

Si $a = \pm p_1^{n \cdot \alpha_1} \cdot p_2^{n \cdot \alpha_2} \cdot\ ... \cdot p_k^{n \cdot \alpha_k}$, entonces $a = \pm (p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot\ ...\ \cdot p_k^{\alpha_k})^n = \pm b^n$.


# Teorema 8.9

Sea $a \in \mathbb{Z}$ tal que su representación canónica es $a = \pm p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot\ ... \cdot p_k^{\alpha_k}$.

$d \mid a$ si y solo si $d = \pm p_1^{\beta_1} \cdot p_2^{\beta_2} \cdot\ ... \cdot p_k^{\beta_k}$ con $0 \leq \beta_i \leq \alpha_i$.

Demostración:

($\Rightarrow$)

Para llegar a una contradicción, se asume que $d$ tiene un factor en su representación canónica que no cumple las condiciones del teorema. Esto puede ocurrir en dos formas, que tenga un $p_i^{\beta_i}$ donde $p_i$ no es un factor primo que aparezca en la representación canónica de $a$, o que $p_i = p_j$ con $1 \leq j \leq k$ y $\beta_i > \alpha_j$.

Si $p_i$ no es un factor primo de $a$, entonces por el contrarrecíproco de _Teorema 8.3_, $p_i \nmid a$. Pero dado que $p_i \mid d \wedge d \mid a$, entonces por _Teorema 2.4_, $p_i \mid a$, llegando a un absudo.

Si $p_i$ es un factor primo de $a$ pero $\beta_i > \alpha_j$, dado que $p_i^{\beta_i} \mid d \wedge d \mid a$, entonces por _Teorema 2.4_, $p_i^{\beta_i} \mid a$. Luego $a = p_i^{\beta_i} \cdot c$ para algun $c \in \mathbb{Z}$. Si se toma la representación canónica de $c$, el exponente de $p_i$ será mayor o igual a $0$, y por lo tanto el exponente de $p_i$ de $a$ será mayor o igual a $\beta_i$, y por lo tanto mayor a $\alpha_j$, llegando a un absurdo.

Por lo tanto $d = \pm p_1^{\beta_1} \cdot p_2^{\beta_2} \cdot\ ... \cdot p_k^{\beta_k}$ con $0 \leq \beta_i \leq \alpha_i$.

($\Leftarrow$)

Si $d = \pm p_1^{\beta_1} \cdot p_2^{\beta_2} \cdot\ ... \cdot p_k^{\beta_k}$ con $0 \leq \beta_i \leq \alpha_i$, entonces $a = \pm d \cdot (p_1^{\alpha_1 - \beta_1} \cdot p_2^{\alpha_2 - \beta_2} \cdot\ ...\ \cdot p_k^{\alpha_k - \beta_k})$, y por lo tanto $d \mid a$.


# Teorema 8.10

Sea $a = \pm p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot\ ... \cdot p_k^{\alpha_k}$.

$a \mid b$ si y solo si cada $p_i^{\alpha_i}$ divide a $b$.

Demostración:

($\Rightarrow$)

Si $a \mid b$, dado que cada $p_i^{\alpha_i} \mid a$, por _Teorema 2.4_, cada $p_i^{\alpha_i} \mid b$.

($\Leftarrow$)

Si cada $p_i^{\alpha_i}$ divide a $b$, dado que $mcd(p_i^{\alpha_i}, p_j^{\alpha_j}) = 1$ para $i \neq j$, por _Teorema 6.5_, $mcd(p_1^{\alpha_1}, p_2^{\alpha_2} \cdot p_3^{\alpha_3})= 1$. Por _Teorema 6.3_, $p_2^{\alpha_2} \cdot p_3^{\alpha_3} \mid b$, y por el mismo teorema entonces $p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot p_3^{\alpha_3} \mid b$. Aplicando el mismo procedimiento reiteradas veces se llega a que $p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot\ ...\ \cdot p_k^{\alpha_k} \mid b$.


# Teorema 8.11

Sea $a \in \mathbb{N}$ tal que $a = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot\ ... \cdot p_k^{\alpha_k}$.

$a$ tiene exactamente $(\alpha_1 + 1) \cdot (\alpha_2 + 1) \cdot\ ...\ \cdot (\alpha_k + 1)$ divisores positivos distintos.

Demostración:

Sea $d \in \mathbb{N}$ tal que $d \mid a$, por _Teorema 8.9_, $d = p_1^{\beta_1} \cdot p_2^{\beta_2} \cdot\ ... \cdot p_k^{\beta_k}$ con $0 \leq \beta_i \leq \alpha_i$. Dado que cada $\beta_i$ puede tomar $\alpha_i + 1$ valores enteros distintos, entonces la cantidad de posibles combinaciones para todos los $\beta_i$ será $(\alpha_1 + 1) \cdot (\alpha_2 + 1) \cdot\ ...\ \cdot (\alpha_k + 1)$. Por _Teorema 8.5_, eso determina exactamente la cantidad de valores distintos que puede tomar $d$.


# Teorema 8.12

Sean $a, b \in \mathbb{N}$.

El máximo común divisor de $a$ y $b$ es el producto de los factores primos comunes de $a$ y $b$ elevados a la menor potencia con la que aparece en las respectivas representaciones canónicas.

Demostración:

Sea $d = p_1^{\alpha_1} \cdot p_2^{\alpha_2} \cdot\ ... \cdot p_k^{\alpha_k}$ tal que cada $p_i$ es un primo que aparece en las formas canónicas de $a$ y $b$ y $\alpha_i$ la menor de las potencias que tiene $p_i$ en ambas formas canónicas.

Por _Teorema 8.9_, $d \mid a \wedge d \mid b$.

Sea $d'$ otro divisor común de $a$ y $b$, por ser divisor común y por _Teorema 8.9_, $d' = p_1^{\beta_1} \cdot p_2^{\beta_2} \cdot\ ... \cdot p_k^{\beta_k}$, con $0 \leq \beta_i \leq \alpha_i$. Nuevamente por _Teorema 8.9_, $d' \mid d$. Por lo tanto, por _Teorema 5.3_, $mcd(a, b) = d$.


# Teorema 8.13

Sean $p, k \in \mathbb{N}$, siendo $p$ un número primo y $k < p$.

$p \mid \binom{p}{k}$

Demostración:

Por definición se tiene que $\binom{p}{k} = \frac{p!}{(p-k)! \cdot k!} = \frac{p \cdot (p-1) \cdot (p-2) \cdot\ ...\ \cdot (p-k+2) \cdot (p-k+1)}{k!} \in \mathbb{N}$.

Dado que $k < p$, si $k = 1$ entonces la expresión anterior es un multiplo de $p$, y por lo tanto $p \mid \binom{p}{k}$. Si $k > 1$, dado que $\binom{p}{k} \in \mathbb{N}$, entonces $k! \mid p \cdot (p-1) \cdot (p-2) \cdot\ ...\ \cdot (p-k+2) \cdot (p-k+1)$. Como $k < p$ y $p$ es primo, entonces ningún factor de $k!$ divide a $p$, por lo que $mcd(p, k!)$ = 1. Y por _Teorema 6.4_, $k! \mid (p-1) \cdot (p-2) \cdot\ ...\ \cdot (p-k+2) \cdot (p-k+1)$. Por lo tanto $\frac{(p-1) \cdot (p-2) \cdot\ ...\ \cdot (p-k+2) \cdot (p-k+1)}{k!} \in \mathbb{N}$. Lo que implica que $p \mid \binom{p}{k}$.



# Teorema

Si $a > 1$ es compuesto si y solo si es divisible por un primo < a raiz de a


# Teorema

Dirichlet


# Teorema

T. numeros primos
