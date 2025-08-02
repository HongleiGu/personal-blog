---
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
level: Imperial
---
# part1
## lecture 1: Instructions:
### overview:
$\begin{array}{r}\text{instruction}=\text{opcode} & \text{what it does}\\+\\\text{operand} & \text{register/memory/data}
\end{array}
$

- the MIPS instruction includes three types: R,I,J
- we use MIPS to explain ideas in computer architecture in this course
### MIPS architecture:
- representative of the modern RISC architectures
- 32 bit register and $ \$ $ 0 wired to 0
- since memeory access is usually faster than register access, we need to minimise memory access
- instruction type:
  - most instructions involve registers only, this is faster
  
  ```
  add $1,$2,$3 #reg1 = reg2+reg3
  ```
  - special memory access instructions: possbly multicycle:
  ```
  lw $8, Astart($19) #reg8 = M[Astart+reg19]
  ```


### MIPS instructions:
$\text{32-bit register}\begin{cases}R(\text{register})\\I(immediate)\\J(jump)\end{cases}$

the opcode is always 6-bits
#### R
this includes arithmetic, comparison, logical,$\dots$operations

example:
```
add $8, $17,$18 # reg8 = reg17 + reg18
```

$\begin{cases}
\text{opcode} & 6bits & 0\\
\text{source 1} & 5bits & 17\\
\text{source 2} & 5bits & 18\\
\text{destination} & 5bits & 8\\
\text{function to use} & 6bits & 32\\
\end{cases}$

in the MIPS format, the destination comes first

#### I
memory access, conditional branches, arithmetic involving constants:

example:
```
lw $8, Astart($19) # reg8 = M[Astart + reg19]
```

$\begin{cases}
\text{opcode} & 6bits & 35\\
\text{source 1} & 5bits & 19\\
\text{destination} & 5bits & 8\\
\text{immediate constant} & 16bits & Astart
\end{cases}$

#### J
unconditional jump to instruction in memory

example:
```
j 1236 #jump to instruction at address 1236
```

$\begin{cases}
\text{opcode} & 2bits\\
\text{memory address} & 26bits\\
\end{cases}$

the jump instructions can also be I-type or R-type
- I-type
  ```
  bne $19 $20 label # if reg 19 != reg20 goto Label
  ```
- R-type
  ```
  jr $ra # jump to address in register ra
  ```
#### example:
if (i == j) f=g+h; else f= g-h;

allocate $\begin{cases}
reg16 = f\\
reg17 = g\\
reg18 = h\\
reg19 = i\\
reg20 = j
\end{cases}$

```
    bne $19, $20, Else # if 1 != j goto Else
    add $16 $17 $18    # f = g + h
    j Exit             # goto Exit
Else: sub $16 $17 $18  # f = g - h
Exit:
```

## lecture2:performance
### calculating performance:
- CPI average clock sycles per instruction
- $\begin{aligned}
\text{number of cycles for program P} &= \text{number of instructions for P} &\times  CPI\\
\end{aligned}
$$\begin{aligned}
\text{execution time for P} &= \text{clock cycle time} \times \text{number of cycles for P}\\
&= \frac{1}{\text{clock speed}} \times\text{number of cycles for P}\\
\text{average execution time for P1,P2...} &= \frac{1}{n}(\text{execution time for P1} + ... + \text{execution time for Pn})
\end{aligned}$
- execution time = instruction counts $\times$ CPI $\times$ cycle time
### example:
- M1,M2 implemented on the same set of instructions with instruction classes A and B
- CPI for M1 on class A: A1, on class B: B1
- CPI for M2 on class A: A2, on class B: B2
- clock speed for M1: C1 MHz, M2: C2 MHz

then
- peak performance for N instructions($P\downarrow Q = \min(P,Q)$)
  - $\text{excution time for M1} = \frac{1}{C1}\times N\times\text{minimum CPI for M1} = \frac{N(A1\downarrow B1)}{C1} $
  - $\text{compare M1 and M2}:\frac{\text{execution time for M1}}{\text{execution time for M2}} = \frac{(A1\downarrow B1)C2}{(A2\downarrow B2)C1}$
- average performance given by execution time of N instructions, half class A and half class B
  - $\text{excution time for M1} = \frac{1}{C1}\times N\times\text{average CPI for M1} = \frac{N(A1+B1)}{2C1} $
  - $\text{compare M1 and M2}:\frac{\text{execution time for M1}}{\text{execution time for M2}} = \frac{(A1+B1)C2}{(A2+B2)C1}$

## lecture3: address mode:
### MIPS addressing modes:
- register addressing: data in registers
- immediate addressing: data in instruction itself
- base addressing: data in memory
- PC-relative: base addressing with registers replaced by PC

### classifiying architectures:
we can classify architectures based on how memory is addressed
- stack: operand specified implicitly at the top of a stack
```
# C=A+B:
push A;
push B;
add;
pop C;
```
- accumulator: one operand in accumulator:
```
# C=A+B
load A;
add B;
store C;
```
- register: explicit operands:
```
# C=A+B
load R1 A;
add R2,R1,B;
store C,R2
```
### custom instructions:
we can implement custom instructions, for example, squaring
### Amdahl's law
if $\alpha$ portion of the runtime $T_{old}$ runs $\beta$ times faster

