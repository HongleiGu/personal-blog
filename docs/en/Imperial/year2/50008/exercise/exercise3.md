---
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
level: Imperial
---
# 2

**Electrons hit a ciruclar plate with unti radius. Let X be the random vairbale representing the distance of a particle strike from the centre of the plate. Assuming that a particle is equally likely to strike anywhere on the plate**

## (a)
**$P(x\le r)$ and hence write down the full cumulative distribution function of $X, F_X$**

we can calculate the probability using the area of strike

$P(x\le r) = \frac{\pi * r^2}{\pi *1 ^ 2} = r^2$

so $F_X(r) = P(x\le r) =  r^2$, where r is only defined in [0,1]

therefore, the cdf of X is 

$$F(r) =\begin{cases}\begin{array}{c}
0 & r\le 0\\
r^2 & 0\lt r\lt 1\\
1 & r\ge 1
\end{array}\end{cases}$$

## (b)
**find $P(r< X\le s)$, where $0< r < s < 1$**

$P(r<X\le s) = P(X\le s) - P(X\le r) = F_X(s) - F_X(r) = s^2 - r^2$

## (c)
**would the expression of $P(r\le X\le s)$ be different? Explain**

no, geometrically a ring with radius r and no width has area 0, so $P(X = r) = 0$, however, in probability, this does not mean that the event is not possible to happen, instead, it only means the possibility of $P(X = r)$ is so low that it is negligable

## (d)
**find the probability density function for $X, f_X$**

so $f_X(r) = F_X' = \frac{dr^2}{dr} = 2r$

since in this question r can only be in [0,1]

$$f_X(r) = \begin{cases}
\begin{array}{c}
2r & 0\le r\le 1\\
0 & \text{otherwise}
\end{array}
\end{cases}$$


## (e)
**calculate the mean distance of a particle strike from the origin**

in this question, the scope of x can only be [0,1]
$E(x) = \int_{0}^1 xf_x(x) dx = \int_{0}^1 x*2x dx = \int_{0}^1 2x^2 dx = \frac{2}{3}x^3|_0^1 = \frac{2}{3}$

