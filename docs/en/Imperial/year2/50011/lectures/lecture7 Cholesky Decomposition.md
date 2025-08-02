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

# Triangular matrices:
## Lower Triangular Matrices:

- $A\in\mathbb{R}^{n\times n}$ is er-triangular if $A_{ij} = 0$ for $j>i$
- Then $Ax = b$ can be easily solved by forward substitution: obtain $x_1$ first then use $x_1$ obtain $x_2$ then get $x_3$...
- like solving a set of equations manually

## Upper Triangular Matrices:

similar to Lower triangular matrices, but in the opposite way

- $A\in\mathbb{R}^{n\times n}$ is er-triangular if $A_{ij} = 0$ for $i> j$
- Then $Ax = b$ can be easily solved by forward substitution: obtain $x_1$ first then use $x_1$ obtain $x_2$ then get $x_3$...
# Idea of Cholesky Decomposition

Suppose $A\in\mathbb{R}^{n\times n}$ is a symmetric matrix ($A^T = A$) and is given by $A = LL^T$

where L is lower triangular ($L^T$ is upper triangular)

Any matrix of the form $LL^T$ is necessarily symmetric

Also $LL^T$ is positive semi-definite since for any $c\in\mathbb{R}^n$

$$x^T(LL^T)x = (L^Tx)^T(L^Tx)\ge 0$$
we can solve $Ax = LL^T x = b$ by putting $y = L^Tx$

and solving $Ly = b$ for y by forward substitution

THen we will solve $L^Tx = y$ on backward substitution

It turns out that for any positive semi-definite symmetric matrix A there is a lower triangular matrix L such that $A = LL^T$ called the Cholesky factorisation of A

# Cholesky Decomposition:

We have seen that for any lower triangular matrix $L \in\mathbb{R}^{n\times n}$ the matrix $LL^T$ is symmetric and positive semi-definite,

The above properties have a converse which says that any positive definite or positive semi-definite symmetric matrix can be decomposed as $LL^T$with a L a lower triangular matrix

There are two versions of Cholesky decomposition: one for positive definite and one for positive semi-definite

Let A $\in\mathbb{R}^{m\times m}$ i.i $A = A^T$

The matrix A is positive semi-definite iff there exists a lower triangular matrix L such that $A = LL^T$

The matrix A is positive definite iff there exists a (necessarily unique) lower triangular matrix L withpositive diagonal elements such that $A = LL^T$

# Cholesky Decomposition

Suppose $A\in\mathbb{R}^{n\times n}$ is a symmetric matrix ($A^T = A$)

We try to find lower triangular matrix $L\in\mathbb{R}^{n\times n}$ such that $A = LL^T$

We take the entries of L as unknown and see if we can determine them so that $A = LL^T$

It follows that when we apply the procedure to obtain L for a symmetric matrix there are three possibilities:

- The procedure terminates and finds a matrix L whose diagonal elements are all positive. In this case A is positive definite and L is unique
- The procedure terminates and find a matrix whose diagonal elements are not all positive. In this case A is positive semi-definte and L is not unique
- The procedure fails (as we get a complex number as an entry for L) In this case A is not positive semi-definite

## Properties of +ve(semi) definite symmetric matrices

Suppose $A\in\mathbb{R}^{n\times n}$ is a symmetric positive (semi-)definite matrix i.e $A = A^T$ and 

$$\forall x\in\mathbb{R}^n\setminus \{0\}.x^TAx > 0(x^TAx\ge 0)$$
Then we can easily show the following properties of A

- Diagonal elements are positive (non-negative): In (1), put $x_j = 1$ for $j = i$ and $x_j = 0$ for $j\neq i$ to get $A_{ii} > 0$ ($A_{ii}\ge 0$)

$\begin{bmatrix}x_1 &\dots&x_n\end{bmatrix}\begin{bmatrix}A_{11} & \dots & A_{1n}\\\vdots & \ddots &\vdots\\ A_{n1} &\dots &A_{nn}\end{bmatrix}\begin{bmatrix}x_1 \\\dots\\x_n\end{bmatrix} > 0$

so that $A_{ii}x_i^2 > 0, A_{ii} > 0$ (or $A_{ii}\ge 0$, if semi-definite)

- The largest element in absolute value is on the diagonal:

Fix $i\neq j$ between 1 and n. In (1) put $x_k = 1$ for k = i, $x_k=\pm 1$ for $k= j$ and $x_k = 0$ for $j\neq k\neq i$ to get the more general property: $|A_{ij}|<\max(A_{ii}, A_{jj})$ or if semi-definite $|A_{ij}|\le\max(A_{ii}, A_{jj})$ 

