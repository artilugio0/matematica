# Divisibilidad 2


## Bezout
- d > 0: mcd(a,b) = d si solo si d divide a, b y para todo divisor de a, b, tambien es divisor de d

  si d = mcd(a,b) ==> d = ax+by. Si c divide a a, b ==> c | ax+by ==> c | d

  si d divide a, b, y todo divisor de a, b divide a d ==> c | d ==> c <= |c| < |d| = d

- los enteros ax + by son multiplos de mcd(a, b)

(a) There exist integers x and y for which c =ax+by if and only if gcd(a, b) I c.
(b) If there exist integers x and y for which ax+by= gcd(a, b), then gcd(x, y)= 1.

Si $a \mid b \cdot c$, entonces $a \mid mcd(a, b) \cdot mcd(a, c)$


## Coprimos
- definicion de coprimo
- coprimo sii ax + by = 1
- mcd(a,b) = d, entonces mcd(a/d, b/d) = 1
- a|c, b|c, mcd(a, b) = 1, entonces ab | c
- a|bc y mcd(a,b) = 1, entonces a|c

(a) If gcd(a, b)= 1, and gcd(a, c)= 1, then gcd(a, be)= 1.
1 =(ax+by)(au +cv) =a(aux+cvx+byu) +bc(yv).]
(b) If gcd(a, b)= 1, and c I a, then gcd(b, c)= 1.
(c) If gcd(a, b)= 1, then gcd( ac, b) = gcd(c, b).
(d) If gcd(a, b)= 1, and c I a+b, then gcd(a, c)= gcd(b, c) = 1.
(e) If gcd(a, b)= 1, d I ac, and d I be, then d I c.
(f ) If gcd(a, b)= 1, then gcd( a2, b2)= 1.
a, b coprimos => a^m b^n coprimos
a^m | b^m sii a | b
gcd(a, a+ 1) = 1.
