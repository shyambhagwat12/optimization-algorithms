
# Basic Stochastic Gradient Descent

**Key features:**
1. In case of machine learning problems such as minimizing loss, the number of training samples could be very high. Gradient descent goes over all of the traning data at each step.
2. Stochastic gradient descent, will randomly select a sample and minimize instead of going over entire data set. Objective is eventually - it will converge , but with significantly lesser steps.
3. Particularly useful in low variance settings



**Update Step**

Initialize x0 ∈ X

<!-- $$
x_{t+1} = x_t−η∇f_{i}(x_t)
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/lqxB1demtG.svg"></div>
where i ∈ {1, . . . , m} is  selected at random

