---
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
level: Imperial
---
# Problem 1:

**In the standard basis of $\mathbb{R}^2$, let the linear map f: $\mathbb{R}^2\to\mathbb{R}^2$ have matrix representation $A =\begin{bmatrix}4 & 2\\2 & 1\end{bmatrix}$**

**Find the eigenvalues and eigenvectors of $A$. Hence find the basis with respect to which $A$ is a diagonal matrix and find the matrix for this change of basis**

eigenvalue 0 or 5

eigenvector $[1,-2]^T$ or $[1,2]^T$

so $Q= \begin{bmatrix}1 & 1\\ -2 & 2\end{bmatrix}$

and the new basis $\begin{bmatrix}0 & 0\\0 & 5\end{bmatrix}$

# Problem 2:

**Use the normal equations given in the lecture notes to derive the formula for the following Linear Regression. Given the model $y(t) = p_1 + p_2t$**

**find expressions for the optimal parameters $p_1$ and $p_2$ in terms of data $y_i$ and $t_i$ in the following steps**

## (a)
**What are the basis functions**

$f_1(t) = p_1$

$f_2(t) = p_2t$

## (b)
**What is the matrix A**

$\begin{bmatrix}1 & t_1\\1 & t_2\\\vdots & \vdots\\1 & t_n\end{bmatrix}$

## (c)
**What is the condition on A for the normal equations to have a unique solution? What condition does this imply for $t_i$s**

the condition is $Ax = b$ has no solutions

the normal equations are $A^TAz = A^T y$

there is no line that can perfectly fit the data with zero errors
## (d)
**compute the matirx $A^TA$ (use shorthand notations like $S_{ty}$ for sums of the form $t_1y_1 + t_2y_2 + ...$ etc.)**

$\begin{bmatrix}n & \sum t_i\\\sum t_i&\sum t_i^2\end{bmatrix}$

## (e)
**Compute the deteminant of $A^TA$, and its inverse**

$n\sum t_i^2 - (\sum t_i)^2 = (n-1)\sum t_i^2 - 2 * \sum t_i*t_j = \sum(t_i-t_j)^2 > 0$

so the inverse exists

for a non-singular $2\times 2$ matrix, the inverse can b e calculated with

$\begin{bmatrix}a & b\\c & d\end{bmatrix}^{-1} =\frac{1}{ad - bc}\begin{bmatrix}d & -b\\-c & a\end{bmatrix}$

so the inverse is $\frac{1}{n\sum t_i^2 - (\sum t_i)^2}\begin{bmatrix}\sum t_i^2 & -\sum t_i\\-\sum t_i & n\end{bmatrix}$

## (f)
**compute $A^Tb$**

$$\begin{bmatrix}1 & 1 & \dots & 1\\t_1 & t_2 & \dots & t_n\end{bmatrix} * \begin{bmatrix}y_1\\y_2\\\vdots\\y_n\end{bmatrix} = \begin{bmatrix}\sum y_i\\\sum t_iy_i\end{bmatrix}$$
## (g)
**Hence find the optimal parameters**

$$z = (A^TA)^{-1}A^Tb = \frac{1}{n\sum t_i^2-(\sum t_1)^2}\begin{bmatrix}(\sum t_i^2)(\sum y_i) - (\sum t_i)(\sum t_iy_i)\\n\sum t_iy_i - (\sum t_i)(\sum y_i)\end{bmatrix}$$

## (h)
**Check that your expressions give $p_1$ and $p_2$ back given just two suitably chosen data pairs satisfying (1). Why does this test work?**

choose t = 0, 1 and substitute back to the equation in (g)

<span style="color:red">the consistency check works as for the two data points, the optimal parameters are just the ones for the line through these points, so if the points are taken from the model itself, the correct formulae are bound to reproduce the model paramters</span>

# Problem 3

**The purpose of this exercise is to show you an application of eigenvalues and eigenvectors to a topic which, at rst glance, might seem totally unrelated: the Fibonacci series. Recall (from the 1st year PPT classes) that the series is de ned by $x_0$ := 0, $x_1$ := 1 and $x_{n+1}:= x_n + x_{n-1}$ for $n\le 1$. This formula is recursive, that is, in order to find $x_n$ for higher values of n, you have to know (or compute) the values for smaller n. In many situations recursive formulae are not good enough, for instance if one wants to know how $x_n$ grows with n. In this exercise you can nd a formula for xn which is non-recursive in the sense that it gives $x_n$ as a function of the index n rather than as a function of previously computed values. Eigenvalues and-vectors are a good tool for this. Here is how to do it:**

## (a)
**Express (2) as a vector equation of the form**

$\begin{bmatrix}x_{n+1}\\ x_n\end{bmatrix} = A\begin{bmatrix}x_n\\ x_{n-1}\end{bmatrix}$

**for some $2\times 2$matrix A. This transforms the original series into a series of two-dimentsional vectors**

$A = \begin{bmatrix}1 & 1 \\ 1 & 1\end{bmatrix}$

$\color{red}A = \begin{bmatrix}1 & 1\\ 1 & 0\end{bmatrix}$

## (b)
**By recursive application of (3), express $[x_{n+1}, x_n]^T$ as a power of A times the intital vector**

$[x_{n+1}, x_n]^T = A^{n}[1,0]^T$


## (c)

**Now, find eigenvalues $\lambda_i$ and eigenvectors $u_i$ of A (here the $u_i$ need not be normalized)**

$det(A - \lambda I) = 0$

so $(1-\lambda)(-\lambda) - 1$

$\lambda^2 - \lambda - 1 = 0$

$\lambda = \frac{1 \pm \sqrt{5}}{2}$


so the eigenvetors are $[\lambda,1]^T$

## (d)

**Express the initial vector as a linear combination of the eigenvectors of A**

$\frac{1}{\sqrt{5}}(u_1 - u_2)$


## (e)
**use the results of (b)-(d) and the relation $Au_i = \lambda_i u_i$ to find the vector $[x_{n+1}, x_n]$ and hence $x_n$ itself - as a function of n alone**

$[x_{n+1}, x_n] = (A^n)(\frac{1}{\sqrt{5}}(u_1-u_2)) = \frac{A^{n+1}u_1 - A^nu_2}{\sqrt{5}} = \frac{\lambda_1^nu_1 - \lambda_2^nu_2}{\sqrt{5}}$

so $x_n = \frac{\lambda_1^n - \lambda_2^n}{\sqrt{5}}$

