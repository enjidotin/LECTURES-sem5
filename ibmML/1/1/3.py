
import matplotlib.pyplot as plt
import numpy as np

list1 = np.random.rand(500)
list2 = np.random.rand(500)

list1x = np.random.normal(0, 0.01, 500)
list2y = np.random.normal(0, 0.01, 500)

plt.scatter(list1, list2)
plt.show()
plt.scatter(list1x, list2y)
plt.show()
