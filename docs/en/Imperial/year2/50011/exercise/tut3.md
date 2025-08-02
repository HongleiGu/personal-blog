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
# Problem 1:

**In the standard basis of $\mathbb{R}^2$, let the linear map f: $\mathbb{R}^2\to\mathbb{R}^2$ have matrix representation $A =\begin{bmatrix}4 & 2\\2 & 1\end{bmatrix}$**

**Find the eigenvalues and eigenvectors of $A$. Hence find the basis with respect to which $A$ is a diagonal matrix and find the matrix for this change of basis**

eigenvalue 0 or 5

eigenvector $[1,-2]^T$ or $[1,2]^T$

so $Q= \begin{bmatrix}1 & 1\\ -2 & 2\end{bmatrix}$

and the new basis $\begin{bmatrix}0 & 0\\0 & 5\end{bmatrix}$

# Problem 2:

**Show that an orthogonal transformation preserves the Euclidean length of any vector and the angle between any two vectors.**


Assume we have arbitrary two vectors $v_1, v_2$

then we have a orthogonal matrix $O$ 

then $O^TO = I$

then $||v|| = \sqrt{v^Tv}$

and $||Ov|| = \sqrt{(Ov)^T(Ov)} = \sqrt{v^TO^TOv} = \sqrt{v^Tv}$

and for the angle

$cos(<v1, v2>) = \frac{v_1^Tv_2}{||v_1||||v_2||}$

$\cos(<Ov_1, Ov_2>) = \frac{(Ov_1)^TOv_2}{||Ov_1|||Ov_2||} = \frac{v_1^TO^TOv_2}{||v_1||||v_2||} = \frac{v_1^Tv_2}{||v_1||||v_2||}$

# Problem 3:

$$A = \begin{bmatrix}
3 & 1 & 1\\
-1 & 3 & 1
\end{bmatrix}$$

**Find the singular value decomposition of A, i.e. find othorgonal matrices U and V and a diagonal matrix S with $A = USV^T$**

we need to do this in the opposite way using $AA^T$ because of the dimensions or decompose $A^T$

$$AA^T = \begin{bmatrix}3 & 1 & 1\\ -1 & 3 & 1\end{bmatrix}\begin{bmatrix}3 & -1\\ 1 & 3\\ 1 & 1\end{bmatrix} = \begin{bmatrix}11 & 1\\1 & 11\end{bmatrix}$$

eigenvalues $\lambda = 12, 10$

the eigenvectors are $[1,1]^T,[1,-1]^T$

normalised $\frac{1}{\sqrt{2}}[1,1]^T,[1,-1]^T$

so $V = \begin{bmatrix}\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}}\\\frac{1}{\sqrt{2}} & \frac{-1}{\sqrt{2}}\end{bmatrix}$

$u_1 = \frac{1}{\sqrt{12}} A^Tv_1 = \frac{1}{2\sqrt{6}}[2,4,2]^T = \frac{1}{\sqrt{6}}[1,2,1]^T$
$u_2 = \frac{1}{\sqrt{10}}A^Tv_2 = \frac{1}{2\sqrt{5}}[4,-2,0]^T = \frac{1}{\sqrt{5}}[2,-1,0]^T$

we dont need to extend since m = 2 in this case



and $S = diag(\sqrt{12},\sqrt{10}) = \begin{bmatrix}-2\sqrt{3} & 0\\0 & \sqrt{10}\end{bmatrix}$


# Problem 4:

**Use the property that an orthogonal transformation preserves the $l_2$ norm of a vector to show via the SVD representation that for any matrix $A\in\mathbb{R}^{m\times n}$ we have $||A||_2:=\sup_{||x||_2 = 1}||Ax||_2 = \sigma_1$ the largest singular value of A**

assume that $A = USV^T$ as SVD suggest, and $U, V^T$ are orthogonal matrix,

then the equation we want to prove is $||S||_2:=\sup_{||x||=1}||USV^Tx||2 = \sigma_1$


