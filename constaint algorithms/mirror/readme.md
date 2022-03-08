
# Mirror Descent

**Key features:**
1. Non euclidean approach - Dimension independent optimization



**Update Step**
<!-- $$
∇Φ(yt+1) = ∇Φ(xt) − ηg_{t}, 
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/rxwZFs0nfy.svg"></div>
<!-- $$
g_{t} ∈ ∂f(xt)
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/hIz86dIUfz.svg"></div>
<!-- $$
xt+1 ∈ Prox ΦX (yt+1) 
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/N0Bvbm79wh.svg"></div>

Where Φ is mirror map and Mirror map has to be strictly convex and differentiable


**Bregman Divergence**
<!-- $$
D_\Phi(x, y) = \Phi(x) - \Phi(y) - \nabla \Phi(y)^\mathsf{T}(x - y) 
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/WVugHAaaMx.svg"></div>

