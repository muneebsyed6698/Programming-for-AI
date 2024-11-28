import numpy as np

a = np.arange(1, 19, 2).reshape(3,3)

print(a)

for r in a:
    for e in r:
        print(e)