# Teorema de la division entera: Demostracion: Unicidad para $a, b\ \in \mathbb{N}$

Sean $a, b\ \in \mathbb{N_0},\ b > 0$ y $q_0, r_0\ \in \mathbb{N_0}$ tales que $a = bq_0 + r_0$, con $0 \leq r_0 < b$ (su existencia ya fue demostrada).

Y sean tambien $q_1, r_1\ \in \mathbb{N_0}$ tales que $a = bq_1 + r_1$, con $0 \leq r_1 < b$.

Sin perdida de generalidad, se puede asumir $r_0 \leq r_1$, y por lo tanto, $q_1 \leq q_0$.


De $a = bq_1 + r_1$ y $a = bq_0 + r_0$, tenemos que $r_1 - r_0 = b(q_0-q_1)$. Pero $0 \leq r_1 - r_0 < b$, porque $r_0 \leq r_1 < b$. Entonces se debe dar que $q_0 - q_1 = 0$, y por lo tanto, $q_1 = q_0$. De donde sigue que $r_1 = r_0$.

Quedando asi demostrada la unicidad de $r$ y $q$.