the overall improvement id $T_{new} = \frac{\alpha T_{old}}{\beta} + (1-\alpha)T_{old}$


### summary for lectures 1 2 3
![image.png](attachment:image.png)

## lecture 4:
### basic arithmetic:
- two's complement: $(1\times -2^3) + (0\times 2^2) + (1\times 2^1) +(1\times 2^0) = -5_{10}$
- n-bit: range (-2^{n-1}..2^{n-1}-1)
- sign extension: $1011_{2C} = 1111011_{2C}$
- overflow
- in the MIPS structure:
  - slt, slti work with two's complement
  - sltu, sltiu work with unsigned representation and do not cause overflow exceptions
### logical operations:
- shift left logical:
  ```
  sll $10, $16, 8 # reg10 = reg16 << 8
  ```
  - $\begin{array}{c}reg16 & 0..0 & 0000 & 0000\text{ }1101\\
             reg10 & \underbrace{0..0}_{20bits} & 1101 & \underbrace{0000\text{ }0000}_{\text{introduce zeros}}\end{array}$
  - instruction: $\begin{array}{c}0 & 0 & 16 & 10 & 8 & 0\\\text{R type} & \text{source1} & \text{source2} & \text{destination} & \text{shamt} & \text{function}\end{array}$
- shift left logical variable(sllv): shamt in the register source 1
- srl,srlv,sra(right shifts) extend high order bits
- bitwise: 
  - or, and : R-type
  - ori, andi : I-type
### ALU:
the ALU can do four things: add, subtractm bitwise and, bitwise or.
#### bitwise and/or
turn a and/or gate into a multiplexer:

![image.png](attachment:image.png)

when d is 0, it choose the one in the left, otherwise right

#### add and subtract
we know how we can add, aubtract etc. with one bit, now extend it to multiple bits:

![32fb6ecb51fccfe72c9501c75458a02.png](attachment:32fb6ecb51fccfe72c9501c75458a02.png)

- ha stands for half adder, fa, stands for full adder

- subtracting is just adding one inverse
#### grouping components
we can group components together to form larger repeated unit

![cc37de243f05f115b42c3636dee168a.png](attachment:cc37de243f05f115b42c3636dee168a.png)

the aor block is simply outputing the and and or at once, the afa block is outputing the sum, and, or at once

#### select ALU operation:

![8a7cbb8e48b2ca486141a71fcec3de7.png](attachment:8a7cbb8e48b2ca486141a71fcec3de7.png)

when $d_0$ is 0, the next $d_0$ will be 0, similar for 1

$d_1$ same as $d_0$

$C_1$ remain unchanged

#### comparisons bitwise:

if $a < b$, then $a - b<0$ so MSB(most significant bit) of $a-b$ is 1

![image.png](attachment:image.png)

### zero detection:

add another gate at the bottom for beq, bne, (a = b, or a-b = 0)

![8a7cbb8e48b2ca486141a71fcec3de7.png](attachment:8a7cbb8e48b2ca486141a71fcec3de7.png)

## lecture 5: multiplication and division:
### mul:
$\text{multiplicand}\times \text{multiplier} = \text{product}$

so the idea is just sum of the multiplcand $mc$ shifted successively by one bit relative to multiplier $mp$

basically what the following graph is doing is just calling the ALU to add every shifted mc to the product

![image.png](attachment:image.png)

the procedure is as follows, pretty straightforward

![image-2.png](attachment:image-2.png)

actually we can do this, we do not need to shift the mc, and if mc and mp are shorter than product, things get easier

![image-3.png](attachment:image-3.png)

the procedure is now:

![image-4.png](attachment:image-4.png)

we could also just initialise the mp in the right half of the product register, so we do not need to shift two registers

![image-5.png](attachment:image-5.png)

the procedure:

![image-6.png](attachment:image-6.png)

#### booth's algorithm:
- replacing summing k terms $\sum_{i=0}^{k-1}m$ by $-m + 2^k m$

### division:
$\text{dividend} = \text{Quotient}\times\text{divisor} + Remainder$

basically the same as multiplication, but in the reversed way

![image-7.png](attachment:image-7.png)

the procedure is as follows:

![image-8.png](attachment:image-8.png)




