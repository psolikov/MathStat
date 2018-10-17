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
    s = 0
    for j in range(1, i):
        s += nmoment(np.random.normal(0, 1, i), 2, i) ** 2
    x = 1 / (chi2.ppf((1 - gamma) / 2, i))
    y = 1 / (chi2.ppf((1 + gamma) / 2, i))
    s *= (x - y)
    first.append(abs(s))

    ###############

    s = 0
    for j in range(1, i):
        s += nmoment(np.random.normal(0, 1, i), 2, i) ** 2
    x = 1 / (norm.ppf((3 + gamma) / 4))
    y = 1 / (norm.ppf((3 - gamma) / 4))
    s *= (x * x - y * y)
    second.append(abs(s))

plt.plot([i for i in range(1, N)], first)

plt.subplot(2, 1, 1)
plt.title("Exponential (up) and uniform (down) distributions")
plt.ylabel("Square of error's delta")
plt.xlabel("Kth moment")
plt.plot([i for i in range(1, N)], first)
plt.subplot(2, 1, 2)
plt.ylabel("Square of error's delta")
plt.xlabel("Kth moment")
plt.plot([i for i in range(1, N)], second)
plt.show()