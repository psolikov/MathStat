import numpy as np
import math
from scipy.stats import norm, chi2
import matplotlib.pyplot as plt
from scipy.stats import moment

N = 100
gamma = 0.7

first = []
second = []

def nmoment(x, i, n):
    return np.sum(x**i) / n

for i in range(1, N):
    s = []
    for j in range(0, 20):
        x = 1 / (chi2.ppf((1 - gamma) / 2, i))
        y = 1 / (chi2.ppf((1 + gamma) / 2, i))
        s.append(abs(nmoment(np.random.normal(0, 1, i), 2, 1) * (x - y)))
    first.append(np.mean(s))

    ###############

    s = []
    for j in range(0, 20):
        x = (norm.ppf((3 + gamma) / 4))
        y = (norm.ppf((3 - gamma) / 4))
        nprn = np.random.normal(0, 1, i)
        s.append(abs(nmoment(nprn * nprn, 1, 1) * (1/(x * x * i) - 1/(y * y * i))))
    second.append(np.mean(s))

plt.plot([i for i in range(1, N)], first)

plt.subplot(2, 1, 1)

plt.plot([i for i in range(1, N)], first)
plt.subplot(2, 1, 2)
plt.plot([i for i in range(1, N)], second)
plt.show()