```python
def to2(a):
    temp = []
    a = int(a)
    if a < 0:
        a = 2**8+ a
    while a > 0:
        temp.append(a%2)
        a = int(a/2)
    while(len(temp) < 8):
        temp.append(0)
    return list(reversed(temp))[:8]

def to10(a):
    cnt = 0
    rtrn = 0
    for i in reversed(a):
        rtrn += i*2**cnt
        cnt+=1
    return rtrn
def minus(a,b):
    return to2(to10(a) - to10(b))

def add(a,b):
    print(a,b,to10(a) + to10(b) - 256)
    if to10(a) + to10(b) > 255:
        return to2(to10(a) + to10(b) - 256)
    return to2(to10(a) + to10(b))

def shift_left(a):
    return to2(to10(a) * 2)

def shift_right(a):
    return to2(to10(a) / 2)

add(to2(2),to2(5))
```

    [0, 0, 0, 0, 0, 0, 1, 0] [0, 0, 0, 0, 0, 1, 0, 1] -249
    




    [0, 0, 0, 0, 0, 1, 1, 1]




```python
class div:
    def __init__(self, dd, ds):
        self.r = to2(dd)
        self.dd = to2(dd)
        self.q = to2(0)
        self.ds = to2(ds * 16)
        print("init:")
        print(self)
    def __str__(self):
        return "dd: "+str(self.dd)+"\nr:  "+str(self.r)+"\nq:  "+str(self.q)+"\nds: "+str(self.ds)+"\n"+"-"*40
cnt = 0
a = div(15,6)
for i in range(33):
    a.r = minus(a.r,a.ds)
    if a.r[0] == 0:
        a.q = shift_left(a.q)
        a.q[-1] = 1
    else:
        a.r = add(a.r,a.ds)
        a.q = shift_left(a.q)
        a.q[-1] = 0
    a.ds = shift_right(a.ds)
    if to10(a.ds) <= 1:# to10(a.r):
        break
    print("cnt:"+str(i+1)+"\n"+str(a))
print(to10(a.dd))
print(to10(a.ds))
print(to10(a.q))
print(to10(a.r))
```

    init:
    dd: [0, 0, 0, 0, 1, 1, 1, 1]
    r:  [0, 0, 0, 0, 1, 1, 1, 1]
    q:  [0, 0, 0, 0, 0, 0, 0, 0]
    ds: [0, 1, 1, 0, 0, 0, 0, 0]
    ----------------------------------------
    [1, 0, 1, 0, 1, 1, 1, 1] [0, 1, 1, 0, 0, 0, 0, 0] 15
    cnt:1
    dd: [0, 0, 0, 0, 1, 1, 1, 1]
    r:  [0, 0, 0, 0, 1, 1, 1, 1]
    q:  [0, 0, 0, 0, 0, 0, 0, 0]
    ds: [0, 0, 1, 1, 0, 0, 0, 0]
    ----------------------------------------
    [1, 1, 0, 1, 1, 1, 1, 1] [0, 0, 1, 1, 0, 0, 0, 0] 15
    cnt:2
    dd: [0, 0, 0, 0, 1, 1, 1, 1]
    r:  [0, 0, 0, 0, 1, 1, 1, 1]
    q:  [0, 0, 0, 0, 0, 0, 0, 0]
    ds: [0, 0, 0, 1, 1, 0, 0, 0]
    ----------------------------------------
    [1, 1, 1, 1, 0, 1, 1, 1] [0, 0, 0, 1, 1, 0, 0, 0] 15
    cnt:3
    dd: [0, 0, 0, 0, 1, 1, 1, 1]
    r:  [0, 0, 0, 0, 1, 1, 1, 1]
    q:  [0, 0, 0, 0, 0, 0, 0, 0]
    ds: [0, 0, 0, 0, 1, 1, 0, 0]
    ----------------------------------------
    cnt:4
    dd: [0, 0, 0, 0, 1, 1, 1, 1]
    r:  [0, 0, 0, 0, 0, 0, 1, 1]
    q:  [0, 0, 0, 0, 0, 0, 0, 1]
    ds: [0, 0, 0, 0, 0, 1, 1, 0]
    ----------------------------------------
    [1, 1, 1, 1, 1, 1, 0, 1] [0, 0, 0, 0, 0, 1, 1, 0] 3
    cnt:5
    dd: [0, 0, 0, 0, 1, 1, 1, 1]
    r:  [0, 0, 0, 0, 0, 0, 1, 1]
    q:  [0, 0, 0, 0, 0, 0, 1, 0]
    ds: [0, 0, 0, 0, 0, 0, 1, 1]
    ----------------------------------------
    15
    1
    5
    0
    



## lecture 6: Datapath and control:

usually we get a datapath by the following 3-steps:
1. get different datapaths for 
  - register-based instructions e.g. addition, subtraction
  - memory-access instructions e.g. lw, sw
  - branch instrcutions e.g. beq, j
2. combine the datapath by adding multiplexers
3. add a control unit to activate the relevant parts
### instructions
#### register-based instructions
select read/write registers from operands

select ALU operation from opcode and function code fields

```
add $5, $6,$7 #reg[5] = reg[6] + reg[7]
```
this completes in a single cycle:
- read from reg[6] and reg[7]
- add through ALU
- write to reg[5]

#### Memory access instructions: load
```
lw $5, offset($6) # reg[5] = M[reg[6] + offset]
```

the 32 bits of instruction $\begin{cases}\text{opcode}\\\text{source}\\\text{destination}\\\text{offset}\end{cases}$

