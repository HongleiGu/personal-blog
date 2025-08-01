---
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
level: Imperial
---

# 1.

**Suppose the joint pdf of a pair of continuous random variables is given by**

$$f(x,y) = \begin{cases}\begin{array}{c}k(x + y) & 0 < x < 2, 0 < y < 2\\ 0 &\text{otherwise}\end{array}\end{cases}$$

## (a) 
**find the constant k**

so following the definition

$$\begin{aligned}\int_0^2\int_0^2k(x + y)dxdy &= 1\\
\int_0^2(\frac{k}{2}x^2 + kxy)\Big|_{x = 0}^2 dy &= 1\\
\int_0^2(2k + 2ky)dy &= 1\\
(2ky + ky^2)\Big|_{y = 0}^2 &= 1\\
8k &= 1\\
k &= \frac{1}{8}
\end{aligned}$$

## (b) 

**find the marginal pdfs of X and Y**

$$\begin{aligned}f_X(x) &= \int_{y = -\infty}^{\infty}f(x,y) dy\\
&=\int_{-\infty}^0f(x,y)dy + \int_0^2f(x,y)dy + \int_2^{\infty}f(x,y)dy\\
&= \int_{-\infty}^0 0dy + \int_{y = 0}^{2}(kx + ky) dy + \int_2^{\infty}0dy\\
&= \int_{y = 0}^2(kx + ky)dy\\
&=(kxy + \frac{k}{2}y^2)\Big|_0^2\\
&=2kx + 2k\\
&=\frac{1}{4}x +\frac{1}{4}& k = \frac{1}{8}\text{by (a)}
\end{aligned}$$

similarly the marginal pdfs of Y is given by $f_Y(y) = \frac{1}{4}y + \frac{1}{4}$


## (c)
**Find if X and Y are independent**

X and Y are independent if and only if $f(x,y) = f_X(x)f_Y(y),\forall x,y$

however, $f(x,y) = \frac{1}{8}(x + y) \neq \frac{1}{16}xy +\frac{1}{16}x + \frac{1}{16}y + \frac{1}{16} = (\frac{1}{4}x + \frac{1}{4})(\frac{1}{2}y +\frac{1}{4}) = f_X(x)f_Y(y)$

therefore X and Y are not independent

# 2
**A manufacturer has been using two different manufacturing processes to make computer memory chips. Let X and Y be a two continuous random variables, where X denotes the time to failure of chips made by process A and Y denotes the time to failure of chips made by process B. Assuming that the joint pdf of (X,Y) is**

$$f(x,y) = \begin{cases}
\begin{array}{c}
abe^{-ax + by} &x,y > 0\\
0 & \text{otherwise}
\end{array}
\end{cases}$$

**where $a = 10^{-4}$ and $b = 1.2\times 10^{-4}$ determine $P(X>Y)$**

since in this question the probabilities are only non-zero when x,y are both greater than 0, so we only discuss those cases

