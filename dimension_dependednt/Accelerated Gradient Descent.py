def compute_quadratic(Q,q, x):
    return np.asscalar(1 / 2 * x.T.dot(Q).dot(x))
def compute_derivate(Qd,xd):
    tq = np.dot(Qd,xd)
    return tq
def compute_gradient_descent(Q,x,stepsize):
    error = []
    for i in range(49):
        d = compute_derivate(Q,x)
        x = x - stepsize * d
        if (i % 1 == 0):
            error.append(compute_quadratic(Q,q,x))
            assert not np.isnan(error[-1])
    return error

def compute_agd(Q,x,stepsize,k):
    error = []
    y_t = x
    for i in range(49):
        y_t1 = x - stepsize*compute_derivate(Q,x)
        x = (((1 + (math.sqrt(k) -1)/(math.sqrt(k) +1)) * y_t1)  -  (((math.sqrt(k) -1)/(math.sqrt(k) +1)) * y_t))
        y_t = y_t1
        if (i % 1 == 0):
            error.append(compute_quadratic(Q,q,x))
            assert not np.isnan(error[-1])
    return error