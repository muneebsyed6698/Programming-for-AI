import matplotlib.pyplot as plt

# Updated data
cities = ["Springfield", "Riverdale", "Brookhaven", "Mapleton", "Lakeside", 
          "Fairview", "Hillcrest", "Oakridge", "Cedarville", "Pinehurst"]
populations = [542000, 678000, 825000, 910000, 460000, 
               580000, 620000, 710000, 495000, 380000]

# Horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(cities, populations, color='skyblue')
plt.xlabel("Population")
plt.ylabel("Cities")
plt.title("Population of Cities")

plt.show()
