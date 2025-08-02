---
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
level: Imperial
---



# 8.

**Consider the following distribution**

$$f(x|k,\lambda) = \frac{\lambda^kx^{k-1}e^{-\lambda x}}{(k-1)!}$$
## a.
**Knowing that this distribution gives the density of the sum of k i.i.d. exponential random variables with rate $\lambda$, use the moment generating function method to derive analytical expressions for its mean and variance**

we know this is a gamma distribution from the question

the mgf can be calculated with 
$$\begin{aligned}
M_x(t) = &\int_{-\infty}^{\infty}e^{tx}f(x|k,\lambda)dx\\
&=\int_{-\infty}^{\infty}e^{tx}\frac{\lambda^kx^{k-1}e^{-\lambda x}}{(k-1)!}dx\\
&=\int_{0}^{\infty}e^{tx}\frac{\lambda^kx^{k-1}e^{-\lambda x}}{(k-1)!}dx & f(x|k,\lambda) \text{is only defined for}x\ge 0\\
&=\int_{0}^{\infty}\frac{\lambda^kx^{k-1}e^{(t-\lambda)x}}{(k-1)!}dx\\
&=\frac{\lambda^k}{(k-1)!}\int_{0}^{\infty}x^{k-1}e^{(t-\lambda)x}dx\\
\end{aligned}$$

at this point, for clarity, we focus on the integral part 

$$
\begin{aligned}
\int_{0}^{\infty}x^{k-1}e^{(t-\lambda)x}dx &=\frac{1}{(t-\lambda)}\int_0^{\infty}x^{k-1}de^{(t-\lambda)x}\\
&=\frac{1}{(t-\lambda)}\Big(x^{k-1}e^{(t-\lambda)x}\Big|_{0}^{\infty}-\int_{0}^{\infty}e^{(t-\lambda)x}dx^{k-1}\Big)\\
&=\frac{k-1}{(t-\lambda)}\Big(x^{k-1}e^{(t-\lambda)x}\Big|_{0}^{\infty}-\int_{0}^{\infty}e^{(t-\lambda)x}x^{k-2}dx\Big)\\
\end{aligned}
$$

to evaluate $x^{k-1}e^{(t-\lambda)x}\Big|_{0}^{\infty}$

we need to discuss in cases, 

if $t-\lambda \ge 0$, $x^{k-1}e^{(t-\lambda)x}\Big|_{0}^{\infty}$ is obviously $\infty$, which make the whole mgf $\infty$ and meaningless, therefore we assume this case would never happen, in other words, we enforce $\lambda>t$

we rewrite the formula

$$x^{k-1}e^{(t-\lambda)x} = \frac{x^{k-1}}{e^{(\lambda-t)x}}$$

notice that the numerator and the denominator have similar characteristics in the limit, or

if $x\to 0, x^{k-1}\to 0\quad(k\ge 1), e^{(\lambda -t)x}\to 0$

and if $x\to \infty, x^{k-1}\to \infty\quad(k\ge 1), e^{(\lambda -t)x}\to \infty\quad(\lambda > t)$

also notice that in the general case, this also applies for all $x^{a},x>0$ and also apply when $x^{a}$ is multiplied by any constant, since $C * 0 = 0, C * \infty = \infty$

therefore, by recursively applying L'hopital rule, we get

$\lim_{x\to\infty}\frac{x^{k-1}}{e^{(k-t)x}} = \lim_{x\to\infty}\frac{(k-1)x^{k-2}}{(\lambda-t)e^{(\lambda-t)x}} = \dots = \lim_{x\to\infty}C*\frac{1}{e^{(\lambda - t)x}} = 0$
and $\lim_{x\to 0}\frac{x^{k-1}}{e^{(\lambda-t)x}} = \frac{0}{1} = 0$

so $x^{k-1}e^{(t-\lambda)x}\Big|_{0}^{\infty} = 0$

back to the integral, this gives

$$
\begin{aligned}
\int_{0}^{\infty}x^{k-1}e^{(t-\lambda)x}dx 
&=\frac{k-1}{(t-\lambda)}\Big(x^{k-1}e^{(t-\lambda)x}\Big|_{0}^{\infty}-\int_{0}^{\infty}e^{(t-\lambda)x}x^{k-2}dx\Big)\\
&=\frac{k-1}{\lambda-t}\int_{0}^{\infty}e^{(t-\lambda)x}x^{k-2}dx\\
&=\text{this iterates}
\end{aligned}
$$
if we denote $I_{k-1} = \int_{0}^{\infty}x^{k-1}e^{(t-\lambda)x}dx$ and so forth, then $I_{k-1} = \frac{k-1}{\lambda-t}I_{k-2}$

and actually $I_{n} = \frac{n}{\lambda-t}I_{n-1}$

the final term $I_0 = \int_{0}^{\infty}e^{(t-\lambda)x}dx = \frac{1}{t-\lambda}e^{(t-\lambda)x}\Big|_{0}^{\infty} = \frac{1}{t-\lambda}e^{u}\Big|_{u = 0}^{-\infty} = \frac{1}{\lambda-t}e^{u}\Big|_{u=-\infty}^{0} = \frac{1}{\lambda-t}$

