def subgradient(x, A, b, t, lam, c=1e-3):
    g = np.dot(np.dot(A.T, A), x) - np.dot(A.T, b) + np.sign(x) * lam
    eta = c / np.sqrt(t+1)
    x -= eta * g
    return x
    
def loss(A,b,lam, x):
    return 0.5 * np.sum(np.square(np.dot(A, x) - b)) + lam * np.sum(np.abs(x))

        
def prox(x, s, t=1.):
    return np.sign(x)*np.maximum(np.abs(x)-s,0)
    

def ista_step(x,A, b,reg):
        g = np.dot(np.dot(A.T, A), x) - np.dot(A.T, b)

        hessian = np.dot(A.T, A)
        beta = la.eigvals(hessian).max()
        step_size = 1/beta

        x = x - step_size * g
        x = prox(x, reg * step_size)
        return x

def fista_step(x,A, b,z,reg,mu):

        g = np.dot(np.dot(A.T, A), x) - np.dot(A.T, b)
        hessian = np.dot(A.T, A)
        beta = la.eigvals(hessian).max()
        step_size = 1/beta

        x = x - step_size * g
        z_new = prox(x, 0.)

        mu = (1/2)*(1 + np.sqrt(1 + 4*(mu**2)))
        gamma_t = (1 - mu) / mu+1

        x = (1- gamma_t) * z_new + gamma_t * z

        return x, z_new , mu

def ista_descent(update, A, b, reg, T=int(1e4)):
    x = np.zeros(A.shape[1])
    error = []
    l1 = []
    for t in range(T):
        x = update(x, A, b, reg)
        if (t % 1 == 0) or (t == T - 1):
            error.append(la.norm(np.dot(A, x) - b))
            l1.append(np.sum(abs(x)))

            assert not np.isnan(error[-1])

    return x, error, l1

def fista_descent(update, A, b, reg, T=int(1e4)):
    x = np.zeros(A.shape[1])
    z = x.copy()
    error = []
    l1 = []
    mu = 0
    for t in range(T):
        x,z,mu = update(x, A, b,z, reg,mu)
        if (t % 1 == 0) or (t == T - 1):
            error.append(la.norm(np.dot(A, x) - b))
            l1.append(np.sum(abs(x)))

            assert not np.isnan(error[-1])

    return x, error, l1

def subgradient_descent(update, A, b, reg, T=int(1e4)):
    x = np.zeros(A.shape[1])
    error = []
    l1 = []
    for t in range(T):

        x = update(x, A, b, t, reg)

        if (t % 1 == 0) or (t == T - 1):
            error.append(la.norm(np.dot(A, x) - b))
            l1.append(np.sum(abs(x)))

            assert not np.isnan(error[-1])

    return x, error, l1
