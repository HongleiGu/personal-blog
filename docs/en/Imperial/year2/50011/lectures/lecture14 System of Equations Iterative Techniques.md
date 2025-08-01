---
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
level: Imperial
---

Matrix problems can be up to a million data points

# Iterative methods overview:

Iterative methods can give approximate solution much faster.

Some take advantage of structure (large problems often involve sparse A matrices)

Key idea: start from initial guess and successively improve it

We want to write the system of Ax = b in to form of

$$x^{(k+1)} = Bx^{(k)}+d,k = 0,1,2,\dots$$

B and d are chosen so that a fixed poitn of (1) is a solution to $Ax = b$ (recall Banach fixed point theorem from Part 1)

Method is stationary is B and d are constants

We need to know how to get B and d from A and b, and also How $x^{(0)}$ should be chosen

Stopping criterion usually defined by relative residual:

$$\frac{||b-Ax^{(k)}||}{||b||}\le \epsilon$$
# Classical iterative methods:

- Jacobi iteration (easy to parallelise)

$$x_i^{(k+1)} = \frac{1}{a_{i,i}}\Big(b_i = \sum_{j=1,i\neq j}^na_{i,j}x_j^{(k)}\Big)$$

- Gauss-Seidel iteration (lower storage requirements)
$$x_i^{(k+1)} = \frac{1}{a_{i,i}}\Big(b_i - \sum_{j=1}^{i-1}a_{i,j}x_j^{(k+1)}-\sum_{j=i+1}^n a_{i,j}x_j^{(k)}\Big)$$
- Successive overrelaxation (SOR) iteration:
$$x_i^{k+1} = \frac{\omega}{a_{i,i}}\Big(b_i-\sum_{j=1}^{i-1}a_{i,j}x_j^{k+1}-\sum_{j=i+1}^na_{i,j}x_j^{(k)}\Big) + (1-\omega)x_i^{(k)}$$

# Matrix form of classical iterative methods

These schemes split matrix A into A = G + R

Assuming we define this split so G is non-singular:

or

$$\begin{aligned}
Ax = b &\iff (G+R)x = b\\\
&\iff x = G^{-1}b - G^{-1}Rx\\
&\iff x = Bx + d
\end{aligned}$$

Jacobi iteration: $G= D,R= L + U$

Gauss-Seidel iteration: $G = D + L, R = U$

SOR iteration: $G = (\omega^{-1}D + L), R = ((1-\omega^{-1})D + U)$

where

$$D = \begin{bmatrix}q_{1,1} & \cdots & 0\\\vdots & \ddots & \vdots\\0 &\cdots & a_{n,n}\end{bmatrix};L = \begin{bmatrix}0 & 0 & \cdots & 0\\a_{2,1} & 0 & \cdots & 0\\\vdots & & \ddots & \vdots\\a_{n,1} &\cdots & a_{n,n-1} & 0\end{bmatrix};U = \begin{bmatrix}0 & a_{1,2} & \cdots & a_{1,n}\\\vdots & & \ddots & \vdots\\0 & \cdots & 0 & a_{n-1,n}\\0 & 0 & \cdots & 0\end{bmatrix}$$

# Convergence of sequence $x^{(k+1)} = Bx^{(k)} + d$

we can define $f: \mathbb{R}^m\to\mathbb{R}^m$ as $f(x) = Bx + d$

Theorem: Let $B\in\mathbb{R}^{m\times m},d\in\mathbb{R}^m$, and $||\bullet||$ be a consistent norm on $\mathbb{R}^{m\times m}$ If $||B||<1$, then sequence ${x^{(k)}}_{k=0}^{\infty}$ converges for any starting point $x^{(0)}$

Proof: We have a complete metric space $(\mathbb{R}^m,||\bullet||)$

$$\begin{aligned}
||f(x) - f(y)|| &= ||Bx + d - (By + d)||\\
&= ||B(x-y)||\\
&= ||B||\text{ }||x-y||
\end{aligned}$$

therefore f is continuous and a contraction with contracting factor $||B||<1$ The Bananch fixed point theorem tells us it has a unique fixed point $x_*$

# Design choices: iterative scheme for $Ax + b$

In summary, we want to split matrix $A = G + R$ such that
- $||B|| = ||G^{-1}R||$ is small $(||B|| < 1)$
- $B = -G^{-1}R$ and $d = G^{-1}b$ are easy to compute
- Preprocessing: permute A or change of basis
With this in mind, the classical schemes:
- Jacobi iteration: $G= D,R= L + U$
- Gauss-Seidel iteration: $G = D + L, R = U$
- SOR iteration: $G = (\omega^{-1}D + L), R = ((1-\omega^{-1})D + U)$
If A is strictly row-diagonally dominant, then Jacobi and Gauss-Seidel iterations converge (proof is non-examinable)

$$|a_{i,i}|>\sum_{j=1;i\neq j}^m|a_{i,j}|, i = 1,\dots, m$$

If A is symmetric positive definite, then Gauss-Seidel and SOR iterations $(\omega\in(0,1))$ converge