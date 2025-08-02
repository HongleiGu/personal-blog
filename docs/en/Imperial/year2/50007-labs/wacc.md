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
# lexer:
- [ ] ⟨int-liter⟩ ::= ⟨int-sign⟩? ⟨digit⟩+
- [ ] ⟨digit⟩ ::= (‘0’-‘9’) 
- [ ] ⟨int-sign⟩ ::= ‘+’ | ‘-’
- [ ] ⟨bool-liter⟩  ::= ‘true’ | ‘false’
- [ ] ⟨char-liter⟩ ::= ‘'’ ⟨character⟩ ‘'’
- [ ] ⟨str-liter⟩  ::= ‘"’ ⟨character⟩* ‘"’
- [ ] ⟨character⟩  ::= any-graphic-ASCII-character-except-‘\’-‘'’-‘"’ | ‘\’ 
- [ ] ⟨escaped-char⟩ ::= ‘0’ | ‘b’ | ‘t’ | ‘n’ | ‘f’ | ‘r’ | ‘"’ | ‘'’ | ‘\’ 
- [ ] ⟨pair-liter⟩ ::= ‘null
- [ ] ⟨ident⟩ ::= ( ‘_’ | ‘a’-‘z’ | ‘A’-‘Z’ ) ( ‘_’ | ‘a’-‘z’ | ‘A’-‘Z’ | ‘0’-‘9’ )*
- [ ] ⟨comment⟩ ::= ‘#’ (any-character-except-EOL)* (⟨EOL⟩ | ⟨EOF⟩)
- [ ] operators:

| Precedence  | Associativity | Operators                     |
| ----------- | ------------- | ----------------------------- |
| 0(tightest) | prefix        | ‘!’, ‘-’, ‘len’, ‘ord’, ‘chr’ |
| 1           | infix left    | ‘*’, ‘%’, ‘/’                 |
| 2           | infix left    | ‘+’, ‘-’                      |
| 3           | infix non     | ‘⟩’, ‘⟩=’, ‘⟨’, ‘⟨=’          |
| 4           | infix non     | ‘==’, ‘!=’                    |
| 5           | infix right   | ‘&&’                          |
| 6(weakest)  | infix right   | ‘\|\|’                        |
# parser:

## Expr

### ⟨expr⟩

- [ ] ⟨unary-oper⟩⟨expr⟩
- [ ] ⟨expr⟩⟨binary-oper⟩⟨expr⟩
- [ ] ⟨atom⟩

### ⟨atom⟩
- [ ] ⟨int-liter⟩
- [ ] ⟨bool-liter⟩
- [ ] ⟨char-liter⟩
- [ ] ⟨str-liter⟩
- [ ] ⟨pait-liter⟩
- [ ] ⟨ident⟩
- [ ] ⟨array-elem⟩
- [ ] '('⟨expr⟩')'

### ⟨unary-oper⟩
- [ ] ‘!’ 
- [ ] ‘-’ 
- [ ] ‘len’ 
- [ ] ‘ord’ 
- [ ] ‘chr'

### ⟨binary-oper⟩
- [ ] ‘*’ 
- [ ] ‘/’ 
- [ ] ‘%’ 
- [ ] ‘+’ 
- [ ] ‘-’ 
- [ ] ‘⟩’ 
- [ ] ‘⟩=’ 
- [ ] ‘⟨’ 
- [ ] ‘⟨=’ 
- [ ] ‘ == ’ 
- [ ] ‘!=’ 
- [ ] ‘&&’ 
- [ ] ‘||‘

### ⟨array-elem⟩

- [ ] ⟨ident⟩('['⟨expr⟩']')+


### additionals:
- [ ] precedence respected
- [ ] left-associative operators must be able to appear repeatly
- [ ] left-associative operators must implicitly bracket to the left
- [ ] right-associative operators must be able to appear repeatly
- [ ] right-associative operators must implicityly bracket to the right
- [ ] non-associative operators should not appear repeatly
- [ ] non-associative operators should not bracket
- [ ] brackets override precedence

## types

### ⟨type⟩
- [ ] ⟨base-type⟩
- [ ] ⟨array-type⟩
- [ ] ⟨pair-type⟩


### ⟨base-type⟩

- [ ] 'int'
- [ ] 'bool'
- [ ] 'char'
- [ ] 'string'

### ⟨array-type⟩

- [ ] ⟨type⟩'['']'
### ⟨pair-type⟩

- 'pair' '('⟨pair-elem-type⟩','⟨pair-elem-type⟩')'

### ⟨pair-elem-type⟩

- [ ] ⟨base-type⟩
- [ ] ⟨array-type⟩
- [ ] 'pair'

## statements

TBC in this doc

# semantics:

## Types:

