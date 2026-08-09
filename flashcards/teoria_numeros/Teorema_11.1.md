# Teorema 11.1


$a \cdot x \equiv b\ (mod\ n)$ tiene solución si y solo si $mcd(a, n) \mid b$.

Si tiene solución, entonces tiene $mcd(a, n)$ soluciones incongruentes módulo $n$.

**Demostración**:

Si $a \cdot x \equiv b\ (mod\ n)$, por definición de congruencia se tiene que $n \mid a \cdot x - b$. Y por definición de divisibilidad, existe un $k \in \mathbb{Z}$ tal que $a \cdot x - b = n \cdot k$. Es decir que la ecuación de congruencia tendrá solución si y solo si la ecuación $a \cdot x + (-n) \cdot k = b$ tiene solución (donde $x$ y $k$ son las incógnitas). Por _Teorema 5.4_, la ecuación tiene solución si y solo si $mcd(a, n) \mid b$.

Si la ecuación de congruencia tiene solución, sea $x_0$ una solución particular. Por lo anteriormente expuesto y por _Teorema 7.1_, cualquier otra solución será de la forma $x_0 - \frac{n}{mcd(a, n)} \cdot t$, con $t$ tomando cualquier valor de $\mathbb{Z}$.

Sean $t, t' \in \mathbb{Z}$ tales que las soluciones a la ecuación de congruencia sean congruentes módulo $n$. Entonces, $x_0 - \frac{n}{mcd(a, n)} \cdot t \equiv x_0 - \frac{n}{mcd(a, n)} \cdot t'\ (mod\ n)$. Lo que implica que $\frac{n}{mcd(a, n)} \cdot t \equiv \frac{n}{mcd(a, n)} \cdot t'\ (mod\ n)$. Luego, como $mcd(n, \frac{n}{mcd(a, n)}) = \frac{n}{mcd(a, n)}$, por _Teorema 10.21_, $t \equiv t'\ (mod\ mcd(a, n))$. Por lo tanto, si se toman valores de $t$ incongruentes módulo $mcd(a, n)$, las soluciones serán incongruentes módulo $n$.

Si se toman $t, t'$ congruentes módulo $mcd(a, n)$, sean $x_t, x_{t'}$ las soluciones asociadas a esos valores. Luego se tiene que $x_t - x_{t'} = (x_0 - \frac{n}{mcd(a, n)} \cdot t) - (x_0 - \frac{n}{mcd(a, n)} \cdot t') = \frac{n}{mcd(a, n)} \cdot (t' - t)$. Y como $mcd(a, n) \mid t' - t$, entonces $x_t - x_{t'} = \frac{n}{mcd(a, n)} \cdot k' \cdot mcd(a, n) = n \cdot k'$, para algún $k' \in \mathbb{Z}$. Por lo tanto $n \mid x_t - x_{t'}$, es decir, $x_t \equiv x_{t'}\ (mod\ n)$.

En conclusión, todas las soluciones incongruentes módulo $n$ se obtienen tomando valores incongruentes de $t$ módulo $mcd(a, n)$. Y dado que todo entero es congruente a algún valor entre $0$ y $mcd(a, n) - 1$, entonces $mcd(a, n)$ es la cantidad total de soluciones incongruentes módulo $n$.
