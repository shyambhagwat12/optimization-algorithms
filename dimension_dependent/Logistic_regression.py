def fista_descent(X, Y,max_iter, eta, mu):

    Y_onehot = onehot_encoder.fit_transform(Y.reshape(-1,1))
    np.random.seed(1000)
    B = np.random.rand(X.shape[1], Y_onehot.shape[1])
    z = B.copy()
    loss_l = []
    mu = 0
    for t in range(max_iter):
        B,z,mu = fista_step(X, Y_onehot, B,eta,z, 0.01,mu)
        loss_l.append(loss(X, Y_onehot, B))
    return loss_l

def fista_step(X,Y,B,eta,z,reg,mu):
        g = gradient(X, Y, B, mu)
        B = B - eta * g
        z_new = prox(B, eta)

        mu = (1/2)*(1 + np.sqrt(1 + 4*(mu**2)))
        gamma_t = (1 - mu) / mu+1
        B = (1- gamma_t) * z_new + gamma_t * z

        return B, z_new , mu

def prox(x, s, t=1.):
    return np.sign(x)*np.maximum(np.abs(x)-s,0)

def loss(X, Y, B):
    Z = np.dot(X,B)
    N = X.shape[0]
    loss = 1/N * (np.trace(np.dot(X,B).dot(Y.T)) + np.sum(np.log(np.sum(np.exp(Z), axis=1))))
    return loss

def gradient(X, Y, B, mu):
    Z = np.dot(X,B)
    P = softmax(Z, axis=1)
    N = X.shape[0]
    gd = 1/N * (np.dot(X.T,(Y - P))) + 2 * mu * B
    return gd

def gradient_descent(X, Y, max_iter,eta,mu):

    Y_onehot = onehot_encoder.fit_transform(Y.reshape(-1,1))
    np.random.seed(1000)
    B = np.random.rand(X.shape[1], Y_onehot.shape[1])
    step = 0
    loss_l = []
 
    while step < max_iter:
        step += 1
        B -= eta * gradient(X, Y_onehot, B, mu)
        loss_l.append(loss(X, Y_onehot, B))
    return loss_l