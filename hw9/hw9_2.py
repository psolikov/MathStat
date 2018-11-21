import numpy as np
import sys
from scipy.stats import chi2

num = 2020
rasp = np.array([527, 1017, 476]) / num
k = chi2.ppf(0.95, 2)
r = sys.maxsize
for p in np.array(range(1, 1000)) / 1000:
    prob = np.array([p ** 2, p * (1 - p) * 2, (1 - p) ** 2])
    ans = np.sum((rasp - prob) ** 2 / prob * num)
    r = min(r, ans)
print(r <= k)