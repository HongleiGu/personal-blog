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
# Problem 1
**Show that, for any matrix $A\in\mathbb{R}^{m\times n}$, if $v$ is an eigenvector of $A^TA$ with eigenvalue $\lambda\neq 0$, then $Av$ is an eigenvector of $AA^T$ with the same eigenvalue of $A^TA$, then $Av_1$ and $Av_2$ are orthogonal, State and prove a similar result for eigenvectors of $AA^T$. Deduce that for any matrix $A\in\mathbb{R}^{m\times n}$, the two matrices $A^TA$ and $AA^T$ have the same set of non-zero eigenvalues**


since v and $\lambda$ are eigenvector and eigenvalue of $A^TA$

so $A^TAv = \lambda v$

then we multiply both sides with A

$AA^TAv = A\lambda v$

so $(AA^T)Av = \lambda (Av)$

therefore $Av$ is a eigenvector of $AA^T$ and the eigenvalue is still $\lambda$, this holds for any $A,A^T,v,\lambda$ therefore $AA^T$ and $A^TA$ have the same set of non-zero eigenvalues since $AA^T\neq 0$

# Problem 2:

**Show that the matrix**

$$A =\begin{bmatrix}-1 & -1 & 0\\0 & -1 & -1 \\ 0 & 0 & -1\end{bmatrix}$$

**has an eigenvalue $\lambda$ with algebraic multiplicity 3 and geometric multiplicity 1. Find vectors $v_i$ with $i = 1,2,3$, such that**

- $(A - \lambda I)v_1 = 0$
- $(A -\lambda I)v_2 = v_1$
- $(A -\lambda I)v_3 = v_2$
**What would be the basis with respect to which A will have its Jordan Normal Form**

the characteristic polynomial of A is $(-1-\lambda)^3$

therefore the algebraic multiplicity is 3 and geometric multiplicity of 1, the eigenvalue if -1 (three times)

therefore $(A-\lambda I) =\begin{bmatrix}0 & -1 & 0\\0 & 0 & -1 \\ 0 & 0 & 0\end{bmatrix}$

so we can find 

$v_1 = [1,0,0]^T$

$v_2 = [0,-1,0]^T$

$v_3 = [0,0,1]^T$

therefore, the basis is $\begin{bmatrix}1 & 0 & 0\\0 & -1 & 0\\0 & 0 & 1\end{bmatrix}$
the transformed matrix is $\begin{bmatrix}-1 & 1 & 0\\ 0 & -1 & 1\\ 0 & 0 & -1\end{bmatrix}$


# Problem 3:

## (a) 
**Find the Cholesky factorization of the matrix**

**$A = \begin{bmatrix}1 & 1 & 1\\1 & 5 & -5\\-1 &-5 & 6\end{bmatrix}$**

the eigenvalues are 1, so it is positive definite

assume $L = \begin{bmatrix}l_{11} & 0 & 0\\l_{21} & l_{22} & 0\\l_{31} & l_{32} & l_{33}\end{bmatrix}$ $L^T = \begin{bmatrix}l_{11} & l_{21} & l_{31}\\0 & l_{22} & l_{32}\\0 & 0 & l_{33}\end{bmatrix}$


$$A = LL^T = \begin{bmatrix}l_{11}^2 & l_{11}l_{21} & l_{11}l_{31}\\l_{21}l_{11} & l_{21}^2 + l_{22}^2 & l_{21}l_{31} + l_{22}l_{32}\\l_{31}l_{11} & l_{31}l_{21} + l_{22}l_{32} &l_{31}^2 + l_{32}^2 + l_{33}^2\end{bmatrix}$$

$L = \begin{bmatrix}1 & 0 & 0\\1 & 2 & 0\\-1 & -2 & 1 \end{bmatrix}$


## (b)

**Then solve $Ax =b$ for $b =[1,-3,6]^T$ by forward and backward substitution, using the triangular shape of the factorisation matrices**

let $y = L^Tx$

then $Ax = LL^Tx = Ly = b$

we can solve this easily since L is triangular

then similarly solve for x
