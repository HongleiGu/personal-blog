---
hide:
  - navigation # 显示右
  - toc #显示左
  - footer
  - feedback  
comments: true  #默认不开启评论
---
# classification with logistic regression,

the purpose of this algorithm is to do binary classification, for example, it this email spam

it could only have two results, yes or no, 0 or 1

if the result is 0, then it is in negative class

if the result is 1, then it is in posiive class

we can think of the data s as adding in an extra 0 or 1 feature to it

on possible measure is to pick a threshold, if passing the threshold then 1 else 0

![pic3](docs/assets/AI/coursera/SupervisedML/week3-pic1.png)

but if we add in another example

![pic2](docs/assets/AI/coursera/SupervisedML/week3-pic2.png)

this lead in some data to be miclassified

## logistic regression

we use th sigmoid function or the logicstic function as our model

![3](docs/assets/AI/coursera/SupervisedML/week3-pic3.png)

it only output between 0 and 1

$g(z) = \frac{1}{1+e^{-z}}$, $0<g(z)<1$

when z is large, g(z) is close to 1, when z is small, g(z) is close to 0

it intersects with the x axis at (0,0.5)

so we convert a linear regression model to a logicstic regression model

$z = \vec{w}\bullet\vec{x} + b\underset{z}{\to} g(z) = \frac{1}{1 + e^{-z}}$

so in logistic regrassion $f_{\vec{w}, b}(\vec{x}) = \frac{1}{1 + e^{\vec{w}\bullet\vec{x} + b}}$

the model gives the probability that the modle input belong to class 1

and $P(y = 0) + P(y = 1) = 1$

so sometimes we give the notation $f_{\vec{w}, b}(\vec{x}) = P(y=1|\vec{x};\vec{w},b)$


## decision boundary

so we have

$f_{\vec{w}, b}(\vec{x}) = g(\vec{w}\bullet\vec{x}+b) = \frac{1}{1 + e^{-(\vec{w}\bullet\vec{x}+b)}} = P(y=1|x;\vec{w},b)$

and if $f_{vec{w},b}(\vec{x})\ge 0.5$

if yes then $\hat{y} = 1$, else 0

we could analyse through the function that when $\vec{x}\bullet\vec{x} + b\ge 0, \hat{y} = 1$ else 0

so a deeper analysis, consider two features $x_1, x_2$

then $f_{\vec{w}, b}(\vec{x}) = g(\vec{w}\bullet\vec{x}+b) = \frac{1}{1 + e^{-(w_1x_1+w_2x_2+b)}}$

the decision boundary is when $\vec{x}\bullet\vec{x} + b = 0$ as this separates whether $\hat{y}$ is 1 or 0

the decision boundary is a line in the plot, one side is all the $\hat{y} = 1$, the other $\hat{y} = 0$

we can also do the same ploynimial regression to logistic regression

## cost function for logistic regression

for linear regression, we use the squared error

$J(\vec{w}, b) = \frac{1}{m}$

![pic4](docs/assets/AI/coursera/SupervisedML/week3-pic4.png)

if we try to apply gradient descent to the non-convex curve, we have a lot of local minimum, which is not desirable

so we use the logistic loss function

$L(f_{\vec{w},b}(\vec{x}^{(i)}),y^{(i)}) = \begin{cases}\begin{array}-\log(f_{\vec{w}, b}(\vec{x}^{(i)})) & y^{(i)} = 1\\-\log(1-f_{\vec{w}, b}(\vec{x}^{(i)})) & y^{(i)} = 0\end{array}\end{cases}$

so we get a curve that intersects the y axis at (1,0)

if $y^{(1)} = 1$, then as $f_{\vec{w},b}(\vec{x}^{(i)})\to 1$ then $loss\to 0$, as $f_{\vec{w},b}(\vec{x}^{(i)})\to 0$ then $loss\to \infty$

if $y^{(1)} = 0$, then as $f_{\vec{w},b}(\vec{x}^{(i)})\to 1$ then $loss\to \infty$, as $f_{\vec{w},b}(\vec{x}^{(i)})\to 0$ then $loss\to 0$

