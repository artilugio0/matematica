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
