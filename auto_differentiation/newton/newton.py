
def loss(Xk, Xst):
    loss = np.log(np.square(la.norm(Xk - Xst)))
    return loss

def gradient(X,m):
    Z = 3 * np.dot(X,la.norm(X)) + m * X
    return Z

def hessian(X,m):
    Z = (3/la.norm(X)) * X @ X.T + (3*la.norm(X) + m)*np.identity(5)
    return Z

def newton_descent(X,Xst,m,stepsize,max_iter):
    error = []
    step = 0
    while step < max_iter:
        step += 1
        d = stepsize*np.dot(np.linalg.inv(hessian(X,m)),gradient(X, m))
        X = X - d
        error.append(loss(X,Xst))
    return error