the offset goes into the sign extention where the 16-bit offset will be extended to 32 bits and add together with the source to get a address to write the data

#### Memory access instructions: store:
```
sw $5,offset($6) #M[reg[6] + offset] = reg[5]
```

this is basically the same as the above

#### Combine datapaths for R-type and memory instructions: R-type flow:

basically the same, but we add two multiplxer to control the datapath

![image.png](attachment:image.png)

#### Combine datapaths for R-type and memory instructions: memory flow



![image.png](attachment:image.png)

### branching:

```
beq $5,$6,L
```

checking for equals is simple, just subtract and check for the zero output of the ALU

but checking for the address needs an additional Adder to add the ALU output with altered offset

offset specifies the number of instruction, each takes 4 bytes(32 bits), so we need to right shift by 2(divide by 4)

### add instruction memory




### check for R-type:
now the R-type instructions are as follows
![3e540b93ce239b8d1b5d394bf15be4e.png](attachment:3e540b93ce239b8d1b5d394bf15be4e.png)






### control:

the control basically controls the four multiplexer to achieve different functions



![cbb84e560f219fbbce7862e3ca98b54.png](attachment:cbb84e560f219fbbce7862e3ca98b54.png)



![127b424c6f631f90a6a551668fb45d6.png](attachment:127b424c6f631f90a6a551668fb45d6.png)

## lecture 7: multi-cycle datapaths
the different instructions take a different number of cycles to finish, we want to combine them togather\
### components:
- basic: memory, instruction register, register file, ALU, input/output signal controls
- new internal registers: IR, A, B, ALUOut, MDR
- from instruction format, derive connections and multiplexers
- feedbacks: ALU result to PC, ALUOut to memory address and register data, B to memory data
- next instruction: multiplexer to select the next instruction

### instructions:
#### load instruction RTL(register transfer level)

we want:
- $Reg[dest] = M[Reg[source] + sign-extention(addr)]$
- $dest = IR_{20-16}$
- $source = IR_{25-21}$
- $addr = IR_{15-0}$
the process:
- cycle1: $IR = M[PC],PC = PC + 4$
- cycle2: $A = Reg[source]$
- cycle3: $ALUOut = A + sign-extention(addr)$
- cycle4: $MDR = M[ALUOut]$
- cycle5: $Reg[dest] = MDR$

the internal registers serves as variables

#### execution steps: program format
- $IR = M[PC],PC = PC+4$
- $A = Reg[IR_{25-21}],\\B=Reg[IR_{20-16}],\\ALUOut = PC + sign-extention(IR_{15-0})<<2$
  - if R-type:
  $ALUOut = A\text{ } op\text{ } B;\\Reg[IR_{15-11}] = ALUOut$
  - if load or store:
  $ALUOut = A + sign-extention(IR_{15-0})$
    - if load:
    $MDP = M[ALUOut]\\Reg[IR_{20-16}] = MDR$
    - if store:
    $M[ALUOut] = B$
  - if beq:
  $\text{if } (A==B) \text{ then }PC = ALUOut$
  
#### state diagram
![image.png](attachment:image.png)

with the control signal it should be this:

![image-2.png](attachment:image-2.png)

## lecture 8: microprogram and microsequencer
### grouping signals
we want to group the states in the state diagram into some control signals for the control unit

for example:

$\Big(\begin{array}{c}ALUOp = 10\\ALUSrcA = 1\\ALUSrcB = 00\end{array}\Big)_{state6}\to \Big(\begin{array}{c}RegWrite\\MemtoReg = 0\\RegDst = 1\end{array}\Big)_{state7}$

we can define several values to achieve the task

- SRC1 = A denotes ALUSrcA = 1
- RegControl = WriteALU denotes RegWrite, MemtoReg = 0, RegDst = 1


so it can be change into 

$\Big(\begin{array}{c}ALUControl = FnCode\\Src1 = A\\Src1 = B\end{array}\Big)_{state6}\to \Big(\begin{array}{c}RegControl = WriteALU\end{array}\Big)_{state7}$

so the state diagram can be converted into this

we want to divide the 13 control signals into 7 fields
- each field covers one or more related control signals


### fields:
#### ALU fields:
$\begin{array}{c|c|c|c}
\text{field} & \text{field values} & \text{control values assignemnt} & \text{other}\\
\hline
\text{ALU control} & 
    \begin{array}{c}
    \text{Add}\\
    \text{FnCode}\\
    \text{Subtract}
    \end{array} & 
    \begin{array}{c}
    ALUOp = 00\\
    ALUOp = 10\\
    ALUOp = 01
    \end{array}\\
\hline
\text{SRC1} & 
    \begin{array}{c}
    \text{PC}\\
    \text{A}
    \end{array} & 
    \begin{array}{c}
    ALUSrcA = 0\\
    ALUSrcA = 1
    \end{array} &
    \begin{array}{c}
    \text{actually controls }\\
    \text{the multiplexer of A}
    \end{array}\\
