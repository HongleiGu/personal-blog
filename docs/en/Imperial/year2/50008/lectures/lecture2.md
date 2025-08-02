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
random variables

# Definition:

- A probability space $(\mathbf{S},\mathbf{F},P)$ is  a triplet that models the random experiment, P is a probability function, define on subsets $E\subset \mathbf{S}$ of the sample space S belonging to the $\sigma$-algebra $\mathbb{F}$

-  A Random variable is a mapping from the sample space to real numbers. So if X is a random variable, $\mathbf{X}: S\to\mathbb{R}$.

- If we denote the generic outcome of the random expriment as s, then the correpsonding outcome of the random vairbale $X(s)$ can be referred to as X

For example, when rolling a die, $X(s) = \text{the number of spots on the face up}$

likewise, we can also define, $Y(s) = \text{the number of spot on the die face up is odd}$

then we can refer to the events, for example $P_Y(Y = 0) = \frac{1}{2}$

# Inducted Probability

For each $x\in\mathbb{R}$, let $S_x\subseteq S$ be the set containing just those elements of $\mathbf{S}$ which are mapped by X to numbers no greater than x, or $S_x = \{s\in S|X(s)\le x\}$

so we can write $P_X(X\le x)\equiv P(S_x)$

## support

the image of S under X is called the support of X:

$supp(X)\equiv X(S) = \{\in\mathbb{R}|\exists s\in \mathbf{S}\text{ s.t. } X(s) = x\}$

S contains all the possible outcomes of the expreiment

supp(X) contains all the possible outcomes of the random variable

so $P_X(X\le x)$ is defined for all $x\in supp(X)$

# Cumulative Distribution Function(CDF)

THe CDF of a random variable X written $F_X(x)$ ofr just F(x) is the probability that X takes a value less or equal than x

$F_X(x) = P_X(X\le x)$

Fo rany random variable X, $F_X$ is right continuous, meaning if a decreasing sequence of real numbers $x_1, x_2,\dots\to x$, then $F_X(x_1),F_X(x_2),\dots\to F_X(x)$

for a valid CDF

- Monotonicity: $\forall x_1, x_2\in \mathbb{R}, x_1<x_2\Rightarrow F_X(x_1)\le F_X(x_2)$
- $F_X(-\infty) = 0, F_X(\infty) = 1$
- $F_X$ is right continuous

Note that the first two conditions imply $0\le F_X(x)\le 1, \forall x\in\mathbb{R}$

For finite intervals $(a,b]\subseteq\mathbb{R}$ it is possible to check that

$P_X(a<X\le b) = F_X(b)-F_X(a)$

this can be done noting that the event $E=\{X\le b\}$ may be written as the union $E=H\cup G$ of the disjoint events:

- $H = (-\infty, a]$
- $G = (a,b]$
