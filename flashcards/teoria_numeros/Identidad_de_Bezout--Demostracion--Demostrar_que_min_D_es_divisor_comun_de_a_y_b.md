# Identidad de Bezout: Demostración: Demostrar que $min\ D$ es divisor común de $a$ y $b$


Sea $d = min\ D$. Por pertenecer a $D$, existen $x_0,\ y_0 \in \mathbb{Z}$ tales que $d = a \cdot x_0 + b \cdot y_0$.

Usando el _Teorema 1_, existen $q, r \in \mathbb{Z}$ tales que $a = d \cdot q + r$, con $0 \leq r < d$ (definición de $D$, $d \geq 1$).

Reemplazando a $d$ en esta última igualdad, se tiene $a = (a \cdot x_0 + b \cdot y_0) \cdot q + r$, entonces $r = a \cdot (1 - x_0 \cdot q) + b \cdot (-y_0 \cdot q)$. Como $0 \leq r < d$, $r$ debe ser $0$, de otra forma pertenecería a $D$ y sería menor a $d$, lo cual es un absurdo.

Como $r = 0$, entonces $a = d \cdot q$. Por lo tanto $d \mid a$.

Utilizando el mismo argumento, se tiene $d \mid b$. Luego $d$ es divisor común de $a$ y $b$.
