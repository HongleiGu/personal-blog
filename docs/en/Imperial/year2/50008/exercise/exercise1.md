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

**For two events F and E $\subseteq$, show that $P(E)\subset P(F)$**

since $E\subseteq F$, we take arbitrary event A such that $F \setminus A = E$

then $P(F) = P(E) + P(A) - P(E\cap A) \ge P(E) + P(A) - P(A) = P(E)$

therefore $P(E)\le P(F)$

modal answer:

replace E with $F\cap \overline{E}$ and remove the $P(E\cap A)$

since E is a subset of F, E and $F\cap \overline{E}$ are disjoint

$\begin{aligned}
P(F) &= P(E\cup (F\cap \overline{E}))\\
P(E) + P(F\cap \overline{E})\\
\ge P(E)
$

# 2.

**Suppose two events E and F are mutually exclusive. State the precise conditions under which they may also be independent.**

following the definition of mutualy exclusive, if E and F are mutually exclusive, then $E\cap F = \varnothing$

so $P(E\cap F) = P(\varnothing) = 0$

if E and F are also independent, then by definition $P(E\cap F) = P(E)P(F) = 0$

so at least one of $P(E), P(F)$ is 0, or in other word, at least one of E and F is $\varnothing$

# 3.
**What is the probability that a single roll of a die will give an odd number if**
## (a)
**no other information is given**

then sample space is $\mathbf{S} = \{1,2,3,4,5,6\}$

and the odd numbers are $\mathbf{E} = \{1,3,5\}$

under this setting, all the events are equally likely to happen

so $P(odd) = \frac{3}{6} = \frac{1}{2}$

## (b)
**you are told that the number is less than 4**

then the sample space if $\mathbf{S} = \{1,2,3,4\}$ (or $\{1,2,3\}$)

then odd number are $\mathbf{E} = \{1,3\}$

so $P(odd) = \frac{2}{4} = \frac{1}{2}$ (or $\frac{2}{3}$)

the brackets are because the question is unclear, whether it is $\le$ or $<$ (the latter)

# 4.
## (a)

**What's the probability of getting two sixes with two dice?**

The sample space is

$\begin{bmatrix}
(1,1) & (1,2) & (1,3) & (1,4) & (1,5) & (1,6)\\
(2,1) & (2,2) & (2,3) & (2,4) & (2,5) & (2,6)\\
(3,1) & (3,2) & (3,3) & (3,4) & (3,5) & (3,6)\\
(4,1) & (4,2) & (4,3) & (4,4) & (4,5) & (4,6)\\
(5,1) & (5,2) & (5,3) & (5,4) & (5,5) & (5,6)\\
(6,1) & (6,2) & (6,3) & (6,4) & (6,5) & (6,6)
\end{bmatrix}$

the valid event is $\{(6,6)\}$

under this setting all the events are equally likely to happen

so $P(\text{two 6}) = \frac{1}{36}$

## b
**What's the probability of getting a total of 3 with two dice?**

The sample space is

$\begin{bmatrix}
(1,1) & (1,2) & (1,3) & (1,4) & (1,5) & (1,6)\\
(2,1) & (2,2) & (2,3) & (2,4) & (2,5) & (2,6)\\
(3,1) & (3,2) & (3,3) & (3,4) & (3,5) & (3,6)\\
(4,1) & (4,2) & (4,3) & (4,4) & (4,5) & (4,6)\\
(5,1) & (5,2) & (5,3) & (5,4) & (5,5) & (5,6)\\
(6,1) & (6,2) & (6,3) & (6,4) & (6,5) & (6,6)
\end{bmatrix}$

the valid event is $\{(1,2),(2,1)\}$

under this setting all the events are equally likely to happen

so $P(\text{adds up to 3}) = \frac{2}{36} = \frac{1}{18}$

# 5.

**Two studetns try to solve a problem they've been set. Student A has a probability of $\frac{2}{5}$ of being able to solve the problem, and studetn B has a probability of $\frac{1}{3}$. If both try it independently, what is the probability of that problem is solved?**

by the definition of independence, $P(A\cap B) = P(A)P(B) = \frac{2}{5}\times\frac{1}{3} = \frac{2}{15}$

