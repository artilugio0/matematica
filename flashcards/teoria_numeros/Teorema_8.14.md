# Teorema 8.14


Sea $a \in \mathbb{N}$, tal que $a > 1$.

$a$ es compuesto si y solo si es divisible por un primo menor o igual a $\sqrt{a}$.

**Demostración**:

($\Rightarrow$)

Si $a$ es compuesto, entonces tiene al menos un divisor $d \in \mathbb{N}$ tal que $1 < d < a$. Si $d \leq \sqrt{a}$, dado que $d > 1$, por _Teorema 8.5_ $d$ tiene al menos un divisor $p$ primo. Luego, por _Teorema 2.4_ $p \mid a$ y por _Teorema 2.6_, dado que $p \mid d$, $p \leq \sqrt{a}$.

Si $d > \sqrt{a}$, dado que $d \mid a$, existe un $k \in \mathbb{N}$ tal que $a = d \cdot k$. Y como $d < a$, entonces $k > 1$. Si $k > \sqrt{a}$, entonces $a = d \cdot k > \sqrt{a} \cdot \sqrt{a} = a$, lo cual es absurdo. Por lo tanto $k \leq \sqrt{a}$. Luego, como $k \mid a$, por el argumento antes presentado, existe un primo $p$ tal que $p \mid a$ y $p \leq \sqrt{a}$.

($\Leftarrow$)

Si $a$ es divisible por un primo menor o igual a $\sqrt{a}$, entonces por definición $a$ no es primo. Por lo tanto $a$ es compuesto.
