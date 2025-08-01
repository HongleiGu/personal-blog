---
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
level: Imperial
---
# Problem1:

## (i) 
**Show that for any pair of vector $v,w\in\mathbb{R}^m$,we have $|v\bullet w|\le ||v||_1||w||_{\infty}$**

assume $v = [v_1, v_2, \dots, v_m]^T$ and $w = [w_1, w_2,\dots, w_m]^T$

by definition

$||v||_1 = \sum_{i=0}^m|v_i|$

$||w||_{\infty} = \max\{w_1, w_2,\dots, w_m\}$

$$\begin{aligned}|v\bullet w| &= |v^Tw| \\
&= |\sum_{i=0}^m v_iw_i| &\text{(by definition of dot product)}\\
&= \sum_{i=0}^m|v_iw_i| & (\text{since }\Big|\sum a\Big| = \sum|a|)\\
&\le \sum_{i=0}^m|v_i||w_i| & \text{(by triangular inequality)}\\
&\le \sum_{i=0}^m|v_i|\Big|||w||_{\infty}\Big| & \text{(by definition of l}_{\infty})\\
&=||w||_{\infty}\sum_{i=0}^m|v_i| & \text{(since }||w||_{\infty}\text{ doesnt involve i)}\\
&=||w||_{\infty}||v||_1 & \text{(by definition of }||v||_i)\\
&=||v||_1||w||_{\infty} & \text{(since both terms are scalar values)}
\end{aligned}$$


## (ii)

**As in the lecture notes, define the $l_{\infty}$ matrix norm for $A\in\mathbb{R}^{m\times n}$ by**

$$||A||_{\infty}:=\underset{1\le i\le m}{\max}||a^i||_1$$

**where $a^i$ is the ith row of A. Show carefully using part (i) that**

$$||A||_{\infty} = \max\{||Ax||_{\infty}:||x||_{\infty}\le 1\} = \max\{||Ax||_{\infty}: ||x||_{\infty} = 1\}$$

by the definition of $||A||_{\infty}$

we have 

for any $A\in\mathbb{R}^{m\times n}, x\in\mathbb{R}^{n}$

assume $A = [a^1, a^2,\dots, a^m], x = [x_1, x_2, \dots, x_n]^T$ where $\forall i\le m, a_i\in\mathbb{R}^n$

$$||A||_{\infty} = \max_{1\le i\le m}||a^i||_1$$
and
$$\begin{aligned}||Ax||_{\infty} 
&=\max_{1\le i\le m}||a^ix||_1 & \text{(by  definition of the norm)}\\
&\le\max_{1\le i\le m}||a^i||_1||x||_{\infty} & \text{by part (i)}
\end{aligned}$$

if at this point, we add the constraint of $||x||_{\infty}$, or $\Big|\Big|[x_1,x_2,\dots,x_n]\Big|\Big|\le 1$ as required in $\max\{||Ax||_{\infty}:||x||_{\infty}\le 1\}$

then
$$
\begin{aligned}||Ax||_{\infty} 
&\le \max_{1\le i\le m}||a^i||_1||x||_{\infty} & \text{by part (i)}\\
&=\max_{1\le i\le m}||a^i||_1 & \max||x||_{\infty} = 1\\
&= ||A||_{\infty}
\end{aligned}\\ $$


and also, since the max can only be obtained when $||x||_{\infty} = 1$

we proved that

$$\max\{||Ax||_{\infty}:||x||_{\infty}\le 1\} = \max\{||Ax||_{\infty}:||x||_{\infty}= 1\}$$

in conclusion $$||A||_{\infty} = \max\{||Ax||_{\infty}:||x||_{\infty}\le 1\} = \max\{||Ax||_{\infty}: ||x||_{\infty} = 1\}$$
# Problem 2:

**Find the singular value decomposition of the matrix**

$$A = \begin{bmatrix}3 & 2 & 2\\2 & 3 & -2\end{bmatrix}$$

A is in dimension $2\times 3$ with $3 > 2$

therefore, we first calculate 
$$A^TA = \begin{bmatrix}3 & 2\\2 & 3\\ 2 &-2\end{bmatrix}\begin{bmatrix}3 & 2 & 2\\2 & 3 & -2\end{bmatrix} =\begin{bmatrix}13 & 12 & 2\\12 & 13 & -2\\2 & -2 & 8\end{bmatrix}$$

then we find the eigenvectors of $A^TA$

$det(A^TA-\lambda) = 0$

$det(\begin{bmatrix}13-\lambda & 12 & 2\\12 & 13-\lambda & -2\\2 & -2 & 8-\lambda\end{bmatrix}) = 0$

so $(13-\lambda)((13-\lambda)(8-\lambda)-4) - 12(12(8-\lambda)-(-4)) + 2(-24-2(13-\lambda)) = 0$
$(13-\lambda)(\lambda^2-21\lambda +100) - 12(100-12\lambda) + 2(-50+2\lambda) = 0$
$(13\lambda^2-273\lambda+1300) + (-\lambda^3 +21\lambda^2 - 100\lambda) - 1200+144\lambda + (-100 + 4\lambda) = 0$
$-\lambda^3 + 34\lambda^2 -255\lambda = 0$

