
# Franke Wolfe

**Key features:**
1. Constraint optimization algorithm.
2. Non euclidean approach - Dimension independent optimization
2. In some cases, (condition number - illformed), provides faster convergence using linear minimization in the direction of dot product of negative gradient and some vector(gamma) .



**Update Step**
<!-- $$
γ_{t}=2/t+1
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/szFrO6hqaY.svg"></div>
<!-- $$
y_t :=argmin⟨y,∇f(x_t)⟩ y∈X
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/t7CWXdSAWd.svg"></div>
<!-- $$
x_t+1 :=(1−γ_t)x_t+γ_ty_t =x_t+γ_t(y_t−x_t)
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/wBQCOJKilq.svg"></div>

**Convergence**
<!-- $$
f(x_t ) − f(x_∗) ≤ 2βR^2/T+1 
$$ --> 

<div align="center"><img style="background: white;" src="../../svg/5r3uDX0GGy.svg"></div>

Notes:
1) Unlike Projection, each step will not go outside of constraint set.
2) It will do a linear minimization (LP) to find the extreme points of the level sets
   and go in that direction.