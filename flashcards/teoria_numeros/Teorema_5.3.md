# Teorema 5.3


Sea $d \in \mathbb{N}$ y $a, b\ \in \mathbb{Z}$ no ambos nulos.

$mcd(a, b) = d$ si y solo si $d \mid a \wedge d \mid b$ y para todo entero $c$, si $c \mid a \wedge c \mid b$ entonces $c \mid d$.

**Demostración**:

Si $mcd(a, b) = d$, por definición de máximo común divisor, $d \mid a \wedge d \mid b$.

Sea $c \in \mathbb{Z}$ tal que $c \mid a \wedge c \mid b$. Por el _Teorema 5.1_, existen $x_0, y_0 \in \mathbb{Z}$ tales que $d = a \cdot x_0 + b \cdot y_0$. Por _Teorema 2.7_, $c \mid d$.

Recíproco:

Sea $d \in \mathbb{N}$ tal que $d \mid a \wedge d \mid b$ y para todo entero $c$, si $c \mid a \wedge c \mid b$ entonces $c \mid d$.

Sea $k \in \mathbb{Z}$ tal que $k \mid a \wedge k \mid b$, entonces por hipótesis, $k \mid d$. Por _Teorema 2.6_, $k \leq \lvert k \rvert \leq \lvert d \rvert = d$. Por lo tanto, $d \mid a \wedge d \mid b \wedge d \geq k$, para todo $k$ divisor de $a$ y $b$, es decir, $d = mcd(a, b)$.