so $A'_{ij} = A_{ij}x_ix_j = \pm A_{ij}$, $A'_{ii} = A_{ii}x_i^2 = A_{ii}, A'_{jj} = A_{jj}x_j^2 = A_{jj}$

anyway we know that $x_i x_j \le \max(x_i^2,x_j^2)$

since if $x_i\le x_j$ then $x_ix_j\le x_j^2$ and vice versa

so the largest element is on the diagonal

- Leading principal minors (i.e the $1\times 1, 2\times 2, 3\times 3,\dots, m\times m$ matrices in the upper left corner) are +ve (semi-)definite: In (1) put $x_k = 0$ for $k>m$ to prove that the top left $m\times m$ matrix is +ve (semi-) definite.

so

$\begin{bmatrix}x_1 &\dots&x_n&\dots\end{bmatrix}\begin{bmatrix}A_{11} & \dots & A_{1n} &\dots\\\vdots & \ddots &\vdots &\dots\\ A_{n1} &\dots &A_{nn} &\dots\\\vdots & \vdots &\vdots &\ddots\end{bmatrix}\begin{bmatrix}x_1 \\\dots\\x_n\\\vdots\end{bmatrix} > 0$

then it reverts back to the $m\times m$ case

## Examples

- If any of the properties in the previous page does not hold for a symmetric matrix , we already know that it cannot be a positive semi-definite matrix
- Eg, the following symmetric matrices are not positive semi-definite and have no Cholesky factorisation
$A = \begin{bmatrix}1 & -1 & 1\\-1 & -1 & -1\\1 & -1 & 5\end{bmatrix}$

Here, A has a negative diagonal element

$B = \begin{bmatrix}1 & -1 & -3\\ -1 & 10 & -1\\-3 & -1& 2\end{bmatrix}$

Note: $|B_{13}| = |-3| = 3 > 2 - \max\{1,2\} = \max\{|B_{11}|, |B_{33}|\}$

the elements on the diagonal should be the largest ones

## Another Example

We have shown that if A is a positive definite matrix then for every off-diagonal element $A_{ij}$ we have:

$|A_{ij}|<\max\{A_{ii}, A_{jj}\}$

However if A is a positive definite matrix then it is not necessarily the case that $|A_{ij}|$ is less than both $A_{ii}$ and $A_{jj}$

for example consider

$A= \begin{bmatrix}1 & 2 \\ 2 &5\end{bmatrix}$

Then A is positive definite (eigenvalue 1 and 3 are both greater than 0, see lecture 5 spectral decomposition and +ve definiteness)

but $A_{11} < A_{12}$


# Example of Cholesky decomposition

$$\begin{align}A &= \begin{bmatrix}1 & -1 & 1\\-1 & 10 & -1\\ 1 & -1 & 5\end{bmatrix}\\& = LL^T=\begin{bmatrix}l_{11} & 0 & 0\\l_{21} & l_{22} & 0\\l_{31} & l_{32} & l_{33}\end{bmatrix}\begin{bmatrix}l_{11} & l_{21} & l_{31}\\0 & l_{22} & 0\\0 & 0 & l_{33}\end{bmatrix}\\&=\begin{bmatrix}
l_{11}^2 & l_{11}l_{21} & l_{11}l_{31}\\
l_{11}l_{21} & l_{21}^2 + l_{22}^2 & l_{21}l_{31} + l_{22}l_{32}\\
l_{11}l_{31} & l_{21}l_{31} + l_{22}l_{32} & l_{31}^2+l_{32}^2+l_{33}^2\\
\end{bmatrix}\end{align}$$

- Solve equations for the elements in the three rows of A taking positive square roots for the diagonal elements

$$\begin{array}{l}
i = 1 & \begin{cases}\begin{aligned}l_{11}^2 = 1 &\Rightarrow l_{11} = 1\\ l_{11}l_{21} = -1&\Rightarrow  l_{21} = -1\\l_{11}l_{31} = -1 &\Rightarrow l_{31} = 1\end{aligned}\end{cases}\\
i = 2 & \begin{cases}\begin{aligned}l_{21}^2+l_{22}^2 = 10 &\Rightarrow l_{22} = 3\\ l_{21}l_{31} +l_{22}l_{32}= -1 &\Rightarrow l_{32} = 0\end{aligned}\end{cases}\\
i = 3 & l_{31}^2 + l_{32}^2 + l_{33}^2 = 5\Rightarrow l_{33}^2 = 4\Rightarrow l_{33} = 2\\
\end{array}$$

Thus A is positive definite with a Cholesky factorisation