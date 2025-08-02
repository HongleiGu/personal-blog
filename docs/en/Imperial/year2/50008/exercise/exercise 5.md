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
# 1

**Suppose to draw five times with replacement from a deck of cards. What is the probability of drawing 2 spades, 1 heart, 1 diamond and 1 club?**

$\frac{(C_{13}^1)^3 C_{13}^2A_5^5}{52*51*50*49*48}$

<span style="color: red">Using the multinomial distribution</span>

$\color{red}p(n_1,\dots, n_r) = P_z(X_1 = n_1,\dots, X_r = n_r) = \frac{n!}{\prod n_i!} \prod q_i^{n_i}$

$\color{red}p(\spadesuit) = \frac{1}{4}, p(\heartsuit) = \frac{1}{4}, p(\diamondsuit) = \frac{1}{4}, p(\clubsuit)=\frac{1}{4}$

<span style="color:red">therefore, we have</span>

$\color{red}\begin{aligned}&P(X_1 = 2, X_2 = 1, X_3 = 1, X_4 = 1) \\=& \frac{5!}{2!1!1!1!}p(\spadesuit)^2p(\heartsuit)p(\diamondsuit)p(\clubsuit) \\=& 60(0.25)^4 = 0.05859\end{aligned}$


# 2.

**Suppose that whether or not it rains today probabilistically depends on previous weather conditions through the last three days**

## (a)
**Propose a discrete time Markov chain to analyse this system. What is the cardinality of the state space**

since the weather today depends on the weather of the past three days, so the state space is all the possiblity of the past three days combined, which is $2^3 = 8$

## (b)
**Suppose that if it has rained for the past three days, then it will rain today with probability 0.8; if it did not rain for any of the past three days, then it will rain today with probability 0.2; and in any other case the weather today will with probability 0.6, be the same as the weather yesterday. Determine the transition matrix R**

let 0 denote that on this day it did not rain, and 1 for rains, the the triplet (a,b,c) symbolise the state of the past three days

we know that 

$$\begin{cases}(1,1,1)\to\begin{cases}\begin{array}{c}1 & p=0.8\\0 & p = 0.2\end{array}\end{cases}\\(0,0,0)\to\begin{cases}\begin{array}{c}1 & p=0.2\\0 & p = 0.8\end{array}\end{cases}\\\text{otherwise}(a,b,c)\to c\end{cases}$$

so the matrix is 
<table>
  <tr>
    <td>
      <table>
        <tr>
          <th></th>
          <th>(0,0,0)</th>
          <th>(0,0,1)</th>
          <th>(0,1,0)</th>
          <th>(0,1,1)</th>
          <th>(1,0,0)</th>
          <th>(1,0,1)</th>
          <th>(1,1,0)</th>
          <th>(1,1,1)</th>
        </tr>
        <tr>
          <th>(0,0,0)</th>
          <td>0.8</td>
          <td>0.2</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>(0,0,1)</th>
          <td>0.4</td>
          <td>0.6</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>(0,1,0)</th>
          <td>0</td>
          <td>0</td>
          <td>0.6</td>
          <td>0.4</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>(0,1,1)</th>
          <td>0</td>
          <td>0</td>
          <td>0.4</td>
          <td>0.6</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>(1,0,0)</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0.6</td>
          <td>0.4</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>(1,0,1)</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0.4</td>
          <td>0.6</td>
          <td>0</td>
          <td>0</td>
        </tr>
        <tr>
          <th>(1,1,0)</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0.6</td>
          <td>0.4</td>
        </tr>
        <tr>
          <th>(1,1,1)</th>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0</td>
          <td>0.2</td>
          <td>0.8</td>
        </tr>
      </table>
    </td>
  </tr>
</table>



# 3.

**Three political parties have 30%, 50%, 20% of the votes. If you reach on the phone 10 adults, what is the probability that they support the political parties in the same proportions**

so in the 10 adults we need 3 support party A, 5 for party B, 2 for party C

$p(A) = 0.3 p(B) = 0.5 p(C) = 0.2$

