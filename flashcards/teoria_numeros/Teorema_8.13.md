# Teorema 8.13


Sean $p, k \in \mathbb{N}$, siendo $p$ un número primo y $k < p$.

$p \mid \binom{p}{k}$

**Demostración**:

Por definición se tiene que $\binom{p}{k} = \frac{p!}{(p-k)! \cdot k!} = \frac{p \cdot (p-1) \cdot (p-2) \cdot\ ...\ \cdot (p-k+2) \cdot (p-k+1)}{k!} \in \mathbb{N}$.

Dado que $k < p$, si $k = 1$ entonces la expresión anterior es un múltiplo de $p$, y por lo tanto $p \mid \binom{p}{k}$. Si $k > 1$, dado que $\binom{p}{k} \in \mathbb{N}$, entonces $k! \mid p \cdot (p-1) \cdot (p-2) \cdot\ ...\ \cdot (p-k+2) \cdot (p-k+1)$. Como $k < p$ y $p$ es primo, entonces $p \nmid k!$, luego por _Teorema 8.1_, $mcd(p, k!)$ = 1. Y por _Teorema 6.4_, $k! \mid (p-1) \cdot (p-2) \cdot\ ...\ \cdot (p-k+2) \cdot (p-k+1)$. Por lo tanto $\frac{(p-1) \cdot (p-2) \cdot\ ...\ \cdot (p-k+2) \cdot (p-k+1)}{k!} \in \mathbb{N}$. Lo que implica que $p \mid \binom{p}{k}$.
