# Algoritmo de Euclides: Demostración: Paso 1: $r_n$ es divisor común


Siguiendo el algoritmo de Euclides, se tiene la sucesión de pasos:

$r_{-1} = r_0 q_1 + r_1$

$r_{0} = r_1 q_2 + r_2$

$r_{1} = r_2 q_3 + r_3$

...

$r_{n-2} = r_{n-1} q_n + r_n$

$r_{n-1} = r_n q_{n+1} + 0$

Por definición de divisibilidad, $r_n \mid r_{n-1}$. Entonces, por _Divisibilidad - Teorema 1 - Propiedad 3_, $r_n \mid r_{n-1} q_n$. Entonces, por _Divisibilidad - Teorema 1 - Propiedad 7_, $r_n \mid r_{n-2}$. Iterando de esta forma sobre todos los $r_i$, se llega a que $r_n \mid r_0 \wedge r_n \mid r_{-1}$.

Como $r_{-1} = \lvert a \rvert$ y $r_0 = \lvert b \rvert$, entonces $r_n \mid \pm \lvert a \rvert \wedge r_n \mid \pm \lvert b \rvert$. Por lo tanto, $r_n \mid a \wedge r_n \mid b$.