so using the multinomial distribution

$p(X_1 = 3, X_2 = 5, X_3 = 2) = \frac{10!}{3!5!2!}p(A)^3p(B)^5p(C)^2 = \frac{10!}{144}0.027*0.3125*0.04 = 0.0851$

# 4.

A Markov chain ${X_n,n\ge 0}$ with state space $S = \{0,1,2\}$ has the transition probability matrix

$$R = \begin{bmatrix}\frac{3}{5} & \frac{2}{5} & 0\\\frac{2}{5} & \frac{2}{5} & \frac{1}{5}\\0 & \frac{2}{5} & \frac{3}{5}\end{bmatrix}$$

## (a)
**Knowing that $\pi_{00} = \pi_{01} = \frac{1}{4}$, find the expected value $E[X_n]$ a t time n=2**

since $||\pi_0||_1 = 1$ so $\pi_{02} = \frac{1}{2}$

so we can get 

$$\begin{aligned}\pi_2 &= \pi_0R^2 \\&= \begin{bmatrix}\frac{1}{4} & \frac{1}{4} & \frac{1}{2}\end{bmatrix}\begin{bmatrix}\frac{13}{25} & \frac{10}{25} & \frac{2}{25}\\\frac{10}{25} & \frac{10}{25} & \frac{5}{25}\\\frac{4}{25} & \frac{10}{25} & \frac{11}{25}\end{bmatrix} \\&= \begin{bmatrix}\frac{31}{100} &\frac{40}{100} & \frac{29}{100}\end{bmatrix}\end{aligned}$$

so $E[X_n] = 0*\frac{31}{100} + 1 *\frac{40}{100} + 2 * \frac{29}{100} = 0.98$


## (b)

**State if the DTMC is irreducible, Then, determine the steady state equilibrium probability vector $\pi_{\infty}$ for this DTMC**

it is irreducible since for every pair $i,j$ $R_{ij}!= 0$

$\pi_{\infty} = \pi_{0}R^{\infty}$

so $\pi_{\infty} = \pi_{\infty}R$

assume $\pi_{\infty} =\begin{bmatrix}a & b & c\end{bmatrix}$

so we have 

$$\begin{cases}\begin{aligned}
\frac{3}{5}a + \frac{2}{5}b &=& a\\
\frac{2}{5}a + \frac{2}{5}b +\frac{2}{5}c &=& b\\
\frac{1}{5}b + \frac{3}{5}c &=& c\\

\end{aligned}\end{cases}$$

we have three sets of $[\frac{2}{5},\frac{2}{5},\frac{1}{5}]$ 

# 5.
**For the multinomial distribution with r outcomes, n trials, and probabilities $q_i$, Let $X_i$ denote the number of time outcome i occurs**

<span style="color:red">this and lecture5 - multinomial distribution needs to be revisited seriously,</span>

<ul style="color:red">
	<li>(a): definition of multinomial distribution (lecture5 - multinomial distribution)</li>
	<li>(b): expectation and variance of binomial distribution (lecture2 - binomial distribution)</li>
	<li>(c): linearity of expectation (lecture5 - linearity of expectation)</li>
	<li>(d): the same as (b) but need a bit twist</li>
</ul>

## (a) 

**Show that for $r = 2$ the multinomial distribution reduces to a binomial distribution**

following the definition of multinomial distribution

assume outcome 1 happens a times and outcome 2 happens b times, then $a+b =  n$

$$\begin{aligned}
P(X_1 = a, X_2 = b) &= \frac{n!}{a!b!}q_1^aq_2^b \\&=\frac{n!}{a!(n-a)!}q_1^aq_2^{n-a} \\&= \Big(\begin{matrix}a\\n\end{matrix}\Big)q_1^aq_2^{n-a}\end{aligned}$$

which is in the form of binomial distribution

## (b)

**Find $E[X_i]$ and $Var(X_i)$**

<span style="color:red">Each trial can be seen as a binomial distribution</span> $\color{red}Binomial(n,q_i)$

