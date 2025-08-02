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

**In this exercise, you should see how to translate a simple high-level language into assembly code for a stack machine. Most recent past papers have included a question on code generation (C244 2014Q2, C221 2016Q2, C221 2015Q2, C221 2016Q2, C221 2020Q2, COMP50006 2021Q2)- this exercise sets the foundations**

# Exercise 2.1: Code Generation for Statements

## Input: 
**assume the following abstract syntax tree data type for statements**:

```haskell
data Statement = Assign Name Expression |
				 Compound [Statement] |
				 IfThen Expression Statement |
				 IfThenElse Expression Statement Statement |
				 While Expression Statement
```

**Here Expression is a haskell data type for the abstract syntax tree of expressions**

## Output:
**your translator should return a list of assembly language instructions. The instructions are represented as the following Haskell data type**

```haskell
data Instruction = 
	Add | Sub | Mul | Div -- (as before) 
	| PushImm num -- (push constant onto stack) 
	| PushAbs Name -- (push variable at given location onto stack) 
	| Pop Name -- (remove value at top of stack and store it at given locn) 
	| CompEq -- (subtract top two elements of stack, and replace with 1 if the result was zero, 0 otherwise) 
	| JTrue label -- (remove top item from stack; if 1 jump to label) 
	| JFalse label -- (jump if stack top is 0) 
	| Jump label -- (jump unconditionally 
	| Define label -- (set up destination for jump)
```

**Note that Define is an assembler directive not an executable instruction**

**Write a function translate_statement which generates assembly code for a statement. You are given some of the cases below: your job is to supply the rules for Compound, IfThenElse and While. Assume that you have been given a function translate expression, which takes as input the AST for an expression, and produces assembly code for a stack machine which when executed leaves the value of the expression on the top of the stack (a simple version of such a function is given in Chapter 2 of the lecture notes).**

### Hint1: Assignments:

**For example, here is the rule for translating assignment statements**

```haskell
translate_statement :: Statement-> [Instruction] 
translate_statement (Assign var exp) = 
	translate_expression exp ++ 
	[Pop var]
```

**The Pop instruction takes the value at the top of the stack and stores it at the named location. The ++ operator is used to join lists of instructions. For example,**

```haskell
translate_statement (Assign "y" (Binop Plus (Number 12)(Ident "x")))
```

**would yield the following list of assembly language instructions for some simple stack-based machine**

```haskell
[PushImm 12, PushAbs "x", Add, Pop "y"]
```

**This could then be printed out in the proper syntax for some real processor. For example, for Intels IA32 instruction set you would get something like this:**

```assembly
pushl $12 
pushl x 
popl %eax 
addl %eax,(%esp) 
popl y
```

**It turns out that the Add pseudo-instruction cant be done with just one IA32 instruction, you need two.**

### Hint2: If-then statements

**As another example, here is the rule for the if-then statement:**

```haskell
translate_statement (IfThen cond_exp body)
  = translate_expression cond_exp ++ 
	[JFalse label] ++ 
	translate_statement body ++ 
	[Define label] 
		where label = a new label name which has not been used before in the program
```

**The instruction JFalse removes the element at the top of the stack, and jumps to the given label if the value represents false for example we could encode True as 1 and False as 0. There is a similar instruction JTrue.**

**For example the statement if a=100 then a:=b translates to the stack machine sequence**

```haskell
[PushVar "a", PushConst 100, CompEQ, JFalse "L1234", PushVar "b", Pop "a", Define "L1234"]
```

**This could then be printed out in IA32 assembler as follows**

```assembly
	mov.w a,-(sp) 
	mov.w #100,-(sp) 
	mov.w (sp)+,d0 ; These two IA32 instructions achieve the effect  
	sub.w d0,(sp) ; of the stack machine CompEQ instruction. 
	tst.w (sp)+ ; These two IA32 instructions achieve the effect
	beq L1234 ; of the stack machine JTrue instruction
	mov.w b,-(sp) 
	mov.w (sp)+,a 
L1234:
```

