# Teorema 5.2


Sean $V$ un espacio vectorial, $S \subseteq V$ y $S \neq \emptyset$.

$S$ es un subespacio vectorial de $V$ si y solo si para todo $\alpha \in \mathbb{K}$ y para todos $s, t \in S$ se cumple que $\alpha \cdot s + t \in S$.

**Demostración**:

($\Rightarrow$)

Si $S$ es un subespacio vectorial de $V$, por _Teorema 4.8_, $\alpha \cdot s + t \in S$ para todo $\alpha \in \mathbb{K}$ y para todos $s, t \in S$.

($\Leftarrow$)

Si para todo $\alpha \in \mathbb{K}$ y para todos $s, t \in S$ se cumple que $\alpha \cdot s + t \in S$:

- Sea $s \in S$, $(-1) \cdot s + s = -s + s = o \in S$. Por lo tanto, $o \in S$. 
- Sean $s, t \in S$, $1 \cdot s + t \in S$. Por lo tanto, $s + t \in S$.
- Sean $s \in S$ y $\alpha \in \mathbb{K}$, $\alpha \cdot s + o \in S$. Por lo tanto, $\alpha \cdot s \in S$.

Por _Teorema 5.1_, $S$ es un subespacio vectorial de $V$.

## Tags

- algebra_lineal
- subespacios
- teorema
