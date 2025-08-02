---
encrypt_content:
  level: Imperial
  password: Raymond#1234
  username: hg1523
level: Imperial
---
# Problem 1:

**we consider the system of linear equations $Ax = b$, where:**

$$A= \begin{bmatrix}2 & 1 \\ 1 & 1\end{bmatrix};b = \begin{bmatrix}-0.5\\0.5\end{bmatrix}$$

## a)
**Find the solution vector x**

$x = \begin{bmatrix}-1\\1.5\end{bmatrix}$

## b)
**Show that the given system, in the form of a quadratic function $f(x) = x^TAx - 2x^Tb$, where $x^T = [x_1,x_2]$, can be expressed as $f(x) = x_1 - x_2 + 2x_1^2 + 2x_1x_2 + x_2^2$**

in this system let $\vec{x} =\begin{bmatrix}x_1\\x_2\end{bmatrix}$

$x^TAx = \begin{bmatrix}2x_1 + x_2 & x_1 + x_2\end{bmatrix} \begin{bmatrix}x_1 \\ x_2\end{bmatrix} = 2x_1^2+2x_1x_2 + x_2^2$

$2x^Tb = 2\begin{bmatrix}x_1 & x_2\end{bmatrix}\begin{bmatrix}-0.5\\0.5\end{bmatrix} = x_2 - x_1$

so the system can be expressed in the term

## c)
**Show that f(x) has a local minimum at some $x_*$ and find the values of $x_*$ and $f(x_*)$**

since $f(x) = x_1 - x_2 + 2x_1^2 + 2x_1x_2 + x_2^2$

so $f_{x_1} = 1 + 4x_1 + 2x_2$. $f_{x_2} = -1 + 2x_1 + 2x_2$ $\nabla f = \begin{bmatrix}1+4x_1+2x_2\\-1+2x_1+2x_2\end{bmatrix}$

so $f_{x_1x_1} = 4, f_{x_1x_2} = 2,f_{x_2x_1} = 2,f_{x_2x_2} =2,\nabla^2f = \begin{bmatrix}4 & 2 \\2 & 2\end{bmatrix}$

for any vector $\begin{bmatrix}a\\b\end{bmatrix}$

$$x^TAx = \begin{bmatrix}4a+2b&2a+2b\end{bmatrix}\begin{bmatrix}a\\b\end{bmatrix} =4a^2 + 2ab + 2ab + 2b^2 = b^2 + (2a +b)^2\ge 0$$

therefore this is PD

therefore it has a local minimum

when $\nabla f = 0$ $x_1 = -1,x_2 = 1.5$ $x_* = \begin{bmatrix}-1\\1.5\end{bmatrix}$

## d)
**Starting from an initial guess of $x^{(0)} = [0,0]$, compute 4 iterations of steepest descent (you can use a fixed length of 0.5)**

$$x^{(k+1)} = x^{(k)} - \alpha \nabla f(x^{(k)})$$
- step1: $x^{(0)} = [0,0], \nabla f(x^{(0)}) = [1,-1], x^{(1)} = [-0.5,0.5]$
- step2: $x^{(1)} = [-0,5,0.5],\nabla f(x^{(1)}) = [0,-1],f^{(2)} = [-0.5,1]$
- step3: $x^{(2)} = [-0.5,1],\nabla f(x^{(2)}) = [1,0],f^{(3)} = [-1,1]$
- step4: $x^{(3)} = [-1,1],\nabla f(x^{(3)}) = [-1,-1],x^{(4)} = [-0.5,1.5]$

# Problem 2:

**Consider the matrix**

$$A = \begin{bmatrix}
4 & 1 & -2\\
1 & 3 & -1\\
-2 & -1 & 5
\end{bmatrix}$$

**and the initial guess $x^{(0)} = [1;1;1]$. Perform two iterations of the power iteration method and compute the Rayleigh quotient after two iterations**

## power iteration:

step 1: 

$$\hat{x}^{(1)} = Ax^{(0)} = \begin{bmatrix}3\\3\\2\end{bmatrix}$$
$$x^{(1)} = \begin{bmatrix}1\\1\\\frac{2}{3}\end{bmatrix}$$
step 2:

$$\hat{x}^{(2)} = Ax^{(1)} = \begin{bmatrix}\frac{11}{3}\\\frac{10}{3}\\\frac{1}{3}\end{bmatrix}$$
$$x^{(2)} = \begin{bmatrix}1\\\frac{10}{11}\\\frac{1}{11}\end{bmatrix}$$

the Rayleigh quotient is thus

$\frac{(x^{(2)})^TAx^{(2)}}{(x^{(2)})^Tx^{(2)}} = \frac{\frac{945}{121}}{\frac{222}{121}} \approx 4.26$

