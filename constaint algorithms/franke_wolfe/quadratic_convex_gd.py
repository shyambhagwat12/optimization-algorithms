def compute_quadratic(Q,q, x):
    return np.asscalar(1 / 2 * x.T * Q * x + q.T * x )
def compute_derivate(Q,q, x):
    t= Q * x 
    t1= t + q
    return t1
def compute_gradient_descent(Q,q,x,f,stepsize):
    for i in range(49):
        d = compute_derivate(Q,q,x)
        x -= stepsize * d
        f.append(compute_quadratic(Q,q,x))