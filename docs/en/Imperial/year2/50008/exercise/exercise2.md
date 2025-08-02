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

# 1.
**An experiment involves tossing two unbiased coins.**

## (a) 
**What is the sample space of this experiment?**

$\mathbf{S} = \{(H,H),(H,T),(T,H),(T,T)\}$

where H is for Heads and T for Tails

## (b) 
**What is the probability mass function of the random variable X, which takes value 2 if two heads show, 1 if one head shows, and 0 if no heads show?**


$f(X)=\begin{cases}\begin{array}{c}\frac{1}{4} & \text{X = 2}\\\frac{1}{2} & \text{X = 1}\\\frac{1}{4} & \text{X = 0}\\\end{array}\end{cases}$

## (c) 
**What is the probability mass function of the random variable Y, which takes the value 3 if at least one head shows and 1 if no head shows?**

$f(Y)=\begin{cases}\begin{array}{c}\frac{1}{4} & \text{Y = 1}\\\frac{3}{4} & \text{Y = 3}\end{array}\end{cases}$

# 2. 
**Suppose that two fair dice are thrown and define a random variable X as the total number of spots showing. Make a table showing the probability mass function, p(x) of X and plot a graph of p(x)**

|x|2|3|4|5|6|7|8|9|10|11|12|
|-|-|-|-|-|-|-|-|-|-|-|-|
|p(x)|1/36|1/18|1/12|1/9|5/36|1/6|5/36|1/9|1/12|1/18|1/36|

# 3.
**In tossing a fair coin four times, what is the probability that one will obtain**

## (a) 
**four heads;**

$0.5 ^ 4 = 0.0625$

## (b) 
**three heads;**

$4 * (0.5^4) = 0.25$

## (c) 
**at least two heads;**

$P((a)) + P((b)) = 0.0625 + 0.25 = 0.3125$

$\color{red} P(a) + P(b) + P(2) = 0.375 + 0.0625 + 0.25 = 0.6875$
 
## (d) 
**not more than one head?**

$P(\text{one head}) + P(\text{no head}) = 4 * (0.5)^4 + 0.5 ^ 4 = 0.3125$
 
# 4. 
**An urn holds 5 white and 3 black marbles.**

## (a) 
**If two marbles are drawn at random without replacement and X denotes the number of white marbles**

### i. 
**find the probability mass function of X, and**

$\begin{array}X & 0 & 1 & 2\\P(X) & \frac{3}{8}\times\frac{2}{7} = \frac{3}{28} & \frac{5}{8}\times\frac{3}{7} +\frac{3}{8}\times\frac{5}{7}= \frac{15}{28} & \frac{5}{8}\times\frac{4}{7} =\frac{5}{14}\end{array}$

### ii.
**plot the cumulative distribution function of X.**

$\begin{array}X & 0 & 1 & 2 & 3\\P(X) & \frac{3}{28} & \frac{9}{15} & 1\end{array}$

## (b) 
**Repeat 4a if the marbles are drawn with replacement.**

### i. 
**find the probability mass function of X, and**

$\begin{array}X & 0 & 1 & 2\\P(X) & \frac{3}{8}\times\frac{3}{8} = \frac{9}{64} & \frac{5}{8}\times\frac{3}{8} +\frac{3}{8}\times\frac{5}{8}= \frac{15}{32} & \frac{5}{8}\times\frac{5}{8} =\frac{25}{64}\end{array}$

### ii.
**plot the cumulative distribution function of X.**

$\begin{array}X & 0 & 1 & 2 & 3\\P(X) & \frac{9}{64} & \frac{39}{64} & 1\end{array}$


# 5. 
**The probability that a student will pass a particular course is 0.4. Find the probability that, out of 5 students**

## (a) 
**none pass;**

$0.6^5 = 0.07776$

## (b) 
**one passes;**

$5 * 0.6^5 = 0.3888$

$\color{red} 5 * 0.4 * 0.6^4 = 0.26$
## (c) 
**at least one passes**

$1 - 0.6^5 = 0.92224$

# 6. 
## (a) 
**If each student in a class of 110 has the same probability, 0.8, of passing an examination, what is**

### i. 
**the expected number of passes?**

110 * 0.8 = 88

### ii. 
**the standard deviation of the number of passes?**

following the formula in lectures $\sigma = \sqrt{np(1-p)} = \sqrt{110 * 0.8 * 0.2} = \sqrt{17.6}\approx 4.2$


## (b) 
**If each student in a college of 11000 has the same probability of graduating, what is**
### i. 
**the expected number of graduates?**
11000 * 0.8 = 8800

### ii. 
**the standard deviation of the number of graduates?**

following the formula in lectures $\sigma = \sqrt{np(1-p)} = \sqrt{11000 * 0.8 * 0.2} = \sqrt{1760}\approx 42$

# 7. 
**An insurance salesman sells policies to 5 computer companies. The probability that each of these companies will make a claim over the next five years is $\frac{1}{5}$. Find the probability that, over the next five years**
## (a) 
**all companies will claim;**

$\frac{1}{5^5} = \frac{1}{3125}$

