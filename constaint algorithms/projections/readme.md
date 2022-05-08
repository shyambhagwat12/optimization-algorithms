
# Projected Gradient Descent 

**Key features:**
1. Can solve Optimization convex problems with Constraints for instance -  white box problem where pertubations are bounded by constraints and constaints are seperable.
2. At t iteration if xt is outside of constraint set, the xt is projected back to constraint set.
3. Extension of Gradient/Subgradient descent with Projection step.
4. Special case of Proximal GD with identity- when to use etc in Proximal alg


**Projected Gradient descent update step - f convex and L-Liptschitz Continuity**
<!-- $$
xt+1 = xt − ηt · ∇f(xt) 
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/a9Ywst18S8.svg"></div>
<!-- $$
xt+1 ← Proj_C (w=xt+1) 
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/PdQq0uWXrf.svg"></div>

Projection Operator
<!-- $$ 
Proj_{X}x = argmin_{u} I_{X}(u) + 1/2 |u-x|^2
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/lmemDLZp8H.svg"></div>
where 
<!-- $$
  \mathbf {I} _{X}(x):=
  \begin{cases}+ \infty ~&{\text{ if }}~x\notin X~,\\0~&{\text{ if }}~x\in X~.\end{cases}\
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/rxjw2cWqGI.svg"></div>
Convergence Rate:
<!-- $$
O(1/\sqrt(t))
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/85Xyd74ux5.svg"></div>


Example - Projection onto simplex , Projection onto L2 Euclidian(Divide by L2 norm),L1 , Infinity Ball etc

Note:
1. This is not dimension independent. 
2. Hold for convex set alone.