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

# Function calls:

Changing the order of evaluation may change the result because of side-effects

Register targeting can be used to make sure arguments are computed in the right registers

At the point of the call several registers may already be in use
- But a function might be called from different call-sites
- Each call site might have different registers in use

## evaluation order:
in $f(a)  + f(b) + f(c)$

which sub-expression should we evaluate first?
- this is a correctness issue
- In C++ the order is undefined
- In Java the order is left to right

but in $(1 + f(x))*((2*y) + (3/u-z))$

then the order is a performance issue

## order of the execution
usually the order looks like this:

![slide5](lecture5-slide5.png)

we label the path

![slide5](docs/assets/Imperial/50006/lecture5-slide6.png)

in this graph
- a -> b -> c -> d -> e -> f -> g is a feasible path
- but a -> b -> f -> g should not be a feasible path, it is returning to the wrong address
- Control-flow graphs correctly capture control flow inside functions/methods, but not between them

# Saving the registers:

We must ensure that the function begin called doesnt clobber any registers which contain intermediate values

- Caller Saves: save registers being used by caller in case they are clobbered by callee
- Callee Saves: save only the registers which callee actually uses

Neither protocol is always the best

## example:

consider the following example"

section 1 has N registers in use and calls function F

section 2 has M registers in use and calls function F

function F needs P registers

![slide9](docs/assets/Imperial/50006/lecture5-slide9.png)

### caller save
so the caller save is generally

save all the registers before calling

and restore them on end of functions

a disadvantage of this is that if has to save all the P registers

## callee save


the function has to store all the registers the caller will need, which might be in use

## Intel IA32 convention:

in the 8 registers starting with e

%eax, %edx, %ecx are caller-save registers

%ebx, %esi, %edi are callee-save registers

%esp and %ebp are Stack pointer and Frame pointers

the rest:

![slide5](lecture5-slide12.png)

# Summary:
- Function calls can occur within expressions
- In some languages, the order in which such function are called is strictly defined
- The same issue arises with the order of evaluation of function arguments
- In some languages it is up to the compiler

- A function may be called from several call sites
- At each site, some set of registers may be user
- The function itself may need to use some registers
- The compiler needs to produce one implementation of the function body that can be used from different call sites
- Each processors type/OS has a Application Binary Interface (ABI) that specifies how function arguments and results are passed, and which registers must be preserved
- In the caller-saves protocol, the caller saves all the register it is using
- Typical ABIs are a hybrid - some registers are caller saves, some are calle saves