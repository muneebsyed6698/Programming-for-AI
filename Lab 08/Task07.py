import numpy as np
import random

array = np.random.randint(1, 1000, size = (10, 100))

average = np.mean(array)
variance = np.var(array)
stdDev = np.std(array)

print(array)

result = f"Average: {average}\nVariance: {variance}\nStandard Deviation: {stdDev}\n"

with open('stutus.txt', 'w+') as file:
    file.write(result)

file.close()

print("Data saved")