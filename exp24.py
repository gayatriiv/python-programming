import math
import numpy as np

# Calculate area and circumference of a circle
radius = float(input("Enter the radius of the circle: "))
area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

print("Area:", round(area, 2))
print("Circumference:", round(circumference, 2))

# Generate ten random numbers and calculate statistics
random_numbers = np.random.rand(10)
mean = np.mean(random_numbers)
median = np.median(random_numbers)
std_dev = np.std(random_numbers)

print("\nRandom Numbers:", random_numbers)
print("Mean:", round(mean, 2))
print("Median:", round(median, 2))
print("Standard Deviation:", round(std_dev, 2))
