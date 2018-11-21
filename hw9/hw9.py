import numpy as np
from scipy.stats import chi2

num = 3.9 * 10 ** 5
k = chi2.ppf(0.95, 4)
y2018 = np.array([3.85, 31.13, 32.96, 29.92, 2.13]) / 100
y2017 = np.array([7.92, 36.16, 25.09, 27.49, 3.34]) /100
sum = ((y2018 - (y2018+y2017)/2)**2 + (y2017 - (y2018+y2017)/2)**2) / ((y2018 + y2017) / 2)
ans = np.sum(sum*num)
print(ans <= k)
print("Квантиль - " + str(k) + ", итог - " + str(ans))