$$\begin{aligned}
\int_{x=0}^{\infty}\int_{y = x}^{\infty}abe^{-(ax + by)} dydx &= \int_{x=0}^{\infty}\int_{y=x}^{\infty}ae^{-(ax + by)}d(by)dx\\&= \int_{x=0}^{\infty}\int_{y=x}^{\infty}-ae^{-(ax + by)}d(-(ax+by)dx\\
&=\int_{x=0}^{\infty}-(ae^{-(ax+by)}\Big|_{y=x}^{\infty})dx\\
&=\int_{x=0}^{\infty}-ae^{-(ax+bx)}dx\\
&=\frac{a}{a+b}\int_{x=0}^{\infty}e^{-(ax+bx)}d(-(ax+by))\\
&=\frac{a}{a+b}e^{-(ax+bx)}\Big|_{x=0}^{\infty}\\
&=\frac{a}{a+b}\\
&=\frac{1.2}{2.2} = 0.55
\end{aligned}$$



# 3.

**The joint probability mass function of two discrete random variables X and Y is given by p(x,y) = cxy for x = 1,2,3 and zero otherwise, Find**

## (a)
**the constant c**

the probability must adds up to 1, so $\frac{1}{36}$

## (b)
**$P(X=2, Y=3)**

$\frac{1}{6}$

## (c)
**$P(X \le 2, Y \le 2)$**

$\frac{1}{4}$

## (d)
$P(X\ge 2)$

$\frac{5}{6}$

## (e)
$P(Y < 2)$

$\frac{1}{6}$

## (f)
$P(X = 1)$

$\frac{1}{6}$

## (g)
$P(Y = 3)$

$\frac{1}{2}$

# 4 

**Let X and Y be continuous variables  having joint density function $f(x, y) = c(x^2 + y^2)$ when $0\le x\le 1$ and $0\le y\le 1$ and $f(x,y) = 0$ otherwise. Determine**

## (a)

**the constant c**

again, the probability must adds up to 1

$$\begin{aligned}
\int_{x = 0}^1\int_{y = 0}^1c(x^2+y^2)dydx &= 1\\
\int_{x = 0}^1(cx^2y + \frac{c}{3}y^3)\Big|_{y=0}^1 dx &= 1\\
\int_{x = 0}^1(cx^2 + \frac{c}{3})dx &= 1\\
(\frac{cx^3}{3} + \frac{c}{3}x)\Big|_{x = 0}^1 &= 1\\
\frac{2}{3}c &= 1\\
c &= \frac{3}{2}
\end{aligned}$$

## (b)

**P(X< 1/2, Y > 1/2)**

$$\begin{aligned}\int_{x=0}^{\frac{1}{2}}\int_{y = \frac{1}{2}}^1\frac{3}{2}(x^2 + y^2)dydx &=\int_{x=0}^{\frac{1}{2}}\frac{3}{2}x^2y + \frac{1}{2}y^3\Big|_{y = \frac{1}{2}}^1\\
&=\int_{x=0}^{\frac{1}{2}}\frac{3}{4}x^2 + \frac{7}{16}\\
&=\frac{1}{4}x^3 + \frac{7}{16}x\Big|_{x = 0}^{\frac{1}{2}}\\&=\frac{1}{4}\end{aligned}$$

## (c)
**$P(\frac{1}{4}< X<\frac{3}{4})$**

$$\begin{aligned}
\int_{x=\frac{1}{4}}^{\frac{3}{4}}\int_{y = 0}^{1}\frac{3}{2}(x^2 + y^2)dydx &= \int_{x=\frac{1}{4}}^{\frac{3}{4}}\frac{3}{2}x^2y +\frac{1}{2}y^3\Big|_{y = 0}^{1}dx\\
&=\int_{x=\frac{1}{4}}^{\frac{3}{4}}\frac{3}{2}x^2+\frac{1}{2}dx\\
&=\frac{1}{2}x^3 + \frac{1}{2}x\Big|_{x=\frac{1}{4}}^{\frac{3}{4}}\\
&=\frac{75}{128} -\frac{17}{128}\\
&=\frac{29}{64}
\end{aligned}$$

## (d)
$P(y<\frac{1}{2})$

$$\begin{aligned}
\int_{y = 0}^{\frac{1}{2}}\int_{x = 0}^1\frac{3}{2}(x^2 + y^2)dxdy &=\int_{y = 0}^{\frac{1}{2}}\frac{1}{2}x^3 + \frac{3}{2}y^2x\Big|_{x = 0}^1dy\\
&=\int_{y = 0}^{\frac{1}{2}}\frac{1}{2} +\frac{3}{2}y^2dy\\
&=\frac{1}{2}y + \frac{1}{2}y^3\Big|_{y=0}^{\frac{1}{2}}\\
&=\frac{5}{8}
\end{aligned}$$

## (e)

**whether X and Y are independent**

$$\begin{aligned}
f_X(x) &= \int_{y=0}^1\frac{3}{2}(x^2 + y^2)dy \\
&=\frac{1}{2}x^3 +\frac{3}{2}y^2x\Big|_{y =0}^1\\
&=\frac{1}{2}x^3 + \frac{3}{2}x\\
\end{aligned}$$

similarly $f_Y(y) = \frac{1}{2}y^3 + \frac{3}{2}y$

but notice that 
$$\begin{aligned}
f_X(x)f_Y(y) &= (\frac{1}{2}x^3 + \frac{3}{2}x)(\frac{1}{2}y^3 + \frac{3}{2}y)\\
&= (\frac{1}{4}x^3y^3 + \frac{3}{4}xy^2 + \frac{3}{4}x^2y + \frac{9}{4}xy)\\
&\neq\frac{3}{2}(x^2 + y^2)\\
&=f(x,y)
\end{aligned}$$

therefore they are not independent


## 5
(assessed)

**Let X and Y be continuous random variables**

## (a)

**Show that $P(X<Y + 1) = \int_{-\infty}^{\infty}P(X<y+1|Y = y)f_Y(y)dy$**

since y is a continuous random variable

following the total probability law

$$P(E) = \sum_{i}P(E|F_i)P(F_i)$$
therefore, 

$$\begin{aligned}P(X<Y+1) &= \sum P(X<y+1|Y=y)P(Y = y) &(\forall y\in(-\infty,\infty))\\
&=\int_{-\infty}^{\infty}P(X<y+1|Y=y)P(Y=y)dy\\
&=\int_{-\infty}^{\infty}P(X<y+1|Y = y)f_Y(y)dy\end{aligned}$$

## (b)

**Hence or otherwise, if X and Y are $Exp(\lambda)$ and $N(0,1)$ respectively and independent, give an expression for the probability that $X<Y+1$. Your answer need to hold for any value of $\lambda$ and show the details of the derivations**

since $X\sim Exp(\lambda)$, $f_X(x) = \begin{cases}\begin{array}{c}\lambda e^{-\lambda x} &x\ge 0\\0 & \text{otherwise}\end{array}\end{cases}$

and since $Y\sim N(0,1)$ $f_Y(y) =\frac{1}{\sqrt{2\pi}}e^{-\frac{y^2}{2}}$


so (and since $X\sim Exp(\lambda)$ is only meaningful for $x\ge 0$, given that $Y=y$)

$$\begin{aligned}
P(X<y+1|Y = y) &= \int_{0}^{y+1}f_X(x)dx\\
&=\int_{0}^{y+1}\lambda e^{-\lambda x}dx\\
&=-\int_{-\lambda x = 0}^{-\lambda(y+1)}e^{\lambda x}d(-\lambda x)\\
&=-e^{-\lambda x}\Big|_{-\lambda x=0}^{-\lambda(y+1)}\\
&=1-e^{-\lambda(y+1)}
\end{aligned}$$
and 0 if x is less than 0, obviously

therefore, using the lemma we proved in (a)

and also for x to be greater than 0, the lower bound of y should be -1

$$\begin{align}
P(X<Y+1) &= \int_{-\infty}^{\infty}P(X<y+1|Y=y)f_Y(y)dy\\
&= \int_{-1}^{\infty}P(X<y+1|Y=y)f_Y(y)dy\\
&= \int_{-1}^{\infty}(1-e^{-\lambda(y+1)})(\frac{1}{\sqrt{2\pi}}e^{-\frac{y^2}{2}})dy\\
&=\int_{-1}^{\infty}(\frac{1}{\sqrt{2\pi}}e^{-\frac{y^2}{2}} - \frac{1}{\sqrt{2\pi}}e^{-\frac{y^2}{2}-\lambda(y+1)})dy\\
&=\int_{-1}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-\frac{y^2}{2}}dy - \int_0^{\infty}\frac{1}{\sqrt{2\pi}}e^{-\frac{y^2}{2}-\lambda(y+1)}dy\\ \\& (\text{since the first term is in the form of a normal distribution pdf})\\
&= \Big(\int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-\frac{y^2}{2}} - \int_{-\infty}^{-1}\frac{1}{\sqrt{2\pi}}e^{-\frac{y^2}{2}}\Big) - \int_0^{\infty}\frac{1}{\sqrt{2\pi}}e^{-\frac{y^2}{2}-\lambda(y+1)}dy\\
&= \Big(1 - \Phi(-1)\Big)-\int_0^{\infty}\frac{1}{\sqrt{2\pi}}e^{-\frac{y^2}{2}-\lambda(y+1)}dy\\
&\Big(\text{the integral from }-\infty \text{ to } \infty\text{ of a normal distribution pdf is 1}\\
&\qquad\text{and}\\
&\int_{-\infty}^{-1}\phi(x)dx = \Phi(-1)\Big)\\
&=\Phi(1) - e^{-\lambda+\frac{\lambda^2}{2}}\int_{-1}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-\frac{y^2}{2} -\lambda y - \frac{\lambda^2}{2}}dy\\
&\Big(\Phi(x) = 1 - \Phi(-x)\text{ as in the lectures}\Big)\\
&=\Phi(1) - e^{-\lambda+\frac{\lambda^2}{2}} \int_{-1}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-\frac{(y +\lambda)^2}{2}}dy\\
&=\Phi(1) - e^{-\lambda+\frac{\lambda^2}{2}}\int_{-1 +\lambda}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-\frac{z^2}{2}}dz \\& (\text{substituting } y+\lambda \text{with }z)\\
&= \Phi(1) - e^{-\lambda+\frac{\lambda^2}{2}}(\int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-\frac{z^2}{2}}dz - \int_{\infty}^{-1+\lambda}\frac{1}{\sqrt{2\pi}}e^{-\frac{z^2}{2}}dz)\\
&=\Phi(1) - e^{-\lambda+\frac{\lambda^2}{2}}(1-\Phi(-1+\lambda))\\
&=\Phi(1) - e^{-\lambda+\frac{\lambda^2}{2}}\Phi(1-\lambda)\\
\end{align}$$


