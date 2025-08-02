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
# Discrete Random Variables

We say a random variable is discrete if it can take only a countable number of possible values. That is,

$X\text{ is discrete}\iff supp(X)\text{ is countable}$

Thus $supp(X)$ can either be finite or countably infinite

$S_x = \{s\in \mathbf{S}|X(s)\le x\}$ is constant in $[x_{i-1}, x_i)$

so $F_X$ will be a step function

$F_X(x_i) = F_X(x_{i-1}) + P_X(X = x_i)$

or 

$P_X(X = x_i) = F_X(x_i) - F_X(x_i - 1)$

## Probability Mass function (PMF)

For a discrete random vairbale X and $x\in\mathbb{R}$, we define the probability mass function (omf), p(x)(more precisely as $p_x(x)$) as

$p(x) = P_x(X = x)$

if X can take values $supp(X) = \{x_1, x_2,\dots\}$

- $0\le p(x)\le 1, \forall x \in\mathbb{R}$
- $\sum_{x\in supp(X)}p(x) =1$

we can derive the cdf from pmf and vice versa

$$\begin{aligned}
p(x_i) &= F(x_i) - F(x_{i-1})\\
F(x_i) &= \sum_{j = 1}^ip(x_j)
\end{aligned}$$

# Expectation

For a discret erandom variable X we define the expectation of X to be

$E(X) = \sum_{x}xp(x)$

this is a weighted average and is reffered to as the mean of the distribution of X

if applied to a functio of a random variable

$E(g(X)) = \sum_x g(x)p(x)$

Expectation satisfy linearity

$$\begin{aligned}
E(aX + b) &= \sum_x(ax+b)p(x)\\
&= a\sum_{x}xp(x) + b\sum_{x}p(x)\\
&= aE(x) + b \forall a,b\in\mathbb{R}
\end{aligned}$$

we can also prove that $E(g(X) + h(X)) = E(g(X)) + E(h(X))$

# Moments:

## Variance:

The expectation of a function $g(X) = X^n$ gives us the nth (raw) moment of X.

A central moment is similarly defined, but re-centered to characterize the deviation from the mean. 

$g(X) = (X - E(X))^2$

$Var(x) = \sigma^2 = E[(X - E(X))^2]$

also

$$\begin{aligned}
(X - E(X))^2 &= X^2 - 2E(X)X + (E(X))^2\\
\Rightarrow Var(X) &= E[X^2 - (2E(X))X + (E(X))^2]\\
&= E(X^2) - 2E(X)E(X) + (E(X))^2\\
&= E(X^2) - (E(X))^2
\end{aligned}$$

we can also prove that $Var(aX+b) = a^2Var(X)$

## standard deviation

$sd(X) = \sigma_X = \sqrt{Var_X(X)}$

## Skewness:

The skewness ($\gamma_1$) of a discrete random variable X is a measure of its asymmetry. It is expressed as the following standardized moment:

$\gamma_1 = \frac{E[(X-E(X))^3]}{sd(X)^3}$

usually we have $\mu = E(X)$ and $\sigma = sd(X)$

so $\gamma_1 = \frac{E[(X-\mu)^3]}{\sigma^3}$

# Sum of Random Variables

let $X_1, X_2,\dots, X_n$ be n variables, possibly with different distributions and not necessarily

let $S_n = \sum_{i=1}^n X_i$ be their sum, and $\overline{X} = \frac{S_n}{n}$ be their average.

Then 

$E(S_n) = \sum_{i=1}^n E(X_i),E(\overline{X}) = \frac{\sum_{i=1}^n E(X_i)}{n}$

if the random variables are independent, then

$Var(S_n) = \sum_{i=1}^n Var(X_i), Var(\bar{X}) = \frac{\sum_{i=1}^n Var(X_i)}{n^2}$

if $X_1, X_2,\dots, X_n$ are independent and identically distirbuted with $E(X_i) = \mu_X$ and $Var(X_i) = \sigma_X^2$

$E(\bar{X}) = \mu_X, Var(\bar{X}) =\frac{\sigma_X^2}{n}$

# Discrete Distributions

## Bernoulli(p)

one experiment, p success (1-p) fail

$pmf = p^x(1-p)^{1-x}, (x = 0,1)$

$\mu = p, \sigma^2 = p(1-p)$

## Binomial(n,p)

n * Bernoulli(p)

$p(x) = \big(\begin{matrix}n\\x\end{matrix}\big)p^x(1-p)^{n-x}, x = 0,1,2,3,4...$

$\mu = np, \sigma^2 = np(1-p),\gamma_1 = \frac{1-2p}{\sqrt{np(1-p)}}$

## Geometric(p)

an infinite sequence of Bernoulli(p), we try until succeed

$p(x) = p(1-p)^{x - 1}, x = 1,2,...$

$\mu = \frac{1}{p},\sigma^2 =\frac{1-p}{p^2}, \gamma_1 = \frac{2-p}{\sqrt{1-p}}$

the skewness is always positive

## Poisson: Poi($\lambda$)

$p(x) = \frac{e^{-\lambda}\lambda^x}{x!}, x= 0,1,2,...$

for some $\lambda > 0$

poisson random variable are concerned with the number of random events occurring per unit of time or space, if there is a constant rate a random events occurring across the unit

e.g. minor car crashes per day in the UK

$\mu = \lambda,\sigma^2 =\lambda,\gamma_1 = \frac{1}{\sqrt{\lambda}}$

if we have a non-unit interval or space of length t, the we use Poi($\lambda$t)

## Uniform

$p(x) = \frac{1}{n}, x = 1,2,...,n$

$\mu = \frac{n+1}{2},\sigma^2 = \frac{n^2-1}{12}$