<span style="color:red">the modal answer used the norm of the vector when normalising, but the slides means to use the max element, The results are the same, but require recheck, stick to the norm I suppose</span>


# Problem 3

**Inverse iteration depends on the solution of a system of equations $(A-\mu I)w = v$ that may be exceedingly ill-conditioned, with condition the order of $\epsilon_{\text{machine}}^{-1}$. We know that it is impossible in general to solve ill-conditioned systems accurately. Is this not a fatal flaw in the algorithm**

**Show as follows that the answer is no-that ill-conditioning is not a problem in inverse iteration. Suppose A is a real symmetric matrix with one eigenvalues much smaller than the others in absolute value (without loss of generality, we are taking $\mu = 0$, or $A = (\tilde{A}-\mu I)$). Suppose $v$ is a vector with components in the directions of all the eigenvector $q_1,\dots, q_m$ of A and suppose $Aw = v$ is backward stably, yielding a computed vector $\tilde{w}$. Show that although $\tilde{w}$ may be far from w $\frac{\tilde{w}}{||\tilde{w}||}$ will not be far from $\frac{w}{||w||}$. Note: you do not need a rigorous proof here-the goal is to gain some intuition as to why inverse iteration works in practice**

to be consistent with the tutorial notes and to make the symbols clear

the inverse iteration can be represented as

$x_{n+1} = \frac{(A-\mu I)x_n}{||(A-\mu I)x_n||}$

we take $\mu = 0$ and $\lambda_1$ is the eigenvalue of A with the smallest absolute value

then $w = A^{-1}x_n = \sum_{i=1}^mc_i\frac{1}{\lambda_i}q_i$ (see lecture slide 4, pick k = -1)

$$\begin{aligned}
w &= A^{-1}v = \sum_{i=1}^m c_i\frac{1}{\lambda_i}q_i\\
&=\frac{1}{\lambda_1}\Big(c_1q_1+\sum_{i=2}^m\frac{\lambda_1}{\lambda_i}c_iq_i\Big)\\
&\approx \frac{1}{\lambda_1}c_1q_1\qquad \text{since}\frac{\lambda_1}{\lambda_i}\to 0\forall i\neq 1
\end{aligned}$$
$\frac{w}{||w||}\approx \frac{\frac{c_1}{\lambda_1}q_1}{||\frac{c_1}{\lambda_1}q_1||} = q_1$

$\tilde{w} = w + \delta w$
$$\begin{aligned}
\tilde{w} &= \tilde{A^{-1}}\tilde{x_n}\\&=(A^{-1} +\delta A^{-1})(x_n +\delta x_n) \\&= (A^{-1}+\delta A^{-1})(\sum_{i=1}^m(c_i + \delta c_i)q_i)\\
&=A^{-1}v + A^{-1}(\sum_{i=1}^m(\delta c_i)q_i) + \delta A^{-1}(\sum_{i=1}^m(c_i + \delta c_i)q_i)\\
&= w + A^{-1}(\sum_{i=1}^m(\delta c_i)q_i) + \delta A^{-1}(\sum_{i=1}^m(c_i + \delta c_i)q_i)
\end{aligned}$$

$$\begin{aligned}
\delta w &= A^{-1}(\sum_{i=1}^m(\delta c_i)q_i) + \delta A^{-1}(\sum_{i=1}^m(c_i + \delta c_i)q_i)
\\&=A^{-1}(\sum_{i=1}^m(\delta c_i)q_i) + \delta A^{-1}(\sum_{i=1}^m(c_i)q_i) + O(\epsilon^2)\\
&=A^{-1}\delta x_n + \delta A^{-1}x_n + O(\epsilon^2)
\end{aligned}$$

therefore, we need to know what $\delta A^{-1}$ is

we apply a small turbulence matrix $\epsilon_{ij}$ to matrix A, then the change can be expressed in term of partial derivative

since $f(x) - f(y)\approx \frac{df}{dx} * (x-y)$ (mean value theorem), therefore $\delta A^{-1} = \sum_{i,j}\epsilon_{ij}\frac{\delta A^{-1}}{\delta a_{ij}}$

this part is the formal proof of this

where $\epsilon_{ij}\frac{\delta A^{-1}}{a_{ij}}$ is the turbulence of a single element

recall that $(A+UV^T)^{-1} = A^{-1} + \alpha A^{-1}UV^TA^{-1},\alpha = -\frac{1}{1 + V^TA^{-1}U}$

(Sherman-Morrison formula, A is invertible, U and V are vectors that the shape of A and UV^T are the same)

let $u = [0,\dots,\underset{ith}{1},0,\dots,0],v = [0,\dots,\underset{jth}{\epsilon_{ij}},0,\dots,0]$

then $uv^T = \Delta A_{ij}$

