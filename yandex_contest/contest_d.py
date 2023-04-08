import numpy as np
from scipy.optimize import minimize, Bounds


def mse(p, t, w):
    return np.sum(w * (t - p) ** 2) / np.sum(w)


def msle(p, t, w):
    return np.sum(w * (np.log(1.0 + t) - np.log(1 + p)) ** 2) / np.sum(w)


def log_loss(p, t, w):
    # p = np.clip(p, 0.05, 0.95)
    log1 = t * np.log(p)
    log2 = (1.0 - t) * np.log(1 - p)
    return -np.sum(w * (log1 + log2)) / np.sum(w)


data = [
    [5.66192, 6.322711, 121.257938],
    [3.049585, 5.285749, 46.892782],
    [0.227632, 4.771393, 9.516171],
    [145.759519, 5.320249, 28.646039],
    [22.774692, 13.604903, 36.033962]
]
data = np.array(data)
# # 0.14568 0.138623 0.14568
# # n = int(input().split()[0])
# # data = np.array([list(map(float, input().split())) for _ in range(n)])
# a = data[:, -2]
# b = data[:, -1]
# t = a / b
# w = b
# e = 1e-8
# # c = 1000

# lim = [0.25, 0.30, 0.75, 0.8]

# # bounds = Bounds([lim[0], lim[1]],  # [min x0, min x1]
# #                 [lim[2], lim[3]])  # [max x0, max x1]

# # result = minimize(
# #     f, x_start, method='trust-constr', jac=df, bounds=bounds)

# # p_optim = np.random.rand(3)
# p_optim = np.array([0.5, 0.5, 0.5])

# res1 = minimize(mse, p_optim[0], args=(t, w))
# res2 = minimize(msle, p_optim[1], args=(t, w))
# res3 = minimize(log_loss, p_optim[2], args=(t, w), bounds=Bounds([e],[1.0 - e]))
# # res3 = basinhopping(log_loss, p_optim[2], minimizer_kwargs={'args': (t, w)})

# print(np.round(res1.x, 6)[0], np.round(res2.x, 6)[0], np.round(res3.x, 6)[0])
# n = int(input().split()[0])
# data = np.array([list(map(float, input().split())) for _ in range(n)])
a = data[:, -2]
b = data[:, -1]
t = a / b
w = b
e = 1e-8
# c = 1000

# p_optim = np.random.rand(3)
p_optim = np.array([0.5, 0.5, 0.5])
res1 = minimize(mse, p_optim[0], args=(t, w))
res2 = minimize(msle, p_optim[1], args=(t, w))
# res3 = minimize(log_loss, p_optim[2], args=(t, w))
res3 = minimize(log_loss, p_optim[2], args=(t, w), bounds=Bounds([e],[1.0 - e]))

print(np.round(res1.x, 6)[0], np.round(res2.x, 6)[0], np.round(res3.x, 6)[0])
