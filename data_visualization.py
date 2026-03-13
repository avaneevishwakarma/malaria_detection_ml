import matplotlib.pyplot as plt
import numpy as np

labels = ["Infected","Uninfected"]
values = [13779,13779]

plt.bar(labels,values)
plt.title("Malaria Dataset Distribution")
plt.xlabel("Cell Type")
plt.ylabel("Number of Images")
plt.show()
