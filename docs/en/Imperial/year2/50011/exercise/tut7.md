---
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
level: Imperial
---
# problem 1:

**In Gaussian elimination we apply matrices of the form to A via lefthand-side multiplication**

$$L_k = \begin{bmatrix}1 & & & & &\\ & \ddots & & & &\\
& & 1 & & \\
& & -\ell_{k+1,k} & 1 & & \\
& & \vdots & &\ddots & \\
& & -\ell_{m,k} & & & 1\end{bmatrix}L^{-1}_k =\begin{bmatrix}1 & & & & &\\ & \ddots & & & &\\
& & 1 & & \\
& & \ell_{k+1,k} & 1 & & \\
& & \vdots & &\ddots & \\
& & \ell_{m,k} & & & 1\end{bmatrix}$$

## (a)

**show that $L_k^{-1}$ is the inverse of $L_k$**

$$\begin{aligned}L_kL_k^{-1} &= \begin{bmatrix}1 & & & & &\\ & \ddots & & & &\\
& & 1 & & \\
& & -\ell_{k+1,k} & 1 & & \\
& & \vdots & &\ddots & \\
& & -\ell_{m,k} & & & 1\end{bmatrix}\begin{bmatrix}1 & & & & &\\ & \ddots & & & &\\
& & 1 & & \\
& & \ell_{k+1,k} & 1 & & \\
& & \vdots & &\ddots & \\
& & \ell_{m,k} & & & 1\end{bmatrix}\\
&= \begin{bmatrix}1 & & & & &\\ & \ddots & & & &\\
& & 1 & & \\
& &  & 1 & & \\
& &  & &\ddots & \\
& & & & & 1\end{bmatrix} = I\end{aligned}$$

therefore $L_k$ is the inverse of $L_k^{-1}$


<span style="color: red">from modal answer: (basically the same but a better proof formating)</span> 

If we denote the off-diagonal elements of $L_k$ as $\ell_k$ and use $e_k$ as the usual column vector with 1 in position k and 0 elsewhere

then 

$$\ell_k = \begin{bmatrix}0\\\vdots\\0\\\ell_{k+1,k}\\\vdots\\\ell_{m,k}\end{bmatrix};e_k = \begin{bmatrix}0\\\vdots\\1\\\vdots\\0\end{bmatrix}$$

then we can rewrite $L_k = I - \bar{\ell_k}e_k^T$ and $L_k^{-1} = I + \bar{\ell_k}e_k^T$. We want to show these are inverses, or they multiply to be $I$

$$\begin{aligned}(I - \bar{\ell_k}e_k^T)(I + \bar{\ell_k}e_k^T) &= I\\
I - \bar{\ell_k}e_k^T\bar{\ell_k}e_k^T &= I\\
I - \bar{\ell_k}(0)\ell_k^T &= I\\
I &= I
\end{aligned}$$

Note that because $\ell_k$ has 0 at position k, the inner product $e_k^T\bar{\ell_k} = 0$

## (b)

Show that $L_1^{-1}L_2^{-1}\dots L_{m-1}^{-1}$ is equal to 

$$L = \begin{bmatrix}1\\\ell_{2,1} & 1\\\ell_{3,1} & \ell_{3,2} & 1\\\vdots &\vdots &\ddots &\ddots &\\
\ell_{m,1} & \ell_{m,2} & \dots &\ell_{m,m-1} & 1\end{bmatrix}$$

consider $AL_1^{-1}$

$$\begin{aligned}
AL_1 &= A\begin{bmatrix}1 & & & & &\\ & \ddots & & & &\\
& & 1 & & \\
& & \ell_{k+1,k} & 1 & & \\
& & \vdots & &\ddots & \\
& & \ell_{m,k} & & & 1\end{bmatrix}\\
&= A(I + \begin{bmatrix}0 & & & & &\\ & \ddots & & & &\\
& & 0 & & \\
& & \ell_{k+1,k} & 0 & & \\
& & \vdots & &\ddots & \\
& & \ell_{m,k} & & & 0\end{bmatrix})\\
&= A + A\begin{bmatrix}0 & & & & &\\ & \ddots & & & &\\
& & 0 & & \\
& & \ell_{k+1,k} & 0 & & \\
& & \vdots & &\ddots & \\
& & \ell_{m,k} & & & 0\end{bmatrix}\\
&= A + \begin{bmatrix}0 & & & & &\\ & \ddots & & & &\\
& & 0 & & \\
& & a_{k+1,k}\ell_{k+1,k} & 0 & & \\
& & \vdots & &\ddots & \\
& & a_{m,k}\ell_{m,k} & & & 0\end{bmatrix}
\end{aligned}$$

so we can generalise to $L_1^{-1}L_2^{-1}\dots L_{m-1}^{-1}$

<span style="color: red">from modal answer: (basically the same but a better proof formating)</span> 

