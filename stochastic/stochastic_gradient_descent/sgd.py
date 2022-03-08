def sgd(X, Y, epochs,eta,mu):
    n = X.shape[0]
    dx = X.shape[1]
    Y_onehot = onehot_encoder.fit_transform(Y.reshape(-1,1))
    np.random.seed(1000)
    B = np.random.rand(X.shape[1], Y_onehot.shape[1])
    loss_l = []
    total_steps = 0
    step = 0
    t = 0
    while step < epochs:
        step += 1
        while t < n:
            t += 1
            it = np.random.choice(n)
            x_temp = X.iloc[it].values
            x = x_temp.reshape((1,dx))
            yt = Y_onehot[it,:]            
            y = yt.reshape((1,10))
            B -= eta * gradient(x, y, B, mu)
            total_steps = total_steps + 1 
        loss_l.append(loss(X, Y_onehot, B))           
    return total_steps,loss_l
