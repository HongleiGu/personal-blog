---
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
level: Imperial
---
Parsing

# Parsing

Parsing is passing a string to lexer/tokenizer and tokens and then to parser to get parse trees

## Lexing:

we use regular expressions, We often want this because Tokens can be easier to work with

for example

```hs
lex "if x < y then x else y" = [If, Id "x", LAngle, Id "y", Then, Id "x" ...]
```


### what is the token

being a C tokenizer, "*"

(multiplication, pointer dereference, pointer type) "star"

being a Java tokenizer, ">>"

(right shift, generics)

if it is generics

```java
something<List<T>>
```

we need to treat >> as two tokens

tokenizers does nto have much info about the context, so in context sensitive language like python(indent), this migh tcause trouble

## PEG(Parser Expression Grammars) / CFG(Contect-free-grammar)

```bnf
<stmt> ::= 'if' <expr> 'then' <stmt>
         | 'if' <expr> 'then' <stmt> 'else' <stmt>
```

```bnf
<stmt> ::= 'if' <expr> 'then' <stmt> ['else' <stmt>]
```

so an example is

if x < y then (if true then x) else y

```peg
<stmt> <- 'if' <expr> 'then' <stmt>
         / 'if' <expr> 'then' <stmt> 'else' <stmt>
```

if we have an erronous code

if x < y then if true then x

the in peg, we match the first branch and it just when to the first branch

PEG is 