I don't think we should decompose any further, $\Phi(1)$ is a constant and $\Phi(1-\lambda)$ depends on $\lambda$, unrolling them gives another nasty expression with the normal distributions.

and also, the domain of $\Phi$ is $\mathbb{R}$ or $(-\infty, \infty)$, therefore, $\lambda$ can take any values in $\mathbb{R}$

## (c) 
**Assume in this part that $\lambda = 1$, i.e. X and Y+1 have the same mean. Show that this implies for the result obtained in part (b) that $P(X<Y+1) = \Phi(1) - \frac{1}{2\sqrt{e}}$**


since $\lambda = 1$

substituting this in the expression we obtained in (b) gives

$$\begin{aligned}
P(X<Y+1) &= \Phi(1) - e^{-1 + \frac{1}{2}} \Phi(0)\\
&=\Phi(1) - \frac{1}{\sqrt{e}}\frac{1}{2}\\
&=\Phi(1) - \frac{1}{2\sqrt{e}}
\end{aligned}$$

# 6

## (a)
**Let $N_x$ be the number of events generated by a Poisson process with rate $\mu$ in a time period of length x and Let $T_n$ be the time elapsed between an event and the nth one after it. Using a logically reasoned argument, show that $T_n\le x\iff N_x\ge n$**

$T_n\le x$ if and only if the nth arrival occurs before time x. But the nth arrival occurs before time x if and only if $N_x$ is at least n or $N_x \ge n$

