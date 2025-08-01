---
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
level: Imperial
---
Vector and Matrix Forms

# some revision

The dot product is $v\bullet w = ||v||\text{ }||w||\cos{\theta}$

if we change the basis(from the default orthorgonal basis to another basis) the formula survives(may need to revisit)

for a matrix $f = \mathbb{R}^{m\times n}$

this is also independent of the basis

# vector norms:

The vector norm is the generalisation of Euclidean length of a vector

$||\bullet||:\mathbb{R}^n\to\mathbb{R}$

axioms:

- $||x|| > 0 \text{ if } x\neq 0$
- $\forall \lambda\in\mathbb{R} ||\lambda v|| = |\lambda|\text{ }||v||$
- $\forall x,y\in\mathbb{R}^{n}, ||x+y||\le ||x|| + ||y||$ triangular inequality

this is actualy just the norm being a metric, and the three rules being the rules required for a metric

when $n = 2$, the norm is the Euclidean distance

A norm $||\bullet||$ on $\mathbb{R}^n$ includes a metric d on $\mathbb{R}^n$ by $d(x,y) := ||x-y||$, this is translation-invariant so $d(x+z,y+z) = d(x,y)$

# the l-norms

recall the norms l1 l2 and $l_{\infty}$ from last year

these are, by default w.r.t orthorgonal basis, but if we change the basis, only the l2 norm is invariant regardless of basis

and also recall we proved that $l_1\le l_2\le l_{\infty}$

- p > 0, the $l_p$ norm of any vector $v\in \mathbb{R}^n$ is defined as $||v||_p = \Bigg(\sum_{i=1}^n|v_i|^p\Bigg)^{1/p}$

- p = 1 $l_1$ norm $||x||_1 = \sum_{i=1}^n|x_i|$
- p = 2 $l_2$ norm $||x||_2 = \sqrt{\sum_{i=1}^nx_i^2}$ this is also called the Euclidean norm
- p = $\infty$ $l_{\infty}$ norm: $||x||_{\infty} = \max_{1\le i\le n}|x_i|$

## relation between the $l_p$ norms

- $||x||_{\infty} \le ||x||_2$

$||x||_{\infty}^2 = \max_{1\le i\le n}|x_i^2\le \sum_{i=1}^n x_i^2 = (||x||_2)^2$

- $||x||_2\le ||x||_1$

$||x||_2^2 = \sum_{i=1}^n x=i^2\le \sum_{i=1}^nx_i^2 + \sum_{i\neq j}|x_i||x_j| = (\sum_{i=1}^n|x_i|)^2 = ||x||_1^2$

and thus $||x||_1\le ||x||_1$

## The $l_{\infty}$ norm

Claim: As $p\to\infty$, we have $||v||_p\to||v||_{\infty} =\max_{1\le i\le n}|v_i|$

Let $m\in\{1,2,3,\dots,n\}$ be such that $|v_m| = \max_{i\le i\le n}|v_i|$

$||v||_p = \Bigg(\sum_{i=1}^n|v_i|^p)^{1/p}\Bigg)$

The map $x\mapsto x^{1/p}$ is montone for $x\in\mathbb{R}$. Therefore

$|v|_m\le ||v||_p = \Bigg(\sum_{i=1}^n|v_i|^p\Bigg)^{\frac{1}{p}}\le \Bigg(\sum_{i=1}^n|v_m|^p\Bigg)^{\frac{1}{p}} = (n)^{\frac{1}{p}}|v_m|\to|v_m|$

as $p\to\infty$, since $n^{\frac{1}{p}}\to 1$ as $p\to\infty$ for $n\ge 1$

Thus $||v||_p\to |v_m| = ||v||_{\infty}$ as $p\to\infty$


## equivalence of all vector norms

- proposition1:

$||v||_2\le\sqrt{n}||v||_{\infty}$


- proposition2:

$||v||_1\le\sqrt{n}||v||_2$

we use the Cauchy Schwartz

pick $w\in \mathbb{R}^{n}$ with all the elements as 1

$||v||_2^2 = \sum_{i=1}^nv_i^2$

$||v||_1^2 = (\sum_{i=1}^{n}|x_i|) \le n(\sum_{i=0}^n v_i)$ by cauchy schartz

- Any two vector norms $||v||_a$ and $||v||_b$ for $v\in\mathbb{R}^n$ are equivalent, i.e. there exist constants $r>0$ and $s > 0$ such that for all $v\in\mathbb{R}^n$

$r||v||_a\le ||v||_b\le s||v||_a$

- This means that any sequence of vectors converging wrt to one norm converges wrt also any other norm

- Any function $f:\mathbb{R}^n\to\mathbb{R}^m$ is continuous wrt a given pair of norms is continuous wrt any other pair

# Matrix norms:

A matrix norm, defined only on any Euclidean space $\mathbb{R}^{m\times n}$ for positive integers m and n, is a real-valued map satisfying thefollowing four axioms

- For any nonzero matrix $A\in\mathbb{R}^{m\times n}.||A||>0$
- For any scalar $\lambda$, and $A\in\mathbb{R}^{m\times n}:||\lambda A|| =|\lambda|||A||$
- For $A, B\in\mathbb{R}^{m\times n}: ||A+B||\le ||A|| + ||B||$ (triangular inequality)
- For $A\in\mathbb{R}^{m\times n}$ and $B\in\mathbb{R}^{n\times p}: ||AB||\le ||A||||B||$ (sub-multiplicative)

