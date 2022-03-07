
# Basic Subgradient method Lipschitz Cvx

**Key features:**
1. For non smooth functions, basic subgradient method provides $\epsilon$ accurate solutions


**Subgradient method update step -

<!-- $$
xk+1 = xk − γg_{k}
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/7enjRmJHXO.svg"></div>
where gk - subdifferential 

where step size is based on the number of iterations t*

Example - Lasso - non smooth function
<!-- $$
\frac{1}{2}\|{Ax-b}\|_2^2 + \lambda \|{x}\|_1 
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/x5xetoMxm5.svg"></div>




<br>
<br>


**step size - based on t iterations**
<!-- $$
γ = 1/ \sqrt t
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/ObkCPSoAP0.svg"></div>



Convergence rate - $O(1/\sqrtt)$


**Useful Notes**

1. Subgradient at point is based on subdifferential. 
2. Subdifferential calculus -scaling,addition,affine transformation, max ,min etc similar to differentiable.
3. A function which has both differentiable and non differentiable. the differentiable part can be derived using first order. The non differentiable part can be computed using subdifferential.