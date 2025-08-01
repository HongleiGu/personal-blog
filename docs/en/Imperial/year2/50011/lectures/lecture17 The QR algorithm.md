---
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
level: Imperial
---
# Review: eigenvalue problems

Given $A\in\mathbb{C}^{m\times m}$, we seek $x\in\mathbb{C}^m,\lambda\in\mathbb{C}$, such that:

$Ax = \lambda x$

Review: Schur factorisation can reveal eigenvalues
- Any matrix A has a Schur factorisation $A = QTQ^*$ with upper-triangular T containing eigenvalues on its diagonal.
- Equivalently, this also means that $QAQ^* = T$
- Review: matrices $A'$ and $A$ are similar if $A' = P^{-1}AP$ and share rank, eigenvalues, trace, etc.
Key idea: we can iteratively construct a sequence of matrices $A^{(k)}$ such that $A^{(k+1)}$ is similar to $A^{(k)}$ and that $A^{(k)}$ converges to a real Schur matrix T as $k\to\infty$

# The QR algorithm

In 1961, the QR algorithm was introduced, which uses the QR-decomposition and is very efficient.

Let $A \in\mathbb{R}^{m\times m}$ satisfying certain conditions. After 'sufficient' iterations, the output is (almost) an upper triangular matrix, with the eigenvalues of A along its diagonal:

```pseudo
\begin{algorithm}
\caption{Basic QR iteration}
	\begin{algorithmic}
		\For{k = 1,2,3 do}
			\State $A^{(k-1)} = Q^{(k-1)}R^{(k-1)}$
			\State $A^{(k)} = R^{(k-1)}Q^{(k-1)}$
        \EndFor
	\end{algorithmic}
\end{algorithm}
```

Matrices $A^{(k)}$ are similar for $k = 1,2,3,\dots$

$$\begin{aligned}
A^{(1)} &= R^{(0)}Q^{(0)} &= (Q^{(0)})^TA^{(0)}Q^{(0)}\\
A^{(2)} &= R^{(1)}Q^{(1)} &= (Q^{(1)})^TA^{(1)}Q^{(1)}
\end{aligned}$$

Convergence of QR algorithm is non-examinable

# Convergence of QR algorithm in an important case

- Let $A\in\mathbb{R}^{m\times m}$ be symmetric PD with distinct eigenvalues $\lambda_1>\dots \lambda_m> 0$ such that $A = Q\Lambda Q^T$. Suppose $Q^T = LU$ with $U$ having positive diagonal elements. Then $A^{(k)}\to\Lambda$
- Proof(outline) $A = Q\Lambda Q^T\Rightarrow A^K = Q\Lambda^kQ^T$ (Q is orthogonal so $Q^TQ = I$)
- by using induction, we can get $A^k = Q_1\dots Q_kR_k\dots R_1$ 
	- base case: $A = Q_1R_1$, 
	- inductive step gives $$\begin{aligned}A^{k+1} &=(Q_1R_1)Q_1\dots Q_kR_k\dots R_1\\&=Q_1Q_2R_2Q_2\dots Q_kR_k & (R_1Q_1 = Q_2R_2)\\
		&=Q_1\dots Q_{k+1}R_{k+1}\dots R_1\end{aligned}$$
- therefore $Q\Lambda^kQ^T = Q_1\dots Q_kR_k\dots R_1$

$$\begin{aligned}
Q\Lambda^kQ^T &= Q_1\dots Q_kR_k\dots R_1\\
Q\Lambda^kLU &= Q_1\dots Q_kR_k\dots R_1\\
Q\Lambda^kL &= Q_1\dots Q_kR_k\dots R_1U^{-1}\\
Q\Lambda^kL\Lambda^{-k} &= Q_1\dots Q_kR_k\dots R_1U^{-1}\Lambda^{-k}\\
\end{aligned}$$

when $k\to\infty$, the off diagonal entries decay to zero due to the dominance of larger eigenvalues

therefore $\Lambda^kL\Lambda^{-k} \to I$ ($L$ is upper triangular and $\frac{\lambda_i}{\lambda_j}^k = 1$)

$$\begin{aligned}
QI &\approx (Q_1\dots Q_k)(R_k\dots R_1U^{-1}\Lambda^{-k})\\
&\approx\tilde{Q}\tilde{R}
\end{aligned}$$

with $\tilde{R} = (R_k\dots R_1U^{-1}\Lambda^{-k})$ having positive diagonal elements

By uniqueness of the QR decomposition in this case:
- $\tilde{Q}^{(k)} = Q_1\dots Q_k\to Q$ as $k\to\infty$
- $A^{(k)} = (\tilde{Q}^{(k)})^TA\tilde{Q}^{(k)}\to Q^TAQ$ as $k\to\infty$

# We can apply tricks from power iteration

Apply a shift $\mu^{(k)}$ at iteration k:

$$\begin{aligned}
A^{(k-1)} - \mu^{(k)}I &= Q^{(k-1)}R^{k-1}\\
A^{(k)} &= R^{(k-1)}Q^{(k-1)} + \mu^{(k)}I
\end{aligned}$$

If these shifts are good eigenvalue estimates, the last column of $\tilde{Q}^{(k)}$ converges quickly to an eigenvector

We can estimate $\mu^{(k)}$ using Rayleigh quotient, which is already in $A^{(k)}$, Cubic convergence as in Rayleigh quotient iteration

$$\begin{aligned}
A^{(k)}[m,m] &= e_m^TA^{(k)}e_m &=e_m^T(\tilde{Q}^{(k)})A\tilde{Q}^{(k)}e_m\\
&=q_m^{(k)}A q_m^{(k)}
\end{aligned}$$
where $q_m^{(k)}$ is the mth column of $\tilde{Q}^{(k)}$
