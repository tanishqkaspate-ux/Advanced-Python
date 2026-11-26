
import numpy as np

rainfall = np.array([50, 60, 80, 120, 150, 200,
                     250, 180, 140, 100, 70, 40])

total = np.sum(rainfall)

average = np.mean(rainfall)

months = np.where(rainfall > 100)[0] + 1

print("Total Annual Rainfall:", total, "mm")
print("Average Annual Rainfall:", average, "mm")

print("Months with rainfall above 100 mm:")
print(months)
