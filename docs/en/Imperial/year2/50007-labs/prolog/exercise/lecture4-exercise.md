---
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
level: Imperial
---
# 4.1

```prolog
 %student(?ID,?First,?Last,?Address)
 % First Last is a student with id ID living at Address
 % where Address is a terma ddress(Street,City,Country)
student(
  ppr120,
  'Pierre',
  'Programmer',
  address('1 Rue Eclaire', 'LeHavre', 'France')
).
 ...
```

**Given a file containing ground clauses for student /4 as illustrated above, write a Prolog porgram city(+ID, -City) that returns the city in which a studetn lives, given their id.**

```prolog:
city(ID, City) :-
  student(ID,_,_,address(_, City, _)).
```

# 4.2:

**Write a Porlog program city(+Student, -City) that returns the city in which the Student lives, where**

- **Student is a term of the form student(ID,First, Last, Address)**
- **Address is a term of the form address(Street, City, Country)**
- **ID, First, Last, Street, City and Country are atoms**

```prolog
city(Student, City) :-
  student(_, _, _, Address) is Student,
  address(_,_City) is Address. % this is wrong as is can only do arithmetic evaluation, not unification
```

```prolog
city(Student, City) :-
  Student = student(_, _, _, Address),
  Address = address(_, City, _).
```

# 4.3

**What is the output of the following queries?**

- a) ```X = Y, Y = 5``` X = 5, Y = 5
this unifies X and Y, Y and 5.

- b) ```X \= Y, X = 3, Y = 5``` no

in this case when it tries to evaluate X \= Y, by the order of backtracking X,Y are not defined

```prolog
?- X=3,Y=5,X\=Y.

X = 3,
Y = 5 ? 

yes
```

# 4.4

**What is the outcome of the following queries?**

- a) ?- X == Y, X = 5.

no. X and Y are not defined

- b) ?- X = Y, X == Y,

Y = X. the == does not return anything, it is a check

# 4.5

What is the outcome of the following queries

- a) f(A) @< f(A, a).

yes

- b) f([g(1)],2,3) @> f([a])

yes

these are all same name predicates with differnet arities

# 4.6

**Without using append! Write a program my_append/3 that behaves like append/3 describes above**

```prolog
my_append([H|L1], L2,[H|LT]) :-
  my_append(L1, L2, LT).

my_append(L1, [], L1).
my_append([], L1, L1).
```

# 4.7:

```prolog
% bad_add(+L1, +Elem, -L2)
%   L2 is the list L1 after adding a new element Elem
bad_add(L1, Elem, L2) :-
  append(L1, [Elem], L2).
```

**Improve the program above**

```prolog
bad_add(L1, Elem, [Elem|L2]).
```

# 4.8:

What is the result of the following queries?

```prolog
% (a)

X = Y, X =:= Y.

% (b)

X = 5, X =:= 5.

% (c)

X = 2 + 2.

% (d)

4 is 2 + 2.
```

- (a) error
- (b) X = 5
- (c) X = 2 + 2 (notice this is not a number)
- (d) yes
