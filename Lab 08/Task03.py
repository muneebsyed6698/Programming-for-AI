import numpy as np

m = np.arange(2, 19, 2).reshape(3, 3)
print(m)

m = m * 4
print(m)

i = np.eye(3, 3)
print(i)

m = m * i
print(m)