in this loss function, we can reach a global minimum

### a simplified cost and loss function

we combine the two cases in the last section

$L(f_{\vec{w},b}(\vec{x}^{(i)},y^{(i)})) = -y^{(i)}\log(f_{\vec{w}, b}(\vec{x}^{(i)}))- (1-y^{(i)})\log(1-f_{\vec{w}, b}(\vec{x}^{(i)}))$

if $y^{(i)} = 1$, we omit the second part, it is 0, if $y^{(i)} = 0$, we omit the first part, it is 0

so for the cost

$J(f_{\vec{w},b}(\vec{x}^{(i)},y^{(i)})) = -\frac{1}{m}\sum_{i=1}^m[y^{(i)}\log(f_{\vec{w}, b}(\vec{x}^{(i)}))- (1-y^{(i)})\log(1-f_{\vec{w}, b}(\vec{x}^{(i)}))]$

this is using the maximum likelihood principle, and is convex

## gradient descent with logistic regression

recall

$J(f_{\vec{w},b}(\vec{x}^{(i)},y^{(i)})) = -\frac{1}{m}\sum_{i=1}^m\Big[y^{(i)}\log(f_{\vec{w}, b}(\vec{x}^{(i)}))- (1-y^{(i)})\log(1-f_{\vec{w}, b}(\vec{x}^{(i)}))\Big]$

$\begin{array}{l}
\text{repeat until convergence }\{\\
\quad w := w-\alpha\frac{\partial}{\partial w}J(w,b)\\
\quad b := b-\alpha\frac{\partial}{\partial b}J(w,b)\\
\}
\end{array}$

so

$\frac{\partial}{\partial w_j}J(\vec{w},b) = \frac{1}{m}\sum_{i=1}^m(f_{\vec{w},b}(\vec{x}^{(i)})-y^{(i)})x_j^{(i)}$


$\frac{\partial}{\partial b}J(\vec{w},b) = \frac{1}{m}\sum_{i=1}^m(f_{\vec{w},b}(\vec{x}^{(i)})-y^{(i)})$

so

$\begin{array}{l}
\text{repeat until convergence }\{\\
\quad w := w-\alpha\Big[\frac{1}{m}\sum_{i=1}^m(f_{\vec{w},b}(\vec{x}^{(i)})-y^{(i)})x_j^{(i)}\Big]\\
\quad b := b-\alpha\Big[\frac{1}{m}\sum_{i=1}^m(f_{\vec{w},b}(\vec{x}^{(i)})-y^{(i)})\Big]\\
\}
\end{array}$

even though this looked the same as linear regression, the definition of f varies

same concepts:
- monitor gradient descent(learning curve)
- vectorization
- feature scaling

# overfitting

![pic5](docs/assets/AI/coursera/SupervisedML/week3-pic5.png)

![pic6](docs/assets/AI/coursera/SupervisedML/week3-pic6.png)

the problem of overfitting illustrates that the model fits overly well to the training set so generalisation to other data could be difficult

## addressing over fitting

- solution1: collect more training data, which may not always be a viable option
- solution2: select the features to include


all the feature + insufficient data $\to$ overfitting

disadvantge of the feature selection includes loss of important features

- solution3: regularization, encourages the model to use small parameters

## cost function with regularization

for example, if the model is $w_1x + w_2x^2 + w_3x^3 + w_4 x^4 + b$

then we would make $w_3$, $w_4$ really small so that the impact of them would also be extrmemly small to the model

originally the cost function look somewhat like this

$\underset{\min}{\vec{w},b}\frac{1}{2m}\sum_{i=1}^m(f_{\vec{w},b}()\vec{x}^{(i)}- y^{(i)})^2$

with normalisation, we apply a large coefficient to the $x_3$, $x_4$

