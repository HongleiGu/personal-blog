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

**Find the condition number of the following matrix using the $\ell_1$ norm and $\ell_{\infty}$ norm**

$$A = \begin{bmatrix}-4 & -5 & 6\\-4 & -3 & 4\\-5 & -5 & 7\end{bmatrix}$$

**The following are eigenvectors of A**

$$v_1 = \begin{bmatrix}1\\1\\1\end{bmatrix};v_2 = \begin{bmatrix}-1\\1\\0\end{bmatrix};v_3 = \begin{bmatrix}1\\0\\1\end{bmatrix}$$

**You can assume that the following is true for the given two matrices**

$$\begin{bmatrix}1 & -1 & 1\\1 & 1 & 0\\ 1 & 0 & 1\end{bmatrix}^{-1} = \begin{bmatrix}1 & 1 & -1\\-1 & 0 & 1\\-1 & -1 & 2\end{bmatrix}$$

following the lecture notes, $\kappa(A) = ||A||\text{ }||A^{-1}||$

we decompose A using SVD, 

the eigenvalues are -3, 1, 2

so $A = \begin{bmatrix}1 & -1 & 1\\1 & 1 & 0\\ 1 & 0 & 1\end{bmatrix}\begin{bmatrix}-3 & 0 & 0\\0 & 1 & 0\\ 0 & 0 & 2\end{bmatrix}\begin{bmatrix}1 & 1 & -1\\-1 & 0 & 1\\ -1 & -1 & 2\end{bmatrix}$

therefore $A^{-1} = \begin{bmatrix}1 & -1 & 1\\1 & 1 & 0\\ 1 & 0 & 1\end{bmatrix}\begin{bmatrix}\frac{-1}{3} & 0 & 0\\0 & 1 & 0\\ 0 & 0 & \frac{1}{2}\end{bmatrix}\begin{bmatrix}1 & 1 & -1\\-1 & 0 & 1\\ -1 & -1 & 2\end{bmatrix} = \begin{bmatrix}1 & -5 & 2\\-8 & -2 & 8\\ -5 & -5 & 8\end{bmatrix}$
so the conditional number is 51 for both cases

# Problem 2:

**Given the linear system $Ax = b$**

$$\begin{bmatrix}1 & 1\\0 & \epsilon\end{bmatrix}x =\begin{bmatrix}3\\\epsilon\end{bmatrix}$$

## (a)

**What is the solution x for $\epsilon = 1$**

$\begin{bmatrix}1 & 1\\0 & 1\end{bmatrix}\begin{bmatrix}a\\b\end{bmatrix}=\begin{bmatrix}3\\1\end{bmatrix}$

so a = 2, b = 1

## (b)

**How does this change as $\epsilon\to 0$**

$\begin{bmatrix}1 & 1\\0 & \epsilon\end{bmatrix}\begin{bmatrix}a\\b\end{bmatrix}=\begin{bmatrix}3\\\epsilon\end{bmatrix}$

so whatever $\epsilon$ is, a = 2, b = 1

a b
c d

a+c = 1
b+d = 0
ec = 0, ed = 1
## (c)

$\kappa(A) = ||A||\text{ }||A^{-1}||$

$A^{-1} = \begin{bmatrix}1 & \frac{-1}{\epsilon}\\0 & \frac{1}{\epsilon}\end{bmatrix}$


assume $0<\epsilon < 1$


using L1 norm

so $\kappa(A) = \frac{2}{\epsilon}$

it gradually become infinty, the error become huge when the input changes slightly

# Problem 3:

**Each of the following describes an algorithm implemented on a computer using standard floating point numbers and arithmetic. For each one. determine whether the algorithm is backward stable, stable but not backward stable or unstable**

# a)
**Data: $x\in\mathbb{R}$, Solution: $2x$, computed as $x\oplus x$**

$f(x) = 2x$ $\tilde{f}(x) = fl(x)\oplus fl(x)$

so $\tilde{f}(x) = x(1+\epsilon_1)\oplus x(1+\epsilon_1),|\epsilon_1|\le \epsilon_{\text{machine}}$

$\tilde{f}(x) = 2x(1+\epsilon_1)(1+\epsilon_2),|\epsilon_2|\le \epsilon_{\text{machine}}$

let $\tilde{x} = x(1+\epsilon_1)(1+\epsilon_2)$

$\frac{||\tilde{x} - x||}{x} = \frac{||x(\epsilon_1+\epsilon_2\le + \epsilon_1\epsilon_2)||}{||x||}\le 2\epsilon + \mathcal{O}(\epsilon_{\text{machine}^2})$
Therefore this algorithm is backward stable

$\frac{\tilde{x} - x}{x} = \mathcal{O}{\epsilon_{\text{machine}}};f(\tilde{x}) = \tilde{f}(x)$

## (b)
**Data $x\in\mathbb{R}$, Solution: $x^2$, computed as $x\otimes x$**

$f(x) = x^2, \tilde{f}(x) = fl(x)\otimes fl(x)$

$\tilde{f}(x) = x(1+\epsilon_1)\otimes x(1+\epsilon_1), |\epsilon_1|\le \epsilon_{\text{machine}}$

$\tilde{f}(x) = x^2(1+\epsilon_1)^2(1+\epsilon_2),|\epsilon_2|\le \epsilon_{\text{machine}}$

let $\tilde{x} = x(1+\epsilon_1)\sqrt{(1+\epsilon_2)}$

then $\frac{||\tilde{x} - x||}{||x||} = \frac{||x((1+\epsilon_1)\sqrt{1+\epsilon_2} - 1)||}{||x||}\le 2\epsilon + \mathcal{O}(\epsilon_{\text{machine}})$

## (c)
**Data none, Solution,: e, computed as $\sum_{k=0}^{\infty}\frac{1}{k!}$ from left to right using $\oplus$ and $\otimes$ and stopping when a summand is reached of magnitude $< \epsilon_{\text{machine}}$**

There is no input data, so not backward stable

and to achieve summand, we have to use $\oplus$ all the time

therefore we can show that $\frac{1}{0!}\oplus\frac{1}{1!}\oplus\dots$

or $\Big((1+\frac{1}{2})(1+\epsilon_1) + \frac{1}{6}\Big)(1+\epsilon_2)\oplus\dots$

so it is a linear combination of all epsilon and all the original sum

so stable


(d)

kind of the same