modal answer:

this solution is calculating the probability that both the student can solve the problem, actually we should do $1 - (1-\frac{2}{5})(1-\frac{1}{3}) = \frac{3}{5}$

# 6.

**A straight AB line of unit length is divided internally at a point X, where X is qually likely to be any poing of AB. Call AX and XB the lengths of the corresponding segments. What is the probability that $AX\bullet XB<\frac{3}{16}$**

since $AB = 1$

so assume $AX = x$, then $XB = 1 - x$

then $AX\bullet XB = x(1-x) = x - x^2\ <\frac{3}{16}$

so $\frac{1}{4} > x  \vee x > \frac{3}{4}$

so $P(AX\bullet XB>\frac{3}{16}) = \frac{\frac{1}{2}}{1} = \frac{1}{2}$

# 7.
## (a) 
**In one spin of a European roulette wheel (which has pockets numbered 0,1,2, up to and including 36) what is the probability that the outcome is odd?**

the sample space is $\mathbf{S} = \{1,2,3,\dots, 36\}$

and the event is $\mathbf{E} = \{1,3,5\dots,35, 37\}$

$P(odd) = \frac{18}{37}$

## (b)
**An urn contains x red balls and y green ones (both larger than 2). You remove them, without replacing them, one at a time. Answer each of the questions below assuming you cannot look at the colour of the balls you previously extracted**

### i.
**What is the chance that the first is red**

we only consider the first draw, the sample space is $\mathbf{S} = \{\underset{\text{x\times}}\text{red},\text{red},\dots,\text{red},\underset{\text{y times}}\text{green},\text{green},\dots,\text{green}\}$

then the Event is $\{\underset{\text{x times}}\text{red},\text{red},\dots,\text{red}\}$

so $P(\text{first red}) = \frac{x}{x+y}$

### ii.
**What is the chance that the second is red**

case 1: the first draw is red, then we have x-1 red balls and y green balls

so the probability is $\frac{x-1}{x+y-1}$

case 2: the first draw is green, then we have x red balls and y-1 green balls

so the probability is $\frac{x}{x+y-1}$

as we discussed case 1 has probability $\frac{x}{x+y}$

then case 2, the complement of case 1 has probability $\frac{y}{x+y}$

and in this case we assume the first draw and the second draw are independent

so the probability that the second is red is $\frac{x}{x+y}\frac{x-1}{x+y} + \frac{y}{x+y}\frac{x}{x+y-1} = \frac{x(x-1) + xy}{(x+y)(x+y-1)} = \frac{x}{x+y}$

# iii.
**what is the chance that the first two are red?**

this is the case1 in question2

# iv

**what is the chance that the last but one is red**

this is the case2 in question2

# 8.

## (a)

**An experiment consists of tossing a fair coin and rolling a fair die. What is the probability of the joint event ’heads with an odd number of spots’?**

the spots is only on the die, the coin and die is independent of each other, so $\frac{1}{4}$

## (b)

**In a particular class, 10% of the students were repeating the year. 60% of them passed the examination. For the remaining students, the pass rate was 80%. What percentage of the class passed the examination altogether?**

$P(\text{passed the exam}) = P(\text{pass rate}) + P(\text{repeating the year})\times P(\text{passed the examinations}) = 80\% * 90\% + 10\% * 60\% = 78\%$

# 9.

**On any day the chance of rain is %25 The chance of rain on two consecutive days is 10%**

## (a)

**Does this mean that the vents of rain on two consecutive days are independent or dependent events**

If the two event are independent, then $P(\text{first day rain}\cap \text{second day rain}) = P(\text{first day rain})P(\text{second day rain})$

but $10\% \neq 25\%\times 25\%$ so the two events are dependent

## (b)

**Given that it is rains today, what is the chance of rain tomorrow?**

the two events are independent, so the probability that it will rain tomorrow is 25%

modal answer:

$P(\text{tomorrow rain}|\text{today rain}) = \frac{0.1}{0.25} = 0.4$

## (c)

**Given that it will rain tomorrow, what is the chance of rain today?**

the same

# 10.

