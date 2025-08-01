---
hide:
  - navigation # 显示右
  - toc #显示左
  - footer
  - feedback  
comments: true  #默认不开启评论
---

# Overview of Machine Learning
some intro, skip

a discord-like website: https://community.deeplearning.ai/?utm_campaign=forum-engagement&utm_medium=long-form-courses&utm_source=coursera

# Supervised vs. Unsupervised learning
## What is machine learning?
### Machine learning algorithms
- Supervised learning
- Unsupervised learning
- Recommender systems
- Reinforcement Learning

## Supervised ML
### prediction
give input examples to predict y

Learns from being given the correct answers

for example, given an email, classify whether it is spam

or the classic example, given the house size in square feet predict the house price

so we predict a straight line or some twisted curve like this

![pic1](docs/assets/AI/coursera/SupervisedML/week1-pic1.png)

### classification

for example, breast cancer detection

we want to know if the tumor is maliganant or benign

in this case, the output is just 0 or 1, whereas in prediction, the output can be infinitely many kinds of numbers

if the input is multidimensional, we try to find a bounary to classify the different kinds of data

## Unsupervised ML

supervised learning learn from data labeled with the right answers

but in unsupervised learning, we dont know the right answers

one typical question is clustering, google news does this

# regression models
## linear regression

classic house price prediction according to house size

regression model predicts numbers, and since it is supervised, we have the correct answers, it an possibly get infinitely many outputs

if it a classification model, then if predicts categories, in this case we only have a small number of possible outputs

![pic2](docs/assets/AI/coursera/SupervisedML/week1-pic2.png)

### Terminologies:

training set: data used to train the model

- x = the feature, the input variable
- y = the output, the target variable
- m = number of training examples
- (x,y) = single training example
- $(x^{(i)}, y^{(2)})$ = $i^{th}$ training example

### how to train

![pic3](docs/assets/AI/coursera/SupervisedML/week1-pic3.png)

we use the data from the training set to fit with the model and get the predicted target

in the linear regression case the model is a linear function

$f_{w,b} = wx + b$

## cost functions

we have the model

$f_{w,b} = wx + b$

w and b are parameters

![pic4](docs/assets/AI/coursera/SupervisedML/week1-pic4.png)

w is the slop of the line, b is the y-intercept of the line

so we have $\hat{y}^{(i)} = f_{w,b}(x^{(i)}) = wx^{(i)} + b$

so the question is how to find the best w and b so that $\hat{y}^{(i)}$ is close to $y^{(i)}$ for all $(x^{(i)}, y^{(i)})$

so in the case we may use a squared error cost function cost function

$J(w,b) = \frac{1}{2m}\sum_{i=1}^m(\underset{error}{\hat{y}^{(i)} - y^{(i)}})^2$

or $J(w,b) = \frac{1}{2m}\sum_{i=1}^m(f_{w,b}x^{(i)} - y^{(i)})^2$

### intuition

we have a 

- model $f_{w,b} = wx + b$
- parameters w,b
- cost function $J(w,b) = \frac{1}{2m}\sum_{i=1}^m(f_{w,b}x^{(i)} - y^{(i)})^2$
- goal $\underset{w,b}{\min}J(w,b)$

so we simplify the model

$f_w(x) = wx$ so b = 0

$J(w) = \frac{1}{2m}\sum_{i=1}^m(f_{w}x^{(i)} - y^{(i)})^2$
we want to minimize J(w)

if we have thre data (1,1),(2,2),(3,3)


and $f_w(x)$ is $y = 0.5x$ or w = 0.5

then $J(w) = \frac{1}{2\times 3}[(0.5-1)^2 + (1-2)^2 + (1.5-3)^2]$

$J(w)$ gives us a plot of the parameter w and the cost, wto choose the best w, we just have to minimize $J(w)$


we have

$\begin{array}{ll}
\text{Model} & f_{w,b} = wx + b\\
\text{Parameters} & w,b\\
\text{Cost Function} & J(w,b) = \frac{1}{2m}\sum_{i=1}^m(f_{w,b}(x^{(i)})-y^{(i)}))^2\\
\text{Objective} & \underset{\text{minimize}}{w,b} J(w,b)
\end{array}$

# Gradient descent

objective, we have a function, and want to find the minimum of the function

say $\underset{\min}{w_1,\dots,w_n}J(w_1,\dots, w_n)$

Outline:

- we start with a point usually all 0
- keep changing the parameters to reduce the function until we settle at or near a minimum, a function may have different minimums

## implementation

at each step(taking the linear regression loss function as an example)

$w := w-\alpha\frac{\partial}{\partial w}J(w,b)$

$b := b-\alpha\frac{\partial}{\partial b}J(w,b)$

where $\alpha$ is the Learning rate, it take the partial derivative of the function

but note we want to simultaneouslt update w and b

so we may implement it this way 

$\text{temp_w} = w - \alpha\frac{\partial}{\partial w}J(w,b)$

$\text{temp_b} = b - \alpha\frac{\partial}{\partial b}J(w,b)$

$w :=\text{temp_w}, b:=\text{temp_b}$

it is incorrect to assign w somewhere in the middle as use have to use it to update b, you should not use the modified version

we have the following algorithm

$\begin{array}{l}
\text{repeat until convergence }\{\\
\quad w := w-\alpha\frac{\partial}{\partial w}J(w,b)\\
\quad b := b-\alpha\frac{\partial}{\partial b}J(w,b)\\
\}
\end{array}$

which means we subtract w by a small amout of the slope

## learning rate

we have $w := w - \alpha\frac{\partial}{\partial w}J(w)$

if $\alpha$ is small, each step is small, but if the learning rate is too large, then we are likely to go pass the minimum, may fail to converge

also. gradient descent may get stuck at local minimum instead of the global zero since the slope at local minimum is 0

when we get close to a local minimum, as slop decreases, each step is smaller

![pic5](docs/assets/AI/coursera/SupervisedML/week1.pic5.png)

## gradient descent for linear regression

we have

$\begin{array}{c}
\text{Linear regression model} & f_{w,b}(x) = wx + b\\
\text{Cost function} & J(w,b) = \frac{1}{2m}\sum_{i=1}^m(f_{w,b}(x^{(i)})-y^{(i)})^2\\
\text{Gradient descent algorithm} & \begin{array}{l}\text{repeat until convergence} \{\\
\quad w := w - \alpha\frac{\partial}{\partial w}J(w,b)\\
\quad b := b - \alpha\frac{\partial}{\partial b}J(w,b)\\
\}
\end{array}
\end{array}$

In the linear regression case

$\begin{aligned}
\frac{\partial}{\partial w} \\
&= \frac{\partial}{\partial w}\frac{1}{2m}\sum_{i=1}^m(f_{w,b}(x^{(i)})-y^{(i)})^2 \\
&= \frac{\partial}{\partial}\frac{1}{2m}\sum_{i=1}^m(wx^{(i)} + b - y^{(i)})^2 \\
&= \frac{1}{2m}\sum_{i=1}^m(wx^{(i)} + b - y^{(i)})2x^{(i)} \\
&= \frac{1}{m}\sum_{i=1}^m(wx^{(i)} + b - y^{(i)})x^{(i)}
\end{aligned}$

in the same way

$\frac{\partial}{\partial w} = \frac{1}{m}\sum_{i=1}^m(f_{w,b}(x^{(i)})-y^{(i)})$

we are using batch strategy, or using all the data in the training set to update the params