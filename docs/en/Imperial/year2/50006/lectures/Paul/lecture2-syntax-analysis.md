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
# components of a complete compiler:

in order of 

|syntax| semantics                  |
|-|-|
|Source language program| arithmetic expressions     |
|Lexical analyser| scanner                    |
|Syntax analyser| abstract syntax tree       |
|Translator("instruction selection")| powerful magic             |
|Target language program| stack machine instructions |

we use the haskell syntax to specify the data types and functions which made up the compiler

a sampler compiler would be this:

```haskell
compile :: [char] -> [instruction]
compile program 
= translate(parse(scan program))
-- translate is walking down the tree and generate instructions
-- parse is syntacitic analysis, finding the tree of nested eg, if, for, while, statements
-- scan is lexical anlysis, identify, keywords, punctuation, identifier
```

# Syntax analysis(parsing)

## Syntax and semantics:

Syntax consists of rulle for constructing acceptable utterances. we need to consider the grammar rules used to construct it, we can use some parser generators for generating analysis phases

Semantics is the meaning of the code

## syntatic rules:

Syntax is usually sepcified using the Backus-Naur Form(BNF) or Backus Normal Form

```BNF
stat -> 'if' '('exp')' stat 'else' stat
```

each BNF would only show one valid way which the non-terminal lines can be converted into a string of terminals and non-terminals

in the BNF above:

- Terminals: 'if', '(', ')', 'else'
- Non-terminals: stat, exp

only terminals can appear in the final result

## Using syntatic rules:

still using 

```BNF
stat -> 'if' '('exp')' stat 'else' stat
```

suppose we have 

$\text{if(stuff)}_1 \text{stuff}_2 \text{else stuff}_3$

to prove this is grammarically correct, we must show that $stuff_1$ can be derived from exp and $stuff_2, stuff_3$ from non-terminal stat

### more formally:

A context-free grammar(CFG) consist of

- S: a non-terminal start symbol
- P: a set of productions
- t: a set of tokens(terminals)
- nt: a set of non-terminals

for example:

$P = \begin{cases}\begin{aligned}\text{bin}&\to\text{bin'+'dig}\\\text{bin}&\to\text{bin'-'dig}\\\text{bin}&\to\text{dig}\\\text{dig}\to\text{'0'}\\\text{dig}\to\text{'1'}\end{aligned}\end{cases}$

or $P = \begin{cases}\text{bin}&\to\text{bin'+'dig|bin'-'dig|dig}\\\text{dig}\to\text{'0'|'1'}\end{cases}$

Terminals $t = \{\text{'+','-','0','1'}\}$

Non-terminals $nt = \{\text{bin, dig}\}$

in this example, we choose bin as the start symbol S

- Strings of terminals can be derived using the grammar by beginning with the start symbol, and repeatedly replacing each non-terminal with the RHS of some production
- A string so derived which consists only of terminals is called a sentence
- THe language of a grammar is the set of all sentences which can be derived from the starting symbol

### parse tree:

an tree whose branch corresponds precisely to a production in the grammar

![slide11](docs/assets/Imperial/50006/lecture2-slide11.png)

an to use the tree, we simply do DFS or BFS

![slide12](docs/assets/Imperial/50006/lecture2-slide12.png)

### Ambiguities:

as seen previously, we would encounter different productions like this

```
exp -> exp '+' exp |
       exp '-' exp | const | ident
```

in this case, there exists a string with multiple different parse trees

say 9+a-2, we can parse the + first or the - first

#### Associativity

so we define Associativity to define the order of how this executes

For example, how do we interpret 2-3-4

in left associativity: (2-3)-4

in right associativity: 2-(3-4)

The choice is a matter for the language designer, who must take into account intuitions and convenience

#### Precedence

in the case of 9 + 5 * 2

then usually, we need * to have higher precedence

and there can be even higher levels of precedence

#### For our example Language

- All the operators are left-associative'
- "*" and "/" have higher precedence than "+" and "-"


#### unambiguous grammar for arithmetic expressions

this grammar avoid ambiguity by spliting exp in to exp and term

```
exp -> exp + term |
       exp - term |
       term
term -> term * factor |
        term / factor |
        factor
factor -> const | ident
```

now in the example of 9 + 5 * 2, we cannot find two parse trees

![slide21](docs/assets/Imperial/50006/lecture2-slide21.png)

![slide22](docs/assets/Imperial/50006/lecture2-slide22.png)

## Parsers:

the purpose of a parser is to check the input is grammatically correct and to build an abstract syntax tree(AST) representing its structure

two general classes of parsing algorithms

- top-down or predictive (we will study the recursive descent algorithm)
- bottom-up (shift-reduce algorithm)

### Top-down parsing:

Example:

- stat -> 'begin' statlist
- stat -> 's'
- statlist -> 'end'
- statlist -> stat ';' statlist

an example input: "begin S; S; end"

the Slogan is: Starting from the start symbol, search for a rule which rewrites the nonterminals to yield terminals consistent with the input

for efficiency, it will be best if we can go through the rules just once

![slide2425](docs/assets/Imperial/50006/lecture2-slide2425.png)

so we follow the below procedures:

- Assume input is derived from the start symbol(stat in our example)
- Examine each alternative production for stat
- Compare first unmatched input token with first symbol on RHS of each production for stat
- - If found, we use it to rewrite
- - Repeat the process on the next input token
- - If no match, try a production that begin with a non-terminal

If we choose the wrong production

say 

```
stat -> 'loop' statlist 'until' exp
stat -> 'loop' statlist 'forever'
```

in this example we need to find two production starting with loop, there might be confusion in the compilation process

## Bottom-up parsing:

In top-down parsing the grammar is used left-to-right: the possible RHSs are tried

In bottom-up parsing, the input is compared with alll the RHSs, to finbd where we can replace with a production from right-to-left

![slide31](docs/assets/Imperial/50006/lecture2-slide31.png)

these are somewhat complicated to construct, but can be constructed automatically by parser generators

this is often the most practical way to build a parser

we will look at top-down(in particular, recursive descent)

relatively easy, but need to sometime modify the grammar first

## a complete compiler
### syntax
The input: a string of characters representing an arithmetic expression -> sequence of instructions for a simple computer

the grammar:

```
exp -> factor '+' exp | factor
factor -> number | identifier
```

then the parse tree of a+b+1 would be

![slide36](lecture2-slide36.png)

notice the difference of the parse tree and the AST:

```haskell
Plus (Ident "a") (Plus (Ident "b") (Num 1))
```

We need data type specifications for lexical tokens

using haskell to write the compiler then

```haskell
data Token = IDENT [Char] | NUM Int | PLIUS
-- this is the whole set of tokens we may encounter in the lexing process

data AST = Ident [Char] | Num Int | Plus Ast Ast
-- similar to the tree structure we encountered before, each AST is a Tree with the first two nodes
```

they look like BNF but similarity is misleading

### lexical analysis/ parsing
assume we have already written the lexical analyser/scanner

```haskell
scan :: [Char] -> [Token]
-- this transfroms the String to a set of tokens

parser :: [Token] -> Ast
-- this turns the Token to a AST
```

#### A simple parse function

for example, we want to process the rule of

```
factor -> number | identifier
```

then we would write

```haskell
parseFactor((NUM n): tokens) = (Num n, tokens)
parseFactor((IDENT x): tokens) = (Ident x, tokens)
```

to make this syntactically more appealing, we use cases

```haskell
parseFactor(firstToken: tokens)
	 = case firstToken of
		 NUM n -> (Num n, tokens)
		 IDENT x -> (Ident x, tokens)
		 other ->
			 error "Number or identifier expected"
```

then we consider the case of

```haskell
exp -> factor '+' exp | factor
```

this is a non-terminal case

so in haskell we do it recursive

```haskell
parseExp tokens 
	= let (factortree, rest) = parseFactor tokens
	-- we first parse an Factor 
		in 
		case rest of 
			(PLUS : rest2) -> 
				let 
					(subexptree, rest3) = parseExp rest2
					-- the rest is an exp, we call this recursivelt until everything is parsed
						in (Plus factortree subexptree, rest3) 
			othertokens -> (factortree, othertokens)
```

combine these gives

```haskell
parse tokens = 
	let 
		(tree, rest) = parseExp tokens 
	in 
		if null rest then 
			tree 
		else 
			error "excess rubbish“
```

### code generator

suppose we have a stack-based computer whose instruction set is represented by the following Haskell data type:

```haskell
data Instruction = PushConst Int | PushVar [Char] | Add
```

then the translator would be 

```haskell
translate :: Ast -> [Instruction]
translate (Num n) = [PushConst n]
translate (Ident x) = [PushVar x]
translate (Plus e1 e2) = translate e1 ++ translate e2 ++ [Add]
```

## scanner/lexical analysis

```haskell
scan :: [Char] -> [Token]

data Token = PLUS | MINUS | TIMES | DIVIDE | NUM Int | IDENT [Char]
```

then we first handle the punctuaction

```haskell
scan [] = [] -- end of input
scan (' ': rest) = scan rest -- skip spaces
scan ('+': rest) = PLUS : (scan rest)
scan ('-': rest) = SUB : (scan rest)
```

then if we meet a number

```haskell
scan (ch:rest)
	| isDigit ch =
		let (n, rest2) =
			convert (ch: rest)
		in
			(NUM n): (scan rest2)
```

assume convert is a function that collects the digits of a number, convert it into binary and returns the remaining chars

Identifiers

```haskell
scan (ch: rest)
	| isAlpha ch =
		let 
			(n, rest2) = getname (ch: rest)
		in 
			(IDENT n): (scan rest2)
```
where getname work the same as convert, but with chars

for completeness

```haskell
getname :: [Char] -> ([Char], [Char]) 
getname str = 
	let 
		getname' [] chs = (chs, []) 
		getname' (ch : str) chs 
			| isAlpha ch = getname' str (chs++[ch]) 
			| otherwise = (chs, ch : str) 
	in 
		getname' str []


convert :: [Char] -> (Int, [Char]) 
convert str = 
	let 
		conv' [] n = (n, []) 
		conv' (ch : str) n 
			| isDigit ch = conv' str ((n*10) + digitToInt ch) 
			| otherwise = (n, ch : str) 
	in 
		conv' str 0
```