**A scientist leaves his umbrella behind with probability $\frac{1}{4}$ every time he visits a shop(and once he has left it, he does not collect it again)**

## (a)

**If he sets out with his umbrella to visit four different shops, what is the probability the he will leave it in the fourth shop?**

first of all, leaving the umbrella in each store is independent of the other, and leaving it in the fourth shop means he needs to remember bring it in the first three shops and left it in the last one

so the probability is $P(\text{umbrella in the fourth shop}) = P(\text{leave})^3 P(\text{remember}) = (1-25\%)^325\% = \frac{27}{256}$


## (b)

**If he arrives home without his umbrella, what is the probability that he left it in the fourth shop?**

$P(\text{left in fourth shop} | \text{arrives home without umbrella}) = \frac{P(\text{left in fourth shop})}{P(\text{arrives home without umbrella})} = \frac{\frac{27}{256}}{P(\overline{\text{remembers at all four shops}})} = \frac{\frac{27}{256}}{1 - P(\text{remembers})^4} = \frac{\frac{27}{256}}{1 - 75\%^4} = \frac{\frac{27}{256}}{\frac{{175}}{256}} = \frac{27}{175}$

## (c)

**If he arrives home without it, and was seen to be carrying it after leaving the first shop, what is the probability that he left it in the fourt h shop?**

the probability of him carrying the umbrella after the first shop and arrives home without it, we can see this as remembering in the first shop but forgot at one of the rest 3 shops and the events are independent

so $P(\text{remembers in first shop}\cap\text{forgot in the rest three}) = P(\text{remebers in first})P(\text{forgot in the rest three}) = P(\overline{forgot})P(\overline{\text{rememebers in all the three shops}}) = (1-25\%)(1 - 25\%^3) = (75\%)(\frac{37}{64}) = \frac{111}{256}$

then $P(\text{remembers in first shop}\cap \text{left in the fourth shop}) = P(\text{remember})^3P(\text{forgot}) = 75\%^3 25\% = \frac{27}{256}$

so the final probability is $\frac{27}{111} = \frac{9}{37}$

(for simplicity, the reast will just be written briefly)
# 11.

**A warehouse contains packs of electronic components. Forty percent of the packs contain components of low quality for which the probability that any given component will prove satisfactory is 0.8; forty percent contain components of medium quality for which this probability is 0.9; and the remaining twenty percent contain high quality components which are certain to be satisfactory.**

## (a) 
**If a pack is chosen at random and one component from it is tested, what is the probability that this component is satisfactory?**

40% * 0.8 + 40% * 0.9 + 20% = 88%


## (b) 

**If a pack is chosen at random and two components from it are tested, what is the probability that exactly one of the components tested is satisfactory?**

40% * 0.8 * 0.2 * 2 + 40% * 0.9 * 0.1 * 2 = 20%

## (c) 

**If it was found that just one of the components tested was satisfactory, what is the probability that the selected pack contained medium quality components?**

$\frac{40\% * 0.9}{88\%} = \frac{9}{22}$

(the question is unclear, this inherit the setting of (b), so we pick two items and one of them is satisfactory)

modal answer:

$\frac{2 * 0.9*0.1*0.4}{0.2}$
 
## (d) 
**If both components were found to be satisfactory, what is the probability that the selected pack contained high quality components?**

$\frac{20\%}{40\% * 0.8 * 0.8 + 40\% * 0.9 * 0.9 + 20\%} = \frac{50}{195} = \frac{10}{39}$

# 12.
**Prove that if $P(A) \ge P(B) > 0 then P(A|B) \ge P(B|A)$**

if $P(A)\ge P(B)>0$

then $P(A|B) = \frac{P(A\cap B)}{P(B)}$

then $P(B|A) = \frac{P(A\cap B)}{P(A)}$

if $P(A)\ge P(B)>0$

so $P(A|B)\ge P(B|A)$

# 13

**Show that if three events A, B, and C are independent, then A and B ∪C are independent.**

since A,B,C are independent,

so $P(B\cap C) = P(B)P(C)$

then $P(B\cup C) = P(B) + P(C) - P(B\cap C) = P(B) + P(C) - P(B)P(C)$

