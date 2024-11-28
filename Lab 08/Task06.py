import numpy as np
import random

a = np.random.randint(1, 10, size = (5, 3))
b = np.random.randint(1, 10, size = (3, 2))

print(a)
print(b)

res = np.matmul(a,b)
print(res)