$$\begin{aligned}
L_k^{-1}L_{k+1}^{-1} &= (I + \ell_{k}e_k^T)(1 + \bar{\ell_{k+1}}e_{k+1}^T)\\
&= I + \bar{\ell_{k}}e_{k}^T + \bar{\ell_{k+1}}e_{k+1}^T + \bar{\ell_{k}}e_{k}^T\bar{\ell_{k+1}}e_{k+1}^T\\
&= I + \bar{\ell_{k}}e_{k}^T + \bar{\ell_{k+1}}e_{k+1}^T
\end{aligned}$$

therefore, $L_k^{-1}L_{k+1}^{-1} = L_k^{-1} + L_{k+1}^{-1} - I$
# Problem 2:

**The Gaussian elimination algorithm can also be applied to find the Cholesky factorisation for symmetric positive-definite matrices, with slight modification. In particular, the diagonal elements of L can no longer be set to zero (otherwise the diagonal elements of U would also have to be zero). Please show how the Gaussian elimination process can be modified to give a symmetric decomposition for a symmetric positive-definite matrix A (i.e. $U = L^T$)**

<span style="color: red">from modal answer: </span> 

we write the matrix A to isolate the first element $a_{1,1}$

$$A = \begin{bmatrix}\begin{array}{c|c}a_{1,1} & b\\\hline b^T & C\end{array}\end{bmatrix}$$

the Applying the $L_1A$ as in standard Gaussian elimination gives

$$\begin{aligned}\underset{L_1}{\begin{bmatrix}\begin{array}{c|c}1 & 0\\\hline \frac{-b^T}{a_{1,1}} & I\end{array}\end{bmatrix}}\underset{A}{\begin{bmatrix}\begin{array}{c|c}a_{1,1} & b\\\hline b^T &C\end{array}\end{bmatrix}} & = \underset{U_1}{\begin{bmatrix}\begin{array}{c|c}a_{1,1} & b\\\hline 0 & C -\frac{bb^T}{a_{1,1}}\end{array}\end{bmatrix}}\\
\underset{A}{\begin{bmatrix}\begin{array}{c|c}a_{1,1} & b\\\hline b^T &C\end{array}\end{bmatrix}}  &=
\underset{L_1^{-1}}{\begin{bmatrix}\begin{array}{c|c}1 & 0\\\hline \frac{-b^T}{a_{1,1}} & I\end{array}\end{bmatrix}}\underset{U_1}{\begin{bmatrix}\begin{array}{c|c}a_{1,1} & b\\\hline 0 & C -\frac{bb^T}{a_{1,1}}\end{array}\end{bmatrix}}\\
\end{aligned}$$

we wanted this to be symmetric, so instead of applying a factor 1, we apply a factor of $\sqrt{a_{1,11}}$

$$\underset{A}{\begin{bmatrix}a_{1,1} & b\\b^T & C\end{bmatrix}} = \underset{L_1^{-1}}{\begin{bmatrix}\sqrt{a_{1,1}} & 0\\\frac{b^T}{\sqrt{a_{1,1}}} & I\end{bmatrix}}\underset{U_1}{\begin{bmatrix}\sqrt{a_{1,1}} & \frac{b}{\sqrt{a_{1,1}}}\\b^T & C - \frac{bb^T}{a_{1,1}}\end{bmatrix}}$$

we can also rewrite this as

$$\underset{A}{\begin{bmatrix}a_{1,1} & b\\b^T & C\end{bmatrix}} = \underset{L_1^{-1}}{\begin{bmatrix}\sqrt{a_{1,1}} & 0\\\frac{b^T}{\sqrt{a_{1,1}}} & I\end{bmatrix}}\underset{A_1}{\begin{bmatrix}1 & 0\\0 & \bar{A}\end{bmatrix}}\underset{U_1}{\begin{bmatrix}\sqrt{a_{1,1}} & \frac{b}{\sqrt{a_{1,1}}}\\b^T & I\end{bmatrix}}$$
where $\bar{A} = C - \frac{bb^T}{a_{1,1}}$

we can see that this process eliminates one of the columns and rows, turning A to $A_1$

therefore, we can proceed with the same process until

$$\begin{aligned}
A &= R_1^TR_2^T\dots R_m^TA_mR_m\dots R_2R_1\\
A &=\underset{R^T}{(R_1^TR_2^T\dots R^T_m)}I\underset{R}{(R_m\dots R_2R_1)}\\
A&= R^TR
\end{aligned}$$

thus giving the Cholesky factorisation of A

# Problem 3:

**Showing convergence of a sequence in a metric space is very similar to one in $\mathbb{R}$. We just need to swap the absolute value of the difference with metric. Let's consider $\mathbb{R}^{m\times m}$ with a given sub-multiplicative norm $||\bullet||$ as the matrix. Given some matrix $B\in\mathbb{R}^{m\times m}$, we define the sequence for $n\in \mathbb{N}$**

