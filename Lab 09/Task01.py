import matplotlib.pyplot as plt

# Updated data
names = [
    "Ali", "Zara", "Hadi", "Ayan", "Noor",
    "Omar", "Lina", "Iza", "Sara", "Rami",
    "Mia", "Zayn", "Ira", "Kian", "Ava",
    "Yara", "Zoe", "Ray", "Liam", "Nia"
]
h = [162, 157, 168, 163, 170, 166, 159, 171, 160, 165, 164, 158, 169, 167, 161, 155, 173, 164, 162, 159]

# Using short color names
c = [
    "b", "g", "r", "c", "m", "y", "k", "w", "orange", "pink",
    "navy", "lime", "teal", "gray", "brown", "purple", "olive", "skyblue", "gold", "lightgreen"
]

# Bar chart
plt.figure(figsize=(12, 6))
plt.bar(names, h, color=c)
plt.xlabel("Students")
plt.ylabel("Height (cm)")
plt.title("Student Heights - Bar Chart")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Pie chart
plt.figure(figsize=(8, 8))
plt.pie(h, labels=names, colors=c, autopct='%1.1f%%', startangle=140)
plt.title("Student Heights - Pie Chart")
plt.show()
