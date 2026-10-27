# Teorema 5.5


Sea $V$ un espacio vectorial y $G \subseteq V$.

$\langle G \rangle$ es la intersección de todos los subespacios de $V$ que contienen a $G$.

**Demostración**:

Sea $W$ la intersección de todos los subespacios de $V$ que contienen a $G$.

Sea $g \in \langle G \rangle$, entonces $g$ es una combinación lineal de los vectores de $G$. Como $G$ está incluido en todos los subespacios en la intersección que define a $W$, por _Teorema 4.8_, $g$ pertenece a cada uno de esos subespacios. Entonces $g \in W$, y por lo tanto, $\langle G \rangle \subseteq W$.


Como $G \subseteq V$, por _Teorema 5.4_, $\langle G \rangle$ es un subespacio de $V$. Entonces, $\langle G \rangle$ es uno de los subespacios de $V$ en la intersección que define a $W$. Si $w \in W$, entonces $w \in \langle G \rangle$. Por lo tanto, $W \subseteq \langle G \rangle$.

De donde se concluye que $\langle G \rangle = W$.

## Tags

- algebra_lineal
- subespacios
- teorema
