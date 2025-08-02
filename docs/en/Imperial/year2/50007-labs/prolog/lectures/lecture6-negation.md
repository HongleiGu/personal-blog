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

# The \+ predicate

this is the prolog not,

```prolog

?- \+ (member (a, [1,2,3]))

% this can also be written as

?- \+ member (a, [1,2,3])
```

the \+ defines a Goal, but if there are more than one subgoals, then it must be put into parentheses

for example,

```prolog
character(harry)
character(bilbo)
character(bart)

has_cloak(harry)
has_cloak(bilbo)

disappears(X) :-
  has_cloak(X)
disappears(X) :-
  has_ring(x)


%-------------------

?- \+ disappears(X), character(X)


?- character(X), \+ disappears(X)

% characrter(x), \+ diappear
% x = harry
% - character(harry)
% - yes
% - \+ disappear(harry)
% - - disappear(harry) 
% - - - has_cloak(harry)
% - - - yes
% - - yes
% - no

% x = bilbo
% - character(bilbo)
% - yes
% - \+ disappear(bilbo)
% - - disappear(bilbo)
% - - - has_cloak(bilbo)
% - -  -no
% - - - has_ring(bilbo)
% - - - yes
% - - yes
% - no

% x = bart
% - character(bart)
% - yes
% - \+ diappear(bart)
% - - disappear(bart)
% - - - has_cloak(bart)
% - - - no
% - - - has_cloak(bart)
% - - - yes
% - - no
% - yes

% x = bart



```