import matplotlib.pyplot as plt

# Updated ages
ages = [19, 21, 24, 26, 28, 22, 27, 29, 33, 31, 20, 25, 30, 34, 37, 39, 32, 36, 38, 23, 19, 26]

# Updated age groups
age_groups = {"18-25": 0, "26-30": 0, "31-35": 0, "36 and above": 0}
for age in ages:
    if 18 <= age <= 25:
        age_groups["18-25"] += 1
    elif 26 <= age <= 30:
        age_groups["26-30"] += 1
    elif 31 <= age <= 35:
        age_groups["31-35"] += 1
    else:
        age_groups["36 and above"] += 1

labels = age_groups.keys()
sizes = age_groups.values()

# Plotting pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Student Age Distribution by Age Group")
plt.show()
