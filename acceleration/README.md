
# Acceleration Gradient Descent

**Key features:**
1. Faster lower bounds O(1/T^2)
2. If the problem is ill conditioned, GD convergence is zigzag. AGD overcomes using the momentum of previous iterations.


**Useful Background:**

**Polyaks Heavy Ball Algorithm:**
Use of momentum as an extrapolation
<!-- $$
wt+1 = wt - γ∇f(wt)  + β(wt - wt1) 
$$ --> 

<div align="center"><img style="background: white;" src="../svg/wUzI7MZ6wA.svg"></div>

**AGD/ Nesterov's Update step:**
Same as heavy ball. Gradient at extrapolated position - Y_t+1
<!-- $$
y_{t+1} = x_{t} + β(x_{t} -x_{t-1})
$$ --> 

<div align="center"><img style="background: white;" src="../svg/GvU0FXdgOy.svg"></div>
<!-- $$
x_{t+1} = y_{t+1}  -γ∇f(y_{t+1})
$$ --> 

<div align="center"><img style="background: white;" src="../svg/yKJMx2emVm.svg"></div>

Convergence/lower bound - O(1/T^2) 

**Accelerated  GD /FISTA:**
Refer to constraint alg/fista
<!-- $$
x_{t+1} = argmin_x |y{t+1}| + (x - y_{t+1}∇f(y_{t+1}) + 1/2η |x-y_{t+1}|^2 + r(w)
$$ --> 

<div align="center"><img style="background: white;" src="../svg/53GAafalU1.svg"></div>

