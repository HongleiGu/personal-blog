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
# Exercise 6.1

```prolog
person(john).
person(mary).
person(jane).

likes(mary, jane).
likes(john, mary).
likes(jane, mary).
```

**Given the clauses above for person/1 and likes/2, write a definition for sad(-P). A person is sad if there is no person that likes them**

Joker!

```prolog
sad(P) :-
  person(P),
  !,
  \+ likes(_,P).
```