since orthogonal matrix preserve $l_2$ norm


$(*)\iff ||A||_2 := \sup_{||x|| = 1}||SV^Tx|| = \sup_{||x|| = 1}||Sx||_2 = \sigma_1$

since the largest possible outcome is x is a vector with 1 on the largest $\sigma$ and 0 otherwise

# Problem 5:

**Recall that if an eigenvalue $\lambda_0$ of a matrix $A\in\mathbb{R}^{n\times n}$ has multiplicity k, i.e. the characteristic polynomial $det(A - \lambda I)$ has a term $(\lambda-\lambda_0)^k$, then**

$k = nullity(A - \lambda_0I)^k$

**and any generalised eigenvector v for $\lambda_0$ satisfies $(A - \lambda_0I)^kv = 0$ Assume now that A is symmetric**

## (1)

**Show that any generalised eigenvector for $\lambda_0$ is actually an eigenvector i.e. show that $(A-\lambda_0I)^kv = 0$ implies $(A-\lambda_0I)v = 0$ Hint: assume $p\le k$ is the least positive integer with $(A-\lambda_0I)^pv = 0$. Obtain a contradiction if $1<p$ by considering the two cases when p is odd or even**

assume $p$ is the least positive integer that satisfies $(A-\lambda_0 I)^pv = 0$

since A is symmetric

$(A - \lambda_0I)^T = (A-\lambda_0I)^T = (A^T - \lambda_0 I^T) = (A-\lambda_0I)$

and since $(A-\lambda_0I)$ is symmetric $(A-\lambda I)^l$ is also symmetric

if $p$ is even then 

$$\begin{aligned}
||(A-\lambda_0I)^{\frac{p}{2}}v||_2^2 &=((A-\lambda_0I)^{\frac{p}{2}}v)^T((A-\lambda_0I)^{\frac{p}{2}}v)\\
&= v^T((A-\lambda_0I)^{\frac{p}{2}})^T(A-\lambda_0I)^{\frac{p}{2}}v\\
&= v^T(A-\lambda_0I)^{\frac{p}{2}}(A-\lambda_0I)^{\frac{p}{2}}v\\
&= v^T(A \lambda_0I)^p v\\
&= v^T 0 = 0
\end{aligned}$$

therefore since $\frac{p}{2}<p$ for $p>0$, we can find a smaller p that satisfy the equation so contradiction

for the odd case, we denote $p = 2n - 1$

$$\begin{aligned}
||(A-\lambda_0I)^nv||_2^2 &=((A-\lambda_0I)^nv)^T((A-\lambda_0I)^nv)\\
&= v^T((A-\lambda_0I)^n)^T(A-\lambda_0I)^nv\\
&= v^T(A-\lambda_0I)^n(A-\lambda_0I)^nv\\
&= v^T(A \lambda_0I)^{2n} v\\
&= v^T(A \lambda_0I)^{p+1} v\\
&= v^T(A\lambda_0 I)(A\lambda_0 I)^pv\\
&= v^T(A\lambda_0 I) 0 = 0
\end{aligned}$$

the rest is the same

## (2)

**Using Gram-Schmidt process, to show that we can select a set of k orthonormal vectors as the eigenvectors for $\lambda_0$**

from (1) we know that we can get  a set of k orthogonal eigenvectors with $(A-\lambda_0 I)^i v = 0$ for $1\le i\le k$

if $(A-\lambda_0I)^iv_1 = 0, (A-\lambda_0I)^jv_2 = 0$

then 

$$\begin{aligned}((A-\lambda_0I)^iv_1)^T((A-\lambda_0 I)^jv_2) &= v_1^T(A-\lambda_0I)^i(A-\lambda_0I)^jv_2\\
&= v_1^Tv_2 = 0*0 = 0\end{aligned}$$

so they are orthogonal

therefore we can use Gram-Schmidt to convert it to orthonormal

