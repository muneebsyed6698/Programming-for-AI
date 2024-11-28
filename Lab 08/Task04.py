import numpy as np

dtype = [('name', 'U10'), ('height', 'f4'), ('class', 'i4')]

students = np.array([
    ('Alice', 5.7, 8),
    ('Bob', 6.1, 10),
    ('Charlie', 5.8, 9),
    ('David', 6.0, 10),
    ('Eva', 5.4, 8)
], dtype=dtype)

sorted_students = np.sort(students, order = ['class', 'height'])

print(students)
print(sorted_students)