\hline
\text{SRC2(actually for the multiplexer)} & 
    \begin{array}{c}
    \text{PC}\\
    \text{B}
    \end{array} & 
    \begin{array}{c}
    ALUSrcB = 0\\
    ALUSrcB = 1
    \end{array} &
    \begin{array}{c}
    \text{actually controls }\\
    \text{the multiplexer of B}
    \end{array}\\
\end{array}$

#### Read/Write/Sequencing fields

$\begin{array}{c|c|c|c}
\text{field} & \text{field values} & \text{control values assignemnt} & \text{other}\\
\hline
\text{Memory} & 
    \begin{array}{c}
    \text{Read PC}\\
    \text{Read ALU}\\
    \text{Write ALU}
    \end{array} & 
    \begin{array}{c}
    MemRead, IorD = 0, IRWrite\\
    MemRead, IorD = 1\\
    MemRead, IorD = 1
    \end{array} &
    \begin{array}{c}
    \text{IRWrite is the address in PC}\\
    \text{IorD is the address from ALUOut}
    \end{array}\\
\hline
\text{Reg Control} & 
    \begin{array}{c}
    \text{Read}\\
    \text{Write ALU}\\
    \text{Write MDR}
    \end{array} & 
    \begin{array}{c}
    A = Reg[IR_{25-21}],B=Reg[IR_{20-16}]\\
    RegWrite, MemtoReg = 0, RegDst = 1\\
    RegWrite, MemtoReg = 1, RegDst = 0
    \end{array}\\
\hline
\text{PCWrite Control} & 
    \begin{array}{c}
    \text{ALU}\\
    \text{ALUoutcond}\\
    \text{Jump addr}
    \end{array} & 
    \begin{array}{c}
    PC\text{ }source = 00, PC\text{ }write\\
    PC\text{ }WriteCond, PC\text{ }source = 01\\
    PC\text{ }write, PC\text{ }source = 10\\
    \end{array}\\
\text{Sequencing} & 
    \begin{array}{c}
    \text{seq}\\
    \text{fetch}\\
    \text{dispatch 1}\\
    \text{dispatch 2}
    \end{array} & 
    \begin{array}{c}
    \text{next state} = \text{current state}+1\\
    \text{goto label fetch, back to state 0}\\
    \text{next state from dispatch 1}\\
    \text{next state from dispatch 2}
    \end{array}\\
\end{array}$

so we can then turn the field assignment as a microprogram

![image-2.png](attachment:image-2.png)

and according to the field assignement and opcode, turn the program into the following table:

![image-3.png](attachment:image-3.png)

### microsequencor:

same as PC, a micro program counter

# part2:
aseembly
## lecture 1:
skip the intro
### Data types:
this is crucial for instructions like movl, movq
![image-3.png](attachment:image-3.png)

### address mode:

a register or immediate value specifies the memory address

#### expressions with the values
##### $(r_b,r_i,s)$
- this gets $Memory[R[r_b] + s* R[r_i]]$

- example: $(\%rdx,\%rcx,4)$
##### $Imm(r_b,r_i,s)$
- this gets $Memory[R[r_b] + s* R[r_i]+Imm]$

- example: $0x8(\%rdx,\%rcx,4)$
##### $(r_b,r_i)$
- this gets $Memory[R[r_b] + R[r_i]]$

- example: $(\%rdx, \%rcx)$
##### $Imm(r_b,r_i)$
- this gets $Memory[R[r_b] + R[r_i] + Imm]$

- example: $0x4(\%rdx,\%rcx)$
### moving data instructions:
- mov{x} Source, Destination(the x in the datatype of the moving data)

the registers are as follows, the number indicate the bits, for example %al takes 8 bits
![image-2.png](attachment:image-2.png)

the operand have there type:
- immediate: constant value given by a integer data
  - $\$$0x400, $\$$-526
- register: one of the 16
  - %rax %r13
  - %rsp is reserved for special use
- Memory: 8 consective bytes whose address is given by the register


#### movl operands:
$\text{movl}:\begin{array}{c|c}
\text{Source} & \text{Destination} & \text{Source, Destination} & \text{C analong}\\
\hline
\text{Immediate value} & \begin{array}{c}\text{Register}\\\text{Memory}\end{array} & \begin{array}{c}\text{movl }\$\text{0x4, %rax}\\\text{movl }\$\text{-147,(%rax)}\end{array} & \begin{array}{l}\text{temp = 0x4}\\\text{*p = -147}\end{array}\\
\hline
\text{Register} & \begin{array}{c}\text{Register}\\\text{Memory}\end{array} & \begin{array}{c}\text{movl }\text{%eax, %rax}\\\text{movl }\text{%esi,(%rcx)}\end{array} & \begin{array}{l}\text{temp2 = temp1}\\\text{*p = temp}\end{array}\\
\hline
\text{Memory} & \text{Register} & \text{movl (%rax). %eax} & \text{int temp = *p}
\end{array}$


## lecture 2
### movz & movs:
movx{x,y} : move with zero extention

