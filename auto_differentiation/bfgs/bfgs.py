def exact_line_search(M,x,b):
    d = gradient(M,x,b)
    alpha = np.square(la.norm(d)) / np.dot(d ,hessian(M)).dot(d.T)
    return alpha

def bfgs(Xst,M,b,maxiter):
    np.random.seed(100)
    X = np.random.rand(1000)
    k = 0
    I = np.eye(len(X), dtype=int)
    Hk = I
    xk = X
    error = []
    while  k < maxiter:
        direction = -np.dot(Hk, gradient(M,xk,b))
        eta = exact_line_search(M,xk,b)
        xk_1 = xk + eta * direction
        sk = xk_1 - xk
        yk = gradient(M,xk_1,b) - gradient(M,xk,b)
        ro = 1.0 / (np.dot(yk, sk))
        Hk = np.dot(I - np.dot(ro,sk).dot(yk.T), np.dot(Hk, I - np.dot(ro,yk).dot(sk.T))) + np.dot(ro,sk).dot(sk.T)
        xk = xk_1
        k += 1
        error.append(loss(xk,Xst))
    return error