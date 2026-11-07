# Teorema 6.13


Sea $V$ un espacio vectorial de dimensión finita.

Todo subespacio de $V$ tiene una base finita.

**Demostración**:

Sea $dim\ V = n$.

Sea $U$ un subespacio vectorial de $V$. Por _Teorema 6.6_, todo subconjunto linealmente independiente de $U$, por ser un subconjunto de $V$, tiene como máximo $n$ elementos. Sea $B \subseteq U$ un conjunto linealmente independiente con la máxima cantidad de elementos posible, por lo mencionado anteriormente $B$ tiene una cantidad finita de elementos.

Por _Teorema 5.4_, $\langle B \rangle$ es un subespacio vectorial de $U$, entonces $\langle B \rangle \subseteq U$.

Si $u \in U$ entonces $u \in \langle B \rangle$, sino por _Teorema 6.11_, $B \cup \{u\}$ sería linealmente independiente y sería un conjunto linealmente independiente con más elementos que $B$, lo cual es absurdo. Por lo tanto $U \subseteq \langle B \rangle$, lo que implica que $\langle B \rangle = U$, y $B$ es una base de $U$.

Por lo tanto todo subespacio de $V$ tiene una base finita.

## Tags

- algebra_lineal
- bases_y_dimension
