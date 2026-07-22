# Teorema 10.7


$a \equiv b\ (mod\ n)$ y $c \equiv d\ (mod\ n)$ entonces $a \cdot c \equiv b \cdot d\ (mod\ n)$.

**Demostración**:

Si $a \equiv b\ (mod\ n)$ y $c \equiv d\ (mod\ n)$, entonces $n \mid a - b$ y $n \mid c - d$. Luego, existen $k, k' \in \mathbb{Z}$ tales que $n \cdot k = a - b$ y $n \cdot k' = c - d$. Multiplicando la primera igualdad por $c$ se tiene que $n \cdot k \cdot c = a \cdot c - b \cdot c$, entonces $n \cdot k \cdot c + b \cdot c = a \cdot c$. Restando $b \cdot d$ se llega a que $n \cdot k \cdot c + b \cdot (c - d) = a \cdot c - b \cdot d$. Dado que $n$ divide a ambos términos del lado izquierdo de la igualdad, por _Teorema 2.7_, $n \mid a \cdot c - b \cdot d$. Luego, $a \cdot c \equiv b \cdot d\ (mod\ n)$.
