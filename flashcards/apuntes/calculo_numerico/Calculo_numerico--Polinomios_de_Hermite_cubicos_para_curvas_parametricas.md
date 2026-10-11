# Cálculo numérico: Polinomios de Hermite cúbicos para curvas paramétricas


Dados los nodos $(x_0, y_0), (x_1, y_1)$. Las ecuaciones paramétricas con polinomios de Hermite que interpolan esos nodos en $t \in [0, 1]$ cumpliendo $x'(0) = \alpha_0,\ x'(1) = \alpha_1,\ y'(0) = \beta_0,\ y'(1) = \beta_1$ son:

$x(t) = [2 \cdot (x_0 - x_1) + (\alpha_0 + \alpha_1)] \cdot t^3 + [-3 \cdot (x_0 - x_1) - (2 \cdot \alpha_0 + \alpha_1)] \cdot t^2 + \alpha_0 \cdot t + x_0$

$y(t) = [2 \cdot (y_0 - y_1) + (\beta_0 + \beta_1)] \cdot t^3 + [-3 \cdot (y_0 - y_1) - (2 \cdot \beta_0 + \beta_1)] \cdot t^2 + \beta_0 \cdot t + y_0$

## Tags

- calculo_numerico