$\lambda(\lambda -9)(\lambda -25) = 0$

therefore the eigenvalues are 25, 9, 0

(skipping eigenvector calculation)

and the eigenvectors are $v_1 = [1,1,0]^T, v_2 = [1,-1,4]^T, v_3 = [-2,2,1]^T$

after normalising

$v_1 = \frac{1}{\sqrt{2}}[1,1,0]^T, v_2 = \frac{1}{3\sqrt{2}}[1,-1,4]^T,v_3 = \frac{1}{3}[-2,2,1]$

therefore in the SVD expression of $A = USV^T$

$V = [v_1,v_2,v_3] = \begin{bmatrix}\frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{6} & -\frac{2}{3}\\\frac{\sqrt{2}}{2} & -\frac{\sqrt{2}}{6} & \frac{2}{3}\\0 & \frac{2\sqrt{2}}{3} & \frac{1}{3}\end{bmatrix}$


and each $u_i = \frac{1}{\sigma_i}Av_i$

therefore 
- $u_1 = \frac{1}{5}Av_1 = \frac{1}{5}\begin{bmatrix}3 & 2 & 2\\2 & 3 & -2\end{bmatrix}\begin{bmatrix}\frac{\sqrt{2}}{2}\\\frac{\sqrt{2}}{2}\\0\end{bmatrix} = \begin{bmatrix}\frac{\sqrt{2}}{2}\\\frac{\sqrt{2}}{2}\end{bmatrix}$
- $u_2 = \frac{1}{3}Av_2 = \frac{1}{3}\begin{bmatrix}3 & 2 & 2\\2 & 3 & -2\end{bmatrix}\begin{bmatrix}\frac{\sqrt{2}}{6}\\-\frac{\sqrt{2}}{6}\\\frac{2\sqrt{2}}{3}\end{bmatrix} = \begin{bmatrix}\frac{\sqrt{2}}{2}\\-\frac{\sqrt{2}}{2}\end{bmatrix}$
- $u_3$ does not exist since the corresponding eigenvalue is 0

therefore $U = \begin{bmatrix}\frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2}\\\frac{\sqrt{2}}{2}&-\frac{\sqrt{2}}{2}\end{bmatrix}$

and $S = diag(\sigma_1,\sigma_2) = diag(5,3) = \begin{bmatrix}5 & 0 & 0\\0 & 3 & 0\end{bmatrix}$

in conclusion the SVD representation is

$\begin{bmatrix}3 & 2 & 2\\2 & 3 & -2\end{bmatrix} = A = USV^T = \begin{bmatrix}\frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2}\\\frac{\sqrt{2}}{2}&-\frac{\sqrt{2}}{2}\end{bmatrix}\begin{bmatrix}5 & 0 & 0\\0 & 3 & 0\end{bmatrix}\begin{bmatrix}\frac{\sqrt{2}}{2} & \frac{\sqrt{2}}{2} & 0\\\frac{\sqrt{2}}{6} & -\frac{\sqrt{2}}{6} & \frac{2\sqrt{2}}{3}\\-\frac{2}{3} & \frac{2}{3} & \frac{1}{3}\end{bmatrix}$

# Problem 3:

**Show that for any matrix $A\in\mathbb{R}^{mn}$ the two matrices $A^TA$ and $A$ have the same nullspace, Deduce carefully that the three matrices $A, A^TA, AA^T$ have the same rank**

first we prove that $A^TA$ and $A$ have the same nullspace

1. $null(A^TA)\subseteq null(A)$
	for arbitrary vector $x\in\mathbb{R}^m$
	
	if $x\in null(A)$, or $Ax = 0$
	
	then $A^TAx = A^T(Ax) = A^T0 = 0$
	
	so $x\in null{A^TA}$
	
	therefore $null(A^TA)\subseteq null(A)$
2. $null(A)\subseteq null(A^TA)$
	 for arbitrary vector $x\in\mathbb{R}^m$
	
	 if $x\in null(A)$, or $A^TAx = 0$
	
	then $x^TA^TAx = 0$
	
	therefore $(Ax)^T(Ax) = 0$
	
	thus $Ax =  0$, or $x\in null(A)$
	
	so  $null(A)\subseteq null(A^TA)$
in conclusion $null(A) = null(A^TA)$

the in the exact similar way we can also prove $null(A) = null(A^TA)$

and since $null(M) + rank(M) = \text{cols of M}$ for any matrix M

$A\in\mathbb{R}^{m\times n}.A^TA\in\mathbb{R}^{n\times n}$

therefore, they have the same number of columns and the same rank

$rank(A) = rank(A^TA) = n - null(A)$

in addition using singular value decomposition

assume

$A = USV^T$

then $AA^T = USV^T(USV^T)^T = USV^TVS^TU^T$

and $A^TA = (USV^T)^TUSV^T = VS^TU^TUSV^T$

since V and U in singular value decomposition are orthonormal

therefore $UU^T = 0, VV^T = 0$

$AA^T = USS^TU^T, A^TA = VS^TSV^T$

