# Teorema 5: Algoritmo de Euclides: Ejemplos destacables


- Uno de los enteros es nulo: $a = 0, b = 9$:

  $0 = 9 \cdot 0 + 0$

  El último $r_i$ no nulo es $r_0 = 9$, por lo tanto $mcd(0, 9) = 9$.
- Entero negativo: $a = -66, b = 18$:

  $\lvert -66 \rvert = 66 = 18 \cdot 3 + 12$

  $18 = 12 \cdot 1 + 6$

  $12 = 6 \cdot 2 + 0$

  Entonces, $mcd(-66, 18) = 6$.
