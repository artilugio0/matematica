# Teorema 2.3


Para toda operación elemental de fila existe una operación elemental de fila del mismo tipo tal que si se aplica una seguida de la otra se obtiene la matriz original.

Se dice que esa operación es una operación inversa de la original.

**Demostración**:

Sea $A \in \mathbb{K}^{m \times n}$.

Para $ero1_{k,l}$, una operación inversa es $ero1_{l,k}$ dado que $\left( ero1_{k,l}(ero1_{l,k}(A)) \right)_{ij} = A_{ij}$ y $\left( ero1_{l,k}(ero1_{k,l}(A)) \right)_{ij} = A_{ij}$.

Para $ero2_{k,c}$ con $c \neq 0$, una operación inversa es $ero2_{k,c^{-1}}$ dado que $\left( ero2_{k,c}(ero2_{k,c^{-1}}(A)) \right)_{ij} = A_{ij}$ y $\left( ero2_{k,c^{-1}}(ero2_{k,c}(A)) \right)_{ij} = A_{ij}$.

Para $ero3_{k,l,c}$, una operación inversa es $ero3_{k,l,-c}$ dado que $\left( ero3_{k,l,c}(ero3_{k,l,-c}(A)) \right)_{ij} = A_{ij}$ y $\left( ero3_{k,l,-c}(ero3_{k,l,c}(A)) \right)_{ij} = A_{ij}$.

## Tags

- algebra_lineal
- sistema_ecuaciones_lineales
