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
# Properties of symmetric matrix:

a matrix is symmetric if $A^T = A$

- All eigenvelues of a real symmetric matrix are real
- eigenvectors for distinct eigenvalues are othorgonal
The algebraic and geometric multiplcity of any eigenvalue are the same (Tutorial sheet 3, will come back later)

In order to show (i) and (ii)

we need to consider complex matrix $A\in\mathbb{C}^{n\times n}$

we write the conjugate of A to be $A^*$ where $(A_{ij})^* = (A^*_{ij})$

then $(Au)^* = A^* u^*$and $(A^*)^T = (A^T)^*$ this is easy to prove

## eigenvalues of symmetric real matrix are real:
in order ot prove $\lambda\in\mathbb{R}$, we first assume $\lambda\in\mathbb{C}$ then try to prove that $\lambda^* = \lambda$, then the imaginary part of $\lambda$ can only be zero, yielding $\lambda\in\mathbb{R}$

assumption $A\in\mathbb{R}^{n\times n}, \lambda\in\mathbb{C}, u\in\mathbb{C}^n$

for eigenvector u and eigenvalue $\lambda$

we have $Au = \lambda u$

taking the conjugate of both side gives

$(Au)^* = A^*u^* =\lambda^* u^*$

since $A\in\mathbb{R}^{n\times n}$, $A^* =A$

so $Au* = \lambda^*u^*$

we pre-multiply $Au = \lambda u$ with $(u^*)^T$

$$\begin{aligned}
\lambda (u^*)^Tu &= (u^*)^T(Au)\\
&= ((u^*)^T A)u\\
&= (A^T u^*)^T u & (Bv)^T = v^TB^T\\
&= (Au^*)^Tu & (A^T = A)\\
&= (\lambda^* u^*)^T u\\
&= \lambda^* (u^*)^Tu\\
& = \lambda^* (u^*)^Tu
\end{aligned}$$

therefore, since $(u^*)^Tu$ is not zero(as u being an eigen vector)

so $\lambda =\lambda^*$, so $\lambda\in\mathbb{R}$, and one step further $u\in\mathbb{R}^n$

## Eigenvectors of distinct eigenvalues of a symmetric matrix are orthogonal

so we take $A$ to be a real symmetric matrix, and two sets of eigen value/vectors

$Au_1 = \lambda_1 u_1$ and $Au_2 = \lambda_2 u_2$ with $u_1, u_2$ non-zero

we want to get $u_1^Tu_2$

so obviously we try to get $u_2^TAu_1$

by pre-multiplying the first equation, we get

$\lambda_1u_2^Tu_1 = u_2^T(Au_1) = (u_2^TA)u_1 = (A^Tu_2)^Tu_1 = (Au_2)^T u_1 = \lambda_2u_2^Tu_1$

again $\lambda_1 = \lambda_2$ since $u_2^Tu_1$ is non-zero

If the eigenvalue $\lambda$ has multiplicity m then we can find a set of m orthonormal eigenvectors for $\lambda$ (Tut3, TBC)

# spectral decomposition:

by the above proof, $A\in\mathbb{n\times n}$ is symmetric, then it has an orthonormal set of eigenvectors $u_1,\dots, u_n$ corresponding to (not necessarily distinct) eigenvalues $\lambda_1,\dots, \lambda_n$

The spectral decomposition $QA^TQ = S$ where $Q = [u_1, u_2, \dots, u_n]$ is an orthonormal matrix, or $Q^{-1} = Q^T$ (when $Q^TQ = I$, then all the columns are unit sized and orthonormal to each other)

and $S = diag(\lambda_1, \lambda_2,\dots, \lambda_n)$

then the matrix $C := Q^{-1}\in\mathbb{R}^{n\times n}$ is the matrix for the change of basis into another basis where f is represented by B


![pic1](../../../../../assets/Imperial/50011/lecture4-pic1.png)

## Example:

Consider the matrix $A = \begin{bmatrix}1 & 2\\2 & 1\end{bmatrix}$
ERO gives $A' = \begin{bmatrix}1 & 2\\0 & -3\end{bmatrix}$

so eigen value -1 and 3

then eigen vector $\frac{1}{\sqrt{2}}(1,-1)^T$ and $\frac{1}{\sqrt{2}}(1,1)^T$

so $Q = [u_1, u_2] = \frac{1}{\sqrt{2}}\begin{bmatrix}1 & 1\\-1 & 1\end{bmatrix}$

And $S = Q^TAQ = diag(-1,3)$