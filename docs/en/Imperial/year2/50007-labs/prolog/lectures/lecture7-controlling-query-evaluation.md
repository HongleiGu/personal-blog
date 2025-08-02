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
comments: true
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
hide:
- navigation
- toc
- footer
- feedback
level: Imperial
---

# pruning computations with !

it prevents further backtracking

for example

```prolog
send(Csut, Balance, Message) :-
  Balance =< 0,
  warning(Cust, Message)

send(Cust, Balence, Message) :-
  Balance > 0,
  Balance =< 50000,
  credit_card_info(Cust, Message)

send(Cust, Balance, Message) :-
  Balance > 50000,
  investment_offer(Cust, Message)
```

the clauses are mutually exclusive, when one is executed, we dont need to execute the other clauses, so we add a cut to prevent it from further executing

```prolog
send(Csut, Balance, Message) :-
  Balance =< 0,
  !,
  warning(Cust, Message)

send(Cust, Balence, Message) :-
  Balance > 0,
  Balance =< 50000,
  !,
  credit_card_info(Cust, Message)

send(Cust, Balance, Message) :-
  Balance > 50000,
  !,
  investment_offer(Cust, Message)
```

in this case it is the green cuts, when we remove it, the code still works

```prolog
send(Cust, Balance, Message) :-
  Balance =< 0,
  !,
  warning(Cust, Message)

send(Cust, Balence, Message) :-
  Balance =< 50000,
  !,
  credit_card_info(Cust, Message)

send(Cust, Balance, Message) :-
  investment_offer(Cust, Message)
```

in this case it is a red cut, the code will not work as expected after all cuts are removed

we should try to use green cuts as possible during optimization

# Collection All Solutions:

## findall / 3

findall(+Template, +Goal, -List), each element in List is a instance of Template and the elements satisfy Goal

for example

```
friend(alice, bob).
friend(alice, clare).
friend(bob, clare).

% ----------

findall(F, friend(F, clare), Friends).
Friends = [alice,bob] ? ;
```

## setof / 3

the same as findall, but removes duplicates

but setof is not treated as existentially quantified (the actual value is significant) so it will return a list for each possible value

for example

```prolog
| ? - findall(F, friend(F, P), Fs).
Fs=[alice,alice,bob]?
| ? - setof(F, friend(F, P), Fs).
P = bob,
Fs = [alice]?;
P = clare,
Fs = [alice, bob]?;
```

we can use the existential quantifier ^ to signify we want the answers returned as a single list

```prolog
| ? - setof(F, P^friend(F,P), Fs)

Fs = [alice, bob]
```


## forall

forall(P,Q)

succeed iff goal Q is true for every true instance of goal P

```prolog
forall(P,Q) :-
  \+ (P, \+ Q).
```