**The expression Define "L1234" does not correspond to an actual instruction to be executed. Instead it makes the destination of the JFalse instruction. Thus if the conditional expression evaluates to the representation of False, the body is not executed, and control transfers directly to the end of the sequence.**

### Common problems
### Haskell's algebraic data types

**Note that Statement and Instruction are examples of Haskells algebraic data types. This is a compact representation, which would be implemented using a union in C. The symbols Assign, Compound, IfThen, Add, Pop etc. are called constructors. For example, a statement can have one of ve forms; the constructor indicates which form is present and introduces the elements of the structure, such as (e.g. for While, the ASTs for the conditional expression and the loop body**

#### Haskell's list

**The translator returns a list of instructions. Haskell has three operators for building lists**

| expression | meaning                                                                            | example                     |
| ---------- | ---------------------------------------------------------------------------------- | --------------------------- |
| [x]        | given an element x                                                                 | e.g.[1]                     |
| x : A      | given a list A and an element x, make a new list starting with x and ending with A | e.g. 2:[1]=[2,1]            |
| A++B       | join the two lists A and B                                                         | e.g. [1,2]++[3,4]=[1,2,3,4] |

**If you have spare time, you might like to think about how to implement this code generator in Java, using a Visitor pattern. **

## answer:

```haskell
translate_statement :: Statement -> [Instruction]

-- copied from hint
translate_statement (Assign var exp) = 
	translate_expression exp ++ 
	[Pop var]

translate_statement (Compound []) = []
translate_statement (Compound (stmt: stmts)) = 
	[translate_statement stmt] ++
	translate_statement Componud stmts
	

translate_statement (IfThen cond_exp body)
  = translate_expression cond_exp ++ -- translate the condition
	[JFalse label] ++ -- set the jump address of false condition
	translate_statement body ++ -- stmt
	[Define label] -- false jump address
		where label = a new label name which has not been used before in the program

translate_statement (IfThenElse cond_exp true_stmt false_stmt)
  = translate_expression cond_exp ++ -- translate the condition
	[JFalse false_label] ++ -- set the jump address of false condition
	translate_statement true_stmt ++ -- stmt
	[Jump end_label] ++
	[Define false_label] ++ -- false jump address
	translate_statement false_stmt
	[Define end_label]
		where label = a new label name which has not been used before in the program

translate_statement (While expr stmt)
  = [Define start_label] ++
	translate_expression expr ++
	[JFalse end_label] ++
	translate_statement stmt ++
	[Jump state_label] ++
	[Define end_label]
```

*note, some considerations should be taken in the while, we could potentially jump the entire stmt if the first expr evaluates to false*
## Extension- boolean operators 
**Consider adding an AST type for Boolean expressions, such as comparisons. How would you design a transBExp function for Boolean expressions? How about we also add And, Or and Not operators. The trick, of course, would be to avoid executing the second operand of an And expression if the rst operand turns out to be false (since the result is already guaranteed to be false). An idea for doing this might be to give transBExp the labels of the statements to jump to if the result is true, and, respectively, false**

```haskell
-- Bool AST, for example
data BoolAST =
	
	And Expression Expression|
	Or Expression Expression|
	Not Expression |
	Compare Expression Expression 
	
transBExp (And expr1 expr2) true_label false_label
  = translate_expression expr1 ++
	[JFalse false_label] ++
	translate_expression expr2 ++
	[JFalse false_label] ++
	[Jump true_label]

transBExp (Or expr1 expr2) true_label false_label
  = translate_expression expr1 ++
	[JTrue true_label] ++
	translate_expression expr2 ++
	[JTrue true_label] ++
	[Jump false_label]

transBExp (Not expr) true_label false_label
  = translate_expression expr ++
	[JFalse true_label] ++
	[Jump false_label]

```
