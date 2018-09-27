import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.stats import moment

def nmoment(x, i, n):
    return np.sum(x**i) / n

print('Write a range: ')
r = float(input())
print('Write number of Xs: ')
n = int(input())

k = range(1, 100)

u = [np.mean([pow(r - pow(nmoment(np.random.uniform(0, r, n), i, n) * (i + 1), (1 / float(i))), 2) 
    for j in range(1, 100)]) for i in k]
e = [np.mean([pow(r - pow(nmoment(np.random.exponential(r, n), i, n) / math.factorial(i), (1 / float(i))), 2) 
    for j in range(1, 100)]) for i in k]

plt.subplot(2, 1, 1)
plt.title("Exponential (up) and uniform (down) distributions")
plt.ylabel("Square of error's delta")
plt.xlabel("Kth moment")
plt.plot([i for i in range(1, 100)], e)
plt.subplot(2, 1, 2)
plt.ylabel("Square of error's delta")
plt.xlabel("Kth moment")
plt.plot([i for i in range(1, 100)], u)

plt.show()