## (b)

**Hence prove that $P(T_n\le x) = 1 - e^{-\mu x}\sum_{k=0}^{n-1}\frac{(\mu x)^k}{k!}$**

following the conclusion of (a)

$$\begin{aligned}
P(T_n\le x) = P(N_x\ge n) &= 1 - P(N_x<n)\\
&= 1 - \sum_{k=0}^{n-1}Poi(\mu)\\
&= 1 - \sum_{k=0}^{n-1}\frac{(\mu x)^k e^{-\mu x}}{k!}\\
&= 1 - e^{-\mu x}\sum_{k=0}^{n-1}\frac{(\mu x)^k}{k!}
\end{aligned}$$

## (c)

**The time, in minutes, elapsed between two consecutive red buses arriving at a bus top is an exponential random variable with parameter $\lambda$, t.e. with pdf $f_R(t) = \lambda e^{-\lambda t}$ for $t\ge 0$, 0 otherwise. Green buses on the other hand always stop for a 5-minute break shortly before the bus stop; hence their inter-arrival time has pdf $f_G(t) = \mu e^{-\mu(t-5)}$ for $t\ge 5$, 0 otherwise. You arrive at the bus top, just missing a green bus. What is the probability the the next bus to arrive will be red? State clearly any assumptions you make**

So currently we are just missing a green bus

for the next bus to be red (assuming no other buses except red and green)

assumption:

- the question means I only missed one green train  since t = 0
- green train and red trains are independent

so the answer is just $P(R\le G)$

skipping the calculation here

# 7.
**A professor travels to work by train, with scheduled arrival time at Victoria 08:00 hours. The train is usually late, arriving at time 08:05+5Z minutes, where Z is a Standard Normal random variable. If the train arrives before 08:00 (i.e. Z < −1), the professor walks to work but is usually distracted on the way, so that he always arrives at work late, by X minutes, where X is an exponential random variable with mean 10. Otherwise, he takes the tube but stops off for breakfast, so that he is again always late, by Y minutes, where Y is an exponential random variable with mean 20**

## (a)

case 1: Z < -1 and X > m
case 2: Z >= -1 and Y > m

so 

$$\begin{aligned}
&\qquad\Phi(-1)P(X > m) + (1-\Phi(-1))P(Y > m)\\
&=\Phi(-1)(1-P(X\le m)) + (1-\Phi(-1))(1-P(Y\le m))\\
&=\Phi(-1)(1-\int_{-\infty}^m Exp(\frac{1}{10})) + (1-\Phi(-1))(1-\int_{-\infty}^mExp(\frac{1}{20}))


\end{aligned}$$


## (b)

Z < -7

$\Phi(-7) = 1.28\times 10^{-12}$

