
#  ISTA /FISTA

**Key features:**
1. ISTA - Proximal GD - very useful for Lasso/Sparse problems
2. FISTA - Accelerated Fista with momentum



**FISTA - Update step:**
Refer to constraint alg/fista
<!-- $$
x_{t+1} = argmin_x |y{t+1}| + (x - y_{t+1}∇f(y_{t+1}) + 1/2η |x-y_{t+1}|^2 + r(w)
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/NlBw7QGbhp.svg"></div>


<!-- $$
Prox_r(y_{t+1} - η∇f(y_{t+1})).
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/gYaN4cSYsR.svg"></div>