therefore $(A+\Delta A_{ij})^{-1} = A^{-1}-\frac{A^{-1}\Delta A_{ij}A^{-1}}{1+\epsilon_{ij}A_{ji}^{-1}}$

therefore 

$$\begin{aligned}\frac{\partial A^{-1}}{\partial a_{ij}} &= \lim_{\epsilon_{ij}\to 0}\frac{1}{\epsilon_{ij}}[(A+\Delta A_{ij})^{-1} - A^{-1}] \\&= -A^{-1}\underset{1 \text{ at }(i,j)}{\begin{bmatrix}0 & \dots & 0\\\vdots & 1 & \vdots\\0 & \dots & 0\end{bmatrix}}A^{-1}\end{aligned}$$

$\frac{\partial A^{-1}}{x} = -A^{-1}\frac{\partial A}{\partial x}A^{-1}$

therefore $\delta A^{-1} \approx \sum_{ij}\epsilon\frac{\partial A^{-1}}{\delta a_{ij}} = -A^{-1}\delta A A^{-1}$

so back to the analysis

$$\begin{aligned}
\delta w & \approx A^{-1}\delta x_n + \delta A^{-1}x_n\qquad\text{(omit higher order terms})\\
&= A^{-1}\delta x_n - A^{-1}\delta AA^{-1}x_n\\
&= A^{-1}(\delta x_n - \delta A A^{-1}x_n)\\
&= A^{-1}(\delta x_n - \delta A w)\\
\end{aligned}$$

we can make the term $\tilde{v} = (\delta x_n - \delta A w) = \sum_{i=1}^m\Delta c_iq_i$

$w = A^{-1}x_n$

$\tilde{w} = w + \delta w = A^{-1}(x_n + \tilde v) = A^{-1}\tilde{x_n}$

therefore, this is actually proving if $A^{-1}b$ is backwards stable, then $\tilde{x} = \tilde{A}^{-1}\tilde{b} = A^{-1}\tilde{b}$

back to the proof, $\delta w\approx = \sum_{i=1}^m\frac{\delta c_i}{\lambda_i}q_i\approx\frac{\delta c_1}{\lambda_1}q_1$ (this is exactly the same as the w approximation above)

$\frac{\tilde{w}}{||\tilde{w}||} \approx\frac{\frac{1}{\lambda_1}(c_1 + \delta c_i)q_i}{||\frac{1}{\lambda_1}(c_1 + \delta c_i)q_i||} = q_i$

# Problem 4:

**The QR algorithm consists of computing the sequence defined by $A^{(k+1)} = R^{(k+1)}Q^{(k+1)}$ where $A^{(k)} = Q^{(k+1)}R^{(k+1)}$ is the QR decomposition of $A^{(k)}$. Prove the following results for this sequence, for example, by induction**

## a)
**for $k\ge 0, Q^{(1)}R^{(1)}Q^{(1)}Q^{(2)}\dots Q^{(k)} = Q^{(1)}Q^{(2)}\dots Q^{(k)}Q^{(k+1)}R^{(k+1)}$**
we use induction:

### base case: k = 0

then $Q^{(1)}R^{(1)} = Q^{(1)}R^{(1)}$

this is of course true

### induction hypothesis

$k\ge 0, Q^{(1)}R^{(1)}Q^{(1)}Q^{(2)}\dots Q^{(k)} = Q^{(1)}Q^{(2)}\dots Q^{(k)}Q^{(k+1)}R^{(k+1)}$

we want to show

$k\ge 0, Q^{(1)}R^{(1)}Q^{(1)}Q^{(2)}\dots Q^{(k+1)} = Q^{(1)}Q^{(2)}\dots Q^{(k+1)}Q^{(k+2)}R^{(k+2)}$
from the hypothesis

$A^{(1)}Q^{(1)}Q^{(2)}\dots Q^{(k)} = Q^{(1)}Q^{(2)}\dots Q^{(k)}A^{(k+1)}$

then we are actually trying to prove that

${Q^{(k+1)}}^{-1}\dots {Q^{(2)}}^{-1}{Q^{(1)}}^{-1}A^{(1)}Q^{(1)}Q^{(2)}\dots Q^{(k+1)} = A^{(k+2)}$

with the assumption ${Q^{(k)}}^{-1}\dots {Q^{(2)}}^{-1}{Q^{(1)}}^{-1}A^{(1)}Q^{(1)}Q^{(2)}\dots Q^{(k)} = A^{(k+1)}$

or ${Q^{(k+1)}}^{-1}A^{(k)}Q^{(k+1)} = A^{(k+1)}$

but notice that ${Q^{(k+1)}}^{-1}A^{(k)} = R^{(k+1)}$

so $R^{(k+1)}Q^{(k+1)} = A^{(k+1)}$

which is obviously true