movs{x,y} : move with sign extension

- these two are usually used to copy a smaller source value to a larger destination

- the source could be memory or register, but the destination has to be a register

- it fills the remaining bits of dest with 0 or sign bit

example: movzbq %al %rbx

### lea:
lea src, dest

- this is for loa effective address
- src is in memory address mode expression
- it sets the register dest to address computed by expression
- it does not do memory reference

difference of lea and mov
![image.png](attachment:image.png)

lea moves the address, mov moves the value stored in the address

### arithmetic operations
![image-2.png](attachment:image-2.png)
![image-3.png](attachment:image-3.png)

### conditionals
so we use 4 condition codes
- CF - carry flag(for unsigned)
- ZF - zero flag
- SF - Sign Flag(for signed)
- OF - Overflow Flage(for signed)

#### set conditional codes(implicit setting)
after arithmetic operation(not lea)
- CF set if carry out from most significant bit
- ZF set if the result == 0
- SF set if the result < 0
- OF set if two's complement overflow

#### set conditional codes(explicit setting by cmp)
cmp{x} src1, src2

the compare instruction is like a-b without destination

- CF set if carry out from most significant bit
- ZF set if the result == 0
- SF set if the result < 0
- OF set if two's complement overflow

#### set conditional codes(explicit setting by test)
test{x} src1, src2

the test instruction is like a&b without destination

- ZF set when a&b == 0
- SF
set when a&b < 0

### set instruction:
![image.png](attachment:image.png)

### jump instruction:
![image.png](attachment:image.png)

consider this as the java
```java
out:
   some code
   continue out;
```

## lecture 3
### do-while loop with assembly

so basically it just iterate through the code and check the conditionals, if satisfied, execute, else exit

```
fact_do: # consider this a bullet point
    movl $1, %eax
.L2: # another bullet point
    imull %edi, %eax
    subl $1, %edi
    cmpl $1, %edi
    jg .L2
    rep ret # just a safe version of return
```

### for loop

the for loop is similar:

just execute additional initialization and additional increment or other stuff

### switch case

you need multiple labels and jump to the corresponding one when the conditional is satisfied
![image.png](attachment:image.png)

## lecture 3
### stack discipline
- the stack grow toward lower addresses
- the %rsp reigister contains the lowest stack address, which is the addres of the top element

#### stack discipline: push
```
push Src
```
- fetch operand at Src
- Decrement %rsp by 8
- write operand at address given by %rsp

so what it does when we execute pushq %rbq is:
- subq $\$$8, %rsp
- movq %rbx, (%rsp)

#### stack discipline: pop
```
pop Src
```

- read operand at address %rsp
- Increment %rsp by 8
- write operand to Dest

so what it does when we execute popq %rbq is:
- movq (%rsp) %rbq
- addq $\$$8 %rsp

### procedure calls
when we call a function, we need to do the following:
- control flow
  - begin at procedure call
  - back when return
- pass data:
- memory:
  - alllocate during procedure execution
  - deallocate when return
#### overview:

the Caller calls the Callee to execute
![image.png](attachment:image.png)
basically the following:
- callee must know where to find the args and where to find the return address
- caller must know where to find the return val

so the Callee will first store the values in a stack and pop all of them
#### control flow:
- Procedure ```call label```
  - push the return address on stack
  - jmp to the label of the call function
- return address
  - after procedure call, the return value is in %rsp
- return:
  - pop the address from stack
  - jmp to address
#### example:
![image-3.png](attachment:image-3.png)

![image-2.png](attachment:image-2.png)
where the %rip stores the insturction pointer
![image-4.png](attachment:image-4.png)
it basically jumps to where the next instruction after the call should be

### pass in data:
![image.png](attachment:image.png)
the registers in circle are the arguments passed

Diana's Silk Dress Costs 89

- we dont have enough registers to hold all the local data
- so we use arrays or structure as local variable
- A procedure allocate space on the stack by decrementing the stack pointer


always move the return value to %rax

### example:
```java
long call_proc()
{
 long x1 = 1; // we need to store x1 in the stack, 8bytes since it is long
 int x2 = 2; // similar 
 short x3 = 3; // similar
 char x4 = 4; // similar
 proc(x1, &x1, x2, &x2, // function call, only the first 6 arguments are stored in the register, the rest in stack
 x3, &x3, x4, &x4);
 return (x1+x2)*(x3-x4); // these xs should be the previous value, we need to retrieve tham from stack
}
```

let's first analyze this code, we have 8 parameters, which are x1, the address of x1, x2, the address of x2, x3, the address of x3, x4, the address of x4

the thing is, we can only store at most 6 parameters in the registers, so the rest two, x4 and the address of x4 are going the be stored in the register


