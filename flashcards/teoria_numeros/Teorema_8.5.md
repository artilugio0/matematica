# Teorema 8.5


Teorema fundamental de la aritmética.

Sea $a \in \mathbb{N}$ tal que $a > 1$.

$a$ es primo o puede representarse como un producto de números primos positivos de forma única, sin tener en cuenta el orden de los factores.

**Demostración**:

Sea $a \in \mathbb{N}$ tal que $a > 1$.

Si $a$ es primo, entonces el teorema se cumple.

Si $a$ no es primo, sea $p_1$ su mínimo divisor mayor a $1$. Por _Teorema 8.4_, $p_1$ es primo.

Luego, $a = p_1 \cdot a_1$, con $a_1 \in \mathbb{N}$. Si $a_1$ es primo, entonces el teorema se cumple, sino, aplicando el mismo procedimiento anterior con $a_1$, se llega a que $a = p_1 \cdot p_2 \cdot a_2$, donde $p_2, a_2 \in \mathbb{N}$ y $p_2$ es primo. Se continúa de esta forma hasta llegar a un $a_n = 1$. Esto debe suceder dado que $a_i = p_{i+1} \cdot a_{i+1}$, y por lo tanto $0 < a_{i+1} < a_i$. Como los $a_i$ forman una sucesión estrictamente descendente de números naturales, debe tener un último elemento que será $1$.

Por lo tanto queda demostrado que $a$ es primo o puede ser expresado como un producto de primos.

Para demostrar que los factores son únicos, sea $a = p_1 \cdot p_2 \cdot\ ...\ \cdot p_\alpha = q_1 \cdot q_2 \cdot\ ...\ \cdot q_\beta$, donde cada $p_i, q_j$ son primos positivos, y $\alpha \leq \beta$. También se asume que los factores están ordenados de forma que $p_1 \leq p_2 \leq ... \leq p_\alpha$ y $q_1 \leq q_2 \leq ... \leq q_\beta$.

De la definición de los productos se tiene que $p_1 \mid q_1 \cdot q_2 \cdot\ ...\ \cdot q_\beta$. Por _Teorema 8.3_, $p_1 = q_k$, para algún $k$, por lo tanto $p_1 \geq q_1$. Con el mismo razonamiento sobre $q_1$, se llega a que $q_1 \geq p_1$. Por lo tanto $p_1 = q_1$.

Luego, $p_2 \cdot p_3 \cdot\ ...\ \cdot p_\alpha = q_2 \cdot q_3 \cdot\ ...\ \cdot q_\beta$. Repitiendo este procedimiento se llega a que $p_1 = q_1,\ p_2 = q_2,\ ...\ ,\ p_\alpha = q_\alpha$.

$\alpha$ y $\beta$ deben ser iguales, sino luego de repetir el procedimiento $\alpha$ veces, se llega a que $1 =\ ...\ \cdot q_{\beta - 1} \cdot q_\beta$, lo cual es un absurdo.

Por lo tanto, todos los factores de ambos productos deben coincidir y la representación de $a$ como un producto de números primos es única.
