
# Newtons method

**Key features:**
1. Quadratic convergence of certain optimization problems using hessian
2. Peforms affine transformation at each step fixing the ill conditioning scenario in GD
3. Runs in two phase - damped (using stepsize), undamped (quadratic - auto tuning)
4. Affine Invariant 
5. Self concordant using Barrier methods.



**Update Step**

<!-- $$
direction =−∇^2f(x)^{−1}∇f(x);
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/S6O0tldLkJ.svg"></div>

choose step size using backtracking line search
<!-- $$
x_{t+1} = x_t + η direction
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/KeMF1HxS3n.svg"></div>


