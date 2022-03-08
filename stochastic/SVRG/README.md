
# SVRG

**Key features:**
1. Fixes the problems in Stochastic GD - to reduce variance by recentering at each step


**Update Step**

Initialize y_0 ∈ Rn

Outerloop - 1 to K
<!-- $$
x_1 = y(k)
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/YG8qw6xccr.svg"></div>
Inner loop 1 to T
<!-- $$
x_{t+1} = x_t − η ∇f_i(x_t) − ( ∇f_i (y_k) - ∇f(y_k))
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/B8UkCgSlnO.svg"></div>
where i ∈ {1, . . . , m} is  selected at random

Update y_{k+1}
<!-- $$
y(s+1) = 1/T \sum x_t
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/GjmsqEZWka.svg"></div>