<span style="color:red">Therefore, the expectation and the variance are</span>

$\color{red}E[X_i]=nq_i,\color{red}Var[X_i] = nq_i(1-q_i)$


## (c)

**After the nth trial it is possible that some of the r outcomes did not occur at all. Let Y count the number of outcomes that did not occur bu the nth trail. Find $E[Y]$**

so this is the same, this can be considered as another combination of binomial distributions

 if let $Y_i$ be 1 if the outcome i does not occur in the n trials, then

$$\begin{aligned}
E\Big[\sum_{i=1}^r Y_i\Big] &= \sum_{i=1}^rE[Y_i]\\
&= \sum_{i=1}^rP(\text{outcome i does not occur})\\
&= \sum_{i=1}^r(1-q_i)^n
\end{aligned}$$


<span style="color:aquamarine">A small question: if from the reverse i it the same</span> 
 $\color{aqua} E[Y] = n - \sum_{i=1}^rE[X_i]$
 <span style="color:aquamarine">then we have</span> 
 $$\color{aqua}
 \begin{aligned}
 E[Y] &= n - \sum_{i=1}^r(q_i^{n} + q_i^{}\\
 &= ???
 \end{aligned}$$
 <span style="color:aquamarine">problem: the reverse is not E[X_I] but when the outcome occur at least once</span> 
 

## (d)
**Give an expression for $P(X_1+\dots+X_k)$ for $k<r$**

so this is equivalent to a binomial pmf where the probability of success is $q_1 +\dots + q_k$, $P(X_1+\dots + X_k) = \Big(\begin{matrix}n\\m\end{matrix}\Big)(q_1+\dots+q_k)^m(q_{k+1}+\dots+q_r)^{n-m}$
# 6.
**An urn always contains 2 balls. Ball colors are red an blue. At each stage, a ball is randomly chosen and then replaced by a new ball, which with probability 0.8 is the same color, and with probability 0.2 is the opposite color, as the ball it replaces. Let $X_n$ be the number of red balls in the urn after the nth selection and subsequent replacement. If initially both balls are red, find the probability that the fifth ball selected is red**

there are 3 states in the DTMC that can model this scenarios

let us denote R for red and B for B, then according to the balls in the urn

$$R = \begin{array}{c|cc}
 & (R,R) & (R,B) & (B,B)\\
 \hline
(R,R) & 0.8 & 0.2 & 0\\
(R,B) & 0.1 & 0.8 & 0.1\\
(B,B) & 0 & 0.2 & 0.8\\
\end{array}$$

and $\pi_0 = \begin{bmatrix}1 & 0 & 0\end{bmatrix}$ since both balls are red initially

then $\pi_4 = \pi_0R^4 = \begin{bmatrix}\frac{1218}{2500} & \frac{1088}{2500} & \frac{194}{2500}\end{bmatrix}$

so the probability that the fifth selected ball is red is 

$\frac{1218}{2500} + \frac{1}{2}\frac{1088}{2500} = \frac{1762}{2500}$

# 7
**Consider an urn that contains initially two red balls and one green ball. At every time step you draw a ball at random. This is then put back into the urn and another ball of the same color is also added to the urn before the next draw. Assume that the experiment is stopped after 2 draws, when the urn contains 5 balls in total. Upon stopping, the urn is emptied and the experiment is restarted placing again two red balls and one green ball in the urn. You are asked to model this experiment using a DTMC.**

## (a):

**Define the state space S of this repeated experiment. Assume here and later that restarting takes a time step, i.e. you should make sure that the DTMC also visits states where the urn has 5 balls before restarting.**

for clarity and simplicity, we use the pair $(Red,Green)$ where $Red,Green\in\mathbb{R}$ to denote a state that the urn has R red balls and B green balls

the since initially we are in state (2,1), we assume that taking out one ball and put back and adding one additional ball is considered as one timestep, but according to the question, restarting takes another timestep

then we are able to notice the the number of each kind of balls would never be less that the initial state except just after emptying (taking out and put back does not decrease the number of balls, restarting resets the initial state, also, we assume that emptying does not take an extra timestep as the question implies)

the experiment stops when there is 5 balls in total and restarts with the state (2,1)

so the state space is (using the pair notation define above)

$S = \{(2,1),(2,2),(3,1),(2,3),(3,2),(4,1)\}$

there are only fsix possible states

## (b) 

**Give the transition probability matrix R and the initial probability vector $\pi_0$ for a DTMC that models the content of the urn over time**

so the experiment can be modelled by the following

$$\begin{cases}
\begin{array}{c}
(Red,Green) &\Rightarrow &(2,1) & (Red+Green=5), p = 1\\
(Red,Green) &\Rightarrow &(Red,Green+1) & (\text{when a green ball is chosen}, p=\frac{Green}{Red+Green})\\
(Red,Green) & \Rightarrow & (Red+1,Green) &(\text{when a blue ball is chosen}, p=\frac{Red}{Red + Green})\\
\end{array}
\end{cases}$$

therefore we can write out the probability matrix R 

(we order the states in the order of $(2,1),(2,2),(3,1),(2,3),(3,2),(4,1)$ for both rows and columns in the matrix, so for example, $R_{11}$ denotes the probability of state $(2,1)$ to state $(2,1)$)

$$R = \begin{bmatrix}
0 & \frac{1}{3} & \frac{2}{3} & 0 & 0 & 0\\
0 & 0 & 0 & \frac{1}{2} & \frac{1}{2} & 0\\
0 & 0 & 0 & 0 & \frac{1}{4} &\frac{3}{4}\\
1 & 0 & 0 & 0 & 0 & 0\\
1 & 0 & 0 & 0 & 0 & 0\\
1 & 0 & 0 & 0 & 0 & 0\\
\end{bmatrix}$$

and since the initial state is (2,1)

therefore $\pi_0 = \begin{bmatrix}1 & 0 & 0 & 0 & 0 & 0\end{bmatrix}$

## (c)

**Let X be the number of red balls in the urn observed after the 2nd draw and immediately before emptying the urn, Calculate the probability P(X<4)**

so the probability of all the possible states after the 2nd draw is 

$$\begin{aligned}
\pi_2 &= \pi_0R^2 \\
&=  \begin{bmatrix}1 & 0 & 0 & 0 & 0 & 0\end{bmatrix}\Big(\begin{bmatrix}
0 & \frac{1}{3} & \frac{2}{3} & 0 & 0 & 0\\
0 & 0 & 0 & \frac{1}{2} & \frac{1}{2} & 0\\
0 & 0 & 0 & 0 & \frac{1}{4} &\frac{3}{4}\\
1 & 0 & 0 & 0 & 0 & 0\\
1 & 0 & 0 & 0 & 0 & 0\\
1 & 0 & 0 & 0 & 0 & 0\\
\end{bmatrix}\Big)^2\\
&=\begin{bmatrix}1 & 0 & 0 & 0 & 0 & 0\end{bmatrix}\Big(\begin{bmatrix}
0 & 0 & 0 & \frac{1}{6} & \frac{1}{3} & \frac{1}{2}\\
1 & 0 & 0 & 0 & 0 & 0\\
1 & 0 & 0 & 0 & 0 &0\\
0 & \frac{1}{3} & \frac{2}{3} & 0 & 0 & 0\\0 & \frac{1}{3} & \frac{2}{3} & 0 & 0 & 0\\0 & \frac{1}{3} & \frac{2}{3} & 0 & 0 & 0\\
\end{bmatrix}\Big)\\
&=\begin{bmatrix}
0 & 0 & 0 & \frac{1}{6} & \frac{1}{3} & \frac{1}{2}\end{bmatrix}
\end{aligned}$$

therefore $P(X<4) = P((2,1)) +P((2,2)) + P((3,1)) + P((2,3)) + P((3,2)) = 0 + 0 + 0 + \frac{1}{6} + \frac{1}{3} = \frac{1}{2}$
# 8.

**Consider a discrete-time Markov chain (DTMC) with initial probability vector $\pi_0 = (1,0,0,0)$ and transition probability matrix**

$$R = \begin{bmatrix}0 & 1 & 0 & 0\\0 & 0 & 1 & 0\\ 0 & 0 & 0 & 1\\a& 0 & 0&1-a\end{bmatrix}$$

## (a)
**without calculations, state which value of a would you choose to make $\pi_{\infty}^*$ uniformly distributed across the four states. Justify your answer**

a = 1

## (b)
**Assume in this part a = $\frac{1}{2}$. Let $X_n$ be the DTMC state at time $n\ge 0$. State if the DTMC is aperiodic and irreducible. Calculate the steady-state probability vector $\pi_{\infty}^*$**

$$R = \begin{bmatrix}0 & 1 & 0 & 0\\0 & 0 & 1 & 0\\ 0 & 0 & 0 & 1\\\frac{1}{2}& 0 & 0&\frac{1}{2}\end{bmatrix}$$


- the matrix indicate the DTMC is strongly connected, therefore irreducible
- the matrix indicate it is possible to visit a node infinite times, therefore not aperiodic

$\pi_{\infty}^*R = \pi_{\infty}^*$ and $\sum_i\pi_{\infty,i}^* = 1$

so 

$$\begin{aligned}
&\begin{bmatrix}
\pi_{\infty,1}^* &
\pi_{\infty,2}^* &
\pi_{\infty,3}^* &
\pi_{\infty,4}^*
\end{bmatrix} \\=& \begin{bmatrix}
\pi_{\infty,1}^* &
\pi_{\infty,2}^* &
\pi_{\infty,3}^* &
\pi_{\infty,4}^*
\end{bmatrix}
 \begin{bmatrix}0 & 1 & 0 & 0\\0 & 0 & 1 & 0\\ 0 & 0 & 0 & 1\\\frac{1}{2}& 0 & 0&\frac{1}{2}\end{bmatrix}\\
 =&\begin{bmatrix}\frac{1}{2}\pi_{\infty,4}^*&\pi_{\infty,1}^* & \pi_{\infty,2}^* & 
\pi_{\infty,3}^*+\frac{1}{4}\pi_{\infty,4}^*\end{bmatrix}
\end{aligned}$$
so $\pi_{\infty}^* = \begin{bmatrix}0.2 & 0.2 & 0.2 & 0.4\end{bmatrix}$

# 9.
**Consider a two-state homogeneous discrete-time Markov chain (DTMC). Let $X_i$be the state of DTMC at time t**

## (a)
**Give an expression for the conditional probability $P(X_t=i|X_{t+1} = j)$ that the DTMC was in state i at time t given that it was  observed to be in state j at time t+1**

$P(X_t = i|X_{t+1}=j) = \frac{P(X_t=i)P(X_{t+1}P(X_t = i) = j)}{P(X_{t+1} = j)}P(X_t = i) = \frac{r_{ij}}{P(X_{t+1} = j)}P(X_t = i)$

## (b)
**Consider now the limit $t\to\infty$. Using the last answer find $\lim_{t\to\infty}P(X_t = 2|X_{t+1} = 1)$ when the DTMC transition matrix is**

$$R = \begin{bmatrix}r_{11} & r_{12}\\r_{21} & r_{22}\end{bmatrix} = \begin{bmatrix}0.8 & 0.2\\0.3 & 0.7\end{bmatrix}$$

$\pi^{\infty}R = \pi^{\infty}$

so $\begin{bmatrix}\pi_{\infty,1} & \pi_{\infty,2}\end{bmatrix} \begin{bmatrix}0.8 & 0.2\\0.3 & 0.7\end{bmatrix}  = \begin{bmatrix}\pi_{\infty,1} & \pi_{\infty,2}\end{bmatrix}$

so $\pi_{\infty} = [0.6,0.4]$



$P(X_t = 2|X_{t_1} =1) = \frac{0.3*0.4}{0.6} = 0.2$