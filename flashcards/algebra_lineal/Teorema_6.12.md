# Teorema 6.12


Sea $V$ un espacio vectorial de dimensión finita.

Todo subconjunto linealmente independiente de $V$ es finito y forma parte de una base de $V$.

**Demostración**:

Sea $dim\ V = n$.

Sea $U \subseteq V$ linealmente independiente. Por _Teorema 6.6_, $U$ es finito y no tiene más de $n$ vectores.

Si $U$ tiene $n$ vectores, entonces por _Teorema 6.9_, $U$ es una base de $V$ y por lo tanto forma parte de una base de $V$.

Si $U$ tiene $m$ vectores con $m < n$, entonces $U$ no es una base de $V$ y $\langle U \rangle \neq V$. Sea $v_1 \in V \setminus \langle U \rangle$, como $v_1 \not\in U$, por _Teorema 6.11_, $U \cup \{v_1\}$ es linealmente independiente. Si $U \cup \{v_1\}$ tiene $n$ elementos, entonces por _Teorema 6.9_, es una base de $V$ y por lo tanto $U$ es parte de una base de $V$. Si $U \cup \{v_1\}$ tiene menos de $n$ elementos, puede repetirse el procedimiento obteniendo un vector $v_2 \in V \setminus \langle U \cup \{v_1\} \rangle$, de manera que se obtiene un nuevo conjunto linealmente independiente $U \cup \{v_1, v_2\}$. Repitiendo el procedimiento $n - m$ veces, se obtiene un conjunto de vectores linealmente independientes de $n$ elementos, que por _Teorema 6.9_, será una base de $V$.

Por lo tanto $U$ es parte de una base.

## Tags

- algebra_lineal
- bases_y_dimension
