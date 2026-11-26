
import numpy as np
import matplotlib.pyplot as plt

downtime = np.array([30, 45, 70, 25, 90, 55, 40])

average = np.mean(downtime)

print("Average Downtime:", average, "minutes")

critical = downtime[downtime > 60]

print("Critical Downtime:", critical)

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

plt.plot(days, downtime, marker='o')

plt.title("Weekly Machine Downtime")
plt.xlabel("Days")
plt.ylabel("Downtime (Minutes)")

plt.grid()
plt.show()