this additional axiom is because in the processing of mapping

$v\mapsto Mv\mapsto NMv$

but in vector scalor multiplication is pre-defined
# Consistent and Compatible Matrix norms

A matrix norm $||\bullet||$ is consistent with vetor norms $||\bullet||_a$ on $\mathbb{R}^n$ and $||\bullet||_b$ on $\mathbb{R}^m$ if forall $A\in\mathbb{R}^{m\times n}$ and $v\in\mathbb{R^n}$ and $v\in \mathbb{R}^n$ we have $||Av||_b\le ||A||||A||_a$.If in addition a = b, we say the matrix norm is compatible with the vector norm $||\bullet||_a$

For a matrix $A\in\mathbb{R}^{m\times n}$ let $a_j$ denote its jth column and $a^i$ its ith row, $1\le j\le n$ and $1\le i\le m$

Norms $||v||_1,||v||_2,||v||_{\infty}$ have compatible matrix norms:

$\begin{aligned}||A||_1 &=\max_j||a_j||_1 &\text{maximum absolute column sum}\\||A||_2 &=\sigma_1(A) & \text{largest eigen/singular value of A}(studied later)\\||A||_{\infty} &=\max_i||a^i||_1 & \text{maximum absolute row sum}\end{aligned}$

Note that $||A||_1 = ||A^T||_{\infty}$

The Frobenius norm: $||A||_F = \sqrt{\sum^{m}_{i=1}\sum_{j=1}^n|A_{ij}|^2}$ is consistent with the l2 vector norm, $||Av||_2\le ||A||_F||v||_2$

so for example, $A = \begin{bmatrix}2 & 3 & 1 & 4\\ 2 & 3 & -1 & 5\\\sqrt{2} & 0 & -2 & 2\end{bmatrix}$

- $||A||_1 = 11$
- $||A||_{\infty} = 10$
- $||A||_F = 76$

To find $||A||_2$, the largest singular value, we need to do more work

## Definition:

A matrix norm |||| is sais to be consisitent with vector norm $||||_{\alpha}$ and $||||_{b}$ if 

$\forall x\in\mathbb{R}: ||Ax||_b\le ||A|\times||x||_a$

$A\in\mathbb{R}^{n}$

And if a = b then |||| is said to be compatible with $||||_a = ||||_b$ if

$\forall x\in\mathbb{R}^n, |||Ax|\le ||A||·||x||$

so the size od the output is bounded by the size of the inputs times the size of the matrix (consider this as a mapping)

# Matrix norms in term of vector norms

We have the following expressions for matrix norms for any matrix $A\in\mathbb{R}^{m\times n}$

$\begin{aligned}||A||_1 = sup\{||Ax||_1: ||x||_1\le 1\} = \max\{||Ax||_1:||x||_1\le 1\}\\||A||_2 = sup\{||Ax||_2: ||x||_2\le 1\} = \max\{||Ax||_2: ||x||_2\le 1\}\\||A||_{\infty} = sup\{||Ax||_{\infty}: ||x||_{\infty}\le 1\} = \max\{||Ax||_{\infty}: ||x||_{\infty}\le 1\}\\\end{aligned}$

In each case, we used the same vector norm in $\mathbb{R}^n$ and $\mathbb{R}^m$

It follows that

- $||Ax||_p\le ||A||||x||_p$ for $p = 1,2,\infty$

for example, we try to prove the case when $p =\infty$

then

$\begin{aligned}||Ax||_{\infty} &= \max_{1\le i\le m}|\sum_{j = 1}^n a_{ij}x_{i}|\\&= \max_{1\le i\le m}|\sum_{j=1}^n a_{ij}x_j|\\&= \max_{1\le i\le m}|\sum_{1\le i\le m}a_{ij}x_j|\\&\le\max_{1\le i\le m}\sum_{j=1}^n|a_{ij}||x_j|\\&= (\max_i\max_{j=1}^n|a_{ij}|)||x||_{\infty}\\&= ||A||_{\infty}||x||_{\infty}\\\end{aligned}$

and for $p=1$ we have $||A||_{1} = ||A^{T}||_{\infty}$

but this is only part of the proof, we need to state that the maximum can be reached for the max

- $||AB||_p\le ||A||_p||B||_p$ for m = n, p = 1,2,$\infty$

# Matrix norm subordinate to a vector norm

- For a vector norm $||\bullet||$ the subordinate matrix norm for $A\in\mathbb{R}^{m\times n}$ is defiend as

$||A|| = \sup\{||Ax||: x\in\mathbb{R}^n, ||x|| = 1\}$

the matrix norms ||A|| defined above satisfies $||A|| = \sup \{||Ax||: ||x||\le 1\} = \sup \{||Ax||/||x||: x\neq 0\}$

$||A|| = \sup\{||Ax||:||x||\le 1\} = \max\{||Ax||:||x|| = 1\}$ 

we can also use different vector norms in $\mathbb{R}^n$ and $\mathbb{R}^m$ i.e.

$||A||_{\alpha,\beta} = \sup\{||Ax||_{\beta}: x\in\mathbb{R}^n,||x||_{\alpha} = 1\}$

where $||\bullet||_{\alpha}, ||\bullet||_{\beta}$ are norms for $\mathbb{R}^n, \mathbb{R}^m$



the matrix norms are compatible and suboridinate with the vector norms