## (b) 
**at least three companies will claim;**

$\frac{\begin{matrix}3\\5\end{matrix}* 1^3*4^2+\begin{matrix}4\\5\end{matrix}* 1^4*4^1+\begin{matrix}5\\5\end{matrix}* 1^5 }{5^5} = \frac{181}{3125}$
## (c) 
**only two will claim;**

$\frac{\begin{matrix}2\\5\end{matrix}* 1^2*4^3}{5^5} = \frac{640}{3125}$
## (d) 
**at least one will not claim**

$1-\frac{4^5}{3125} = 1-\frac{1024}{3125} = \frac{2001}{3125}$

# 8. 
**Compute the mean, standard deviation, and the skewness for the following binomial distributions, and comment on the result**

## (a)
**Binomial(100,0.9)**

- mean:90.0
- std:3.0
- skew:-0.27

## (b)
**Binomial(100,0.7)**

- mean:70.0
- std:4.58
- skew:-0.09

## (c)
**Binomial(100,0.5)**

- mean:50.0
- std:5.0
- skew:0.0

## (d)
**Binomial(1000,0.9)**

- mean:900.0
- std:9.49
- skew:-0.08

## (e)
**Binomial(1000,0.7)**

- mean:700.0
- std:14.49
- skew:-0.03

## (f)
**Binomial(1000,0.5)**

- mean:500.0
- std:15.81
- skew:0.0

#  9. 
**In a box of 500 partly used batteries from 3 different laboratories that need very high reliability, it is estimated that:**

- **300 have probability 0.9 of working adequately;**
- **150 have probability 0.5 of working adequately;**
- **50 have probability 0.4 of working adequately.**

**Each laboratory produces each type of battery. Assuming batteries from each laboratory are independent, what are the mean and standard deviation of the number of adequate batteries in the box?**

lab 1: Binomial(300,0.9)
- mean:270.0
- std:5.2
- skew:-0.15


lab 2: Binomial(150,0.5)
- mean:75.0
- std:6.12
- skew:0.0


lab 3: Binomial(50,0.4)
- mean:20.0
- std:3.46
- skew:0.06

# 10. 
**In a class of 20 students taking an examination,**

- **2 have probability 0.4 of passing;**
- **4 have probability 0.6 of passing;**
- **5 have probability 0.7 of passing;**
- **7 have probability 0.8 of passing;**
- **2 have probability 0.9 of passing.**
## (a) 
**What is the expected number of passes?**

this is a combination of 5 binomials, the events are all independent

so:

Binomial(2,0.4)

- mean: 0.8
- std: 0.69
- skew: 0.29


Binomial(4,0.6)

- mean: 2.4
- std: 0.98
- skew: -0.2


Binomial(5,0.7)

- mean: 3.5
- std: 1.02
- skew: -0.39


Binomial(7,0.8)

- mean: 5.6
- std: 1.06
- skew: -0.57


Binomial(2,0.9)

- mean: 1.8
- std: 0.42
- skew: -1.89


Combined Metrics:
Total Mean: 14.1
Total Variance: 3.79
Total Standard Deviation: 1.95
Combined Skewness: -0.55


## (b) 
**What is the standard deviation of the number of passes?**

in (a)

# 11. 
**(Geometric distribution.)**
**A computer class has a limited number of terminals available for use. A student notices that, on average, there is a 0.4 chance that there will be a free terminal each time he tries to use a machine.**
## (a) 
**What is the average number of times he will have to try use a machine until he is successful?**

1/0.4 = 2.5

## (b) 
**What is his chance of being successful the first time he tries?**

0.4

## (c) 
**What is his probability of being successful the first time on each of three different occasions**

$0.4^3 = 0.064$

# 12
## (a)
**What is the mean and variance of a sum of n independent Bernoulli random variables, each with parameter p**

mean: np

varaince: np(1-p)

## (b) 
**What if they have different parameters $(p_1,p_2,\dots, p_n)$**

mean: $\sum_{i=1}^n p_i$

variance: $\sum_{i=1}^n p_i*(1-p_i)$


## (c)
**What can you say if I now tell you that they are not independent**

Wow

they the combine metrics are unknown

# 13. 

**Molly the dog is very particular about her food, so she created a start-up to make cartons of her favourite food, which she called MollyBix. These cartons are produced in three plants, in Lancashire, Derbyshire and Yorkshire, and supplied to customers through various distribution centres. MollyBix production is not an exact science, and not every carton is approved by Molly. She likes 95%, 40% and 25% of the MollyBix made in Lancashire, Derbyshire and Yorkshire, each plant of which produces 50%, 20% and 30% of cartons, respectively. Molly’s food-orders come in boxes of 500 cartons that are sourced randomly from all three plants.**

## (a) 
**If a carton of MollyBix is selected at random from a box, what is the probability that Molly will like it?**

95% * 50% + 40% * 20% + 25% * 30% = 47.5% + 8% + 7.5% = 63% = 0.630

## (b) 
**Molly doesn’t like a randomly selected carton. What are the probabilities that it was produced at each of the plants?**

