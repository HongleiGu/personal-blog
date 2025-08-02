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

# Review: eigenvalue problems

Given $A\in\mathbb{C}^{m\times m}$, we seek $x\in\mathbb{C}^m,\lambda\in\mathbb{C}$, such that:

$$Ax = \lambda x$$

Review: factorizations can reveal eigenvalues
- If A is nondefective (a square matrix that has a set of n independent eignevectors), it can be diagonalised $A = X\Lambda X^*$
- If A is normal $(A^*A = AA^*)$, then $A = Q\Lambda Q^*$ where Q is a unitary matrix $Q= Q^{-1}$
- Any matrix has a Schur factorisation $A = QTQ^*$, with upper triangular T containing eigenvalues on its diagonal
Recall that solving characteristic polynomial is ill-conditioned. Most algorithms thus try to construct Schur factorisation
- Polynomials solved via eigenvalues of corresponding matrix
- Any eigenvalue solve must be iterative

# Motivation for power iteration

Definition: for $A\in\mathbb{R}^{m\times m}$m, a dominant eigenvalue is an eigenvalue with the largest modulus, A dominant eigenvector is and eigenvector corresponding to a dominant eigenvalue

The sequence $\frac{x}{||x||},\frac{Ax}{||Ax||},\frac{A^2x}{||A^2x||},\frac{A^3x}{A^3x},\dots$, can converge to the dominant eigenvector of A

Take some $x^{(0)},||x^{(0)}|| = 1$ and a symmetric $A = Q\Lambda Q^T$

$$\begin{aligned}
x^{(0)} &= a_1q_1 + a_2q_2 + \dots + a_mq_m\\
x^{(k)} &= x_kA^kx^{(0)} = c_k(a_1\lambda_1^k q_1 + a_2\lambda_2^k q_2 + \dots + a_m\lambda^m q_m)\\
&= c_k\lambda_1^k(a_1q_1 + a_2(\lambda_1/\lambda_2)^kq_2 + \dots + a_m(\lambda_m/\lambda_1)^kq_m)
\end{aligned}$$

```pseudo
\begin{algorithm}
\caption{Simple Power Iteration}
\begin{algorithmic}
    \State \textbf{Input:} Matrix A, initial vector x^{(0)}
    \State \textbf{Output:} Dominant eigenvector approximation x^{(k)}
    \For{k = 1,2,3$\dots$}
        \State $( \hat{x}^{(k)} = A x^{(k-1)} )$
        \State $( x^{(k)} = \frac{\hat{x}^{(k)}}{\max(\hat{x}^{(k)})} )$
    \EndFor
\end{algorithmic}
\end{algorithm}
```

# Power iteration with Rayleigh quotient

Given a symmetric matrix $A\in\mathbb{R}^{m\times m}$, the Rayleigh quotient of a vector $x\in\mathbb{R}^m$ is $r(x) = \frac{x^TAx}{x^Tx}$

If x is an eigenvector of A then $r(x) = \lambda$

Some interesting properties of Rayleigh quotient
- Eigenvectors of A are stationary points of the function $r(x)$
- $r(x)$ gives the quantity that acts most like an eigenvalue for $x'$ in a least square sense $r(x) = \arg\min_{\alpha}||Ax - \alpha x||_2$
- Writing x as a linear combination of the eigenvectors of A: $x = \sum_{j=1}^m a_jv_j$, we get that $r(x) = \sum_{j=1}^ma_j^2\lambda_j/\sum_{j=1}^m a_j^2$
- $r(x)$ is therefore quadratically accurate, i.e. $r(x) - r(v) = \mathcal{O}(||x = v||^2)$ as $x\to v$
We can include the Rayleigh quotient into the power iteration

# Power iteration and convergence

Convergence depends on ratio of eigenvalues. Assuming $|\lambda_1|>|\lambda_2|\le\dots\le|\lambda_m|\ge 0$ and $a_1\neq 0$

$$\begin{aligned}
||x^{(k)}-\alpha q_1|| &\le |\frac{\lambda_2}{\lambda_1}|^k|a_2|\text{ }||q_2||+\dots +|\frac{\lambda_m}{\lambda_1}|^k|a_m|\text{ }||q_m||\\
||x^{(k)} - \alpha q_1|| &=\mathcal{O}\Big(|\frac{\lambda_2}{\lambda_1}|^k\Big)
\end{aligned}$$
We can adjust ratio $\frac{\lambda_2}{\lambda_1} \Rightarrow \frac{\lambda_2 - \sigma}{\lambda_1-\sigma}$ using a shift $A - \sigma I$, since shifting A by $\sigma$ shifts the eigenvalues by $\sigma$

```pseudo
\begin{algorithm}
\caption{Power iteration}
	\begin{algorithmic}
		\For{$k = 1,2,3,\dots$}
			\State $\hat{x}^{(k)} = Ax^{(k-1)}$
			\State $x^{(k)} = \frac{\hat{x}^{(k)})}{\max(\hat{x}^{(k)})}$
			\State $\lambda^{(k)} = (x^{(k)})^TAx^{(k)}$
		\EndFor
	\end{algorithmic}
\end{algorithm}
```

# Motivation for inverse iteration

If we can find the biggest eigenvalue of $A\in\mathbb{R}^{m\times m}$, we can also find the smallest, since $A^{-1}$ has eigenvalues $\lambda_1^{-1},\dots,\lambda_m^{-1}$

