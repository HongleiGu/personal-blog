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
# 7.1
```prolog
% min_of_two(+X, +Y, ?Min)
% Succeeds iff Min is the lower of the numbers X and Y

min_of_two(X,Y,X) :-
  X =< Y,
  !.
min_of_two(X,Y,Y).
```

**The version of min_of_two above has a red cut, and a bug in it. Find the bug and fix it, with-out removing the cut**

```prolog
min_of_two(X,Y,X) :-
  X =< Y,
  !.

min_of_two(X,Y,Y) :-
  Y < X,
  !,
```

# 7.2

```
% min_of_two(+X, +Y, -Min)
%   returns the lower of X and Y as Min
min_of_two(X,Y,X) :-
  X =< Y.
min_of_two(X,Y,Y).

% min_of_three(+X, +Y, +Z, -Min)
%   Returns the lowest of the X, Y and Z as Min.
min_of_three(X,Y,Z,Min) :-
  min_of_two(X,Y,MinXY), !,
  min_of_two(MinXY, Z, Min), !.
```

**The version of min_of_three above correctly finds the lowest of three given number, using cuts to make it determinate, Improve the code by changing the placement of the cuts.**



```
% min_of_two(+X, +Y, -Min)
%   returns the lower of X and Y as Min
min_of_two(X,Y,Min) :-
  X =< Y,
  !,
  Min = X.
min_of_two(X,Y,Y).

% min_of_three(+X, +Y, +Z, -Min)
%   Returns the lowest of the X, Y and Z as Min.
min_of_three(X,Y,Z,Min) :-
  min_of_two(X,Y,MinXY), !,
  min_of_two(MinXY, Z, Min).
```

# 7.3:

**write a query to construct a list containing all the possible pairs(X,Y) such that concatenating X and Y gives the list [a,b,c]**

```prolog
findall((X,Y),append(X,Y,[a,b,c]),Ans).
```

# 7.4:

```prolog
person(alice).
person(bob).
person(clare).

friend(alice, bob).
friend(alice, clare).
friend(bob, clare).
```

**Assuming a file containing the data above, write a program for all_friends(-List) that returns a list containing all the pairs(Name, Num), such that Name is a person with Num friends (You may find the built-in predicate length(List, Len) that finds the length of a list helpful)**

```prolog
all_friend_num(Person, Num) :-
  person(X),
  findall(X, friend(X, Person), Xs),
  length(Xs, Num).

all_friend(List) :-
  finall((Name, Num), all_friend_num(Name, Num), List).
```

# 7.5

**Assuming afile containing ground clauses for friend/2 as described above, write a program for all_friendly(-Set) that returns a sorted, duplicate-free list Set containing the name of everyone that is a friend of somebody, As a challenge you may not use the existential quantifier in your program**

```prolog
all_friendly(Fs) :-
  setof(F, friendly(F), Fs).

friendly(F) :-
  friend(F, _).
```