```java
call_proc:
 subq $32, %rsp // make the stack pointer point to the bottom of the stack
 movq $1, 24(%rsp) // x1 is long, takes 8bytes, 32-8=24
 movl $2, 20(%rsp) // x2 is int, takes 4 byttes
 movw $3, 18(%rsp) // x3 is short, takes 2bytes
 movb $4, 17(%rsp) // x4 is char, takes 1 byte
 // store these values in the stack for later use
 // we can only store at most 6 arguments(6 registers) in the register, so x4 and &x4 should stored in the stack
 leaq 17(%rsp), %rax // we cannot directly move from stack to stack, so we have to store this to a temporary register, the moved value is &x4
 movq %rax, 8(%rsp) // move &x4 
 movl $4,(%rsp) // move 4 to the end of the stack, this is for x4, the 7th argument, the length of each piece in stack is 8bytes, and argument 8, &x4
 leaq 18(%rsp), %r9 // move &x3 to register
 movw $3, %r8w // move x3 to register
 leaq 20(%rsp), %rcx // move &x2 to register
 movl $2, %edx // move x2 to register
 leaq 24(%rsp), %rsi // move &x1 to register
 movl $1, %edi // move x1 to register
 call proc // function call

 // the previous values of x1,x2,x3,x4 could have been changed, the code ask us to return
 // something based on the previous values, so moving from the stack
 movslq 20(%rsp),%rdx // previous x2 from stack
 addq 24(%rsp),%rdx // added by x1
 movswl 18(%rsp),%eax // previous x3 from stack, note this value is short
 movsbl 17(%rsp),%ecx // previous x4 from stack, we cannot directly do operations on values from the stack
 subl %ecx,%eax // subtract x3, x4
 cltq // extend %eax to a 64-bit integer(previously 32bits)
 imulq %rdx,%rax // multiply
 addq $32,%rsp // restore the stack pointer
 ret // return


```

## lecture 5: arrays
in the course, we only focus on Integrals, whether it is signed or not depends on the instruction used
- b: byte
- w: word
- l: double word
- q: quad word
the floating point numbers are stored on floating point registers, but is not included in the lecture

### Basic principle:
the memeory continuously allocate a region of $L*size$ bytes in the memory, depending on the data type

#### example:
consider an array reference is stored in the register %rdx, and %rax stores the index

then $\begin{array}{c}\text{C refernece} & \text{expression} & \text{type} & \text{value}\\
\text{val} & \text{mov %rdx, %rax} & \text{int*} & \text{val}\\
\text{val[0]} & \text{movl (%rdx), %rax} & \text{int} & \text{val[0]}\end{array}$

#### another example:
```C
int get_digit(int val[], int dig) // the memory reference of val[] is in %rdi, and the index in %rsi
{
 return val[dig];
}
```

```java
get_digit:
 movslq %esi, %rsi 
 movl (%rdi,%rsi,4), %eax // int take 4 bytes, so we move to the rdi + 4*rsi byte to get the desired value
 ret
```

### NestedArrays:

basically the same, if we want the element at column c and row r, the start address is A

then the address of the target row vector is $A + i*(c*k)$, the rest is the same as a 1-dimensional vector

### Multi-Level Array:
for example
```C
int cmu[5] = {1, 5, 2, 1, 3};
int mit[5] = {0, 2, 1, 3, 9};
int ucb[5] = {9, 4, 7, 2, 0};

int* univ[3] = {mit, cmu, ucb}; // this is only a pointer array
```

then univ will only stor the pointers that point to the threee arrays in *different* parts of the memory, a pointer is 8 bytes


the difference is as follows:
![image.png](attachment:image.png)

### structs:
also continuously stored in the memory

members of structs may have different types

#### example:/'
```C
typedef struct rec {
 int a[4];
 long i;
 struct rec *next;
} *rec_p;
```

```C
long get_i(rec_p r){ // pass in a pointer
 return r->i; // returns the point of the i in the struct
}
```

the corresponding assembly code 
```java
// at the start of the function, % rdi store the pointer to the struct
// three elements in struct,int a[4], 4*4 bytes, long i 8btyes, pointer next 8bytes
movq 16(%rdi), %rax // the point of i in the struct
ret
```

```C
int find_addr_of_array_elem
(rec_p r, long index){
 return r->a[index];
}

```

```java
// at the start of the function, %rdi store the pointer to the struct,
// %rsi stores the index
movl (%rdi, %rsi, 4), %eax
```

### alignment
some processors (not x86_64) requires alignment, but x64_86 suggests alignment

aligned means that any primitive object of K bytes must have an address that is a multiple of the K (1,2,4,8,16), for structs, it might not align

#### align for struct:
so each structure will have alignment requirement $K_{max}$,(counting array elements individually as elements)

![image.png](attachment:image.png)
#### programmar can reorder the elements to save space

## lecture 6:

### stroage technology:

- RAM(Random Access Memory)
  - static RAM: can find register file and use for cache memory
  - dynamic RAM: used for main memory
  - data is stored as long as the computer is powered
- ROM(read only memory)
  - non-volatile memory, data is stored permanantly
### Principle of Locality
- Locality: Progrmas tend to use the data and instructions with addresses near or equal to thos they have used recently

- Temporal locality
  - Recently refernce items are likely to be referenced again
