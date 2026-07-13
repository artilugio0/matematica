# Teorema 8.2


Sea $p \in \mathbb{Z}$ tal que $\lvert p \rvert > 1$. $p$ es primo si y solo si se cumple: si $p \mid a \cdot b$, entonces $p \mid a \lor p \mid b$ para todo $a, b \in \mathbb{Z}$.

**Demostración**:

($\Rightarrow$)

Sea $p \in \mathbb{Z}$ primo tal que $p \mid a \cdot b$. Si $p \mid a$, entonces queda demostrado. Si $p \nmid a$, entonces por _Teorema 8.1_, $mcd(p, a) = 1$. Luego, por _Teorema 6.4_, $p \mid b$.

($\Leftarrow$)

Sea $p \in \mathbb{Z}$ y $\lvert p \rvert > 1$, tal que si $p \mid a \cdot b$, entonces $p \mid a \lor p \mid b$ para todo $a, b \in \mathbb{Z}$.

Si $p$ no es primo, entonces existe $x \in \mathbb{Z}$ tal que $x \mid p \wedge x \neq \pm 1 \wedge x \neq \pm p$. Por lo tanto, $p = x \cdot k$ para algún $k \in \mathbb{Z}$. Dado que $x \neq \pm 1$, entonces $k \neq \pm p$. Luego, $p \mid x \cdot k$, pero dado que $\lvert x \rvert, \lvert k \rvert < \lvert p \rvert$ (por _Teorema 2.6_ y ser distintos de $\pm p$), $p \nmid x \wedge p \nmid k$, lo cual es un absurdo por contradecir la hipótesis. Por lo tanto, $p$ debe ser un número primo.
