# Teorema 6.10


Sean $m, n \in \mathbb{N}$.

$mcd(a, b) = 1$ si y solo si $mcd(a^m, b^n) = 1$.

Demostración:

($\Rightarrow$)

Paso 1: Primero se demuestra que $mcd(a, b) = 1 \Rightarrow mcd(a, b^n) = 1$ por inducción sobre $n$.

Si $mcd(a, b) = 1$, entonces la proposición es verdadera para $n = 1$. Se asume cierta para $n = k$. Si $mcd(a, b) = 1$, entonces $mcd(a, b^k) = 1$. Por _Teorema 6.5_, como $mcd(a, b) = 1 \wedge mcd(a, b^k) = 1$, entonces $mcd(a, b^k \cdot b) = mcd(a, b^{k+1}) = 1$. Por lo tanto, se cumple para todo $n \in \mathbb{N}$.

Paso 2: Se demuestra que $mcd(a, b) = 1 \Rightarrow mcd(a^m, b^n) = 1$ por inducción sobre $m$.

Si $mcd(a, b) = 1$, por lo demostrado en _Paso 1_, $mcd(a, b^n) = 1$. Entonces la proposición es verdadera para $m = 1$.

Se asume cierta para $m = k$. Si $mcd(a, b) = 1$, entonces $mcd(a^k, b^n) = 1$.

Por lo demostrado en _Paso 1_, si $mcd(a, b) = 1$, entonces $mcd(a, b^n) = 1$. Luego, $mcd(a, b^n) = 1 \wedge mcd(a^k, b^n) = 1$. Entonces por _Teorema 6.5_, $mcd(a^k \cdot a, b^n) = mcd(a^{k+1}, b^n) = 1$. Por lo tanto, se cumple para todo $m \in \mathbb{N}$.

De esta forma queda demostrado para todo $m, n \in \mathbb{N}$

($\Leftarrow$)

Si $mcd(a^m, b^n) = 1$:

Si $a = 0$, entonces por _Teorema 3.2_, $mcd(a^m, b^n) = mcd(0, b^n) = \lvert b^n \rvert = 1$. Por lo tanto $b = \pm 1$, y por _Teorema 3.3_, $mcd(0, \pm 1) = mcd(a, b) = 1$.

Si $a \neq 0$, como $a \mid a^m$, por _Teorema 6.6_ $mcd(a, b^n) = 1$. Y dado que $b \mid b^n$, por el mismo teorema, $mcd(a, b) = 1$.