- Spactial locality
  - Items with nearby addresses tend to be referenced again
  
for exmaple:

```C
int sum_array_cols(int a[M][N])
{
 int i, j, sum = 0;
 for (j = 0; j < N; j++) {
 for (i = 0; i < M; i++) {
 sum += a[i][j];
 }
 }
 return sum;
}

```

under the array layout of 
![image.png](attachment:image.png)

when i reaches N, j += 1, i = 0, it will do a jump in the memory not to adjacent by some far away address,

each time the sum is altered

- Temporal Locality: good
- Spacial Locality: Bad

under the array layout of 

![image-2.png](attachment:image-2.png)

- Temporal Locality: good
- Spacial Locality: good

### cache and memory hierachies
the cache is a memory to store data that is going to be accessed frequently, can be easily accessed with less time
![image-3.png](attachment:image-3.png)

If you look for data in the cache: teo cases:
the data is in the cache: hit

the data is not in the cache: miss, we look in to the memory in search of the data and replace one block of the cache that is not used recently with the value
- placement policy
- replacement policy

these two scenarios have huge difference in cost

#### Performance Metircs:
- Miss Rate = 1 - Hit Rate = $\frac{\text{misses}}{\text{accesses}}$
- Hit Rate = $\frac{\text{hits}}{\text{accesses}}$
- Miss Penalty: Additional time require because of a miss

- AMAT: avaerage time to access memory AMAT = Hit Time + Miss Rate * Miss Penalty

notice that 99% hit rate is twice as good as 97% hit rate because:
- Assume HT 1 cycle, MP 100 cyles
- 97% AMAT = 1 + (1-0.97)*100 = 4
- 99% AMAT = 1 + (1-0.99)*100 = 2

#### more cache:
just to avoid going in to the memory

### summary
![image-4.png](attachment:image-4.png)

#### cache organization:
- Cache Set(S)
  - A chache with $M = 2^m$ addresses is organised as a group of $S = 2^s$ cache sets with each cache set consists of $E$ cache line
- Block Size (B)
  - Each cache lines consists of $B = 2^b$ blocks of data
- Offset fields

we donoot want collision to happen(storing two data at the same address)

this basically forms a hash map

## lecture 7
- CPU sends a request for data
- TIO: in the cache:
  a m-bit address is seperarted into the following:$\begin{array}{|c|c|c|}\hline\text{Tag(T)} & \text{Index(I)} & \text{Offset(O)}\\\hline\end{array}$
  - Index: where to look in the cache
  - Tag: check that data is the block you want
  - Offset selects specified start byte within block
  
### Associativity:
- Each address mas to exactly one set
- Each set can store block in more than one way:
![image.png](attachment:image.png)

- Associativity(N): number of lines for each set
  - we now index into cache sets, of which there are C/B/N
  - Use the lowest $\log_2{C/B/N} = I$ bits of block address
  - Directed-mapped: N = 1, so $I = \log_2(C/B)$
  - fully-associative $N =C/B$, $I = 0$bits
  
#### example:
the data from address 0x1833

$0b\text{ }0001\text{ }1000\text{ }0011\text{ }0011$

![image-2.png](attachment:image-2.png)

### General Cache Organisation(S,N,B)

- N = blocks/lines per set
- S = # sets = $2^I$

![image-3.png](attachment:image-3.png)

### Read:
- locate set
- check if tag matchs
- if Yes then hit and locate data staring at the offset

#### N=1:
we compare the tags, and read from the offset bit ot the end, since N = 1

#### N = 2:
if tags match, then we read the bits starting from the offset

if no match, then one line the selected for replacement

### Misses:
- Compulsory miss:
  - Occurs on first access to a block
  
- Conflict miss:
  - occurs when the cache is large enough, but multiple data objects all map to the same slot
  - Direct-mapped caches ahve more conflicts misses than N-way set-associative
  
- Capacity:
  - Occurs when the set of active cache blcok is larger than the cache
  - for Full-associative , no such misses
  
### write hit:(write while the data is in the cache)
- write through:
  - write immedieately to memory and all caches between
  - always consistent
  - slow
- write back
  - defer write the memory until line is replaced
  - needs a dirty bit to indicate that line is different from memory
  - quick but complex
  
### write miss (write while the data is not in the cache)
- write allocate(load into cache and update the line)
  - more complex

- no write allocate (writes immediately to memory)
  - slower but simpler
  
![image-4.png](attachment:image-4.png)

### program optimizations:
- locality
- methods to achieve this:
  - Adjust memory accesss in the code to improve Miss Rate
    - may not always be available because you need to know how the machine work under your conditions
  - choose Algorithm properly
  - tranformt the loop
  
#### example: matrix multiplication:
- Assume:
  - Square matrix of doubles
  - Cache block size B=64, 8doubles
  - C << n
  
![image-5.png](attachment:image-5.png)

### some optimization:

seperate it into blocks and compute multiplication of the blocks


![image-7.png](attachment:image-7.png)


```python
import random
int(6*random.random())+1
```




    4




```python

```
