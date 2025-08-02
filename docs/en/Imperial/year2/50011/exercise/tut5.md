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
# Problem 1:
**Let**

$$A = \begin{bmatrix}
1 & 1 & 0 & 1\\
1 & 0 & 0 & 1\\
1 & 1 & 1 & 1\\
1 & 0 & 1 & 0
\end{bmatrix}$$

**Perform QR decomposition on matrix A = QR**


following Gram Schmidt algorithm

$a_1 = [1,1,1,1]^T$
$e_1 = u_1 = \frac{1}{2}a_1$

$a_2 = [1,0,1,0]^T$
$u_2 = a_2 - (e_1a_2)e_1 = \frac{1}{2}[1,-1,1,-1]$
$e_2 = \frac{1}{1}u_2 = e_2 (||u_2|| = 1)$

$a_3 = [0,0,1,1]^T$
$u_3 = a_3 - (e_1a_3)e_1 - (e_2a_3)e_2 = \frac{1}{2}[-1,-1,1,1]$
$e_3 = \frac{1}{1}u_3 = u_3 (||u_3|| = 1)$

$a_4 = [1,1,1,0]^T$
$u_4 = a_4 - (e_1a_4)e_1 - (e_2a_4)e_2 - (e_3a_4)e_3 = \frac{1}{4}[-1,1,1,-1]^T$
$e_4 = \frac{1}{\frac{1}{2}}u_4 = 2u_4 = \frac{1}{2}[-1,1,1,-1]^T(||u_4|| = \frac{1}{2})$

# Problem 2:

**Consider the Householder operator $H_u = I - 2uu^T$ where $I\in \mathbb{R}^{m\times m}$ is the identity matrix and $u\in\mathbb{R}^m$ is a unit vector. Show that $H_u$ is a reflection through the plane $P_u = \{x\in\mathbb{R}^m:u\bullet x = 0\}$ with $H_u = H_u^T = H_u^{-1}$ and find a complete set of eigenvalues and eigenvectors of $H_u$**


so consider a vector x

then $H_ux = x - 2uu^Tx = x - 2u^Txu = 2(u\bullet x)u$

where $uu^Tx$ is the projection of x onto $\perp u$

so $H_ux$ is the reflection of x through the plane

and since u is a unit vector, so $||u|| = 1$ and $uu^T$ is symmetric 

$H_u^T = (I - uu^T)^T = I^T - (uu^T)^T = I - uu^T = H_u$

$H_uH_ux = H_u(x-2uu^Tx) = x - 2uu^Tx - 2uu^Tx + 4uu^Tuu^Tx = x- 4uu^T + 4uu^T = x$ since $u^Tu = 1$

and since $H_uu = -u$ so u is an eigenvalue of $H_u$ with eigenvalue -1, 

and 1 for any vector in P, since vectors are inverted by H, there is no other way that $Hx = x$

# Problem 3:



## (i) 

**Show that for a matrix $A\in\mathbb{R}^{m\times n}$ with n independent columns we can obtain $2^n$ number of QR-decomposition using GS**

so we obtaining $e_n$ using $u_n = a_n - \sum_{i=0}^{n-1}(e_i\bullet a_n)e_i$ then normalise

we can randomly apply a optional -1 before $e_n$

(note we cannot apply any coefficient as this needs to be orthonormal)

since $e_n$ and $-e_n$ are are perpendicular to the other vectors,

which gives $2^n$

## (ii)

Show that using GS, there is only one way of obtaining a QR decomposition $A = QR$ for which the diagonal elements of R are positive:

the only way is to not introduce the -1, or to make $e_n$ all positive






