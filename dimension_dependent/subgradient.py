def subgradient(x, A, b, t, lam, c=1e-3):
    g = np.dot(np.dot(A.T, A), x) - np.dot(A.T, b) + np.sign(x) * lam
    if( t ==0):
        t=1
    eta = c / (t)
    x -= eta * g
    return x
    
def loss(A,b,lam, x):
    return 0.5 * np.sum(np.square(np.dot(A, x) - b)) + lam * np.sum(np.abs(x))


def descent(update, A, b, reg, T=int(1e4)):
    x = np.zeros(A.shape[1])
    error = []
    l1 = []
    for t in range(T):
        # update A (here subgradient, but you can re-use when we develop other algorithms)
        x = update(x, A, b, t, reg)

        # record error and l1 norm
        if (t % 1 == 0) or (t == T - 1):
            error.append(la.norm(np.dot(A, x) - b))
            l1.append(np.sum(abs(x)))

            assert not np.isnan(error[-1])

    return x, error, l1