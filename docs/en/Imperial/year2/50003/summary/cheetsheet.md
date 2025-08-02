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
# Register Machines:
**register machine**(RM) is specified by finitely many **registers** each capable of storing a natural number and a **program** consisting of a finite list of the form label:body where, for i = 0,1,2.., the $(i+1)^{th}$ instruction has Label $L_i$
**Instructions**: $R^+\to L'$,: R += 1, moveto L'; $R^-\to L',L''$, if R > 0 then R-=1, moveto L' else moveto L''; $HALT$: end of program

**configuration**: $c = (\ell, r_0,\dots, r_n)$, the current label and all the corresponding values of $R_i$, **initial configurations** $\ell = 0$, $r_i$ may not be zero!! **halting configuration**: the last configuration of the finite computation (can be HALT or an error, attempting to jump to label that does not exist); **Non-halting Computations**: not all programs eventually halt, recall the graphical representations of the register machines

**partial functions**: $(x,y)\in f\wedge (x,y')\in f\to y = y'$
- $f(x) = y$ means $(x,y) \in f$
- $f(x)\downarrow$ means $\exists y\in Y(f(x) = y)$
- $f(x)\uparrow$ means $\neg\exists y\in Y(f(x) = y)$
- $x\rightharpoonup y$ = set of all partial functions from X to Y
- $x\to Y$ = set of all (total) functions from X to Y
A partial function is total if $\forall x\in X, f(x)\downarrow$