$P(\text{Lancashire}|\text{doesnt like}) = \frac{P(\text{Lancashire}\cap\text{doesnt like})}{P(\text{doesnt like})} = \frac{(1-95\%) *50\%}{1-63\%} = \frac{5}{74} = 0.0676$

$P(\text{Derbyshire}|\text{doesnt like}) = \frac{P(\text{Derbyshire}\cap\text{doesnt like})}{P(\text{doesnt like})} = \frac{(1-40\%) *20\%)}{1-63\%} = \frac{12}{37} = 0.324$

$P(\text{Yorkshire}|\text{doesnt like}) = \frac{P(\text{Yorkshire}\cap\text{doesnt like})}{P(\text{doesnt like})} = \frac{(1-25\%) *30\%}{1-63\%} = \frac{45}{74} = 0.608$

## (c) 
**In a particular box, assume that the numbers of cartons produced at each plant are exactly in proportion to the production percentages given, e.g. 250 were produced at the Lancashire plant. What are the expectation and standard deviation of the number of cartons in the box that Molly will like? (Hint: Let Xi be the number of cartons that Molly likes out of those produced at plant i. Model Xi as a Binomial distribution.)**

so this a combination of 3 binomial distributions

### Lancashire:
Binomial(250,0.95)
- n = 250, p = 0.95
- mean: $E(X_{\text{Lancashire}}) = np = 250 * 0.95 = 237.5$
- variance: $Var(X_{\text{Lancashire}}) = np(1-p) = 250 * 0.95*(1-0.95) = 11.875$

### Derbyshire
Binomial(100,0.4)
- n = 100, p = 0.4
- mean: $E(X_{\text{Derbyshire}}) = np = 100 * 0.4 = 40.0$
- variance: $Var(X_{\text{Derbyshire}}) = np(1-p) = 100 *0.4 * 0.6 = 24$


### Yorkshire
Binomial(150,0.25)
- n = 150, p = 0.25
- mean: $E(X_{\text{Yorkshire}}) = np = 150 * 0.25 = 37.5$
- variance: $Var(X_{Yorkshire}) = np(1-p) = 150 * 0.25 * 0.75 = 28.125$
- skew: 0.09

### combined

since the events of the three places are obviouly independent

we denote $S_X$ as the three events combined
$E(S_X) = E(X_{\text{Lancashire}}) + E(X_{\text{Derbyshire}}) + E(X_{\text{Yorkshire}}) = 237.5 + 40.0 + 37.5 = 315$
$Var(S_X) = Var(X_{\text{Lancashire}}) + Var(X_{\text{Derbyshire}}) + Var(X_{\text{Yorkshire}}) = 11.875 + 24 + 28.125 = 64  = \sigma(S_X)^2$
so $\sigma(S_X) = \sqrt{Var(S_X)} = \sqrt{64} = 8$

# 14.
**A network consists of the links shown in the diagram below. Each node represents a router.The directed edges indicate the links that a packet can use between each node pair. Consider a packet that needs to traverse the network from A to B. Each edge is annotated with the probability hij that the link $i \to j$ is healthy, e.g., $H_{AD} = 0.75$. Links fail independently of each other. A path is said to be faulty if there exist at least one faulty link along the path. A path without faulty links is said to be healthy. Compute the probability that there exist at least a healthy path between node A and node B. Detail and justify your steps. (Hint: consider first the same question for the two sub-paths that start from C)**

then 

$\begin{aligned}P(\text{faulty }CEB) &= 1 - P(\text{healthy }CEB)\\&=1 - H_{CE} * H_{EB} \\&= 1 - 0.8 * 0.9 \\&= 0.28\end{aligned}$

$\begin{aligned}P(\text{faulty }CFB) &= 1 - P(\text{healthy }CFB)\\&=1 - H_{CF} * H_{FB} \\&= 1 - 0.85 * 0.95 \\&= 0.1925\end{aligned}$

therefore

$\begin{aligned}P(\text{at least one healthy path between }C\text{ and }B) &= 1 - P(\text{faulty }CB)\\&= 1 - P(\text{faulty }CEB\cap\text{faulty }CFB)\\&=1 - P(\text{faulty }CEB)*P(\text{faulty }CFB)\\&=1 - 0.28*0.1925\\&=0.9461\end{aligned}$
and

$\begin{aligned}P(\text{faulty }ACB) &=1 - P(ACB)\\&=1 - P(AC) * P(\text{at least one healthy path in }CB)\\&=1 - 0.9 * 0.9461\\&= 0.14851\end{aligned}$

$\begin{aligned}P(\text{faulty }ADB) &= 1 - P(ADB)\\&= 1 - H_{AD}*H_{DB}\\&=1 - 0.75 * 0.95\\& = 0.2875\end{aligned}$


therefore,

$\begin{aligned}P(\text{at least one healthy path in }A\text{ and }B) & = 1 - P(\text{no healthy path between }A\text{ and }B)\\&=1 - P(\text{faulty }ACB\cap \text{faulty }ADB)\\&=1- 0.14851* 0.2875\\&=0.957\end{aligned}$

in conclusion, the probability that there is at least one healthy path between A and B is 0.957 or 95.7%