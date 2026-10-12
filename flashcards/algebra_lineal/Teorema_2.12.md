# Teorema 2.12


Sea $A \in \mathbb{K}^{n \times n}$. $A$ es equivalente por filas a $I_n$ si y solo si el sistema de ecuaciones $A \cdot X = O$ solo tiene la solución trivial.

**Demostración**:

($\Rightarrow$)

Si $A$ es equivalente por filas a $I_n$, entonces por _Teorema 2.6_, $A \cdot X = O$ tiene exactamente las mismas soluciones que $I_n \cdot X = O$, que es un sistema de ecuaciones trivial donde cada incógnita toma el valor $0$, por lo tanto solo tiene la solución trivial. Luego, $A \cdot X = O$ tiene únicamente la solución trivial.

($\Leftarrow$)

Sea $A \in \mathbb{K}^{n \times n}$ tal que $A \cdot X = O$ solo tiene la solución trivial. Por _Teorema 2.8_, $A$ es equivalente por filas a una matriz escalonada reducida por filas $A'$. $A'$ no debe tener filas nulas, porque de otra forma la cantidad de filas no nulas sería menor a la cantidad de columnas, y por _Teorema 2.11_, $A' \cdot X = O$ tendría soluciones no triviales, lo que implicaría por _Teorema 2.6_ que $A \cdot X = O$ tendría soluciones no triviales.

Por lo tanto $A'$ es una matriz de $n$ filas y $n$ columnas escalonada reducida por filas sin filas nulas. Por _Teorema 2.9_, $A' = I_n$. Luego, $A$ es equivalente por filas a $I_n$.

## Tags

- algebra_lineal
- sistema_ecuaciones_lineales
