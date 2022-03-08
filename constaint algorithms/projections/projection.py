def loss(A,b,x):
    return (np.linalg.norm(A.dot(x) - b, 1))


def grad(x,A,b):
    return (A.T).dot(np.sign(A.dot(x)-b))

def projection_simplex_sort(v, z=1):
    ### reference - https://arxiv.org/pdf/1309.1541.pdf
    n_features = v.shape[0]
    u = np.sort(v)[::-1]
    cssv = np.cumsum(u) - z
    ind = np.arange(n_features) + 1
    cond = u - cssv / ind > 0
    rho = ind[cond][-1]
    theta = cssv[cond][-1] / float(rho)
    w = np.maximum(v - theta, 0)
    return w

def projected_gd_step(x,A, b,mu):
        g = grad(x,A,b) 
        x = x - mu * g
        x = projection_simplex_sort(x,2)
        return x

def project_gradient_descent(update, X,y, eta, T=int(1e4)):
    loss_l = []
    np.random.seed(1000)
    x = np.random.rand(X.shape[1])
    for i in range(int(T)):
        x = update(x,X, y,eta)
        loss_l.append(loss(X,y,x))
    return loss_l