$$G^{(n)} = \sum_{i=0}^nM^i = I + M + \dots + M^n$$

**where we use parathetical superscripts to indicate iteration as in the textbook by Darta**

## (a)
**Show that $(I-M)G^{(n)} = G^{(n)}(I-M) = I-M^{n+1}$**

so $(I - M)G^{(n)} = (I-M)\sum_{i=0}^nM^i = \sum_{i=0}^nM^i - \sum_{i=1}^{n+1}M^i = 1 - M^{n+1}$

similarly, we can prove $(I-M)G^{(n)} = G^{(n)}(I-M)$

## (b)
**Suppose that $||M||<1$; show that $M^n\to n$ as $n\to\infty$**

since $||\bullet||$ is sub-multiplicative $||AB||\le ||A||\text{ }||B||$

therefore $||M||^n\le ||M^n||$

and since $||M||\lt 1$ $||M||^n \to n$ as $n\to\infty$

therefore $||M^n||\to 0$

and therefore $M^n \to 0$ (<span style="color:red">this means the matrix would approach a state where every entry is 0</span>)

## (c)
**Again supposing that $||M|| < 1$, show that $\lim_{n\to\infty}G^{(n)} = (I-M)^{-1}$**

$(*)\iff \lim_{n\to\infty}(I-M)G^{(n)} = (I-M)(I-M)^{-1} = I$

and we prove that $(I-M)G^{n} = 1-M^{n+1}$

and $M^{n+1}\to 0$ as $n+1\to\infty$

therefore $\lim_{n\to\infty}(I-M)G^{(n)} = I$

$\lim_{n\to\infty}G^{(n)} = (I-M)^{-1}$

# Problem 4:

**We define an iterative method as the sequences $a^{(n)}$ and $b^{(n)}$ for $n\in\mathbb{N}$ as**

$$\begin{aligned}
a^{(n+1)} &= \alpha a^{(n)} + 1\\
b^{(n+1)} &= \beta b^{(n)} + 2\\
\alpha,\beta &\in (0,1)
\end{aligned}$$
**where we use parenthetical superscripts to indicate iterative as in the textbook by Darta**

## (a)

**Defining the vector $x^{(n)} = \begin{bmatrix}a^{(n)}\\b^{(n)}\end{bmatrix}$, write this iterative method in the form we used for classical iterative schemes, $x^{(n+1)} = Bx^{(n)} + d$**

let $B = \begin{bmatrix}\alpha & 0\\0 &\beta\end{bmatrix}$ and $d = \begin{bmatrix}1\\2\end{bmatrix}$

## (b)

**prove that the sequence $x^{(n+1)} = Bx^{(n)} + d$ converges $n\to\infty$**

since $B = \begin{bmatrix}\alpha & 0\\0 &\beta\end{bmatrix}$

and $\alpha,\beta\in(0,1)$

so $||B||<1$

according to the lecture notes, we know $x^{(n)}$ is convergent

## (c)
**We now suppose $\alpha <\beta$, and we define $c^{(n)} = a^{(n)} + b^{(n)}$ and $x^{(n)} = \begin{bmatrix}a^{(n)}\\b^{(n)}\\c^{(n)}\end{bmatrix}$. Show this results in the scheme**
$$x^{n+1} = \begin{bmatrix}\alpha & 0 & 0\\0 &\beta & 0\\\alpha -\beta & 0 & \beta\end{bmatrix}$$

this is obvious

unfolding the equation gives

$$\begin{aligned}\begin{bmatrix}a^{(n+1)}\\b^{(n+1)}\\c^{(n+1)}\end{bmatrix} &= \begin{bmatrix}\alpha & 0 & 0\\0 &\beta & 0\\\alpha -\beta & 0 & \beta\end{bmatrix}\begin{bmatrix}a^{(n)}\\b^{(n)}\\c^{(n)}\end{bmatrix} +\begin{bmatrix}1\\2\\3\end{bmatrix}\\&= \begin{bmatrix}\alpha a^{(n)}\\\beta b^{(n)}\\(\alpha - \beta)a^{(n)} + \beta c^{(n)}\end{bmatrix}+\begin{bmatrix}1\\2\\3\end{bmatrix}\\
&=\begin{bmatrix}\alpha a^{(n)}\\\beta b^{(n)}\\\alpha a^{(n)} + \beta b^{(n)}\end{bmatrix}+\begin{bmatrix}1\\2\\3\end{bmatrix}
\end{aligned}$$
## (d)

**Show that this new sequence for $x^{(n+1)}$ converges as $n\to\infty$**

still $\alpha-\beta \in(0,1)$

so the $\ell_{\infty}$ norm of $\begin{bmatrix}\alpha & 0 & 0\\0 &\beta & 0\\\alpha -\beta & 0 & \beta\end{bmatrix}$ is less than 1