in SVD, S is a diagonal matrix with the singular values on the diagonals, we assume S is shape $n\times m$, with $m\le n$ (the other case is just the reverse)

then $SS^T$ would give a $m\times m$ square matrix with the n eigenvalues on the diagonal and the rest 0

$S^TS$ would give a $n\times n$square matrix with the n eigenvalues the fill the whole diagonal

or to be more specific $rank(SS^T) = rank(S^TS)$

also notice that $A^TA = (A^TA)^T$ therefore $A^TA$
is symmetric, the same for $AA^T$

therefore $AA^T = USS^TU^T$ and $A^TA = VS^TSV$ posses the form of the spectral theorem, so the eigenvalues of $AA^T$ is the non-zero elements on the diagonal of $SS^T$ and the eigenvalues of $A^TA$ is the non-zero elements on the diagonal of $S^TS$

as mentioned before, the non-zero elements of $SS^T$ and $S^TS$ are the same, so $AA^T$ and $A^TA$ possess the same set of eigenvalues,

therefore $rank(AA^T)=rank(A^TA)$

in conclusion $rank(A) = rank(AA^T) = rank(A^TA)$


# Problem 4:

**which one of the following two matrices A and B does not have a Cholesky decomposition? Find the Cholesky decomposition of the other matrix**

$$A = \begin{bmatrix}25 & 15 & -5\\15 & 18 & 0\\-5 & 0 & 11\end{bmatrix}, B = \begin{bmatrix}5 & 7 & 1\\7 & 6 & 4\\1 & 4 & 13\end{bmatrix}$$


for a matrix to have a Cholesky decomposition, the matrix has to be semi-definite

therefore we test we a random vector x say $x = [1,-1,0]$

$$\begin{aligned}x^TAx &= \begin{bmatrix}1 & -1 &0\end{bmatrix}\begin{bmatrix}25 & 15 & -5\\15 & 18 & 0\\-5 & 0 & 11\end{bmatrix}\begin{bmatrix}1\\-1\\0\end{bmatrix} \\&= \begin{bmatrix}10 & -3 & -5\end{bmatrix}\begin{bmatrix}1\\-1\\0\end{bmatrix} = 13 >0\end{aligned}$$

$$\begin{aligned}x^TAx &= \begin{bmatrix}1 & -1 &0\end{bmatrix}\begin{bmatrix}5 & 7 & 1\\7 & 6 & 4\\1 & 4 & 13\end{bmatrix}\begin{bmatrix}1\\-1\\0\end{bmatrix} \\&= \begin{bmatrix}-2 & 1 & -3\end{bmatrix}\begin{bmatrix}1\\-1\\0\end{bmatrix} = -3 < 0\end{aligned}$$

We cannot say A is semi-positive definite, but we are certain that B is not semi-positive definite

so B is the one that does not have a Cholesky decomposition

therefore, assume $A = LL^T$ where L is an upper triangular matrix

$$L = \begin{bmatrix}l_{11} & 0 & 0\\l_{21} & l_{22} & 0\\l_{31} & l_{32} & l_{33}\end{bmatrix}$$

$$\begin{aligned}&\begin{bmatrix}25 & 15 & -5\\15 & 18 & 0\\-5 & 0 & 11\end{bmatrix} = A\\
=&LL^T = \begin{bmatrix}l_{11} & 0 & 0\\l_{21} & l_{22} & 0\\l_{31} & l_{32} & l_{33}\end{bmatrix}\begin{bmatrix}l_{11} & l_{21} & l_{31}\\0 & l_{22}& l_{32}\\0 & 0 & l_{33}\end{bmatrix}\\
=&\begin{bmatrix}
l_{11}^2 & l_{11}l_{21} & l_{11}l_{31}\\
l_{11}l_{21} & l_{21}^2 + l_{22}^2 & l_{21}l_{31} + l_{22}l_{32}\\
l_{11}l_{31} & l_{21}l_{31} + l_{22}l_{32} & l_{31}^2+l_{32}^2+l_{33}^2\\
\end{bmatrix}\end{aligned}$$

therefore 

$$\begin{cases}
\begin{array}{c}
l_{11}^2 = 25 & \Rightarrow &l_{11} = 5\\
l_{11}l_{21} = 15 & \Rightarrow& l_{21} = 3\\
l_{11}l_{31} = -5 & \Rightarrow& l_{31} = -1\\
\hline
l_{21}^2 + l_{22}^2 = 18 &\Rightarrow& l_{22} = 3\\
l_{21}l_{31} + l_{22}l_{32} &\Rightarrow& l_{32} = 1\\
\hline
l_{31}^2 + l_{32}^2 + l_{33}^2 = 11 & \Rightarrow& l_{33} = 3
\end{array}
\end{cases}$$

in conclusion, the Cholesky decomposition is 

$$A = LL^T = \begin{bmatrix}5 & 0 & 0\\3 & 3 & 0\\-1 & 1 & 3\end{bmatrix}\begin{bmatrix}5 & 3 & -1\\0 & 3 & 1\\0 & 0 & 3\end{bmatrix}$$

