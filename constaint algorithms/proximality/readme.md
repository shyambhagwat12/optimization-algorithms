
# Proximal Operator/Proximal Subgradient

**Key features:**
1. Useful when function is not differentiable where the non differentiable part can be solved easily using the prox operator.
2. Generalization of Projection
3. Though not differentiable, algorithm provides similar rates of convergence as smooth functions.


**Proximal Gradient descent update step - f convex and L-Liptschitz Continuity**
<!-- $$
xt+1 = xt − ηt · ∇f(xt) 
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/vlquuAxSdZ.svg"></div>

<!-- $$
xt+1 ← Prox_{ηh} (y=xt+1) 
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/hQNHKKBdAI.svg"></div>


Proximal Operator
<!-- $$ 
Prox_{h}Y = argmin_{x} h(x) + 1/2 |x-y|^2
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/NM7wxisVNl.svg"></div>
<!-- $$ 
Prox_{ηh}Y = argmin_{x} h(x) + 1/2η |x-y|^2
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/XQ41gsnJSc.svg"></div>
when h(x) is below indicator function , we get back projection
<!-- $$
  \mathbf {I} _{X}(x):=
  \begin{cases}+ \infty ~&{\text{ if }}~x\notin X~,\\0~&{\text{ if }}~x\in X~.\end{cases}\
$$ --> 

Objective: To make sure h(x) is small , and in case its far away from y, then the quadratic term penalizes for x going far away from y.

<div align="center"><img style="background: white;" src="../../svg/K8QAK5pHKP.svg"></div>
Convergence Rate - Proximal - smooth:
<!-- $$
O(1/t)
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/ct9EflCmGQ.svg"></div>


Example - Projection onto simplex

