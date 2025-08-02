---
level: Imperial
---
---
level: Imperial
---
---
level: Imperial
---
---
level: Imperial
---
---
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
level: Imperial
---
Revision: Linear algebra

# vector space

a vector space has linear structure givne by scalr multiplication and addition

$A\in\mathbb{R}^n,C\in\mathbb{R}^n$

we have a mapping $f: A\to C$, then f is linear if 

$f(av + bw) = af(v) + bf(w)$

Any basis A and C gives a unique way of representing linear f wrt the two basis

let $B_A$ and $B_C$ be basis for A and C

## example1 
then the mapping $\underset{B_A\text{ basis}}{A}\overset{f}{\to}\underset{B_C\text{ basis}}{C}$

assume $B_A = (a_1,\dots, a_n)$ (an ordered basis) $B_C = (c_1,\dots, c_n)$

then $a_j\underset{U}{\mapsto}f(a_j) =\sum_{i=1}U_{ij}c_i$

so we can have $Uc = \begin{bmatrix}u_{11} & \dots & u_{1n}\\\vdots & &\vdots\\u_{n1} & \dots & u_{nn}\\\end{bmatrix} *\begin{bmatrix}0\\0\\vdots\\1(\text{at the jth position})\\\vdots\\0\end{bmatrix} = \text{the jth column of U}$

