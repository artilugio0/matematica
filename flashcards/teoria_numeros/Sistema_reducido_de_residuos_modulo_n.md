# Sistema reducido de residuos módulo $n$


Un sistema reducido de residuos módulo $n$ es un conjunto cuyos elementos son coprimos con $n$ y no congruentes módulo $n$ entre sí, y para todo entero coprimo con $n$ existe un elemento en el conjunto que es congruente a él módulo $n$.

$R$ es un sistema reducido de residuos módulo $n$ si:

- $\forall\ a \in R: mcd(a, n) = 1$
- $\forall\ c \in \mathbb{Z}$ tal que $mcd(c, n) = 1: \exists\ a \in R \mid a \equiv c\ (mod\ n)$
- $\forall\ a, b \in R: a \equiv b\ (mod\ n) \Rightarrow a = b$