so the integral can be evaluated as 

$$\int_{0}^{\infty}x^{k-1}e^{(t-\lambda)x}dx =\frac{1}{(t-\lambda)}\int_0^{\infty}x^{k-1}de^{(t-\lambda)x}\\ = \frac{1}{\lambda-t}\prod_{n=1}^{k-1}(\frac{n}{\lambda-t}) = \frac{(k-1)!}{(\lambda-t)^k}$$
therefore, finally,

$$M_x(t) = \frac{\lambda^k}{(k-1)!}\int_{0}^{\infty}x^{k-1}e^{(t-\lambda)x}dx = \frac{\lambda^k}{(k-1)!}\frac{(k-1)!}{(\lambda-t)^k} = \Big(\frac{\lambda}{\lambda-t}\Big)^k$$
therefore
$$\begin{aligned}
\mu=\frac{dM_x(t)}{dt}\Big|_{t=0} &=\frac{d}{dt}\Big(\frac{\lambda}{\lambda-t}\Big)^k\Big|_{t=0}\\
&=k\lambda^k(\lambda-t)^{-(k+1)}\Big|_{t=0}\\
&=\frac{k}{\lambda}
\end{aligned}$$
and 
$$\begin{aligned}E[X^2] &= \frac{d^2M_x(t)}{dt^2}\Big|_{t=0}\\
&=\frac{d(k\lambda^k(\lambda-t)^{-(k+1)})}{dt}\Big|_{t=0}\\
&=k(k+1)\lambda^k(\lambda-t)^{-(k+2)}\Big|_{t=0}\\&=\frac{k(k+1)}{\lambda^2}\end{aligned}$$

therefore

$$Var(X) = E[X^2]-E[X]^2 =\frac{k(k+1)}{\lambda^2}-(\frac{k}{\lambda})^2 = \frac{k}{\lambda^2}$$

## b

**Assume in this part that you collected the following n = 10 samples from the distribution** 

**(2.846,3.445,4.376,0.402,2.893,2.522,0.458,3.742,3.156,1.030)**

**Give unbiased estimates for the mean and variance of this distribution. Using the results of part a., obtain estimates for k and λ, ensuring that the obtained values are admissible for this distribution.**

the mean value of this sample is 

$$\begin{aligned}\frac{1}{n}&\sum_{n=1}^{10} x_n \\ &=\frac{2.846+3.445+4.376+0.402+2.893+2.522+0.458+3.742+3.156+1.030}{10}\\&=\frac{24.87}{10} = 2.487\end{aligned}$$

the variance of this sample is

$$\begin{aligned}
\sigma^2 = \frac{1}{n-1}\sum_{n=1}^{10}(x_n-\mu)^2\\
=&\frac{1}{9}\Big((2.846-2.487)^2 + (3.445-2.487)^2 +\\& (4.376-2.487)^2 + (0.402-2.487)^2 +\\& (2.893-2.487)^2 + (2.522-2.487)^2 +\\& (0.458-2.487)^2 + (3.742-2.487)^2+\\&(3.156-2.487)^2 + (1.030-2.487)^2\Big)\\
=& \frac{1}{9}\Big(0.359^2 + 0.958^2 + 1.889^2 + (-2.085)^2\\
&0.406^2 + 0.035^2 + (-2.029)^2 + 1.255^2\\
&0.669^2 + (-1.457)^2\Big)\\
=&\frac{17.3905}{9} \approx 1.9323
\end{aligned}$$

therefore

$\mu = \frac{k}{\lambda} = 2.487$

$\sigma^2 = \frac{k}{\lambda^2} = 1.9323$

so $\lambda = \frac{\mu}{\sigma^2}\approx\frac{2.487}{1.9323} = 1.287$

$k = \mu\lambda = 2.487*1.287\approx 3.201$

and since $\lambda > 0,k\ge 1$, this set of parameters is admissable

## (c)

**Assume in this part that k is known. Suppose now that you have collected n independent samples $(x_1,x_2,...,x_n)$ from this distribution. Derive an analytical expression for the maximum likelihood estimate for $\lambda$ based on these samples, expressing it as a function of the sample mean X and the known value of k**

(to be consistent with the notation in the lectures, the log in the following proof is actually ln)

to get the MLE of this distribution, we first try to obtain the log-likelihood function of the distribution

$$\begin{aligned}
\ell(\lambda) = \log L(\lambda) &=\log\prod_{i=1}^nf(x_i|\lambda,k) &\text{k is known}\\&=\log\prod_{i=1}^n\frac{\lambda^kx_i^{k-1}e^{-\lambda x_i}}{(k-1)!}\\
&=nk\log\lambda + (k-1)\sum_{i=1}^n\log x_i + -\lambda \sum_{i=0}^nx_i\log e - n\log(k-1)!\\
\end{aligned}$$

we would want to maximize, or calculate the value of $\lambda$ that make the derivative 0

$\frac{d\ell(\lambda)}{\lambda} = \frac{nk}{\lambda} - \sum_{i=0}^n x_i$

therefore $\lambda = \frac{nk}{\sum_{i=0}^n x_i} = \frac{k}{\bar{X}}$

