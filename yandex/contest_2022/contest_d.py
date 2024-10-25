import torch
from torch.optim import SGD

x = [
    [5.66192],
    [3.049585],
    [0.227632],
    [145.759519],
    [22.774692]
]

a = [
    6.322711,
    5.285749,
    4.771393,
    5.320249,
    13.604903
]

b = [
    121.257938,
    46.892782,
    9.516171,
    28.646039,
    36.033962
]

correct = [0.14568, 0.138623, 0.14568]


x = torch.tensor(x, dtype=torch.float64)
a = torch.tensor(a, dtype=torch.float64)
b = torch.tensor(b, dtype=torch.float64)


def MSE(a, b, p):
    t = a / b
    mse = torch.sum(b * torch.square(t - p), dim=0) / torch.sum(b, dim=0)
    return mse


def MSLE(a, b, p):
    t = a / b
    msle = torch.sum(b * torch.square(torch.log(1 + t) - torch.log(1 + p)), dim=0) / torch.sum(b, dim=0)
    return msle


def LogLoss(a, b, p, c=1e1):
    t = a / b
    log_loss = -(torch.sum(b * (t / c * torch.log(p / c) + (1 - t / c) * torch.log(1 - p / c)), dim=0) /
                 torch.sum(b, dim=0))
    return log_loss


p = torch.rand(1, requires_grad=True, dtype=torch.float64)
optimizer = SGD({p}, lr=0.001)
for e in range(10000):
    loss = MSE(a, b, p)
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
print(round(p.item(), 6))

p = torch.rand(1, requires_grad=True, dtype=torch.float64)
optimizer = SGD({p}, lr=0.001)
for e in range(10000):
    loss = MSLE(a, b, p)
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
print(round(p.item(), 6))

p = torch.rand(1, requires_grad=True, dtype=torch.float64)
optimizer = SGD({p}, lr=0.001)
for e in range(100000):
    loss = LogLoss(a, b, p)
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()
print(round(p.item(), 6))
