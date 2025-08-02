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
![ex7](../../../../../assets/Imperial/50006/ex7.png)
# (i)
```haskell
effect :: PointsToSet -> SFGNode -> PointsToSet
effect pts (Node id (Cmp r1 r2)) = pts
effect pts (Node id (Bgt label)) = pts
effect pts (Node id (New n r)) = pts \cup {(r,id)}
effect pts (Node id (Mov r1 r2)) = pts - (r2, id) + (r1, id)
-- model answer
removeTargets r1 pts = [(r2, id) | (r2, id) <- pts, r1 != r2] -- basically removing all entries with r2
effect pts (Node id (Mov r1 r2))
	= (removeTargets r2 pts) \cup [(r2, id) | (r1, id) <- pts] -- removing all entries of r2 and replace with r1
```


# (ii)
never though we could write like this

$$pointsIn(n) =\underset{p\in pred(n)}{\cup} pointsOut(p)$$

$$pointsOut(n) = effect\quad pointsIn(n)\quad instruction_n$$

# (iii)
it does not account for the points-to elements that are killed by the assignment so remove r first

```haskell
effect pts (Node id (New n r))
	= pts' \cup {(r,id)}
		where pts' = [(reg,t) | (reg,t) <- pts, reg \neq r]
```

# (iv)
model answer:

Points-to analysis can be used to determine whether two pointers might point to the same location- which is important for understanding dataflow and potential dependence or interference. It can also be used to determine whether a pointer can escape from the method in which it allocated- and more generally, to automate storage reclamation. You might also wonder whether pointer analysis might enable you to reason about which parts of the code might be able to reach private (or vulnerable) data.