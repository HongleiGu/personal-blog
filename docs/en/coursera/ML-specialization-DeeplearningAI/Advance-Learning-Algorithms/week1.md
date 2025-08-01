---
hide:
  - navigation # 显示右
  - toc #显示左
  - footer
  - feedback  
comments: true  #默认不开启评论
---
# Neural network intuition
## Neurons and the brain

this originate from algorithms that try to mimic the brain

so each neuron will transform a number to another neuron

we have multiple neurons in each layer

## Demand prediction

for example, we want to predict at what price will the buyer buy the shirt

it would be a logistic regression thing in previous courses

$\begin{aligned}
&x &=\text{price}\\
&f(x) &= \frac{1}{1 + e^{-(wx+b)}}
\end{aligned}$

now we denote $a = f(x)$ as the activation

this can be imagined to be what a single neuron is doing

so for example, we now take the price, the shipping cost, the marketing and the material of the shirt as input to predict the probability of this being a top seller

so we would see something like this

![pic1](docs/assets/AI/coursera/Advanced-Algorithms/week1-pic1.png)

now we treat the input as a single vector x and then we pass this through a layer to get another vector

the final layer is called output layer

the middle layers are call hidden layers

the first layer is called input layer

In logistic regression and linear regression, we need to do feature engineering, but in neural networks, it learn the feature engineering itself

We can of course have multiple hidden layers\

## Example: Recongnition Images

For example, Face recognition

we take in a picture of 1000 * 1000 pixels, then it would be a 1000*1000 matrix with the pixel value (we here only care when the pixel value is a single value)

we might build a neural network by passing the image to multiple hidden layers

and it output a probability of being person "aaa"

so for examples, the first hidden layer may learn simple edges, and the second part detect different parts of eys, ear etc. and another may learn the part of the face.

# Neural network model
## neural network layers

the neural network would look like this

$x\to\begin{bmatrix}\circ\\\circ\\circ\end{bmatrix}\to\begin{bmatrix}\circ\end{bmatrix}\to$

so we zoom in to the first layer

for each neuron, we have a weight w and bias b

so what the first neuron would do is it takes in a number or a vector x, $a_1 = g(\underbrace{\vec{w_1}\bullet\vec{x_1}+b_1}_{z_1})$ where g is the sigmoid function

then the second neuron would do similar stuff

$a_2 = g(\underbrace{\vec{w_2}\bullet\vec{x_2}+b_2}_{z_2})$

etc.

then values combine into a matrix

we introduce the notation $x^{[1]}$ to denote this is the param of the first layer

the output of layer 1 is the input of layer 2

so we could write $a_1^{[2]} = g(\vec{w_1}^{[2]}\bullet \vec{a}^{[1]} + b_1^{[2]})$

then for example, we want a binary classification, we set a threshold for the classification and make the output 1-dimensional

## More complex neural network

![pic2](docs/assets/AI/coursera/Advanced-Algorithms/week1-pic2.png)

so we have $\vec{a}^{[2]} = \begin{bmatrix}a_1^{[3]}\\a_2^{[3]}\\a_3^{[3]}\end{bmatrix}$

the general equation would be $a_j^{[l]} = g(\vec{w}_j^{[l]}\bullet\vec{a}^{[l-1]}+b_j^{[l]})$

- $a_j^{[l]}$ is the Activation value of layer l, unit(neuron) j
- g is the sigmoid function, will later be referenced as the activation function
- $\vec{a}^{[l-1]}$ is the output of layer l-1, or the previous layer
- $\vec{w}_j^{[l]},b_j^{[j]}$ are the parameters w and b of layer l unit j

## inference: making predictions (forward propagation)

scenario: we need to classify images of handwritten 0 and 1,

we pass in the image as a matrix with the pixel values

we use two hidden layers the first one with 25 units, the second one with 15 units

so we have $\vec{a}^{[1]} = \begin{bmatrix}g(\vec{w}_1^{[1]}\bullet \vec{x} + b_1^{[1]})\\\vdots\\g(\vec{w}_{25}^{[1]}\bullet \vec{x} + b_{25}^{[1]})\end{bmatrix}$

and 

$\vec{a}^{[2]} = \begin{bmatrix}g(\vec{w}_1^{[2]}\bullet \vec{x} + b_1^{[2]})\\\vdots\\g(\vec{w}_{15}^{[2]}\bullet \vec{x} + b_{15}^{[2]})\end{bmatrix}$

then we get $\vec{a}^{[3]} = [g(\vec{w}_1^{[3]}\bullet \vec{a}^{[2]}+b_1^{[3]})]$

we then compare $a_1^{[3]}$ with the pre-defined threshold (0.5)

this is called forward propogation

# Implementation in python

the layer a ![pic3](docs/assets/AI/coursera/Advanced-Algorithms/week1-pic3.png)

can be done by 

```python
import numpy as np
from tensorflow.keras.layers import Dense
x = np.array([200.0, 17.0])
layer_1 = Dense(units = 3, activation='sigmoid')
a1 = layer_1(x)
...
```

or in pytorch with 

```python
import numpy as np
import torch.nn as nn
x = np.array([200.0, 17.0])
layer_1 = nn.Sequential(
  nn.Linear(in_features = 2, out_features = 3),
  nn.Sigmoid()
)
a1 = layer(x)
```

## data in tensorflow

$\begin{bmatrix}1 & 2 & 3 \\ 4 & 5 & 6\end{matrix}$

```python
x = np.array([[1,2,3],[4,5,6]])
```

if we do  

```python
x = np.array([[200.0,17.0]])
layer_1 = Dense(units=3, activation='sigmoid')
a1 = layer_1(x) # something like tf.Tensor([[0.2,0.7,0.3]], shape=(1,3), dtype=float32)
```

## building a neural network

```python
layer_1 = Dense
```