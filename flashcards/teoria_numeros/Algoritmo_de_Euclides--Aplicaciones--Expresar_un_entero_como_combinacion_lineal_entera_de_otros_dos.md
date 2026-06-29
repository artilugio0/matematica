# Algoritmo de Euclides: Aplicaciones: Expresar un entero como combinación lineal entera de otros dos


Sean $a, b, c \in \mathbb{Z}, b \neq 0$ tales que $mcd(a, b) \mid c$. Para expresar a $c$ como una combinación lineal entera de $a$ y $b$ se sigue el siguiente procedimiento:

Inicialmente se definen $\alpha_{-1} = 1,\ \beta_{-1} = 0$ y $\alpha_0 = 0,\ \beta_0 = 1$.

Siguiendo el algoritmo de Euclides:

- $a = b \cdot q_1 + r_1 \Rightarrow r_1 = a \cdot 1 + b \cdot (-q_1)$.

  Se define $\alpha_1 = 1 = \alpha_{-1} - \alpha_0 \cdot q_1$.

  Se define $\beta_1 = -q_1 = \beta_{-1} - \beta_0 \cdot q_1$.

  $\Rightarrow r_1 = a \cdot \alpha_1 + b \cdot \beta_1$

- $b = r_1 \cdot q_2 + r_2 \Rightarrow r_2 = b - r_1 \cdot q_2 \Rightarrow r_2 = a \cdot (-q_2) + b \cdot (1 + q_1 \cdot q_2)$.

  Se define $\alpha_2 = -q_2 = \alpha_0 - \alpha_1 \cdot q_2$.

  Se define $\beta_2 = 1 + q_1 \cdot q_2 = \beta_0 - \beta_1 \cdot q_2$.

  $\Rightarrow r_2 = a \cdot \alpha_2 + b \cdot \beta_2$

Siguiendo este procedimiento se llega a:

- $r_{i-2} = a \cdot \alpha_{i-2} + b \cdot \beta_{i-2}$
- $r_{i-1} = a \cdot \alpha_{i-1} + b \cdot \beta_{i-1}$

Por el algoritmo de división:

- $r_{i-2} = r_{i-1} \cdot q_i + r_i$

  $\Rightarrow r_i = a \cdot (\alpha_{i-2} - \alpha_{i-1} \cdot q_i) + b \cdot (\beta_{i-2} - \beta_{i-1} \cdot q_i)$

Por lo tanto en cada paso se obtiene:

$\alpha_i = \alpha_{i-2} - \alpha_{i-1} \cdot q_i$

$\beta_i = \beta_{i-2} - \beta_{i-1} \cdot q_i$

Al continuar con el algoritmo hasta el final, se obtiene:

$r_n = a \cdot \alpha_n + b \cdot \beta_n$

Luego, como $mcd(a, b) \mid c$, existe $k \in \mathbb{Z}$ tal que $c = mcd(a,b) \cdot k = r_n \cdot k$. Por lo tanto:

$c = r_n \cdot k = a \cdot (k \cdot \alpha_n) + b \cdot (k \cdot \beta_n)$

Dejando expresado a $c$ como una combinación lineal entera de $a$ y $b$.