then $P(A\cap (B\cup C)) = P((A\cap B)\cup(A\cap C)) = P(A\cap B) + P(A\cap C) - P((A\cap B)\cap (A\cap C)) = P(A)P(B) + P(A)P(C) - P(A)P(B)P(C) = P(A)(P(B) + P(C) - P(B)P(C)) = P(A)P(B\cup C)$

so independent

# 14.
**The sample space S of a random experiment is given by S = {a,b,c,d}, with probabilities P({a}) = 0.2, P({b}) = 0.3, P({c}) = 0.4, P({d}) = 0.1. Let A denote event {a,b}, and B the event {b, c, d}. Determine the following probabilities:**

## (a)

**P(A)**

the element in the sample space are assumed to be disjoint

so $P(\{a,b\}) = P(\{a\})+P(\{b\}) = 0.2 + 0.3 = 0.5$

## (b)

**P(B)**

0.3 + 0.4 + 0.1 = 0.8

## (c)

**P(C)**

1 - P(A) = 0.5

## (d)

**$P(A\cup B)$**

$P(\{a,d,c,b\}) = 1$

## (e)

**$P(A\cap B)$**

$P(\{b\}) = 0.3$

# 15

**Two factories produce similar parts. Factory 1 produces 1000 parts, 100 of which are defective. Factory 2 produces 2000 parts, 150 of which are defective. A part is selected at random and found to be defective; what is the probability that it came from factory 1**

$P(\text{defective}) = \frac{100 + 150}{2000 + 1000} = \frac{250}{3000} = \frac{1}{12}$

$P(\text{defective}\cap A) = \frac{100}{2000 + 1000} = \frac{1}{30}$

so $P(A|\text{defective}) = \frac{12}{30} = \frac{2}{5}$

# 16

**In an experiment in which two fair dice are thrown, let A be the event that the first die is odd, let B be the event that the second die is odd, and let C be the event that the sum is odd. Show that events A, B, and C are pairwise independent, but A, B, and C are not jointly independent.**

## A and B:

$P(A) = 0.5, P(B) = 0.5, P(A\cap B) = \frac{3 * 3}{36} = 0.25 = P(A)P(B)$

## B and C:

$P(B) = 0.5, P(C) = \frac{3 * 3 + 3 * 3}{36} = 0.5, P(B\cap C) = \frac{3*3}{36} = 0.25 = P(B)P(C)$

## A and C:
the same

## A,B,C:

$P(A\cap B\cap C) = \frac{0}{36} = 0\neq P(A)P(B)P(C)$

# 17. 
**A company producing mobile phones has three manufacturing plants, producing 50, 30, and 20 percent respectively of its product. Suppose that the probabilities that a phone manufactured by these plants is defective are 0.02, 0.05, and 0.01 respectively.**
 
 
## (a) 
**If a phone is selected at random from the output of the company, what is the probability that it is defective?**

50% * 0.02 + 30% * 0.05 + 20% * 0.01 = 2.7%
## (b) 

**If a phone selected at random is found to be defective, what is the probability that it was manufactured by the second plant?**

$P(\text{defective}) = 2.7%$

$P(\text{defective} & \text{second plant}) = 30\% * 0.05 = 1.5\%$

so $P(\text{second plant}|\text{defective}) = \frac{1.5}{2.7} = \frac{5}{9}$
 
# 18. 

**In a gambling game called craps, a pair of dice is rolled and the outcome is the sum of the dice. The player wins on the first roll if the sum is 7 or 11 and loses if the sum is 2, 3, or 12. If the sum is 4, 5, 6, 8, 9, or 10, that number is called the players ’point’. Once the point is established, the rule is: If the player rolls a 7 before the point, the player loses; but if the point is rolled before a 7, the player wins. Compute the probability of winning in the game of craps**


$P(win) = P(\text{first win}) + (1-P(\text{first win}) -P(\text{first lose}))P(\text{points})$

$P(\text{first win}) = \frac{8}{36} = \frac{2}{9}$

$P(\text{first lose}) = \frac{4}{36} = \frac{1}{9}$

then for each number the probability of winning is $P(\text{roll a n}|\text{roll 7 or n})$

just discuss the cases

final answer 0.49293