Key idea: we can now adjust ratio $\frac{\lambda_1}{\lambda_2}\Rightarrow\frac{\lambda_1 -\sigma}{\lambda_2-\sigma}$

$$\begin{aligned}
x^{(k)} &= c_k((A-\sigma I)^{-1})x^{(0)}\\
&=c_k\Big(\frac{a_1}{(\lambda_1-\sigma)^k}q_1 +\dots +\frac{a_m}{(\lambda_m-\sigma)^k}q_m\Big)\\
&=c_k\frac{1}{(\lambda_J-\sigma)^k}\Big(a_jq_j +\sum_{i=1;i\neq j}^m a_i(\frac{\lambda_J -\sigma}{\lambda_i - \sigma})^kq_i\Big)
\end{aligned}$$
where $\lambda_J$ is the eigenvalue closest to $\sigma$

Power iteration on $(A - \sigma I)^{-1}$ finds eigenvalue closest to $\sigma$

# Inverse iteration and convergence

Convergence depends on ratio eigenvalues, Assuming $|\lambda-\sigma|<|\lambda_k-\sigma|\le\dots\le|\lambda_m -\sigma|$ and $a_J\neq 0$

$$\begin{aligned}
||x^{(k)}-\alpha q_J||&\le\Big|\frac{\lambda_J-\sigma}{\lambda_K-\sigma}\Big|\text{ }|a_K|\text{ }||q_K|| + \dots + \Big|\frac{\lambda_J-\sigma}{\lambda_m-\sigma}\Big|\text{ }|a_m|\text{ }||q_m||\\
||x^{(k)}-\alpha q_J|| &=\mathcal{O}\Big(\Big|\frac{\lambda_J-\sigma}{\lambda_K-\sigma}\Big|\Big)
\end{aligned}$$

This is an efficient way to compute eigenvectors for known eigenvalues

```pseudo
\begin{algorithm}
\caption{Power iteration}
	\begin{algorithmic}
		\For{$k = 1,2,3,\dots$}
			\State $\hat{x}^{(k)} = {\color{red}(A-\sigma I)^{-1}}x^{(k-1)}$
			\State $x^{(k)} = \frac{\hat{x}^{(k)})}{\max(\hat{x}^{(k)})}$
			\State $\lambda^{(k)} = (x^{(k)})^TAx^{(k)}$
		\EndFor
	\end{algorithmic}
\end{algorithm}
```

Matrix inversion $\mathcal{O}(m^3)$ at each k cannot be reduced by pre-factorisation

# Rayleigh quotient iteration

- Rayleigh quotient: eigenvector guess $\to$ estimated <span style="color:red">eigenvalue</span>
- Inverse iteration: eigenvalue guess $\to$ estimated <span style="color:red">eigenvector</span>
- The combined algorithm converges cubicly (Non-examinable)

```pseudo
\begin{algorithm}
\caption{Power iteration}
	\begin{algorithmic}
		\For{$k = 1,2,3,\dots$}
			\State $\hat{x}^{(k)} = {\color{red}(A-\lambda^{k-1} I)}^{-1}x^{(k-1)}$
			\State $x^{(k)} = \frac{\hat{x}^{(k)})}{\max(\hat{x}^{(k)})}$
			\State $\lambda^{(k)} = (x^{(k)})^TAx^{(k)}$
		\EndFor
	\end{algorithmic}
\end{algorithm}
```

# Returning to Schur factorisation

Any matrix has a Schur factorisation $A = QTQ^*$, with upper triangular T containing eigenvalues on its diagonal

equivalently, this also means that $QAQ^* = T$

Review: matrices $A'$ and $A$ are similar if $A' = P^{-1}AP$ and share rank eigenvalues trace, etc.
- Note that $A' + \Delta A' = P^{-1}(A+\Delta A)P\Rightarrow ||\Delta A'||_2 = ||\Delta A||_2$

Key idea: we can iteratively construct a sequence of matrices $A^{(k)}$ such that $A^{(k+1)}$ is similar to $A^{(k)}$ and that $A^{(k)}$ converges to a real Schur matrix T as $K\to\infty$

# The QR algorithm

In 1961, the QR algorithm was introduced, which uses the QR-decomposition and is very efficient

Let $A\in\mathbb{R}^{m\times m}$ satisfying certain conditions. After 'sufficient' iterations, the output is (almost) an upper triangular matrix, with the eigenvalues of A along its diagonal

```pseudo
\begin{algorithm}
\caption{Power iteration}
	\begin{algorithmic}
		\For{$k = 1,2,3,\dots$}
			\State $A^{(k-1)} = Q^{(k-1)}R^{(k-1)}$
			\State $A^{(k)} = R^{(k-1)}Q^{(k-1)}$
		\EndFor
	\end{algorithmic}
\end{algorithm}
```

Matrices $A^{(k)}$ are similar for $k = 1,2,3$

$$\begin{aligned}
A^{(1)} &= R^{(0)}Q^{(0)} = (Q^{(0)})^TA^{(0)}Q^{(0)}\\
A^{(2)} &= R^{(1)}Q^{(1)} = (Q^{(1)})^TA^{(1)}Q^{(1)}
\end{aligned}$$

Convergence of QR algorithm is non-examiable