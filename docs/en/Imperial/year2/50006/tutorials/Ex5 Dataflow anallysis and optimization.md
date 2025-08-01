---
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
level: Imperial
---
**In this exercise we will use data-flow analysis to compute a lower bound on the execution time of the code. Assume that we have as input a control flow graph (CFG) as described in the lecture notes**

```haskell
data CFGNode = Node Id Instruction [Register] [Register]  [Id]   [Id]
									defs         uses       succs preds
```

**We will pretend that all instruction take 1 unit of time to execute - even function calls. The output of the analysis will be, for every node in the graph, the earliest time at which this node could have been reached, assuming that the start node is reached at time 0. Nodes that are never reached are assigned the special value infinity. If all final (exit) nodes of the graph have the value Infinity, the code will never terminate. In fact, nodes assign Infinity correspond to unreachable nodes that may be removed from the control flow graph**

# 1. 
**One of the data flow equations clearly will take the form**

$$\text{timeOut}(n) = timeIn(n) + 1$$

## (a)
**What is the equation for defining timeIn in terms of timeOut?**

recall that for LiveOut(n), $LiveOut(n) = \cup_{s\in succ(n)}LiveIn(s)$

similarly $TimeIn(n) = \min_{s\in pred(n)}TimeOut(s)$

the shortest time of any previous nodes is the shortest time it takes to get to the node

## (b)
**As shown in the lecture notes, we use iteration to solve the system of DFA equations timeIn(n) and timeOut(n) for each node n in the CFG**

**What are the initial assignments for timeIn(n) and timeOut(n)?**

following the same manner as LiveIn and LiveOut

```haskell
for each n in CFG {
	TimeIn(n) := 0; Timeout(n) := infinity; Timeout(start) := 0
}
repeat {
	for each n in CFG {
		TimeOut(n) = TimeIn(n) + 1
		TimeIn(n) = \min_{s\in pred(n)} Timeout(s)
	}
} until TimeIn and TimeOut stops changing
```

(but note the start node should be 0, or else every node would be zero)

### (c)
**do any nodes need to be initialise with a different value?**

yes, the start node

## (d)
**Is this a forward or backward data-flow analysis**

forward, since information never sends to pred nodes

![slide40](../../../../../../assets/Imperial/50006/ex5-2.png)