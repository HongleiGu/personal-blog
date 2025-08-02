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
for the most part, see the pdf, too much words to type

# Three address code:
the basic intermediate representation, take the form of $c = a\oplus b$, at most 3 operands, 

the available expressions are the expression with all variables not killed, for example in the b = a - f case, b is killed, removing b+c from the available expressions

# Available expressions enable common sub-expression elimination

![slide40](../../../../../../assets/Imperial/50006/tut6-slide2.png)
available expressions can be optimised with a temporal variable, so that this variable may be kept to later computation. (see After CSE line 1,2,7, the b + c is reused, changing it to t reduces some operation)

![slide40](../../../../../../assets/Imperial/50006/tut6-slide3.png)
in this example (the case in the tut), we can see that a + b reappears in 1 and 7, and d + e in 2 and 8, g + h in 3 and 9,

by using available expressions

| Node | Gen   | Killed | AvailIn                    | AvailOut(since no kill, this is the same as AvailIn) |
| ---- | ----- | ------ | -------------------------- | ---------------------------------------------------- |
| 0    | -     | -      | -                          | -                                                    |
| 1    | (a+b) |        | a+b                        |                                                      |
| 2    | (d+e) |        | a+b, d+e                   |                                                      |
| 3    | (g+h) |        | a+b, d+e, g+h              |                                                      |
| 4    | -     |        | a+b, d+e, g+h              |                                                      |
| 5    | x*2   |        | a+b, g+h, x*2 (d killed)   |                                                      |
| 6    | x*2   |        | a+b, d+e, x*2 (g killed)   |                                                      |
| 7    | a+b   |        | a+b, x*2 (branch combined) |                                                      |
| 8    | d+e   |        | a+b, x*2                   |                                                      |
| 9    | g+h   |        | a+b, x*2                   |                                                      |
| 10   | -     |        | a+b, x*2                   |                                                      |
# (1)
from top to bottom, since the available expression of the current instruction is determined by all the instructions before itself.

similar to the reaching definitions

```pseudo
\begin{algorithm}
\caption{Available iteration}
	\begin{algorithmic}
		\State $AvailOut(0) = \varnothing$
		\For{$n\in N-\{0\}$}
			\State $AvailIn(n) = AvailOut(n) = U$
		\EndFor
		\While{$\text{any }AvailOut(n)\text{ changes}$}
			\State $AvailIn(n) = \cap_{p\in preds(n) AvailOut(p)}$
			\State $AvailOut(n) = gen(n)\cup (AvailIn(n) - kill(n))$
        \EndWhile
	\end{algorithmic}
\end{algorithm}
```

- This is a forward analysis - information flows from from predecessors to successors
- So try to visit nodes in a forward direction in order to propagate information as quickly as possible
- At each visit to node n, compute AvailIn(n) then AvailOut(n)

# (2)
since we only have few expressions in the available expressions, we can assign every bit to a variable and 1 represent this is present in the expression, 0 otherwise

- When we compute U, we can assign a bit index for each expression - and pre-compute the bitwise representation of each node's kill(n)
- Then the set operations can be done with bitwise logical operations
# Using availble expressions:
- Mechanism: You need to look at each node, check it's RHS, and see whether that epression is in that node's AvailIn
- If so then find the instruction that generates it and insert and instruction to copy the result to a new temporal register
- You can then replace this node's RHS with that register (recall the t = b + c, a = t)
- Strategy: common sub-expression requires the allocation of an additional register. If this were to cause spilling, it;s unlikely that the optimisation would be profiable
