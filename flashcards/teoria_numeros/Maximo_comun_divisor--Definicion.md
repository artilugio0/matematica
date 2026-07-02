# Máximo común divisor: Definición


Sean $a, b \in \mathbb{Z}$ no ambos nulos, el máximo común divisor de $a$ y $b$ es el número $d \in \mathbb{N}$ tal que:

- $d \mid a \wedge d \mid b$
- $\forall\ c \in \mathbb{Z}: c \mid a \wedge c \mid b \Rightarrow c \leq d$

Se suele simbolizar de las siguientes formas:

- $mcd(a, b)$
- $gcd(a, b)$
- $(a : b)$

Nota: su existencia está garantizada ya que $1 \mid a \wedge 1 \mid b$, y dado que $a$ y $b$ no son ambos nulos. Por _Teorema 2.2_, la cantidad de divisores comunes es finita, y por lo tanto habrá uno que sea el máximo.