so $\underset{\min}{\vec{w},b}\frac{1}{2m}\sum_{i=1}^m(f_{\vec{w},b}()\vec{x}^{(i)}- y^{(i)})^2 + 1000w^2_3 + 1000_4^2$

the as we do gradient descent to minimize th cost function, we make $w_3, w_4$ very small, so $w_3x_3^3, w_4x^4$ would also be very small

but for example, if we have a dataset where we have 100 features, all of them are important

then regualrization would do $J(\vec{w},b) = \frac{1}{2m}\sum_{i=1}^m(f_{\vec{w},b}(\vec{x}^{(i)})-y^{(i)})^2 + \frac{\lambda}{2m}\sum_{j=1}^n w_j^2$

to apply regularization on every weight

where lambda is a regularization parameter, and strictly greater than 0

we scale it be $\frac{1}{2m}$ so that regularization have the same effect when dataset enlarges

## regularized linear regression
recall

$\underset{\vec{w},b}{\min}J(\vec{w},b) = \underset{\vec{w},b}{\min}\frac{1}{2m}\sum_{i=1}^m(f_{\vec{w},b}(\vec{x}^{(i)})-y^{(i)})^2 + \frac{\lambda}{2m}\sum_{j=1}^n w_j^2$

and gradient descent

$\begin{array}{l}
\text{repeat until convergence }\{\\
\quad w_j := w_j-\alpha\frac{\partial}{\partial w}J(w,b)\\
\dots\\
\quad b := b-\alpha\frac{\partial}{\partial b}J(w,b)\\
\}\text{simultaneous update}\\
\end{array}$

with regularization, the derivative has a extra term

$\frac{\partial}{\partial w_j}J(\vec{w},b) = \frac{1}{m}\sum_{i=1}^m(f_{\vec{w},b}(x^{(i)})-y^{(i)})x_j^{(i)} + \frac{\lambda}{m}w_j$

we dont apply regularization to b, so no change to the b derivative

$\begin{array}{l}
\text{repeat until convergence }\{\\
\quad w_j := w_j-\alpha\Bigg[\frac{1}{m}\sum_{i=1}^m\Big[(f_{\vec{w},b}(x^{(i)})-y^{(i)})x_j^{(i)}\Big] + \frac{\lambda}{m}w_j\Bigg]\\
\dots\\
\quad b := b-\alpha\Big[\frac{1}{m}\sum_{i=1}^m(f_{\vec{w},b}(\vec{x}^{(i)})-y^{(i)})\Big]\\
\}\text{simultaneous update}\\
\end{array}$

so we could see

$w_j:=\underset{w_j(1-\alpha\frac{\lambda}{m})}{w_j-\alpha\frac{\lambda}{m}w_j} - \\underset{\text{normal gradient descent}}{alpha\frac{1}{m}\sum_{i=1}^m(f_{\vec{w},b}(\vec{x}^{(i)})-y^{(i)})x_j^{(i)}}$

## regularized logistic regression

the idea is the same


$J(\vec{w},b) = -\frac{1}{m}\sum_{i=1}^m\Big[y^{(i)}\log(f_{\vec{w},b}(\vec{x}^{(i)})) + (1-y^{(i)})\log(1-f_{\vec{w},b}(\vec{x}^{(i)}))\Big] + \frac{\lambda}{2m}\sum_{j=1}^nw_j^2$


$\begin{array}{l|l}
\text{repeat until convergence }\{\\
\quad w_j := w_j-\alpha\frac{\partial}{\partial w_j}J(\vec{w},b) &=\frac{1}{m}\sum_{i=1}^m(f_{\vec{w},b}(\vec{x}^{(i)})-y^{(i)})x_j^{(i)} + \frac{\lambda}{m}w_j\\
\dots\\
\quad b := b-\alpha\frac{\partial}{\partial b}J(\vec{w},b) &=\frac{1}{m}\sum_{i=1}^m(f_{\vec{w},b}(\vec{x}^{(i)})-y^{(i)})\\
\}\text{simultaneous update}\\
\end{array}$

also, this look the same like linear regression, but the f is not the same